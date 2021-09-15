from flask_sqlalchemy import SQLAlchemy

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

    @property
    def full_name(self):
        """ Full name of user """
        return f"{self.first_name} {self.last_name}"




