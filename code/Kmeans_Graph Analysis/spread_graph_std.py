import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import community


# Use community to detect the community in the graph
df = pd.read_csv('PatientInfo-label.csv')
df = df[['patient_id', 'infected_by']]
subset = df.dropna(axis=0, how='any')

G = nx.from_pandas_edgelist(subset, 'patient_id', 'infected_by')
spring_pos = nx.spring_layout(G)

# Draw the graph, colors based on nodes' degree
'''
    egrees = G.degree()
    values = [degrees[node] for node in G.nodes()]
    nx.draw_spring(G, cmap='coolwarm', node_color=values, node_size=10, with_labels=False)
    plt.show()
'''

part = community.best_partition(G)
values = [part.get(node) for node in G.nodes()]
# Draw the graph using networkX
nx.draw_spring(G, cmap=plt.get_cmap('jet'), node_color=values, node_size=10, with_labels=False, edge_color="gray")
plt.show()
