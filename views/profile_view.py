from flask import Blueprint, jsonify, redirect, url_for
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

class AuthAdminMixin:
    def is_accessible(self):
        return auth.current_user() is not None

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login'))

class ProfileView(AuthAdminMixin, ModelView):
    column_exclude_list = ['password', ]
    column_searchable_list = ['username', ]
    can_export = True
    can_view_details = True
