resultado_tipo_sql =''

resultado_status_sql =''

codigo_fornecedor_sql =''

codigo_filial_sql =''

codigo_comprador_sql =''

def atualizar_resultado_tipo_sql(novo_valor):
    global resultado_tipo_sql
    resultado_tipo_sql = novo_valor
    #print(resultado_tipo_sql)
    #return resultado_tipo_sql
    
def atualizar_resultado_status_sql(novo_valor):
    global resultado_status_sql
    resultado_status_sql = novo_valor
    
def atualizar_codigo_fornecedor_sql(novo_valor):
    global codigo_fornecedor_sql
    codigo_fornecedor_sql = novo_valor

"""def atualiza_campo_filial(valor):
    campo_filial.set(valor)"""
    
#from frame_filial import campo_filial
def atualiza_codigo_filial_sql(novo_valor):
    global codigo_filial_sql
    codigo_filial_sql = novo_valor
    #atualiza_campo_filial(codigo_filial_sql)
    
def atualiza_codigo_comprador_sql(novo_valor):
    global codigo_comprador_sql
    codigo_comprador_sql = novo_valor
    