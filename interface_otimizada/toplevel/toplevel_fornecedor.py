from tkinter import Button, Toplevel, Frame, Label, Entry, Canvas, Scrollbar, SOLID
import sys
sys.path.append('../interface_otimizada')
from conecta_banco import cursor



def toplevel_fornecedor(root):
    toplevel_fornecedor = Toplevel(root)
    toplevel_fornecedor.title('FORNECEDORES')
    largura = 400
    altura = 400
    largura_screen = root.winfo_screenwidth()
    altura_screen = root.winfo_screenheight()
    posx = largura_screen/2 - largura/2
    posy = altura_screen/2 - altura/2
    toplevel_fornecedor.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))
    toplevel_fornecedor.grab_set()

    # Cria um Canvas com um Frame dentro pra exibir o resultado e interagir com a barra de rolamento
    canvas_fornecedor = Canvas(toplevel_fornecedor, borderwidth=0, highlightthickness=2, highlightbackground='black')
    canvas_fornecedor.pack(side='left', fill='both', expand=True, padx=(10,30), pady=(55,30))
    
    frame_canvas = Frame(canvas_fornecedor, relief=SOLID, bd=1)
    
    canvas_fornecedor.create_window((4,4), window=frame_canvas, anchor='nw', tags='frame')
    
    vsb = Scrollbar(toplevel_fornecedor, orient='vertical', command=canvas_fornecedor.yview)
    vsb.pack(side='right', fill='y', pady=(0,0))
    
    canvas_fornecedor.configure(yscrollcommand=vsb.set)
    
    def on_configure(event):
        canvas_fornecedor.configure(scrollregion=canvas_fornecedor.bbox('all'))
        
    canvas_fornecedor.bind('<Configure>', on_configure)
    
    ############
    
    frame_canvas.update_idletasks()
    canvas_fornecedor.config(scrollregion=canvas_fornecedor.bbox('all'))
    
    ###############
    
    label_codigo = Label(toplevel_fornecedor, text='CÓDIGO', font=('Arial', 9))
    label_codigo.place(x=20, y=10)
    #label_codigo.grid(row=0, column=0, padx=(10,0), pady=(10,0), sticky='w')
    
    campo_codigo = Entry(toplevel_fornecedor, width= 9)
    campo_codigo.place(x=20, y=30)
    #campo_codigo.grid(row=1, column=0, padx=(10,0), sticky='w')
    
    label_fornecedor = Label(toplevel_fornecedor, text='FORNECEDOR', font=('Arial', 9))
    label_fornecedor.place(x=90, y=10)
    #label_fornecedor.grid(row=0, column=1, padx=(20,0), pady=(10,0), sticky='w')
    
    campo_fornecedor = Entry(toplevel_fornecedor, width=33)
    campo_fornecedor.place(x=90, y=30)
    #campo_fornecedor.grid(row=1, column=1, padx=(20,0), sticky='w')
    
    botao_pesquisar = Button(toplevel_fornecedor, text='PESQUISAR', width=10, bg='silver')
    botao_pesquisar.place(x=300, y=25)
    #botao_pesquisar.grid(row=1, column=2, padx=(20,0), sticky='w')

    botao_filial_confirmar = Button(toplevel_fornecedor, text='CONFIRMAR', bg='silver', command=toplevel_fornecedor.destroy)
    botao_filial_confirmar.place(x=230, y=370)

    botao_filial_cancelar = Button(toplevel_fornecedor, text='CANCELAR', command=toplevel_fornecedor.destroy)
    botao_filial_cancelar.place(x=320, y=370)
