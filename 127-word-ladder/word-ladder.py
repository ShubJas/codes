import collections

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Given two words (beginWord and endWord), and a dictionary's word list, this function returns the length of the shortest transformation sequence from beginWord to endWord, such that only one letter can be changed at a time and each transformed word must exist in the word list. If no such sequence exists, it returns 0.

        Approach:
        1. Use Breadth-First Search (BFS) to explore all possible transformations of the given words.
        2. Initialize a queue with the beginWord and start from there.
        3. For each word in the queue, generate all possible transformations by changing one letter at a time.
        4. If a transformation matches the endWord, return the number of steps.
        5. Use a visited set to keep track of visited words to avoid cycles.
        6. If the queue is empty and no transformation matches the endWord, return 0.
        """

        # Initialize the BFS queue with the beginWord
        q = collections.deque([beginWord])
        
        # Set to keep track of visited words to avoid cycles
        visited = set()
        
        # Convert wordList to a set for faster lookup
        words = set(wordList)
        
        # Get the length of the words
        word_len = len(beginWord)

        # If the endWord is not in the wordList, there is no valid transformation
        if endWord not in wordList:
            return 0

        # Start with step 1 because the beginWord itself is the first step
        steps = 0
        
        # Perform BFS traversal
        while q:
            steps += 1  # Increment steps for each level of BFS
            qlen = len(q)  # Number of elements at the current level
            for _ in range(qlen):
                word = q.popleft()  # Get the next word from the queue
                
                # If the current word is the endWord, return the number of steps
                if word == endWord:
                    return steps 
                
                # Generate all possible transformations by changing one letter at a time
                for i in range(word_len):
                    for c in 'abcdefghijklmnopqrstuvwxyz':  # Iterate over all letters
                        adj_word = word[:i] + c + word[i+1:]  # Form the new word by changing one letter
                        # If the transformed word is in the wordList and not visited
                        if adj_word in words and adj_word not in visited:
                            q.append(adj_word)  # Add the new word to the queue
                            visited.add(adj_word)  # Mark the new word as visited
        
        # If no valid transformation is found, return 0
        return 0
