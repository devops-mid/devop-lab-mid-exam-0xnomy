#!/bin/bash
echo "Building the application..."

# Exit if any command fails
set -e

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Ensure database migrations (if using Flask-Migrate)
if [ -d "migrations" ]; then
    echo "Applying database migrations..."
    flask db upgrade
else
    echo "No migrations found. Skipping..."
fi

echo "Build completed successfully."
