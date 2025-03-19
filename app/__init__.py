import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

# Set a secret key for session management
app.config['SECRET_KEY'] = '9f3c2b45678d2a4e9170b8f02e5d3c43a3b7d1a638ec0f739c7e3e1d8f5a6d27'

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@postgres/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Import models and routes after db initialization to avoid circular imports
from app import models, routes

# Create database tables (only for development, not recommended for production)
with app.app_context():
    db.create_all()
