# create a base class - car
class Car:
    brand = "unknown";
    wheels = [];

    def __init__(self, brand):
        self.brand = brand;

    def drive(self):
        print("brumm brumm!");

    def get_brand(self):
        print(self.brand);

    def get_wheels_count(self):
        print(len(self.wheels));

# you can use classes for e.g. categorization!
class WheelPosition:
    FRONT_LEFT = "front_left";
    FRONT_RIGHT = "front_right";
    BACK_LEFT = "back_left";
    BACK_RIGHT = "back_right";
    UNKNOWN = "unknown";

# parts of the car can also be classes!
class Wheel:
    brand = "unknown";
    size = "unknown";
    wheel_position = WheelPosition.UNKNOWN;

    def __init__(self, brand, size, wheel_position):
        self.brand = brand;
        self.size = size;
        self.wheel_position = wheel_position;
    
    def get_brand(self):
        print(self.brand);

    def get_size(self):
        print(self.size);

# we create a car - audi
class Audi(Car):
    def __init__(self):
        self.brand = "Audi";
        self.add_wheels();
        print("new Audi!")

    def add_wheels(self):
        self.wheels.append(Wheel("Kansei Astro", "28/32", WheelPosition.FRONT_LEFT));
        self.wheels.append(Wheel("Kansei Astro", "28/32", WheelPosition.FRONT_RIGHT));
        self.wheels.append(Wheel("Kansei Astro", "28/32", WheelPosition.BACK_LEFT));
        self.wheels.append(Wheel("Kansei Astro", "28/32", WheelPosition.BACK_RIGHT));

audi = Audi();
audi.drive();
audi.get_brand();
audi.get_wheels_count();
