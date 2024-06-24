import unittest
from database import Database

class TestProductFunctions(unittest.TestCase):
    def setUp(self):
        self.db = Database()

    def test_add_product(self):
        self.db.add_product(1, 'Product1', 'Category1')
        self.assertIn(1, self.db.products)

    def test_get_product(self):
        self.db.add_product(1, 'Product1', 'Category1')
        self.assertEqual(self.db.get_product(1).name, 'Product1')

    def test_update_product(self):
        self.db.add_product(1, 'Product1', 'Category1')
        self.db.update_product(1, 'Product2', 'Category2')
        self.assertEqual(self.db.get_product(1).name, 'Product2')

    def test_delete_product(self):
        self.db.add_product(1, 'Product1', 'Category1')
        self.db.delete_product(1)
        self.assertNotIn(1, self.db.products)

if __name__ == '__main__':
    unittest.main()