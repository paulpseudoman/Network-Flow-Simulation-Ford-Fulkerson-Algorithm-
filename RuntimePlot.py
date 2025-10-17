import time

def benchmark(algorithm_name, func):
    start = time.time()
    max_flow = func()
    end = time.time()
    print(f"{algorithm_name}: flow={max_flow}, time={end - start:.6f} seconds")

# Example:
# benchmark("Dinic", lambda: mf.dinic(0, 5))
# benchmark("Edmonds-Karp", lambda: mf.edmonds_karp(0, 5))
# benchmark("Ford-Fulkerson DFS", lambda: mf.ford_fulkerson(0, 5))
