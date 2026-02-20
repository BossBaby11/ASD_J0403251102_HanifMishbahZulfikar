#========================================
#Nama  : Hanif Mishbah Zulfikar 
#NIM   : J0403251102
#Kelas : A2
#Tugas :Latihan Stack 
#=========================================
#Implementasi dasar stack
#=========================================

class Node:
    #konstruktor adalah fungsi yang dijalankan otomatis ketika class Node dipanggil/diinstalasi
    def __init__(self,data):
        self.data = data #menyimpan nilai atau data pada list
        self.next = None #pointer ini menunjuk ke note berikutnya
        
#stack ada operasi push(memasukkan head baru) dan pop (menghapus head)
class stack:
    def __init__(self):
        self.top = None #top menunjuk ke node paling atas(awalnya kosong)
    
    def is_empty(self):
        return self.top is None
    
    def push(self,data): #memasukkan data baru pada stack
        #1) membuat node baru
        new_node = Node(data) #instantiasi/memanggil konstruktor pada class Node
        
        #2) node baru harus menunjuk ke top yang lama(head yang lama)
        new_node.next = self.top
        
        #3) geser top ke node baru
        self.top = new_node
        
    def pop(self): #mengambil/menghapus node paling atas(top/head)
        if self.is_empty():
            print("Stack Kosong, tak bisa dipop")
            return None
        delete_data = self.top.data #soroti bagian top dan save di variable
        self.top = self.top.next
        return delete_data
    
    def peek(self):#Melihat data yang paling atas tanpa menghapus
        if self.is_empty():
            return None
        return self.top.data
    
    def display(self):
        current = self.top
        print("Head -> ", end=" ")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
        
#Instansitasi class stack
s = stack()
s.push("A")
s.push("B")
s.push("C")
s.push("D")
s.display()
s.pop()
s.display()
print("Peek (Lihat Top): ", s.peek())
s.pop()
s.display()
print("Peek (Lihat Top): ", s.peek())
