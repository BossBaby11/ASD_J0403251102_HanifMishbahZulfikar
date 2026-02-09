# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
# Nama  : Hanif Mishbah Zulfikar
# NIM   : J0403251102
# Kelas : A2
# ==========================================================
# -------------------------------
# Konstanta nama file
# -------------------------------
stock_file = "./Praktikum2/data_barang.txt"
# -------------------------------
# Fungsi: Membaca data dari file
# -------------------------------
def read_stock(stock_file):    
# """Membaca data stok dari file teks.
# Format per baris: KodeBarang,NamaBarang,Stok
# Output:
# - stok_dict (dictionary)
# key = kode_barang
# value = {"nama": nama_barang, "stok": stok_int}
# """    
    stock_dict = {}
# TODO: Buka file dan baca seluruh baris
# Hint: with open(nama_file, "r", encoding="utf-8") as f:
# TODO: Untuk setiap baris:
# - gunakan strip() untuk menghilangkan \n
# - split(",") untuk memisahkan kolom
# - simpan ke dictionary
    with open(stock_file, 'r', encoding='utf-8') as f:
        for baris in f:
            baris = baris.strip()
            kode, nama, stok = baris.split(",")
            stock_dict[kode]={"nama": nama, "stok": int(stok)}
        return stock_dict

# -------------------------------
# Fungsi: Menyimpan data ke file
# -------------------------------
def save_stock(stock_file, stock_dict):
# """
# Menyimpan seluruh data stok ke file teks.
# Format per baris: KodeBarang,NamaBarang,Stok
# """
# TODO: Tulis ulang seluruh isi file berdasarkan stok_dict
# Hint: with open(nama_file, "w", encoding="utf-8") as f:
    with open(stock_file, 'w', encoding='utf-8') as f:
        for kode in sorted(stock_dict.keys()):
            nama = stock_dict[kode]["nama"]
            stok = stock_dict[kode]["stok"]
            f.write(f"{kode}, {nama}, {stok}\n") 
    pass

# -------------------------------
# Fungsi: Menampilkan semua data
# -------------------------------
def show_all_stock(stock_dict):
# """
# Menampilkan semua barang di stok_dict.
# """
# TODO: Jika kosong, tampilkan pesan stok kosong
# TODO: Tampilkan dengan format rapi: kode | nama | stok
    print("\n========= DAFTAR STOK BARANG =========")
    print(f"{'    KODE' : <10} | {'    NAMA' : <12} | {' JUMLAH STOK' : >5}")
    print("-" * 36)#Create Line
    #Show Dictionary Value
    for kode in sorted(stock_dict.keys()):
        nama = stock_dict[kode]["nama"]
        stok = stock_dict[kode]["stok"]
        print(f"{kode: <10} | {nama: <12} | {int(stok): >5}")
    pass

# -------------------------------
# Fungsi: Cari barang berdasarkan kode
# -------------------------------
def search_stock(stock_dict):
# """
# Mencari barang berdasarkan kode barang.
# """
    search_code = input("Masukkan kode barang: ").strip().upper()
# TODO: Cek apakah kode ada di dictionary
# Jika ada: tampilkan detail barang
# Jika tidak ada: tampilkan 'Barang tidak ditemukan'
    if search_code in stock_dict:
        nama = stock_dict[search_code]["nama"]
        stok = stock_dict[search_code]["stok"]
        print("======  DATA BARANG DITEMUKAN =====")
        print(f"NIM   : {search_code}")
        print(f"Nama  : {nama}")
        print(f"Stok  : {stok}")
    else: print("Data tidak ditemukan. Pastikan KODE yang dimasukkan benar!!!")
    pass

# -------------------------------
# Fungsi: Tambah barang baru
# -------------------------------
def add_stock(stock_dict, stock_file):
# """
# Menambah barang baru ke stok_dict.
# """
    kode = input("Masukkan kode barang baru: ").strip().upper()
    if kode in stock_dict:
        print("Kode barang sudah digunakan, pastikan KODE yang anda masukkan belum digunakan!")
        return
    nama = input("Masukkan nama barang: ").strip()
    check_name = [item["nama"].lower() for item in stock_dict.values()]
    if nama.lower() in check_name:
        print("Nama barang sudah digunakan, pastikan NAMA yang anda masukkan belum digunakan!")
        return
    try:
        stok_awal = int(input("Masukkan jumlah barang: "))
    except ValueError:
        print("Masukkan harus berupa ANGKA, silahkan coba lagi")
        return
    stock_dict[kode] = {"nama": nama, "stok": int(stok_awal)} 
    with open(stock_file, 'a', encoding='utf-8') as f:
        f .write(f"\n{kode},{nama},{int(stok_awal)}")
# TODO: Validasi kode tidak boleh duplikat
# Jika sudah ada: tampilkan 'Kode sudah digunakan' dan return
# TODO: Input stok awal (integer)
# Hint: stok_awal = int(input(...))
# TODO: Simpan ke dictionary
    pass

# -------------------------------
# Fungsi: Update stok barang
# -------------------------------
def update_stock(stock_dict):
# """
# Mengubah stok barang (tambah atau kurangi).
# Stok tidak boleh menjadi negatif.
# """
    kode = input("Masukkan kode barang yang ingin diupdate: ").upper().strip()
# TODO: Cek apakah kode ada di dictionary
# Jika tidak ada: tampilkan pesan dan return
    if kode not in stock_dict:
        print("Barang yang anda cari tidak ada pada daftar, pastikan anda memasukkan KODE dengan tepat!")
        return
    print("Pilih jenis update:")
    print("1. Tambah stok")
    print("2. Kurangi stok")
# TODO: Input jumlah perubahan stok
# Hint: jumlah = int(input("Masukkan jumlah: "))
    try: 
        pilihan = int(input("Masukkan pilihan (1/2): "))
    except ValueError:
        print("Masukkan harus berupa angka silahkan coba kembali")
# TODO:
# - Jika pilihan 1: stok = stok + jumlah
# - Jika pilihan 2: stok = stok - jumlah
# - Jika hasil < 0: batalkan dan tampilkan error
    if pilihan == 1:
        try:
            add = int(input("Masukkan jumlah yang ingin ditambahkan: "))
        except ValueError:
            print("Masukkan harus berupa ANGKA, silahkan coba kembali!")
        if add < 0:
            print("Angka harus lebih besar dari 0")
            return
        stok_awal = stock_dict[kode]["stok"]
        stok_terbaru = stok_awal + add
        stock_dict[kode]["stok"] = stok_terbaru
        print(f"Update berhasil. Nilai {kode} berubah dari {stok_awal} menjadi {stok_terbaru}")
    elif pilihan == 2:
        try:
            minus = int(input("Masukkan jumlah yang ingin dikurangi: "))
        except ValueError:
            print("Masukkan harus berupa ANGKA, silahkan coba kembali!")
        if minus < 0:
            print("Angka harus lebih besar dari 0")
        stok_awal = stock_dict[kode]["stok"]
        stok_terbaru = stok_awal - minus
        stock_dict[kode]["stok"] = stok_terbaru
        if stok_terbaru < 0:
            print("Jumlah stok tidak boleh kurang dari 0. Perubahan dibatalkan")
        else: 
            print(f"Update berhasil. Nilai {kode} berubah dari {stok_awal} menjadi {stok_terbaru}")
    else:
        print("Pilih opsi dengan memasukkan angka antara 1 (menambah) atau 2(mengurangi)!")
        return
    pass

# -------------------------------
# Program Utama
# -------------------------------
def main():
# Membaca data dari file saat program mulai
    stok_barang = read_stock(stock_file)
    while True:
        print("\n=== MENU STOK BARANG ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")
        option = input("Pilih menu: ").strip()
        if option == "1":
            show_all_stock(stok_barang)
        elif option == "2":
            search_stock(stok_barang)
        elif option == "3":
            add_stock(stok_barang, stock_file)
        elif option == "4":
            update_stock(stok_barang)
        elif option == "5":
            save_stock(stock_file, stok_barang)
            print("Data berhasil disimpan.")
        elif option == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan program utama
if __name__ == "__main__":
    main()


