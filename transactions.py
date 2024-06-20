class ShoppingCart:
    """
    A class to handle shopping cart operations.
    """
    def __init__(self):
        """
        Initializes a new empty shopping cart.
        """
        self.items = {}  # Dictionary to store product_id and quantities

    def add_item(self, product_id, quantity):
        """
        Adds a product to the cart or updates the quantity if it already exists.

        Args:
        product_id (int): The unique identifier of the product.
        quantity (int): The number of products to add.
        """
        if product_id in self.items:
            self.items[product_id] += quantity
        else:
            self.items[product_id] = quantity
        print(f"Added {quantity} of product {product_id} to cart.")

    def remove_item(self, product_id):
        """
        Removes a product from the cart.

        Args:
        product_id (int): The unique identifier of the product to remove.
        """
        if product_id in self.items:
            del self.items[product_id]
            print(f"Product {product_id} removed from cart.")
        else:
            print("Product not found in cart.")

    def checkout(self):
        """
        Simulates the checkout process.

        Returns:
        dict: The items in the cart.
        """
        return self.items

class Order:
    """
    A class to handle order processing.
    """
    def __init__(self, cart_items):
        """
        Initializes a new order with items from the shopping cart.

        Args:
        cart_items (dict): A dictionary of cart items with product_id as key and quantity as value.
        """
        self.cart_items = cart_items

    def process_order(self):
        """
        Processes the order.

        Returns:
        str: A confirmation message with the order details.
        """
        print("Processing your order...")
        return f"Order confirmed for {self.cart_items}"

class Payment:
    """
    A class to handle payment processing.
    """
    def __init__(self, amount):
        """
        Initializes the payment processor for a given amount.

        Args:
        amount (float): The total amount to be paid.
        """
        self.amount = amount

    def make_payment(self, payment_type):
        """
        Simulates making a payment.

        Args:
        payment_type (str): The type of payment (e.g., 'credit', 'debit').

        Returns:
        str: A confirmation message of the payment.
        """
        print("Processing payment...")
        return f"Payment of ${self.amount} made using {payment_type}."

# Example usage
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item(101, 2)
    cart.add_item(102, 1)
    cart.remove_item(102)

    order = Order(cart.checkout())
    print(order.process_order())

    payment = Payment(59.99)
    print(payment.make_payment('credit'))
