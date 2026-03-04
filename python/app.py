from PySide6.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QPushButton,
    QWidget
)

from screen.cadastrar import Cadastrar
from screen.listar import Listar

import sys

class App:
    def aplicar_estilo(self):
        self.janela.setStyleSheet("""
        QWidget {
            background-color: #0f172a;
            font-family: Arial;
            color: white;
        }

        QPushButton {
            background-color: #1e293b;
            border: 2px solid #334155;
            border-radius: 12px;
            padding: 15px;
            font-size: 16px;
            font-weight: bold;
            margin: 10px 40px;
        }

        QPushButton:hover {
            background-color: #2563eb;
            border: 2px solid #2563eb;
        }

        QPushButton:pressed {
            background-color: #1e40af;
        }
    """)
    def __init__(self):
        self.app = QApplication(sys.argv)
        
        self.janela = QWidget()
        self.layout = QVBoxLayout()
        
        self.janela.setWindowTitle("Sistema Universidade")
        self.janela.resize(400, 200)
        self.janela.setLayout(self.layout)
        
        self.criar_botoes()
        self.aplicar_estilo()
        
        self.janela.show()

    def criar_botoes(self):
        botao_listar = QPushButton("Listar")
        self.layout.addWidget(botao_listar)
        botao_listar.clicked.connect(self.abrir_listagem)
        
        botao_cadastrar = QPushButton("Cadastrar")
        self.layout.addWidget(botao_cadastrar)
        botao_cadastrar.clicked.connect(self.abrir_cadastro)
        
    def abrir_listagem(self):
        self.tela_listagem = Listar(self.app)
        self.tela_listagem.janela.show()
        
    def abrir_cadastro(self):
        self.tela_cadastro = Cadastrar(self.app)
        self.tela_cadastro.janela.show()

if __name__ == "__main__":
    system = App()
    sys.exit(system.app.exec())