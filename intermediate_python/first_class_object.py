# 일급함수 (일급 객체)
# 1. 런타임 초기화
# 2. 함수에 변수 할당 가능
# 3. 함수를 인수로 전달 가능
# 4. 함수 결과 반환 가능(return)

def factorial(n):
    '''Factorial Function -> n: int'''
    if n == 1:
        return 1
    return n * factorial(n-1)

class A:
    pass

# print(factorial(5))
# print(factorial.__doc__)
# print(type(factorial), type(A))
# print(set(sorted(dir(factorial))) - set(sorted(dir(A))))
# print(factorial.__name__)
# print(factorial.__code__)
# print(factorial.__call__)

# assign variables: 함수를 인수로 전달
var_func = factorial

# print(var_func)
# print(var_func(10))
# print(list(map(var_func, range(1, 11))))

# 함수 인수 전달 및 함수로 결과 변환 -> 고위 함수
# map, filter, reduce
# javascript ES6
# print([var_func(i) for i in range(1, 6) if i % 2])
# print(list(map(var_func, filter(lambda x: x % 2, range(1, 6)))))

# from functools import reduce
# from operator import add

# print(sum(range(1, 11)))
# print(reduce(add, range(1, 11)))
# print(reduce(lambda x, t: x + t, range(1, 11))) 
# 익명함수: lambda 가급적 주석을 꼭 작성해라 일반 함수형태로 리팩토링을 권장

# Callable: 호출 연산자 -> 메소드 형태로 호출 가능한지 확인
# __call__ attribute makes function callable

# print(callable(str))
# print(str('a'))
# print(callable(str('a')))
# print(type(str('a')))
# print(callable(str('a').__add__))
# print(type(str('a').__add__))

print(callable(str), callable(list), callable(var_func), callable(3.14))

# partial: 인수 고정 -> callback function
from operator import mul
from functools import partial

print(mul(10, 10))

# 인수 고정
five = partial(mul, 5)
print(five(5))

six = partial(five, 6)
print(six()) # 30
# print(six(10)) # mul expected 2 arguments, got 3
print([five(i) for i in range(1, 11)])
print(list(map(five, range(1, 11))))