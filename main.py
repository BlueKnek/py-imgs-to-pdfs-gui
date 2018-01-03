#!/usr/bin/python3

from window import Ui_MainWindow

import sys
import os

from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QRectF, QModelIndex, pyqtSignal

PATH = 'scans'

# https://stackoverflow.com/questions/43126721/pyqt-detect-resizing-in-widget-window-resized-signal/43126946


class Window(QMainWindow):
    resized = pyqtSignal()

    def __init__(self, parent=None):
        super(Window, self).__init__(parent=parent)
        ui = Ui_MainWindow()
        ui.setupUi(self)

    def resizeEvent(self, event):
        self.resized.emit()
        return super(Window, self).resizeEvent(event)


class App():
    def __init__(self, w):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(w)
        self.prepare_ui(w)

    def prepare_ui(self, w):
        self.filenames = os.listdir(PATH)
        self.groups = ['x' for i in range(len(self.filenames))]
        self.last_group = 0
        self.ui.progress.setMaximum(len(self.filenames))
        self.current_i = 0
        self.ui.list.addItems([self.list_filename(i) for i in range(len(self.filenames))])
        self.ui.prev.pressed.connect(self.prev)
        self.ui.next.pressed.connect(self.next)
        self.ui.new_.pressed.connect(self.new)
        self.ui.last.pressed.connect(self.last)
        self.ui.group.textChanged.connect(self.manual)
        self.ui.list.activated.connect(self.move_to_model_index)
        w.resized.connect(self.update_ui)

    def update_ui(self):
        filename = self.filenames[self.current_i]
        self.ui.current.setText(filename)
        self.ui.group.setText(self.groups[self.current_i])
        self.ui.progress.setValue(self.current_i+1)
        # https://stackoverflow.com/questions/2286864/how-can-i-add-a-picture-to-a-qwidget-in-pyqt4
        pixmap = QPixmap(os.path.join(PATH, filename))
        # self.ui.img.setPixmap(pixmap) # to QLabel
        # https://stackoverflow.com/questions/8766584/displayin-an-image-in-a-qgraphicsscene
        scene = QGraphicsScene()
        scene.addPixmap(pixmap)
        w = pixmap.size().width()
        h = pixmap.size().height()
        self.ui.img.setScene(scene)
        self.ui.img.fitInView(QRectF(0, 0, w, h), Qt.KeepAspectRatio)
        self.ui.list.setCurrentItem(self.ui.list.item(self.current_i))

    def prev(self):
        self.current_i = max(0, self.current_i-1)
        self.update_ui()

    def next(self):
        self.current_i = min(len(self.filenames)-1, self.current_i+1)
        self.update_ui()

    def new(self):
        self.last_group += 1
        self.last()

    def last(self):
        self.set_group(self.last_group)
        self.next()

    def manual(self, a):
        self.set_group(a)

    def move_to_model_index(self, model_index):
        self.current_i = model_index.row()
        self.update_ui()

    def set_group(self, group):
        i = self.current_i
        self.groups[i] = str(group)
        self.ui.list.item(i).setText(self.list_filename(i))

    def list_filename(self, i):
        return self.filenames[i] + ' (' + self.groups[i] + ')'

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    a = App(w)
    w.show()
    a.update_ui()
    sys.exit(app.exec_())