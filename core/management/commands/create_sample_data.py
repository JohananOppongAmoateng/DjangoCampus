from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from core.models import WorkShop, WorkshopRegistration


class Command(BaseCommand):
    help = 'Create sample workshops and registrations for testing the API'

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS('Creating sample workshops...')
        )

        # Create sample workshops
        workshops_data = [
            {
                'workshop_name': 'Django Fundamentals',
                'workshop_date': timezone.now().date() + timedelta(days=30),
                'workshop_location': 'Tech Hub Building, Room 101',
                'workshop_description': (
                    'Learn the basics of Django web framework. '
                    'Perfect for beginners who want to start building '
                    'web apps.'
                )
            },
            {
                'workshop_name': 'Advanced Django Patterns',
                'workshop_date': timezone.now().date() + timedelta(days=45),
                'workshop_location': 'Innovation Center, Auditorium A',
                'workshop_description': (
                    'Deep dive into advanced Django concepts including '
                    'custom managers, signals, and design patterns.'
                )
            },
            {
                'workshop_name': 'Django REST API Development',
                'workshop_date': timezone.now().date() + timedelta(days=60),
                'workshop_location': 'Online Session',
                'workshop_description': (
                    'Build robust REST APIs using Django REST Framework. '
                    'Covers serializers, viewsets, and authentication.'
                )
            }
        ]

        workshops = []
        for workshop_data in workshops_data:
            workshop, created = WorkShop.objects.get_or_create(
                workshop_name=workshop_data['workshop_name'],
                defaults=workshop_data
            )
            workshops.append(workshop)
            if created:
                self.stdout.write(
                    f'Created workshop: {workshop.workshop_name}'
                )
            else:
                self.stdout.write(
                    f'Workshop already exists: {workshop.workshop_name}'
                )

        # Create sample registrations
        registrations_data = [
            {
                'workshop': workshops[0],  # Django Fundamentals
                'user_name': 'Alice Johnson',
                'user_email': 'alice.johnson@example.com',
                'will_attend_physical': True,
                'django_experience': 'Beginner'
            },
            {
                'workshop': workshops[0],  # Django Fundamentals
                'user_name': 'Bob Smith',
                'user_email': 'bob.smith@example.com',
                'will_attend_physical': True,
                'django_experience': 'Beginner'
            },
            {
                'workshop': workshops[1],  # Advanced Django Patterns
                'user_name': 'Charlie Brown',
                'user_email': 'charlie.brown@example.com',
                'will_attend_physical': False,
                'django_experience': 'Intermediate'
            },
            {
                'workshop': workshops[2],  # Django REST API Development
                'user_name': 'Diana Prince',
                'user_email': 'diana.prince@example.com',
                'will_attend_physical': True,
                'django_experience': 'Advanced'
            }
        ]

        for reg_data in registrations_data:
            registration, created = WorkshopRegistration.objects.get_or_create(
                workshop=reg_data['workshop'],
                user_email=reg_data['user_email'],
                defaults=reg_data
            )
            if created:
                self.stdout.write(
                    f'Created registration: {registration.user_name} -> '
                    f'{registration.workshop.workshop_name}'
                )
            else:
                self.stdout.write(
                    f'Registration already exists: {registration.user_name} '
                    f'-> {registration.workshop.workshop_name}'
                )

        self.stdout.write(
            self.style.SUCCESS(
                f'\nSample data creation completed!'
                f'\nWorkshops created: {len(workshops)}'
                f'\nRegistrations created: {len(registrations_data)}'
            )
        )

        self.stdout.write(
            self.style.HTTP_INFO(
                '\nYou can now test the API endpoints:'
                '\n- GET /api/workshops/ - List all workshops'
                '\n- POST /api/registrations/create/ - Register for a workshop'
                '\n- GET /api/registrations/ - List all registrations'
            )
        )
