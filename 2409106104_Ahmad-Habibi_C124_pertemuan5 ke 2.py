nama = ["shandy",106,true,
        ["yuyun",145],3.96,
        [123,"ALVITO,",FALSE,3.66],
        "rehan"]
print(nama[4][2])

matkul = ["APD",
          "APL",
          "WEB",
          "JARKOM",
          "BASDAT",
          "STRUKDAT",
          "PTI",
          "KALKULUS",
          "PROBAS"
 ]
print(matkul[6])

makanan = ["Bakso","Sate","Soto","Nasi Goreng","mie ayam"]
print ("sebelum: ")
print(makanan)
makanan.append("Nasi Goreng")
print("Sesudah: ")

makanan.clear()
print (makanan)

data = makanan.pop(5)
print (makanan)
print (data)

del makanan{}

print (maknanan)
makanan,insert(2,"Nasi Goreng")
makanan[1] = ["AYAM",";BEBEK"]
print(makanan)



minuman = ["ES TEH",
           "ES JERUK",
           "ES DOGER",
           "JUS ALPULKAT",
           "Pocari",
           "Es Teler"
]
print("sebelum")
print(minuman)

del minuman(2)

print("Sesudah")

print (minuman)

minuman(5) = ["Air Putih"]
print (minuman)

minuman.insert(0,"Jus Tomat")
print (minuman)



makanan = ["Ayam","Ikan", ["Baksa","Soto","Sate","Ikan","Bebek"] , 
           ["teh","kopi","air"]]  



for i in makanan :
    print(i)



for i in makanan :
    print(i, end=" ")



for i in makanan :
    for j in i :
        print (j, end=" ")



for i in makanan :
    if isinstance(i, list) :
        for j in i :
         print (j, end=" ")
    else:
        print(i)



for i in makanan :
    if isinstance(i, list) :
     for j in i :
        print (j)
    else:
        print(i)
    

    