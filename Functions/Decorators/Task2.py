import time


def log(fn):
    from time import time
    f = open("log.txt", "w")

    def wrapper(*args, **kwargs):
        args_names = fn.__code__.co_varnames[:fn.__code__.co_argcount]
        start = time()
        time_used = time() - start
        execution_time = time_used
        fn(*args, **kwargs)
        args_field = "args: "
        for i in range(len(args)):
            args_field += f"{args_names[i]}={args[i]}, "
        args_field = args_field[:-2]
        args_field+="; "
        print(args_names)
        print(len(args))
        if len(kwargs) != 0:
            kwargs_field = "kwargs: "
            for key, val in kwargs.items():
                kwargs_field += f"{key}={val}, "
            kwargs_field = kwargs_field[:-2]
            kwargs_field += "; "
            args_field += kwargs_field
        f.write(
            f'{fn.__name__}; {args_field[:-2]}; execution time: {execution_time} sec')
        return fn(*args, **kwargs)
    return wrapper


@log
def foo(a, b, c):
    return a, b, c


print(foo(1, 2, c=3))
