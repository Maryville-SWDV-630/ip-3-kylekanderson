# SWDV-630: Object-Oriented Coding
# Kyle Anderson
# Week 3 Assignment

##################################
# INSTRUCTIONS
##################################
# For this exercise, we want you to code a generic superclass and at least three subclasses of that superclass, each class needs to have at least 2 attributes and 2 methods. It’s easiest to simply describe a real-world object in this manner.  You need to provide a test method that shows your classes in operation.

# I would highly suggest that you look at week 8 and the final project.   You should pick a system for your week 8 project now and start building using this assignment as a base.

# NOTE: MenuItem is my superclass and Pizza, Drink, and Wings are my subclasses. The Order class is an extra class I created because it's used by the other classes.

##################################
# IMPORTS
##################################
from datetime import datetime
import uuid

##################################
# CLASS DEFINITIONS
##################################


class Order:
    """
    A class used to represent an order

    Attributes
    ----------
    createdOn : datetime

        the date and time the order was created

    Customer : Customer object

        the Customer object which corresponds to the customer placing the order

    orderID : uuid

        a unique identifier for the order

    orderItems : list

        a list of items (objects) in the order
    """
    def __init__(self, Customer):
        self.createdOn = datetime.now()
        self.Customer = Customer
        self.orderId = self.generateOrderId()
        self.orderItems = []

    def generateOrderId(self):
        return uuid.uuid4()


class MenuItem:
    """
    A class used to represent a Menu Item

    Attributes
    ----------
    name : str

        the name of the menu item

    description : str

        a description of the item to appear on the menu

    category : str

        a category used to group menu items together

    __sizePricing : dict

        a private dictionary that contains sizes (keys) and prices (values) for menu items
    """

    def __init__(self, name, description, category, sizePricing):
        self.name = name
        self.description = description
        self.category = category
        self.__sizePricing = sizePricing

    def getPrice(self, size):
        """returns corresponding price for supplied size from the __sizePricing dictionary"""
        return self.__sizePricing[size]

    def updatePrice(self, size, price):
        """updates price for the supplied size in the __sizePricing dictionary"""
        self.__sizePricing[size] = price

    def addToOrder(self, Order):
        """appends the MenuItem object to the supplied Order's orderItems list"""
        Order.orderItems.append(self)

    def removeFromOrder(self, Order):
        """removes the MenuItem object from the supplied Order's orderItem list"""
        Order.orderItems.remove(self)


class Pizza(MenuItem):
    """
    A class representing a single pizza

    Attributes
    ----------
    crustStyle : str

        the style of crust (ex: thin crust, thick crust, deep dish, etc.)

    toppings : list

        a list of toppings (str) to be included on the pizza

    size : str

        the size of the pizza (Small, Medium, Large)

    """

    def __init__(self, crustStyle, size, toppings):
        super().__init__('Pizza', 'Baked fresh in our wood-fire oven',
                         'Entrees', {'Small': 10.00, 'Medium': 15.00, 'Large': 20.00})
        self.crustStyle = crustStyle
        self.toppings = toppings
        self.size = size

    def addToppings(self, toppings):
        """add a supplied list of toppings to a Pizza object"""
        for topping in toppings:
            self.toppings.append(topping)

    def removeToppings(self, toppings):
        """remove a supplied list of toppings from a Pizza object"""
        for topping in toppings:
            if topping in self.toppings:
                self.toppings.remove(topping)


class Drink(MenuItem):
    """
    A class representing a single drink 

    Attributes
    ----------
    size : str

        the size of the drink (Small, Medium, Large)

    flavor : str

        the flavor of the drink (Coke, Diet Coke, Root Beer, etc.)

    __additionalFlavors : list

        a private list of additional flavorings to be added to the drink
    """

    def __init__(self, size, flavor):
        super().__init__('Drink', 'Served cold', 'Refreshments',
                         {'Small': 1.00, 'Medium': 1.50, 'Large': 2.00})
        self.size = size
        self.flavor = flavor
        self.__additionalFlavors = []

    def freeDrink(self):
        """update the price of a Drink object to be 0.00"""
        super().updatePrice(self.size, 0.00)

    def addFlavor(self, flavor):
        """add an additional flavor to a Drink object"""
        self.__additionalFlavors.append(flavor)


class Wings(MenuItem):
    """
    A class representing a single wings order

    Attributes
    ----------
    quantity : int

        the number of wings being ordered (6, 12, 18)

    flavor : str

        the sauce flavoring for the wings

    sides : list

        a list of sides to be included with the wings (celery, carrots, ranch, etc.)
    """

    def __init__(self, quantity, flavor, sides):
        super().__init__('Wings', 'Lots of different flavors available',
                         'Appetizers', {6: 3.00, 12: 5.00, 24: 8.00})
        self.quantity = quantity
        self.flavor = flavor
        self.sides = sides

    def superHot(self):
        """adds 'SUPER HOT: ' to the flavor name"""
        self.flavor = 'SUPER HOT: ' + self.flavor

    def halfPrice(self):
        """cuts the price of a Wings object in half"""
        super().updatePrice(self.quantity, self.getPrice(self.quantity) / 2)


##################################
# DRIVER CODE - Pizza
##################################
# Create a pizza object
myPizza = Pizza('Thin', 'Medium', ['Cheese', 'Pepperoni'])

# Print a list of the toppings on the pizza
print('Pizza toppings: %s' % myPizza.toppings)

# Print the price of the pizza, based on the size
print('Pizza price: %s' % myPizza.getPrice(myPizza.size))

# Add some toppings to the pizza
myPizza.addToppings(['Anchovies', 'Peppers'])

# Remove some toppings from the pizza
myPizza.removeToppings(['Anchovies', 'Black Olives'])

# After changing toppings, print out the toppings list
print('Pizza toppings: %s' % myPizza.toppings)

##################################
# DRIVER CODE - Drink
##################################
# Create a drink object
myDrink = Drink('Medium', 'Diet Coke')

# Print the flavor of the drink
print('Drink flavor: %s' % myDrink.flavor)

# Print the price of the drink, based on the size
print('Drink price: %s' % myDrink.getPrice(myDrink.size))

##################################
# DRIVER CODE - Wings
##################################
myWings = Wings(12, 'Buffalo', ['Celery', 'Carrots', 'Ranch Sauce'])

# Make the wings super hot
myWings.superHot()

# Make the wings half price
myWings.halfPrice()

# Print the wings flavor
print('Wings flavor: %s' % myWings.flavor)

# Print the wings price, based on the quantity (and half-price)
print('Wings price: %s' % myWings.getPrice(myWings.quantity))

##################################
# DRIVER CODE - Order
##################################
# Create an order object
myOrder = Order('Kyle')

# Print the order id
print('Order ID: %s' % myOrder.orderId)

# Add the pizza object to the order object's orderItems list
myPizza.addToOrder(myOrder)

# Print out the items and prices in the orderItems list
for item in myOrder.orderItems:
    print('Order Item: %s' % item.name)
    print('Price: %s' % item.getPrice(item.size))
