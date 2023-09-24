class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self,item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push('Hello')
    print(s.peek())
    print(s.pop())
    print(s.is_empty())