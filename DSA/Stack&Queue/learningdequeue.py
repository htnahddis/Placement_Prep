#Learning deuqueu concepts here 

from collections import dequeue

dq = dequeue([2,3,1,4])

#append and extend
dq.append(4)
dq.extend([3,4,2,12])
print(dq)

#appendleft and extendleft
dq.appendleft(0)
dq.extendleft([2,4,2])
print("Print the append left:", dq)

#remove adn pop 
dq.remove(4) #remvoes teh first occurence of the element
dq.pop()
dq.popleft()
print("Print the pop and popleft:", dq)
