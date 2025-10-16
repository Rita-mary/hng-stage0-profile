#  HNG Stage 0 — Dynamic Profile Endpoint

A simple REST API built with **Django** and **Django REST Framework** that returns my profile information along with a **random cat fact** from the public [Cat Facts API](https://catfact.ninja/fact).

---

## Project Overview

This project was created as part of the **HNG Internship (Stage 0 — Backend)**.  
It demonstrates how to:
- Build an API endpoint using Django REST Framework  
- Consume data from an external API  
- Return dynamic JSON responses  
- Handle third-party API errors gracefully  

---

## Endpoint

### `GET /me`

#### Example Response
```json
{
  "status": "success",
  "user": {
    "email": "amakomritamary322@gmail.com",
    "name": "Rita-mary Ngozi Amakom",
    "stack": "Python/Django/Django REST Framework"
  },
  "timestamp": "2025-10-16T14:00:00.000Z",
  "fact": "Cats sleep for 70% of their lives."
}
```

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Rita-Mary/hng-stage0-profile.git
cd hng-stage0-profile
```

### 2. Install Dependencies
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Run Migrations
```bash
python manage.py migrate
```

### 4. Start the Server
```bash
python manage.py runserver
```

---

## Running Tests

```bash
python manage.py test
```

---

## Environment Variables

Create a `.env` file in the project root and add:
```
SECRET_KEY=your_secret_key
DEBUG=True