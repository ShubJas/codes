# from collections import OrderedDict

# class LRUCache:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.linkedList = OrderedDict()

#     def put(self, key, value):
#         if key in self.linkedList:
#             self.linkedList.move_to_end(key)
#         else:
#             if len(self.linkedList) == self.capacity:
#                 self.linkedList.popitem(last=False)
#         self.linkedList[key] = value
    
#     def get(self, key):
#         if key not in self.linkedList:
#             return -1
        
#         self.linkedList.move_to_end(key)
#         return self.linkedList[key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class Node:
    def __init__(self,key = 0,val = 0,next = None,prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        # left and right are dummy nodes
        self.left , self.right = Node(), Node()
        self.left.next , self.right.prev = self.right, self.left

    def remove(self,node):
        before, after = node.prev , node.next
        before.next , after.prev= after , before
        
    def insert(self,node):
        # Inserting to the left of mru(right)
        before , after = self.right.prev , self.right
        before.next = after.prev = node
        node.prev , node.next = before , after


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
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
        


# # Your LRUCache object will be instantiated and called as such:
# # obj = LRUCache(capacity)
# # param_1 = obj.get(key)
# # obj.put(key,value)