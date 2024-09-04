class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        

        def dist(x,y):
            return x**2 + y **2
        
        maxD = 0
        x = y = 0
        d = 0

        obstacles = set(map(tuple,obstacles))
        for c in commands:
            print(x,y)
            if c == -1:
                d = (d + 1) % 4
            elif c == -2:
                d = (d + 3) % 4
            else:

                if d==0:
                    for _ in range(c):
                        y+=1
                        
                        if (x,y) in obstacles:
                            y-=1
                            break
                elif d== 1:
                    for _ in range(c):
                        x+=1
                        # print(x,y)
                        if (x,y) in obstacles:
                            x-=1
                            break
                elif d == 2:
                    for _ in range(c):
                        y-=1
                        if (x,y) in obstacles:
                            y+=1
                            break
                else:
                    for _ in range(c):
                        x-=1
                        if (x,y) in obstacles:
                            x+=1
                            break
                
                maxD = max(maxD,dist(x,y))

        return maxD




