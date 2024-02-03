#!/bin/bash

# migrations
python manage.py makemigrations
python manage.py migrate

# Run Django development server in the background
python manage.py runserver 0.0.0.0:8000 &

# Wait for all background jobs to finish
wait

echo "All commands completed."
