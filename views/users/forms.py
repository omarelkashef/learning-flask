from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , EmailField
from wtforms.validators import DataRequired , EqualTo , Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired() , Length(min=3, max=25)])
    email = EmailField("email", validators=[DataRequired() , Length(min=6, max=40)])
    password = PasswordField('Password', validators=[DataRequired() , Length(min=5, max=25)])
    confirm_passowrd = PasswordField('Password', validators=[DataRequired(),
                                                             EqualTo('password',
                                                                     message='Passwords must match') ])


