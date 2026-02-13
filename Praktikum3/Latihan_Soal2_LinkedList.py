#=================================
#Nama  : Hanif Mishbah Zulfikar 
#NIM   : J0403251102
#Kelas : A2
#Tugas :Latihan LinkedList 
#=================================
#=================================
#Latihan 2: Buat kode implementasikan pencarian pada node tertentu single circular linked list
#=================================
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularSinglyLinkedList1:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
    
    def display(self):
        if not self.head:
            print("List is empty")
            return
        print("Circular Linked List Traversal: ")
        temp = self.head
        print(temp.data, end = " -> ")
        temp = temp.next
        
        while temp != self.head:
            print(temp.data, end = " -> ")
            temp = temp.next
            
        print("...(back to head)")
    
    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

class CircularSinglyLinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
    
    def display(self):
        if not self.head:
            print("List is empty")
            return
        print("Circular Linked List Traversal: ")
        temp = self.head
        print(temp.data, end = " -> ")
        temp = temp.next
        
        while temp != self.head:
            print(temp.data, end = " -> ")
            temp = temp.next
            
        print("...(back to head)")
    
    def search(self, key):
        temp = self.head  
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False
     
class CircularSinglyLinkedListBlank:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
    
    def display(self):
        if not self.head:
            print("List is empty")
            return
        print("Circular Linked List Traversal: ")
        temp = self.head
        print(temp.data, end = " -> ")
        temp = temp.next
        
        while temp != self.head:
            print(temp.data, end = " -> ")
            temp = temp.next
            
        print("...(back to head)")
    
    def search(self, key):
        temp = self.head  
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

call = CircularSinglyLinkedList1()
for e in [3,7,12,19,25]:
    call.insert_at_end(e)
print("\n=== First List ===")
call.display()
if call.search(12):
    print("Data Found")
else:
    print("Data Not Found")

call2 = CircularSinglyLinkedList2()
for e in [5,10,15,20,30]:
    call2.insert_at_end(e)
print("\n=== Second List ===")
call2.display()
if call.search(25):
    print("Data Found")
else:
    print("Data Not Found")

call0 = CircularSinglyLinkedListBlank()
print("\n=== Blank List ===")
call0.display()
if call0.search(10):
    print("Data Found")
else:
    print("Data Not Found")
# search_number = int(input("Masukkan Angka yang ingin dicari: "))
# if call.search(search_number):
#     print("Data Found")
# else:
#     print("Data Not Found")
        
            
