class Graph:
    
    def __init__(self):
        self.graph = {}


    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.graph:
            self.graph[src] = []
        if dst not in self.graph:
            self.graph[dst] = []
        if dst not in self.graph[src]:
            self.graph[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.graph:
            return False
        if dst not in self.graph[src]:
            return False
        self.graph[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        visit = set()
        return self.dfs(src, dst, visit)

    def dfs(self, cur, target, visit):
        if cur in visit:
            return False

        if cur == target:
            return True

        visit.add(cur)
        for neigh in self.graph[cur]:
            if self.dfs(neigh, target, visit):
                return True
        # visit.remove(cur)

        return False
        
