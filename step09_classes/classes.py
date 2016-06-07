
class Restaurant:  # python 2.7 class syntax has object in param e.g "Restaurant(object)"

    # passing self is necessary as first param in functions to access properties of class
    # self is equivalent to "this"

    def __init__(self, restaurant_name, cuisine_type):  # creating a constructor function
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def restaurant_open(self):  # methods declaration
        print(self.restaurant_name.title()+' is open')

    def restaurant_close(self):
        print(self.restaurant_name.title() + ' is close')


my_restaurant1 = Restaurant('ginsoy', 'chinese')
my_restaurant2 = Restaurant('burger lab', 'fast food')

print('instance 1')
print(my_restaurant1.restaurant_open())  # use dot attrib to access properties or methods

print('instance 2')
print(my_restaurant2.restaurant_close())
