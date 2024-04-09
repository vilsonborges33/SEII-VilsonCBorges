import threading
import time

start = time.perf_counter()

def do_something(seconds):
    print(f"Sleeping {seconds} second...")
    time.sleep(seconds)
    print("Done Sleeping...")

#do_something()
#do_something()

#t1 = threading.Thread(target= do_something)
#t2 = threading.Thread(target= do_something)

#t1.start()
#t2.start()
#t1.join()
#t2.join()

threads = []

for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()
print(f"Finished in {round(finish-start, 2)} seconds")



import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f"Sleeping {seconds} second...")
    time.sleep(seconds)
    return "Done Sleeping..."

#do_something()
#do_something()

#t1 = threading.Thread(target= do_something)
#t2 = threading.Thread(target= do_something)

#t1.start()
#t2.start()
#t1.join()
#t2.join()

with concurrent.futures.ThreadPoolExecutor() as executor:
     results = [executor.submit(do_something, 1) for _ in range(10)]

     for f in concurrent.futures.as_completed(results):
         print(f.result())

#    f1 = executor.submit(do_something, 1)
#    f2 = executor.submit(do_something, 1)
    #print(f1.result())
    #print(f2.result())

#threads = []

#for _ in range(10):
#    t = threading.Thread(target=do_something, args=[1.5])
#    t.start()
#    threads.append(t)

#for thread in threads:
#    thread.join()

finish = time.perf_counter()
print(f"Finished in {round(finish-start, 2)} seconds")




start = time.perf_counter()

def do_something(seconds):
    print(f"Sleeping {seconds} second...")
    time.sleep(seconds)
    return f"Done Sleeping...{seconds}"


with concurrent.futures.ThreadPoolExecutor() as executor:
     secs = [5, 4, 3, 2, 1]
     results = executor.map(do_something, secs)

     for result in results:
         print(result)


finish = time.perf_counter()
print(f"Finished in {round(finish-start, 2)} seconds")






start = time.perf_counter()

def do_something(seconds):
    print(f"Sleeping {seconds} second...")
    time.sleep(seconds)
    return f"Done Sleeping...{seconds}"


with concurrent.futures.ThreadPoolExecutor() as executor:
     secs = [5, 4, 3, 2, 1]
     results = [executor.submit(do_something, sec) for sec in secs ]

     for f in concurrent.futures.as_completed(results):
         print(f.result())


finish = time.perf_counter()
print(f"Finished in {round(finish-start, 2)} seconds")