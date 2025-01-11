#melihat jam,menit,detik dan mikrodetik
import datetime

#mencetak waktu sekarang
a = datetime.datetime.now()
print("Waktu sekarang menujukkan pukul :",a.year) # a.year menampilkan tahun sekarang
print(a.strftime("%A")) # menampilkan hari dalam bahasa inggris