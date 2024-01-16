from tkinter import Button, Toplevel, Frame, Label, Entry, Canvas, Scrollbar, SOLID, IntVar, Checkbutton
import sys
sys.path.append('../interface_otimizada')
#from frames.frame_forn_comp import campo_fornecedor
from conecta_banco import cursor


resultado_fornecedor = []

codigo_fornecedor_sql = ''

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

    canvas_fornecedor = Canvas(toplevel_fornecedor, borderwidth=0)
    canvas_fornecedor.pack(side='left', fill='both', expand=True, padx=(0,0), pady=(55,30))

    frame_canvas = Frame(canvas_fornecedor)

    canvas_fornecedor.create_window((4,4), window=frame_canvas, anchor='nw', tags='frame')

    vsb = Scrollbar(toplevel_fornecedor, orient='vertical', command=canvas_fornecedor.yview)
    vsb.pack(side='right', fill='y', pady=(50,40))

    canvas_fornecedor.configure(yscrollcommand=vsb.set)

    def on_configure(event):
        canvas_fornecedor.configure(scrollregion=canvas_fornecedor.bbox('all'))

    canvas_fornecedor.bind('<Configure>', on_configure)

    lista_fornecedores = []
    checkbox_vars = []
    
    
    def nova_consulta():
        global resultado_fornecedor
        codfornec = campo_codigo.get()
        fornecedor = campo_fornecedor.get()
        
        if codfornec != '':
            consulta_fornecedor = f"SELECT codfornec, fornecedor FROM pcfornec WHERE codfornec = {codfornec}"
        elif fornecedor != '':
           consulta_fornecedor = f"SELECT codfornec, fornecedor FROM pcfornec WHERE fornecedor LIKE  UPPER('{fornecedor}')"
        else:
            consulta_fornecedor = f"SELECT codfornec, fornecedor FROM pcfornec"

        
        #consulta_fornecedor = f"SELECT codfornec, fornecedor FROM pcfornec WHERE codfornec = {codfornec}"
        cursor.execute(consulta_fornecedor)
        resultado_fornecedor.clear()  # Limpa os resultados antigos
        resultado_fornecedor.extend(cursor.fetchall())  # Adiciona os novos resultados

        # Limpa o conteúdo existente no Frame e nos CheckboxVars
        for widget in frame_canvas.winfo_children():
            widget.destroy()
        checkbox_vars.clear()

        for i, (codigo, razaosocial) in enumerate(resultado_fornecedor):
            var = IntVar()
            checkbox_vars.append(var)
            checkbox = Checkbutton(frame_canvas, text=f"{codigo} - {razaosocial}", variable=var)
            checkbox.grid(row=i, column=0, sticky='w', padx=(0, 50))

        frame_canvas.update_idletasks()
        canvas_fornecedor.config(scrollregion=canvas_fornecedor.bbox("all"))
    

    def atualizar_selecao():

        global resultado_fornecedor


        for i, checkbox_var in enumerate(checkbox_vars):
            if checkbox_var.get():
                codigo = resultado_fornecedor[i][0]
                lista_fornecedores.append(codigo)
                
        codigo_fornecedor_sql = ', '.join(map(str, lista_fornecedores))
        print(codigo_fornecedor_sql)
        toplevel_fornecedor.destroy()
        
        
        return codigo_fornecedor_sql

    frame_canvas.update_idletasks()
    canvas_fornecedor.config(scrollregion=canvas_fornecedor.bbox("all"))
    
    label_codigo = Label(toplevel_fornecedor, text='CÓDIGO', font=('Arial', 9))
    label_codigo.place(x=20, y=10)
    
    campo_codigo = Entry(toplevel_fornecedor, width= 9)
    campo_codigo.place(x=20, y=30)
   
    label_fornecedor = Label(toplevel_fornecedor, text='FORNECEDOR', font=('Arial', 9))
    label_fornecedor.place(x=90, y=10)
       
    campo_fornecedor = Entry(toplevel_fornecedor, width=33)
    campo_fornecedor.place(x=90, y=30)
      
    botao_pesquisar = Button(toplevel_fornecedor, text='PESQUISAR', width=10, bg='silver', command=nova_consulta)
    botao_pesquisar.place(x=300, y=25)
    
    botao_filial_confirmar = Button(toplevel_fornecedor, text='CONFIRMAR', bg='silver', command=atualizar_selecao)
    botao_filial_confirmar.place(x=230, y=370)

    botao_filial_cancelar = Button(toplevel_fornecedor, text='CANCELAR', command=toplevel_fornecedor.destroy)
    botao_filial_cancelar.place(x=320, y=370)
