# def ini_fungsi(fname):
#     print("Muhammad " + fname)



# # ini cara panggill fungsi

# ini_fungsi("Yusuf")
# ini_fungsi("Julian")
# ini_fungsi("YusJul")



# #fungsi penjumlahan

# def penjumlahan(angka1, angka2):
#     hasil = angka1 + angka2
#     return hasil

# # penggunaan fungsi2

# angka1 = int(input("Masukkan Angka: ")) 
# angka2 =int(input("Masukkan Angka: "))

# print("Operator Penjumlahan")
# print(angka1, "+", angka2, "=",penjumlahan(angka1, angka2))

#cara menggunakan fungsi string

# def string(string1, string2):
#     return string1 + string2


# string1 = str(input("Masukkan Nama Depan: "))
# string2 = str(input("Masukkan Nama Belakang: "))

# print("Penggabungan string")
# print("Nama Lengkap Anda: ", string(string1, string2))

def fungsi(*nama):
    print("nama teman saya " + nama[2])

fungsi("Muhammad", "Yusuf", "Julian")

