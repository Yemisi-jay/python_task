
class Vehicle:
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def start(self):
        print(self.color, self.model)

class Car(Vehicle):
    def __init__(self, color, model,num_wheels):
        Vehicle.__init__(self, color, model)
        self.num_wheels = num_wheels
        
    def start(self):
        print("Starting Car", self.color, self. model, self.num_wheels)

class Motorcycle(Vehicle):
    def __init__(self,color,model, num_wheels):
        Vehicle.__init__(self, color, model)
        self.num_wheels = num_wheels

    def start(self):
        print('Starting motorcycle')

x = Car('Blue','Toyota', 4)
x.start()


x = Motorcycle('Black','Bajaj', 2)
x.start()


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        print("Area of a rectangle: ", self.width * self.height)

class Square(Rectangle):
    def __init__(self, width, height):
       super().__init__(width, height)
       self.side_lenght = 8

    def area(self):
        print("Area of a square:", self.width * self.height * self.side_lenght)

x = Rectangle(4, 8)
x.area()

x = Square(5, 7)
x.area()
        
        
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound():
        print(self.sound)

class Dog(Animal):
    def __init__(self, name, sound):
        super().__init__(name, sound)
        self.breed = "caucasian"

    def make_sound(self):
        print(self.sound)

class Cat(Animal):
    def __init__(self, name, sound):
        super().__init__(name, sound)
        self.color = "white"

    def make_sound(self):
        print(self.sound)

x = Dog('Jack', 'bark')
x.make_sound()

x = Cat('billy', 'meow')
x.make_sound()
        
        
        

    
