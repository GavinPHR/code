import collections


class Search:

    def bfs(self, graph: dict):
        self.visited = {v: False for v in graph.keys()}
        self.Q = collections.deque()
        for v in graph.keys():
            if not self.visited[v]:
                self.bfsFromVertex(graph,v)

    def bfsFromVertex(self, graph: dict, v: str):
        self.visited[v] = True
        print(v)
        self.Q.append(v)
        while self.Q:
            v = self.Q.popleft()
            for w in graph[v]:
                if not self.visited[w]:
                    self.visited[w] = True
                    print(w)
                    self.Q.append(w)


if __name__ == '__main__':
    graph = {"n": ["p"],
             "p": ["s"],
             "s": ["v","w","t"],
             "t": ["u","x"],
             "u": ["t","z"],
             "z": ["y"],
             "y": ["y","z"],
             "x": ["w","y"],
             "w": ["x"],
             "v": ["q","r","w"],
             "r": ["s"],
             "q": ["o"],
             "o": ["n","p"]
             }
    s = Search()
    s.bfs(graph)
