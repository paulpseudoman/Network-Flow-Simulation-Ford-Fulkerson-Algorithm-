from collections import deque, defaultdict

class DinicMaxFlow:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)   # adjacency list
        self.capacity = defaultdict(lambda: defaultdict(int))
        self.original_capacity = defaultdict(lambda: defaultdict(int))

    def add_edge(self, u, v, cap):
        # Add directed edge u->v with given capacity
        self.graph[u].append(v)
        self.graph[v].append(u)   # reverse edge
        self.capacity[u][v] += cap
        self.capacity[v][u] += 0
        self.original_capacity[u][v] += cap
        self.original_capacity[v][u] += 0

    def _bfs_level(self, s, t, level):
        # Construct level graph using BFS
        for i in range(self.n):
            level[i] = -1
        level[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v in self.graph[u]:
                if level[v] < 0 and self.capacity[u][v] > 0:
                    level[v] = level[u] + 1
                    q.append(v)
        return level[t] >= 0

    def _dfs_flow(self, u, t, flow, level, next_iter):
        # DFS to send blocking flow
        if u == t:
            return flow
        while next_iter[u] < len(self.graph[u]):
            v = self.graph[u][next_iter[u]]
            if level[v] == level[u] + 1 and self.capacity[u][v] > 0:
                curr_flow = min(flow, self.capacity[u][v])
                pushed = self._dfs_flow(v, t, curr_flow, level, next_iter)
                if pushed > 0:
                    self.capacity[u][v] -= pushed
                    self.capacity[v][u] += pushed
                    return pushed
            next_iter[u] += 1
        return 0

    def dinic(self, s, t):
        # Compute max flow using Dinic's algorithm
        max_flow = 0
        level = [-1] * self.n

        while self._bfs_level(s, t, level):
            next_iter = [0] * self.n
            while True:
                pushed = self._dfs_flow(s, t, float("inf"), level, next_iter)
                if pushed == 0:
                    break
                max_flow += pushed

        return max_flow

    def _dfs_residual(self, s, visited):
        # DFS on residual graph to find reachable vertices
        stack = [s]
        visited[s] = True
        while stack:
            u = stack.pop()
            for v in self.graph[u]:
                if not visited[v] and self.capacity[u][v] > 0:
                    visited[v] = True
                    stack.append(v)

    def min_cut(self, s):
        # Find nodes reachable from s in residual graph and compute cut edges
        visited = [False] * self.n
        self._dfs_residual(s, visited)

        S = {i for i in range(self.n) if visited[i]}
        T = {i for i in range(self.n) if not visited[i]}

        # Edges from S → T in the original capacity graph
        cut_edges = [(u, v, self.original_capacity[u][v])
                     for u in S for v in self.graph[u]
                     if v in T and self.original_capacity[u][v] > 0]

        min_cut_value = sum(cap for _, _, cap in cut_edges)
        return min_cut_value, cut_edges


# Example usage
if __name__ == '__main__':
    mf = DinicMaxFlow(31)
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
    max_flow = mf.dinic(1, 30)
    print("Maximum Flow:", max_flow)

    min_cut_value, cut_edges = mf.min_cut(1)
    print("Min Cut Value:", min_cut_value)
    print("Cut Edges:", cut_edges)
