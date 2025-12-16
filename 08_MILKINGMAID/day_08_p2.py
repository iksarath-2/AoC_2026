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
    print(f"obtaining dists {jb1+1} out of {data.shape[0]}")
distlist.sort()
components = list([1,2])
i = 0
while len(components) > 1: 
    itemindex = np.where(dists == distlist[i])
    adj[itemindex[0][0]][itemindex[1][0]] = 1
    adj[itemindex[0][1]][itemindex[1][1]] = 1
    G = nx.from_numpy_array(adj)
    components = list(nx.connected_components(G))
    print(len(components))
    i += 1
    
print(data[itemindex[0][0]][0]*data[itemindex[1][0]][0])