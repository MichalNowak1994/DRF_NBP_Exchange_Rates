import os
import django
from django.contrib.auth import get_user_model
from django.db import IntegrityError
import sys
from typing import NoReturn

os.environ['DJANGO_SETTINGS_MODULE'] = 'APIQuotesFactory.settings'
django.setup()

User = get_user_model()


def create_user() -> NoReturn:
    """
    Create a superuser for the Django application.

    The script should be run with three command line arguments:
        1. username (str): The username for the superuser.
        2. email (str): The email address for the superuser.
        3. password (str): The password for the superuser.

    Prints a success message if the superuser is created successfully,
    or an error message if the user already exists.
    """
    try:
        print("Creating superuser...")
        User.objects.create_superuser(sys.argv[1], sys.argv[2], sys.argv[3])
        print("Superuser created.")
    except IntegrityError:
        print("User already exists.")


create_user()
