from . import db
from werkzeug.security import generate_password_hash
from datetime import datetime  # Import datetime directly

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class Movies(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(90))
    description = db.Column(db.Text)
    poster = db.Column(db.String(81)) 
    created_at = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, title, description, poster):
        self.title = title
        self.description = description
        self.poster = poster

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)


class ArticlesSchema(SQLAlchemyAutoSchema):
    class Meta:
        fields = ('id', 'title', 'description', 'poster', 'created_at')
