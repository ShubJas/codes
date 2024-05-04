class Solution:
    def reverseVowels(self, s: str) -> str:
        l, r, s = 0, len(s)-1, list(s)
        vowels = 'aeiouAEIOU'

        while l < r:
            if s[l] in vowels and s[r] in vowels:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            l += s[l] not in vowels
            r -= s[r] not in vowels

        return "".join(s)