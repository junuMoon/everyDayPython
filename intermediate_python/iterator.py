# nums = [1, 2, 3]

# i_nums = iter(nums) # remove ugly dunder method

# while True:
#     try:
#         item = next(i_nums)
#         print(item)
#     except StopIteration:
#         break


from typing import Generator


class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current
    
nums = MyRange(1, 10)
# print(next(nums))


def my_range(start):
    current = start
    while True:
        yield current
        current += 1
        
nums = my_range(1, 10)
# print(next(nums))
# iterator: object with a state so that where it's at during its iteration.