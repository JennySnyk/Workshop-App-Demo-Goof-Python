from flask import Blueprint, render_template, request
import os

path_traversal_bp = Blueprint(
    'path_traversal',
    __name__,
    template_folder='../templates'
)

@path_traversal_bp.route('/vulnerabilities/path_traversal', methods=['GET', 'POST'])
def path_traversal():
    content = None
    error = None
    if request.method == 'POST':
        filename = request.form.get('filename')
        # VULNERABLE: The user-provided filename is joined directly to a path
        file_path = os.path.join('logs', filename)
        try:
            with open(file_path, 'r') as f:
                content = f.read()
        except FileNotFoundError:
            error = f"Error: File '{filename}' not found."
        except Exception as e:
            error = f"An error occurred: {e}"
    
    # Create a dummy log file for the demo
    if not os.path.exists('logs'):
        os.makedirs('logs')
    with open('logs/app.log', 'w') as f:
        f.write('This is a sample log file.')

    return render_template('vulnerabilities/path_traversal.html', content=content, error=error)
