def modASCII(string, cellNumber): #deklarasi fungsi bernama modASCII yang memiliki dua parameter
    total = 0 # Membuat variabel total dan menginisialisasinya dengan nilai 0
    for i in string: #Melakukan iterasi untuk setiap karakter i dalam string.
        total += ord(i)#Menambahkan nilai ASCII dari karakter i ke variabel total menggunakan fungsi ord()
    return total % cellNumber #Mengembalikan sisa hasil pembagian total dengan cellNumber
  
message = "Hello, world!" #Mendefinisikan variabel message yang berisi string "Hello, world!". 
checksum_cells = 16 #Mendefinisikan variabel checksum_cells yang berisi bilangan bulat 16. 

checksum = modASCII(message, checksum_cells) #Memanggil fungsi modASCII dengan argumen message dan checksum_cells, dan menyimpan hasilnya ke dalam variabel checksum
print(f"Checksum dari pesan '{message}': {checksum}") #Mencetak hasil checksum
