import math
import numpy as np
def split_num(total, part_size):
    group_num = math.ceil(total / part_size)
    parts = np.full(group_num, part_size)
    parts[-1] = total - part_size * (group_num - 1)
    return parts.tolist()

def timer(fn):
    from time import perf_counter
    
    def inner(*args, **kwargs):
        start_time = perf_counter()
        to_execute = fn(*args, **kwargs)
        end_time = perf_counter()
        execution_time = end_time - start_time
        print('{0} took {1:.8f}s to execute'.format(fn.__name__, execution_time))
        return execution_time
    
    return inner