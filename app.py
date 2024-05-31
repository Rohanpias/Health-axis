from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def init_users_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users 
                 (id INTEGER PRIMARY KEY, email TEXT UNIQUE, password TEXT)''')
    conn.commit()
    conn.close()

def init_admins_db():
    conn = sqlite3.connect('admin.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS admins 
                 (id INTEGER PRIMARY KEY, email TEXT UNIQUE, password TEXT)''')

    # Predefined admin credentials
    admin_email = 'admin@gmail.com'
    admin_password = generate_password_hash('Admin@99419')
    
    try:
        c.execute("INSERT INTO admins (email, password) VALUES (?, ?)", (admin_email, admin_password))
        conn.commit()
    except sqlite3.IntegrityError:
        # Admin user already exists
        pass
    
    conn.close()

def init_patient_db():
    conn = sqlite3.connect('patient_details.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS patients 
                 (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, email TEXT, phone TEXT, consultation_date TEXT, test_result BLOB, prescription BLOB, doctor_description TEXT)''')
    conn.commit()
    conn.close()

init_users_db()
init_admins_db()
init_patient_db()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    email = request.form.get('signupEmail')
    password = generate_password_hash(request.form.get('signupPassword'))

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
        conn.commit()
        flash('User created successfully', 'success')
    except sqlite3.IntegrityError:
        flash('User with that email already exists', 'danger')
    finally:
        conn.close()

    return redirect(url_for('home'))

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('userEmail')
    password = request.form.get('userPassword')
    user_type = request.form.get('userType')

    conn = sqlite3.connect('users.db' if user_type == 'user' else 'admin.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email = ?" if user_type == 'user' else "SELECT * FROM admins WHERE email = ?", (email,))
    user = c.fetchone()
    conn.close()

    if user and check_password_hash(user[2], password):
        session['user_id'] = user[0]
        session['user_email'] = user[1]  
        return redirect(url_for('user_dashboard' if user_type == 'user' else 'admin_dashboard'))
    else:
        flash('Login Unsuccessful. Please check email and password', 'danger')
        return redirect(url_for('home'))

@app.route('/user_dashboard')
def user_dashboard():
    if 'user_id' in session:
        user_email = session['user_email']
        conn = sqlite3.connect('patient_details.db')
        c = conn.cursor()
        c.execute("SELECT * FROM patients WHERE email = ?", (user_email,))
        patient_details = c.fetchall()
        conn.close()
        return render_template('user_dashboard.html', patient_details=patient_details)
    else:
        return redirect(url_for('home'))

@app.route('/admin_dashboard', methods=['GET', 'POST'])
def admin_dashboard():
    if 'user_id' in session:
        if request.method == 'POST':
            name = request.form.get('patientName')
            age = request.form.get('patientAge')
            email = request.form.get('patientEmail')
            phone = request.form.get('patientPhone')
            consultation_date = request.form.get('consultationDate')
            test_result = request.files['testResultFile'].read() if 'testResultFile' in request.files else None
            prescription = request.files['prescriptionFile'].read() if 'prescriptionFile' in request.files else None
            doctor_description = request.form.get('doctorDescription')
            conn = sqlite3.connect('patient_details.db')
            c = conn.cursor()
            c.execute("SELECT * FROM patients WHERE name = ?", (name,))
            existing_patient = c.fetchone()

            if existing_patient:
                patient_id = existing_patient[0]
                c.execute("UPDATE patients SET age=?, email=?, phone=?, consultation_date=?, test_result=?, prescription=?, doctor_description=? WHERE id=?",
                          (age, email, phone, consultation_date, test_result, prescription, doctor_description, patient_id))
                flash('Patient record updated successfully', 'success')
            else:
                c.execute("INSERT INTO patients (name, age, email, phone, consultation_date, test_result, prescription, doctor_description) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                          (name, age, email, phone, consultation_date, test_result, prescription, doctor_description))
                flash('Patient record uploaded successfully', 'success')

            conn.commit()
            conn.close()  
            return jsonify({'success': True, 'message': 'Patient record uploaded successfully'}), 200
        else:
            return render_template('admin_dashboard.html')
    else:
        return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('user_email', None)
    flash('You have successfully logged out.', 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
