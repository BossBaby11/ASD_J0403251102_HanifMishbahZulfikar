# ==========================================================
#Nama       : Hanif Mishbah Zulfikar 
#NIM        : J0403251102
#Kelas      : A2
#Latihan 1  : Memahami Konsep Spanning Tree
# ==========================================================
#Graph tersebut memiliki beberapa kemungkinan spanning tree.
#Buatlah program Python sederhana yang:
#1. Menampilkan daftar edge pada graph.
#2. Menampilkan contoh spanning tree yang valid.
#3. Menampilkan jumlah edge pada graph awal.
#4. Menampilkan jumlah edge pada spanning tree.
#Gunakan list atau dictionary sederhana untuk menyimpan data edge

# Daftar edge graph
edges = [
 ('A', 'B'),
 ('A', 'C'),
 ('A', 'D'),
 ('C', 'D'),
 ('B', 'D')
]
# Contoh spanning tree
spanning_tree = [
 ('A', 'C'),
 ('C', 'D'),
 ('D', 'B')
]
print("Edge pada graph:")
for edge in edges: #Menampilkan daftar edge pada graph
 print(edge)
print("\nSpanning Tree:")
for edge in spanning_tree: #Menampilkan contoh spanning tree yang valid
 print(edge)
print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

# Jawaban Analisis:
# 1. Apa perbedaan graph awal dan spanning tree?
# Graph awal adalah representasi lengkap dari sebuah graf, termasuk semua vertex dan edge. 
# Spanning tree adalah subgraf yang menghubungkan semua vertex dalam graf dengan jumlah edge yang minimal dan tidak memiliki siklus/perulangan.

# 2. Mengapa spanning tree tidak boleh memiliki cycle?
# Karena jika spanning tree memiliki siklus, maka ada edge yang berlebihan yang tidak diperlukan untuk menghubungkan semua vertex,
# sehingga tidak memenuhi syarat sebagai tree.

# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
# Karena spanning tree hanya mencakup edge yang diperlukan untuk menghubungkan semua vertex tanpa membentuk siklus, 
# sehingga jumlah edge-nya selalu n-1, di mana n adalah jumlah vertex.