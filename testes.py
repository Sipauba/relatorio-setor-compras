from tkinter import Tk, Label, Frame, IntVar, Checkbutton, Button

def frame_status(root):
    frame_status = Frame(root)
    frame_status.pack(side='left', padx=(5, 0))  # Utilizando pack para gerenciar a geometria

    label_status = Label(frame_status, text='STATUS DO PEDIDO', font=('Arial', 9))
    label_status.grid(row=0, column=0, pady=(20, 0), padx=(0, 0), sticky='w')

    # Variáveis de controle para os Checkbuttons
    var_total = IntVar(value=1)
    var_parcial = IntVar(value=1)
    var_aguardando_faturamento = IntVar(value=1)
    var_aguardando_entrega = IntVar(value=1)

    # Checkbuttons individuais
    checkbutton_aguardando_faturamento = Checkbutton(frame_status, text='AGUARDANDO FATURAMENTO', variable=var_aguardando_faturamento)
    checkbutton_aguardando_faturamento.grid(row=1, column=0, sticky='w')
    
    checkbutton_aguardando_entrega = Checkbutton(frame_status, text='AGUARDANDO ENTREGA', variable=var_aguardando_entrega)
    checkbutton_aguardando_entrega.grid(row=2, column=0, sticky='w')
    
    checkbutton_parcial = Checkbutton(frame_status, text='ENTREGA PARCIAL', variable=var_parcial)
    checkbutton_parcial.grid(row=3, column=0, sticky='w')
    
    checkbutton_total = Checkbutton(frame_status, text='ENTREGA TOTAL', variable=var_total)
    checkbutton_total.grid(row=4, column=0, sticky='w')

    # Função para exibir os valores dos Checkbuttons
    def exibir_valores():
        valores = [
            f"'{status}'" if var.get() else ''
            for status, var in zip(['TOTAL', 'PARCIAL', 'AGUARDANDO FATURAMENTO', 'AGUARDANDO ENTREGA'],
                                   [var_total, var_parcial, var_aguardando_faturamento, var_aguardando_entrega])
        ]
        valores = [valor for valor in valores if valor]  # Remove os valores vazios
        resultado = ', '.join(valores)
        print(resultado)  # Substitua por qualquer ação que você deseja fazer com a lista de valores

    # Botão para exibir os valores
    botao_exibir = Button(frame_status, text='Exibir Valores', command=exibir_valores)
    botao_exibir.grid(row=5, column=0, pady=(10, 0))

# Exemplo de uso
if __name__ == "__main__":
    root = Tk()
    frame_status(root)
    root.mainloop()
