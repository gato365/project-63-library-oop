import json

class Database:
    def __init__(self):
        self.products = {}
        self.users = {}
        self.orders = {} 

    def save_data(self):
        with open('products.json', 'w') as f:
            json.dump(self.products, f)
        with open('users.json', 'w') as f:
            json.dump(self.users, f)
        with open('orders.json', 'w') as f:
            json.dump(self.orders, f)
        print("Data saved successfully")
        pass

    def load_data(self):
        with open('products.json', 'r') as f:
            self.products = json.load(f)
        with open('users.json', 'r') as f:
            self.users = json.load(f)
        with open('orders.json', 'r') as f:
            self.orders = json.load(f)
        print("Data loaded successfully")
        pass

