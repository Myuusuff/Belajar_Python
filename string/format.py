# formasi string
# dis kita tidak bisa mengabungkan string dengan angka
# seperti ini contoh:
umur = 17
a = "umur saya adalah" + umur
print(a)

# cara yg benar begini memakai format()
# Contoh;

# umur = 17
# a = "Umur saya sudah mencapai "
# print(a.format(umur))

# contoh kedua
kuantitas = 5
potongan = 322
harga = 23.34

pesan = "saya ingin membayar{} dollar untuk{0} harga 1 potongan{1}"
print(pesan.format(kuantitas,potongan,harga))

