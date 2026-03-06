#========================================
#Nama  : Hanif Mishbah Zulfikar 
#NIM   : J0403251102
#Kelas : A2
#Tugas :Latihan sorting 
#=========================================
#Latihan 10: Merge Sort Descending
#=========================================
def mergeSort(data): 
    print("Splitting ",data)
    if len(data)>1:             #Syarat rekursi jika data tersisa 1 maka rekursi akan berhenti
        mid = len(data)//2      #proses membagi dua datalist untuk mencari titik tengah
        lefthalf = data[:mid]   #proses membagi data dimana data dari index awal hingga tengah akan masuk ke bagian kiri
        righthalf = data[mid:]  #proses membagi data dimana data dari index tengah hingga akhir akan masuk ke bagian kanan
        mergeSort(lefthalf)     #proses rekursi yang akan terus membelah data sebelah kiri
        mergeSort(righthalf)    #proses rekursi yang akan terus membelah data sebelah kanan
        i=0                     #variabel yang akan digunakan untuk memasukkan data sebelah kiri
        j=0                     #variabel yang akan digunakan untuk memasukkan data sebelah kanan
        k=0                     #variabel untuk menempatkan kembali data ke list utama
        
        #proses membandingkan data kiri dan kanan dengan metode descending
        while i < len(lefthalf) and j < len(righthalf): 
            if lefthalf[i] >= righthalf[j]:
                data[k]=lefthalf[i]
                i=i+1
            else:
                data[k]=righthalf[j]
                j=j+1
            k=k+1
        #pengecekan kembali sisa data yang belum terurut disebelah kiri
        while i < len(lefthalf):
            data[k]=lefthalf[i]
            i=i+1
            k=k+1
        #pengecekan kembali sisa data yang belum terurut disebelah kanan
        while j < len(righthalf):
            data[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",data)
data = [0.1,0.5,0.7,0.8,0.9,0.99,0.19] #input data
mergeSort(data)                        #memasukkan data ke dalam fungsi
print(data)

#output = [0.99, 0.9, 0.8, 0.7, 0.5, 0.19, 0.1]
