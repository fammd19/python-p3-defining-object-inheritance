class Vehicle:
    #this is the parent or superclass
    def __init__(self, wheel_size, wheel_number):
        self.wheel_size = wheel_size
        self.wheel_number = wheel_number

    def go(self):
        return "vrrrrrrrooom!"

    def fill_up_tank(self):
        return "filling up!"


class Car(Vehicle):
    #this is the subclass or child
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"