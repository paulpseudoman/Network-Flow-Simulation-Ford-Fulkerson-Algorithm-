import pandas as pd
import networkx as nx
from pyvis.network import Network
import os, webbrowser
# Load CSV file
df = pd.read_csv("D:\scotland yard data(Sheet1).csv")

# Initialize a directed graph
G = nx.Graph()

# Add edges with capacities
for _, row in df.iterrows():
    G.add_edge(row['source'], row['target'], capacity=row['weight'])

print("Value: ", nx.maximum_flow_value(G.to_directed(),1,200))
