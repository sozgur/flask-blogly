from unittest import TestCase

from app import app
from models import db, User

app.config['TESTING'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///test_db'
app.config['SQLALCHEMY_ECHO'] = False

class UserTestCase(TestCase):

    def setUp(self):
        db.create_all()
        self.client = app.test_client()
        user = User(first_name="Bob", last_name="Kaplan")
        db.session.add(user)
        db.session.commit()

        self.user_id = user.id

    def tearDown(self):
        db.drop_all()


    # test add user
    def test_add_user(self):
        with self.client:
            res = self.client.post('/users/new', 
                data={'fname':"John", 'lname':"David", 'imgUrl':""}, 
                follow_redirects=True)
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn("John David", html)


    # test show user detail
    def test_show_user_detail(self):
        with self.client:
            res = self.client.get(f"/users/{self.user_id}")
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn("<h1>Bob Kaplan</h1>", html)

    # test edit user
    def test_edit_user(self):
        with self.client:
            res = self.client.post(f"/users/{self.user_id}/edit", 
                data={'fname':"Tom", 'lname':"Peker", 'imgUrl':""}, 
                follow_redirects=True)
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn("<h1>Tom Peker</h1>", html)


    # test delete user
    def test_delete_user(self):
        with self.client:
            res = self.client.post(f"/users/{self.user_id}/delete", 
                follow_redirects=True)
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)







