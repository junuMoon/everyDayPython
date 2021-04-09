# Concurrency: 동시성
# asynchronous: 비동기
# 지연시간(Block) CPU 및 리소스 낭비 방지: I/O 관련 작업에서 동시성 활용 권장

import os
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait, as_completed, TimeoutError
import concurrent.futures

WORK_LIST = [100000, 10000000, 100000000, 100000000]

def sum_generator(n):
    return sum(n for n in range(1, n+1))

def main():
    # Worker Count
    worker = min(10, len(WORK_LIST))
    
    start_time = time.time()
    
    future_list = list()
    with ThreadPoolExecutor() as executor:
    # with ProcessPoolExecutor(max_workers=worker) as executor:
        # result = executor.map(sum_generator, WORK_LIST)
        for work in WORK_LIST:
            future = executor.submit(sum_generator, work)
            # scheduling
            future_list.append(future)
            print(f'Scheduled for {work} : {future}')
            print()
            
        # result = wait(future_list, timeout=7)
        # print(f'Completed Tasks: {str(result.done)}')  # 성공
        # print(f'Pending ones after waiting for 7 seconds: {str(result.not_done)}')  # 실패
        # print(f'Result: {[future.result() for future in result.done]}')  # 결과값
        
        try:
            for future in as_completed(future_list, timeout=4):
                result = future.result()
                done = future.done()
                print(f'Done: {done} / Result: {result}')
        except TimeoutError:
            print('Request to server time out')
            
    
    end_time = time.time() - start_time
    
    msg = f'Time: {end_time:.4f}'
    
    print(msg)


if __name__ == '__main__':
    main()
    
    
    
    
    
     
