
#  Relatório Follow Up Setor de Compras

Este programa tem por objetivo facilitar e agilizar (agilizar bastante) o processo de acompanhamento dos pedidos de compras feitos pelos compradores da empresa diretamente com os fornecedores. Este controle, conhecido como Follow Up, é de extrema importância para aocmpanhamento das entregas dos pedidos, se estão dentro do prazo de entrega previsto para cada fornecedor em particular. Este programa contempla pedidos realizados de duas maneiras, Venda ou Bonificação, sendo a venda o processo comum de venda de mercadoria pelo fornecedor e a bonificação um 'brinde' à empresa. Quanto ao status do pedido depois de realizado, pode ser classificados de duas maneiras, entregues e não entregues. Os pedidos entregues também podem ser classificados como entrega total e entrega parcial, pois o pedido pode ser faturado e enviado à empresa de de forma parcial de acordo com a disponibilidade de estoque e dependendo de algumas particularidades inerentes da regra de negócio adotada pela empresa ou fornecedores. Os pedidos não entregues podem ser classificados como faturados(aguardando entrega) ou não faturados(aguardando faturamento). Cada uma dessas situações serão explicadas no decorrer deste artigo.

## O antigo processo

## O novo processo

# Sobre o processo de desenvolvimento
Esta aplicação eu decidi mudar a forma como eu desenvolvia. Em projetos anteriores eu sempre usava apenas um arquivo contendo todo o código para criar a aplicação, neste projeto decidi fazer diferente. Criei vários arquivos contendo funções separadas e um arquivo principal que chama as funções. Isso permitiu que fosse muito mais fácil encontrar determminados trechos do código e fazer a manutenção nos mesmos. O que eu não esperava era descobrir que esse método seria o único viável, tendo em vista que o número de linhas escritas aumentava cada vez mais e eu pude perceber que meu método antigo era inviável para esse projeto. A estrutura gráfica do programa é separada por partes de forma que possam ser alteradas separadamente sem afetar as outras partes, o que facilitou ao fazer as diversas modificações solicitadas pela equipe do setor de compras. Outra mudança em relação à contrução do programa foi voltada à utilização do client oracle necessário para fazer a conexão com o banco de dados. Em aplicações passadas, ao finalizar o projeto, eu sempre compactava o programa para a sua forma executável junto com a pasta do client. Este procedimento deixava o executável mais lento e muito maior, tendo em vista que a pasta do client tem aproximadamente 100 Mb. Neste projeto, e em projetos futuros, deixei o client separado em um servidor e programei a aplicação para apontar para este local. Este servidor é necessário estar conectado à todos os computadores da empresa para que possam acessar o ERP WinThor, então é garantido que todos os computadores dentro da rede da empresa tenham acesso à esse diretório. Esta mudança deixou a aplicação menor e mais leve, entretando, está mais sujeita a lentidão por conta de eventuais instabilidades na rede interna.

## Conexão com banco de dados Oracle
O banco de dados utilizado no ERP Winthor na empresa é Oracle e a biblioteca python utilizada para fazer a conexão com o banco foi a cx_Oracle.

`conecta_banco.py`
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

`credenciais_oracle.py`
```bash
host = ''
servico = ''
usuario = ''
senha = ''
```

Com estes arquivos é possível fazer a conexão com o banco de dados, e sempre que for necessário fazer uma consulta, basta importar a variável 'cursor' do arquivo 'conecta_banco'.

## Consulta SQL
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

##
Outro ponto importante da consulta é o relacionamento entre as tabelas. Esse foi um dos pontos mais desafiadores deste projeto.

```bash
FROM
    pcpedido p
    LEFT JOIN pcfornec f ON p.codfornec = f.codfornec
    LEFT JOIN PCMOVPREENT PN ON p.numped = PN.numped
    LEFT JOIN PCNFENT N ON PN.numtransent = N.numtransent AND PN.NUMTRANSENT = N.NUMTRANSENT
```
O código do fornecedor da tabela de pedidos (P) deve se relacionar com o código do fornecedor da tabela de fornecedores (F). Este relacionamento é importante para trazer à consulta o nome do fornecedor corretamente.

O número do pedido da tabela P deve estar alinhada com o número do pedido da tabela de movimentação de entrada (PN). A partir deste relacionamento vai ser possível verificar se o pedido em questão atenderá os requisitos dos valores AGUARDANDO FATURAMENTO e AGUARDANDO ENTREGA. Tendo em vista que, se neste pedido não há registro de movimentação de entrada, então não há uma pré entrada deste pedido, portanto, não há nota faturada, AGUARDANDO FATURAMENTO. 

Cada movimentação de pré-entrada gera um número de transação e cada nota fiscal de entrada gerada proveniente dessa pré-entrada, proveniente desse pedido (pois cada pedido pode ter várias notas fiscais), possui o mesmo número de transação. Esse relacionamento entre as tabelas PN e a tabela de notas fiscais de entrada (N) tornarão possível buscar todas as notas fiscais referentes ao pedido de compra.

Estes são os pontos que merecem atenção especial na construção do código que irá fazer a consulta no banco. O LEFT JOIN foi usado nesses relacionamentos pois nem sempre o valor de uma tabela será encontrada em outra, exemplo: em AGUARDANDO FATURAMENTO, não será possível será possível encontrar o número do pedido na tabela PN, se fosse um INNER JOIN o código não funcionaria nesse caso.
Posterior à isso estão as clausulas que servirão de filtros para a subconsulta.

É importante explicar que não seria possível fazer essa consulta sem uma sub consulta. Pois nos requisitos do desenvolvimento da aplicação era necessário expor campos que não existem no banco de dados, como por exemplo o status do pedido. Por esse motivo foi necessário criar esses campo com os CASEs na subconsulta (consulta interna como eu mencionei anteriormente) para que a consulta externa pudesse manipular os valores desses campos que foram criados.

## Criando a interface gráfica principal

Como dito anteriomente, este programa foi dividido em vários arquivos onde cada um dos arquivos possui elementos fundamentais para o funcionamento da aplicação como um todo. A arquitetura desde programa foi projetada para um arquivo principal (`main.py`) criasse a janela principal de forma básica e fizesse a chamada de todos os outros elementos que irão compor a interface através de funções. Observe que este arquivo importa a maioria das funções presentes no programa:

```bash
import tkinter as tk
from frame_filial import frame_filial
from frame_data import frame_data
from frame_tipo import frame_tipo
from frame_status import frame_status
from frame_forn_comp import frame_forn_comp
from treeview import treeview
from label_assinatura import label_assinatura
from botao_exportar import botao_exportar
from botao_pesquisar import botao_pesquisar
```

Sobre a construção da interface gráfica principal, estes foras os arquivos criados contendo os frames para montar a interface principal como um todo:

- `frame_filial.py`: contém o label 'FILIAL', o campo Entry, o botão que exibe o toplevel com todas as filiais e a função que atualiza o campo entry.

- `frame_data.py`: contém o label 'EMISSÃO' e 'a', dois campos DateEntry (um para data inicial e outro para data final) e a função que salva as datas em variáveis para a consulta em SQL no arquivo `variaveis.py`.

- `frame_tipo.py`: contém a label 'TIPO DE PEDIDO', os Checkbuttons com seus respectivos valores (VENDA e BONIFICAÇÃO) e função que salva os valores selecionados em uma lista e faz um tratamento com os valore dessa lista, deixa na forma adequada para a consulta SQL e envia para uma função no arquivo `variaveis.py` para salvar essa variável.

- `frame_status.py`: Este arquivo segue de forma identica a lógica do arquivo `frame_tipo.py`, a diferença é o que está escrito na Label e a quantidade de Checkbuttons e seus respectivos valores(TOTAL, PARCIAL, AGUARDANDO FATURAMENTO e AGUARDANDO ENTREGA).

- `frame_forn_comp.py`: contém os Labels 'FORNECEDOR' e 'COMPRADOR' com seus respectivos campos Entry e seus respectivos botões que exibem o toplevel com os compradores e fornecedores, e as funções que atualizam os valores dos campos.

- `treeview.py`: possui a Treeview com a configuração de todas as colunas, como cabeçalho, alinhameto e afins.

- `label_assinatura.py`: possui um Label com assinatura do autor com uma função redireciona o usuário para a página web deste repositório.

- `botao_exportar.py`: contém o botão responsável por chamar a função que realiza coleta os dados da consulta e salva em um arquivo excel. Essa função é importada de ouro arquivo.

- `botao_pesquisar`: contém o botão com a função de chamar a função responsável por salvar as variáveis FILIAIS, FORNECEDORES e COMPRADORES e fazer a consulta. A função em questão é `gera_sql_geral` e é importada do arquivo `variaveis.py`.


Importante lembrar que a aplicação tem outras 3 interfaces secundárias para coleta de dados de filiais, fornecedores e compradores. Estas interfaces (Toplevel) serão explicadas posteriormente.

## Interfaces secundárias (Toplevel)

A interface principal está integrada com outras três interfaces menores que serão exibidas ao clicar nos botões contidos nos frames filial, fornecedor e comprador. Essas interfaces não são essenciais para o funcionamento do programa, elas foram incluídas para auxiliar o usuário nas consultas exibindo valores em checkbuttons para ser selecionados, onde este procedimento é dispensável caso o usuário tenha colocado esses valores de forma manual nos campos Entry de filial, fornecedor e comprador.

`toplevel_filial.py`

Responsável pela construção da toplevel contendo todas as filiais ativas no banco de dados. Ao iniciar o programa é feito uma consulta prévia para exibir as filiais disponíveis para a consulta.

```bash
SELECT codigo, razaosocial FROM pcfilial WHERE dtexclusao IS NULL ORDER BY codigo
```

Esta consulta é realizada mesmo sem o usuário acessar o toplevel de filiais. Ao abrir essa interface, é construida toda a estrutura para comportar as informações provenientes da consulta. Além da janela é criado um Canvas e um Frame dentro deste Canvas. Desta forma é possível organizar melhor os no Frame. O Canvas é necessário para que seja possível incluir uma barra de rolagem vertical para exibir os valores que não cabem na janela, o mesmo não é possível com o Frame. Neste arquivo também contém uma função(`atualizar_selecao`), que quando acionada pelo botão CONFIRMAR, que atualizao valor da variável de acordo com as filiais que foram selecionadas pelo usuário. Ela capta os valores, os trata para que sejam separados com vírgula quando necessário para ser usada na consulta SQL e em seguida esse valor é inserido em outra função(`atualiza_codigo_filial_sql`)importada do arquivo `variaveis.py` que irá armazenar esse valor para posteriormente ser usada na consulta SQL.

`toplevel_comprador.py`

Este arquivo segue exatamente a mesma lógica aplicada no toplevel filial, mudando apenas a consulta SQL inicial que irá exibir os compradores e o nome das funções.

```bash
SELECT codigo, razaosocial FROM pcfilial WHERE dtexclusao IS NULL ORDER BY codigo
```
A função responsável por armazenar a variável no arquivo `variaveis.py` é `atualiza_codigo_comprador_sql`.

`toplevel_fornecedor.py`

Apesar de semelhante ao toplevels citados anteriormente, esta interface possui algumas peculiaridades que fogem um pouco à regra das demais. Como são milhares de fornecedores cadastrados no banco de dados, seria inviável trazer essa consulta, pois a aplicação certamente iria travar e seria bem complicado buscar um ou três fornecedores específicos entre milhares. 

A diferença desse toplevel para os demais é que este possui dois campos Entry voltados para filtrar a pesquisa de fornecedores acompanhados de um botão para executar a pesquisa. Um dos campos é destinado apenas para fazer a consulta pelo código do fornecedor, o outro campo faz a consulta apenas pelo nome do mesmo. Apenas ao executar a pesquisa é que os dados são inseridos no canvas seguindo à logica citada anteriormente.

Outra peculiaridade é a necessidade de excluir todos os dados que foram exibidos na consulta anterior, tendo em vista que pode ser necessário pesquisar novamente em caso de erro de digitação do usuário ou outras situações. A função que executa esta tarefa se chama nova_consulta. Os valores armazenados pela seleção também são enviados pelos para o arquivo `variaveis.py` seguindo a mesma lógica citada anteriormenete pela função `atualiza_codigo_fornecedor_sql`.

## Manipulando as variáveis da consulta SQL

A aplicação funciona com 7 variáveis responsáveis por compor or filtros necessários para fazer a consulta no banco de dados, apenas uma não é obrigatória. São elas: 
- FILAIS;
- FORNECEDORES (não obrigatória);
- COMPRADORES;
- TIPO DO PEDIDO;
- ESTATUS DO PEDIDO;
- DATA INICIAL;
- DATA FINAL.

As variáveis FILIAIS, FORNECEDORES e COMPRADORES são obtidas a partir do campo Entry de cada um. Se o usuário utilizar os topleveis, ao confirmar a seleção, o valor escolhido será enviado para o campo Entry através de uma função(`atualiza_codigo_filial_sql`, `atualiza_codigo_comprador_sql` e `atualiza_codigo_fornecedor_sql`) presente no arquivo `variaveis.py` que faz uso de funções em seus respectivos frames para incluir o valor da variável nos campos Entry(`atualiza_campo_filial`, `atualiza_campo_comprador` e `atualiza_campo_fornecedor`). Ao clicar no botão pesquisar, a função `gera_sql_geral` é chamada de `variaveis.py` e coleta os valores contidos dentro dos campos Entry e executa a consulta com esses valores. Desta forma, não é necessário que o usuário acesse os topleveis para que a consulta funcione, tendo em vista que a consulta será realizada com os valores contidos nos campos Entry, sejam eles inseridos manualmente ou com o auxílio dos topleveis.

As variáveis com o TIPO do pedido e o STATUS são são atualizadas ao clicar no checkbutton pela função `exibir_valores_tipo` e `exibir_valores_status`, e atualizadass e armazenadas na tabela de variáveis pelas funções `atualizar_resultado_tipo_sql` e `atualizar_resultado_status_sql`. Ao clicar em PESQUISAR, essas variáveis irão para a consulta SQL.

As variáveis do tipo de data funcionam da mesma forma que as demais, a diferença é o tratamento mais rigoroso com a sintaxe, para que aconteça a consulta sem erros. A função resposável pela conversão dos valores obtidos do calendário é `salvar_datas` e as funções responsáveis por armazenar os valores das variáveis são `atualizar_data_inicial_sql` e `atualizar_data_final_sql`.

OBS: os valores de todas as variáveis são tratados de forma que respeitem a sintaxe da linguagem SQL.

## Executando a consulta SQL

A variável com o código SQL está no arquivo `variaveis.py` juntamente com todas as variáveis necessárias para execução da consulta pela função `gera_sql_geral`. Essa função é responsável por coletar os valores dos campos Entry e inserir esses valores nas variáveis juntamente com as variáveis de TIPO e STATUS. Um ponto de destaque importante nessa função é sobre a não obrigatpriedade do uso da variável dos fornecedores. No código da consulta SQL discutida no começo desse artigo é possível ver a variável `fornec` e o seu valor é definido a partir da seguinte forma:

```bash
if codigo_fornecedor_sql != '':
        fornec = f"AND codfornec IN ({codigo_fornecedor_sql})"
```

Se o valor for vazio não irá interfeir no funcionamento da consulta e não será incluido a cláusula de dos fornecedores. Mas se houver um valor, será incluído uma linha com essa cláusula para consultar por fornecedores

## Exibindo o resultado da consulta

Ao execultar a consulta, todo o resultado é armazenado na variável `dados` gerado pela função `gera_sql_geral`. Ao final dessa função esses dados são incluídos dentro da treeview localizada na interface principal da aplicação.

```bash
dados = cursor.fetchall()
    from treeview import tree
    for item in tree.get_children():
        tree.delete(item)

    # Preencher a Treeview com os dados
    for row in dados:
        tree.insert('', 'end', values=row)
    return dados
```
Note que antes de incluir as linhas da consulta é necessário excluir os dados que podem estar na treeview, possibilitando que possa ser feito consultas suscessivas sem que haja sobreposição de dados. Sempre que for feito uma nova pesquisa, os dados da treeview serão apagados para que os novos dados sejam incluídos.

## Exportando para EXCELL

O arquivo que contém o código e a função para exportar os dados é o `exporta_excell.py` e possui apenas uma função, `exporta_excell`. Esta função é acionada ao clica no botão EXPORTAR presente na interface principal. Ao ser acionada, o primeiro passo é criar uma variável (dado) com os dados fornecidos pela função `gera_sql_geral` que é responsável por executar a consulta no banco de dados com as variáveis fornecidas pelo usuário. Após guardar os dados a função exibe uma telapara o usuário solicitando que o mesmo escolha o local onde será salvo o arquivo xlsx e altere o nome do arquivo. Em seguida, com uso da biblioteca pandas os dados são inseridos no arquivo. Após as informações estrem inseridas, inicia-se uma série de procedimentos de formatação, como alinhamento, alteração da cor dos campos de acordo com o resultado e formatação de alguns campos como DATA e VLTOTAL para que seja possível tratar esses dados como data e valor financeiro dentro do excell. Feito todos esses procedimentos, o arquivo é salvo no local selecionado com o nome escolhido.

Obs: o arquivo com todos esses procedimentos está comentado em cada trecho, sendo possível verificar o que cada parte do código ira executar.

## Exemplos de caso de uso

A aplicação pode ser usada de muitas formas diferentes se for levar em consideração a combinação de variáveis utilizadas. Mas para entendimento da lógica do código descrita anteriormente, será representado dois simples exemplos de uso: utilizando o toplevel e usando apenas os campos entry.

- Fazendo uso do Toplevel:

Ao iniciar a aplicação e se o usuário optar pelo uso dos topleveis, será necessário clicar nesses botões para exibir as respectivas janelas:

![TELA INICIAL](https://github.com/Sipauba/relatorio-setor-compras/blob/main/imagens/inteface_principal_top_destaque.png)

No toplevel filial o usuário poderá selecionar apenas uma filial ou várias dentre as que estão disponíveis. Ao seleciona-las, basta clicar em CONFIRMAR para retornar à interface principal:

![TOPLEVEL FILIAL](https://github.com/Sipauba/relatorio-setor-compras/blob/main/imagens/topleve_filial.png)

Já com os fornecedores o usuário poderá fazer a consulta a partir de um trecho do nome do fornecedor(desde que o termo esteja entre %) ou pesquisar diretamente pelo código. Ao clicar em pesquisar o resultado da pesquisa é exibido com os valores disponíveis para seleção. Depois de selecionar é só clicar em confirmar:

![TOPLEVEL FORNECEDOR](https://github.com/Sipauba/relatorio-setor-compras/blob/main/imagens/toplevel_fornecedor.png)

Com os compradores segue exatamente a mesma lógica do processo para selecionar as filiais:

![TOPLEVEL COMPRADOR](https://github.com/Sipauba/relatorio-setor-compras/blob/main/imagens/toplevel_comprador.png)

Após a inclusão das informações a partir dos respectivos topleveis(note que ao retornar para interface principal, as informações selecionadas ficam dentro dos campos entry, é a partir desses campos que a consulta será realizada), basta preencher os demais filtros de acordo a preferência do usuário e clicar no botão PESQUISAR:

![PESQUISA](https://github.com/Sipauba/relatorio-setor-compras/blob/main/imagens/Interface_principal_preenchida.png)

As informações coletadas na consulta serão exibidas na treeview. Feito isso, basta clicar no botão EXPORTAR para exibir a janela que irá solicitar ao usuário que renomeie o arquivo e escolha onde o mesmo será salvo: 

![EXPORTAR](https://github.com/Sipauba/relatorio-setor-compras/blob/main/imagens/interface_principal_exportar.png)
![EXPORTAR2](https://github.com/Sipauba/relatorio-setor-compras/blob/main/imagens/exportando.png)

Este é o arquivo gerado a partir da consulta:

![EXCELL](https://github.com/Sipauba/relatorio-setor-compras/blob/main/imagens/resultado_excell.png)


- Sem uso do Toplevel:

Este caso de uso é semalhante ao procedimento apresentado anteriormente, porém mais simples e rápido tendo em vista que não será necessário exibir as interfaces secundárias. Este procedimento será realizado caso o usuário tenha preferência por acrescentar os valores diretamente no campo Entry de filiais, compradores e fornecedores. Vale ressaltar que o campo FORNECEDOR não é obrigatório para realizar a consulta.

![INTERFACE](https://github.com/Sipauba/relatorio-setor-compras/blob/main/imagens/Interface_principal_preenchida2.png)

Após preencher os campos, selecionar os demais filtros como datas, tipo de pedido e status do pedido e clicar em PESQUISAR, o resultado será exibido na treeview:

![EXCELL2](https://github.com/Sipauba/relatorio-setor-compras/blob/main/imagens/resultado_excell2.png)

E ao exportar o arquivo como demonstrado anteriormente, será possível obter a planilha como o exemplo abaixo.

##

Importante informar que ambos resultados podem ser obtidos das duas formas sem nenhuma diferença nos dados, desde que os filtros usados para um caso sejam os mesmos usados no outro.

# Conclusão










```bash
  npm run deploy
```

