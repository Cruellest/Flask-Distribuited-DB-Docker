from repositories.profile_repository import get_user_by_username
from config.config import Config

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

def verify_admin(username,password):
    if username == Config.ADMIN_USERNAME and password == Config.ADMIN_PASSWORD:
        return True
    
    return False