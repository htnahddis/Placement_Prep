class ArrayQueue:
    def __inti__(self, size):
        self.rear = -1
        self.front = 0
        self.arr = [0] * size
        self.size =size
        

    def enqueue(x):
        if self.rear != self.size -1 :
            self.arr.append(x)
            self.rear +=1
        else:
            return "Queue is full"
    

    def dequeue():
        if self.front > self.rear:
            self.front += 1 
        else:
            return "Queue is empty"

    def front():
        return self.front

    def rear():
        return self.rear
        
