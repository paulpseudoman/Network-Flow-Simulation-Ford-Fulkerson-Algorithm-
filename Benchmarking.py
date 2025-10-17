import timeit

setup_code = """
from __main__ import DinicMaxFlow
mf = DinicMaxFlow(6)
mf.add_edge(0, 1, 16)
mf.add_edge(0, 2, 13)
mf.add_edge(1, 2, 10)
mf.add_edge(2, 1, 4)
mf.add_edge(1, 3, 12)
mf.add_edge(2, 4, 14)
mf.add_edge(3, 2, 9)
mf.add_edge(4, 3, 7)
mf.add_edge(3, 5, 20)
mf.add_edge(4, 5, 4)
"""

stmt_code = "mf.dinic(0, 5)"

print(timeit.timeit(stmt=stmt_code, setup=setup_code, number=10))
