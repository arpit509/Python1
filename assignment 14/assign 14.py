queue = [3,5]
print("Initial queue:", queue)
item = int(input("Enter a number to enqueue: "))

def enqueue(item):
    queue.append(item)
enqueue(item)
print("New queue:", queue)

def is_empty():
    if len(queue) == 0:
        return True
    else:
        return False

print("Queue is empty:", is_empty())

def dequeue():
    if len(queue) == 0:
        return "Queue is empty"
    return queue.pop(0)

print("Dequeue:", dequeue())

def size():
    return len(queue)

print("Size of queue:", size())


