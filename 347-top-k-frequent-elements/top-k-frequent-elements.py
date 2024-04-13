class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        # Populate the hashmap with frequency counts of each element in nums
        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1

        # Sort the hashmap by value (frequency) in ascending order and then reverse it
        # to have the most frequent elements at the beginning
        sorted_items = sorted(hashmap.items(), key=lambda item: item[1], reverse=True)

        # Extract the keys from the sorted items and take the first k keys
        top_k_keys = [item[0] for item in sorted_items[:k]]

        return top_k_keys
