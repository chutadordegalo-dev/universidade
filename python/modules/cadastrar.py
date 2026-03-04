from modules.mysql import MySQL
from modules.aluno import Aluno

import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox
)
from PySide6.QtGui import QGuiApplication


class Cadastrar:
    def __init__(self, app):
        self.app = app
        self.janela = QWidget()
        self.layout = QVBoxLayout()
        self.banco = MySQL()

        self.campos = {}

        self.configurar_janela()
        self.criar_componentes()

    def configurar_janela(self):
        self.janela.setWindowTitle("Cadastrar Aluno")

        # 🔹 Redimensiona dinamicamente com base na tela
        tela = QGuiApplication.primaryScreen().availableGeometry()
        largura = int(tela.width() * 0.4)
        altura = int(tela.height() * 0.6)

        self.janela.resize(largura, altura)
        self.janela.setLayout(self.layout)

    def criar_componentes(self):
        componentes = {
            "nome": "Digite seu nome:",
            "email": "Digite seu email:",
            "cpf": "Digite seu CPF:",
            "telefone": "Digite seu telefone:",
            "endereco": "Digite seu endereço:"
        }

        for chave, valor in componentes.items():
            label = QLabel(valor)
            campo = QLineEdit()

            self.layout.addWidget(label)
            self.layout.addWidget(campo)

            self.campos[chave] = campo

        self.botao_Cadastrar = QPushButton("Cadastrar")
        self.layout.addWidget(self.botao_Cadastrar)

        self.botao_Cadastrar.clicked.connect(self.cadastrar)

    # 🔹 MÉTODO DE VALIDAÇÃO
    def validar_campos(self):
        for chave, campo in self.campos.items():
            if not campo.text().strip():
                QMessageBox.warning(
                    self.janela,
                    "Validação",
                    f"O campo '{chave}' é obrigatório."
                )
                campo.setFocus()
                return False

        if "@" not in self.campos["email"].text():
            QMessageBox.warning(
                self.janela,
                "Validação",
                "Email inválido."
            )
            self.campos["email"].setFocus()
            return False

        if not self.campos["cpf"].text().isdigit():
            QMessageBox.warning(
                self.janela,
                "Validação",
                "CPF deve conter apenas números."
            )
            self.campos["cpf"].setFocus()
            return False

        return True

    def cadastrar(self):
        # 🔹 Só continua se a validação passar
        if not self.validar_campos():
            return

        aluno = Aluno(
            self.campos['nome'].text(),
            self.campos['email'].text(),
            self.campos['cpf'].text(),
            self.campos['telefone'].text(),
            self.campos['endereco'].text()
        )

        self.banco.connect()

        try:
            aluno.cadastrar(self.banco)
            QMessageBox.information(self.janela, "Sucesso", "Aluno cadastrado!")
            self.limpar_campos()
        except Exception as e:
            QMessageBox.critical(self.janela, "Erro", f"Erro ao cadastrar: {str(e)}")
        finally:
            self.banco.disconnect()

    def limpar_campos(self):
        for campo in self.campos.values():
            campo.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    tela = Cadastrar()
    tela.janela.show()
   
    sys.exit(tela.app.exec())