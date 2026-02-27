#==========================================
#Nama  : Hanif Mishbah Zulfikar 
#NIM   : J0403251102
#Kelas : A2
#Tugas :Latihan Rekursif 
#===========================================
#Contoh Rekursi 3: Menjumlahkan Element List
#===========================================
def jumlah_list(data, index=0):
    #Base case: jika index sudah mencapai panjang list
    if index == len(data):
        return 0
    
    #recursive case: elemen sekarang + jumlah elemen setelahnya
    return data[index] + jumlah_list(data, index + 1 )
print(jumlah_list([2,4,6,8])) #output 20