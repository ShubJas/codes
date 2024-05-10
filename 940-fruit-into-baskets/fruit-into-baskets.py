class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        


        hashmap =defaultdict(int)
        l = result= total = 0
        for r in range(len(fruits)):
            hashmap[fruits[r]] +=1

            while len(hashmap) > 2:
                curr = fruits[l]
                hashmap[curr] -= 1
                l+=1

                if not hashmap[curr]:
                    hashmap.pop(curr)
            
            result = max(result,r-l+1)
        return result

        