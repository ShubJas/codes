class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:

        visited = set()

        for i in range(len(nums)):
            if nums[i] not in visited:
                iscycle = set()
                while True:
                    if i in iscycle:
                        return True

                    visited.add(i)
                    iscycle.add(i)
                    prev = i
                    i = (i + nums[i] )% len(nums)

                    if prev == i:
                        break
                    if (nums[i]>0) != (nums[prev]>0):
                        break
        return False


        