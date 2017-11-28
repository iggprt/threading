import threading
import time

print_lock = threading.Lock()

def work(i):
	with print_lock:
		print "thread " + str(i) + " is working on"
	time.sleep(1)

for i in range(10):
	thread = threading.Thread(target = work, args=(i,))
	thread.daemon = True
	thread.start()
