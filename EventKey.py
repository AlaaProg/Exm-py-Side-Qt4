try:
    import PySide.QtGui as gui,time
except:
     import PyQt4.QtGui as gui,time

# Event Key

class Window (gui.QWidget):
	def __init__(self,p=None):
		super(Window,self).__init__(p)
		self.setFixedSize(600,500)
		self.setWindowTitle("KeyEvent")
		vbox = gui.QVBoxLayout(self)
		self.release  = gui.QLabel();self.release.setFont(gui.QFont("",15))
		self.press  = gui.QLabel();self.press.setFont(gui.QFont("",15))
		vbox.addWidget(self.release)
		vbox.addWidget(self.press)

	def keyReleaseEvent(self,event):
		self.release.setText("keyReleaseEvent :"+str(event.key())+"  "+event.text())

	def keyPressEvent(self,event):
		self.press.setText("keyPressEvent :"+str(event.key())+"  "+event.text())

if __name__ == '__main__':
	app = gui.QApplication([])
	win = Window()
	win.show();app.exec_()
