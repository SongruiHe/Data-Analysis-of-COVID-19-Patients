import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import community

# Read file
df = pd.read_csv('PatientInfo-label.csv')
df = df[['patient_id', 'infected_by']]
subset = df.dropna(axis=0, how='any')


# Find the nodes with mean centrality > threshold
def most_important(G):
    ranking = nx.betweenness_centrality(G).items()
    # print ranking
    r = [x[1] for x in ranking]
    m = sum(r) / len(r)  # mean centrality
    t = m * 10  # threshold
    Gt = G.copy()
    for k, v in ranking:
        if v < t:
            Gt.remove_node(k)
    return Gt


# Construct the edge list
G = nx.from_pandas_edgelist(subset, 'patient_id', 'infected_by')
spring_pos = nx.spring_layout(G)
# Community
part = community.best_partition(G)
values = [part.get(node) for node in G.nodes()]
nx.draw_networkx_nodes(G, spring_pos, cmap=plt.get_cmap('jet'), node_color=values, node_size=50, with_labels=False)
nx.draw_networkx_edges(G, spring_pos, alpha=0.1)
# Draw the central nodes with a circle and a label
Gt = most_important(G)
nx.draw_networkx_nodes(Gt, spring_pos, node_color='r', alpha=0.4, node_size=150)
nx.draw_networkx_labels(Gt, spring_pos, font_size=6, font_color='b')

#print(list(Gt.nodes))
plt.show()
