class Product:
    """
    A base class for all products in the system.
    """
    def __init__(self, product_id, name):
        """
        Initializes a new Product instance.

        Args:
        product_id (int): The unique identifier for the product.
        name (str): The name of the product.
        """
        self.product_id = product_id
        self.name = name

    def update(self, new_name):
        """
        Updates the name of the product.

        Args:
        new_name (str): The new name to set for the product.
        """
        self.name = new_name
        print(f"Product name updated to {self.name}")

    def search(self, query):
        """
        Checks if the product's name matches the query.

        Args:
        query (str): The search query to compare with the product's name.

        Returns:
        bool: True if the product's name matches the query, False otherwise.
        """
        return self.name == query

class Clothing(Product):
    """
    A subclass of Product that represents clothing items.
    """
    def __init__(self, product_id, name, size):
        """
        Initializes a new Clothing instance.

        Args:
        product_id (int): The unique identifier for the clothing item.
        name (str): The name of the clothing item.
        size (str): The size of the clothing item.
        """
        super().__init__(product_id, name)
        self.size = size

    def update_size(self, new_size):
        """
        Updates the size of the clothing item.

        Args:
        new_size (str): The new size to set for the clothing item.
        """
        self.size = new_size
        print(f"Size updated to {self.size}")

class Electronics(Product):
    """
    A subclass of Product that represents electronic items.
    """
    def __init__(self, product_id, name, brand):
        """
        Initializes a new Electronics instance.

        Args:
        product_id (int): The unique identifier for the electronic item.
        name (str): The name of the electronic item.
        brand (str): The brand of the electronic item.
        """
        super().__init__(product_id, name)
        self.brand = brand

    def update_brand(self, new_brand):
        """
        Updates the brand of the electronic item.

        Args:
        new_brand (str): The new brand to set for the electronic item.
        """
        self.brand = new_brand
        print(f"Brand updated to {self.brand}")

# Example usage
if __name__ == "__main__":
    shirt = Clothing(1, "T-Shirt", "M")
    shirt.update("Casual Shirt")
    shirt.update_size("L")

    laptop = Electronics(2, "Laptop", "Dell")
    laptop.update("Gaming Laptop")
    laptop.update_brand("Asus")
