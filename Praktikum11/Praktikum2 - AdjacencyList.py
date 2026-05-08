#========================================
#Nama   : Hanif Mishbah Zulfikar 
#NIM    : J0403251102
#Kelas  : A2
#Tugas  : Latihan Adjacency List
#=========================================

# Fungsi untuk membuat adjacency list dari daftar edge
def createGraph(edges):
    graph = {}

    for it in edges:
        u = it[0]
        v = it[1]

        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []

        graph[u].append(v)
        graph[v].append(u)

    return graph

if __name__ == "__main__":
    
    # Daftar edge yang menghubungkan node-node (dalam bentuk huruf)
    edges = [["A", "B"], ["A", "C"], ["B", "D"], ["D", "C"]]
    graph = createGraph(edges)

    print(f"""Nama  : Hanif Mishbah Zulfikar 
NIM   : J0403251102
Kelas : A2
Materi: Adjacency List secara huruf""")

    print("Adjacency List Representation:")
    for node in sorted(graph):
        print(f"{node}: {graph[node]}")