# Пункт 4 завдання
import hazelcast
from threading import Thread
import time

def counter_function():
    for i in range(10000):
        counter = distributed_map.get("counter")
        distributed_map.put('counter', counter + 1)

# Connect to Hazelcast cluster.
client = hazelcast.HazelcastClient()
# Get or create the "distributed-map" on the cluster.
distributed_map = client.get_map("locking-map").blocking()
distributed_map.put("counter", 0)

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

get_future = distributed_map.get("counter")
print('Result counter is ', get_future)
print('Counter running time = ' + str(t) + ' seconds')

# Shutdown the client.
client.shutdown()
