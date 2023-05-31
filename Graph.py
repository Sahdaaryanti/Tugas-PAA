from collections import deque

class Graph: # definisi kelas Graph yang akan digunakan untuk merepresentasikan graf dan melakukan operasi
    def __init__(self, gdict=None):#inisialisasi (constructor) kelas Graph
        if gdict is None: #Memeriksa apakah argumen gdict diberikan saat membuat objek Graph.
            gdict = {} #Jika argumen gdict tidak diberikan, kita inisialisasi gdict dengan kamus kosong.
        self.gdict = gdict # Menyimpan kamus gdict ke dalam atribut gdict pada objek Graph
    
    def addEdge(self, vertex, edge): #menambahkan tepi (edge) ke dalam graf.
        self.gdict[vertex].append(edge) #enambahkan simpul tujuan ke daftar yang terhubung dengan simpul awal dalam kamus gdict.
    
    def bfs(self, startVertex, targetVertex): #menerima dua parameter: startVertex (simpul awal) dan targetVertex (simpul tujuan yang ingin dicapai).
        visited = set() # Membuat himpunan kosong visited untuk melacak simpul-simpul yang sudah dikunjungi selama BFS
        queue = deque([[startVertex]])#Membuat deque queue yang berisi daftar dengan simpul awal startVertex
        
        if startVertex == targetVertex:#Memeriksa apakah simpul awal sama dengan simpul tujuan.
            print("Kamu Sudah Berada DiKebun Binatang") #mencetak kalimat
            return
        
        while queue: #Melakukan iterasi selama antrian queue tidak kosong.
            path = queue.popleft() #Menghapus jalur pertama dari antrian queue dan menyimpannya ke dalam path.
            lastVertex = path[-1] #Mengambil simpul terakhir dari jalur path.
            
            if lastVertex == targetVertex: # Memeriksa apakah simpul terakhir sama dengan simpul tujuan.
                print("Jalur Menuju kebun Binatang Ditemukan : \n", ' -> '.join(path)) #Jika simpul terakhir sama dengan simpul tujuan, mencetak jalur menuju kebun binatang.
                return
            
            if lastVertex not in visited: #Memeriksa apakah simpul terakhir belum dikunjungi.
                visited.add(lastVertex) #Menambahkan simpul terakhir ke dalam himpunan visited untuk menandai bahwa simpul tersebut sudah dikunjungi.
                for adjacentVertex in self.gdict[lastVertex]: #: Melakukan iterasi untuk setiap simpul terhubung dengan simpul terakhir.
                    new_path = list(path) # Membuat salinan baru dari jalur path
                    new_path.append(adjacentVertex) #Menambahkan simpul terhubung ke jalur baru.
                    queue.append(new_path) #Menambahkan jalur baru ke dalam antrian queue.
        
        print("Jalan Menuju Kebun Binatang Tidak Ditemukan") #mencetak kalimat
        return
      
#Membuat kamus khusus customDict yang merepresentasikan graf dengan simpul-simpul yang terhubung.      
customDict = {
    "Rumah": ["Sekolah", "Pasar"],
    "Sekolah": ["Rumah", "Kebun Binatang", "Sungai"],
    "Pasar": ["Rumah", "Kebun Binatang", "Rumah Sakit"],
    "Kebun Binatang": ["Sekolah", "Pasar"],
    "Sungai": ["Sekolah"],
    "Rumah Sakit": ["Pasar"]
}

g = Graph(customDict) #Membuat objek g dari kelas Graph dengan menggunakan kamus khusus customDict
g.bfs("Rumah", "Kebun Binatang") #Memanggil metode bfs pada objek g
