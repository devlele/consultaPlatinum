import pandas as pd
from PySide6.QtWidgets import QMessageBox

def read_df():
        
    global dataBase_df
    try:
        dataBase_df = pd.read_parquet("teste.parquet") #a função read_parquet le o arquivo parquet e transforma em um data freame
        dataBase_df.columns = ['CPF', 'contaAntiga', 'contaNova', 'limiteClassic', 'limitePlatinum']
    except Exception as e:
        return QMessageBox.information(None, 'Erro', f'Erro inesperado: {e}')
        

    
def search_CPF(cpf):
    if dataBase_df is None:
        return QMessageBox.information(None, 'Erro','Base de dados não carregada.')

    cpf = int(cpf)
        
    required_columns = ['CPF', 'contaAntiga', 'contaNova', 'limiteClassic', 'limitePlatinum'] #Caso o nome da cpluna estiver errado ele retorna esse erro
    for c in required_columns:
        if c not in dataBase_df.columns:
            return QMessageBox.information(None, 'Erro', f'Coluna {c.upper()} não encontrada')
    try:
        client_mask = dataBase_df['CPF'] == cpf #Compara o CPF digitado com todos os valores da coluna CPF e gera uma mascara booleana 
        client_line = dataBase_df.loc[client_mask].iloc[0] #Usa a mascara como filtro e retorna apenas a linha onde aquela mascara é True. .iloc[0] seleciona a primeira linha do resultado
        
        if client_line.empty:
            return QMessageBox.information(None, 'Erro', 'Cliente não encontrado')
        
        old_number = client_line['contaAntiga']
        new_number = client_line['contaNova']
        old_limit = client_line['limiteClassic']
        new_limit = client_line['limitePlatinum']
        return old_number, new_number, old_limit, new_limit
        
    except Exception as e:
        return QMessageBox.information(None, 'Erro', f'Erro ao buscar cliente: {e}')