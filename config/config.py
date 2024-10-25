import os
class Config:
    #Secret Key do Banco de dados
    SECRET_KEY = os.getenv('SECRET_KEY','default_secret')
    
    FLASK_ADMIN_SWATCH = os.getenv('FLASK_ADMIN_SWATCH','yeti')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS','False')
    ADMIN_USERNAME = os.getenv('ADMIN_USERNAME', 'admin')
    ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'admin')
    
    @staticmethod
    
    def get_database_uri():
        db_type = os.getenv('DB_TYPE','sqlite')
        
        if db_type == "mysql":
            MYSQL_USER = os.getenv('MYSQL_USER', 'root')
            MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', '')
            MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
            MYSQL_PORT = os.getenv('MYSQL_PORT', '3306')
            MYSQL_DB = os.getenv('MYSQL_DATABASE', 'mydb')
            return f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
        
        else:
            return 'sqlite:///usersdb.sqlite3'
        
    SQLALCHEMY_DATABASE_URI = get_database_uri()