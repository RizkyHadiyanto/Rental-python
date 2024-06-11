def baca():                          #membuat fungsi untuk membaca file data yang diberikan 
    try:
        with open("teks.txt", "r") as raw:  # Membaca file txt dalam suatu variabel
            lines = raw.readlines()                      # Dipisahkan perbarisnya menjadi kumpulan list
            pisah = [x.split() for x in lines]         # Dipisahkan lagi perbarisnya menggunakan split()
            data = []         # Buat list kosong untuk menyimpan data
            for mobil in pisah: # Memisahkan tiap isi dari list yang sudah dipisahkan sesuai kebutuhan
                tanggal = list(map(int, mobil[0].split("-")))    # Menggunakan split untuk memisahkan tanggal, bulan, tahun, serta map untuk mengubah semuanya menjadi integer
                jenis = mobil[1]  # Memasukan nama mobil ke variabel jenis
                jumlah = int(mobil[2]) # Memasukan jumlah sewa ke variabel jumlah, tidak lupa mengubahnya ke integer
                data.append([jenis, tanggal, jumlah])   # Masukan semua data tersebut ke list data
        return data # Mereturn list data yang berisi list
    except FileNotFoundError:
        print("File tidak ditemukan!")
        return []
    except ValueError:
        print("File tidak berformat dengan benar!")
        return []

def rental(): # Membuat fungsi rental untuk menyimpan data penyewaan mobil
    # Dimana key adalah tipe mobil sedangkan value berupa dictionary yang digunakan untuk menyimpan bulan dan total sewa pada bulan tersebut.
    dict_rental = {} # Membuat dictionary kosong
    
    for listdata in baca(): # Membaca stiap data yang sudah dibaca
        # Dibuat variabel agar tidak kebingungan
        jenis = listdata[0]
        bulan = listdata[1][1] # Membuat variabel khusus bulan saja, karena yang dibutuhkan hanya bulan
        jumlah = listdata[2]
        
        if jenis not in dict_rental: # Jika tidak ada jenis mobil di dict_rental
            dict_rental[jenis] = {} # Maka akan dibuatkan key dengan jenis mobil itu, tapi isinya masih dict kosong
        if bulan not in dict_rental[jenis]: # Kalau belum ada bulan yang belum terdaftar di dict jenis mobil tadi
            dict_rental[jenis][bulan] = jumlah # Maka akan ditambahkan key bulan keberapa, serta valuesnya adalah jumlah pada bulan tersebut
        else: # Namun apabila sudah terdaftar bulan tersebut, maka kita perlu menambahkannya dengan jumlah lainnya
            dict_rental[jenis][bulan] += jumlah
    return dict_rental # Return dict_rental yang sudah dibuat

def favorit(): # Fungsi favorit untuk mengembalikkan (return) nama mobil yang paling banyak disewa di tahun 2021.
    mobil = {} # Buat dulu dict kosong untuk mengelompokan jenis dan total sewa mobil
    for data in rental(): # Membaca setiap data di rental() dengan perulangan
        jumlah = sum(list(rental()[data].values())) # Membaca data mobil, lalu kita ambil valuesnya saja, untuk dijadikan list, lalu menjumlahkan semuanya dengan sum agar mendapatkan total sewanya
        if data not in mobil:       # Jika data belum ada di dict mobil
            mobil[data] = jumlah    # Maka akan dimasukan jumlah pertamanya
        else:                       # Namun jika sudah ada data di dict mobil
            mobil[data] += jumlah   # Maka akan ditambahkan jumlah baru dan jumlah sebelumnya
            
    fav = max(mobil,key=mobil.get)  # Menggunakan fungsi max untuk mendapatkan sewa tertinggi, jangan lupa gunakan keynya agar mendetect valuesnya, dan mereturn key nya
    return fav, mobil[fav]          # Return mobil fav yaitu mobil dengan sewa terbanyak, serta jumlah sewanya juga

def rerata(jenis):      # Fungsi report yang digunakan untuk menampilkan rata-rata sewa suatu mobil tertentu di setiap bulannya.
    if jenis in rental():
        bulan = len
        bulan = len(rental()[jenis])    # Menghitung jumlah bulan menyewa mobil
        jumlah = sum(list(rental()[jenis].values()))    # Menjumlahkan semua jumlah sewa tiap mobil
        return round(jumlah / bulan, 2) # Mereturn hasil bagi dari jumlah sewa total mobil, dengan jumlah bulan penyewaan (jika bulan sama, maka sewa akan ditotalkan dahulu perbulan)
    else:
        return None

def main_menu():
    while True:
        print("""
        Yuk Rental
    
1. Lihat Mobil Sewa Terfavorit
2. Hitung Rata-rata Sewa Mobil
3. Keluar
        """)

        choice = input("Pilih opsi (1/2/3): ")
        if choice == "1":
            fav_mobil, total_sewa = favorit()
            print(f"Mobil terfavorit di Yuk Rental adalah {fav_mobil.title()} dengan jumlah sewa sebanyak {total_sewa}")
        elif choice == "2":
            jenis = []
            urutan = 0
            for car in baca():  # Membaca data nama mobilnya saja dari fungsi yang sudah dibuat
                if car[0] not in jenis:  # Jika belum ada di list jenis, maka akan di append
                    jenis.append(car[0])

            for car in jenis:  # Melakukan perulangan untuk mencetak daftar mobil
                urutan += 1  # Urutan dibuat dengan cara menambah 1 setiap jenis mobil berganti
                print(f"{urutan}. {car.title()}")  # Mengubah dulu urutan menjadi string agar dapat ditambahkan titik dibelakang

            try:
                rataan = int(input("Input nomor jenis mobil: "))  # Lalu user diminta input nomor jenis mobil yang sudah dicetak sebelumnya
                if 1 <= rataan <= urutan:  # Pilihan nomor akan benar jika inputan merupakan nomor yang ditampilkan
                    jenis_mobil = jenis[rataan - 1]
                    avg = rerata(jenis_mobil)
                    if avg is not None:
                        print(f"Rata-rata sewa mobil {jenis_mobil.title()} adalah {avg}")
                    else:
                        print("Mobil tidak ditemukan dalam data rental.")
                else:
                    print("Inputan salah")
            except ValueError:
                print("Inputan harus berupa angka.")
        elif choice == "3":
            print("Terima kasih telah menggunakan layanan Yuk Rental!")
            break
        else:
            print("Opsi tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main_menu()
