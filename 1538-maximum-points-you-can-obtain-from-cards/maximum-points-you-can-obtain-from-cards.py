class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        total = sum(cardPoints)
        winlength = len(cardPoints)- k
        winsum = sum(cardPoints[:winlength])
        result = total - winsum
        for i in range(winlength,len(cardPoints)):
            winsum = winsum + cardPoints[i] - cardPoints[i - winlength]
            result = max(result, total - winsum)

        return result
            

        