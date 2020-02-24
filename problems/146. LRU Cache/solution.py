# Doubly Linked-list class
class Node(object):
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.lookup = {}
        self.head = self.tail = None

    def get(self, key: int) -> int:
        if key not in self.lookup:
            return -1
        node = self.lookup[key]

        self.moveForward(node)
        return node.val[1]

    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            self.updateNode(key, value)
            return
        if self.size == self.capacity:
            node = self.tail
            k, val = node.val
            del self.lookup[k]
            if self.capacity == 1:
                self.head = self.tail = None
            else:
                node.prev.next = None
                self.tail = self.tail.prev
            self.size -= 1

        node = Node((key, value))
        self.lookup[key] = node
        if not self.head:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1

    def updateNode(self, key: int, value: int) -> None:
        node = self.lookup[key]
        node.val = (key, value)
        self.moveForward(node)

    def moveForward(self, node):
        # print(node.val, node.prev, node.next)
        if not self.head:
            return
        if self.head == node:
            return
        if self.tail == node and self.head != self.tail:
            self.tail = self.tail.prev
            node.prev.next = node.next
            node.prev = None
            node.next = self.head
            node.next.prev = node
            self.head = node
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = None
            node.prev = None
            node.next = self.head
            node.next.prev = node
            self.head = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
