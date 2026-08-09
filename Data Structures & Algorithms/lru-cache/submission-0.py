class Node:
    def __init__(self,key=0,val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} #key -> Node

        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self,node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _addToFront(self,node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._addToFront(node)
        return node.val
    
    def put(self, key: int, value: int) -> None:
        # if the key is already present in the cache
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            node.val = value
            self._addToFront(node)
        else:
            node = Node(key,value)
            self.cache[key] = node
            self._addToFront(node)

            if len(self.cache)>self.capacity:
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]

