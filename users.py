

class User:
    """
    A base class for all user types in the system. This class may be abstract if
    it should not be instantiated directly.
    """
    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email

    def login(self):
        """Simulate user login process."""
        print(f"{self.username} logged in.")
        return True

    def logout(self):
        """Simulate user logout process."""
        print(f"{self.username} logged out.")
        return True

    def update_profile(self, **kwargs):
        """Allow a user to update their profile information."""
        for key, value in kwargs.items():
            setattr(self, key, value)
        print("Profile updated successfully.")
        return True

    ## Define User id attribute
    
    def user_id(self):
        return self._user_id
    
class Customer(User):
    """
    A class representing a customer in the system. Inherits from User.
    """
    def view_catalog(self, catalog):
        """Allow the customer to view the product catalog."""
        print(f"{self.username} is viewing the catalog.")
        for product in catalog:
            print(product)
        return catalog

    def place_order(self, order):
        """Simulate placing an order."""
        print(f"{self.username} placed an order with order id {order}.")
        return order

class Admin(User):
    """
    A class representing an admin in the system. Inherits from User.
    Admins have additional privileges like accessing reports and modifying product listings.
    """
    def access_reports(self):
        """Allow the admin to access various system reports."""
        print(f"{self.username} accessed system reports.")

    def modify_product_listing(self, product_id, **changes):
        """Allow the admin to modify product listings."""
        print(f"{self.username} modified product listing for product id {product_id}. Changes: {changes}")

