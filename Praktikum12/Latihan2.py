# ==========================================================
#Nama     : Hanif Mishbah Zulfikar 
#NIM      : J0403251102
#Kelas    : A2
#Latihan 2: Implementasi Dijkstra
# ==========================================================

import heapq
from tracemalloc import start
# Weighted graph dengan bobot positif
graph = {
 'A': {'B': 4, 'C': 2},
 'B': {'D': 5},
 'C': {'D': 1},
 'D': {}
}
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    # Jarak dari start ke start adalah 0
    distances[start] = 0
    # Priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
    # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat,
    # maka proses dilewati
        if current_distance > distances[current_node]:
            continue
    # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
    # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances
hasil = dijkstra(graph, 'A')
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

# Jawaban Analisis:
# 1. Berapa jarak terpendek dari A ke B?
# Jawaban: Jarak terpendek dari A ke B adalah 4.

# 2. Berapa jarak terpendek dari A ke C?
# Jawaban: Jarak terpendek dari A ke C adalah 2.

# 3. Berapa jarak terpendek dari A ke D?
# Jawaban: Jarak terpendek dari A ke D adalah 3.

# 4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B?
# Jawaban: Jarak A ke D melalui C adalah 2 + 1 = 3, sedangkan jarak A ke D melalui B adalah 4 + 5 = 9.

# 5. Apa fungsi priority_queue dalam algoritma Dijkstra?
# Jawaban: priority_queue digunakan untuk menyimpan pasangan (jarak, node) dan memastikan bahwa node dengan jarak terpendek selalu diproses pertama.

# 6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif?
# Jawaban: Dijkstra tidak cocok untuk graph dengan bobot negatif karena algoritma ini mengasumsikan bahwa semua bobot adalah positif, dan penggunaan bobot negatif dapat menyebabkan hasil yang tidak benar.