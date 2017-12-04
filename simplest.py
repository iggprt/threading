import threading
import time
"""
print_lock = threading.Lock()
def work(i):
	
	with print_lock:
		print "thread " + str(i) + " is working on+"
	with print_lock:
		print "work" + str(i)+ "is done"
	time.sleep(1)
for i in range(10):
	thread = threading.Thread(target = work, args=(i,))
	thread.daemon = True
	thread.start()
with print_lock:	
	print "done"
"""

list = []
print_lock = threading.Lock()
def is_prime(num):
	for i in range(2,num/2+1):
		if num%i == 0:
			return 0
	return 1
	
def prime(touple):
	for i in range(touple[0],touple[1]):
		#for j in range(1000000):
		#	pass
		if is_prime(i):
			list.append(i)
	with print_lock:
		print "done " + str(touple[0])+ " - " + str(touple[1])
		#print time.time()-start 
start = time.time()
			
touple = (0,100)
prime(touple)
with print_lock:
	print time.time()-start 
	
for j in range (10000000):
	pass

start = time.time()

for i in range (10):
	t = (i*10,(i+1)*10)
	thread = threading.Thread(target = prime, args = (t,))
	thread.daemon = True
	thread.start()

with print_lock:
	print time.time()-start
	#print list

