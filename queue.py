class Queue:
    def __init__(self, max_size, ):
        self.size = max_size
        self.ele=[None]*self.size
        self.front = 0
        self.rear = -1

    def is_full(self):
        if self.front >= self.size-1:
            # print("overflow")
            return True
        return False

    def is_empty(self):
        if self.front > self.rear:
            return True
        return False
    
    def enqueue(self, val):
        if self.is_full():
            print("overflow condition")
        else:
            self.rear += 1
            self.ele[self.rear] = val
    
    def dequeue(self):
        if self.is_empty():
            print(" underflow conditon ")
        else :
            data = self.ele[self.front]
            self.front += 1
            # print(data+" is deleted")
            return data
    
    def display(self):
        if self.is_empty():
            print(" underflow conditon ")
        i = self.front
        while i < self.rear+1 :
            print( self.ele[i])
            i+=1

    def get_max_size(self):
        return self.size

size=int(input("enter the size of queue: "))
q1= Queue(size)
q1.get_max_size()
q1.dequeue()
q1.enqueue(23)
q1.enqueue(24)
q1.display()
q1.enqueue(25)
q1.enqueue(26)
print(q1.get_max_size())
q1.dequeue()
print(q1.get_max_size())
q1.display()