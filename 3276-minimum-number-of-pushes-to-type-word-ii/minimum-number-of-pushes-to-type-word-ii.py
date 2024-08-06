class Solution:
    def minimumPushes(self, word: str) -> int:

        count = defaultdict(int)
        mapper = defaultdict(int)


        for c in word:
            count[c] +=1
        
        #  when u sort it becomes a list of tuples
        count  = sorted(count.items(),key = lambda item: item[1],reverse = True) 
        i= 1

        pos = 1
        for c,cnt in count:
            # mapper[i] = (c,pos)
            mapper[c] = pos
            i += 1
            if i == 9:
                pos += 1
                i = 1
        
        result = 0
        for c in word:
            result += mapper[c]
        
        return result

        