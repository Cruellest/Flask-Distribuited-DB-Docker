from repositories.profile_repository import get_user_by_username

def verify_password(username,password):
    user = get_user_by_username(username)
    if user and user.password == password:
        return user
    
    return None

def validate_authentication(username,password):
    user = get_user_by_username(username)
    if user and user.password == password:
        return True
    
    return False