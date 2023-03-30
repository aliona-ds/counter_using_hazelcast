# Пункт 5 завдання
import hazelcast
from threading import Thread
import time    

def counter_function():
    for i in range(10000):
        distributed_map.lock(key)
        try:
            counter = distributed_map.get(key)
            distributed_map.put(key, counter + 1)
        finally:
            distributed_map.unlock(key)

key = "counter"

# Connect to Hazelcast cluster.
client = hazelcast.HazelcastClient()
# Get or create the "distributed-map" on the cluster.
distributed_map = client.get_map("pessimistic-locking-map").blocking()
distributed_map.put(key, 0)

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

get_future = distributed_map.get(key)
print('Result counter is ', get_future)
print('Counter running time = ' + str(t) + ' seconds')

# Shutdown the client.
client.shutdown()
