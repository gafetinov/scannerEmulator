import sys
import pyautogui
import time
from views import design
from PyQt5 import QtWidgets


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.scanButton.clicked.connect(self._scan)

    def _scan(self):
        codes = self.codesList.toPlainText().split('\n')
        time.sleep(2)
        for code in codes:
            print(code)
            pyautogui.write(code)
            pyautogui.keyDown('enter')
            pyautogui.keyUp('enter')
            time.sleep(0.8)


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
