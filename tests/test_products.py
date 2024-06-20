import unittest
from database import Database

class TestProductFunctions(unittest.TestCase):
    def setUp(self):
        """Set up a fresh database before each test."""
        self.db = Database()
        self.db.load_data()  # Assuming load_data() can load mock data for testing

    def tearDown(self):
        """Clean up after each test."""
        self.db = None

    ## Test functions for products
    def test_add_product(self):
        """Test adding a product to the database."""
        product = Product(id=1, name="Laptop", category="Electronics")
        self.db.add_product(product)
        self.assertIn(1, self.db.products)

    def test_get_product(self):
        """Test retrieving a product."""
        self.db.products[1] = Product(id=1, name="Laptop", category="Electronics")
        product = self.db.get_product(1)
        self.assertEqual(product.name, "Laptop")

    def test_update_product(self):
        """Test updating a product."""
        product = Product(id=1, name="Old Laptop", category="Electronics")
        self.db.products[1] = product
        product.name = "New Laptop"
        self.db.update_product(product)
        self.assertEqual(self.db.products[1].name, "New Laptop")

    def test_delete_product(self):
        """Test deleting a product."""
        self.db.products[1] = Product(id=1, name="Laptop", category="Electronics")
        self.db.delete_product(1)
        self.assertNotIn(1, self.db.products)






