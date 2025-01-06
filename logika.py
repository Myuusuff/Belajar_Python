angka1 = int(input("Masukkan Angka: "))
angka2 = int(input("Masukkan Angka: "))

if angka1 > angka2:
    print(angka1, "Lebih besar dari", angka2)
elif angka1 < angka2: 
    print(angka1, "Lebih kecil dari", angka2)
else:
    print("Kedua angka sama besar")
# except ValueError:1