#import judul tkinter
import tkinter as tk
import tkinter.messagebox as msg

#buat jendela GUI
top = tk.Tk()

#atur judul jendela
top.title("Aplikasi prediksi Prodi Pilihan ")
#atur besar jendela

top.geometry("400x600")

#atur bg jendela
top.configure(bg="pink")

#tampilkan label judul di bagian bawah
judul = tk.Label(top, text="Aplikasi Prediksi Prodi Pilihan",)
judul.pack(side=tk.TOP, pady = 10)

#menyiapkan list kosong untuk input
entries = []

#buat loop 10 lalu input ke lis
for i in range(10):
    label = tk.Label(top, text=f"Nilai Mata Kuliah {i+1}:")
    label.pack()
    ent = tk.Entry(top, bd=3)
    ent.pack()
    entries.append(ent) 

#untuk menampilkan hasil
def tampilkan_hasil():
    msg.showinfo("Hasil Prediksi", "Prediksi Prodi Anda: Teknologi Informasi")

#membuat tombol hasil prediksi dibawah
tombolPrediksi = tk.Button(top, text="Hasil Prediksi", 
                           command=tampilkan_hasil)
tombolPrediksi.pack(side=tk.BOTTOM)

#nampilin teks hasil prediksi diGUI
hasilLabel = tk.Label(top, text="Prediksi Prodi akan muncul di sini")
hasilLabel.pack(side=tk.BOTTOM)
top.mainloop()