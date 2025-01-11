# pendaftaran mahasiswa
import tkinter as tk
from tkinter import messagebox

def submit(entry_nama, entry_nim, menu_prodi_var, daftar_prodi):
    nama_mahasiswa = entry_nama.get()
    nim_mahasiswa = entry_nim.get()
    pilihan_prodi = menu_prodi_var.get()
    prodi_mahasiswa = daftar_prodi[pilihan_prodi]

    messagebox.showinfo("Data Mahasiswa Baru ",
                         f"Nama: {nama_mahasiswa}\n Nim: {nim_mahasiswa}\n Program Studi:{prodi_mahasiswa}")

# daftar prodi
    daftar_prodi = ["Prodi A", "Prodi B", "Prodi C"]

# membuat GUI
    root = tk.Tk()
    root.title("Pendaftaran Mahasiswa Baru")

    label_nama = tk.label( root,text= "Nama: ")
    label_nama.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'w')
    entry_nama = tk.Entry(root)
    entry_nama.grid(row = 0, column = 1, padx = 5, pady = 5,)

    label_nim = tk.Label(root,text = "Nim: ")
    label_nim.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'w')
    entry_nim = tk.Entry(root)
    entry_nim.grid(row = 1, column = 1, padx = 5, pady = 5,)

    label_prodi = tk.Label(root,text = "Program Studi: ")
    label_prodi.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = 'w')
    entry_prodi = tk.Entry(root)
    entry_prodi.grid(row = 1, column = 1, padx = 5, pady = 5,)
    
    menu_prodi_var = tk.IntVar()
    for i, prodi in enumerate(daftar_prodi):
        tk.Radiobutton(root,text = prodi, variable=i).grid(row=i+2,column=1, padx=5, pady= 5, sticky= 'w')
    
    submit_button = tk.Button(root,text="Submit" , command=submit)
    submit_button.grid(row=len(daftar_prodi)+2, columnspan=2, padx=5, pady=10)

    root.mainloop()