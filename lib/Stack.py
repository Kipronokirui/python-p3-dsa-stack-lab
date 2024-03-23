class Stack:

    def __init__(self, items=None, limit=50):
        if items is None:
            items = []
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if not self.full():
            self.items.append(item)
        else:
            print("Stack is full, cannot push item")

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            print("Stack is empty, cannot pop item")
            return None

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            print("Stack is empty, no item to peek")
            return None
    
    def size(self):
        return len(self.items)

    def full(self):
        return self.size() >= self.limit

    def search(self, target):
        for i in range(len(self.items) - 1, -1, -1):
            if self.items[i] == target:
                return len(self.items) - i - 1
        return -1
