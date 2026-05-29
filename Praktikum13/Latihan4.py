# ==========================================================
#Nama       : Hanif Mishbah Zulfikar 
#NIM        : J0403251102
#Kelas      : A2
#Latihan 4  : Studi Kasus: Jaringan Kabel Antar Gedung
# ==========================================================

#Deskripsi Kasus
#Sebuah kampus ingin membangun jaringan kabel internet antar gedung dengan biaya
#minimum. Setiap hubungan antar gedung memiliki biaya pemasangan kabel yang
#berbeda. Data hubungan gedung:
#GedungA - GedungB = 4
#GedungA - GedungC = 2
#GedungB - GedungD = 3
#GedungC - GedungD = 1
#GedungA - GedungD = 5
#Buatlah program menggunakan algoritma Prim atau Kruskal untuk menentukan
#jaringan kabel dengan total biaya minimum. Ketentuan Program harus memuat:
#• Representasi weighted graph.
#• Implementasi Prim atau Kruskal.
#• Output edge yang dipilih.
#• Output total biaya minimum.
#• Komentar penjelasan program.

# Daftar edge: (bobot, node1, node2)
edges = [
    (4, 'GedungA', 'GedungB'),
    (2, 'GedungA', 'GedungC'),
    (3, 'GedungB', 'GedungD'),
    (1, 'GedungC', 'GedungD'),
    (5, 'GedungA', 'GedungD')
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
# 1. Algoritma apa yang digunakan?
# Algoritma yang digunakan adalah algoritma Kruskal, yang memilih edge dengan bobot terkecil terlebih dahulu untuk membangun minimum spanning tree (MST) tanpa membentuk siklus.

# 2. Edge mana saja yang dipilih?
# Edge yang dipilih adalah: (GedungC, GedungD, 1), (GedungA, GedungC, 2), dan (GedungB, GedungD, 3)

# 3. Berapa total biaya minimum?
# Total biaya minimum adalah 6.

# 4. Mengapa MST cocok digunakan pada kasus ini?
# MST cocok digunakan pada kasus ini karena tujuannya adalah untuk menghubungkan semua gedung dengan biaya minimum tanpa membentuk siklus.