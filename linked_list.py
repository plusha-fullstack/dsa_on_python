class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

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
        prev = self.head
        while node is not None:
            if prev.next is node:
                prev = node
            node = node.next
            if self.head.value == val:
                self.head = prev.next
                if not all:
                    break

            elif node is self.tail and self.tail.value == val:
                prev.next = None
                self.tail = prev
                if not all:
                    break

            elif node is not None and node.value == val:
                prev.next = node.next
                if not all:
                    break

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
        if self.len() == 0:
            self.head = newNode
            self.tail = newNode
            return
        node = self.head
        if afterNode is None:
            newNode.next = node
            self.head = newNode
        elif afterNode == self.tail:
            afterNode.next = newNode
            self.tail = newNode
            return
        else: 
            while node is not None:
                if node is afterNode:
                    newNode.next = node.next
                    node.next = newNode
                    break
                node = node.next
