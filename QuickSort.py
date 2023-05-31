def swap(my_list, index1, index2): #eklarasi fungsi swap yang mengambil tiga argumen
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1] #pernyataan tukar (swap) yang menukar elemen di index1 dengan elemen di index2 dalam my_list

def pivot(my_list, pivot_index, end_index): #deklarasi fungsi pivot yang mengambil tiga argumen: my_list (daftar yang akan diurutkan), pivot_index (indeks pivot) dan end_index (indeks akhir dari bagian daftar yang sedang diproses).
    swap_index = pivot_index #Menginisialisasi swap_index dengan nilai pivot_index.
    for i in range(pivot_index+1, end_index+1): #Melakukan iterasi untuk setiap elemen dalam daftar mulai dari pivot_index+1 hingga end_index+1.
        if my_list[i] < my_list[pivot_index]: #Memeriksa apakah elemen my_list[i] lebih kecil dari elemen di pivot_index.
            swap_index += 1 #Meningkatkan swap_index dengan 1
            swap(my_list, swap_index, i) # Memanggil fungsi swap untuk menukar elemen di swap_index dengan elemen di i
    swap(my_list, pivot_index, swap_index) #Menukar elemen di pivot_index dengan elemen di swap_index
    return swap_index #Mengembalikan nilai swap_index sebagai hasil dari fungsi pivot.

def quicksort_helper(my_list, left, right): #deklarasi fungsi quicksort_helper yang melakukan rekursi dalam algoritma quicksort
    if left < right: #Memeriksa apakah left lebih kecil dari right, yang menandakan bahwa masih ada lebih dari satu elemen dalam bagian daftar yang sedang diproses.
        pivot_index = pivot(my_list, left, right) #Memanggil fungsi pivot untuk menemukan indeks pivot dalam bagian daftar yang sedang diproses.
        quicksort_helper(my_list, left, pivot_index-1) #Memanggil secara rekursif quicksort_helper untuk bagian daftar yang berada di sebelah kiri pivot.
        quicksort_helper(my_list, pivot_index+1, right) #Memanggil secara rekursif quicksort_helper untuk bagian daftar yang berada di sebelah kanan pivot.
    return my_list #Mengembalikan daftar yang telah diurutkan

def quicksort(my_list): #deklarasi fungsi quicksort yang mengambil satu argumen my_list (daftar yang akan diurutkan).
    return quicksort_helper(my_list, 0, len(my_list)-1) #Mengembalikan hasil dari pemanggilan fungsi tersebut.

nama_mahasiswa = ['Naeyon', 'Jake', 'Sahda', 'Hanbin', 'Felix'] #Mendefinisikan sebuah daftar nama_mahasiswa yang berisi nama-nama mahasiswa yang akan diurutkan
nama_terurut = quicksort(nama_mahasiswa) #Memanggil fungsi quicksort untuk mengurutkan nama_mahasiswa dan menyimpan hasilnya ke dalam variabel nama_terurut

#Mencetak hasil
print("Daftar Nama Mahasiswa Yang Belum Terurut :\n", nama_mahasiswa)
print("Daftar Nama Mahasiswa Yang Sudah Terurut Terurut :\n", nama_terurut)
