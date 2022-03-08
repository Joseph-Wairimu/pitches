import os
class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')
  
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    @staticmethod
    def init_app(app):
        pass
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI =' postgresql://tspvpabjirokwt:e470e82d5015246cadcd82ba3ef7f5147054c0feaaaf94a94024a7cccc49f616@ec2-54-157-15-228.compute-1.amazonaws.com:5432/db66ktjucrjr8t'
    print(SQLALCHEMY_DATABASE_URI)
    

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:Access@localhost/pitchdata'
    DEBUG = True  
    

    

config_options = {
'development':DevConfig,
'production':ProdConfig
}

 
