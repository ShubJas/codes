class Solution:
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):

        root_x = self.find(x)
        root_y = self.find(y)

        if root_x ==root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            root_x,root_y = root_y, root_x

        self.rank[root_x] += self.rank[root_y]
        self.parent[root_y] = root_x
        return True
              

    def removeStones(self, stones: List[List[int]]) -> int:
        n =len(stones)
        self.parent = list(range(n))
        self.rank = [1] * n

        X ={}
        Y = {}
        count = 0
        for i,(x,y) in enumerate(stones):

            if x in X:
                count += self.union(i,X[x])
            else:
                X[x] = i
            

            if y in Y:
                count += self.union(i,Y[y])
            else:
                Y[y] = i
        
        return count
            

        