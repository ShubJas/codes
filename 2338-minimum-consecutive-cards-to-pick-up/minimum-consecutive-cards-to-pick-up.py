class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        
        value_index = {}
        min_count  = -1
        for i in range(len(cards)):
            card = cards[i]
            if card in value_index:
                if min_count == -1:
                    min_count = i - value_index[card] + 1
                else:
                    min_count = min(min_count ,  i - value_index[card] + 1)
            value_index[card] = i
        return min_count
        
        
        
        # min_count = len(cards) + 1
        # hashset = defaultdict(int)
        # l = 0

        # for r in range(len(cards)):

        #     current = cards[r]

        #     hashset[current] +=1

        #     while hashset[current]>1:
                
        #         min_count = min(min_count,r-l +1)
        #         remove = cards[l]
        #         hashset[remove] -=1
        #         l+=1
        # return min_count if min_count != len(cards) + 1 else -1


        