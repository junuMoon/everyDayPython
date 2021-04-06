# Closure

# scope of a variable in Python
# b = 20
# b = 30
# def func_v1(a):
#     global b
#     print(a)
#     print('local:', b)
#     b = 40

# print('global:', b)    
# func_v1(10)
# print(b)

# Closure: a function object that remembers values in enclosing scopes even if they are not present in memory.
# Concurrency control in server programming is important because of situations where several resource access to same memory place like Dead lock
# 메모리를 공유하지 않고 메시지 전달로 처리하고자 함 -> 클로저
# 공유하되 변경되지 않는(Immutable, Read Only)
# 불변자료구조 및 atom, STM -> 멀티스레드(Co-routine) 프로그래밍에 강점

# a = 100

# print(a+100)
# print(a+1000)

# # 결과 누적
# print(sum(range(1, 51)))

# class Averager():
#     def __init__(self):
#         self._series = []
        
#     def __call__(self, v):
#         self._series.append(v)
#         print(f'inner >> {self._series} / {len(self._series)}')
#         return sum(self._series) / len(self._series)
    

# averager_cls = Averager()
# # print(dir(averager_cls))
# print(averager_cls(10))
# print(averager_cls(30))
# print(averager_cls(50))
# print(averager_cls(3)) # 함수는 종료되었지만 내부에 기억되고 있음

# 외부에서 호출된 함수의 변수값, 상태(레퍼런스) 복사 후 저장 -> 후에 액세스 가능

def closure_ex1():
    # Free variable 
    series = []
    series2 = []
    def averager(v):
        series.append(v)
        series2.append(v+1)
        print(f'inner >> {series} / {len(series)}')
        return sum(series) / len(series)
    return averager

avg_closure1 = closure_ex1()
# print(avg_closure1(10))
# print(avg_closure1(30))
# print(avg_closure1(50))
# print(dir(avg_closure1))
# print(avg_closure1.__annotations__)
# print(dir(avg_closure1.__code__))
# print(avg_closure1.__code__.co_freevars)
# print(dir(avg_closure1.__closure__))
# print(avg_closure1.__closure__[0].cell_contents)
# print(avg_closure1.__closure__[1].cell_contents)

# wrong closure example
def closure_ex2():
    # Free variables
    cnt = 0
    total = 0
    def averager(v):
        cnt += 1
        total += v
        return total / cnt
    return averager

avg_closure2 = closure_ex2()
# print(avg_closure2(10))

def closure_ex3():
    # Free variables
    cnt = 0
    total = 0
    def averager(v):
        nonlocal cnt, total
        cnt += 1
        total += v
        return total / cnt
    return averager

avg_closure3 = closure_ex3()

print(avg_closure3(15))
print(avg_closure3(32))
print(avg_closure3(20))