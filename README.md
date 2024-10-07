## Introduction

- This is an Online Store REST APIs based application build with Python, Django and Django Rest Framework and sqlite as Database.

## Features

- Users can be created by a `superuser/admin` user.
- User can create new `Category`.
- User can add `Product` under a `Category`.
- User can place `Order`.

## Requirements

- Python (>= 3.12)
- Django (>= 5.x)

## Getting Started

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/madhavsh96/SAS_group_online_store.git
    cd your-project
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```


3. Apply database migrations:

    ```bash
    python manage.py makemigrations

    python manage.py migrate
    ```

4. Create super user (which will act as admin):

    ```bash
    python manage.py createsuperuser
    ```
    Enter email and password

### Development

- Run the development server:

    ```bash
    python manage.py runserver
    ```

- Access the Django admin interface at `http://127.0.0.1:8000/admin/` (default credentials may apply).
- Access the API endpoints at `http://127.0.0.1:8000/api/`.
