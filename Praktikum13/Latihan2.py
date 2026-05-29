# ==========================================================
#Nama       : Hanif Mishbah Zulfikar 
#NIM        : J0403251102
#Kelas      : A2
#Latihan 2  : Implementasi Sederhana Algoritma Kruskal
# ==========================================================

# Daftar edge: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
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
# 1. Edge mana yang dipilih pertama kali?
# Edge (1, 'C', 'D') dipilih pertama kali karena memiliki bobot terkecil.

# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
# Karena algoritma Kruskal memilih edge dengan bobot terkecil untuk memastikan bahwa spanning tree yang dihasilkan memiliki bobot total yang minimum.

# 3. Berapa total bobot MST yang dihasilkan?
# Total bobot MST yang dihasilkan adalah 6.

# 4. Mengapa edge tertentu tidak dipilih?
# Edge tertentu tidak dipilih karena jika ditambahkan, akan membentuk siklus dalam spanning tree, yang melanggar syarat bahwa spanning tree tidak boleh memiliki siklus.