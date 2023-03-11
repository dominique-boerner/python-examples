# Variables stores values of different types. Python itself is loose typed, like e. g. JavaScript.
# In python, the data types can be set implicitly or explicitly:

# Implicit data typing:

car = "Audi"; # python knows, this is a string
age = 12      # python knows, this is an integer
speed = 30.0  # python knows, this is a float
works = True; # python knows, this is a boolean

# Explicit data typing:
# (this is only used by typing libraries like "mypy" or different IDEs)

car: str = "Audi";
age: int = 12;
speed: float = 30.0;
works: bool = True;

# You can use variables to store values and use them in your code:

name = "Max";
age = 23;
print(f"Hello {name}! You are {age} years old? What a nice age to life!");

# In programming, we have the concept of "constants", which are variables which are only defined ONCE.
# These constants are written in UPPER_CASE, which is a convention trough many programming languages:

PI = 3.1415;
print(f"PI is {PI}");