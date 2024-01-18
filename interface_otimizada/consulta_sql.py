from conecta_banco import cursor
from variaveis import codigo_filial_sql, data_inicial_sql, data_final_sql, codigo_comprador_sql, resultado_status_sql, resultado_tipo_sql
from variaveis import atualizar_resultado_consulta_geral

if "AGUARDANDO" in resultado_status_sql:

    sql_geralx = f"""SELECT
        codfornec,
        fornecedor,
        numped,
        dtemissao,
        vltotal,
        codfilial,
        codcomprador,
        NOTAS_FISCAIS,
        status_entrega,
        tipo_pedido
        
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
    UNION ALL
    SELECT
        codfornec,
        fornecedor,
        numped,
        dtemissao,
        vltotal,
        codfilial,
        codcomprador,
        COALESCE(NULLIF(LISTAGG(NUMNOTA, ', ') WITHIN GROUP (ORDER BY NUMNOTA), ''), ' ') AS NOTAS_FISCAIS,
        status_entrega,
        tipo_pedido
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



    
    sql_geral2 = f"""SELECT
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
                AND N.ESPECIE = 'NF'
        ) 
        WHERE
            status_entrega IN ({resultado_status_sql})
            AND tipo_pedido IN ({resultado_tipo_sql})
        GROUP BY
            codfornec, fornecedor, numped, dtemissao, vltotal, codfilial, codcomprador
        ORDER BY
            dtemissao"""
        
        
def consulta():
    print(sql_geralx)
    #global resultado_consulta_geral
    #cursor.execute(sql_geral)
    #resultado_consulta_geral = cursor.fetchall()
    #atualizar_resultado_consulta_geral(resultado_consulta_geral)
    
    #return resultado_consulta_geral
