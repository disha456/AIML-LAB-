#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import defaultdict
class graph:
    
    def __init__(self):
        self.graph = defaultdict(list)
    #fubnction to add edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def DFSUtil(self,v,visited):
    #mark the current node as visited and print it
        visited.add(v)
        print(v,end=' ')
    #recr for all the vertices adjacdent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour,visited)

    def DFS(self,v):
        visited=set()

        self.DFSUtil(v,visited)
#create a graph given in the above diagram
g = graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)

print("following is in dfs starting from vertex 2\n")
g.DFS(0)


# In[ ]:




