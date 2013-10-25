from stacks import Stack

def find_closing_paren(string, start_paren):
    paren_stack = Stack()
    for i in range(start_paren, len(string)):
        ch = search_string[i]
        if ch == "(":
            paren_stack.push("(")
        elif ch == ")":
            paren_stack.pop()
            if paren_stack.is_empty():
                return i

def alphabetize_rotated_array(array):
    last_word = array[0]
    for word in array:
        if [last_word, word].sort[0] == word:
            start = array.index(word)
            break
        else:
            last_word = word

    return array[start:] + array[:start]


class MaxStack:

    def __init__(self):
        self.stack = Stack()
        self.largest = Stack()
    
    def push(self, item):
        self.stack.push(item)
        if item >= self.largest.peek():
            self.largest.push(item)

    def pop(self):
        item = self.stack.pop()
        if item == self.largest.peek():
            self.largest.pop()
        return item

    def get_largest(self):
        return self.largest.peek()

def find_biggest_range(array):
    largest = {'value': array[0], 'time': 0}
    smallest = {'value': array[0], 'time': 0}
    best_profit = largest['value'] - smallest['value']
    best_stock_times = [smallest['time'], largest['time']]
    for i in range(len(array)):
        if i < smallest['value']:
            largest = {'value': array[i], 'time': i}
            smallest = {'value': array[i], 'time': i}
        elif i > largest[0]:
            largest = {'value': array[i], 'time': i}
            profit = largest['value'] - smallest['value']
            if profit > best_profit:
                best_profit = profit
                best_stock_times = [smallest['time'], largest['time']]

    return best_stock_times
