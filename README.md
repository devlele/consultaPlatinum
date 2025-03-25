# **Consulta VIP - Pesquisa da Conta de Origem v1.0**  
A aplicação **Consulta VIP** foi desenvolvida para auxiliar operadores da central de relacionamento VIP. Através da pesquisa de um **CPF**, o operador pode obter informações como o número da conta antiga do cliente, o número da conta nova, além dos limites dessas contas e a diferença entre eles.  

## Tecnologias  
O desenvolvimento foi feito utilizando a linguagem **Python** e algumas de suas bibliotecas:  

- **PySide6**: Utilizada para desenvolver a **interface gráfica do usuário (GUI)**.  
- **Pandas**: Utilizada para a **manipulação da base de dados**.  

## Base de Dados  
Inicialmente, a base de dados é recebida em formato **Excel (.xlsx)**. Utilizamos um **conversor** para transformá-la em um arquivo **.parquet**. Dentro da aplicação, há uma função que utiliza a biblioteca **Pandas** para ler esse arquivo e convertê-lo em um **DataFrame**. Em seguida, manipulamos os dados para extrair e apresentar as informações necessárias. 
Para a aplicação funcionar da forma correta o arquivo da base de dados deve estar salvo dentro da pasta como **UPSELL.parquet**.

## Como Compilar

### Pré-requisitos
- Python 3.x instalado
- Biblioteca `pyinstaller` (se ainda não tiver, instale com `pip install pyinstaller`)

### Compilação
Para gerar o executável, execute o seguinte comando no terminal:

```sh
pyinstaller --onefile --name ConsultaPlatinum main.py
```

## Autoria  
Projeto desenvolvido por **Alefe Freitas**.  
