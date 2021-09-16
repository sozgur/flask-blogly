from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()
IMG_URL = "https://www.edmundsgovtech.com/wp-content/uploads/2020/01/default-picture_0_0.png"

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):

    """ User """

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.Text, nullable=False, default=IMG_URL)

    posts = db.relationship('Post', backref='user', cascade="all, delete-orphan")

    @property
    def full_name(self):
        """ Full name of user """
        return f"{self.first_name} {self.last_name}"


    def __repr__(self):
        return f"<User first_name: {self.first_name} last_name: {self.last_name} image_url: {self.image_url}>"

class Post(db.Model):
    """Post table"""

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f"<Post title: {self.title} content: {self.content} created_at: {self.created_at} user_id: {self.user_id}>"




