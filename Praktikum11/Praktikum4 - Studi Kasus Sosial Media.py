#========================================
#Nama   : Hanif Mishbah Zulfikar 
#NIM    : J0403251102
#Kelas  : A2
#Tugas  : Latihan Studi Kasus Sosial Media
#=========================================

# --- Data utama ---
nodes = ["Hanif", "Hafidz", "Yusuf", "Ilham", "Abi", "Rafi", "Adit"]
V = len(nodes)  # jumlah vertex = 7

# Edge dalam format (u, v) = u follow v
edges = [
    (0, 1),  # Hanif -> Hafidz
    (0, 2),  # Hanif -> Yusuf
    (0, 3),  # Hanif -> Ilham
    (0, 4),  # Hanif -> Abi
    (0, 5),  # Hanif -> Rafi
    (1, 0),  # Hafidz -> Hanif
    (1, 2),  # Hafidz -> Yusuf
    (1, 6),  # Hafidz -> Adit
    (2, 0),  # Yusuf -> Hanif
    (2, 1),  # Yusuf -> Hafidz
    (2, 3),  # Yusuf -> Ilham
    (3, 0),  # Ilham -> Hanif
    (3, 2),  # Ilham -> Yusuf
    (3, 4),  # Ilham -> Abi
    (4, 0),  # Abi -> Hanif
    (4, 3),  # Abi -> Ilham
    (5, 4),  # Rafi -> Abi
    (5, 6),  # Rafi -> Adit
    (6, 0),  # Adit -> Hanif
    (6, 5),  # Adit -> Rafi
]

# Fungsi untuk membuat adjacency list dan adjacency matrix
def buat_adjacency_list(V, edges):
    adj = [[] for _ in range(V)]
    for (u, v) in edges:
        adj[u].append(v)   # directed: hanya satu arah
    return adj


# Fungsi untuk membuat adjacency matrix
def buat_adjacency_matrix(V, edges):
    mat = [[0 for _ in range(V)] for _ in range(V)]
    for (u, v) in edges:
        mat[u][v] = 1      # directed: hanya satu arah
    return mat

# Fungsi untuk menampilkan adjacency list
def tampilkan_adjacency_list(adj, nodes):
    print("=" * 60)
    print("          ADJACENCY LIST - Media Sosial (Follow)")
    print("=" * 60)
    for i in range(len(adj)):
        tetangga = [nodes[j] for j in adj[i]]
        print(f"  {nodes[i]:<8} -->  {', '.join(tetangga)}")
    print()

# Fungsi untuk menampilkan adjacency matrix
def tampilkan_adjacency_matrix(mat, nodes):
    print("=" * 60)
    print("          ADJACENCY MATRIX - Media Sosial (Follow)")
    print("=" * 60)
    # Header kolom
    header = "         " + "  ".join(f"{n[:8]:>5}" for n in nodes)
    print(header)
    print("         " + "-" * (len(nodes) * 7))
    # Isi baris
    for i in range(len(mat)):
        baris = "  ".join(f"{mat[i][j]:>5}" for j in range(len(mat[i])))
        print(f"  {nodes[i]:<7} | {baris}")
    print()

# Fungsi untuk menjelaskan setiap baris adjacency matrix
def tampilkan_penjelasan_matrix(mat, nodes):
    print("=" * 60)
    print("          PENJELASAN SETIAP BARIS ADJACENCY MATRIX")
    print("=" * 60)
    for i in range(len(mat)):
        following = [nodes[j] for j in range(len(mat[i])) if mat[i][j] == 1]
        if following:
            print(f"  Baris {nodes[i]:<8}: follow -> {', '.join(following)}")
        else:
            print(f"  Baris {nodes[i]:<8}: tidak follow siapapun")
    print()

# PRogram utama
if __name__ == "__main__":
    # Format biodata
    print(f"""Nama  : Hanif Mishbah Zulfikar 
NIM   : J0403251102
Kelas : A2
Materi: Studi Kasus Sosial Media\n""")
    
    # Bangun struktur data
    adj = buat_adjacency_list(V, edges)
    mat = buat_adjacency_matrix(V, edges)

    # Tampilkan output
    tampilkan_adjacency_list(adj, nodes)
    tampilkan_adjacency_matrix(mat, nodes)
    tampilkan_penjelasan_matrix(mat, nodes)