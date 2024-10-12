from flask import Flask,request
from flask_migrate import Migrate
from flask_admin import Admin
from models.models import db, Profile
from views.profile_view import profile_bp,ProfileView,auth
from config.config import Config


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
@auth.login_required
def before_request():
    if request.endpoint == 'admin.index' and not auth.current_user():
        return auth.login_required()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)




