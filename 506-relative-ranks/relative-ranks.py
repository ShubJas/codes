class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        answer = [""]  * len(score)

        hashset ={score[i]: i for i in range(len(score))}

        score.sort(reverse = True)


        for i in range(len(score)):
            if i==0:
                answer[hashset[score[i]]] = "Gold Medal"
            elif i==1:
                answer[hashset[score[i]]] = "Silver Medal"
            elif i ==2:
                answer[hashset[score[i]]] = "Bronze Medal"
            else:
                answer[hashset[score[i]]] = str(i+1)
        return answer

        