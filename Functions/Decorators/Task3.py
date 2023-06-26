"""
Functions. Decorators. Decorators. Task 3.
Create decorator validate, which validates arguments in the set_pixel function. All function parameters should be between 0(int) and 256(int) inclusive.

If all parameters are valid, the set_pixel function should return a "Pixel created!" message. Otherwise, it should return the "Function call is not valid!" message.

Use functools.wraps where necessary.

Don't forget about doc strings.

Examples

>>> set_pixel(0, 127, 300)
Function call is not valid!
>>> set_pixel(0,127,250)
Pixel created!
"""

def validate(fn):
    def wrapper(*args):
        intermediate = []
        for i in args:
           if (0 <= i <= 256):
              intermediate.append(i)              
        if (len(intermediate) == len(args)):
              return fn(*args)
        else:
            return "Function call is not valid!"
        
    return wrapper
    
@validate
def set_pixel(x: int, y: int, z: int) -> str:
  return "Pixel created!"


print(set_pixel(0, 127, 300))
print(set_pixel(0, 127, 250))