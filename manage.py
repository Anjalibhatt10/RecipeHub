#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

# Run server
#& C:/Users/anjal/env/Scripts/python.exe E:/project01Dj/core/manage.py runserver

# Migrate
#& C:/Users/anjal/env/Scripts/python.exe E:/project01Dj/core/manage.py migrate

# Make migrations
#& C:/Users/anjal/env/Scripts/python.exe E:/project01Dj/core/manage.py makemigrations

# Shell
#& C:/Users/anjal/env/Scripts/python.exe E:/project01Dj/core/manage.py shell

# Create superuser
#& C:/Users/anjal/env/Scripts/python.exe E:/project01Dj/core/manage.py createsuperuser
