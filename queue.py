class myqueue():
    def __init__(self):
        self.tail = 0
        self.head = 0
        self.queue = [None] * 5
    def enqueue(self, value):
        try:
            if self.queue[self.tail] is None:
                self.queue[self.tail] = value
        except:
            print ("Queue is full. {} cannot be added".format(value))
        if self.tail == len(self.queue):
            self.tail = 0
        else:
            self.tail += 1
    def dequeue(self):
        temp = self.queue[self.head]
        self.queue[self.head] = None
        self.head += 1
        return temp
    def print_queue(self):
        print (self.queue)
        print ("Next item to dequeue is {}".format(self.queue[self.head]))
        print ("Last enqueued item is {}".format(self.queue[self.tail-1]))


new = myqueue()
new.enqueue(1)
new.print_queue()
new.enqueue(2)
new.print_queue()
new.enqueue(3)
new.print_queue()
x = new.dequeue()
new.print_queue()

new.enqueue(4)
new.enqueue(43)
new.enqueue(42)
x = new.dequeue()
x = new.dequeue()
new.enqueue(52)
new.enqueue(62)
new.print_queue()
