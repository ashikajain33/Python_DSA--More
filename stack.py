class stack:
    # buid an constructor for initilization of stack
    def __init__(self, max_size):
        self.size = max_size
        self.stacks = [None]*self.size
        self.top = -1

    def get_max_size(self):
        return self.size
    
    def is_full(self):
        if self.top == self.size-1 :
            return True
        return False

    def is_empty(self):
        if self.top == -1 :
            return True
        return False

    def push(self, val):
        if self.is_full() :
            print(" stack is full or overflow condition ")
        else:
            self.top += 1
            self.stacks[self.top] = val

    def pop(self):
        if self.is_empty():
            print(" stack is empty or underflow condition ")
            
        else :
            data = self.stacks[self.top]
            self.top -= 1
            return data

    def display(self):
        if self.is_empty() :
            print("stack is empty ")
        else:
            index = self.top
            while index >= 0:
                print(self.stacks[index])
                index -= 1

s = int(input("enter the size of stack: "))
s1 = stack(s)
s1.pop()
s1.push(10)
s1.push(20)
s1.push(30)
s1.pop()
s1.display()
s1.pop()
s1.push(40)
s1.push(50)
s1.push(60)
s1.pop()
s1.display()
