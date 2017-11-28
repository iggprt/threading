import threading 
import Queue 
import time

print_lock = threading.Lock()
q = Queue.Queue()

def exampleJob(worker):
	time.sleep(0.5)
	
	with print_lock:
		print(threading.current_thread().name,worker)


def threaderr():
	while True:
		w = q.get()
		exampleJob(w)
		q.task_done()
		
for _ in range (10):
	t = threading.Thread (target = threaderr)
	t.daemon = True
	t.start()
	
start = time.time()

for worker in range (20):
	q.put(worker)
q.join()

print ('entire job took: ',time.time()-start)