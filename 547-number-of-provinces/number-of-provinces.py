class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        def dfs(city):
            visited.add(city)
            for neighbour in range(n):
                if isConnected[city][neighbour]==1 and neighbour not in visited:
                    dfs(neighbour)
        provinces=0
        for city in range(n):
            if city not in visited:
                dfs(city)
                provinces+=1
        return provinces