class ListNode:
    def __init__(self,val=0,key=0,next=None,prev=None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = ListNode()
        self.right = ListNode()
        self.left.next,self.right.prev = self.right,self.left

    def delete(self,node):
        first = node.prev
        second = node.next
        first.next , second.prev = second , first
    
    def insert(self,node):
        first = self.right.prev
        second = self.right
        first.next = second.prev = node 
        node.prev , node.next = first , second

    def get(self, key: int) -> int:
        if key in self.cache:
            self.delete(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(self.cache[key])
        newnode = ListNode(value,key)
        self.cache[key] = newnode
        self.insert(newnode)

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.delete(lru)
            del self.cache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)