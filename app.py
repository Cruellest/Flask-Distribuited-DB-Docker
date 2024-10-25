import logging
from flask import Flask,request,redirect,url_for
from flask_migrate import Migrate
from flask_admin import Admin
from models.models import db, Profile
from views.profile_view import profile_bp,ProfileView,auth
from config.config import Config
from services.auth_service import verify_admin

# Application log
logging.basicConfig(format='%(asctime)s - %(message)s', filename="log/app.log", level=logging.INFO)
log = logging.getLogger()

app = Flask("Comp Dist")
app.config.from_object(Config)

# Inicializar o banco de dados e as migrações
db.init_app(app)
migrate = Migrate(app, db)

# Registrar blueprints de visualização
app.register_blueprint(profile_bp)

with app.app_context():
    db.create_all()  # Criar tabelas no banco de dados
    if not Profile.query.filter_by(username=Config.ADMIN_USERNAME).first():
        admin = Profile(username=Config.ADMIN_USERNAME, password=Config.ADMIN_PASSWORD)
        db.session.add(admin)
        db.session.commit()

from views.profile_view import profile_bp, ProfileView, auth

# Inicializar o Flask-Admin
adminPage = Admin(app, name='Super App', template_mode='bootstrap4')
adminPage.add_view(ProfileView(Profile, db.session, endpoint="admin_profile"))

# Adicionando autenticação na rota /admin

@app.before_request
def before_request():
    if request.endpoint == 'admin.index':
        auth_header = request.authorization
        if not auth_header or not verify_admin(auth_header.username, auth_header.password):
            return redirect(url_for('profile.index'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)




