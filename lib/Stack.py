class Stack:

    def __init__(self, items = [], limit = 100):
        self.limit = limit
        self.items = items
        pass

    def isEmpty(self):
        return len(self.items) == 0
        pass

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            print ('Stack is full')
        pass

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None
        pass

    def peek(self):
        if self.size == self.isEmpty():
            return self.items[-1]
        else:
            return None
        pass
    
    def size(self):
        return len(self.items)
    
        pass

    def full(self):
        return len(self.items) == self.limit
        pass

    def search(self, target):
        for i, item in enumerate(reversed(self.items)):
            if item == target:
                return i
        return -1
            
        
        pass
