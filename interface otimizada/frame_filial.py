from tkinter import Frame, Label, SOLID, Entry, Button

def frame_filial(root) :
    frame_filial = Frame(root,
                        #relief = SOLID,
                        #bd = 1
                        )
    frame_filial.pack(anchor='w', pady=(5,0), padx=(40,0))
    
    label_filial = Label(frame_filial, text='FILIAL', font=('Arial', 11))
    label_filial.grid(row=0, column=0, pady=(20,0), padx=(0,0), sticky='w')

    campo_filial = Entry(frame_filial, width=7)
    campo_filial.grid(row=1, column=0, padx=(0,0), sticky='nw')
    
    botao_filial = Button(frame_filial, text='...', width='1', height='1', bg='silver')
    botao_filial.grid(row=1, column=1, padx=(10,0), sticky='n')
