class calculator:
    """
    A simple calculator class to perform basic arithmetic operations.
    Methods
    -------
    add(x, y)
        Returns the sum of x and y.
    subtract(x, y)
        Returns the difference between x and y.
    multiply(x, y)
        Returns the product of x and y.
    divide(x, y)
        Returns the quotient of x and y.
    power(x, y)
        Returns x raised to the power of y.
    """
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ZeroDivisionError("division by zero")
        return x / y

    def power(self, x, y):
        return x ** y