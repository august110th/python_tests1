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
        new_string_in = [input()]
        new_string_out = list(''.join(new_string_in))
        print(new_string_out)

s=Stack()
s.test_stack()
