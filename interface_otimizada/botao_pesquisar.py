from tkinter import Button
from consulta_sql import consulta
from variaveis import gera_sql_geral
#from frame_tipo import *
#from variaveis import *
"""import sys
sys.path.append('../interface_otimizada')"""
def x():
    from variaveis import resultado_tipo_sql, resultado_status_sql, codigo_fornecedor_sql,codigo_filial_sql, codigo_comprador_sql, data_inicial_sql, data_final_sql
    print(resultado_tipo_sql)
    print(resultado_status_sql)
    print(codigo_fornecedor_sql)
    print(codigo_filial_sql)
    print(codigo_comprador_sql)
    print(data_inicial_sql)
    print(data_final_sql)
    
    
def botao_pesquisar(root):
    botao_pesquisar = Button(root, text='PESQUISAR', width=15, height=1, bg='silver', command=lambda:gera_sql_geral())
    botao_pesquisar.place(x=635, y=150)
    
    