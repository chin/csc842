import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import nmap3

# load data
df = pd.read_csv("./network.csv")

# load pandas df as networkx graph
G = nx.from_pandas_edgelist(df,
                            source='SRC_FQDN',
                            target='DEST_FQDN')
print("No of unique servers:", len(G.nodes), "\n")
for x in G.nodes:
    print(x)
print("\nNo of connections:", len(G.edges), "\n")

# all graph options
graphs_viz_options = [nx.draw, nx.draw_networkx, nx.draw_circular, nx.draw_kamada_kawai, nx.draw_random, nx.draw_shell, nx.draw_spring]

# plot graph option
selected_graph_option = 0

# plot
print("Drawing Graph now...")
plt.figure(figsize=(8,6), dpi=100)
graphs_viz_options[selected_graph_option](G, with_labels=True)
plt.show()
print("Saving figure as graph.png")
plt.savefig("graph.png")


print("\nScanning open ports on available servers...")
for y in G.nodes:
    nmap = nmap3.Nmap()
    results_ports = nmap.scan_top_ports(y)
    print(results_ports)


print("\nScanning tcp ports on available servers...")
nmap = nmap3.NmapScanTechniques()
for z in G.nodes:
    results_tcp = nmap.nmap_tcp_scan(z)
    print(results_tcp)

print("\nPinging on available server...")
for a in G.nodes:
    results_ping = nmap.nmap_ping_scan(a)
    print(results_ping)
