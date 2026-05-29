# ==========================================================
#Nama       : Hanif Mishbah Zulfikar 
#NIM        : J0403251102
#Kelas      : A2
#Latihan 5  : Studi Kasus: Jaringan Komputer
# ==========================================================

# Kasus 2 . Jaringan Komputer
# RouterA - RouterB = 3
# RouterA - RouterC = 2
# RouterB - RouterD = 5
# RouterC - RouterD = 1
# RouterB - RouterC = 4
#Ketentuan Program. Program harus memuat:
#1. Representasi weighted graph.
#2. Implementasi Kruskal atau Prim.
#3. Output MST.
#4. Output total bobot minimum.
#5. Komentar penjelasan program.

# Daftar edge: (bobot, node1, node2)
edges = [
    (3, 'RouterA', 'RouterB'),
    (2, 'RouterA', 'RouterC'),
    (5, 'RouterB', 'RouterD'),
    (1, 'RouterC', 'RouterD'),
    (4, 'RouterB', 'RouterC')
]
# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()
mst = []
total_weight = 0
connected = set()
for weight, u, v in edges:
 # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
print("Total bobot =", total_weight)

# Jawaban Analisis:
# 1. Kasus apa yang dipilih?
# Kasus yang dipilih adalah kasus jaringan komputer

# 2. Algoritma apa yang digunakan?
# Algoritma yang digunakan adalah algoritma Kruskal, yang memilih edge dengan bobot terkecil terlebih dahulu untuk membangun minimum spanning tree (MST) tanpa membentuk siklus.

# 3. Edge mana saja yang dipilih dalam MST?
# Edge yang dipilih adalah: (RouterC, RouterD, 1), (RouterA, RouterC, 2), dan (RouterA, RouterB, 3)

# 4. Berapa total bobot MST?
# Total bobot MST adalah 6.

# 5. Mengapa edge tertentu tidak dipilih?
# Edge (RouterB, RouterC, 4) tidak dipilih karena akan membentuk siklus jika ditambahkan ke MST.