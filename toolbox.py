def add(x, y):
    """Return the sum of x and y."""
    return x + y


def subtract(x, y):
    """Return the difference of x and y."""
    return x - y


def multiply(x, y):
    """Return the product of x and y."""
    return x * y


def divide(x, y):
    """Return the quotient of x divided by y."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y


def greet(name):
    """Return a friendly greeting for the provided name."""
    return f"Hello, {name}! Welcome to PLP Python Week 4."
