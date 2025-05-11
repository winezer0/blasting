import sys
from PyQt6.QtWidgets import QMainWindow
import asyncio
from PyQt6 import QtWidgets
import qasync

# 这里是自己写的库
from PyUi.Uilist import settings


class Ui_MainWindow(object):

    @staticmethod
    def set_text_ui(windows):
        settings.ui_set(windows, loop)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    loop = qasync.QEventLoop(app)
    asyncio.set_event_loop(loop)
    main_windows = QMainWindow()
    with loop:
        ui = Ui_MainWindow()
        ui.set_text_ui(main_windows)
        main_windows.show()
        loop.run_forever()
