try:
    import PySide.QtGui as gui,time
except:
     import PyQt4.QtGui as gui,time

# Event Mouse 
# Event Close Window 

class Window (gui.QWidget):
	def __init__(self,p=None):
		super(Window,self).__init__(p)
		print(dir(self))
		self.setFixedSize(600,500)
		self.setWindowTitle("Mouse Event")
		vbox = gui.QVBoxLayout(self)
		self.lab  = gui.QLabel();self.lab.setFont(gui.QFont("",15))
		vbox.addWidget(self.lab)

	def mousePressEvent(self, event):
		self.lab.setText("mousePressEvent : "+str(event.pos()))

	def mouseReleaseEvent(self, event):
		self.lab.setText("mouseReleaseEvent : "+str(event.pos()))

	def mouseMoveEvent(self, event):
		self.lab.setText("mouseMoveEvent : "+str(event.pos()))

	def closeEvent(self,event):
		time.sleep(2)
		gui.qApp.quit()

if __name__ == '__main__':
	app = gui.QApplication([])
	win = Window()
	win.show();app.exec_()
