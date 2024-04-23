class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)  # key : [['value', timestamp], ...]
        # self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # if key not in self.hashmap:
        #     self.hashmap[key] = []

        self.hashmap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.hashmap.get(key, [])
        l, r = 0, len(values) - 1
        res = ""  # Initialize result as an empty string

        while l <= r:  
            m = (l + r) // 2
            if values[m][1] == timestamp:
                return values[m][0]  # Return immediately if exact timestamp match
            if values[m][1] < timestamp:
                res = values[m][0]  # Update the result
                l = m + 1  # Go right if the middle timestamp is less than the given timestamp
            else:
                r = m - 1  # Go left if the middle timestamp is greater than the given timestamp

        return res  # Return the result after the binary search

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)