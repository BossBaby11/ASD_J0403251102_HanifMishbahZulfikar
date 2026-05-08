#========================================
#Nama   : Hanif Mishbah Zulfikar 
#NIM    : J0403251102
#Kelas  : A2
#Tugas  : Latihan Konversi Matrix ke List
#=========================================

matrix = [
    [0,1,1,0],
    [1,0,1,0],
    [1,1,0,1],
    [0,0,1,0]
]

def convertToAdjList(matrix):
    adjList = {}
    for i in range(len(matrix)):
        adjList[i] = []
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                adjList[i].append(j)
    return adjList

    
if __name__ == "__main__":
    print(f"""Nama  : Hanif Mishbah Zulfikar 
NIM   : J0403251102
Kelas : A2
Materi: Konversi Matrix ke List""")
    adjList = convertToAdjList(matrix)
    for node in sorted(adjList):
        print(f"{node}: {adjList[node]}")