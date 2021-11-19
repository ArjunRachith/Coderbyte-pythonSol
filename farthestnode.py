# Python3 implementation to find the
# farthest node from each vertex
# of the tree
  
# Add edge between
# U and V in tree
def AddEdge(u, v):
     
    global adj
     
    # Edge from U to V
    adj[u].append(v)
  
    # Edge from V to U
    adj[v].append(u)
  
# DFS to find the first
# End Node of diameter
def findFirstEnd(u, p):
     
    global lvl, adj, end1, maxi
     
    # Calculating level of nodes
    lvl[u] = 1 + lvl[p]
     
    if (lvl[u] > maxi):
        maxi = lvl[u]
        end1 = u
  
    for i in range(len(adj[u])):
  
        # Go in opposite
        # direction of parent
        if (adj[u][i] != p):
            findFirstEnd(adj[u][i], u)
  
# Function to clear the levels
# of the nodes
def clear(n):
     
    global lvl, dist1, dist2
     
    # Set all value of lvl[]
    # to 0 for next dfs
    for i in range(n + 1):
        lvl[i] = 0
  
    # Set maximum with 0
    maxi = 0
    dist1[0] = dist2[0] = -1
  
# DFS will calculate second
# end of the diameter
def findSecondEnd(u, p):
     
    global lvl, adj, maxi, end2
     
    # Calculating level of nodes
    lvl[u] = 1 + lvl[p]
     
    if (lvl[u] > maxi):
        maxi = lvl[u]
  
        # Store the node with
        # maximum depth from end1
        end2 = u
  
    for i in range(len(adj[u])):
         
        # Go in opposite
        # direction of parent
        if (adj[u][i] != p):
            findSecondEnd(adj[u][i], u)
  
# Function to find the distance
# of the farthest distant node
def findDistancefromFirst(u, p):
     
    global dist1, adj
     
    # Storing distance from
    # end1 to node u
    dist1[u] = 1 + dist1[p]
     
    for i in range(len(adj[u])):
        if (adj[u][i] != p):
            findDistancefromFirst(adj[u][i], u)
  
# Function to find the distance
# of nodes from second end of diameter
def findDistancefromSecond(u, p):
     
    global dist2, adj
     
    # Storing distance from end2 to node u
    dist2[u] = 1 + dist2[p]
     
    for i in range(len(adj[u])):
        if (adj[u][i] != p):
            findDistancefromSecond(adj[u][i], u)
  
def findNodes():
     
    global adj, lvl, dist1, dist2, end1, end2, maxi
    n = 5
  
    # Joining Edge between two
    # nodes of the tree
    AddEdge(1, 2)
    AddEdge(1, 3)
    AddEdge(3, 4)
    AddEdge(3, 5)
  
    # Find the one end of
    # the diameter of tree
    findFirstEnd(1, 0)
    clear(n)
  
    # Find the other end
    # of the diameter of tree
    findSecondEnd(end1, 0)
  
    # Find the distance
    # to each node from end1
    findDistancefromFirst(end1, 0)
  
    # Find the distance to
    # each node from end2
    findDistancefromSecond(end2, 0)
  
    for i in range(1, n + 1):
        x = dist1[i]
        y = dist2[i]
  
        # Comparing distance between
        # the two ends of diameter
        if (x >= y):
            print(end1, end = " ")
        else:
            print(end2, end = " ")
  
# Driver code
if __name__ == '__main__':
     
    adj = [[] for i in range(10000)]
    lvl = [0 for i in range(10000)]
    dist1 = [-1 for i in range(10000)]
    dist2 = [-1 for i in range(10000)]
    end1, end2, maxi = 0, 0, 0
     
    # Function Call
    findNodes()
 
# This code is contributed by mohit kumar 29
