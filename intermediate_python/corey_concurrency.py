# running synchronously - CPU bound
# IO bound: input ouput bound
import time
import threading
import concurrent.futures


start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} seconds...')
    time.sleep(seconds)
    return f'Done Sleeping... {seconds}'
    
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [1, 1, 4, 2, 3]
    results = executor.map(do_something, secs)
    
    for result in results:
        print(result)
    
    # results = [executor.submit(do_something, sec) for sec in secs]
    
    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())
        
    
# threads = []

# for _ in range(10):
#     t = threading.Thread(target=do_something, args=[1.5])
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} seconds')



