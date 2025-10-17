import pandas as pd
import networkx as nx
from pyvis.network import Network
import os, webbrowser

# ---- Load CSV ----
# Must have columns: src, dst, weight
df = pd.read_csv("D:\internetTrafficPorts(in).csv")

G = nx.DiGraph()
for _, row in df.iterrows():
    G.add_edge(str(row["source"]), str(row["target"]), weight=int(row["fwd"]))
    G.add_edge(str(row["target"]), str(row["source"]), weight=int(row["bwd"]))
# ---- Create PyVis network ----
net = Network(height="750px", width="100%", directed=True, notebook=False,
              bgcolor="#222222", font_color="white")

# Add nodes manually to ensure visibility
for node in G.nodes():
    net.add_node(str(node), label=str(node))

# Add edges manually to preserve 'weight'
for u, v, data in G.edges(data=True):
    w = data["weight"]
    net.add_edge(u, v, label=str(w), title=f"Weight: {w}",
                 color="rgba(150,150,255,0.8)",
                 font={"size": 14, "color": "orange", "align": "top"})

# ---- Optional layout tuning ----
net.force_atlas_2based(gravity=-50, central_gravity=0.01,
                       spring_length=100, spring_strength=0.001,damping=0.95)
# ---- Save and open ----
out_file = "GPort.html"
net.write_html(out_file)
webbrowser.open('file://' + os.path.realpath(out_file))
