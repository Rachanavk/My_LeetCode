#Write a function in python that can reverse a string using stack data structu
from collections import deque

class Stack():
    def __init__(self):
        self.container = deque()
    def push(self,val):
        return self.container.append(val)
    def pop(self):
        return self.container.pop()
    def size(self):
        return len(self.container)
    
    
def reverse_string(strs):
    res = ""
    stack = Stack()
    for i in strs:
        stack.push(i)
    while stack.size() != 0 :
        res += stack.pop()
    return res

if __name__ == '__main__':
    print(reverse_string("We will conquere COVI-19"))
    print(reverse_string("I am the king"))
        

