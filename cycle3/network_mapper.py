import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
%matplotlib inline

# load data
df = pd.read_csv("data/book1.csv")
# pick only important weights (hard threshold)
df = df.loc[df['weight']>10, :]
df

# import
import networkx as nx
# load pandas df as networkx graph
G = nx.from_pandas_edgelist(df,
                            source='Source',
                            target='Target',
                            edge_attr='weight')
print("No of unique characters:", len(G.nodes))
print("No of connections:", len(G.edges))

# all graph options
graphs_viz_options = [nx.draw, nx.draw_networkx, nx.draw_circular, nx.draw_kamada_kawai, nx.draw_random, nx.draw_shell, nx.draw_spring]

# plot graph option
selected_graph_option = 0

# plot
plt.figure(figsize=(8,6), dpi=100)
graphs_viz_options[selected_graph_option](G)
