from tkinter import Button
from variaveis import gera_sql_geral   
    
def botao_pesquisar(root):
    botao_pesquisar = Button(root, text='PESQUISAR', width=15, height=1, bg='silver', command=gera_sql_geral)
    botao_pesquisar.place(x=635, y=150)
    
    