from tkinter import Button
#from exporta_excell import exporta_excell,x
#from variaveis import exporta_excell

def botao_exportar(root):
    botao_exportar = Button(root, text='EXPORTAR', width=15, height=1, bg='silver', command=lambda:exporta_excell)
    botao_exportar.place(x=636, y=455)