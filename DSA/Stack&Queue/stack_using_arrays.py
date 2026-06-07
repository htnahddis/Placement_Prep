class ArrayStack:
    
    def __init__(self, size):
        self.top = -1 
        self.size = size
        self.arr = [0] * size
        
    def push(self, x):
        self.arr.append(x)
        top += 1          

    def pop(self):
        value = self.arr[self.top]
        self.top -= 1

    def top(self):
        return self.top
     
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
        
