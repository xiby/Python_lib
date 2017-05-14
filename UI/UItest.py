import sys
from PyQt5.QtWidgets import QApplication,QWidget
import pySC.dataBase
import tmpUI
if __name__=='__main__':
    app=QApplication(sys.argv)
    w=QWidget()
    ui=tmpUI.Ui_Form()
    
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())