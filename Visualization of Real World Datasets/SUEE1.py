import pandas as pd
import networkx as nx
from pyvis.network import Network
import os, webbrowser

# ---- Load CSV safely ----
df = pd.read_csv("D:\SUEE1.csv")   # use raw string to avoid escape errors

# ---- Initialize directed graph (change to Graph() if undirected) ----
G = nx.Graph()

# ---- Add edges with weights ----
for _, row in df.iterrows():
    G.add_edge(str(row["source"]), str(row["target"]), weight=int(row["weight"]))

# ---- Create PyVis network ----
net = Network(height="750px", width="100%", directed=False,
              bgcolor="#222222", font_color="white")

# ---- Add nodes ----
for node in G.nodes():
    net.add_node(str(node), label=str(node))

# ---- Add edges with weight labels ----
for u, v, data in G.edges(data=True):
    w = data["weight"]
    net.add_edge(
        str(u), str(v),
        label=str(w),
        title=f"Weight: {w}",
        color="rgba(150,150,255,0.8)",
        width=2,
        font={"size": 14, "color": "orange", "align": "top"}
    )

# ---- Layout (slow, smooth animation) ----
net.force_atlas_2based(
    gravity=-50,
    central_gravity=0.01,
    spring_length=100,
    spring_strength=0.001,
    damping=0.95
)
out_file = "SUEE1.html"
net.write_html(out_file)
webbrowser.open('file://' + os.path.realpath(out_file))
