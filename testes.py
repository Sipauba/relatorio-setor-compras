import tkinter as tk
from tkinter import ttk

def on_checkbox_click(event):
    item = tree.identify_row(event.y)
    checked = tree.item(item, 'values')[0]
    tree.item(item, values=(not checked,))

# Criar a janela principal
root = tk.Tk()
root.title("Exemplo de Treeview com Checkboxes")

# Criar a Treeview com uma coluna para checkboxes
tree = ttk.Treeview(root, columns=("Checkbox", "Coluna 1", "Coluna 2"), show="headings")

# Configurar o cabeçalho
tree.heading("Checkbox", text="")
tree.heading("Coluna 1", text="Coluna 1")
tree.heading("Coluna 2", text="Coluna 2")

# Inserir dados de exemplo
for i in range(5):
    tree.insert("", "end", values=(False, f"Dado {i}", f"Outro dado {i}"))

# Adicionar evento de clique para simular o checkbox
tree.tag_configure('Checkbox', background='')  # Para destacar a célula clicada
tree.bind('<ButtonRelease-1>', on_checkbox_click)

# Adicionar uma imagem para simular um checkbox marcado
checked_image = tk.PhotoImage(data='''R0lGODlhCAAIAMIBAAAAAP/sAACH5BAEKAAEALAAAAAAIAAgAAAIbBAA7''')
unchecked_image = tk.PhotoImage(data='''R0lGODlhCAAIAMIFAAAAAP/sAACH5BAEKAAEALAAAAAAIAAgAAAIbBAA7''')

tree.image = unchecked_image
tree.tag_add('Checkbox', '1')
tree.item('1', values=(False, 'Dado 0', 'Outro dado 0'))

# Layout da Treeview
tree.pack()

# Iniciar o loop principal
root.mainloop()
