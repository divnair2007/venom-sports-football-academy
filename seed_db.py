"""
seed_db.py
Database seeding script executed during deployment.
Loads initial fixture data if the database is newly initialized,
and ensures an admin superuser is present.
"""

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "venom_academy.settings")
django.setup()

from django.core.management import call_command
from django.contrib.auth import get_user_model
from teams.models import Team

User = get_user_model()


def seed():
    # 1. Load initial fixtures if no teams exist
    if not Team.objects.exists():
        print("Database is empty. Loading initial fixtures from initial_data.json...")
        call_command("loaddata", "initial_data.json")
        print("Initial fixture loaded successfully.")
    else:
        print("Database already contains team data; skipping initial fixture load.")

    # 2. Ensure default superuser exists
    admin_username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "admin")
    admin_email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "admin@venomacademy.com")
    admin_password = os.environ.get("DJANGO_SUPERUSER_PASSWORD", "VenomAcademy2026!")

    user, created = User.objects.get_or_create(
        username=admin_username,
        defaults={
            "email": admin_email,
            "is_staff": True,
            "is_superuser": True,
        },
    )
    if created or os.environ.get("DJANGO_SUPERUSER_PASSWORD"):
        user.set_password(admin_password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        action = "Created" if created else "Updated"
        print(f"{action} superuser '{admin_username}'.")


if __name__ == "__main__":
    seed()
