from models.models import Profile

def get_user_by_username(username):
    return Profile.query.filter_by(username=username).first()

def create_user(username, password):
    from models import db
    new_user = Profile(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    return new_user