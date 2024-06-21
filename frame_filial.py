from tkinter import Frame, Label, SOLID, Entry, Button
from toplevel_filial import toplevel_filial

def frame_filial(root) :
    frame_filial = Frame(root,
                        #relief = SOLID,
                        #bd = 1
                        )
    frame_filial.pack(anchor='w', pady=(5,0), padx=(40,0))
    
    label_filial = Label(frame_filial, text='FILIAL', font=('Arial', 9))
    label_filial.grid(row=0, column=0, pady=(20,0), padx=(0,0), sticky='w')

    global campo_filial
    campo_filial = Entry(frame_filial, width=7)
    campo_filial.grid(row=1, column=0, padx=(0,0), sticky='w')
    
    botao_filial = Button(frame_filial, text='...', width='1', height='1', bg='silver', command=lambda:toplevel_filial(root))
    botao_filial.grid(row=1, column=1, padx=(2,0), sticky='n')
   
    return frame_filial
    #return campo_filial
    
def atualiza_campo_filial(campo_filial,valor):
    campo_filial.delete(0, 'end')
    campo_filial.insert(0, valor)
    