#=================================
#Nama  : Hanif Mishbah Zulfikar 
#NIM   : J0403251102
#Kelas : A2
#Tugas :Latihan LinkedList 
#=================================
#=================================
#Latihan 4: Buat metode untuk menggabungkan dua single linked list menjadi satu linked list baru
#=================================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList1:
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
    def merge(self, other_list):
        if not self.head: 
            self.head = other_list.head
            self.tail = other_list.tail
        elif other_list.head: 
            self.tail.next = other_list.head
            self.tail = other_list.tail
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("Null")
        
class LinkedList2:
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
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("Null")

class LinkedList3:
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
    
    def merge(self, other_list):
        if not self.head: 
            self.head = other_list.head
            self.tail = other_list.tail
        elif other_list.head: 
            self.tail.next = other_list.head
            self.tail = other_list.tail
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("Null")

class LinkedList4:
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
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("Null")
       
call1 = LinkedList1()
for e in [1,3,5,7]:
    call1.insert_at_end(e)
print("=== Linked List 1 ===")
call1.display()

call2 = LinkedList2()
for e in [2,4,6,8]:
    call2.insert_at_end(e)
print("\n=== Linked List 2 ===")
call2.display()

#Merging List 1 and 2
call1.merge(call2)
print("\n=== Merge Linked List 1 and 2 ===")
call1.display()
    
call3 = LinkedList3()
for e in [5,15,25]:
    call3.insert_at_end(e)
print("\n=== Linked List 3 ===")
call3.display()

call4 = LinkedList4()
print("\n=== Linked List 4 ===")
call4.display()

#Merging List 3 and 4
call3.merge(call4)
print("\n=== Merge Linked List 3 and 4 ===")
call3.display()