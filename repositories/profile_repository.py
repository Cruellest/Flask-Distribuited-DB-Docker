from models.models import Profile

def get_user_by_username(username):
    return Profile.query.filter_by(username=username).first()

def create_user(username, password):
    from werkzeug.security import generate_password_hash
    from models import db
    hashed_password = generate_password_hash(password)
    new_user = Profile(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return new_user

class ProfileView():
    column_exclude_list = ['password', ]
    column_searchable_list = ['username', ]
    can_export = True
    can_view_details = True