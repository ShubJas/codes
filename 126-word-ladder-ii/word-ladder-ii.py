# BFS -> spcial parent adj graph
# DFS -> recusive backtrack
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        


        words = set(wordList)
        if endWord not in words:
            return []
        wlen = len(beginWord)

        parents = defaultdict(list)
        word_level = defaultdict(int)
        word_level[beginWord] = 0

        q = collections.deque([beginWord])
        stop = False
        while q and not stop:

            qlen = len(q)
            local_visited =set()

            for _ in range(qlen):

                word = q.popleft()
                curr_level = word_level[word]

                for i in range(wlen):
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        newword = word[:i] + ch + word[i+1:]

                        if newword in words:
                            if newword not in word_level:
                                word_level[newword] = curr_level + 1
                                q.append(newword)
                                local_visited.add(newword)
                            
                            if word_level[newword] == curr_level + 1:
                                parents[newword].append(word)
                            
                            if newword == endWord:
                                stop = True
            words -= local_visited


        stack = []
        result = []
        def backtrack(word):

            stack.append(word)

            if word == beginWord:
                result.append(stack[::-1])
            else:
                
                for parent in parents[word]:
                    backtrack(parent)
                
            stack.pop()
        

        backtrack(endWord)
        return result



