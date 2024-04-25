# class Solution:
#     def longestSemiRepetitiveSubstring(self, s: str) -> int:
#         longest = 1
#         l = 0

#         while l<len(s)-1:
#             r = l
#             countrep = 0
#             # Move `r` until the end of the string or until more than one repeat is found
#             while r < len(s) - 1:
#                 if s[r] == s[r + 1]:
#                     countrep += 1
#                 r += 1
#                 if countrep > 1:
#                     break

#             # Ensure the longest calculation includes the character at position `r` if not exiting by repeat condition
#             if countrep <= 1:
#                 r += 1

#             longest = max(longest, r - l)
#             l = r

#         return longest

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        last_repeated_char_index = -1

        for r in range(len(s)):
            # If we have a repeat, and it's the second consecutive repeat, move `l`
            if r > 0 and s[r] == s[r - 1]:
                if last_repeated_char_index >= l:
                    # The previous character was a repeat, so move `l` to the right of it
                    l = last_repeated_char_index + 1
                # Update the index for the last repeat
                last_repeated_char_index = r - 1

            # Update the longest after the `l` index may have moved
            longest = max(longest, r - l + 1)

        return longest

