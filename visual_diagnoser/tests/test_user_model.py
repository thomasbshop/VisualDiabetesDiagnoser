import unittest
from app.models import User

class UserModelTestCase(unittest.TestCase):
	def test_password_setter(self):
		u = User(password = 'password1')
		self.assertTrue(u.password_hash is not None)

	def test_no_password_getter(self):
		u = User(password = 'password1')
		with self.assertRaises(AttributeError):
			u.password

	def test_password_verification(self):
		u = User(password = 'password1')
		self.assertTrue(u.verify_password('password1'))
		self.assertFalse(u.verify_password('password2'))

	def test_password_salts_are_random(self):
		u = User(password='password1')
		u2 = User(password='password1')
		self.assertTrue(u.password_hash != u2.password_hash)