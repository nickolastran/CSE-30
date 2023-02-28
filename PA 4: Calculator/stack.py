
# author: Nickolas Tran
# date: 2/22/2023
# creates stack thingy

class Stack:
    def __init__(self):
        self.value = []

    def isEmpty(self):
        if len(self.value) == 0:
            return True
        return False

    def push(self, item):
        self.value.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.value.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.value[-1]

    def size(self):
        return len(self.value)


# a driver program for class Stack
if __name__ == "__main__":
    
    data_in = ["hello", "how", "are", "you"]
    s = Stack()
    for i in data_in:
        s.push(i)
           
    assert s.size() == len(data_in)
    assert s.peek() == data_in[-1]
    data_out = []
    while not s.isEmpty():
        data_out.append(s.pop())
    assert data_out == data_in[::-1]
    assert s.size() == 0
    assert s.peek() == None