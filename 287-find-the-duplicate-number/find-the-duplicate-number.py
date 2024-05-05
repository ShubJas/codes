class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0

        # First phase: finding the intersection point in the cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Second phase: find the entrance to the cycle
        slow = 0  # reset slow to the start
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow  # slow is the duplicate number



        

            










        # hashset = {}

        # for val in nums:
        #     hashset[val] = hashset.get(val,0) + 1
        
        # for val ,  count in hashset.items:
        #     if count >1:
        #         return val
        
        
        
        
        
        
        # ctr = Counter(nums)

        # for value,count in ctr.items():
        #     if count>1:
        #         return value 
        