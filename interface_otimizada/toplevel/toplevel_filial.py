from tkinter import Button, Toplevel, Frame, SOLID, IntVar, Checkbutton
import sys
sys.path.append('../interface_otimizada')
from conecta_banco import cursor

consulta_filial = "SELECT codigo, razaosocial FROM pcfilial WHERE dtexclusao IS NULL"
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
    
    frame_top_filial = Frame(toplevel_filial,
                            width=370,
                            height=345,
                            relief= SOLID,
                            bd=1
                            )
    frame_top_filial.pack(padx=(5,20), pady=(5,50))
    
    def atualizar_selecao():
        for i, checkbox_var in enumerate(checkbox_vars):
            if checkbox_var.get():
                print(f"Selecionado: {resultado_filial[i]}")

    checkbox_vars = []

    # Criação dos checkboxes e rótulos na janela
    for i, (matricula, nome) in enumerate(resultado_filial):
        var = IntVar()
        checkbox_vars.append(var)
        checkbox = Checkbutton(frame_top_filial, text=f"{matricula} - {nome}", variable=var, command=atualizar_selecao)
        checkbox.grid(row=i, column=0, sticky='w')
  

"""    botao_filial_confirmar = Button(toplevel_filial, text='CONFIRMAR', command=toplevel_filial.destroy)
    botao_filial_confirmar.place(x=130, y= 260)

    botao_filial_cancelar = Button(toplevel_filial, text='CANCELAR', command=toplevel_filial.destroy)
    botao_filial_cancelar.place(x=220, y=260)"""

