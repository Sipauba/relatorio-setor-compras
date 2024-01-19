import tkinter as tk
from tkinter import filedialog

def exporta_excell():
    # Obtenha os dados
    #dado = gera_sql_geral()

    # Crie uma janela Tkinter para selecionar o diretório
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal

    # Solicite ao usuário que selecione o diretório de destino
    output_directory = filedialog.askdirectory(title="Selecione o diretório para salvar a planilha Excel")

    if not output_directory:
        print("Operação cancelada pelo usuário.")
        return

    # Construa o caminho completo para o arquivo de saída
    output_file = filedialog.asksaveasfilename(
        title="Escolha o nome do arquivo Excel",
        initialdir=output_directory,
        defaultextension=".xlsx",
        filetypes=[("Planilha Excel", "*.xlsx")]
    )

    if not output_file:
        print("Operação cancelada pelo usuário.")
        return

    # Restante do código para processar e salvar a planilha
    # Certifique-se de usar o caminho completo para o arquivo de saída
    # ...

    print(f"Consulta concluída com sucesso. Resultados salvos em {output_file}")

# Chame a função
exporta_excell()
