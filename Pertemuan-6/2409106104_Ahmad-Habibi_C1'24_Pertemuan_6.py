#contoh 1
# daftar_buku = {
#     "Buku1" : "Harry Potter",
#     "Buku2" : "Percy Jackson",
#     "Buku3" : "Twillight"
# }

# print(daftar_buku["Buku1"])
# print(daftar_buku["Buku2"])
# print(daftar_buku["Buku3"])

# # contoh 2
# daftar_buku = {}

# daftar_buku["Buku1"] = "Harry Potter"
# daftar_buku["Buku2"] = "Percy Jackson"
# daftar_buku["Buku3"] = "Twillight"

# print(daftar_buku)

#contoh 2

Biodata = {
    "Nama" : "Aldy Ramadhan Syahputra",
    "NIM" : 2109106079,
    "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
    "Mahasiswa_Aktif" :True,
    "Social Media" : {
        "Instagram" : "@aldyrmdhns_",
        "Discord" : "\'Izanami#6848"
        "Email" : "iniemail@gmail.com"
    }
}

print(Biodata["KRS"][0])
print(Biodata["Social Media"]["Eamil"])

#contoh 3

Games ={
    "Games1" : "PUBG Mobile"
}
games = dict(Sekiro = "Action", Pokemon = "Adventure",
Valorant = "FPS")
print(games["Sekiro"])



#contoh 4

games = dict(Sekiro = "Action", Pokemon = "Adventure",
Valorant = {"nama" : {123 : "informatika"}})
print(games['Valorant']['nama'][123])

#contoh 5

Games = {
    "Game1" : "PUBG Mobile",
    "Game2" : "MObile Legends",
    "Game3" : "{
        "nama3" : "COC",
        "gendre" : "Startegy"
    }



print((games.get('game3')),get('genre'))
    
# contoh 6

Nilai = {
    "Matematika" : 80,
    "B. Indonesia" : 90,
    "B. Inggris" : 81,
    "Kimia" : 78,
    "Fisika" : 80
}
#tanpa menggunakan items
for i in Nilai:
    print(i)

print("")
#menggunakan items
for i, j in Nilai.items():
    print(f"Nilai {i} anda adalah {j}") 

#contoh 7

Film = {
"Avenger Endgame" : "Action",
"Sherlock Holmes" : "Mystery",
"The Conjuring" : "Horror"
}
#Sebelum Ditambah
print(Film)

Film["Zombieland"] = "Comedy"
Film.update( {"Hours" : "Thriller",
             "Rush Hour", :  "Comedy",
             "obtivition" : "science fition"

             })


#Setelah Ditambah
print(Film)

#penggunaan del = menghapus
del Film ['Avenger Endgame']
print (Film)

#penggunaan simoan = bisa di hapus sementara (bisa di pangil lagi )
simpan = Film.pop('Hours')
print (Film)
Print (simpan) #masih muncul

#pop = memindahkan ke keys lain

#penggunaan clear = jadinya kosong (menghapus semuanya)
simpan = Film.pop('Hours')
Film.clear()
print (Film)
print (simpan)


#contoh 8 
print("Jumlah Film" = ", len(Film)")


#contoh copy
movies = Film.copy()
print(movies)
print()

#contoh fromkeys

key = "apel", "jeruk", "mangga", "semangka"
value = 1
buah = dict.fromkeys(key, value)
print(buah)

#contoh keys and value

Nilai = {
"Matematika" : 80,
"B. Indonesia" : 90,
"B. Inggris" : 81,
"Kimia" : 78,
"Fisika" : 80
}
#menggunakan keys
for i in Nilai.keys():
    print(i)
print("")
#menggunakan value
for i in Nilai.values():
    print(i)


#contoh Setdefault
Nilai = {
"Matematika" : 80,
"B. Indonesia" : 90,
"B. Inggris" : 81
}
#sebelum Setdefault
print(Nilai)
print("")
#menggunakan setdefault = untuk menambahkan keys and value

print("Nilai : ", Nilai.setdefault("Kimia", 70))
print("")
#setelah menggunakan setdefault
print(Nilai)

#Dictionary of List and Nested Dictionary = Sebuah dictionary bisa juga berisi banyak list.

Musik = {
"The Chainsmoker" : ["All we Know", "The Paris"],
"Alan Walker" : ["Alone", "Lily"],
"Neffex" : ["Best of Me", "Memories"]
}
for i, j in Musik.items():
    print(f"Musik milik {i} adalah : ")
for song in j:
    print(song)
print("")



mahasiswa = {
101 : {"Nama" : "Aldy", "Umur" : 19},
111 : {"Nama" : "Abdul", "Umur" : 18}
}
for key, value in mahasiswa.items():
    print("ID Mahasiswa : ", key)
for key_a, value_a in value.items():
    print (key_a, " : ", value_a)
print("")

#NOMOR 2 STUDI KASUS

mapel = {
    "Matematika": 90,
    "Fisika" : 80,
    "Biologi": 80,
    "Kimia" : 70
    
}

nilai = sum(mapel. values ( ))
print("Nilai total : ", nilai)
rata = nilai / len (mapel)
print ("Nilai rata-rata : " , rata)