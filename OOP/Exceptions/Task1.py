def decorator_apply(fn):
    def wrapper(f):
        def dw(x, /):
            return f(fn(x))
        return dw
    return wrapper


@decorator_apply(lambda user_id: user_id + 1)
def return_user_id(num: int):
    return num

print(return_user_id(42))