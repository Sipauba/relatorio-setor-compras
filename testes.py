import tkinter as tk

def criar_janela():
    # Criar janela secundária
    janela_secundaria = tk.Toplevel(root)

    # Criar rótulo grande na linha superior que ocupa duas colunas
    rotulo_grande = tk.Label(janela_secundaria, text="Este rótulo ocupa duas colunas", font=('Helvetica', 12))
    rotulo_grande.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

    # Adicionar widgets nas duas colunas abaixo
    rotulo_esquerda = tk.Label(janela_secundaria, text="Coluna Esquerda")
    rotulo_direita = tk.Label(janela_secundaria, text="Coluna Direita")

    rotulo_esquerda.grid(row=1, column=0, pady=10, padx=10)
    rotulo_direita.grid(row=1, column=1, pady=10, padx=10)

# Criar a janela principal
root = tk.Tk()
root.title("Exemplo de columnspan")

# Criar rótulo grande que ocupa duas colunas na linha superior
rotulo_grande = tk.Label(root, text="Este rótulo ocupa duas colunas", font=('Helvetica', 14))
rotulo_grande.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

# Criar botão que chama a função para criar a janela secundária
botao = tk.Button(root, text="Criar Janela", command=criar_janela)
botao.grid(row=1, column=0, pady=10, padx=10)

# Iniciar o loop principal
root.mainloop()
