#  Solve like the q max sum of array is k
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # Initialize a dictionary to store the first occurrence of each parity configuration.
        # We start with parity 0 at index -1 to handle cases where the substring starts from index 0.
        parity_index = {0: -1}

        # Define the vowels we're interested in.
        vowels = 'aeiou'

        # This will represent the current bitmask, where each bit represents the parity (even/odd) of a vowel.
        # Initially, all vowels are even (0), so the bitmask is 0.
        parity = 0

        # Initialize the length of the longest valid substring.
        longest = 0

        # Iterate through each character in the string along with its index.
        for i, ch in enumerate(s):
            # If the character is a vowel, update the bitmask.
            if ch in vowels:
                # Find the index of the vowel in 'aeiou' to determine which bit to toggle.
                index = vowels.index(ch)
                # Toggle the bit corresponding to this vowel using XOR.
                parity ^= 1 << index

            # If the current parity bitmask has been seen before, it means the substring
            # between the first occurrence of this parity and the current index has an even count
            # of all vowels (since the parity has returned to the same state).
            if parity in parity_index:
                # Calculate the length of the substring and update the longest if necessary.
                longest = max(longest, i - parity_index[parity])
            else:
                # If this parity configuration is seen for the first time,
                # store the current index in the dictionary.
                parity_index[parity] = i
        
        # Return the length of the longest substring found.
        return longest

        
        return longest





        

            