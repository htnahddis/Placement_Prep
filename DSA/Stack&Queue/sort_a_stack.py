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
        
def sorted_insert(stack, x):

    if not stack or stack[-1] <= x:
        stack.append(x)
        return

    temp = stack.pop()

    sorted_insert(stack, x)

    stack.append(temp)


def sort_stack(stack):

    if not stack:
        return

    temp = stack.pop()

    sort_stack(stack)

    sorted_insert(stack, temp)


stack = [3, 1, 4, 2]

sort_stack(stack)

print(stack)