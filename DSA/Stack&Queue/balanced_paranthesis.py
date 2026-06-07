class ArrayStack:
    def __init__(self):
        self.arr = []

    def push(self, x):
        self.arr.append(x)

    def pop(self):
        if not self.arr:
            return None
        return self.arr.pop()

    def is_empty(self):
        return len(self.arr) == 0


def parenthesis_checker(s):
    stack = ArrayStack()

    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for ch in s:

        if ch in "({[":
            stack.push(ch)

        elif ch in ")}]":

            if stack.is_empty():
                return False

            top = stack.pop()

            if top != pairs[ch]:
                return False

    return stack.is_empty()


print(parenthesis_checker("{(){}[]}"))   # True
print(parenthesis_checker("(()[{]})"))   # False