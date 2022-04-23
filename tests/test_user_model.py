from app import db
from app.models.user import User
from app.models.schemas import UserSchema

from tests.utils.base import BaseTestCase


class TestUserModel(BaseTestCase):
    def test_password_setter(self):
        u = User(password="cat")
        self.assertTrue(u.password_hash is not None)

    def test_no_password_getter(self):
        u = User(password="testpassword")
        with self.assertRaises(AttributeError):
            u.password

    def test_password_salts_are_random(self):
        u = User(password="testpassword")
        u2 = User(password="testpassword")
        self.assertTrue(u.password_hash != u2.password_hash)

    def test_schema(self):
        u = User(username="testuser", password="testpassword")
        u_dump = UserSchema().dump(u)

        self.assertTrue(u_dump["username"] == "testuser")

        with self.assertRaises(KeyError):
            u_dump["password_hash"]
