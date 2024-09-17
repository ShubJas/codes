class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        words = s1 +  ' ' + s2
        words = words.split(' ')

        wordcount = defaultdict(int)
        for word in words:
            wordcount[word] += 1
        
        # print(wordcount)
        return list(word for word in wordcount if wordcount[word] == 1)
