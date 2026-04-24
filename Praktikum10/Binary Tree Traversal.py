#========================================
#Nama  : Hanif Mishbah Zulfikar 
#NIM   : J0403251102
#Kelas : A2
#Tugas :Latihan Binary Tree Traversal
#=========================================

class Node: #Definisikan kelas node untuk membuat binary tree
    def __init__(self, x): #definisikan fungsi init untuk inisialisasi node dengan nilai x
        self.left = None #inisialisasi left child dengan None
        self.right = None #inisialisasi right child dengan None
        self.x = x #inisialisasi nilai x pada node dengan nilai yang diberikan saat pembuatan node
        
    def insert(self, x): #definisikan fungsi insert untuk menambahkan nilai x ke dalam binary tree
        if self.x:
            #Jika nilai x yang akan dimasukkan lebih kecil dari nilai x pada node saat ini, maka akan masuk ke subtree kiri
            if x < self.x:
                if self.left is None:
                    self.left = Node(x)
                else:
                    self.left.insert(x)
            #Jika nilai x yang akan dimasukkan lebih besar dari nilai x pada node saat ini, maka akan masuk ke subtree kanan       
            elif x > self.x:
                if self.right is None:
                    self.right = Node(x)
                else:
                    self.right.insert(x)
            else:
                self.x = x
    
    #Definisikan fungsi untuk melakukan pengecekan node secara berurutan dari kiri > root > kanan            
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.x)
            res = res + self.inorderTraversal(root.right)
        return res

    #Definisikan fungsi untuk melakukan pengecekan node secara berurutan dari root > kiri > kanan
    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.x)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res
    
    #Definisikan fungsi untuk melakukan pengecekan node secara berurutan dari kiri > kanan > root
    def PostorderTraversal(self, root):
        res = []
        if root:
            res = res + self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.x)
        return res
    

#Membuat binary tree dengan root node bernilai 2, 
#Lalu menambahkan beberapa nilai ke dalam tree menggunakan fungsi insert
root = Node(2)
root.insert(32)
root.insert(22)
root.insert(22)
root.insert(12)
root.insert(32)
root.insert(37)

#Menampilkan hasil traversal inorder, preorder, dan postorder dari binary tree yang telah dibuat
print("""
==============================
Nama  : Hanif Mishbah Zulfikar
NIM   : J0403251102   
==============================""")
print("Inorder Traversal    : ", root.inorderTraversal(root))
print("Preorder Traversal   : ", root.PreorderTraversal(root))
print("Postorder Traversal  : ", root.PostorderTraversal(root))