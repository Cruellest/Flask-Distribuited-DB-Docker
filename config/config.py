import os
class Config:
    #Secret Key do Banco de dados
    SECRET_KEY = os.getenv('SECRET_KEY','default_secret')
    #Paleta de cores do Bootstrap Swatch
    FLASK_ADMIN_SWATCH = os.getenv('FLASK_ADMIN_SWATCH','yeti')
    #Track Modifications SqlAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS','False')
    #Nome de usuario do Admin
    ADMIN_USERNAME = os.getenv('ADMIN_USERNAME', 'admin')
    #Senha do usuario Admin
    ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'admin')
    
    @staticmethod
    
    def get_database_uri():
        DB_TYPE = os.getenv('DB_TYPE','sqlite')
        
        if DB_TYPE == "mysql":
            #Usuario MySQL
            MYSQL_USER = os.getenv('MYSQL_USER', 'root')
            #Senha MySQL
            MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', '')
            #Endereco do Servidor MySQL
            MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
            #Porta de Conexao ao MySQL
            MYSQL_PORT = os.getenv('MYSQL_PORT', '3306')
            #Tipo de database MySQL
            MYSQL_DB = os.getenv('MYSQL_DATABASE', 'mydb')
            return f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
        
        else:
            return 'sqlite:///usersdb.sqlite3'
        
    SQLALCHEMY_DATABASE_URI = get_database_uri()