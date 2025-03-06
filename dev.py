import pandas as pd

try:
    #dataBase_df = pd.read_excel("Teste.xlsx") #a função read_excel le o excel e transforma em um data freame
    #dataBase_df.to_parquet("teste.parquet")
    global dataBase_df
    dataBase_df = pd.read_parquet("teste.parquet") #a função read_parquet le o arquivo parquet e transforma em um data freame
    dataBase_df.columns = ["CPF", "contaAntiga", "contaNova"]
    print("Arquivo lido e convertido com sucesso!")
except Exception as e:
        print(f"Erro inesperado: {e}")



#Inicio da função de pesquisa do cpf

cpf = input("Informe o CPF: ").strip()
try:
    cpf = int("".join(filter(str.isdigit, cpf))) #Esse comando é um tratamento de erro, caso o cpf tenha pontos e traços ele filtra dexando apenas valores numericos 
except:
     print('CPF inválido')
    
required_columns = ['CPF', 'contaAntiga', 'contaNova']
for c in required_columns:
    if c not in dataBase_df.columns:
         print(f'Coluna {c.upper()} não encontrada')
try:
    client_mask = dataBase_df['CPF'] == cpf #Compara o CPF digitado com todos os valores da coluna CPF e gera uma mascara booleana 
    result = dataBase_df.loc[client_mask].iloc[0] #Usa a mascara como filtro e retorna apenas a linha onde aquela mascara é True. .iloc[0] seleciona a primeira linha do resultado
    conta_antiga = result['contaAntiga']
    conta_nova = result['contaNova']
    print(conta_antiga, conta_nova)
except:
    print('Cliente não encontrado')