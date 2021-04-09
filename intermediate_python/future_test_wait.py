# Concurrency: 동시성
# asynchronous: 비동기
# 지연시간(Block) CPU 및 리소스 낭비 방지: I/O 관련 작업에서 동시성 활용 권장

from future import WORK_LIST
import os
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait, as_completed


def main():
    start_time = time.time()
    
    WORK_LIST = [3, 6.5]
    
    future_list = list()
    with ProcessPoolExecutor() as executor:
        for work in WORK_LIST:
            future = executor.submit(time.sleep, work)
            # scheduling
            future_list.append(future)
            print(f'Scheduled for {work} : {future}')
            print()
              
        result = wait(future_list, timeout=5, return_when='ALL_COMPLETED')
        
        print(f'Completed Tasks: {str(result.done)}')  # 성공
        if result.not_done:
            raise TimeoutError('Time OUT!')
        # print(f'Pending ones after waiting for 5 seconds: {str(result.not_done)}')  # 실패
        end_time1 = time.time() - start_time
    
        msg = f'Time: {end_time1:.4f}'
        print(msg)
        # print(f'Result: {[future.result() for future in result.done]}')  # 결과값
    
    end_time2 = time.time() - start_time
    
    msg = f'Time: {end_time2:.4f}'
    
    print(msg)


if __name__ == '__main__':
    main()
    
    
    
    
    
     
