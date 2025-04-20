# Task Management API

A Django REST Framework API for task management that allows users to create tasks, assign tasks to users, and retrieve tasks assigned to specific users.

## Setup Instructions

### Prerequisites

- Python 3.8+
- pip
- virtualenv (optional but recommended)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/SarvT/josh_talks.git
cd josh_talks
```

2. Set up a virtual environment (optional):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

The API will be available at http://127.0.0.1:8000/

## Authentication

This API uses token-based authentication with Bearer tokens.

### Registering a User

**URL:** `/api/auth/register/`  
**Method:** `POST`  
**Auth required:** No  

**Request Body:**
```json
{
    "username": "newuser",
    "email": "newuser@example.com",
    "password": "securepassword",
    "first_name": "New",
    "last_name": "User",
    "mobile": "1234567890"
}
```

**Success Response:**
- **Code:** 201 Created
- **Content:**
```json
{
    "token": "a96646e293cf3071fd64718cb0d7e75acd",
    "user_id": 1,
    "email": "newuser@example.com"
}
```

### Login

**URL:** `/api/auth/login/`  
**Method:** `POST`  
**Auth required:** No  

**Request Body:**
```json
{
    "username": "existinguser",
    "password": "userpassword"
}
```

**Success Response:**
- **Code:** 200 OK
- **Content:**
```json
{
    "token": "a96646e293cf3071fd64718cb0d7e75acd",
    "user_id": 1,
    "email": "existinguser@example.com"
}
```

### Using the Token

For all protected endpoints, include the token in the Authorization header:

```
Authorization: Bearer a96646e293cf3071fd64718cb0d7e75acd
```

## API Endpoints

### Create a Task

**URL:** `/api/tasks/`  
**Method:** `POST`  
**Auth required:** Yes (Bearer Token)  

**Request Headers:**
```
Authorization: Bearer a96646e293cf3071fd64718cb0d7e75acd
```

**Request Body:**
```json
{
    "name": "Implement Login Feature",
    "description": "Create a login page with email and password fields",
    "task_type": "FEATURE",
    "status": "PENDING"
}
```

**Success Response:**
- **Code:** 201 Created
- **Content:**
```json
{
    "id": 1,
    "name": "Implement Login Feature",
    "description": "Create a login page with email and password fields",
    "created_at": "2025-04-14T10:30:00Z",
    "task_type": "FEATURE",
    "completed_at": null,
    "status": "PENDING",
    "assigned_users": []
}
```

### Assign a Task to Users

**URL:** `/api/tasks/assign/`  
**Method:** `POST`  
**Auth required:** Yes (Bearer Token)  

**Request Headers:**
```
Authorization: Bearer a96646e293cf3071fd64718cb0d7e75acd
```

**Request Body:**
```json
{
    "task_id": 1,
    "user_ids": [1, 2]
}
```

**Success Response:**
- **Code:** 200 OK
- **Content:**
```json
{
    "id": 1,
    "name": "Implement Login Feature",
    "description": "Create a login page with email and password fields",
    "created_at": "2025-04-14T10:30:00Z",
    "task_type": "FEATURE",
    "completed_at": null,
    "status": "PENDING",
    "assigned_users": [
        {
            "id": 1,
            "username": "user1",
            "email": "user1@example.com",
            "first_name": "John",
            "last_name": "Doe",
            "mobile": "1234567890"
        },
        {
            "id": 2,
            "username": "user2",
            "email": "user2@example.com",
            "first_name": "Jane",
            "last_name": "Smith",
            "mobile": "9876543210"
        }
    ]
}
```

### Get Tasks for a User

**URL:** `/api/users/{user_id}/tasks/`  
**Method:** `GET`  
**Auth required:** Yes (Bearer Token)  

**Request Headers:**
```
Authorization: Bearer a96646e293cf3071fd64718cb0d7e75acd
```

**Success Response:**
- **Code:** 200 OK
- **Content:**
```json
[
    {
        "id": 1,
        "name": "Implement Login Feature",
        "description": "Create a login page with email and password fields",
        "created_at": "2025-04-14T10:30:00Z",
        "task_type": "FEATURE",
        "completed_at": null,
        "status": "PENDING",
        "assigned_users": [
            {
                "id": 1,
                "username": "user1",
                "email": "user1@example.com",
                "first_name": "John",
                "last_name": "Doe",
                "mobile": "1234567890"
            },
            {
                "id": 2,
                "username": "user2",
                "email": "user2@example.com",
                "first_name": "Jane",
                "last_name": "Smith",
                "mobile": "9876543210"
            }
        ]
    }
]
```

## Troubleshooting Authentication Issues

If you encounter authentication problems, check the following:

1. **Token Format**: Make sure you're using the correct format in the Authorization header:
   - Correct: `Authorization: Bearer a96646e293cf3071fd64718cb0d7e75acd`
   - Incorrect: `Authorization: Token a96646e293cf3071fd64718cb0d7e75acd`
   - Incorrect: `Bearer a96646e293cf3071fd64718cb0d7e75acd` (missing Authorization prefix)

2. **Token Validity**: Ensure your token is valid and not expired.

3. **Request Headers**: Some HTTP clients automatically drop headers if they don't conform to expected formats.

4. **Server Configuration**: Check if the server has properly configured the BearerTokenAuthentication class.

## Testing

Run the tests using:

```bash
python manage.py test
```

## Project Structure

- `task_management/models.py`: Contains the User and Task models
- `task_management/serializers.py`: Contains serializers for the models
- `task_management/views.py`: Contains the API views
- `task_management/urls.py`: Contains URL patterns for the API
- `task_management/auth_views.py`: Contains authentication-related views
- `task_management/authentication.py`: Contains custom authentication classes
- `task_management/tests.py`: Contains tests for the API

## Dependencies

- Django 4.2+
- Django REST Framework 3.14+
- djangorestframework-authtoken

## License

[MIT License](LICENSE)