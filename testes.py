import tkinter as tk

def abrir_segunda_janela():
    # Coordenadas do botão
    x_botao = root.winfo_rootx() + botao.winfo_x()
    y_botao = root.winfo_rooty() + botao.winfo_y() + botao.winfo_height()
    
    # Criar e posicionar a segunda janela ao lado do botão
    segunda_janela = tk.Toplevel(root)
    segunda_janela.title("Segunda Janela")
    x_segunda_janela = x_botao
    y_segunda_janela = y_botao
    segunda_janela.geometry(f"+{x_segunda_janela}+{y_segunda_janela}")

    label = tk.Label(segunda_janela, text="Esta é a segunda janela!")
    label.pack()

root = tk.Tk()
root.title("Exemplo de Segunda Janela")

botao = tk.Button(root, text="Abrir Segunda Janela", command=abrir_segunda_janela)
botao.pack()

root.mainloop()
