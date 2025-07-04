from flask import Blueprint, render_template, request
import sqlite3

sqli_bp = Blueprint(
    'sqli',
    __name__,
    template_folder='../templates'
)

@sqli_bp.route('/vulnerabilities/sqli', methods=['GET', 'POST'])
def sqli():
    message = ''
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        # VULNERABLE: User input is formatted directly into the SQL query
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        try:
            c.execute(query)
            user = c.fetchone()
            if user:
                message = f"Welcome, {user[1]}!"
            else:
                message = "Invalid credentials."
        except sqlite3.Error as e:
            message = f"Database error: {e}"
        finally:
            conn.close()
    return render_template('vulnerabilities/sqli.html', message=message)
