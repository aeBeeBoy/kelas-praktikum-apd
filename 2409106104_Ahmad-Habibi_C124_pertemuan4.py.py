ulang = 10
for i in range (ulang):
    print("halo")

simpan = [12, "udin petot", 14.5, True, 'A',"102"]
for i in simpan: 
    print(i)

makanan = ("mie","sop","bakso")
minuman = ("es teh","air putih","es jeruk")

for i in makanan:
    for j in minuman:
       print(f"{i} & {j}")    

print("Menu Rumah Makan informatika 24:")
print("--------------------------------")
simpan = ["Nasi Goreng", "Mie Goreng", "Mie Ayam", "Bakso","Soto"]
for i in simpan:
    print(i)

print("Menu Rumah Makan informatika 24:")
print("--------------------------------")
simpan = ["Nasi Goreng", "Mie Goreng", "Mie Ayam", "Bakso","Soto"]
for i, menu in enumerate(simpan,start=100): 
    print(f"{i}.{menu}")

print("Menu Rumah Makan informatika 24:")
print("--------------------------------")
simpan = ["Nasi Goreng", "Mie Goreng", "Mie Ayam", "Bakso","Soto"]
for i in range(len(simpan)): 
    print(f"{I+1}. {simpan[i]}")


jawab = 'ya'
hitung = 0
while(jawab == 'ya'):
    hitung += 1
    # sama aja dengan hitung = hitungan + 1
    jawab = input("balikan lagi tidak? ") 
   if jawab == "ga" or jawab == "engga" :
    print(f"Total perulangan: {hitung}")
    else :
        break

print(“Daftar bilangan ganjil dari 1-10”)
for i in range(10):
    if i % 2 == 0:
        continue
print(i)

hitung = 0
while true:
    hitung += 1
    ulang = input("Masih Ingin Lanjut? ")
    if ulang == "y" or ulang == "Y":
        print("Oke Kita  Lanjut")
        continue