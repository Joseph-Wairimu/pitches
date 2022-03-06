from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES


db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
bootstrap = Bootstrap()
photos = UploadSet('photos',IMAGES)
from flask_mail import Mail
mail = Mail()
def create_app(config_name):

    app = Flask(__name__)
    
    

    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    # config_options[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)
    
    # configure UploadSet
    configure_uploads(app,photos)

    mail.init_app(app)

  
    from .models import User
    
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    # Will add the views and forms
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app