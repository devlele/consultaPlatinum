from PySide6.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QFrame, QTextEdit, QMessageBox
from PySide6.QtCore import Qt
import functions
import locale

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Conta origem')
        self.setGeometry(1000, 100, 465, 280)
        self.setStyleSheet('background-color: #292929')

        #Criação dos Widgets
        self.label_cpf = QLabel('Digite o CPF:', self)
        self.label_origem = QLabel('Conta Origem', self)
        self.label_platinum = QLabel('Conta Platinum', self)
        self.label_limit_orig = QLabel('Limite', self)
        self.label_limit_plat = QLabel('Limite', self)
        self.label_dif = QLabel('Diferença entre limites', self)
        self.button_search = QPushButton('Pesquisar', self)
        self.button_clear = QPushButton('Limpar', self)
        self.input_cpf = QLineEdit(self)
        self.output_origem = QTextEdit(self)
        self.output_platinum = QTextEdit(self)
        self.output_limit_ori = QTextEdit(self)
        self.output_limit_plat = QTextEdit(self)
        self.output_dif = QTextEdit(self)
        self.line = QFrame(self)
        
        
        #Estilização
        self.label_cpf.setStyleSheet('color: white; font-size: 16px')
        self.label_cpf.move(47, 5)# move define a posição
        self.label_cpf.resize(92, 30)#rezise define o tamanho

        self.label_origem.setStyleSheet('Color: white; font-size: 14px')
        self.label_origem.move(47, 107)
        self.label_origem.resize(86, 18)
        
        self.label_platinum.setStyleSheet('color: white; font-size: 14px')
        self.label_platinum.move(47, 159)
        self.label_platinum.resize(98, 18)

        self.label_limit_orig.setStyleSheet('Color: white; font-size: 14px')
        self.label_limit_orig.move(269, 107)
        self.label_limit_orig.resize(40, 18)
        
        self.label_limit_plat.setStyleSheet('Color: white; font-size: 14px')
        self.label_limit_plat.move(269, 159)
        self.label_limit_plat.resize(40, 18)

        self.label_dif.setStyleSheet('color: white; font-size: 14px')
        self.label_dif.move(269, 215)
        self.label_dif.resize(140, 18)

        self.button_search.setStyleSheet('background-color: #00C6CC; color: #ffffff; font-size: 16px; border-radius: 5px; text-align: center')
        self.button_search.move(47, 62)
        self.button_search.resize(175, 20)
        self.button_search.setCursor(Qt.PointingHandCursor)
        
        self.button_clear.setStyleSheet('background-color: #D3FF00; color: #000000; font-size: 16px; border-radius: 5px; text-align: center')
        self.button_clear.move(242, 62)
        self.button_clear.resize(175, 20)
        self.button_clear.setCursor(Qt.PointingHandCursor)

        self.input_cpf.setStyleSheet('background-color: #D9D9D9; color: #000000; font-size: 14px; border-radius: 5px')
        self.input_cpf.move(47, 33)
        self.input_cpf.resize(370, 20)

        self.output_origem.setStyleSheet('background-color: #D9D9D9; color: #000000; font-size: 14px; border-radius: 5px')
        self.output_origem.move(47, 129)
        self.output_origem.resize(207, 20)

        self.output_platinum.setStyleSheet('background-color: #D9D9D9; color: #000000; font-size: 14px; border-radius: 5px')
        self.output_platinum.move(47, 180)
        self.output_platinum.resize(207, 20)

        self.output_limit_ori.setStyleSheet('background-color: #D9D9D9; color: #000000; font-size: 14px; border-radius: 5px')
        self.output_limit_ori.move(269, 129)
        self.output_limit_ori.resize(149, 20)

        self.output_limit_plat.setStyleSheet('background-color: #D9D9D9; color: #000000; font-size: 14px; border-radius: 5px')
        self.output_limit_plat.move(269, 180)
        self.output_limit_plat.resize(149, 20)

        self.output_dif.setStyleSheet('background-color: #D9D9D9; color: #000000; font-size: 14px; border-radius: 5px')
        self.output_dif.move(269, 236)
        self.output_dif.resize(149, 20) 

        #definição da linha que separa a interface
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setStyleSheet('background-color: white')
        self.line.setGeometry(46, 98, 372, 1) 

        #funcionalidade dos botões
        self.button_search.clicked.connect(self.search) #conexão do evento de clique do botão com a função de busca do CPF
        self.button_clear.clicked.connect(self.clear_results)

    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8') #Define o padrão númerico para o padrao do brasil
    #Deixa o valor no padrão númerioco correto
    def format_number(self, limit):
        return locale.format_string('%.2f', limit, grouping=True)

    #Função que faz a busca do cpf
    def search(self):
        cpf = self.input_cpf.text().strip()
        
        if not cpf.isdigit():
            return QMessageBox.information(None, 'Erro','CPF inválido.')

        functions.read_df()
        result = functions.search_CPF(int(cpf)) #armazena o resultado da função de pesquisa do cpf

        #pega os resultados e aloca nos labals certo
        if result:
            old_number, new_number, old_limit, new_limit = result
            self.output_origem.setText(str(old_number))
            self.output_platinum.setText(str(new_number))
            self.output_limit_ori.setText(self.format_number(old_limit))
            self.output_limit_plat.setText(self.format_number(new_limit))
            dif = new_limit - old_limit
            self.output_dif.setText(self.format_number(dif))
   
    #função para limpar a interace
    def clear_results(self):
        self.input_cpf.clear()
        self.output_origem.clear()
        self.output_platinum.clear()
        self.output_limit_ori.clear()
        self.output_limit_plat.clear()
        self.output_dif.clear()

        
    
