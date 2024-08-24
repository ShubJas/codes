class Solution:
    def findAllPaths(self, res: List[List[str]], currentWord: str, beginWord: str, parents: dict, path: List[str]):
        # Add the current word to the path
        path.append(currentWord)
        
        # If the current word is the beginWord, reverse the path and add it to results
        if currentWord == beginWord:
            res.append(path[::-1])
        else:
            # Recursively visit all parents of the current word
            for word in parents[currentWord]:
                self.findAllPaths(res, word, beginWord, parents, path)
        
        # Remove the current word from the path before backtracking
        path.pop()

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        parents = defaultdict(list)
        levels = {beginWord: 0}
        q = deque([beginWord])
        found = False
        wordLen = len(beginWord)
        
        # BFS to construct the graph
        while q and not found:
            level_size = len(q)
            local_visited = set()
            for _ in range(level_size):
                word = q.popleft()
                current_level = levels[word]
                for i in range(wordLen):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        newWord = word[:i] + c + word[i+1:]
                        if newWord in wordSet:
                            if newWord not in levels:
                                levels[newWord] = current_level + 1
                                q.append(newWord)
                                local_visited.add(newWord)
                            if levels[newWord] == current_level + 1:
                                parents[newWord].append(word)
                            if newWord == endWord:
                                found = True
            
            # Remove words that were added in this level to prevent loops
            wordSet -= local_visited
        
        res = []
        if endWord in parents:
            self.findAllPaths(res, endWord, beginWord, parents, [])
        return res
