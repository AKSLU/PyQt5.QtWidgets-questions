import sys
from PyQt5.QtWidgets import *


class SimpleEditor(QWidget):
    def __init__(self):  
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 350, 250)
        self.setWindowTitle("Простой тест")

        self.questions = [
            ["5 - 2 = ?", ["1", "3", "2"], 1],
            ["2 - 2 = ?", ["7", "0", "3"], 1],
            ["5 - 3 = ?", ["6", "2", "3"], 1],
        ]

        self.q_index = 0
        self.score = 0

        self.layout = QVBoxLayout()
        self.label = QLabel()
        self.btn1 = QRadioButton()
        self.btn2 = QRadioButton()
        self.btn3 = QRadioButton()
        self.next_btn = QPushButton("Дальше")

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.btn1)
        self.layout.addWidget(self.btn2)
        self.layout.addWidget(self.btn3)
        self.layout.addWidget(self.next_btn)
        self.setLayout(self.layout)

        self.next_btn.clicked.connect(self.next_question)

        self.show_question()

    def show_question(self):
        q = self.questions[self.q_index]
        self.label.setText(q[0])
        self.btn1.setText(q[1][0])
        self.btn2.setText(q[1][1])
        self.btn3.setText(q[1][2])
        self.btn1.setChecked(False)
        self.btn2.setChecked(False)
        self.btn3.setChecked(False)

        if self.q_index == len(self.questions) - 1:
            self.next_btn.setText("Завершить")

    def next_question(self):
        selected = None
        if self.btn1.isChecked():
            selected = 0
        elif self.btn2.isChecked():
            selected = 1
        elif self.btn3.isChecked():
            selected = 2

        if selected is None:
            QMessageBox.warning(self, "Ошибка", "Выберите ответ.")
            return

        correct = self.questions[self.q_index][2]
        if selected == correct:
            self.score += 1

        self.q_index += 1

        if self.q_index < len(self.questions):
            self.show_question()
        else:
            with open("result.txt", "w") as f:
                f.write(f"{self.score}/{len(self.questions)}")

            QMessageBox.information(self, "Готово", f"Ваш результат: {self.score}/{len(self.questions)}")
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimpleEditor()
    window.show()
    sys.exit(app.exec_())

