from tkinter import Frame, Label, SOLID, ttk
#from tkinter import ttk
from tkcalendar import DateEntry


def frame_cabecalho1(root) :
    frame_cabecalho1 = Frame(root,
                            #width = 640,
                            #height = 50,
                            #relief = SOLID,
                            #bd = 1
                            )
    frame_cabecalho1.pack(anchor='w', pady=(5,0), padx=(40,0))
    
    label_filial = Label(frame_cabecalho1, text='Filial')
    label_filial.grid(row=0, column=0, pady=(20,0), padx=(20,0))

    campo_filial = ttk.Combobox(frame_cabecalho1, width=4, values=['','1','3','4','5','6','7','17','18','19','20','61','70'])
    campo_filial.grid(row=1, column=0, padx=(20,0), sticky='n')

    label_data_ini = Label(frame_cabecalho1, text='Data Inicial')
    label_data_ini.grid(row=0, column=2, pady=(20,0), padx=(20,0))

    data_inicial = DateEntry(frame_cabecalho1, date_pattern='dd/mm/yyyy')
    data_inicial.grid(row=1, column=2, padx=(20,0), sticky='n')

    label_data_fin = Label(frame_cabecalho1, text='Data Final')
    label_data_fin.grid(row=0,column=3, pady=(20,0), padx=(20,0), sticky='w')

    data_final = DateEntry(frame_cabecalho1, date_pattern='dd/mm/yyyy')
    data_final.grid(row=1,column=3, padx=(5,20), sticky='n')

    label_tipo = Label(frame_cabecalho1, text='Tipo Pedido')
    label_tipo.grid(row=0, column=4, pady=(20,0),padx=(15,0), sticky='w')

    campo_tipo = ttk.Combobox(frame_cabecalho1, width=13, values=['Venda','Bonificado'])
    campo_tipo.grid(row=1, column=4, padx=(0,20), sticky='n')

    label_status = Label(frame_cabecalho1, text='Status Pedido')
    label_status.grid(row=0, column=5, pady=(20,0), padx=(12,0), sticky='w')

    campo_status = ttk.Combobox(frame_cabecalho1, width=13, values=['Entregue','Ag. Entrega','Ag. Faturamento'])
    campo_status.grid(row=1, column=5, padx=(0,20), sticky='n')