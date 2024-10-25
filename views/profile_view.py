from flask import Blueprint, jsonify
from flask_httpauth import HTTPBasicAuth
from services.auth_service import verify_password
from flask_admin.contrib.sqla import ModelView

auth = HTTPBasicAuth()
profile_bp = Blueprint('profile', __name__)

@auth.verify_password
def verify_password_handler(username, password):
    return verify_password(username, password)

@profile_bp.route('/')
@auth.login_required
def index():
    user = auth.current_user()
    if user:
        return jsonify({"success": f"Usuário {user.username} acessou o index."})
    return jsonify({"error": "Usuário não encontrado"}), 404

class ProfileView(ModelView):
    column_exclude_list = ['password', ]
    column_searchable_list = ['username', ]
    can_export = True
    can_view_details = True
