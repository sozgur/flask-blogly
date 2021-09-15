from flask import Flask, render_template, redirect, request
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.debug = True
app.config['SECRET_KEY'] = "asdfsaf234esdf456tFGDHsdsgf"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def home():
    """ Home page """
    return redirect('/users')


@app.route('/users')
def list_user():
    """ Show all users name in db """
    users = User.query.order_by(User.last_name, User.first_name).all()
    return render_template("users/list.html", users = users)

@app.route('/users/new', methods=["GET"])
def add_user_form():
    """Show add new user form"""
    return render_template("users/new_form.html")

@app.route('/users/new', methods=["POST"])
def add_user():
    """Add new user to db"""
    first_name = request.form['fname']
    last_name = request.form['lname']
    img_url = request.form['imgUrl']

    user = User(first_name= first_name, last_name=last_name)
    if img_url != "":
        user.image_url = img_url

    db.session.add(user)
    db.session.commit()

    return redirect('/users')

@app.route('/users/<int:user_id>')
def show_user(user_id):
    """Show user detail"""
    user = User.query.get_or_404(user_id)
    return render_template('users/detail.html', user=user)


@app.route('/users/<int:user_id>/edit', methods=['GET'])
def edit_user_form(user_id):
    """Show user edit form"""
    user = User.query.get_or_404(user_id)
    return render_template("users/edit_form.html", user=user)


@app.route('/users/<int:user_id>/edit', methods=['POST'])
def edit_user(user_id):
    """Update user information on db"""
    first_name = request.form['fname']
    last_name = request.form['lname']
    img_url = request.form['imgUrl']

    user = User.query.get_or_404(user_id)
    user.first_name = first_name
    user.last_name = last_name

    if img_url == "":
        user.image_url = "https://www.edmundsgovtech.com/wp-content/uploads/2020/01/default-picture_0_0.png"
    else:
        user.image_url = img_url

    db.session.add(user)
    db.session.commit()

    return render_template('users/detail.html', user=user)


@app.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    """Delete user from db"""
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect("/users")




