class Solution:
    def dfs(self,room,rooms):
        if self.visited[room]:
            return
        self.visited[room] = True
        can_unlock = rooms[room]

        for i in can_unlock:
            self.dfs(i,rooms)

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        n = len(rooms)
        self.visited = [False] * n  
        

        self.dfs(0,rooms)

        # for x in self.visited:
        #     if not x:
        #         return False
        
        return all(self.visited)

        