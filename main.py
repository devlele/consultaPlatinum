import pandas as pd

def read_df():
    dataBase_df = pd.read_excel("Teste.xlsx")

    CPF = dataBase_df['CPF']
    print(CPF)
    

if __name__ == "__main__":
    read_df()