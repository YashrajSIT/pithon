class Product:
    def __init__(self, product_id, name, price, discount_percentage=0):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__discount_percentage = discount_percentage
    
    # Getter methods
    def get_product_id(self):
        return self.__product_id
    
    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price
    
    def get_discount_percentage(self):
        return self.__discount_percentage
    
    # Setter methods
    def set_product_id(self, product_id):
        self.__product_id = product_id
    
    def set_name(self, name):
        self.__name = name
    
    def set_price(self, price):
        self.__price = price
    
    def set_discount_percentage(self, discount_percentage):
        self.__discount_percentage = discount_percentage
    
    # Protected method to calculate final price after discount
    def _calculate_final_price(self):
        return self.__price * (1 - self.__discount_percentage / 100)


class Electronics(Product):
    def __init__(self, product_id, name, price, discount_percentage, warranty_period):
        super().__init__(product_id, name, price, discount_percentage)
        self.__warranty_period = warranty_period
    
    # Getter method
    def get_warranty_period(self):
        return self.__warranty_period
    
    # Setter method
    def set_warranty_period(self, warranty_period):
        self.__warranty_period = warranty_period


class Clothing(Product):
    def __init__(self, product_id, name, price, discount_percentage, size, material):
        super().__init__(product_id, name, price, discount_percentage)
        self.__size = size
        self.__material = material
    
    # Getter methods
    def get_size(self):
        return self.__size
    
    def get_material(self):
        return self.__material
    
    # Setter methods
    def set_size(self, size):
        self.__size = size
    
    def set_material(self, material):
        self.__material = material


class ShoppingCart:
    def __init__(self):
        self.products = []
    
    # Method to add a new electronic item
    def add_electronic_item(self, electronic_item):
        if isinstance(electronic_item, Electronics):
            self.products.append(electronic_item)
        else:
            print("Invalid type of product. Electronic item expected.")
    
    # Method to add a new clothing item
    def add_clothing_item(self, clothing_item):
        if isinstance(clothing_item, Clothing):
            self.products.append(clothing_item)
        else:
            print("Invalid type of product. Clothing item expected.")
    
    # Method to display all products
    def display_all_products(self):
        for product in self.products:
            if isinstance(product, Electronics):
                print(f"Product ID: {product.get_product_id()}, Name: {product.get_name()}, Price: {product.get_price()}, Warranty: {product.get_warranty_period()} months")
            elif isinstance(product, Clothing):
                print(f"Product ID: {product.get_product_id()}, Name: {product.get_name()}, Price: {product.get_price()}, Size: {product.get_size()}, Material: {product.get_material()}")
            else:
                print("Unknown product type.")
    
    # Method to calculate and display the total price including tax
    def calculate_total_price_with_tax(self):
        total_price = 0
        for product in self.products:
            total_price += product._calculate_final_price()  # Using protected method to get final price
        
        # Applying tax rate of 10%
        total_price *= 1.1
        
        print(f"Total Price (including 10% tax): ${total_price:.2f}")


# Example usage:

# Create instances of Electronics and Clothing
electronic_item = Electronics(1, "Laptop", 1200, 10, 12)
clothing_item = Clothing(2, "T-shirt", 25, 5, "M", "Cotton")

# Create a shopping cart
cart = ShoppingCart()

# Add items to the shopping cart
cart.add_electronic_item(electronic_item)
cart.add_clothing_item(clothing_item)

# Display all products in the shopping cart
cart.display_all_products()

# Calculate and display the total price including tax
cart.calculate_total_price_with_tax()
