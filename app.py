from flask import Flask, render_template, request, redirect, url_for, session
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.efficientnet import preprocess_input
from PIL import Image
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
import os
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = "dr_predict_secret_key"

app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# ================= DATABASE SETUP =================
def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    # Admin Table
    c.execute("""
        CREATE TABLE IF NOT EXISTS admin (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)

    # Predictions Table
    c.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image TEXT,
            prediction TEXT,
            confidence REAL,
            date TEXT
        )
    """)

    # Create default admin if not exists
    c.execute("SELECT * FROM admin WHERE username=?", ("admin",))
    if not c.fetchone():
        hashed_pw = generate_password_hash("dr@2025")
        c.execute("INSERT INTO admin (username, password) VALUES (?, ?)", ("admin", hashed_pw))

    conn.commit()
    conn.close()

init_db()

# ================= LOAD MODEL =================
model = load_model('model/hybrid_model_aptos2.h5', compile=False)

CLASS_NAMES = ["No DR", "Mild", "Moderate", "Severe", "Proliferative DR"]

def preprocess_image(image):
    image = image.convert("RGB")
    image = image.resize((224, 224))
    image = np.array(image)
    image = preprocess_input(image)
    image = np.expand_dims(image, axis=0)
    return image

# ================= ROUTES =================

# 🔹 FIRST PAGE → ADMIN LOGIN
@app.route('/')
def home():
    if 'admin' in session:
        return redirect(url_for('admin_dashboard'))
    return redirect(url_for('admin_login'))

@app.route('/about')
def about():
    if 'admin' not in session:
        return redirect(url_for('admin_login'))
    return render_template('about.html')

@app.route('/performance')
def performance():
    if 'admin' not in session:
        return redirect(url_for('admin_login'))
    return render_template('performance.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if 'admin' not in session:
        return redirect(url_for('admin_login'))

    prediction = None
    confidence = None
    image_url = None

    if request.method == 'POST':
        if 'image' in request.files:
            file = request.files['image']

            if file.filename != '':
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)

                image_url = filepath

                img = Image.open(filepath)
                img = preprocess_image(img)

                preds = model.predict([img, img], verbose=0)[0]
                idx = np.argmax(preds)

                prediction = CLASS_NAMES[idx]
                confidence = round(float(np.max(preds) * 100), 2)

                # Save prediction to database
                conn = sqlite3.connect("database.db")
                c = conn.cursor()
                c.execute("""
                    INSERT INTO predictions (image, prediction, confidence, date)
                    VALUES (?, ?, ?, ?)
                """, (image_url, prediction, confidence,
                      datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                conn.commit()
                conn.close()

    return render_template('predict.html',
                           prediction=prediction,
                           confidence=confidence,
                           image_url=image_url)

# ================= ADMIN LOGIN =================
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("SELECT * FROM admin WHERE username=?", (username,))
        admin = c.fetchone()
        conn.close()

        if admin and check_password_hash(admin[2], password):
            session['admin'] = username
            return redirect(url_for('admin_dashboard'))
        else:
            return render_template('admin_login.html', error="Invalid credentials")

    return render_template('admin_login.html')

# ================= ADMIN DASHBOARD =================
@app.route('/admin/dashboard')
def admin_dashboard():
    if 'admin' not in session:
        return redirect(url_for('admin_login'))

    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("SELECT COUNT(*) FROM predictions")
    total = c.fetchone()[0]

    c.execute("SELECT prediction, COUNT(*) FROM predictions GROUP BY prediction")
    class_counts = c.fetchall()

    c.execute("SELECT * FROM predictions ORDER BY id DESC LIMIT 5")
    recent = c.fetchall()

    conn.close()

    return render_template("admin_dashboard.html",
                           total=total,
                           class_counts=class_counts,
                           recent=recent)

# ================= LOGOUT =================
@app.route('/admin/logout')
def admin_logout():
    session.pop('admin', None)
    return redirect(url_for('admin_login'))

# ================= RUN APP =================
if __name__ == '__main__':
    app.run(debug=True)
