class Animal:

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def walk(self):
        print(self.name+' is walking')

    def eat(self):
        print(self.name+' is eating')


class Snake(Animal):  # creating a child class using inheritance

    def __init__(self, name, color):
        super().__init__(name, color)  # making connection with parent class

    def walk(self):
        print(self.name+' is slithering')


my_snake = Snake('Python', 'yellow')

my_snake.walk()  # called from child class
my_snake.eat()  # called from parent class
