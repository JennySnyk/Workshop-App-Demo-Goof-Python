from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

# Import Blueprints
from vulnerabilities.cmd_injection import cmd_injection_bp
from vulnerabilities.sqli import sqli_bp
from vulnerabilities.hardcoded_secret import hardcoded_secret_bp
from vulnerabilities.path_traversal import path_traversal_bp
from vulnerabilities.xss import xss_bp
from vulnerabilities.insecure_deserialization import insecure_deserialization_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(cmd_injection_bp)
app.register_blueprint(sqli_bp)
app.register_blueprint(hardcoded_secret_bp)
app.register_blueprint(path_traversal_bp)
app.register_blueprint(xss_bp)
app.register_blueprint(insecure_deserialization_bp)

# --- Database Setup ---
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    # Create users table if it doesn't exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    # Create todos table if it doesn't exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL
        )
    ''')
    # Add a default user if the table is empty
    c.execute("SELECT COUNT(*) FROM users")
    if c.fetchone()[0] == 0:
        c.execute("INSERT INTO users (username, password) VALUES ('admin', 'password123')")
    conn.commit()
    conn.close()

init_db()

# --- Main Routes ---
@app.route('/')
def index():
    return render_template('index.html')

# --- To-Do List Routes ---
@app.route('/todos')
def todos():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM todos")
    items = c.fetchall()
    conn.close()
    return render_template('todos.html', items=items)

@app.route('/todos/add', methods=['POST'])
def add_todo():
    content = request.form.get('content')
    if content:
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("INSERT INTO todos (content) VALUES (?)", (content,))
        conn.commit()
        conn.close()
    return redirect(url_for('todos'))

@app.route('/todos/delete/<int:item_id>')
def delete_todo(item_id):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("DELETE FROM todos WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('todos'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)
