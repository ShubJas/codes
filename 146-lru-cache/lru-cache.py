class Node:
    def __init__(self,key=0,value=0,next=None,prev=None):
        self.key =key
        self.value = value
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left , self.right = Node(), Node()
        self.left.next , self.right.prev = self.right , self.left

    
    def insert(self, node):
        before = self.right.prev 
        after = self.right
        before.next = node
        after.prev = node
        node.prev = before
        node.next = after
        

    

    def remove(self,node):
        before , after = node.prev , node.next
        before.next = after 
        after.prev = before


    def get(self, key: int) -> int:

        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1
        
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)