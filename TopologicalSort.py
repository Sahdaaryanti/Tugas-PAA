from collections import defaultdict

class Schedule:#membuat class schedule yang digunakan untuk menyimpana & mengatur jadwal nonton fil
    def __init__(self): #menginialisasi constructur class schedule
        self.graph = defaultdict(list) #menginialisasi atribut graph untuk menyimpan ketergantungan film
    
    def addFilm(self, film, dependencies): #menambahkan film ke jadwal dengan ketergantungan film terhadap film lain
        for dependency in dependencies:#melakukan iterasi untuk setiap film dalam daftar
            self.graph[dependency].append(film) #menambahkan fil, ke dalam daftar, yang mempresentasikan film yang bergantung pada dependency
    
    def topologicalSortUtil(self, v, visited, stack):#metode utilitas (rekursif) untuk melakukan penyelesaian topologis pada graf ketergantungan.
        visited.add(v)#Menambahkan film saat ini ke dalam himpunan 

        for dependency in self.graph[v]: #Melakukan iterasi untuk setiap film yang bergantung pada film saat in
            if dependency not in visited: # Memeriksa apakah film ketergantungan belum dikunjungi.
                self.topologicalSortUtil(dependency, visited, stack)#Memanggil metode topologicalSortUtil secara rekursif untuk film ketergantungan

        stack.insert(0, v) #Memasukkan film saat ini ke dalam tumpukan stack. Karena algoritma Topological Sort memproses film tergantung terlebih dahulu, film akan dimasukkan ke dalam tumpukan di awal.
    
    def scheduleFilms(self):#metode untuk menyusun jadwal penontonan film menggunakan algoritma Topological Sort. 
        visited = set()#Membuat himpunan kosong visited untuk melacak film-film yang sudah dikunjungi.
        stack = [] #Membuat daftar kosong stack untuk menyimpan urutan film yang sudah diproses.

        for film in list(self.graph):#Melakukan iterasi untuk setiap film dalam daftar kunci self.graph.
            if film not in visited:#Memeriksa apakah film belum dikunjungi.
                self.topologicalSortUtil(film, visited, stack)# Memanggil metode topologicalSortUtil untuk memulai penyelesaian topologis dari film saat ini.

        return stack # Mengembalikan tumpukan stack yang berisi urutan film yang harus ditonton

schedule = Schedule() #Membuat objek schedule dari kelas Schedule.
#Menambahkan film-film ke dalam schedule dengan menyebutkan ketergantungan antara film-film tersebut.
schedule.addFilm("Avengers: Infinity War", [])
schedule.addFilm("Captain America: Civil War", ["Avengers: Infinity War"])
schedule.addFilm("Avengers: Endgame", ["Captain America: Civil War"])
schedule.addFilm("Spider-Man: Far From Home", ["Avengers: Endgame"])
schedule.addFilm("Spider-Man: No Way Home", ["Spider-Man: Far From Home"])

#Mencetak urutan film yang harus ditonton ke layar.
film_schedule = schedule.scheduleFilms()
print("Urutan Film Yang Harus Ditonton Lebih Dulu (kebergantungan):")
for film_schedule in film_schedule:
    print(film_schedule)
