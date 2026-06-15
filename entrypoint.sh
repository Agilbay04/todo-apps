#!/bin/sh
if [ "$APP_ENV" = "dev" ]; then
    echo "Running in dev mode with Flask dev server..."
    python app.py
else
    echo "Running in production mode with gunicorn..."
    exec gunicorn --bind 0.0.0.0:5005 wsgi:app
fi
