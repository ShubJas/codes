class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        q = collections.deque([beginWord])
        visited = set()
        words = set(wordList)
        word_len = len(beginWord)

        if endWord not in wordList:
            return 0

        steps = 0
        while q:
            steps += 1
            qlen = len(q)
            for _ in range(qlen):
                word = q.popleft()
                if word == endWord:
                    return steps 
                
                for i in range(word_len):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        adj_word = word[:i] + c + word[i+1:]
                        if adj_word in words and adj_word not in visited:
                            q.append(adj_word)
                            visited.add(adj_word)
        return 0

                
        