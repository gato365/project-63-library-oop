import unittest
import sys
sys.path.append('..')  # Adds the root directory to the system path
from users import Customer, Admin

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer(user_id=1, username="john_doe", email="john@example.com")

    def test_login(self):
        # Assuming login method returns True on success
        self.assertTrue(self.customer.login())

    def test_view_catalog(self):
        # Assuming view_catalog returns a list of products
        catalog = self.customer.view_catalog(["Product1", "Product2", "Product3"])
        self.assertEqual(catalog, ["Product1", "Product2", "Product3"])

    def test_place_order(self):
        # Assuming place_order returns an order confirmation
        order_confirmation = self.customer.place_order("Order123")
        self.assertEqual(order_confirmation, "Order123")

        
class TestAdminInitialization(unittest.TestCase):
    def setUp(self):
        self.admin = Admin(user_id=1, username="adminUser", email="admin@example.com")

    def test_inheritance(self):
        """Test that Admin correctly inherits from User."""
        self.assertIsInstance(self.admin, User)

    def test_initialization(self):
        """Test that Admin initializes its specific attributes correctly."""
        self.assertEqual(self.admin.username, "adminUser")
        self.assertEqual(self.admin.email, "admin@example.com")
        self.assertEqual(self.admin.reports_accessed, [])
        self.assertEqual(self.admin.product_changes_log, [])

    def test_user_functionality(self):
        """Test that Admin retains functionality from User."""
        self.assertTrue(self.admin.login())

if __name__ == '__main__':
    unittest.main()