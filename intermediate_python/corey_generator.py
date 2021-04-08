def square_numbers(nums):
    for i in nums:
        yield i*i
        
nums_squared = square_numbers([1, 2, 3, 4, 5])

nums_squared2 = (x*x for x in range(1, 6))



        