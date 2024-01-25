from tkinter import Frame, Label, SOLID, Checkbutton, IntVar
from variaveis import atualizar_resultado_tipo_sql
#import variaveis
#from frame_status import exibir_valores_status

def frame_tipo(root):
    #frame_status(root)
    frame_tipo = Frame(root,
                       #relief=SOLID,
                       #bd=1
                       )
    frame_tipo.place(x=395, y=5)
    
    label_tipo = Label(frame_tipo, text='TIPO DO PEDIDO', font=('Arial', 9))
    label_tipo.grid(row=0, column=0, pady=(20,0), padx=(0,0), sticky='w')

    # Variáveis de controle para os Checkbuttons
    var_venda = IntVar(value=0)
    var_bonificacao = IntVar(value=0)

    # Função para exibir os valores dos Checkbuttons
    def exibir_valores_tipo():
        valores = [
            f"'{status}'" if var.get() else ''
            for status, var in zip(['VENDA', 'BONIFICACAO'],
                                   [var_venda, var_bonificacao])
        ]
        valores = [valor for valor in valores if valor]  # Remove os valores vazios
        global resultado_tipo_sql
        resultado_tipo_sql = ', '.join(valores)
        #print(resultado_tipo_sql)  # Substitua por qualquer ação que você deseja fazer com a lista de valores
        atualizar_resultado_tipo_sql(resultado_tipo_sql)
    
    # Checkbuttons individuais
    box_aguardando_faturamento = Checkbutton(frame_tipo, text='VENDA', variable=var_venda, command=exibir_valores_tipo)
    box_aguardando_faturamento.grid(row=1, column=0, sticky='w')
    
    box_aguardando_entrega = Checkbutton(frame_tipo, text='BONIFICAÇÃO', variable=var_bonificacao, command=exibir_valores_tipo)
    box_aguardando_entrega.grid(row=2, column=0, sticky='w')
