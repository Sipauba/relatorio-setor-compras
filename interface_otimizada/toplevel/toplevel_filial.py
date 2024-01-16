from tkinter import Button, Toplevel, Frame, IntVar, Checkbutton, Scrollbar, Canvas
import sys
sys.path.append('../interface_otimizada')
from conecta_banco import cursor


consulta_filial = "SELECT codigo, razaosocial FROM pcfilial WHERE dtexclusao IS NULL ORDER BY codigo"
cursor.execute(consulta_filial)
resultado_filial = cursor.fetchall()
codigo_filial_sql =''

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
    
    vsb = Scrollbar(toplevel_filial, orient="vertical", command=canvas_filial.yview)
    vsb.pack(side="right", fill="y", pady=(0,40))
    
    canvas_filial.configure(yscrollcommand=vsb.set)
    

    def on_configure(event):
        canvas_filial.configure(scrollregion=canvas_filial.bbox("all"))

    canvas_filial.bind("<Configure>", on_configure)

    lista_filiais = []
    
    def atualizar_selecao():
        nonlocal lista_filiais  # Usar nonlocal para acessar a variável da função externa

        # Limpar a lista de códigos selecionados
        lista_filiais = []

        for i, checkbox_var in enumerate(checkbox_vars):
            if checkbox_var.get():
                codigo = resultado_filial[i][0]
                lista_filiais.append(codigo)  # Adicionar código à lista

        # Imprimir a lista de códigos (para fins de teste)
        #print(lista_filiais)
        #print(f"Códigos Selecionados: {', '.join(map(str, lista_filiais))}")
        global codigo_filial_sql
        codigo_filial_sql = ', '.join(map(str, lista_filiais))
        print(codigo_filial_sql)
        #campo_filial.set(codigo_filial_sql.get())
        toplevel_filial.destroy()
        
        #inclui_filial_campo()
        
        return codigo_filial_sql


    checkbox_vars = []

    # Criação dos checkboxes e rótulos na janela
    for i, (codigo, razaosocial) in enumerate(resultado_filial):
        var = IntVar()
        checkbox_vars.append(var)
        checkbox = Checkbutton(frame_canvas, text=f"{codigo} - {razaosocial}", variable=var)
        checkbox.grid(row=i, column=0, sticky='w', padx=(0, 50))

    frame_canvas.update_idletasks()
    canvas_filial.config(scrollregion=canvas_filial.bbox("all"))
    
    botao_filial_confirmar = Button(toplevel_filial, text='CONFIRMAR', bg='silver', command=atualizar_selecao)
    botao_filial_confirmar.place(x=230, y=370)

    botao_filial_cancelar = Button(toplevel_filial, text='CANCELAR', command=toplevel_filial.destroy)
    botao_filial_cancelar.place(x=320, y=370)

