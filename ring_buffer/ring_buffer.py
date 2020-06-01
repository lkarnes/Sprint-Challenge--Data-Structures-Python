class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.length = 0
        self.position = 0

    def append(self, item):
        if self.length < self.capacity:
            self.storage.append(item)
            self.length += 1
        else:
            self.storage.pop(self.position)
            self.storage.insert(self.position, item)
            if self.position < self.length  - 1:
                self.position +=1
            else: 
                self.position = 0
    def get(self):
        print(self.storage)
        return self.storage


buffer = RingBuffer(5)
buffer.get()
buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')
buffer.append('e')
buffer.append('f')
buffer.append('g')
buffer.append('h')
buffer.append('i')
buffer.get()