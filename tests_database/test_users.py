import unittest
from database import Database


class TestUserFunctions(unittest.TestCase):
    def setUp(self):
        self.db = Database()

    def test_add_user(self):
        self.db.add_user(1, 'User1')
        self.assertIn(1, self.db.users)

    def test_get_user(self):
        self.db.add_user(1, 'User1')
        self.assertEqual(self.db.get_user(1).name, 'User1')

    def test_update_user(self):
        self.db.add_user(1, 'User1')
        self.db.update_user(1, 'User2')
        self.assertEqual(self.db.get_user(1).name, 'User2')

    def test_delete_user(self):
        self.db.add_user(1, 'User1')
        self.db.delete_user(1)
        self.assertNotIn(1, self.db.users)

if __name__ == '__main__':
    unittest.main()
