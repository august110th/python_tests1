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

if __name__ == '__main__':
    string_in = input('Введите данные: ')
    counter = 0
    pairs = {")": "(", "]": "[", "}": "{"}
    s = Stack()
    for i in string_in:
        if i == "(" or i == "[" or i == "{":
            s.push(i)
        if i == ")" or i == "]" or i == "}":
            if s.size() > 0:
                element = s.peek()
                if element == pairs[i]:
                    s.pop()
            else:
                break
        counter += 1

    if counter == len(string_in):
        print("Сбалансированно")
    else:
        print("Несбалансированно")