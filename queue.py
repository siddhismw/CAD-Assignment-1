queue = []

# Enqueue
queue.append(10)
queue.append(20)
queue.append(30)

print("Queue:", queue)

# Dequeue
if queue:
    removed = queue.pop(0)
    print("Removed:", removed)

print("Queue after dequeue:", queue)