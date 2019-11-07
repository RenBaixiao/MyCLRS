class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1

    def stack_empty(self):
        if self.top == -1:
            return True
        return False

    def push(self,x):
        self.top += 1
        self.stack.append(x)

    def pop(self):
        if self.stack_empty():
            print('underflow')
            return
        else:
            self.top -= 1
            self.stack.pop()

class Queue:
    def __init__(self,size):
        self.size = size
        self.head = 0
        self.tail = 0
        self.queue = [0]*size

    def queue_full(self):
        if self.head == (self.tail + 1) % self.size:
            return True
        else return False

    def queue_empty(self):
        if self.head == self.tail:
            return True
        return False

    def enqueue(self,x):
        if self.queue_full():
            print('overflow')
            return
        else:
            self.queue[self.tail] = x
            if self.tail == self.size - 1:
                self.tail = 0
            else:
                self.tail += 1

    def dequeue(self):
        if self.queue_empty():
            print('underflow')
            return
        else:
            x = self.queue[self.head]
            if self.head = self.size - 1:
                self.head = 0
            else:
                self.head += 1
            return x

class Deque:
    def __init__(self,size):
        self.size = size
        self.deque = [0]*size
        self.left = 0
        self.right = 0

    def deque_full(self):
        if self.left == (self.right+1) % self.size:
            return True
        return False

    def deque_empty(self):
        if self.left == self.tail:
            return True
        return False

    def enque_left(self,x):
        if self.deque_full():
            print('overflow')
            return
        else:
            if self.left == 0:
                self.left = self.size - 1
            else:
                self.left -= 1
            self.deque[self.left] = x

    def deque_left(self):
        if self.deque_empty():
            print('underflow')
            return
        else:
            x = self.deque[self.left]
            self.left = (self.left + 1) % self.size
            return x

    def enque_right(self,x):
        if self.deque_full():
            print('overflow')
            return
        else:
            self.deque[self.right] = x
            self.right = (self.right + 1) % self.size

    def deque_right(self):
        if self.deque_empty():
            print('underflow')
            return
        else:
            if self.right == 0:
                self.right = self.size - 1
            else:
                self.right -= 1
            return self.deque[self.right]
