class Car:
    brand = "unknown";

    def __init__(self, brand):
        self.brand = brand;

    def drive(self):
        print("brumm brumm!");

    def get_brand(self):
        print(self.brand);


class Audi(Car):
    def __init__(self):
        self.brand = "Audi";
        print("new Audi!")



car = Audi();
car.drive();
car.get_brand();
