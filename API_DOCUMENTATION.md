"""
API Endpoints Documentation

This document describes the available API endpoints for the Django Campus Workshop system.

## Workshop Endpoints

### 1. List all workshops
- **URL**: `/api/workshops/`
- **Method**: `GET`
- **Description**: Retrieve a list of all available workshops with registration counts
- **Response**: List of workshops with basic information

### 2. Get workshop details
- **URL**: `/api/workshops/<id>/`
- **Method**: `GET`
- **Description**: Retrieve detailed information about a specific workshop
- **Parameters**: 
  - `id`: Workshop ID (integer)

### 3. Create a new workshop
- **URL**: `/api/workshops/create/`
- **Method**: `POST`
- **Description**: Create a new workshop
- **Required fields**:
  - `workshop_name`: String
  - `workshop_date`: Date (YYYY-MM-DD)
  - `workshop_location`: String
  - `workshop_description`: String (optional)

## Registration Endpoints

### 4. Register for a workshop
- **URL**: `/api/registrations/create/`
- **Method**: `POST`
- **Description**: Register a user for a workshop
- **Required fields**:
  - `workshop`: Workshop ID (integer)
  - `user_name`: String
  - `user_email`: Email
  - `will_attend_physical`: Boolean (default: true)
  - `django_experience`: String (choices: "Beginner", "Intermediate", "Advanced")

### 5. List all registrations
- **URL**: `/api/registrations/`
- **Method**: `GET`
- **Description**: Retrieve all workshop registrations

### 6. Get registration details
- **URL**: `/api/registrations/<id>/`
- **Method**: `GET`
- **Description**: Retrieve details of a specific registration
- **Parameters**:
  - `id`: Registration ID (integer)

### 7. Get registrations for a specific workshop
- **URL**: `/api/workshops/<workshop_id>/registrations/`
- **Method**: `GET`
- **Description**: Retrieve all registrations for a specific workshop
- **Parameters**:
  - `workshop_id`: Workshop ID (integer)

## Example API Usage

### Register for a workshop (POST request):
```json
{
    "workshop": 1,
    "user_name": "John Doe",
    "user_email": "john.doe@example.com",
    "will_attend_physical": true,
    "django_experience": "Beginner"
}
```

### Create a workshop (POST request):
```json
{
    "workshop_name": "Django Fundamentals",
    "workshop_date": "2025-09-15",
    "workshop_location": "Tech Hub Building, Room 101",
    "workshop_description": "Learn the basics of Django web framework"
}
```

## Error Handling

The API returns appropriate HTTP status codes:
- `200 OK`: Successful GET requests
- `201 Created`: Successful POST requests
- `400 Bad Request`: Invalid data or duplicate registration
- `404 Not Found`: Resource not found

## Features

- **Duplicate Registration Prevention**: Users cannot register for the same workshop twice
- **Input Validation**: Email and name fields are validated
- **Automatic Registration Count**: Workshops show the number of registered users
- **Detailed Registration Info**: Registrations include workshop information
