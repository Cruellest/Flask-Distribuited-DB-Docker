import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY','default_secret')
    FLASK_ADMIN_SWATCH = 'yeti'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  
    ADMIN_USERNAME = os.getenv('ADMIN_USERNAME', 'admin')
    ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'admin')
    
    @staticmethod
    
    def get_database_uri():
        db_type = os.getenv('DB_TYPE','sqlite')
        
        if db_type == "mysql":
            return os.getenv('MYSQL_URL')
        
        else:
            return 'sqlite:///usersdb.sqlite3'
        
    SQLALCHEMY_DATABASE_URI = get_database_uri()