from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# Configuration for Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Use Gmail's SMTP server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'hatimourahoumoney@gmail.com'  # Your Gmail address
app.config['MAIL_PASSWORD'] = 'nszq mxbh mpnw blnx'  # Replace with the app password you generated
app.config['MAIL_DEFAULT_SENDER'] = 'hatimourahoumoney@gmail.com'  # Your Gmail address

app.secret_key = 'your_secret_key_here'  # Required for flash messages

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        msg = Message("New Contact Form Submission",
                      recipients=['hatimourahoumoney@gmail.com'])  # Your email address
        msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        
        try:
            mail.send(msg)
            flash('Your message has been sent successfully!', 'success')
        except Exception as e:
            flash('An error occurred while sending your message. Please try again later.', 'error')
        
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True)
