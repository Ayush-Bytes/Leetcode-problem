class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        visited = set()
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def dfs(start):
            visited.add(start)
            if start == destination:
                return True
            for neighbour in graph[start]:
                if neighbour not in visited:
                    if dfs(neighbour):
                        return True
            return False
        return dfs(source)
