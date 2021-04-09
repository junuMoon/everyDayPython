# Thread: OS 관리
# CPU 코어에서 실시간/시분할 비동기 작업 -> multithread
# Coroutine: 단일(싱글) 쓰레드, 스택을 기반으로 동작하는 비동기 작업
# yield: 메인 <-> 서브
# 코루틴 제어, 상태, 양방향 전송

def coroutine1():
    print('>>> coroutine start.')
    i = yield
    print(f'>>> coroutine received: {i}.')
    yield 'finished'

# Main Routine
# generator declaration
# cr1 = coroutine1()
# # print(cr1)

# next(cr1)
# # next(cr1) # send(None)
# cr1.send(100)
# next(cr1)

# GEN_CREATED -> GEN_RUNNING -> GEN_SUSPENDED -> GEN_CLOSED

def coroutine2(x):
    print(f'>>> coroutine started: {x}')
    y = yield x
    print(f'>>> coroutine received: {y}')
    z = yield x + y
    print(f'>>> coroutine received: {z}')
    
cr3 = coroutine2(10)

from inspect import getgeneratorstate

# print(getgeneratorstate(cr3))
# print(f'first step: {next(cr3)}')
# print(getgeneratorstate(cr3))
# print(f'second step: {cr3.send(100)}')
# print(getgeneratorstate(cr3))
# cr3.send(100)
# print(getgeneratorstate(cr3))

def generator1():
    for x in 'AB':
        yield x
    for y in range(1, 4):
        yield y
        
t1 = generator1()
# print(next(t1))
t2 = list(generator1())
# print(t2)

def generator2():
    yield from 'AB'
    yield from range(1, 4)
    
t3 = generator2()
t4 = list(generator2())
print(t4)

    