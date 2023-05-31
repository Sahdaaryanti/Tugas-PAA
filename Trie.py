class TrieNode: #definisi kelas TrieNode yang merepresentasikan node dalam Trie
   def __init__(self): # inisialisasi (constructor) kelas TrieNode
       self.children = {} 
       self.endOfString = False


class Trie: #definisi kelas Trie yang akan digunakan untuk menyimpan dan mencari kata kunci dalam Trie.
   def __init__(self): #metode inisialisasi (constructor) kelas Trie
       self.root = TrieNode()
   def insertString(self, word): #memasukkan sebuah kata kunci ke dalam Trie.
       current = self.root #Menyimpan simpul awal (root) ke dalam variabel current.
       for i in word: #Melakukan iterasi untuk setiap karakter (i) dalam kata kunci.
           ch = i #Menyimpan karakter saat ini (i) ke dalam variabel ch.
           node = current.children.get(ch) #Mencari apakah simpul anak dengan karakter ch sudah ada dalam kamus children dari simpul current.
           if node == None: #Memeriksa apakah simpul anak dengan karakter ch belum ada.
               node = TrieNode() #Jika simpul anak belum ada, membuat simpul anak baru.
               current.children.update({ch:node}) #enambahkan simpul anak baru ke dalam kamus children dari simpul current.
           current = node #Memindahkan current ke simpul anak baru.
       current.endOfString = True #Menandai simpul saat ini sebagai akhir dari sebuah string.
  
   def searchString(self, prefix): #mencari kata kunci yang sesuai dengan awalan tertentu dalam Trie. 
       currentNode = self.root #Menginisialisasi variabel currentNode dengan akar Trie.
       for i in prefix: # Melakukan iterasi untuk setiap karakter dalam awalan prefix.
           node = currentNode.children.get(i) #Mengambil anak Trie yang terhubung dengan karakter saat ini.
           if node == None: #Memeriksa apakah anak Trie belum ada.
               return [] #Jika anak Trie belum ada, mengembalikan daftar kosong
           currentNode = node
       return self._getAllWordsFromNode(currentNode, prefix) #Memanggil metode _getAllWordsFromNode dengan simpul saat ini dan awalan sebagai argumen, dan mengembalikan daftar kata kunci yang sesuai dengan awalan tersebut.

   def _getAllWordsFromNode(self, node, prefix): #metode rekursif yang digunakan untuk mengumpulkan semua kata kunci yang sesuai dengan awalan dari simpul yang diberikan
       words = []#Membuat daftar kosong untuk menyimpan kata kunci yang ditemukan
       if node.endOfString: #Memeriksa apakah simpul saat ini adalah akhir dari sebuah string.
           words.append(prefix) #Jika simpul saat ini adalah akhir dari sebuah string, menambahkan awalan ke daftar kata kunci
       for key, childNode in node.children.items(): #Melakukan iterasi untuk setiap anak Trie dari simpul saat ini
           childWords = self._getAllWordsFromNode(childNode, prefix + key) #Memanggil metode _getAllWordsFromNode secara rekursif dengan anak Trie saat ini dan awalan yang diperbarui sebagai argumen, dan menyimpan hasilnya ke dalam childWords
           words.extend(childWords) #Menggabungkan daftar kata kunci dari anak Trie ke dalam daftar words
       return words #Mengembalikan daftar kata kunci yang ditemukan.

#Memasukkan kata kunci "apple", "application", dan "app" ke dalam Trie menggunakan metode insertString() pada objek keyword_trie.
keyword_trie = Trie()
keyword_trie.insertString("apple")
keyword_trie.insertString("application")
keyword_trie.insertString("app")

#Menginisialisasi variabel prefix dengan nilai awalan yang ingin dicari.
prefix = "app"
matching_keywords = keyword_trie.searchString(prefix)

print(f"Kata kunci yang sesuai dengan '{prefix}':")
#Melakukan iterasi pada daftar matching_keywords dan mencetak setiap kata kunci yang sesuai dengan awalan tersebut.
for keyword in matching_keywords:
   print(keyword)
