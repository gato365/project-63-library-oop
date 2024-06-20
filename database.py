import json

class Database:
    def __init__(self):
        self.products = {}
        self.users = {}
        self.orders = {}

    def save_data(self):
        try:
            with open('products.json', 'w') as f:
                json.dump(self.products, f)
            with open('users.json', 'w') as f:
                json.dump(self.users, f)
            with open('orders.json', 'w') as f:
                json.dump(self.orders, f)
            print("Data saved successfully")
        except Exception as e:
            print(f"An error occurred while saving data: {e}")

    def load_data(self):
        try:
            with open('products.json', 'r') as f:
                self.products = json.load(f)
            with open('users.json', 'r') as f:
                self.users = json.load(f)
            with open('orders.json', 'r') as f:
                self.orders = json.load(f)
            print("Data loaded successfully")
        except FileNotFoundError:
            print("Data file not found, initializing new database.")
        except Exception as e:
            print(f"An error occurred while loading data: {e}")
            # Optionally initialize data structures if files are corrupt or unreadable
            self.products = {}
            self.users = {}
            self.orders = {}

    # Product operations
    def add_product(self, product):
        self.products[product.id] = product

    def get_product(self, product_id):
        return self.products.get(product_id, None)

    def update_product(self, product):
        if product.id in self.products:
            self.products[product.id] = product
            return True
        return False

    def delete_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            return True
        return False

    # User operations
    def add_user(self, user):
        self.users[user.id] = user

    def get_user(self, user_id):
        return self.users.get(user_id, None)

    def update_user(self, user):
        if user.id in self.users:
            self.users[user.id] = user
            return True
        return False

    def delete_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False

    # Order operations
    def add_order(self, order):
        self.orders[order.id] = order

    def get_order(self, order_id):
        return self.orders.get(order_id, None)

    def update_order(self, order):
        if order.id in self.orders:
            self.orders[order.id] = order
            return True
        return False

    def delete_order(self, order_id):
        if order_id in self.orders:
            del self.orders[order_id]
            return True
        return False
