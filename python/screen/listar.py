from modules.mysql import MySQL
from modules.aluno import Aluno

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView
)

from PySide6.QtCore import Qt


class Listar:

    def __init__(self, app):
        self.app = app
        self.janela = QWidget()
        self.layout = QVBoxLayout()
        self.banco = MySQL()

        self.configurar_janela()
        self.criar_componentes()
        self.carregar_dados()

    def configurar_janela(self):
        self.janela.setWindowTitle("📋 Listagem de Alunos")

        screen = self.app.primaryScreen().geometry()
        largura = int(screen.width() * 0.6)
        altura = int(screen.height() * 0.7)

        self.janela.resize(largura, altura)
        self.janela.setLayout(self.layout)

        self.janela.setStyleSheet("""
        QWidget {
            background-color: #111827;
            font-family: Arial;
            font-size: 14px;
            color: white;
        }
        """)

    def criar_componentes(self):

        self.tabela = QTableWidget()
        self.tabela.setColumnCount(6)
        self.tabela.setHorizontalHeaderLabels(
            ["ID", "Nome", "Email", "CPF", "Telefone", "Matrícula"]
        )

        self.tabela.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.tabela.setStyleSheet("""
        QTableWidget {
            background-color: #1f2937;
            border-radius: 8px;
            gridline-color: #374151;
            color: white;
        }

        QHeaderView::section {
            background-color: #7c3aed;
            color: white;
            padding: 8px;
            border: none;
            font-weight: bold;
        }

        QTableWidget::item {
            padding: 6px;
        }

        QTableWidget::item:selected {
            background-color: #8b5cf6;
            color: white;
        }
        """)

        self.layout.addWidget(self.tabela)

        self.botao_atualizar = QPushButton("🔄 Atualizar")
        self.botao_atualizar.setCursor(Qt.PointingHandCursor)

        self.botao_atualizar.setStyleSheet("""
        QPushButton {
            background-color: #7c3aed;
            color: white;
            border-radius: 8px;
            padding: 10px;
            font-weight: bold;
        }

        QPushButton:hover {
            background-color: #6d28d9;
        }

        QPushButton:pressed {
            background-color: #5b21b6;
        }
        """)

        self.layout.addWidget(self.botao_atualizar)

        self.botao_atualizar.clicked.connect(self.carregar_dados)

    def carregar_dados(self):

        self.banco.connect()
        alunos = Aluno.listar(self.banco)
        self.banco.disconnect()

        self.tabela.setRowCount(len(alunos))

        for linha, aluno in enumerate(alunos):

            self.tabela.setItem(linha, 0, QTableWidgetItem(str(aluno["id"])))
            self.tabela.setItem(linha, 1, QTableWidgetItem(aluno["nome"]))
            self.tabela.setItem(linha, 2, QTableWidgetItem(aluno["email"]))
            self.tabela.setItem(linha, 3, QTableWidgetItem(aluno["cpf"]))
            self.tabela.setItem(linha, 4, QTableWidgetItem(aluno["telefone"]))

            matricula = "Ativo" if aluno["matricula"] else "Inativo"
            self.tabela.setItem(linha, 5, QTableWidgetItem(matricula))