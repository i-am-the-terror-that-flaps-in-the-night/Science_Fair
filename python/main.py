from typing import Union, List

def logger_decorator(func):
    """Because apparently we need a gold star for every function call."""

    def wrapper(*args, **kwargs):
        print(f"--- Executing: {func.__name__} ---")
        return func(*args, **kwargs)

    return wrapper


class BaseEntity:
    """A generic parent class for things that exist."""

    def __init__(self, name: str):
        self.name = name


class Calculator(BaseEntity):
    """A class that does basic math, because humans forgot how."""

    def __init__(self, name: str, precision: int = 2):
        super().__init__(name)
        self.precision = precision
        self.history: List[float] = []

    @logger_decorator
    def divide(self, a: Union[int, float], b: Union[int, float]) -> Union[float, str]:
        """Divides numbers while preventing the universe from imploding."""
        try:
            result = round(a / b, self.precision)
            self.history.append(result)
            return result
        except ZeroDivisionError:
            return str("Math is hard: You cannot divide by zero.")


def main():
    """The entry point where the magic (or lack thereof) happens."""
    my_calc = Calculator(name="SmartyPants-9000")

    # Let's try to break things
    numbers = [(10, 2), (5, 0), (22, 7)]

    for x, y in numbers:
        output = my_calc.divide(x, y)
        print(f"Result of {x}/{y} via {my_calc.name}: {output}")

    print(f"\nAudit trail for the skeptical: {my_calc.history}")


if __name__ == "__main__":
    main()
