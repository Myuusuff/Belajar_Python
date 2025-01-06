# perulangan for digunakan untuk mengulang rangkain bisa berupa list,tuple, int, float,string dll

kendaraan = []

def input_kendaraan(x): # fungsi untuk input tidak valid
    while True:
        user_input = input(x)
        if user_input.isalpha():
            return user_input
        else:
            print("input tidak valid! harap masukkan nama kendaraan tanpa angka.")

def hapus_kendaraan(kendaraan,kendaraan_dihapus):
    if kendaraan_dihapus in kendaraan:
        kendaraan.remove(kendaraan_dihapus)
        print("kendaraan setelah dihapus: ", kendaraan)
    else:
        print(kendaraan_dihapus,"tidak ada dalam daftar kendaraan")
    return kendaraan   

input1 = input_kendaraan("Masukkan Kendaraan 1: ")
input2 = input_kendaraan("Masukkan Kendaraan 2: ")
input3 = input_kendaraan("Masukkan Kendaraan 3: ")
kendaraan.append(input1)
kendaraan.append(input2)
kendaraan.append(input3)

print("kendaraan diinput ", kendaraan)
tambah = input_kendaraan("Tambahkan kendaraan: ")
kendaraan.append(tambah)
print("kendaraan setelah ditambahkan", kendaraan)



kurang = int(input("Nomor yang ingin dihilangkan: "))
if 1 <= kurang <= len(kendaraan):
    kendaraan.pop(kurang - 1)
    print("Kendaraan setelah dihapus: ", kendaraan)
else: 
    print("nomor tidak valid masukkan nomor antara 1 dan", len(kendaraan))

hapus = hapus_kendaraan("Hapus kendaraan: ")
kendaraan = hapus_kendaraan(kendaraan,hapus)
# if hapus in kendaraan
#     kendaraan.remove(hapus)
#     print("kendaraan setelah di hapus: ", kendaraan)
# else:
#     print(f"'{hapus}' tidak ada dalam daftar kendaraan")
