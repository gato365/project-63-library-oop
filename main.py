from users import User, Customer, Admin
from products import Product, Clothing, Electronics
from transactions import ShoppingCart, Order, Payment
from database import Database


db = Database()
db.load_data()


# Adding users
admin = Admin(user_id=1, username="admin1", email="admin@example.com")
customer = Customer(user_id=2, username="customer1", email="customer@example.com")
db.add_user(admin)
db.add_user(customer)

# # Adding products
# laptop = Electronics(product_id=101, name="Laptop", brand="Dell")
# tshirt = Clothing(product_id=102, name="T-Shirt", size="Medium")
# db.add_product(laptop)
# db.add_product(tshirt)



# cart = ShoppingCart()
# cart.add_item(laptop.product_id, 1)
# cart.add_item(tshirt.product_id, 2)
# order = Order(cart.checkout())
# db.add_order(order)

# # Simulate payment
# payment = Payment(amount=200.00)
# payment.make_payment('credit')


# cart = ShoppingCart()
# cart.add_item(laptop.product_id, 1)
# cart.add_item(tshirt.product_id, 2)
# order = Order(cart.checkout())
# db.add_order(order)

# # Simulate payment
# payment = Payment(amount=200.00)
# payment.make_payment('credit')
