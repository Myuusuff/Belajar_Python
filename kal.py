def kalkulator():
    print("=== Mesin Kalkulator Sederhana ===")
    print("Pilih Operasi:")
    print("+ untuk Penjumlahan")
    print("- untuk Pengurangan")
    print("* untuk Perkalian")
    print("/ untuk Pembagian")

    # Meminta input dari pengguna
    try:
        pilihan = input("Masukkan pilihan operasi (+, -, *, /): ")
        if pilihan not in ['+', '-', '*', '/']:
            print("Pilihan tidak valid. Silakan pilih antara +, -, *, atau /.")
            return

        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))

        # Operasi berdasarkan pilihan
        if pilihan == '+':
            hasil = angka1 + angka2
            print(f"Hasil: {angka1} + {angka2} = {hasil}")
        elif pilihan == '-':
            hasil = angka1 - angka2
            print(f"Hasil: {angka1} - {angka2} = {hasil}")
        elif pilihan == '*':
            hasil = angka1 * angka2
            print(f"Hasil: {angka1} * {angka2} = {hasil}")
        elif pilihan == '/':
            if angka2 == 0:
                print("Kesalahan: Pembagian dengan nol tidak diperbolehkan.")
            else:
                hasil = angka1 / angka2
                print(f"Hasil: {angka1} / {angka2} = {hasil}")
    except ValueError:
        print("Input tidak valid. Silakan masukkan angka.")

# Menjalankan kalkulator
kalkulator()
