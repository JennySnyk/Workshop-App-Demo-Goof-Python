from flask import Blueprint, render_template, request
import subprocess

cmd_injection_bp = Blueprint(
    'cmd_injection',
    __name__,
    template_folder='../templates'
)

@cmd_injection_bp.route('/vulnerabilities/cmd_injection', methods=['GET', 'POST'])
def cmd_injection():
    output = None
    if request.method == 'POST':
        domain = request.form.get('domain')
        # VULNERABLE: User input is passed directly to a shell command
        output = subprocess.getoutput(f"nslookup {domain}")
    return render_template('vulnerabilities/cmd_injection.html', output=output)
