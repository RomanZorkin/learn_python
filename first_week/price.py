"""Tasks of the first week."""
from typing import Any


# exercise 1 functions
def get_summ(one: Any, two: Any, delimeter: str = '&') -> str:
    """The function combines the arguments into a single line.

    Args:
        one (Any): first argument
        two (Any): second argument
        delimeter (str): line separator

    Returns:
        str: Combined string
    """
    return f'{one}{delimeter}{two}'


answer = get_summ('Learn', 'Python')
print(answer.upper())


# exercise 2 functions
def format_price(price: Any) -> int:
    """The function gives an argument to an integer and returns it.

    Args:
         price (Any): the value we want to convert to an integer

    Returns:
        int: integer value
    """
    if isinstance(price, int | float):
        return int(price)
    elif price.isdigit():
        return int(price)
    return int(float(price))


for num in (56.24, 1, 3.5, '3', '3.5'):
    print(format_price(num))
