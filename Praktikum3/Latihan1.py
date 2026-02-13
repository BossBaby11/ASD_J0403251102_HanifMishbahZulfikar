#=================================
#Nama  : Hanif Mishbah Zulfikar 
#NIM   : J0403251102
#Kelas : A2
#Tugas :Latihan LinkedList 
#=================================
#Latihan 1: Implementasikan fungsi untuk menghapus node dengan nilai tertentu
#=================================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None 
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def delete_node(self,key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp and temp.data !=key:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("Null")
        
call = LinkedList()
for e in [3,5,13,2]:
    call.insert_at_end(e)

print("Create Linked List") 
call.display()
call.delete_node(2)
print("Delete Linked List Element : 2")
call.display()

