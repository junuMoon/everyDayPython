# closure

# import logging
# logging.basicConfig(filename='example.log', level=logging.INFO)

# def logger(func):
#     def log_func(*args):
#         logging.info(f'Running {func.__name__} with arguments {args}')
#         print(func(*args))
#     return log_func

# def add(x ,y):
#     return x+y

# def sub(x, y):
#     return x-y

# add_logger = logger(add)
# sub_logger = logger(sub)

# a = add_logger(3, 3)
# add_logger(4, 5)
# sub_logger(10 ,5)
# sub_logger(4, 2)

# print(a)  # none

# Decorator
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f'wrapper executed this before {original_function.__name__}')
        return original_function(*args, **kwargs)
    result = wrapper_function
    return result


# class decorator_class(object):
#     def __init__(self, original_function):
#         self.original_function = original_function
        
#     def __call__(self, *args, **kwargs):
#         print(f'call method executed this before {self.original_function.__name__} function')
#         return self.original_function(*args, **kwargs)


@decorator_function
def display():
    print('display function ran')

# decorated_display = decorator_function(display)
# print(decorated_display)
# decorated_display()

display()

@decorator_function
def display_info(name, age):
    print(f'display_info ran with arguments ({name}, {age})')
    
display_info('John', 30)





