# a = open("yusuf.txt", "r")
# print(a.readline()) # mencetak 1 baris
# print(a.read(5)) # mencetak 5 karakter jika dalam read memiliki angka yg di inginkan

# a = open("yusuf.txt", "r")
# for x in a:
#     print(x)

#parameter open()
    # "a" = append akan ditambahkan ke akhir file
    # "w" = Akan menimpa konten apa pun yang sudah ada
    # "r" = membaca
    # "x" = membuat file
    # "t" = teks
    # "b" = biner
f = open("yusuf.txt", "a") # fungsi "a" menambahkan teks diahkhir  dalam file yg di tuju
f.write(" ini adalah teks yang baru ditambahkan ")
f.close()

#membuka dan membaca file yg sudah ditunda
f = open("yusuf.txt", "r")
print(f.read())

a = open("yusuf2.txt", "w")
a.write("Hallo Teman-teman ini adalah langkah awal saya belajar pthon semmoga diberikan kelancaran dan tetap konsisten semoga yg di harapakan cepat terjadiii aamiin")
a.close()

#buka
a = open("yusuf2.txt", "r")
print(a.read())

