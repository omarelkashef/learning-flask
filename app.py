from flask import Flask , render_template , request , redirect , url_for , session , flash
from models.blogpost import *
import os
from flask_migrate import Migrate
from views import *


app = Flask(__name__)
app.config.from_object(os.environ["APP_SETTINGS"])

db.init_app(app)
bcrypt.init_app(app)

app.register_blueprint(users_blueprint)
app.register_blueprint(home_blueprint)

migrate = Migrate(app , db)

if __name__ == "__main__":
    app.run(debug=True)

