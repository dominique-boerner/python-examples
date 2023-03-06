from constants.Brand import Brand;
from constants.Color import Color;

class Car:
    color = Color.UNKNOWN;
    brand = Brand.UNKNOWN;

    def __str__(self):
        return f'i am a {self.brand} car with a {self.color} color.';