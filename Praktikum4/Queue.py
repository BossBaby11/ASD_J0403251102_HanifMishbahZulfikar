#========================================
#Nama  : Hanif Mishbah Zulfikar 
#NIM   : J0403251102
#Kelas : A2
#Tugas :Latihan Queue 
#=========================================
#Implementasi dasar Queue
#=========================================
class Node:
    #konstruktor adalah fungsi yang dijalankan otomatis ketika class Node dipanggil/diinstalasi
    def __init__(self,data):
        self.data = data #menyimpan nilai atau data pada list
        self.next = None #pointer ini menunjuk ke note berikutnya

class queue:
    #Membuat konstruktor untuk inisialisasi variable front and rear
    def __init__(self):
        self.front = None #Node paling depan
        self.rear = None #Node paling belakang
    
    def is_empty(self):
        return self.front is None
    
    #membuat fungsi untuk menambahkan data baru pada data paling belakang 
    def enqueue(self,data):
        new_node = Node(data) #menambahkan data baru
        #Jika queue kosong, front dan rear meenunjuk ke node yang sama
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
            return
        #Jika queue tidak kosong, maka letakkan data baru ke rear dan jadikan data baru sebagai front
        self.rear.next = new_node #letakkan data baru pada setelahnya rear
        self.rear = new_node #jadikan data baru sebagai rear
    
    def dequeue(self):
        #Menghapus data dari depan/front
        delete_data = self.front.data
        self.front = self.front.next
        
        #jika setelah geser front menjadi none, maka rear harus none
        if self.front is None:
            self.rear = None
        return delete_data
    
    def display(self):
        current = self.front
        print("Front ->", end=" ")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("rear")
        
#Instansiasi class queue
q = queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.display()
q.dequeue()
q.display()