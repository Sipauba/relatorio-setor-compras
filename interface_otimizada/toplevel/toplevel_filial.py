from tkinter import Button, Toplevel, Frame, IntVar, Checkbutton, Scrollbar, Canvas
import sys
sys.path.append('../interface_otimizada')
from conecta_banco import cursor

consulta_filial = "SELECT codigo, razaosocial FROM pcfilial WHERE dtexclusao IS NULL ORDER BY codigo"
cursor.execute(consulta_filial)
resultado_filial = cursor.fetchall()

def toplevel_filial(root):
    toplevel_filial = Toplevel(root)
    toplevel_filial.title('FILIAIS')
    largura = 400
    altura = 400
    largura_screen = root.winfo_screenwidth()
    altura_screen = root.winfo_screenheight()
    posx = largura_screen/2 - largura/2
    posy = altura_screen/2 - altura/2
    toplevel_filial.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))
    toplevel_filial.grab_set()

    # Criar um Canvas e um Frame interno
    canvas_filial = Canvas(toplevel_filial, borderwidth=0)
    canvas_filial.pack(side="left", fill="both", expand=True, pady=(0,40))
    
    frame_canvas = Frame(canvas_filial)
    
    canvas_filial.create_window((4, 4), window=frame_canvas, anchor="nw", tags="frame")
    
    vsb = Scrollbar(toplevel_filial, orient="vertical", command=canvas_filial.yview,)
    vsb.pack(side="right", fill="y", pady=(0,40))
    
    canvas_filial.configure(yscrollcommand=vsb.set)
    

    def on_configure(event):
        canvas_filial.configure(scrollregion=canvas_filial.bbox("all"))

    canvas_filial.bind("<Configure>", on_configure)

    def atualizar_selecao():
        for i, checkbox_var in enumerate(checkbox_vars):
            if checkbox_var.get():
                print(f"Selecionado: {resultado_filial[i]}")

    checkbox_vars = []

    # Criação dos checkboxes e rótulos na janela
    for i, (matricula, nome) in enumerate(resultado_filial):
        var = IntVar()
        checkbox_vars.append(var)
        checkbox = Checkbutton(frame_canvas, text=f"{matricula} - {nome}", variable=var, command=atualizar_selecao)
        checkbox.grid(row=i, column=0, sticky='w', padx=(0, 50))

    frame_canvas.update_idletasks()
    canvas_filial.config(scrollregion=canvas_filial.bbox("all"))
    
    botao_filial_confirmar = Button(toplevel_filial, text='CONFIRMAR', bg='silver', command=toplevel_filial.destroy)
    botao_filial_confirmar.place(x=230, y=370)

    botao_filial_cancelar = Button(toplevel_filial, text='CANCELAR', command=toplevel_filial.destroy)
    botao_filial_cancelar.place(x=320, y=370)

