#========================================
#Nama  : Hanif Mishbah Zulfikar 
#NIM   : J0403251102
#Kelas : A2
#Tugas :Latihan sorting 
#=========================================
#Latihan 12: Quick Sort Descending
#=========================================
def quickSort(data):
    quickSortHelper(data,0,len(data)-1)
def quickSortHelper(data,first,last):
    if first<last:
        splitpoint = partition(data,first,last)
        quickSortHelper(data,first,splitpoint-1)
        quickSortHelper(data,splitpoint+1,last)
def partition(data,first,last):
    pivotvalue = data[first]
    leftmark = first+1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and data[leftmark] >= pivotvalue:
            leftmark = leftmark + 1
        while data[rightmark] <= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1
        if rightmark < leftmark:
            done = True
        else:
            temp = data[leftmark]
            data[leftmark] = data[rightmark]
            data[rightmark] = temp
    temp = data[first]
    data[first] = data[rightmark]
    data[rightmark] = temp
    return rightmark
data = [0.1,0.2,0.3,0.4,0.5,0.21,0.22,0.32,0.54,0.14]
quickSort(data)
print(data)