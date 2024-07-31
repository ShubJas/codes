class Solution:
    def match(self, s1, s2):
        """
        This function checks if s2 can be formed by adding exactly one character to s1.
        """
        n1 = len(s1)
        n2 = len(s2)

        # If the length difference is not exactly 1, return False
        if n2 != n1 + 1:
            return False
            
        i1 = i2 = 0

        # Iterate through both strings
        while i1 < n1 and i2 < n2:
            if s1[i1] == s2[i2]:
                # Characters match, move both pointers
                i1 += 1
            # Always move pointer for s2
            i2 += 1
        
        # All characters of s1 must have been matched in s2
        return i1 == n1

    def longestStrChain(self, words: List[str]) -> int:
        """
        This function calculates the longest chain of words where each word is formed
        by adding exactly one character to the previous word.
        """
        n = len(words)
        # Sort words based on length
        words.sort(key=lambda word: len(word))

        dp = [1] * n  # Initialize DP array with 1, as each word is a chain of at least itself

        # Process each word in words
        for i in range(1, n):
            for prev_i in range(i):
                # Check if words[prev_i] can form words[i] by adding one character
                if self.match(words[prev_i], words[i]):
                    # Update dp[i] if a longer chain can be formed
                    dp[i] = max(dp[i], dp[prev_i] + 1)
        
        # The length of the longest chain is the maximum value in dp
        return max(dp)
