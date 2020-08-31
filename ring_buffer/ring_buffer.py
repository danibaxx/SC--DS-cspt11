class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.value = [None] * capacity
        self.pointer = 0

    def append(self, item):
        pass

    def get(self):
        # set empty list to variable
        items = []
        # return all elements in given order
        # should not return None
        for i in self.value:
            if i != None:
                items.append(i)
        #return items
        return items

buffer = RingBuffer(3)

buffer.get() # should return empty

# buffer.append()
# buffer.append()
# buffer.append()

buffer.get() # should return 3 values