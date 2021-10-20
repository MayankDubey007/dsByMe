class Queue:

    def __init__(self, size):
        self.queue = []
        self.size = size




    def enqueue(self, data):
        if len(self.queue) == (self.size):
            print("Queue is full!")
        else:
            self.queue.append(data)
            print(f"enQueue data = {data}")
            
            return data


    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print(f"poped element : {self.queue.pop(0)}")

    
    
    def print(self):
        ln = len(self.queue)
        print(f"length of  Queue is : {ln}")
        for i in range(ln):
            print(self.queue[i], end=",")
        print(f"\nfirst element = {self.queue[0]} And last element = {self.queue[-1]}")


if __name__ == '__main__':
    positive_infinity = float('inf')
    queue = Queue(positive_infinity)

    queue.enqueue("p1")
    queue.enqueue("p2")
    queue.enqueue("p3")
    queue.enqueue("p4")
    queue.enqueue("p5")
    print("***five people added***")

    queue.dequeue()
    queue.dequeue()
    print("***2 got  people got ticket***")
    queue.enqueue("f1")
    queue.enqueue("f2")
    queue.enqueue("f3")
    print("***3 Friend joined the Queue***")
    queue.dequeue()
    queue.dequeue()
    print("2 got  people got ticket ")
    queue.enqueue("g1")
    queue.enqueue("g2")
    print("***2 girls joined the Queue***")
    queue.print()

    # adding the queue

    # queue.dequeue()
    # queue.print()
    # queue.dequeue()
    # queue.dequeue()
    # queue.dequeue()
    # queue.dequeue()
    # queue.dequeue()
