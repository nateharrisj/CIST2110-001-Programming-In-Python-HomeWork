# HW9.py
# Author: Nate Harris

import sys

### INSERT CODE FROM LAB11.PY HERE 1-11###

class Product:

    def __init__(self, name: str, price: float, product_id: int):
        self.name = name
        self.price = price
        self.product_id = product_id 

    def __str__(self):
        return f'Product: {self.name}, Price: ${self.price:.2f}, ID: {self.product_id}'

class Customer:
    def __init__(self, name: str, customer_id: int):
        self.name = name
        self.customer_id = customer_id
        self.cart = []

    def __str__(self):
        return f'Customer: {self.name}, ID#: {self.customer_id}'
    
    def add_to_cart(self, Product):
        self.cart.append(Product)
        print(f'\n{Product} was added to {self.name}\'s cart')
        print()

    def remove_from_cart(self, Product):
        self.cart.remove(Product)
        print(f'\n{Product} was removed from {self.name}\'s cart')
        print()
    
    def checkout(self):
        total = 0
        for product in self.cart:
            total += product.price
        print(f'{self.name}\'s Total is: ${total:.2f}\n')
        self.cart = []

    def display_products(self):
        print(f'{self.name}\'s cart:')
        for product in self.cart:
            print(product)

class Store:
    def __init__(self):
        self.products = []
        self.customers = []

    def add_product(self, product: Product):
        self.products.append(product)
        print(f'\n{product} was added to the stores database')
        print()
    
    def add_customer(self, customer: Customer):
        self.customers.append(customer)
        print(f'\n{customer} was added to the stores database')
        print()

    def display_products(self):
        print('Products in store:')
        for product in self.products:
            print(product)
            print()

    def display_customers(self):
        print('Customers in store:')
        for customer in self.customers:
            print(customer)
            print()

### END CODE FROM LAB11.PY ###

# START OF HOMEWORK Questions
# 1. Create a method called add_product_to_customer_cart that takes in a Customer object and a Product object. The method should add the product to the customer's cart. The method should also print out the product that was added and the customer's name.
# Hint: You can use the add_to_cart method from the Customer class.
# Hint2: This method does not need to be in a class. It should be a regular function that takes in a Customer object and a Product object.

def add_product_to_customer_cart(Customer, Product):
    Customer.add_to_cart(Product)
    #print(f'{Product} was added to {Customer.name}\'s cart')

# 2. Create a method called remove_product_from_customer_cart that takes in a Customer object and a Product object. The method should remove the product from the customer's cart. The method should also print out the product that was removed and the customer's name.
# Hint: You can use the remove_from_cart method from the Customer class.
# Hint2: This method does not need to be in a class. It should be a regular function that takes in a Customer object and a Product object.

def remove_product_from_customer_cart(Customer, Product):
    Customer.remove_from_cart(Product)
    #print(f'{Product} was removed from {Customer.name}\'s cart')


# 3. Create a menu function:
# The menu function should return the user's choice as an integer.
# Hint: Print out the menu and then use the input() function to get the user's choice.

def menu():
    print('1. Add Product')
    print('2. Add Customer')
    print('3. Add Product to Customer\'s Cart')
    print('4. Remove Product from Customer\'s Cart')
    print('5. Display Products')
    print('6. Display Customers')
    print('7. Display Customer\'s Cart')
    print('8. Checkout')
    print('9. Exit')
    choice = int(input('\nEnter choice: '))
    return choice

# 4. Create a main function that will call the menu function and then call the appropriate methods based on the user's choice. The main function should be in a while loop that will continue to call the menu function until the user enters 0 to exit the program.
# # IMPORTANT: The main function should create a Store object and then call the appropriate methods on the Store object. Without the Store object, you will not be able to add products or customers.

# Hint 1: If you need informtation from the user about a product or customer, you can ask for it in the main function and then pass it to the appropriate method. Don't be afraid to use input() in the main function.
# Hint 2: Some of the methods take in a Product object or a Customer object. You will need to create a Product object or a Customer object before calling the method. You can create a Product object or a Customer object in the main function and then pass it to the appropriate method.

# Hint 3: You can use the display_products and display_customers methods to help you out.
# Hint 4: Some Methods take in parameters. You will need to pass in the correct parameters to the method. For example, the add_product method takes in a Product object. You will need to pass in a Product object to the method. You can pass in a Product as a parameter.
# IE. store.add_product(product) where product is a Product object.
# store.add_product(Product(name, price, product_id))
# You can either ask the user for the name, price, and product_id or you can hard code it in the main function.

def main():
    
    store = Store()
    while True:
        try: 
            choice = menu()
            if choice < 1 or choice > 9:
                print('\nInvalid choice\n')
                continue
        except ValueError:
            print('\nInvalid choice\n')
            continue
        if choice == 1:
            name = input('\nEnter product name: ')
            price = float(input('Enter product price: '))
            product_id = int(input('Enter product id: '))
            store.add_product(Product(name, price, product_id))

        elif choice == 2:
            name = input('\nEnter customer name: ')
            customer_id = int(input('Enter customer id: '))
            store.add_customer(Customer(name, customer_id))

        elif choice == 3:
            customer_name = input('\nEnter customer name: ')
            product_name = input('Enter product name: ')
            customer = None
            product = None
            for cust in store.customers:
                if cust.name == customer_name:
                    customer = cust
            for prod in store.products:
                if prod.name == product_name:
                    product = prod
            if customer and product:
                add_product_to_customer_cart(customer, product)
            else:
                print('\nCustomer or product not found\n')

        elif choice == 4:
            customer_name = input('\nEnter customer name: ')
            product_name = input('Enter product name: ')
            customer = None
            product = None
            for cust in store.customers:
                if cust.name == customer_name:
                    customer = cust
            for prod in store.products:
                if prod.name == product_name:
                    product = prod
            if customer and product:
                remove_product_from_customer_cart(customer, product)
            else:
                print('\nCustomer or product not found\n')

        elif choice == 5:
            print()
            store.display_products()

        elif choice == 6:
            store.display_customers()

        elif choice == 7:
            customer_name = input('\nEnter customer name: ')
            print()
            customer = None
            for cust in store.customers:
                if cust.name == customer_name:
                    customer = cust
            if customer:
                customer.display_products()
                print()
            else:
                print('\nCustomer not found\n')

        elif choice == 8:
            customer_name = input('\nEnter customer name: ')
            print()
            customer = None
            for cust in store.customers:
                if cust.name == customer_name:
                    customer = cust
            if customer:
                customer.checkout()
            else:
                print('\nCustomer not found')

        elif choice == 9:
            print('\nHave a nice day, enjoy your product!')
            sys.exit()

if __name__ == "__main__":
    main()
