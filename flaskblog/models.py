from datetime import datetime
from flaskblog import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.svg')
    password = db.Column(db.String(60), nullable=False)

    user_type = db.Column(db.String(20), nullable=False, default="Patient")
    posts = db.relationship('Post', backref='author',
                            lazy=True)  # Post refer to class Post


    def __repr__(self):
        return f"User('{self.username}', {self.email}', {self.image_file}, {self.user_type}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    # user refer to table user and id to id column
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.title}', {self.date_posted}'')"
