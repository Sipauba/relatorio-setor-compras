from tkinter import Button, Toplevel, Frame, SOLID, IntVar, Checkbutton, Canvas, Scrollbar
import sys
sys.path.append('../interface_otimizada')
from conecta_banco import cursor

consulta_comprador = "SELECT matricula, nome FROM pcempr WHERE codsetor = 2 AND situacao = 'A'"
cursor.execute(consulta_comprador)
resultado_comprador = cursor.fetchall()

def toplevel_comprador(root):
    toplevel_comprador = Toplevel(root)
    toplevel_comprador.title('COMPRADORES')
    largura = 400
    altura = 400
    largura_screen = root.winfo_screenwidth()
    altura_screen = root.winfo_screenheight()
    posx = largura_screen/2 - largura/2
    posy = altura_screen/2 - altura/2
    toplevel_comprador.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))
    toplevel_comprador.grab_set()
    
    # Cria um Canvas com um Frame dentro 
    canvas_comprador = Canvas(toplevel_comprador, borderwidth=0)
    canvas_comprador.pack(side='left', fill='both', expand=True, pady=(0,40))
    
    frame_canvas = Frame(canvas_comprador)
    
    canvas_comprador.create_window((4,4), window=frame_canvas, anchor='nw', tags='frame')
    
    vsb = Scrollbar(toplevel_comprador, orient='vertical', command=canvas_comprador.yview)
    vsb.pack(side='right', fill='y', pady=(0,40))
    
    canvas_comprador.configure(yscrollcommand=vsb.set)
    
  
    def on_configure(event):
        canvas_comprador.configure(scrollregion=canvas_comprador.bbox('all'))
        
    canvas_comprador.bind('<Configure>', on_configure)
    
    def atualizar_selecao():
            for i, checkbox_var in enumerate(checkbox_vars):
                if checkbox_var.get():
                    print(f"Selecionado: {resultado_comprador[i]}")

    checkbox_vars = []

    # Criação dos checkboxes e rótulos na janela
    for i, (matricula, nome) in enumerate(resultado_comprador):
        var = IntVar()
        checkbox_vars.append(var)
        checkbox = Checkbutton(frame_canvas, text=f"{matricula} - {nome}", variable=var, command=atualizar_selecao)
        checkbox.grid(row=i, column=0, sticky='w')
        
    frame_canvas.update_idletasks()
    canvas_comprador.config(scrollregion=canvas_comprador.bbox('all'))

    botao_filial_confirmar = Button(toplevel_comprador, text='CONFIRMAR', bg='silver', command=toplevel_comprador.destroy)
    botao_filial_confirmar.place(x=230, y= 370)

    botao_filial_cancelar = Button(toplevel_comprador, text='CANCELAR', command=toplevel_comprador.destroy)
    botao_filial_cancelar.place(x=320, y=370)
