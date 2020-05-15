from collections import deque

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = deque(maxlen=self.capacity)
        self.neg_count = 1 # Part 1 of my rotating pointer
        self.pos_count = 0 # Part 2 of my rotating pointer

    def append(self, item):
        # Reset both parts of the pointer when it's time
        if self.capacity == (self.neg_count - 1):
            self.neg_count = 1
            self.pos_count = 0 

        # Ring buffer is not full
        if len(self.storage) < self.capacity:
            self.storage.append(item)

        # Ring buffer is full
        elif self.capacity == len(self.storage):
            self.storage.rotate(self.capacity - self.neg_count)
            self.storage.appendleft(item)
            self.storage.rotate(self.capacity + self.pos_count)
            self.neg_count = self.neg_count + 1
            self.pos_count = self.pos_count + 1

    def get(self):
        return list(self.storage)

if __name__ == '__main__':
    # A little testy test
    ring = RingBuffer(5)
    for i in range(50):
        ring.append(i)
        print(ring.get())