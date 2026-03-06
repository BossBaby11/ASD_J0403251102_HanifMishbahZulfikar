#========================================
#Nama  : Hanif Mishbah Zulfikar 
#NIM   : J0403251102
#Kelas : A2
#Tugas :Latihan sorting 
#=========================================
#Latihan 5: Insertion Sort Ascending
#=========================================
def insertionSort(data):
    for index in range(1,len(data)):
        currentvalue = data[index]
        position = index
        while position>0 and data[position-1]>currentvalue:
            data[position]=data[position-1] 
            position = position-1
        data[position]=currentvalue
data = [54,26,93,17,77,31,44,55,20]
insertionSort(data)
print(data)

#output = [17, 20, 26, 31, 44, 54, 55, 77, 93]