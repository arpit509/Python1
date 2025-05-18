
inp = int(input("Enter the elements: "))
stk = [2,6,4]

def is_empty(stk):
    if len(stk) == 0:
        return True
    return False
print("Is empty = ", is_empty(stk))

def push (stk, item):
    stk.append(item)
    return stk
push(stk, inp)
print("Stack after push = ", stk)

def size(stk):
    return len(stk)
print("Size = ", size(stk))

def peep():
    if is_empty(stk):
        return "Stack is empty"
    else:
        return stk[-1]
print("Peep = ", peep())

def pop(stk):
    a  = stk.pop()
    return a
print("Stack after Pop = ", pop(stk))
