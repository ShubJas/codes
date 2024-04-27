class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        for l in range(len(nums) - 2):
            # Skip duplicate values
            if l > 0 and nums[l] == nums[l - 1]:
                continue

            m, r = l + 1, len(nums) - 1
            while m < r:
                total = nums[l] + nums[m] + nums[r]
                if total == 0:
                    result.append([nums[l], nums[m], nums[r]])
                    m += 1
                    r -= 1
                    # Skip duplicate values
                    while m < r and nums[m] == nums[m - 1]:
                        m += 1
                    while m < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif total > 0:
                    r -= 1
                else:
                    m += 1

        return result
