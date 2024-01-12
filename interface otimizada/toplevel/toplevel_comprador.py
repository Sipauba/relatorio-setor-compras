from tkinter import Button, Toplevel, Frame, SOLID, IntVar, Checkbutton
import cx_Oracle
from acesso_banco.acesso_oracle import *

# Encontra o arquivo que aponta para o banco de dados
cx_Oracle.init_oracle_client(lib_dir="P://instantclient_21_10")

# Faz a conexão ao banco de dados
conecta_banco = cx_Oracle.connect(usuario, senha, f'{host}/{servico}')

# Cria um cursor no banco para que seja possível fazer consultas e alterações no banco de dados
cursor = conecta_banco.cursor()

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
    
    frame_comprador = Frame(toplevel_comprador,
                            width=370,
                            height=345,
                            relief= SOLID,
                            bd=1
                            )
    frame_comprador.pack(padx=(5,20), pady=(5,50))
  
    def atualizar_selecao():
            for i, checkbox_var in enumerate(checkbox_vars):
                if checkbox_var.get():
                    print(f"Selecionado: {resultado_comprador[i]}")

    checkbox_vars = []

    # Criação dos checkboxes e rótulos na janela
    for i, (matricula, nome) in enumerate(resultado_comprador):
        var = IntVar()
        checkbox_vars.append(var)
        checkbox = Checkbutton(frame_comprador, text=f"{matricula} - {nome}", variable=var, command=atualizar_selecao)
        checkbox.grid(row=i, column=0, sticky='w')

"""    botao_filial_confirmar = Button(toplevel_comprador, text='CONFIRMAR', command=toplevel_comprador.destroy)
    botao_filial_confirmar.place(x=130, y= 260)

    botao_filial_cancelar = Button(toplevel_comprador, text='CANCELAR', command=toplevel_comprador.destroy)
    botao_filial_cancelar.place(x=220, y=260)"""
