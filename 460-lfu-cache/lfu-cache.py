from collections import defaultdict, deque

class Node:
    def __init__(self, value, key, ctr=1):
        self.val = value
        self.key = key
        self.ctr = ctr

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.key_node = {}
        self.freq_Q = defaultdict(deque)
        self.freq_key = defaultdict(set)
        self.min_ctr = 0

    def touch(self, node):
        old_ctr = node.ctr
        new_ctr = old_ctr + 1

        self.freq_Q[old_ctr].remove(node.key)
        self.freq_key[old_ctr].remove(node.key)

        if len(self.freq_Q[old_ctr]) == 0:
            del self.freq_Q[old_ctr]
            if self.min_ctr == old_ctr:
                self.min_ctr += 1

        self.freq_Q[new_ctr].appendleft(node.key)
        self.freq_key[new_ctr].add(node.key)
        node.ctr = new_ctr

    def get(self, key: int) -> int:
        if key not in self.key_node:
            return -1

        node = self.key_node[key]
        self.touch(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return

        if key in self.key_node:
            node = self.key_node[key]
            node.val = value
            self.touch(node)
            return

        if len(self.key_node) >= self.cap:
            least_freq_key = self.freq_Q[self.min_ctr].pop()
            self.freq_key[self.min_ctr].remove(least_freq_key)
            del self.key_node[least_freq_key]

        self.min_ctr = 1
        self.freq_Q[1].appendleft(key)
        self.freq_key[1].add(key)
        self.key_node[key] = Node(value, key)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)
