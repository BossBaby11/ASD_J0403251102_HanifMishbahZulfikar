#========================================
#Nama   : Hanif Mishbah Zulfikar 
#NIM    : J0403251102
#Kelas  : A2
#Tugas  : Latihan Adjacency Matrix
#=========================================

def createGraph(V, edges): # Fungsi dengan parameter V = jumlah vertex, edges = list of edge
    mat = [[0 for _ in range(V)] for _ in range(V)] # Membuat matriks VxV dengan nilai awal 0
    
    # Mengisi matriks berdasarkan edges yang diberikan
    for it in edges:
        u = it[0]
        v = it[1]
        mat[u][v] = 1
        mat[v][u] = 1
    return mat

# Implementasi Kode
if __name__ == "__main__":
    V = 4 # Jumlah vertex

    # List of edges yang menghubungkan vertex-vertex
    edges = [[0, 1], [0, 2], [1, 2], [2, 3]]

    # Membuat adjacency matrix berdasarkan vertex dan edges yang diberikan
    mat = createGraph(V, edges)
    
    # format biodata
    print(f"""Nama  : Hanif Mishbah Zulfikar 
NIM   : J0403251102
Kelas : A2
Materi: Adjacency Matrix""")
    
    # Menampilkan adjacency matrix
    print("Adjacency Matrix Representation:")
    for i in range(V):
        for j in range(V):
            print(mat[i][j], end=" ")
        print()
        
