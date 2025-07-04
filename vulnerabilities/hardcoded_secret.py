from flask import Blueprint, render_template

hardcoded_secret_bp = Blueprint(
    'hardcoded_secret',
    __name__,
    template_folder='../templates'
)

@hardcoded_secret_bp.route('/vulnerabilities/hardcoded_secret')
def hardcoded_secret():
    # VULNERABLE: API key is hardcoded in the source code
    api_key = "sk_live_1234567890abcdefghijklmnopqrstuv"
    return render_template('vulnerabilities/hardcoded_secret.html', api_key=api_key)
