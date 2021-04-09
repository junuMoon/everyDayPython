# 병행성(Concurrency): 한 컴퓨터가 여러 일을 동시에 수행, 단일 프로그램에서 여러 일을 쉽게 해결
# 병렬성(Parallelism): 여러 컴퓨터가 여러 일을 동시에 수행, 높은 수행 속도 ex) crawler

def generator_ex1():
    print('Start')
    yield 'Point A'
    print('Continue')
    yield 'Point B'
    print('End')

temp = iter(generator_ex1())
# print(next(temp))

# for v in generator_ex1():
#     print(v)
    
# temp2 = [x * 3 for x in generator_ex1()]
# temp3 = (x * 3 for x in generator_ex1())
# print(temp2)
# print(temp3)

# for i in temp3:
    # print(i)

import itertools
# count, takewhile, filterfalse, accumulate, chain, product, groupby
gen1 = itertools.count(1, 2.5)

gen2 = itertools.takewhile(lambda n: n < 10, gen1)

gen3 = itertools.filterfalse(lambda n: n < 3, [i for i in range(5)])
gen4 = filter(lambda n: n < 3, [i for i in range(5)])

gen5 = itertools.accumulate([x for x in range(1, 10)])
    
gen6 = itertools.chain('ABCDE', range(1, 11, 2))
gen7 = itertools.chain(enumerate('ABCDE'))
gen8 = itertools.chain(zip(range(1, 11, 2), 'ABCDE'))

gen9 = itertools.product('ABCDE', range(3)) # (A, 0), (A, 1), (A, 2) ...
gen10 = itertools.product('ABCDE', repeat=4) # (A, A), (A, B), (A, C) ... / 경우의 수

gen11 = itertools.groupby('AAABBCCCCCDD')
# for chr, group in gen11:
#     print(chr, ' : ', list(group))


for v in gen11:
    print(v)
