resultado_tipo_sql =''

resultado_status_sql =''

codigo_fornecedor_sql =''

codigo_filial_sql =''

codigo_comprador_sql =''

data_inicial_sql =''

data_final_sql =''

def atualizar_resultado_tipo_sql(novo_valor):
    global resultado_tipo_sql
    resultado_tipo_sql = novo_valor
    #print(resultado_tipo_sql)
    #return resultado_tipo_sql
    
def atualizar_resultado_status_sql(novo_valor):
    global resultado_status_sql
    resultado_status_sql = novo_valor
    
def atualizar_codigo_fornecedor_sql(novo_valor):
    from frame_forn_comp import atualiza_campo_fornecedor, campo_fornecedor
    global codigo_fornecedor_sql
    codigo_fornecedor_sql = novo_valor
    atualiza_campo_fornecedor(campo_fornecedor, codigo_fornecedor_sql)

#from frame_filial import campo_filial
def atualiza_codigo_filial_sql(novo_valor):
    from frame_filial import atualiza_campo_filial, campo_filial
    global codigo_filial_sql
    codigo_filial_sql = novo_valor
    atualiza_campo_filial(campo_filial,codigo_filial_sql)
    
def atualiza_codigo_comprador_sql(novo_valor):
    from frame_forn_comp import atualiza_campo_comprador, campo_comprador
    global codigo_comprador_sql
    codigo_comprador_sql = novo_valor
    atualiza_campo_comprador(campo_comprador,codigo_comprador_sql)
    
def atualizar_data_inicial_sql(novo_valor):
    global data_inicial_sql
    data_inicial_sql = novo_valor
    
def atualizar_data_final_sql(novo_valor):
    global data_final_sql
    data_final_sql = novo_valor
    
