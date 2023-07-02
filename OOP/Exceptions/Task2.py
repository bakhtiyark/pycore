from typing import Union


def divide(str_with_ints: str) -> Union[float, str]:
    try:
        intermediate = str_with_ints.split()
        return int(intermediate[0])/int(intermediate[1])
    except ValueError as a:
          return f"Error code: {a}"
    except ZeroDivisionError:
          return "Error code: division by zero"
    
print(divide("1 2"))
print(divide("1 0"))
print(divide("* 2"))
print(divide("ddad 2"))
print(divide("4 *"))
print(divide("4 %"))
