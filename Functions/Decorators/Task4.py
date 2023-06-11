"""
Decorators Factory
Create a decorator factory (decorator itself). The factory accepts a function (lambda) as an input and returns a decorator that will return the result of the function as the first argument. The result of the decorated function is passed. The function that the factory accepts (in the example below, it is a lambda) can only take one positional parameter.

For example:

>>> @decorator_apply(lambda user_id: user_id + 1)
>>> def return_user_id(num: int): 
        return num
>>> return_user_id(42) 
>>> 43
"""

def decorator_apply(*args):
    def wrapper(fn):
        print(args)
        result = int(fn(args+1))
        return result
    return wrapper

@decorator_apply(lambda user_id: user_id + 1)
def return_user_id(num: int): 
        return num
print(return_user_id(42))
