from flask import Blueprint, render_template, request
import yaml
import os

insecure_deserialization_bp = Blueprint(
    'insecure_deserialization',
    __name__,
    template_folder='../templates'
)

@insecure_deserialization_bp.route('/vulnerabilities/insecure_deserialization', methods=['GET', 'POST'])
def insecure_deserialization():
    output = None
    error = None
    if request.method == 'POST':
        yaml_data = request.form.get('yaml_data')
        if yaml_data:
            try:
                # VULNERABLE: Using yaml.load on user-controlled data can lead to arbitrary code execution.
                # The safe alternative is yaml.safe_load().
                output = yaml.load(yaml_data, Loader=yaml.FullLoader)
            except Exception as e:
                error = f"An error occurred during deserialization: {e}"

    return render_template('vulnerabilities/insecure_deserialization.html', output=output, error=error)
