from collections import defaultdict
class MaxFlow:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(dict)
        self.original_graph = defaultdict(dict)
        self.edges = []
    def add_edge(self, u, v, capacity):
        """Add edge to graph (directed)"""
        if v in self.graph[u]:
            self.graph[u][v] += capacity  # handle multiple edges
            self.original_graph[u][v] += capacity
        else:
            self.graph[u][v] = capacity
            self.original_graph[u][v] = capacity
        if u not in self.graph[v]:
            self.graph[v][u] = 0  # reverse edge
        if u not in self.original_graph[v]:
            self.original_graph[v][u] = 0

    def _dfs(self, s, t, visited, parent):
        """DFS to find augmenting path"""
        stack = [s]
        visited[s] = True
        while stack:
            u = stack.pop()
            for v in self.graph[u]:
                if not visited[v] and self.graph[u][v] > 0:
                    parent[v] = u
                    visited[v] = True
                    if v == t:
                        return True
                    stack.append(v)
        return False

    def ford_fulkerson(self, s, t):
        parent = [-1] * self.n
        max_flow = 0

        while True:
            visited = [False] * self.n
            if not self._dfs(s, t, visited, parent):
                break

            # find bottleneck
            path_flow = float("inf")
            v = t
            while v != s:
                u = parent[v]
                path_flow = min(path_flow, self.graph[u][v])
                v = u

            # update residual
            v = t
            while v != s:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = u

            max_flow += path_flow

        return max_flow

    def min_cut(self, s):
        """Find nodes reachable from s in residual graph and compute cut edges"""
        visited = [False] * self.n
        self._dfs_residual(s, visited)

        S = {i for i in range(self.n) if visited[i]}
        T = {i for i in range(self.n) if not visited[i]}

        # edges from S → T in the original graph
        cut_edges = [(u, v, self.original_graph[u][v])
                     for u in S for v in self.original_graph[u]
                     if v in T and self.original_graph[u][v] > 0]

        min_cut_value = sum(cap for _, _, cap in cut_edges)
        return min_cut_value, cut_edges

    def _dfs_residual(self, s, visited):
        """DFS on residual graph to find reachable vertices"""
        stack = [s]
        visited[s] = True
        while stack:
            u = stack.pop()
            for v, cap in self.graph[u].items():
                if cap > 0 and not visited[v]:
                    visited[v] = True
                    stack.append(v)

# Example usage
if __name__ == '__main__':
    mf = MaxFlow(31)
    mf.add_edge(1, 2, 5)
    mf.add_edge(1, 7, 8)
    mf.add_edge(2, 3, 7)
    mf.add_edge(2, 8, 6)
    mf.add_edge(3, 4, 4)
    mf.add_edge(3, 9, 10)
    mf.add_edge(4, 5, 3)
    mf.add_edge(4, 10, 9)
    mf.add_edge(5, 6, 7)
    mf.add_edge(5, 11, 5)
    mf.add_edge(6, 12, 11)
    mf.add_edge(7, 8, 2)
    mf.add_edge(7, 13, 9)
    mf.add_edge(8, 9, 8)
    mf.add_edge(8, 14, 12)
    mf.add_edge(9, 10, 6)
    mf.add_edge(9, 15, 10)
    mf.add_edge(10, 11, 7)
    mf.add_edge(10, 16, 8)
    mf.add_edge(11, 12, 5)
    mf.add_edge(11, 17, 9)
    mf.add_edge(12, 18, 6)
    mf.add_edge(13, 14, 4)
    mf.add_edge(13, 19, 10)
    mf.add_edge(14, 15, 8)
    mf.add_edge(14, 20, 7)
    mf.add_edge(15, 16, 5)
    mf.add_edge(15, 21, 12)
    mf.add_edge(16, 22, 9)
    mf.add_edge(17, 18, 3)
    mf.add_edge(17, 23, 11)
    mf.add_edge(18, 19, 7)
    mf.add_edge(18, 24, 10)
    mf.add_edge(19, 20, 6)
    mf.add_edge(19, 25, 8)
    mf.add_edge(20, 21, 4)
    mf.add_edge(20, 26, 9)
    mf.add_edge(21, 22, 10)
    mf.add_edge(21, 27, 5)
    mf.add_edge(22, 28, 6)
    mf.add_edge(23, 24, 7)
    mf.add_edge(23, 29, 8)
    mf.add_edge(24, 25, 6)
    mf.add_edge(24, 30, 9)
    mf.add_edge(25, 26, 5)
    mf.add_edge(26, 27, 7)
    mf.add_edge(27, 28, 4)
    mf.add_edge(28, 29, 6)
    mf.add_edge(29, 30, 8)

    max_flow = mf.ford_fulkerson(1, 30)
    print("Maximum Flow:", max_flow)

    min_cut_value, cut_edges = mf.min_cut(1)
    print("Min Cut Value:", min_cut_value)
    print("Cut Edges:", cut_edges)
