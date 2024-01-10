import tkinter as tk
import webbrowser

def abrir_site(event):
    url = "https://www.example.com"  # Substitua pelo site desejado
    webbrowser.open_new(url)

root = tk.Tk()
root.title("Abrir Site")

label = tk.Label(root, text="Clique aqui para abrir o site", fg="blue", cursor="hand2")
label.pack(padx=20, pady=20)
label.bind("<Button-1>", abrir_site)  # Associa o evento de clique à função abrir_site

root.mainloop()
