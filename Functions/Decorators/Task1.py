from typing import Dict
import time
execution_time: Dict[str, float] = {}


def time_decorator(fn):
    from time import time
    def time_elapsed(*args):
        start = time()
        result = fn(*args)
        time_used = time() - start
        execution_time[fn.__name__] = time_used
        return result
    return time_elapsed


@time_decorator
def func_add(a, b):
    time.sleep(0.2)
    return a + b

func_add(10, 20)
#30

print(execution_time)
#0.212341254
