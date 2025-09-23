# 🥘 Django Recipe Sharing App

A beginner-friendly Django web app where users can share, browse, and manage recipes.Supports user authentication, recipe creation, editing, deletion, and search by ingredients or title.

------------------------------------------------------------------------

## 🚀 Features

-   User authentication (Sign up, Login, Logout)
-   Add, edit, and delete your own recipes
-   Search recipes by title or ingredients
-   Tailwind CSS for modern responsive design

------------------------------------------------------------------------

## 🛠️ Installation & Setup

### 1. Clone the repository

``` bash
git clone https://github.com/OmAr1dev/django-recipe-app.git
cd django-recipe-app
```

### 2. Create a virtual environment

``` bash
python -m venv .venv
# On macOS/Linux
source .venv/bin/activate
# On Windows
.venv\Scripts\activate
```

### 3. Install dependencies

``` bash
pip install -r requirements.txt
```

### 4. Apply migrations

``` bash
python manage.py migrate
```

### 5. Run the server

``` bash
python manage.py runserver
```

Now open your browser at `http://127.0.0.1:8000/` 🎉

------------------------------------------------------------------------

## ⚙️ Project Structure

    django-recipe-app/
    ├── recipe_project/        # Django project settings and URLs
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── recipes/               # Recipes app (models, views, admin)
    │   ├── migrations/
    │   ├── admin.py
    │   ├── models.py
    │   └── views.py
    ├── users/                 # Users app (signup, auth, forms, views)
    │   ├── admin.py
    │   ├── forms.py
    │   └── views.py
    ├── templates/             # Global templates folder
    │   ├── base.html
    │   ├── recipes/
    │   │   ├── recipe_list.html
    │   │   ├── recipe_detail.html
    │   │   ├── recipe_form.html
    │   │   └── recipe_confirm_delete.html
    │   ├── users/
    │   │   └── signup.html
    │   └── registration/
    │       └── login.html
    ├── static/                # Static files (CSS, images, favicon)
    ├── manage.py
    ├── db.sqlite3             # SQLite database (default)
    ├── .gitignore
    ├── LICENSE
    └── README.md

------------------------------------------------------------------------

## 🔐 Security Notes

-   Keep your `.env` file secret if you add one for API keys or settings.
-   Do **not** commit sensitive data (passwords, keys, etc.).

------------------------------------------------------------------------

## 👤 Author

Maintained by [OmAr1dev](https://github.com/OmAr1dev/django-recipe-app)

------------------------------------------------------------------------

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
