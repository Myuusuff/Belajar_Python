print("Membuat daftar pada python")





# daftar kosong untuk menyimpan data
daftar_barang = []

# meminta input nama barang dari pengguna dan menambahkan ke daftar
nm_br1 = str(input("Masukkan barang 1: "))
daftar_barang.append(nm_br1)

nm_br2 = str(input("Masukkan barang 2: "))
daftar_barang.append(nm_br2)

nm_br3 = str(input("Masukkan barang 3: "))
daftar_barang.append(nm_br3)

nm_br4 = str(input("Masukkan barang 4: "))
daftar_barang.append(nm_br4)

nm_br5 = str(input("Masukkan barang 5: "))
daftar_barang.append(nm_br5)


try:
    string =int(input("Masukkan angka: "))

    if 0 <= string < len(daftar_barang):
        print("Ini hasilnya: ", daftar_barang[string - 1])
    else:
        print("angka diluar jangkauan daftar.")
except ValueError:
    print("Masukkan angka yang valid.")



