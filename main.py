import pandas as pd

def read_df():
    try:
        #dataBase_df = pd.read_excel("Teste.xlsx") #a função read_excel le o excel e transforma em um data freame
        #dataBase_df.to_parquet("teste.parquet")
        dataBase_df = pd.read_parquet("teste.parquet")#a função read_parquet le o arquivo parquet e transforma em um data freame
        print(dataBase_df['CPF'])
        print("Arquivo lido e convertido com sucesso!")
    except Exception as e:
        print(f"Erro inesperado: {e}")

    

    
    

if __name__ == "__main__":
    read_df()