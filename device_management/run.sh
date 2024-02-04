#!/bin/bash

# migrations
python manage.py makemigrations
python manage.py migrate

# Run Django development server in the background
python manage.py runserver 0.0.0.0:8000 &

# Create superuser
python manage.py createsuperuser --noinput --username=$DJANGO_SUPERUSER_USERNAME --email=$DJANGO_SUPERUSER_EMAIL

# Run command to populate database with device information
python manage.py populate_devices &

# Wait for all background jobs to finish
wait

echo "All commands completed."
