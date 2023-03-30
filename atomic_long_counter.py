# Пункт 7 завдання
import hazelcast
from threading import Thread
import time    

def counter_function():
    for i in range(10000):
    	counter.increment_and_get()
    	
hazelcastInstance = hazelcast.HazelcastClient()
counter = hazelcastInstance.cp_subsystem.get_atomic_long('iatomaclong-counter')

thr_list = []
t = time.time()
for i in range(10):
    thr = Thread(target=counter_function)
    thr_list.append(thr)
    thr.start()
    print('Thread ' + str(i) + ' started')
for i in thr_list:
    i.join()
    print('Thread ' + str(i) + ' finished')
t = time.time() - t

get_future = counter.get().result()
print('Result counter is ', get_future)
print('Counter running time = ' + str(t) + ' seconds')

# Shutdown the client.
hazelcastInstance.shutdown()
