class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        hm = defaultdict(int)
        # for n in nums1:
        #     hm[n] = i
        for x in nums2:
            hm[x] = -1
        n = len(nums2)


        for i in range(n-1):

            for j in range(i+1,n):
                if nums2[i] < nums2[j]:
                    hm[nums2[i]] = nums2[j]
                    break
        
        for i,x in enumerate(nums1):
            nums1[i] = hm[x]
        
        return nums1




