from conecta_banco import cursor
#from exporta_excell import exporta_excell


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
    print(f"Tipo: {resultado_tipo_sql}")
    #return resultado_tipo_sql
    
def atualizar_resultado_status_sql(novo_valor):
    global resultado_status_sql
    resultado_status_sql = novo_valor
    print(f"Status: {resultado_status_sql}")
    
def atualizar_codigo_fornecedor_sql(novo_valor):
    from frame_forn_comp import atualiza_campo_fornecedor, campo_fornecedor
    global codigo_fornecedor_sql
    codigo_fornecedor_sql = novo_valor
    print(f"Fornecedores: {codigo_fornecedor_sql}")
    atualiza_campo_fornecedor(campo_fornecedor, codigo_fornecedor_sql)

#from frame_filial import campo_filial
def atualiza_codigo_filial_sql(novo_valor):
    from frame_filial import atualiza_campo_filial, campo_filial
    global codigo_filial_sql
    codigo_filial_sql = novo_valor
    print(f"Filiais: {codigo_filial_sql}")
    atualiza_campo_filial(campo_filial,codigo_filial_sql)
    
def atualiza_codigo_comprador_sql(novo_valor):
    from frame_forn_comp import atualiza_campo_comprador, campo_comprador
    global codigo_comprador_sql
    codigo_comprador_sql = novo_valor
    print(f"Compradores: {codigo_comprador_sql}")
    atualiza_campo_comprador(campo_comprador,codigo_comprador_sql)
    
def atualizar_data_inicial_sql(novo_valor):
    global data_inicial_sql
    data_inicial_sql = novo_valor
    print(f"Data Inicial: {data_inicial_sql}")
    
def atualizar_data_final_sql(novo_valor):
    global data_final_sql
    data_final_sql = novo_valor
    print(f"Data Final: {data_final_sql}")
    
def atualizar_resultado_consulta_geral(novo_valor):
    global consulta_geral_sql
    consulta_geral_sql = novo_valor
    print(consulta_geral_sql)
    from treeview import atualiza_tree, tree
    atualiza_tree(tree.resultado_consulta_geral)
    print(consulta_geral_sql)

def gera_sql_geral():
    from frame_filial import campo_filial
    codigo_filial_sql = campo_filial.get()
    from frame_forn_comp import campo_fornecedor, campo_comprador
    codigo_fornecedor_sql = campo_fornecedor.get()
    codigo_comprador_sql = campo_comprador.get()
    global sql_geral
    
    if "AGUARDANDO" in resultado_status_sql:
        sql_geral = f"""SELECT
                dtemissao,
                codfilial,
                numped,
                codfornec,
                fornecedor,
                codcomprador,
                vltotal,
                tipo_pedido,
                status_entrega,
                NOTAS_FISCAIS
            FROM (
                -- Sua primeira consulta aqui
                SELECT
                    codfornec,
                    fornecedor,
                    numped,
                    dtemissao,
                    vltotal,
                    codfilial,
                    codcomprador,
                    LISTAGG(NUMNOTA, ', ') WITHIN GROUP (ORDER BY NUMNOTA) AS NOTAS_FISCAIS,
                    MAX(status_entrega) AS status_entrega,
                    MAX(tipo_pedido) AS tipo_pedido
                FROM (
                    SELECT
                        p.codfornec,
                        f.fornecedor,
                        p.numped,
                        p.dtemissao,
                        p.vltotal,
                        p.codfilial,
                        p.codcomprador,
                        N.NUMNOTA,
                        CASE
                            WHEN ABS(p.vltotal - p.vlentregue) <= 0.1 THEN 'TOTAL'
                            WHEN p.vlentregue = 0 THEN 'PENDENTE'
                            ELSE 'PARCIAL'
                        END AS status_entrega,
                        CASE
                            WHEN p.tipobonific = 'B' THEN 'BONIFICADO'
                            WHEN p.tipobonific = 'N' THEN 'VENDA'
                        END AS tipo_pedido
                    FROM
                        pcpedido p
                        LEFT JOIN pcfornec f ON p.codfornec = f.codfornec
                        LEFT JOIN PCPEDNF PN ON p.numped = PN.numpedido
                        LEFT JOIN PCNFENT N ON PN.numtransent = N.numtransent
                    WHERE
                        p.codfilial IN ({codigo_filial_sql})
                        AND p.dtemissao BETWEEN TO_DATE('{data_inicial_sql}', 'DD-MON-YYYY') AND TO_DATE('{data_final_sql}', 'DD-MON-YYYY')
                        AND p.codcomprador IN ({codigo_comprador_sql})
                        AND N.ESPECIE in ('NF')
                ) 
                WHERE
                    status_entrega IN ({resultado_status_sql})
                    AND tipo_pedido IN ({resultado_tipo_sql})
                GROUP BY
                    codfornec, fornecedor, numped, dtemissao, vltotal, codfilial, codcomprador
                ORDER BY
                    dtemissao
            ) 
            UNION
            SELECT
                dtemissao,
                codfilial,
                numped,
                codfornec,
                fornecedor,
                codcomprador,
                vltotal,
                tipo_pedido,
                status_entrega,
                COALESCE(NULLIF(LISTAGG(NUMNOTA, ', ') WITHIN GROUP (ORDER BY NUMNOTA), ''), ' ') AS NOTAS_FISCAIS
            FROM (
                -- Segunda consulta aqui
                SELECT
                    p.codfornec,
                    f.fornecedor,
                    p.numped,
                    p.dtemissao,
                    p.vltotal,
                    p.codfilial,
                    p.codcomprador,
                    PN.NUMNOTA,
                    MAX(CASE
                        WHEN ABS(p.vltotal - p.vlentregue) <= 0.1 THEN 'TOTAL'
                        WHEN p.vlentregue = 0 AND EXISTS (
                            SELECT DISTINCT numnota FROM pcmovpreent WHERE numped = p.numped
                        ) THEN 'AGUARDANDO ENTREGA'
                        WHEN p.vlentregue = 0 AND NOT EXISTS (
                            SELECT DISTINCT numnota FROM pcmovpreent WHERE numped = p.numped
                        ) THEN 'AGUARDANDO FATURAMENTO'
                        ELSE 'PARCIAL'
                    END) AS status_entrega,
                    MAX(CASE
                        WHEN p.tipobonific = 'B' THEN 'BONIFICADO'
                        WHEN p.tipobonific = 'N' THEN 'VENDA'
                    END) AS tipo_pedido
                FROM
                    pcpedido p
                    LEFT JOIN pcfornec f ON p.codfornec = f.codfornec
                    LEFT JOIN PCMOVPREENT PN ON p.numped = PN.numped
                    LEFT JOIN PCNFENT N ON PN.numtransent = N.numtransent AND PN.NUMTRANSENT = N.NUMTRANSENT
                WHERE
                    p.codfilial IN ({codigo_filial_sql})
                    AND p.dtemissao BETWEEN TO_DATE('{data_inicial_sql}', 'DD-MON-YYYY') AND TO_DATE('{data_final_sql}', 'DD-MON-YYYY')
                    AND p.codcomprador IN ({codigo_comprador_sql})
                GROUP BY
                    p.codfornec, f.fornecedor, p.numped, p.dtemissao, p.vltotal, p.codfilial, p.codcomprador, PN.NUMNOTA
            ) subquery
            WHERE
                status_entrega IN ({resultado_status_sql})
                AND tipo_pedido IN ({resultado_tipo_sql})
            GROUP BY
                codfornec, fornecedor, numped, dtemissao, vltotal, codfilial, codcomprador, status_entrega, tipo_pedido
            ORDER BY
                dtemissao"""
                
    else: 
        sql_geral = f"""SELECT
            dtemissao,
            codfilial,
            numped,
            codfornec,
            fornecedor,
            codcomprador,
            vltotal,
            MAX(tipo_pedido) AS tipo_pedido,
            MAX(status_entrega) AS status_entrega,
            LISTAGG(NUMNOTA, ', ') WITHIN GROUP (ORDER BY NUMNOTA) AS NOTAS_FISCAIS,    
        FROM (
            SELECT
                p.codfornec,
                f.fornecedor,
                p.numped,
                p.dtemissao,
                p.vltotal,
                p.codfilial,
                p.codcomprador,
                N.NUMNOTA,
                CASE
                    WHEN ABS(p.vltotal - p.vlentregue) <= 0.1 THEN 'TOTAL'
                    WHEN p.vlentregue = 0 THEN 'PENDENTE'
                    ELSE 'PARCIAL'
                END AS status_entrega,
                CASE
                    WHEN p.tipobonific = 'B' THEN 'BONIFICADO'
                    WHEN p.tipobonific = 'N' THEN 'VENDA'
                END AS tipo_pedido
            FROM
                pcpedido p
                LEFT JOIN pcfornec f ON p.codfornec = f.codfornec
                LEFT JOIN PCPEDNF PN ON p.numped = PN.numpedido
                LEFT JOIN PCNFENT N ON PN.numtransent = N.numtransent
            WHERE
                p.codfilial IN ({codigo_filial_sql})
                AND p.dtemissao BETWEEN TO_DATE('{data_inicial_sql}', 'DD-MON-YYYY') AND TO_DATE('{data_final_sql}', 'DD-MON-YYYY')
                AND p.codcomprador IN ({codigo_comprador_sql})
                AND N.ESPECIE = 'NF'
        ) 
        WHERE
            status_entrega IN ({resultado_status_sql})
            AND tipo_pedido IN ({resultado_tipo_sql})
        GROUP BY
            codfornec, fornecedor, numped, dtemissao, vltotal, codfilial, codcomprador
        ORDER BY
            dtemissao"""
                
    
    cursor.execute(sql_geral)
    global dados
    dados = cursor.fetchall()
    #print(dados)
    #return dados
    from treeview import tree
    for item in tree.get_children():
        tree.delete(item)

    # Preencher a Treeview com os dados
    for row in dados:
        tree.insert('', 'end', values=row)
    return dados
    

    
