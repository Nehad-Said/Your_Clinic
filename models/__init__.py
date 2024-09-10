from flask import Flask
from config import Config
from routes.routes import main 
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
app.register_blueprint(main)
login_manager = LoginManager(app)
login_manager.login_view = 'main.login'

@login_manager.user_loader
def load_user(user_id):
    from models.models import User
    return User.query.get(int(user_id))



with app.app_context():
    db.create_all()
