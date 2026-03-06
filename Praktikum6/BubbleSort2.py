#========================================
#Nama  : Hanif Mishbah Zulfikar 
#NIM   : J0403251102
#Kelas : A2
#Tugas :Latihan sorting 
#=========================================
#Latihan 2: Bubble Sort Descending
#=========================================
def bubbleSort(data):
    for passnum in range(len(data)-1,0,-1):
        for i in range(passnum):
            if data[i]<data[i+1]:
# Tukar dua data bersebelahan yang urutannya salah
                temp = data[i]
                data[i] = data[i+1]
                data[i+1] = temp
data = [10.1,10.15,10.25,10.14,10.11,10.123,10.12]
bubbleSort(data)
print(data)

# Output = [10.25, 10.15, 10.14, 10.123, 10.12, 10.11, 10.1]