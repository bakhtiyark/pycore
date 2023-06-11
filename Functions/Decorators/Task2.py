import time

def log(fn):
    from time import time
    f = open("log.txt", "w")
    def wrapper(*args, **kwargs):
        start = time()
        time_used = time() - start
        execution_time = time_used
        fn(*args, **kwargs)
        f.write(f'{fn.__name__}; args: {args}; kwargs: {kwargs}; execution time: {execution_time} sec')
        return fn(*args, **kwargs)
    return wrapper

@log
def foo(a, b, c):
    return a,b,c

print(foo(1, 2, c=3))