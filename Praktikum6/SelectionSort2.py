#========================================
#Nama  : Hanif Mishbah Zulfikar 
#NIM   : J0403251102
#Kelas : A2
#Tugas :Latihan sorting 
#=========================================
#Latihan 4: Selection Sort Descending
#=========================================
def selectionSort(data):
    for fillslot in range(len(data)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            if data[location] < data[positionOfMax]:
                positionOfMax = location
                # Swap
        temp = data[fillslot]
        data[fillslot] = data[positionOfMax]
        data[positionOfMax] = temp
data = [50,51,45,1.1,0.1,0.11,10.21,10.25,10.2501]
selectionSort(data)
print(data)

# Output = [51, 50, 45, 10.2501, 10.25, 10.21, 1.1, 0.11, 0.1]