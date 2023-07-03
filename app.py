from flask import Flask
from models.blogpost import *
from models.user import *
import os
from flask_migrate import Migrate
from views import *
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(os.environ["APP_SETTINGS"])

login_manager = LoginManager()
login_manager.login_view = "users.login"
login_manager.login_message = "You need to log in"


db.init_app(app)
bcrypt.init_app(app)
login_manager.init_app(app)

app.register_blueprint(users_blueprint)
app.register_blueprint(home_blueprint)

migrate = Migrate(app , db)

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(int(user_id)==User.id).first()

if __name__ == "__main__":
    app.run(debug=True)

