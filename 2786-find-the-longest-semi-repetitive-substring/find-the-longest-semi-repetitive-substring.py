class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        longest = 1
        l = 0

        for l in range(len(s)-1):
            r = l
            countrep = 0
            # Move `r` until the end of the string or until more than one repeat is found
            while r < len(s) - 1:
                if s[r] == s[r + 1]:
                    countrep += 1
                r += 1
                if countrep > 1:
                    break

            # Ensure the longest calculation includes the character at position `r` if not exiting by repeat condition
            if countrep <= 1:
                r += 1

            longest = max(longest, r - l)

        return longest
