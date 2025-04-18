# Add any form classes for Flask-WTF here
# from flask_wtf import FlaskForm, FileField, FileAllowed, FileRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired
from wtforms import SubmitField


class MovieForm(FlaskForm):
    title = StringField("Title", validators=[InputRequired()])
    description = StringField("Description", validators=[InputRequired()])
    poster = FileField("Poster", validators=[FileRequired(), FileAllowed(["jpg", "png"], "Images only!")])