#Nama: Hanif Mishbah Zulfikar 
#NIM: J0403251102
#==========================================================
#Praktikum 1 : Konsep ADT dan File Handing
#Latihan Dasar 1 : Membaca seluruh isi file data
#==========================================================

file_path = "data_mahasiswa.txt" 
print("\n===Membuka file dalam satu string===")
with open(file_path, 'r', encoding = "utf-8") as file: #Membuka file txt berdasarkan variabel yang diberikan dengan 'r' sebagai mode read
    content = file.read() #membaca isi file sebagai satu baris/index
print(content) #cetak content

print("\n===Membuka file per baris===")
jumlah_baris = 0 #variabel kosong berindex 
with open(file_path, 'r', encoding = "utf-8") as file: #Membuka file dengan mode read 
    for  baris in file: #looping untuk 
        jumlah_baris = jumlah_baris + 1 #counter index berkelanjutan 
        baris = baris.strip() #menghilangkan karakter baris baru
        print("Baris ke-", jumlah_baris)
        print("isinya = ", baris)

#=====================================================================
#Praktikum 1 : Konsep ADT dan File Handing
#Latihan Dasar 2 : Parsing
#=====================================================================

#Parsing Value
print("\n===Mememecah data dalam file===")
with open(file_path, 'r', encoding = "utf-8") as file: #Membuka file dengan mode read 
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")#menghilangkan tanda koma
        print("NIM: ", nim, "|", "Nama: ", nama, "|", "Nilai: ", nilai)

#=====================================================================
#Praktikum 1 : Konsep ADT dan File Handing
#Latihan Dasar 3 : Membaca Data dan Menyimpannya ke Struktur Data List
#=====================================================================

#Input Pada List
data_list = []
with open(file_path, 'r', encoding = "utf-8") as file: #Membuka file dengan mode read 
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        data_list.append([nim, nama, int(nilai)]) #proses menyimpan data ke dalam list

print("\n===Menampilkan data dalam list===")
print(data_list)
print("Data Pertama: ", data_list[0])

#======================================================================
#Praktikum 1 : Konsep ADT dan File Handing
#Latihan Dasar 4 : Membaca Data dan Menyimpannya ke Struktur Dictionary
#======================================================================

data_dic = {}
with open(file_path, 'r', encoding = "utf-8") as file: #Membuka file dengan mode read 
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        #simpan data dalam dictionary
        data_dic[nim]={
            "Nama ": nama,
            "Nilai ": int(nilai)
        }
print("\n===Menampilkan data dalam dictionary===")
print(data_dic)