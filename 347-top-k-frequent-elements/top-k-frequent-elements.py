class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        


        frequency_map = Counter(nums)
        
        # Use a heap to store the frequency and element. Negate the frequency
        # since heapq is a min-heap, but we need a max-heap functionality.
        # The heap will store elements as (-frequency, element).
        heap = [(-freq, num) for num, freq in frequency_map.items()]
        
        # Transform the list into a heap in-place.
        heapq.heapify(heap)
        
        # Extract the top k elements (with the highest frequencies) from the heap.
        # Since the frequencies are negated, we'll use heapq.heappop which
        # will pop the smallest (in this case, the largest negative) elements first.
        top_k = [heapq.heappop(heap)[1] for _ in range(k)]
        
        return top_k

        
        
        
        # # 0(NlogN) - hashmap and sorting keys
        # hashmap = {}

        # # Populate the hashmap with frequency counts of each element in nums
        # for n in nums:
        #     hashmap[n] = hashmap.get(n, 0) + 1

        # # Sort the hashmap by value (frequency) in ascending order and then reverse it
        # # to have the most frequent elements at the beginning
        # sorted_items = sorted(hashmap.items(), key=lambda item: item[1], reverse=True)

        # # Extract the keys from the sorted items and take the first k keys
        # top_k_keys = [item[0] for item in sorted_items[:k]]

        # return top_k_keys
