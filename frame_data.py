from tkinter import Frame, Label, SOLID
from tkcalendar import DateEntry
from variaveis import atualizar_data_inicial_sql, atualizar_data_final_sql


def frame_data(root):
    frame_data = Frame(root,
                       #relief=SOLID,
                       #bd=1,
                       )
    frame_data.place(x=158, y=5)
    
    def salvar_datas(event):
        data_ini = data_inicial.get_date()
        data_fim = data_final.get_date()

        global data_ini_formatada
        global data_fim_formatada
        # Formatar as datas no formato desejado (dia-mês-ano)
        formato_data = "%d-%b-%Y"
        data_ini_formatada = data_ini.strftime(formato_data)
        data_fim_formatada = data_fim.strftime(formato_data)

        atualizar_data_inicial_sql(data_ini_formatada)
        atualizar_data_final_sql(data_fim_formatada)
    
    
    label_data_ini = Label(frame_data, text='EMISSÃO', font=('Arial', 9))
    label_data_ini.grid(row=0, column=1, pady=(20,0), padx=(0,0), sticky='w')
    
    data_inicial = DateEntry(frame_data, date_pattern='dd/mm/yyyy')
    data_inicial.grid(row=1, column=1, pady=(3,0), padx=(0,0), sticky='n')
    data_inicial.bind("<<DateEntrySelected>>", salvar_datas)  # Associa o evento à função
    #data_inicial.set_date(None)
    
    label_a = Label(frame_data, text='a', font=('Arial', 9))
    label_a.grid(row=1, column=2)

    data_final = DateEntry(frame_data, date_pattern='dd/mm/yyyy')
    data_final.grid(row=1, column=3, pady=(3,0), padx=(0,20), sticky='n')
    data_final.bind("<<DateEntrySelected>>", salvar_datas)  # Associa o evento à função
    #data_final.set_date(None)
    
    return frame_data
    salvar_datas(None)