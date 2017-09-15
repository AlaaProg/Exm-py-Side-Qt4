#Alaa Prog ^_^
#Exmple: PySide or PyQt4
# 
try:
	from PySide.QtGui import (QWidget,QApplication,QHBoxLayout,QVBoxLayout,
								QPushButton,QTableWidget,QLabel,QTableWidgetItem,
								QDialog,QTextEdit,qApp)
	from PySide.QtWebKit import QWebView
except:
	from PyQt4.QtGui import (QWidget,QApplication,QHBoxLayout,QVBoxLayout,
							QPushButton,QTableWidget,QLabel,QTableWidgetItem,
							QDialog,QTextEdit,qApp)
	from PyQt4.QtWebKit import QWebView

class Main(QWidget):
	def __init__(self):
		super(Main,self).__init__()
		self.setFixedSize(630,350)

		self.setWindowTitle("Exm with css")


		hbox_Main = QHBoxLayout(self)
		vbox_vb   = QVBoxLayout()
		hbox_but  = QHBoxLayout()

		self.table = table()
		self.view  = view()

		show  = QPushButton("Show Code")
		exit_   = QPushButton("Exit");exit_.clicked.connect(qApp.quit)

		hbox_but.addWidget(show )
		hbox_but.addWidget(exit_)

		vbox_vb.addWidget(self.view)
		vbox_vb.addLayout(hbox_but)

		hbox_Main.addLayout(vbox_vb)
		hbox_Main.addWidget(self.table)

		show.clicked.connect(self.view.showCode)
		self.table.itemChanged.connect(self.print_attrub)
	def print_attrub(self,item):	
		css = "%s : %s ;\n"%(self.table.cellWidget(item.row(),0).text(),item.text())
		self.view.set_(css)



class view(QWebView):
	def __init__(self):
		super(view,self).__init__()
		self.setMaximumWidth(320)
		self.css = ""
		self.html = '''
			<body style="background-color:#eee;">
			<style type="text/css">
				.button{
					%s
				}
			</style>
			<center style="margin-top: 100px">

				<input class="button" type="button" name="button" value="button" />

			</center>
			</body>
			'''
		self.setHtml(self.html)
	def set_(self,css):
		css_t = "";add_ = False
		for i in self.css.split("\n"):
			if i.strip() != "":
				if i.split(":")[0].strip() == css.split(":")[0].strip():
					add_ = True
					if css.split(":")[1].strip() != "":
						css_t += "\t"+i.split(":")[0].strip()+":"+css.split(":")[1].strip()+"\n"
				else:
					css_t += "\t"+i.strip()+"\n"
		if not add_:
			css_t += "\t"+css.strip()+"\n"
		self.css = css_t

		self.setHtml(self.html%self.css)

	def showCode(self):
		style = ".button {\n%s\n}"
		text  = QTextEdit()
		dial  = QDialog(self);dial.setWindowTitle("Button")
		vbox  = QVBoxLayout(dial) 
		vbox.addWidget(text)
		text.setPlainText(style%self.css)	
		dial.show()	

class table(QTableWidget):
	def __init__(self):
		super(table,self).__init__()
		
		self.verticalHeader().setHidden(True)
		self.horizontalHeader().setHidden(True)
		self.setColumnCount(2)
		
		self.attribute()
		self.setSize()

	def attribute(self):
		attrib  = (
			"font-style","font-family","font-size","font-weight",
			"color","background-color","width","height","text-align",
			'border-style','border-width',"border-color",
			'border-bottom-style','border-bottom-width',"border-bottom-color",
			'border-right-style','border-right-width',"border-right-color",
			'border-top-style','border-top-width',"border-top-color",
			'border-left-style','border-left-width',"border-left-color",
		)
		self.setStyleSheet("QLabel{font:bold;}")
		self.setRowCount(len(attrib));count_row = 0
		for row in range(len(attrib)):
			self.setCellWidget(count_row,0,QLabel(" "*2+attrib[row]));
			self.setItem(count_row,1,QTableWidgetItem(""))
			count_row+=1

	def setSize(self):
		self.setColumnWidth(0,130);self.setColumnWidth(1,133);
		for row in range(self.rowCount()):
			self.setRowHeight(row,25)


if __name__ == '__main__':
	prog = QApplication([])
	win = Main()
	win.show()
	prog.exec_()
