from tkinter import Frame, Label, SOLID, Checkbutton, IntVar, Button
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
        print(resultado_tipo_sql)  # Substitua por qualquer ação que você deseja fazer com a lista de valores

        return resultado_tipo_sql
    
    # Checkbuttons individuais
    box_aguardando_faturamento = Checkbutton(frame_tipo, text='VENDA', variable=var_venda, command=exibir_valores_tipo)
    box_aguardando_faturamento.grid(row=1, column=0, sticky='w')
    
    box_aguardando_entrega = Checkbutton(frame_tipo, text='BONIFICAÇÃO', variable=var_bonificacao, command=exibir_valores_tipo)
    box_aguardando_entrega.grid(row=2, column=0, sticky='w')
    
           

    """frame_status = Frame(root,
                         #relief=SOLID,
                         #bd=1
                         )
    frame_status.place(x=555, y= 5)
    
    label_status = Label(frame_status, text='STATUS DO PEDIDO', font=('Arial', 9))
    label_status.grid(row=0, column=0, pady=(20,0), padx=(0,0), sticky='w')

    # Variáveis de controle para os Checkbuttons
    var_total = IntVar(value=0)
    var_parcial = IntVar(value=0)
    var_aguardando_faturamento = IntVar(value=0)
    var_aguardando_entrega = IntVar(value=0)
    
    # Checkbuttons individuais
    box_aguardando_faturamento = Checkbutton(frame_status, text='AGUARDANDO FATURAMENTO', variable=var_aguardando_faturamento)
    box_aguardando_faturamento.grid(row=1, column=0, sticky='w')
    
    box_aguardando_entrega = Checkbutton(frame_status, text='AGUARDANDO ENTREGA', variable=var_aguardando_entrega)
    box_aguardando_entrega.grid(row=2, column=0, sticky='w')
    
    box_parcial = Checkbutton(frame_status, text='ENTREGA PARCIAL', variable=var_parcial)
    box_parcial.grid(row=3, column=0, sticky='w')
    
    box_total = Checkbutton(frame_status, text='ENTREGA TOTAL', variable=var_total)
    box_total.grid(row=4, column=0, sticky='w')

    # Função para exibir os valores dos Checkbuttons
    def exibir_valores_status():
        valores = [
            f"'{status}'" if var.get() else ''
            for status, var in zip(['TOTAL', 'PARCIAL', 'AGUARDANDO FATURAMENTO', 'AGUARDANDO ENTREGA'],
                                   [var_total, var_parcial, var_aguardando_faturamento, var_aguardando_entrega])
        ]
        valores = [valor for valor in valores if valor]  # Remove os valores vazios
        global resultado_status_sql
        resultado_status_sql = ', '.join(valores)
        print(resultado_status_sql)  # Substitua por qualquer ação que você deseja fazer com a lista de valores

        return resultado_status_sql
    
    def clicou():
        exibir_valores_tipo()
        exibir_valores_status()
    
    botao_pesquisar = Button(root, text='PESQUISAR', width=15, height=1, bg='silver', command=clicou)
    botao_pesquisar.place(x=635, y=150)"""
    

    
    