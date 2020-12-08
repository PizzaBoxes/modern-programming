
""""Example of classes and objects, attriutes, calling."""

class Restaurant():
    """A simple restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes for a restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    #def describe_restaurant(self):
        """Printing the name and type"""
    #    print"My restaurant is called", self.restaurant_name.title() + "."

    #def restaurant_type(self):
        """Printing the type"""
    #    print"The restaurant serves", self.cuisine_type + " type of cuisine."

    #def open_restaurant(self):
        """Print a message indicating the restaurant is open"""
    #    print self.restaurant_name.title() + " is currently open."

"""Change the names and type of cuisine vv"""

my_restaurant = Restaurant('the federal', 'french')
restaurant = Restaurant('panda express', 'chinese')

print"My restaurant is called", my_restaurant.restaurant_name.title() + "."
print"The restaurant serves", my_restaurant.cuisine_type.title() + " type of cuisine."
print my_restaurant.restaurant_name.title() + " is currently open."
print(" \n")
print"My restaurant is called", restaurant.restaurant_name.title() + "."
print"The restaurant serves", restaurant.cuisine_type.title() + " type of cuisine."
print restaurant.restaurant_name.title() + " is currently open."

# __update = update  # private copy of original update() method

# getattr()

# setattr()