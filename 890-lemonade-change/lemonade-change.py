class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        five = ten = 0

        for b in bills:
            if b == 5:
                five += 1
            elif b == 10:
                if five:
                    five-=1
                else:
                    return False
                ten += 1
            else:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five > 2:
                    five -= 3
                else:
                    return False
        return True
                    

            