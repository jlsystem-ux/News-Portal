# News Django Project

This is a Django-based web application for managing and displaying news articles.

## Features
- Article listing and detail views
- Article model with title, slug, author, content, publish date, status, and timestamps
- Admin interface for managing articles
- Template-based rendering for article list and detail pages

### Visuals

#### Home Page
![Home Page](screenshots/home.png)

#### Article List
![Article List](screenshots/article_list.png)

#### Django Admin
![Django Admin](screenshots/admin.png)

#### Add Article (Admin)
![Add Article](screenshots/add_article.png)

## Project Structure
```
news/
├── articles/
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── templates/
│   │   └── articles/
│   │       ├── article_detail.html
│   │       └── article_list.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── news/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```

## Setup Instructions
1. **Clone the repository:**
   ```sh
   git clone <your-repo-url>
   cd news
   ```
2. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # or
   source venv/bin/activate  # On macOS/Linux
   ```
3. **Install dependencies:**
   ```sh
   pip install django
   ```
4. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```
5. **Create a superuser (optional, for admin):**
   ```sh
   python manage.py createsuperuser
   ```
6. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

## Usage
- Visit `http://127.0.0.1:8000/articles/` to see the list of articles.
- Visit `http://127.0.0.1:8000/admin/` to manage articles in the Django admin.

## Adding Articles
- Use the Django admin interface to add, edit, or delete articles.

## Database
This project uses **PostgreSQL** as the database backend. Make sure you have PostgreSQL installed and running on your system.

### PostgreSQL Setup
1. Install PostgreSQL from [https://www.postgresql.org/download/](https://www.postgresql.org/download/)
2. Create a database and user for your Django project. Example:
   ```sh
   psql -U postgres
   CREATE DATABASE news_db;
   CREATE USER news_user WITH PASSWORD 'yourpassword';
   GRANT ALL PRIVILEGES ON DATABASE news_db TO news_user;
   ```
3. Update your `news/settings.py` `DATABASES` section:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'news_db',
           'USER': 'news_user',
           'PASSWORD': 'yourpassword',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```
4. Install the PostgreSQL driver:
   ```sh
   pip install psycopg2-binary
   ```
5. Run migrations:
   ```sh
   python manage.py migrate
   ```

## Home Page
A visually appealing home page can make your project stand out. You can create a `home.html` template and update your `urls.py` to display a welcome message, project description, and navigation links.

### Example Home Page Template
```html
<!-- templates/home.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>News Portal Home</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1 class="display-4">Welcome to the News Portal</h1>
        <p class="lead">A Django project for managing and displaying news articles.</p>
        <a href="/articles/" class="btn btn-primary">View Articles</a>
        <a href="/admin/" class="btn btn-secondary">Admin</a>
    </div>
</body>
</html>
```

### How to Add a Home Page
1. Create a `templates` folder in your project root (if it doesn't exist).
2. Add the above `home.html` file to `templates/`.
3. Update your `news/urls.py` to include a view for the home page.

This will give your project a professional first impression during your presentation.

## Custom Management Commands
Currently, there are no custom management commands or scripts in this project. If you add any, document them here with usage instructions.

## License
This project is for educational purposes.
