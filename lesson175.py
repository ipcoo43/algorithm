# -1,1,3,-2,2
import queue

num = [-1,1,3,-2,2]
q1=queue.Queue()
q2=queue.Queue()
for i in num:
	if i<0:
		q1.put(i)
	elif i>=0:
		q2.put(i)

print(list(q1.queue + q2.queue))

print([i for i in num if i<0] + [i for i in num if i>0])