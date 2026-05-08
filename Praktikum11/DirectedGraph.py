#========================================
#Nama   : Hanif Mishbah Zulfikar 
#NIM    : J0403251102
#Kelas  : A2
#Materi : Adjacency List -> Directed Graph
#=========================================

def createGraph(V, edges):
    adj = [[] for _ in range(V)]
    
    for it in edges:
        u = it[0]
        v = it[1]
        adj[u].append(v)
    return adj

if __name__ == "__main__":
    V = 3
    
    edges = [[1, 0], [1, 2], [2, 0]]
    
    adj = createGraph(V, edges)
    
    print("Adjacency List Representation:")
    for i in range(V):
        print(f"{i}:", end=" ")
        for j in adj[i]:
            print(j, end=" ")
        print()