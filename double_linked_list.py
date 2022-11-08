class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        out = []
        node = self.head
        while node is not None:
            if node.value == val:
                out.append(node)
            node = node.next
        return out

    def delete(self, val, all=False):
        if self.head is None:
            return
        if self.len() == 1 and self.head.value == val:
            self.head = None
            self.tail = None
            return
        node = self.head
        while node is not None:
            if self.head.value == val:
                self.head = self.head.next
                self.head.prev = None
                if not all:
                    break
            elif node is self.tail and self.tail.value == val:
                node.prev.next = None
                self.tail = node.prev
                if not all:
                    break
            elif node is not None and node.value == val:
                node.prev.next = node.next
                node.next.prev = node.prev
                if not all:
                    break
            node = node.next

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        length = 0
        node = self.head
        while node is not None:
            length += 1
            node = node.next
        return length

    def insert(self, afterNode, newNode):
        node = self.head
        if afterNode is None and self.len() == 0:
            self.head = newNode
            self.tail = newNode
        elif afterNode is None and self.len() > 0:
            self.add_in_tail(newNode)

        elif afterNode is self.tail:
            self.add_in_tail(newNode)
        else:
            while node is not None:
                if node is afterNode:
                    newNode.prev = node
                    newNode.next = node.next
                    node.next.prev = newNode
                    node.next = newNode
                    break
                node = node.next

    def add_in_head(self, newNode):
        self.head.prev = newNode
        newNode.next = self.head
        self.head = newNode
