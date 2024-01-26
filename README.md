
#  Relatório Follow Up Setor de Compras

Este programa tem por objetivo facilitar e agilizar (agilizar bastante) o processo de acompanhamento dos pedidos de compras feitos pelos compradores da empresa diretamente com os fornecedores. Este controle, conhecido como Follow Up, é de extrema importância para aocmpanhamento das entregas dos pedidos, se estão dentro do prazo de entrega previsto para cada fornecedor em particular. Este programa contempla pedidos realizados de duas maneiras, Venda ou Bonificação, sendo a venda o processo comum de venda de mercadoria pelo fornecedor e a bonificação um 'brinde' à empresa. Quanto ao status do pedido depois de realizado, pode ser classificados de duas maneiras, entregues e não entregues. Os pedidos entregues também podem ser classificados como entrega total e entrega parcial, pois o pedido pode ser faturado e enviado à empresa de de forma parcial de acordo com a disponibilidade de estoque e dependendo de algumas particularidades inerentes da regra de negócio adotada pela empresa ou fornecedores. Os pedidos não entregues podem ser classificados como faturados(aguardando entrega) ou não faturados(aguardando faturamento). Cada uma dessas situações serão explicadas no decorrer deste artigo.

## O antigo processo

## O novo processo

# Sobre o processo de desenvolvimento
Esta aplicação eu decidi mudar a forma como eu desenvolvia. Em projetos anteriores eu sempre usava apenas um arquivo contendo todo o código para criar a aplicação, neste projeto decidi fazer diferente. Criei vários arquivos contendo funções separadas e um arquivo principal que chama as funções. Isso permitiu que fosse muito mais fácil encontrar determminados trechos do código e fazer a manutenção nos mesmos. O que eu não esperava era descobrir que esse método seria o único viável, tendo em vista que o número de linhas escritas aumentava cada vez mais e eu pude perceber que meu método antigo era inviável para esse projeto. A estrutura gráfica do programa é separada por partes de forma que possam ser alteradas separadamente sem afetar as outras partes, o que facilitou ao fazer as diversas modificações solicitadas pela equipe do setor de compras. Outra mudança em relação à contrução do programa foi voltada à utilização do client oracle necessário para fazer a conexão com o banco de dados. Em aplicações passadas, ao finalizar o projeto, eu sempre compactava o programa para a sua forma executável junto com a pasta do client. Este procedimento deixava o executável mais lento e muito maior, tendo em vista que a pasta do client tem aproximadamente 100 Mb. Neste projeto, e em projetos futuros, deixei o client separado em um servidor e programei a aplicação para apontar para este local. Este servidor é necessário estar conectado à todos os computadores da empresa para que possam acessar o ERP WinThor, então é garantido que todos os computadores dentro da rede da empresa tenham acesso à esse diretório. Esta mudança deixou a aplicação menor e mais leve, entretando, está mais sujeita a lentidão por conta de eventuais instabilidades na rede interna.

## Conexão com banco de dados Oracle
O banco de dados utilizado no ERP Winthor na empresa é Oracle e a biblioteca python utilizada para fazer a conexão com o banco foi a cx_Oracle.

conecta_banco.py
```bash
import cx_Oracle
from credenciais_oracle import *

# Encontra o arquivo que aponta para o banco de dados
cx_Oracle.init_oracle_client(lib_dir="P://instantclient_21_10")

# Faz a conexão ao banco de dados
conecta_banco = cx_Oracle.connect(usuario, senha, f'{host}/{servico}')

# Cria um cursor no banco para que seja possível fazer consultas e alterações no banco de dados
cursor = conecta_banco.cursor()
```
Note que o código acima aponta para o diretório P da máquina local(cx_Oracle.init_oracle_client(lib_dir="P://instantclient_21_10")). Este diretório contém os arquivos do Winthor, portanto todos os computadores precisam ter esse diretório mapeado para terem acesso ao sistema, por isso optei por manter o client nesse diretório, já que é garantido que ele estará disponível nos computadores que usarão essa aplicação. É importante informar que essa aplicação não é capaz de se conectar à um computador que não esteja incluida no domínio da empresa.

As variáveis com as credenciais são importadas de um arquivo separado:

credenciais_oracle.py
```bash
host = ''
servico = ''
usuario = ''
senha = ''
```

Com estes arquivos é possível fazer a conexão com o banco de dados, e sempre que for necessário fazer uma consulta, basta importar a variável 'cursor' do arquivo 'conecta_banco'.

## Consulta SQL ao banco de dados
A primeira parte do projeto foi estudar o banco de dados a fim de entender como deveria ser feito a consulta com base nas tabelas que possuem as informações relevantes para atender aos requisitos da aplicação. Após vários testes, o código SQL que faz a consulta no banco de dados é este:

```bash
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
            {fornec}
        GROUP BY
            codfornec, fornecedor, numped, dtemissao, vltotal, codfilial, codcomprador, status_entrega, tipo_pedido
        ORDER BY
            dtemissao
```
Os valores entre chaves são as variáveis cujos valores serão atribuidos de acordo com a preferência do usuário. A forma como será atribuído o valor à essas variáveis será explicado posteriormente.

Esta consulta consiste em duas partes, uma consulta interna (subconsulta) e uma consulta externa. A consulta interna irá buscar as informações diretamente no banco de dados e irá manipula-las para que os campos criados com os CASE sejam exibidos na consulta.

##

Com relação à consulta interna, os CASEs irão criar as variáveis que serão usadas para a consulta. Essas variáveis serão criadas com os seguintes critérios:

PRIMEIRO CASE(status_pedido): irá definir as variáveis do campo status_entrega. Onde TOTAL será definido quando a diferença entre o valor total e o valor entregue da tabela de pedidos de compra for igual a zero, ou seja, se o valor do pedido for igual ao valor entregue, significa que o pedido foi entregue em sua totalidade.

```bash
 WHEN ABS(p.vltotal - p.vlentregue) <= 0.1 THEN 'TOTAL'
```
Obs: nos primeiros testes foi feita  comparação se uma era igual a outra, se sim, então o pedido foi entregue de forma total. Porém, o sistema faz alguns arredondamentos causando uma mínima diferença nos valores. Portanto, para resolver este problema, a situação acima é feita a partir da diferença entre esses dois valores, desconsiderando uma diferença de até 0.1 (10 centavos).

O valor AGUARDANDO ENTREGA é atribuido quando o valor entregue da tabela de pedidos de compra é igual a zero. Porém, pode ser que o pedido já tenha sido faturando pelo fornecedor e já tenha uma nota fiscal para essas mercadorias. Portanto, além do valor entregue ser igual a zero, é necessário verificar se existe alguma movimentação de entrada, na tabela de movimentação de entrada de mercadoria, relacionado ao pedido de compra em questão. Atendendo à essas duas situações, o valor AGUARDANDO ENTREGA é atribuido.

```bash
WHEN p.vlentregue = 0 AND EXISTS (
                        SELECT DISTINCT numnota FROM pcmovpreent WHERE numped = p.numped
                    ) THEN 'AGUARDANDO ENTREGA'
```

O valor AGUARDANDO FATURAMENTO é obtido de forma semelhante ao 'aguardando entrega', a diferença que além do valor entrege do pedido ser igual a zero, não pode ter nenhuma movimentaçãode entrega registrada no banco de dados. Atendendo à essas duas situações, supões-se que ainda não foi emitida nenhuma nota fiscal referente ao pedido de compra em questão.

```bash
WHEN p.vlentregue = 0 AND NOT EXISTS (
                        SELECT DISTINCT numnota FROM pcmovpreent WHERE numped = p.numped
                    ) THEN 'AGUARDANDO FATURAMENTO'
```

O valor PARCIAL é o mais simples dentre os demais. Basicamente é se o valor entregue do pedido é diferente no valor total do mesmo. Assim, supõe-se que parte do pedido já foi entregue. Ou se nenhuma das situações anteriores forem atendidas.

```bash
ELSE 'PARCIAL'
```

##

SEGUNDO CASE(tipo_pedido): mais simples que o primeiro, apenas irá definir um valor para o tipo de pedido que foi feito. Se na tabela de pedido de compras o campo tipobonific for B, então recebe o valor BONIFICAÇÃO. Se for N, então recebe o valor VENDA.

```bash
WHEN p.tipobonific = 'B' THEN 'BONIFICADO'
WHEN p.tipobonific = 'N' THEN 'VENDA'
```







```bash
  npm run deploy
```

