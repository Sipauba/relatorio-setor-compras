from tkinter import ttk

def treeview(root) : 

    # Define a quantidade de colunas
    tree = ttk.Treeview(root, columns=('coluna1','coluna2','coluna3','coluna4','coluna5','coluna6','coluna7','coluna8','coluna9','coluna10'))

    # Centraliza o conteúdo de todas as colunas
    for coluna in ('coluna1','coluna2','coluna3','coluna4','coluna5','coluna6','coluna7','coluna8','coluna9','coluna10'):
        tree.column(coluna, anchor = 'center')
        
    # Nomeia o cabeçalho das colunas
    tree.heading('coluna1', text = 'DTEMISSÃO')
    tree.heading('coluna2', text = 'FILIAL')
    tree.heading('coluna3', text = 'NºPEDIDO')
    tree.heading('coluna4', text = 'CODFORNEC')
    tree.heading('coluna5', text = 'FORNEC')
    tree.heading('coluna6', text = 'COMPRADOR')
    tree.heading('coluna7', text = 'VLPEDIDO')
    tree.heading('coluna8', text = 'TIPO')
    tree.heading('coluna9', text = 'SITUAÇÃO')
    tree.heading('coluna10', text = 'NF')

    # Define uma largura padrão para cada coluna
    tree.column('coluna1', width = 60)
    tree.column('coluna2', width = 60)
    tree.column('coluna3', width = 60)
    tree.column('coluna4', width = 60)
    tree.column('coluna5', width = 60)
    tree.column('coluna6', width = 60)
    tree.column('coluna7', width = 60)
    tree.column('coluna8', width = 60)
    tree.column('coluna9', width = 60)
    tree.column('coluna10', width = 60)

    # Essa linha abaixo esconde a primeira coluna obrigatória do tkinter
    tree.column('#0', width = 0)

    # Define a posição e as dimenções da TreeView
    tree.place(x = 40, y = 180, width = 710, height = 270)
    
    def monta_tree(tree, dados):
        for item in tree.get_children():
            tree.delete(item)
            
        for row in dados:
            tree.insert('','end', values=row)

#from variaveis import consulta_geral_sql        
def atualiza_tree(tree, dados):
    for item in tree.get_children():
        tree.delete(item)

    # Preencher a Treeview com os dados
    for row in dados:
        tree.insert('', 'end', values=row)