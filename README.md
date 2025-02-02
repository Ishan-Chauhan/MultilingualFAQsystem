# FAQ Management System using Django

Welcome to the FAQ Management System built with Django! This project provides an API-driven solution for managing frequently asked questions (FAQs) with multilingual support.

## Features
- CRUD operations for FAQs (Create, Read, Update, Delete)
- Automatic translation of questions and answers using Google Translate API
- Caching for improved performance
- WYSIWYG editor support for rich-text answers using `django-ckeditor`
- Admin panel for managing FAQs

## Installation

### Prerequisites
Ensure you have Python and virtualenv installed.

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### Setup Database
Apply migrations to set up the database.

```sh
python manage.py migrate
python manage.py createsuperuser  # Create an admin user
```

### Run Server
Start the Django development server.

```sh
python manage.py runserver
```

## API Endpoints

### Fetch All FAQs
```sh
GET /api/faqs/
```

### Fetch a Specific FAQ by ID
```sh
GET /api/faqs/<id>/
```

### Create a New FAQ
```sh
POST /api/faqs/add/
Content-Type: application/json
{
    "question": "What is Django?",
    "answer": "Django is a high-level Python web framework."
}
```

### Update an Existing FAQ
```sh
PUT /api/faqs/<id>/update/
Content-Type: application/json
{
    "question": "Updated question?",
    "answer": "Updated answer."
}
```

### Delete an FAQ
```sh
DELETE /api/faqs/<id>/delete/
```

## Admin Panel
To manage FAQs via the Django Admin interface:

```sh
http://127.0.0.1:8000/admin/
```
Login using the superuser credentials created earlier.

