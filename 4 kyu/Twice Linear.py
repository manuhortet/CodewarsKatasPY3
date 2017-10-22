class DoublyLinkedBase:

    class Node:

        def __init__(self, element, prev, next):
            self.element = element
            self.prev = prev
            self.next = next

    def __init__(self):
        self.header = self.Node(None, None, None)
        self.trailer = self.Node(None, None, None)
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.header.next is self.trailer

    def insert(self, element):
        node = self.Node(element, None, None)
        if self.is_empty():
            self.header.next = node
            self.trailer.prev = node
            node.next = self.trailer
            node.prev = self.header
            self.size += 1
        else:
            aux = self.header.next
            for x in range(0, self.size):
                if element < aux.element:
                    node.next = aux
                    node.prev = node.prev
                    aux.prev.next = node
                    aux.prev = node
                    self.size += 1
                elif aux.next is self.trailer:
                    node.prev = self.trailer.prev
                    node.next = self.trailer
                    self.trailer.prev.next = node
                    self.trailer.prev = node
                    self.size += 1
                else:
                    aux = aux.next


def dbl_linear(n):

    u_set = DoublyLinkedBase()
    u_set.insert(1)
    node = u_set.header.next
    for x in range(0, 6):
        u_set.insert((node.element * 2) + 1)
        u_set.insert((node.element * 3) + 1)
        node = node.next

    x = 0
    node2 = u_set.header.next
    while x < n-1:
        node2 = node2.next
        x += 1
    return node2.element

print(dbl_linear(12))
