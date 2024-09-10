class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # If the list is empty, return an empty string
        if not strs:
            return ''
        
        # Start with the first string as the common prefix
        common = strs[0]
        
        # Compare the common prefix with each string in the list
        for i in range(1, len(strs)):
            s2 = strs[i]
            j = 0
            l = min(len(common), len(s2))
            
            # Find the longest common prefix between common and the current string
            while j < l and common[j] == s2[j]:
                j += 1
            
            # Update the common prefix to the matched part
            common = common[:j]
            
            # If at any point the common prefix becomes empty, return ''
            if common == '':
                return ''
        
        return common
