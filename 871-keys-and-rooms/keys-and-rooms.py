class Solution:
    def dfs(self, room, rooms):
        # If this room has already been visited, return
        if self.visited[room]:
            return
        # Mark this room as visited
        self.visited[room] = True
        # Get the keys available in the current room
        can_unlock = rooms[room]

        # Recursively visit each room that can be unlocked with the keys available
        for i in can_unlock:
            self.dfs(i, rooms)

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # Number of rooms
        n = len(rooms)
        # Initialize the visited list to keep track of visited rooms
        self.visited = [False] * n
        
        # Start DFS from room 0
        self.dfs(0, rooms)

        # Check if all rooms have been visited
        # for x in self.visited:
        #     if not x:
        #         return False
        
        # If all rooms are visited, return True
        # return True
        
        return all(self.visited)
