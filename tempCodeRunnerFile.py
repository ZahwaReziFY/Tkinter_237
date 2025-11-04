import tkinter as tk
import tkinter.messagebox as msg

top = tk.Tk()
top.title("Aplikasi prediksi Prodi Pilihan ")
top.geometry("400x600")
top.configure(bg="pink")
judul = tk.Label(top, text="Aplikasi Prediksi Prodi Pilihan",)
judul.pack(side=tk.BOTTOM)

entries = []
for i in range(10):
    label = tk.Label(top, text=f"Nilai Mata Kuliah {i+1}:")
    label.pack()
    ent = tk.Entry(top, bd=3)
    ent.pack()
    entries.append(ent) 

def tampilkan_hasil():
    msg.showinfo("Hasil Prediksi", "Prediksi Prodi Anda: Teknologi Informasi")

tombolPrediksi = tk.Button(top, text="Hasil Prediksi", 
                           command=tampilkan_hasil)
tombolPrediksi.pack(side=tk.BOTTOM)

hasilLabel = tk.Label(top)
hasilLabel.pack(side=tk.BOTTOM)

top.mainloop()