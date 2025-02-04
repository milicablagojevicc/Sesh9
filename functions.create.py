def greet():
    """ A simple function that prints hello
    :return: None
    """
    print("Hello!")

def greet2(name):
    print(f"Hello {name}")
greet2("James")
greet2("Bob")

def average(a, b):
    """
    Average the two numbers
    :param a: first number
    :param b: second number
    :return: the average of the two numbers, a and b
    """
    average = (a + b) / 2
    return average
x = average(10,14)
print(x)

def divide(x, y):
    """
    Divide x by y
    :param x: first number
    :param y: second number
    :return: float, the div result
    """
    if y == 0:
        return None
    return x / y
print(divide(10, 20))
z = divide(10, 20)
print(z)

def bond(first_name, last_name):
    return f"{last_name}, {first_name} {last_name}"
print(bond("James", "Smith"))

def introduce(name):
    print(f"The name is {name}")

print(bond("James", "Smith"))
introduce(bond("James", "Smith"))
introduce(bond())
print(introduce(bond()))