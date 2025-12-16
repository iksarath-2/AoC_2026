import pandas as pd
import numpy as np
import networkx as nx

df = pd.read_csv("08_MILKINGMAID/d08_input.txt", header=None)
data = df.to_numpy()

def d(xyz1, xyz2):
    s = 0
    for i in range(3):
        s += (xyz1[i]-xyz2[i])**2
    dist = np.sqrt(s)
    return dist

# first make a graph to represent the network of junction boxes (jbs) via an adjacency matrix
adj = np.zeros([data.shape[0],data.shape[0]],dtype=int)

dists = np.zeros([data.shape[0],data.shape[0]])
distlist = list()
for jb1 in range(data.shape[0]):
    for jb2 in range(data.shape[0]):
        if jb2 != jb1:
            dist = d(data[jb1],data[jb2])
            dists[jb1,jb2] = dist
            dists[jb2,jb1] = dist
            distlist.append(dist)
distlist.sort()

for i in range(2*1000): ## 2*number of connections: 1 for jb1-jb2, 1 for jb2-jb1
    itemindex = np.where(dists == distlist[i])
    print(itemindex)
    adj[itemindex[0][0]][itemindex[1][0]] = 1
    adj[itemindex[0][1]][itemindex[1][1]] = 1

G = nx.from_numpy_array(adj)
components = list(nx.connected_components(G))
sizes = list(len(cc) for cc in components)
sizes.sort(reverse=True)
print(sizes)

np.savetxt("08_MILKINGMAID/d08_adjacency_matrix_first1000.txt",adj,fmt='%s')

print(sizes[0]*sizes[1]*sizes[2])