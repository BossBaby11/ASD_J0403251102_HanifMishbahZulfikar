#=========================================================================
#Nama  : Hanif Mishbah Zulfikar 
#NIM   : J0403251102
#Kelas : A2
#Tugas :Latihan Rekursif 
#=========================================================================
#Contoh Rekursi 4: Backtracking kombinasi biner dengan batas '1' (pruning)
#=========================================================================
def biner_batas(n, batas, hasil="", jumlah_1 = 0):
    #Pruning: jika jumlah_1 sudah melewati batas, berhenti
    if jumlah_1 > batas:
        return
    #Base case
    if len(hasil) == n:
        print(hasil)
        return
    
    #pilih '0'
    biner_batas(n, batas ,hasil + "0", jumlah_1)
    
    #pilih '1'
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1)
    
biner_batas(4,2)