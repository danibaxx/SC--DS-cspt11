class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
    
    # def __str__(self):
    #     output = ''
    #     curr_node = self.head
    #     while curr_node is not None:
    #         output += f'{curr_node.value} -> '
    #         curr_node = curr_node.next_node
    #     return output

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # check if empty
        if node is None:
            return node
        if node.next_node is None:
            return node 
        # set values
        current = node
        prev = None
        next_node = current.next_node
        # while curr is not none
        while current != None:
            # set next_node to currents next
            next_node = current.next_node
            # set current.next to previous
            current.next_node = prev
            # set prev to current
            prev = current
            # set current to next_node
            current = next_node
        # set head to prev
        self.head = prev


llist = LinkedList()
llist.add_to_head(2)
llist.add_to_head(4)
llist.add_to_head(6)
llist.add_to_head(8)
print(llist)
