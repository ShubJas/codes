class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        card_index = {}
        min_num = -1
        for i in range(len(cards)):
            card = cards[i]
            if card in card_index:
                if min_num == -1:
                    min_num = i - card_index[card] + 1
                else:
                    min_num = min(min_num, i - card_index[card] + 1)
            card_index[card] = i

        return min_num
        
        
        
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


        