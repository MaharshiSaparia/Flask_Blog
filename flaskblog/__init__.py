from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

# python-web-blog-341010


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '867cee5722126dc099712807a1a21182'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db?check_same_thread=False'
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = '587'
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'maharshi@coronation.in'
    app.config['MAIL_PASSWORD'] = 'Aspire@5738g'

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app

