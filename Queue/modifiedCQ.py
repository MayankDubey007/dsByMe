class CircularQueue:

    def __init__(self, maxSize):
        self.queue = []
        self.maxSize = maxSize

        self.head = 0
        self.tail = 0

    def enqueue(self, data):
        if self.size() == (self.maxSize - 1):
            print("Queue is full!")
        else:
            self.queue.append(data)
            print(f"enQueue Data = {data}")
            self.tail = (self.tail+1) % self.maxSize ####
            return data

    def dequeue(self):
        if self.size() == 0:
            print("Queue is empty!")
        else:
            data = self.queue.pop(0)
            print(f"poped element : {data}")
            self.head = (self.head+1) % self.maxSize
            
    def print(self):
        # print
        if len(self.queue) == 0:
            print("no one else element in Queue/n")
        else:      
            ln = len(self.queue)
            print(self.queue[0], end=",")
            i = 1
            for i in range(i, ln):
                if self.queue[i] != self.queue[0]:
                    print(self.queue[i], end=",")
                else:
                    print("")
                    break
    def size(self):
        if self.tail >= self.head:
            qSize = self.tail - self.head
        else:
            qSize = self.maxSize - (self.head - self.tail)
        return qSize


if __name__ == '__main__':
    size = input("Enter the size of the Circular Queue")
    queue = CircularQueue(int(size)+int(1))

    # adding the queue
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(7)

    queue.dequeue()
    queue.dequeue()
    queue.print()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.print()

# input 7 for the size or anything else
# size = input("Enter the size of the Circular Queue")
# q = CircularQueue(int(size)+int(1))

# # change the enqueue and dequeue statements as you want
# print(q.enqueue(10))
# print(q.enqueue(20))
# print(q.enqueue(30))
# print(q.enqueue(40))
# print(q.enqueue(50))
# print(q.enqueue('Studytonight'))
# print(q.enqueue(70))
# print(q.enqueue(80))
# # print(q.dequeue())
# # print(q.dequeue())
# # print(q.dequeue())
# # print(q.dequeue())
# # print(q.dequeue())
# # print(q.dequeue())
# # print(q.dequeue())
# # print(q.dequeue())
# # print(q.dequeue())
# print(q.print())
