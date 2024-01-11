from tkinter import Frame, Label, SOLID
from tkcalendar import DateEntry

def frame_data(root):
    frame_data = Frame(root,
                       #relief=SOLID,
                       #bd=1,
                       )
    frame_data.place(x=158, y=5)
    
    label_data_ini = Label(frame_data, text='EMISSÃO', font=('Arial', 11))
    label_data_ini.grid(row=0, column=1, pady=(20,0), padx=(0,0), sticky='w')

    data_inicial = DateEntry(frame_data, date_pattern='dd/mm/yyyy')
    data_inicial.grid(row=1, column=1, padx=(0,0), sticky='n')
    
    label_a = Label(frame_data, text='a', font=('Arial', 11))
    label_a.grid(row=1, column=2)

    data_final = DateEntry(frame_data, date_pattern='dd/mm/yyyy')
    data_final.grid(row=1, column=3, padx=(0,20), sticky='n')