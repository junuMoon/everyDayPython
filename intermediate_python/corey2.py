# Decorator practice
from functools import wraps


def my_logger(orig_func):
    import logging
    logging.basicConfig(filename=f'{orig_func.__name__}.log', level=logging.INFO)
    
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            f'{orig_func.__name__} function ran with args: {args} and {kwargs}'
        )
        return orig_func(*args, **kwargs)
    
    return wrapper

def my_timer(orig_func):
    import time
    
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f'{orig_func.__name__} ran in {t2} sec')
        return result
    
    return wrapper


import time


@my_timer
@my_logger
def display_info(name=1, age=1):
    time.sleep(1)
    print(f'display_info ran with arguments ({name}, {age})')
    
# display_info1 = my_timer(display_info)
# print(display_info1.__name__)  # wraps is functools.partial function

display_info('Mei', 23)

    