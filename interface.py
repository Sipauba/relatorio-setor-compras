from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkcalendar import *
import datetime

root = tk.Tk()
# Esse trecho até o geometry() é um algorítmo que faz a janela iniciar bem no centro da tela, independente a resolução do monitor
largura = 800
altura = 500
largura_screen = root.winfo_screenwidth()
altura_screen = root.winfo_screenheight()
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2
root.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))

root.title('FLOW UP')
root.resizable(False,False)

frame_cabecalho1 = Frame(root,
                        width = 640,
                        height = 50,
                        #relief = SOLID,
                        #bd = 1
                        )
frame_cabecalho1.pack(pady = (5,0))

label_filial = Label(frame_cabecalho1, text='Filial')
label_filial.grid(row=0, column=0, pady=(20,0))

campo_filial = ttk.Combobox(frame_cabecalho1, width=4, values=['','1','3','4','5','6','7','17','18','19','20','61','70'])
campo_filial.grid(row=1, column=0, pady=(0,20), padx=(20,0))


label_data_ini = Label(frame_cabecalho1, text='Data Inicial')
label_data_ini.grid(row=0, column=2, pady=(20,0))

data_inicial = DateEntry(frame_cabecalho1, date_pattern='dd/mm/yyyy')
data_inicial.grid(row=1, column=2, pady=(0,20), padx=(20,0))

label_data_fin = Label(frame_cabecalho1, text='Data Final')
label_data_fin.grid(row=0,column=3, pady=(20,0))

data_final = DateEntry(frame_cabecalho1, date_pattern='dd/mm/yyyy')
data_final.grid(row=1,column=3,  pady=(0,20), padx=(5,20))

label_tipo = Label(frame_cabecalho1, text='Tipo Pedido')
label_tipo.grid(row=0, column=4, pady=(20,0))

campo_tipo = ttk.Combobox(frame_cabecalho1, width=13, values=['Venda','Bonificado'])
campo_tipo.grid(row=1, column=4, pady=(0,20), padx=(0,20))

label_status = Label(frame_cabecalho1, text='Status Pedido')
label_status.grid(row=0, column=5, pady=(20,0))

campo_status = ttk.Combobox(frame_cabecalho1, width=13, values=['Entregue','Ag. Entrega','Ag. Faturamento'])
campo_status.grid(row=1, column=5, pady=(0,20), padx=(0,20))

frame_cabecalho2 = Frame(root,
                        width = 640,
                        height = 110,
                        #relief = SOLID,
                        #bd = 1
                        )
frame_cabecalho2.pack(side = 'top', anchor ='nw', pady = (0,10), padx=(146,0))

label_fornecedor = Label(frame_cabecalho2, text='Fornecedor')
label_fornecedor.grid(row=0, column=0, pady=(0,0), padx=(0,0))

campo_fornecedor = Entry(frame_cabecalho2, width=10)
campo_fornecedor.grid(row=1, column=0, pady=(0,0), padx=(0,0))

botao_fornecedor = Button(frame_cabecalho2, text='...')
botao_fornecedor.grid(row=1, column=1)

label_comprador = Label(frame_cabecalho2, text='Comprador')
label_comprador.grid(row=2, column=0)

campo_comprador = Entry(frame_cabecalho2,width=10)
campo_comprador.grid(row=3, column=0)

botao_comprador = Button(frame_cabecalho2, text='...')
botao_comprador.grid(row=3, column=1)

# Define a quantidade de colunas
tree = ttk.Treeview(root, columns=('coluna1','coluna2','coluna3','coluna4','coluna5','coluna6','coluna7','coluna8','coluna9'))

# Centraliza o conteúdo de todas as colunas
for coluna in ('coluna1','coluna2','coluna3','coluna4','coluna5','coluna6','coluna7','coluna8','coluna9'):
    tree.column(coluna, anchor = 'center')
    
# Nomeia o cabeçalho das colunas
tree.heading('coluna1', text = 'C.FORNEC')
tree.heading('coluna2', text = 'FORNECEDOR')
tree.heading('coluna3', text = 'NUMPED')
tree.heading('coluna4', text = 'DTEMISSAO')
tree.heading('coluna5', text = 'VLTOTAL')
tree.heading('coluna6', text = 'CODFILIAL')
tree.heading('coluna7', text = 'NF')
tree.heading('coluna8', text = 'STATUS')
tree.heading('coluna9', text = 'TIPO')

# Define uma largura padrão para cada coluna
tree.column('coluna1', width = 60)
tree.column('coluna2', width = 60)
tree.column('coluna3', width = 60)
tree.column('coluna4', width = 60)
tree.column('coluna5', width = 60)
tree.column('coluna6', width = 60)
tree.column('coluna7', width = 60)
tree.column('coluna8', width = 60)
tree.column('coluna9', width = 60)

# Essa linha abaixo esconde a primeira coluna obrigatória do tkinter
tree.column('#0', width = 0)

# Define a posição e as dimenções da TreeView
tree.place(x = 40, y = 200, width = 710, height = 250)

# Botão para exportar dados para excell
botao_exportar = Button(root, text = '   Exportar   ')
botao_exportar.place(x=660, y=460)

barra_rolamento_vertical = Scrollbar(root, orient = 'vertical', command = tree.yview)
#tree.configure(yscrollcommand=scrollbar.set)
barra_rolamento_vertical.place(x=751,y=200, height = 250)


root.mainloop()