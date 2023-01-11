"""fonte:Sistema de cadastro com mysql-Youtube-Eletronica e programação"""
from PyQt5 import uic, QtWidgets
import mysql.connector


def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()
    if formulario.radioButton.isChecked():
        print('Categoria informática foi selecionado')
    elif formulario.radioButton_2.isChecked():
        print('Categoria alimentos foi selecionado')
    elif formulario.radioButton_3.isChecked():
        print('Categoria eletronicos foi selecionado')

    print('Código:', linha1)
    print('Descrição:', linha2)
    print('Preço:', linha3)


app = QtWidgets.QApplication([])
formulario = uic.loadUi('sist_cad_prod/formulario.ui')
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()

# CRIANDO TABELA NO MYSQL console:
""" msql> create table produtos(
          id INT NOT NULL AUTO_INCREMENT,
          codigo INT,
          descricao VARCHAR(50),
          preco DOUBLE,
          categoria VARCHAR(20),
          PRIMARY KEY (id)    
        ); """
# query ok, o rows affected(0.05 sec)

# MOSTRA A TABELA 'produtos' NO MYSQL console:
""" mysql> show tables; """
# 1 row in set(0.02 sec)

# MOSTRA AS CARATERISTICAS DA TABELA 'produtos' NO MYSQL console:
""" mysql> dscribe produtos; """
# 5 rows affected(0.01 sec)

# ANTES DE INSERIR VAMOS MOSTRAR CONEUDO DA TABELA TABELA 'produtos' NO MYSQL console:
""" mysql> select * from produtos; """
# TEM QUE APARACER QUE NÃO TEM NADA CADASTRADO

# INSERINDO REGISTROS OU ITENS NA TABELA produtos NO MYSQL console
""" INSERT INTO produtos(codigo, descricao, preco, categoria) VALUES (123, "impressora", 500.00, "informatica"); """
# 1 row in set(0.00 sec)


