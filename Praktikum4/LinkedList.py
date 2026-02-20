#========================================
#Nama  : Hanif Mishbah Zulfikar 
#NIM   : J0403251102
#Kelas : A2
#Tugas :Latihan LinkedList 
#=========================================
#Implementasi dasar Node pada Linked List
#=========================================

class node:
    #konstruktor adalah fungsi yang dijalankan otomatis ketika class Node dipanggil/diinstalasi
    def __init__(self,data):
        self.data = data #menyimpan nilai atau data pada list
        self.next = None #pointer ini menunjuk ke note berikutnya

#1) Membuat node dengan instantiasi class node
nodeA = node("A")
nodeB = node("B")
nodeC = node("C")

#2) Mendefinisikan head dan Menghubungkan Node A -> B -> C -> None
head = nodeA
nodeA.next = nodeB
nodeB.next = nodeC

#3)Traversal menelusuri node dari head sampai None
current = head
while current is not None:
    print(current.data) #menampilkan data pada node saat ini 
    current = current.next #pindah ke node berikutnya



