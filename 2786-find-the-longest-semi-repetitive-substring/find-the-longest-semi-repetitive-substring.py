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
