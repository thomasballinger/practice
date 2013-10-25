fibdict = {}

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:            
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_memoized(n):
    if n in fibdict:
        pass
    else:
        if n == 0:
            fibdict[n] = 0
        elif n == 1:
            fibdict[n] = 1
        else:
            fibdict[n] = fibonacci_memoized(n-1) + fibonacci_memoized(n-2)
    return fibdict[n]

def fibonacci_iter(n, n1=0, n2=1, count=0):
    if n <= count:
        return n1
    else:
        return fibinacci_iter(n, n2, n1+n2, count+1)

def sum_list(ls):
    def sum_iter(ls, sum):
        if ls:
            return sum_iter(ls[1:], sum + ls[0])
        else:
            return sum

    return sum_iter(ls[:], 0)

def sum_list2(ls):
    if ls:
        return ls[0] + sum_list2(ls[1:])
    else:
        return 0

def contains(num, ls):
    if not ls:
        return False
    elif ls[0] == num:
        return True
    else:
        return contains(num, ls[1:])

def lastIndexOf(num, ls, index=0):
    if not ls:
        return -1
    elif ls[0] == num:
        another_item = lastIndexOf(num, ls[1:], index + 1)
        if another_item == -1:
            return index
        else:
            return another_item
    else:
        return lastIndexOf(num, ls[1:], index + 1)

class Node(object):
    def __init__(self, value, l=None, r=None):
        self.value = value
        self.left = l
        self.right = r

def sum_binary_tree(tree):
    if tree is None:
        return 0
    else:
        return tree.value + sum_binary_tree(tree.left) + sum_binary_tree(tree.right)

tree1 = Node(1, Node(2, Node(3), Node(4)), Node(5, Node(6), Node(7)))
tree2 = Node(1, Node(2, Node(3)), Node(2))

#print sum_binary_tree(tree1)
#print sum_binary_tree(tree2)