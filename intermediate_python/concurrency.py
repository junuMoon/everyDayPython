# 병행성: Concurrency
# Generator: a function that returns an iterator(iterable object)

# Iterable object: collections, str, list, dict, set, tuple, *args

t = 'ABCDEFG'

# print(dir(t))  __iter__

# for c in t:
#     print(c)

# print(t.__iter__().__next__().__iter__().__next__())
# print(dir(t.__iter__().__next__()))

# w = iter(t)

# while True:
#     try:
#         # print(next(w))
#     except StopIteration:
#         break
    
# print()

# is it iterable?
# print(hasattr(t, '__iter__'))

from collections import abc # Abstract Base Classes for Containers¶
# print(isinstance(t, abc.Iterable)) # hasable, iterable, callable


class WordSplitter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')
        
    def __next__(self):
        # print('Called __next__')
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration('No left iterable object')
        self._idx += 1
        return word
    
    def __repr__(self):
        return f"Split words -> {self._text}"
        
        
# w1 = WordSplitter('You used to be much more... "muchier." You\'ve lost your muchness')
# print(w1)
# print(next(w1))
# print(next(w1))
# print(next(w1))
# print(next(w1))
# print(w1._idx)

# Generator
# 1. 지능형 리스트, 딕셔너리, 집합: 데이터 양 증가 후 메모리 사용량 증가 -> 제네레이터 사용 권장
# 2. 단위 실행 가능한 코루틴(Coroutine) 구현과 연동
# 3. 작은 메모리 조각 사용

class WordSplitGenerator:
    def __init__(self, text):
        self._text = text.split(' ')
        
    def __iter__(self):
        for word in self._text:
            yield word # generator
        return 
    
    def __repr__(self):
        return f'Word Split Generator: {self._text}'
    
wg = WordSplitGenerator('You used to be much more... "muchier." You\'ve lost your muchness')
print(wg)
wt = iter(wg)
print(wt)
print('----')
print(type(next(wt)))
print(type(wt))
# print(next(wt))
# print(next(wt))
# print(next(wt))
# print(next(wt))
# print(next(wt))
# print(next(wt))
# print(next(wt))
# print(next(wt))
# print(next(wt))
# print(next(wt))

        