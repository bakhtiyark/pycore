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

def print_function_info(should_count=False): 
    count = 0 
    def wrapper_func(func): 
        def wrapper(*args, **kwargs): 
            if should_count: 
                nonlocal count 
                count += 1
                print(f"Function was called {count} times") 
                print(f"Calling function {func} with args: {args} and kwargs: {kwargs}") 
                return func(*args, **kwargs) 
            return wrapper 
        return wrapper_func 

@print_function_info
def lala(*args, **kwargs):
    print(args)
    print(kwargs)
    print(1)

print(lala(("d","a","a")))