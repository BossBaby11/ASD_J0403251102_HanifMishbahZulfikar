#========================================
#Nama  : Hanif Mishbah Zulfikar 
#NIM   : J0403251102
#Kelas : A2
#Tugas :Latihan sorting 
#=========================================
#Latihan 6: Insertion Sort Descending
#=========================================
def insertionSort(data):
    for index in range(1,len(data)):
        currentvalue = data[index]
        position = index
        while position > 0 and data[position-1] < currentvalue:
            data[position]=data[position-1] 
            position = position-1
        data[position]=currentvalue
data = [0.1,0.11,0.101]
insertionSort(data)
print(data)

#output = [0.11, 0.101, 0.1]