from flask import render_template, request, redirect, url_for, flash
import re
from app import app, db
from app.models import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    phone = request.form.get('phone', '')  # Optional field
    laptop = request.form.get('laptop', '')  # New field

    # Email validation
    email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(email_pattern, email):
        flash("Invalid email format!", "error")
        return redirect(url_for('index'))

    # Phone validation (exactly 10 digits, only numbers)
    if not phone.isdigit() or len(phone) != 10:
        flash("Phone number must be exactly 10 digits!", "error")
        return redirect(url_for('index'))

    user = User(name=name, email=email, phone=phone, laptop=laptop)
    db.session.add(user)
    db.session.commit()
    
    flash("User successfully added!", "success")
    return redirect(url_for('index'))
