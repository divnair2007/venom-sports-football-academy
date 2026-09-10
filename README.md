# Venom Football Academy Website

Starter scaffold for the T.Y.B.Sc. mini project (2026-27), built to match
the SRS and System Design documents: Django 5.2.x + MySQL 8.0.x +
Bootstrap 5.3.x.

## Setup

1. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate   # venv\Scripts\activate on Windows
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a MySQL database and user:
   ```sql
   CREATE DATABASE venom_db CHARACTER SET utf8mb4;
   CREATE USER 'venom_user'@'localhost' IDENTIFIED BY 'changeme';
   GRANT ALL PRIVILEGES ON venom_db.* TO 'venom_user'@'localhost';
   ```

4. Set environment variables (or edit the defaults directly in
   `venom_academy/settings.py` for local dev):
   ```
   DB_NAME=venom_db
   DB_USER=venom_user
   DB_PASSWORD=changeme
   DB_HOST=localhost
   DB_PORT=3306
   ```

5. Run migrations and create a superuser:
   ```
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   ```

6. Run the dev server:
   ```
   python manage.py runserver
   ```

- Public site: http://127.0.0.1:8000/
- Django built-in admin (quick CRUD win): http://127.0.0.1:8000/admin/
- Custom admin dashboard: http://127.0.0.1:8000/dashboard/

## Project layout

- `core/` — home/about/contact pages + the custom admin dashboard (login,
  logout, dashboard home) in `dashboard_views.py` / `dashboard_urls.py`.
- `teams/`, `players/`, `coaches/`, `matches/`, `training/`,
  `announcements/` — one Django app per SRS module, each with its own
  `models.py`, `admin.py` (Django admin registration), `views.py`
  (public read-only views) and `urls.py`.
- `templates/` — `base.html` (shared Bootstrap layout) plus per-app
  templates, matching the wireframes in the System Design doc.

## What's next (see the build guide)

- Add ModelForm-based add/edit/delete views per module under the
  `/dashboard/` prefix, replacing the current links out to `/admin/`.
- Add client-side JS validation on the add/edit forms (FR-12).
- Write tests per module, then run the integrated test pass before
  deployment (see System Design section 2.4/2.5 and SRS NFR-01).
