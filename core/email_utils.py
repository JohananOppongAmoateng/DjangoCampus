from ics import Calendar, Event
from datetime import datetime, timedelta
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from urllib.parse import urlencode


def send_workshop_registration_email(registration):
    """
    Send workshop registration confirmation email with calendar invite
    """
    workshop = registration.workshop
    
    # Create calendar event
    c = Calendar()
    e = Event()
    e.name = workshop.workshop_name
    
    # Combine date and time
    if workshop.workshop_time:
        start_datetime = datetime.combine(
            workshop.workshop_date,
            workshop.workshop_time
        )
    else:
        start_datetime = datetime.combine(
            workshop.workshop_date,
            datetime.min.time().replace(hour=9)
        )
    
    # Set event duration (default 2 hours)
    end_datetime = start_datetime + timedelta(hours=2)
    
    e.begin = start_datetime
    e.end = end_datetime
    e.location = workshop.workshop_location
    
    # Create description
    attendance_type = (
        "Physical" if registration.will_attend_physical else "Virtual"
    )
    e.description = (
        f"Workshop: {workshop.workshop_name}\n"
        f"Location: {workshop.workshop_location}\n"
        f"Attendance: {attendance_type}\n\n"
        f"{workshop.workshop_description or ''}\n\n"
        f"Organized by Django Campus\n"
        f"We look forward to seeing you!"
    )
    
    c.events.add(e)
    ics_content = str(c)
    
    # Prepare email context
    context = {
        'name': registration.user_name,
        'workshop': workshop,
        'registration': registration,
        'add_to_google_calendar_url': generate_google_calendar_link(
            workshop, registration
        )
    }
    
    # Render email templates
    try:
        html_message = render_to_string(
            'emails/workshop_registration.html',
            context
        )
    except Exception:
        html_message = None
    
    try:
        text_message = render_to_string(
            'emails/workshop_registration.txt',
            context
        )
    except Exception:
        # Fallback text message
        text_message = f"""
Registration Confirmed!

Hi {registration.user_name},

Thank you for registering for our workshop!

Workshop: {workshop.workshop_name}
Date: {workshop.workshop_date}
Location: {workshop.workshop_location}

Add to Google Calendar: {context['add_to_google_calendar_url']}

Best regards,
Django Campus Team
        """
    
    # Create email
    from_email = getattr(
        settings,
        'DEFAULT_FROM_EMAIL',
        'noreply@djangocampus.com'
    )
    
    email = EmailMessage(
        subject=f"Registration Confirmed: {workshop.workshop_name}",
        body=text_message,
        from_email=from_email,
        to=[registration.user_email],
    )
    
    # Add HTML version if available
    if html_message:
        email.content_subtype = "html"
        email.body = html_message
    
    # Attach calendar invite
    email.attach(
        filename="workshop_invite.ics",
        content=ics_content,
        mimetype="text/calendar"
    )
    
    # Send email
    try:
        email.send()
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False


def generate_google_calendar_link(workshop, registration):
    """
    Generate Google Calendar "Add to Calendar" link
    """
    if workshop.workshop_time:
        start_datetime = datetime.combine(
            workshop.workshop_date,
            workshop.workshop_time
        )
    else:
        start_datetime = datetime.combine(
            workshop.workshop_date,
            datetime.min.time().replace(hour=9)
        )
    
    end_datetime = start_datetime + timedelta(hours=2)
    
    # Format dates for Google Calendar
    start_str = start_datetime.strftime('%Y%m%dT%H%M%S')
    end_str = end_datetime.strftime('%Y%m%dT%H%M%S')
    
    attendance_type = (
        "Physical" if registration.will_attend_physical else "Virtual"
    )
    
    params = {
        'action': 'TEMPLATE',
        'text': workshop.workshop_name,
        'dates': f"{start_str}/{end_str}",
        'details': (
            f"Workshop: {workshop.workshop_name}\n"
            f"Attendance: {attendance_type}\n"
            f"Experience Level: {registration.django_experience}\n\n"
            f"{workshop.workshop_description or ''}\n\n"
            f"Organized by Django Campus"
        ),
        'location': workshop.workshop_location,
    }
    
    base_url = "https://calendar.google.com/calendar/render"
    return f"{base_url}?{urlencode(params)}"


def send_workshop_notification_email(workshop, previous_registrations):
    """
    Send notification email to previous attendees about a new workshop
    """
    from_email = getattr(
        settings,
        'DEFAULT_FROM_EMAIL',
        'noreply@djangocampus.com'
    )
    for registration in previous_registrations:
        context = {
            'name': registration.user_name,
            'workshop': workshop,
        }
        
        try:
            html_message = render_to_string(
                'emails/workshop_notification.html',
                context
            )
        except Exception:
            html_message = None
        
        try:
            text_message = render_to_string(
                'emails/workshop_notification.txt',
                context
            )
        except Exception:
            text_message = f"""
                    New Workshop Announcement!
                    Hi {registration.user_name},
                    We are excited to announce a new workshop: {workshop.workshop_name} on {workshop.workshop_date} at {workshop.workshop_location}.
                    Join us for another great learning experience!
                    Best regards,
                    Django Campus Team
                                """
                    
        email = EmailMessage(
            subject=f"New Workshop: {workshop.workshop_name}",
            body=text_message,
            from_email=from_email,
            to=[registration.user_email],
        )
        
        if html_message:
            email.content_subtype = "html"
            email.body = html_message
        
        try:
            email.send()
        except Exception as e:
            print(f"Error sending notification email to {registration.user_email}: {e}")

        
        