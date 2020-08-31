class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.value = [None] * capacity
        self.pointer = 0

    def append(self, item):
        # setting the value/pointer to item
        self.value[self.pointer] = item
        # print('item:', item)
        # increment pointer through each value
        self.pointer += 1
        # if pointer == capcity, set pointer back to 0
        if self.pointer == self.capacity:
            self.pointer = 0

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

print(buffer.get()) # should return empty

buffer.append('a')
buffer.append('b')
buffer.append('c')

print(buffer.get()) # should return 3 values

buffer.append('d')
print(buffer.get()) # returns 'd', 'b', 'c'

buffer.append('e')
buffer.append('f')

print(buffer.get()) # returns 'd', 'e', 'f'