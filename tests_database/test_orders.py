import unittest
from database import Database

class TestOrderFunctions(unittest.TestCase):
    def setUp(self):
        self.db = Database()

    def test_add_order(self):
        self.db.add_order(1, 'Order1')
        self.assertIn(1, self.db.orders)

    def test_get_order(self):
        self.db.add_order(1, 'Order1')
        self.assertEqual(self.db.get_order(1).name, 'Order1')

    def test_update_order(self):
        self.db.add_order(1, 'Order1')
        self.db.update_order(1, 'Order2')
        self.assertEqual(self.db.get_order(1).name, 'Order2')

    def test_delete_order(self):
        self.db.add_order(1, 'Order1')
        self.db.delete_order(1)
        self.assertNotIn(1, self.db.orders)

if __name__ == '__main__':
    unittest.main()