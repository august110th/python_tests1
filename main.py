class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def test_stack(self):
        print("Введите данные для проверки:")
        self.items = input()
        self.items = list(''.join(self.items))

s=Stack()
s.test_stack()
print(s.items)
s.pop()
print(s.items)
