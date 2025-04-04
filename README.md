# 🎬 Movie Watchlist - Django Backend API

This is a simple Django-based backend API for managing a Movie Watchlist. It supports full CRUD operations (Create, Read, Update, Delete) using Django REST Framework.

---

## 🚀 Features

- Add new movies to your watchlist
- View the list of movies
- Update movie details
- Delete movies from the list
- Use Django REST Framework's browsable API or Postman

---

## 🧰 Tech Stack

- Python 3.8+
- Django
- Django REST Framework

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/movie-watchlist.git
cd movie-watchlist
```

### 2. Create and activate virtual environment

```bash
python -m venv env
source env/bin/activate  # On Windows: .\env\Scripts\activate
```

### 3. Install dependencies
```bash
pip install django djangorestframework
```

### 4. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser (to access the admin panel)

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

## 🔗 API Endpoints

| Method | Endpoint | Description |
| :---:  |   :---:  |     :---:   |
| GET    | /api/movies/     | List all movies    |
| GET    | /api/movies/<id>/ | Retrieve a single movie |
| POST   | /api/movies/     | Add a new movie     |
| PUT    |   /api/movies/<id>/     |  Update a movie     |
| DELETE | /api/movies/<id>/   | Delete a movie |

## 📁 Project Structure

```bash
movie-watchlist/
├── backend/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── movies/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── manage.py
└── README.md
```

## 🧑‍💻 Author
Built with ❤️ by Poshika mangai M
