from flask import Blueprint, render_template, request
from markupsafe import Markup

xss_bp = Blueprint(
    'xss',
    __name__,
    template_folder='../templates'
)

# In-memory store for comments to keep it simple
comments = []

@xss_bp.route('/vulnerabilities/xss', methods=['GET', 'POST'])
def xss():
    if request.method == 'POST':
        comment = request.form.get('comment')
        if comment:
            # VULNERABLE: User input is stored directly. 
            # It will be rendered unescaped in the template.
            comments.append(comment)
    
    # Use Markup to signal to Jinja2 that the content is safe, thus disabling auto-escaping.
    safe_comments = [Markup(c) for c in comments]

    return render_template('vulnerabilities/xss.html', comments=safe_comments)
