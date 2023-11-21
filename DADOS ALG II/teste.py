import pandas as pd
import numpy as np

def Selecionar(arquivo):
    coluna_obrigatoria = 'Nome_Inteiro'

    df_existente = pd.read_csv(arquivo, delimiter=',', encoding='utf-8')

    print("Colunas disponíveis:")
    for coluna in df_existente.columns:
        print(coluna)

    Coluna_Requerida = input("Escolha uma das colunas existentes: ")

    if Coluna_Requerida not in df_existente.columns:
        print("Coluna inválida.")
        return

    if coluna_obrigatoria not in df_existente.columns:
        print("Coluna obrigatória não encontrada.")
        return

    Colunas_Uso = df_existente[[coluna_obrigatoria, Coluna_Requerida]]  
    DF_CSV_SEPARADO = pd.DataFrame(Colunas_Uso)
    Nomeacao = input("Informe o nome para o arquivo: ")
    DF_CSV_SEPARADO.to_csv(f"{Nomeacao}.csv", index=False)

    print("Arquivo gerado com sucesso!")
    
def gerar_relatorio(arquivo):
    df_existente = pd.read_csv(arquivo, delimiter=',', encoding='utf-8')
    numero_linhas = len(df_existente)
    nomes_colunas = ", ".join(df_existente.columns.to_list())
    
    relatorio_df = pd.DataFrame({
        'Informacao': ['Número de linhas', 'Nomes das colunas'],
        'Valor': [numero_linhas, nomes_colunas]
    })

    Nomeação = input("Informe o nome para o arquivo: ")
    relatorio_df.to_csv(f"{Nomeação}.csv", index=False)

def Gerar_Resumo(arquivo):
    df = pd.read_csv(arquivo, delimiter=',', encoding='utf-8')
    colunas_numericas = df.select_dtypes(include=[np.float64, np.int64]).columns.tolist()
    
    if not colunas_numericas:
        print("Não foram encontradas colunas numéricas no arquivo.")
        return
    
    df_RS = pd.DataFrame(df[colunas_numericas].sum(), columns=['Soma']).reset_index()
    df_RS.columns = ['Coluna', 'Soma']
    Nomeação = input("Informe o nome para o arquivo: ")
    df_RS.to_csv(f"{Nomeação}.csv", index=False)

    print("O arquivo foi criado com exito!")
    
def Estats(arquivo):
    df_estatisticas = pd.read_csv(arquivo, delimiter=',', encoding='utf-8')
    estatisticas = df_estatisticas.describe()
    print("Estatisticas:")
    print(estatisticas)

def Tela(Menu):
    while Menu == 1:
        if Menu == 1: 
            Menu = int(input('1 para ver o relatório\n2 para ver o resumo geral\n3 para ver as estastisticas\n4 para ver as colunas disponiveis e selecionar:'))
            if Menu == 1:
                arquivo = 'DADOSCOD.csv'
                gerar_relatorio(arquivo)
                Menu = int(input("Se deseja continuar digite 1 caso não digite 0 \n"))
            elif Menu == 2:
                arquivo = 'DADOSCOD.csv'
                Gerar_Resumo(arquivo)
                Menu = int(input("Se deseja continuar digite 1 caso não digite 0 \n"))
            elif Menu == 3:
                arquivo = 'DADOSCOD.csv'
                Estats(arquivo)
                Menu = int(input("Se deseja continuar digite 1 caso não digite 0 \n"))
            elif Menu == 4:
                arquivo = 'DADOSCOD.csv'
                Selecionar(arquivo)
                Menu = int(input("Se deseja continuar digite 1 caso não digite 0 \n"))
    print('OBG por usar nosso sistema ;)')

print("Bem-vindo ao sistema de Informações dos Jogadores de seasson 2019 da Premier league a liga mais competitiva do mundo!")
Menu = int(input('Digite 1 (um) para começar ou 0 (zero) para encerrar: '))
Tela(Menu)