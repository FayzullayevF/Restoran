import os
os.system("clear")
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox

class MyRestoran(QWidget):
    def __init__(self):
        super().__init__()
        
        self.v_main_lay = QVBoxLayout()
        self.v1_main_lay = QVBoxLayout()

        self.h_lbl_lay = QVBoxLayout()
        self.h_btn_lay = QHBoxLayout()
        
        self.lbl_btn = QLabel("Restoranimizga xush kelibsiz 🤗 ")
        self.lbl_btn.setStyleSheet("background-color: white; color: lightblue; font-size: 30px")
        
        self.lbl1_btn = QLabel("Ovqatlarimiz 🍵 ") 
        self.lbl1_btn.setStyleSheet("color:coral; font-size: 25px") 
        
        self.lbl2_btn = QLabel("Salatlarimiz 🥗 ") 
        self.lbl2_btn.setStyleSheet("color:lightblue; font-size: 25px") 
        
        self.lbl3_btn = QLabel("Ovqatlarimiz") 
        self.lbl_btn.setStyleSheet("color:lightblue; font-size: 25px") 
        
        self.lbl3_btn = QLabel("Xaridingiz uchun tashakkur 😊 ")
        self.lbl3_btn.setStyleSheet("color: coral; font-size: 30px")
        
        
        
        self.o1 = QCheckBox("Osh       ->    $20000")
        self.o2 = QCheckBox("Mastava   ->    $12000")
        self.o3 = QCheckBox("Chuchvara ->    $12000")
        self.o4 = QCheckBox("Manti     ->    $6000")
        self.o5 = QCheckBox("Norin     ->    $15000")
        self.o6 = QCheckBox("Asarti    ->    $53000")
        self.o7 = QCheckBox("Mol-jaz   ->    $17000")
        self.o8 = QCheckBox("Qo'y-jaz  ->    $19000")
        self.o9 = QCheckBox("Qiyma     ->    $16000")
        self.lst = [self.o1,self.o2,self.o3,self.o4,self.o5,self.o6,self.o7,self.o8,self.o9]
        
        
        self.s1 = QCheckBox("Mujiskoy kapriz ->    $20000")
        self.s2 = QCheckBox("Achiq-chuchuk   ->    $12000")
        self.s3 = QCheckBox("Pintuza         ->    $12000")
        self.s4 = QCheckBox("Alivia          ->    $6000")
        self.s5 = QCheckBox("Chimchi         ->    $15000")
        self.s6 = QCheckBox("Maynez          ->    $53000")
        self.s7 = QCheckBox("Soup            ->    $17000")
        self.lst1 = [self.s1,self.s2,self.s3,self.s4,self.s5,self.s6,self.s7]
        
        self.submit_btn = QPushButton("SUBMIT")
        self.submit_btn.clicked.connect(self.Submit)
        
        self.next_btn = QPushButton("NEXT")
        self.next_btn.clicked.connect(self.Next)
        
        self.buy_btn = QPushButton("BUY")
        self.buy_btn.clicked.connect(self.Buy)
        
        self.ok_btn = QPushButton("OK")
        self.ok_btn.clicked.connect(self.Ok)
        
        self.msg = QMessageBox()
        self.msg.setWindowTitle("Salom")
        self.msg.setText("Xaridingiz uchun tashakkur 😊 ")
        self.msg.buttonClicked.connect(self.Msg)
        self.msg.exec_()
        
        self.h_lbl_lay.addStretch()
        self.h_lbl_lay.addWidget(self.lbl_btn)
        self.h_lbl_lay.addStretch()
        self.v_main_lay.addLayout(self.h_lbl_lay)
        self.h_lbl_lay.addStretch()
        self.h_lbl_lay.addWidget(self.lbl1_btn)
        self.h_lbl_lay.addStretch()
        self.v_main_lay.addLayout(self.h_lbl_lay)
        for i in self.lst:
            i.setStyleSheet("background-color: lightblue; color: black; font-size: 15px")
            self.v_main_lay.addWidget(i)
        
        self.h_btn_lay.addWidget(self.submit_btn)
        self.h_btn_lay.addWidget(self.next_btn)
        self.v_main_lay.addLayout(self.h_btn_lay)
        
        self.setLayout(self.v_main_lay)
        
        
    def Submit(self):
        self.next_btn.hide()
        self.submit_btn.hide()
        self.lbl1_btn.hide()
        
        sum = 0
        for i in self.lst:
            if i.isChecked():
                sum += int(i.text().split('$')[-1])
            else:
                i.hide()
            self.lbl_btn.setText(f"TOTAL: ${sum}")
        self.h_btn_lay.addWidget(self.buy_btn)
        self.v_main_lay.addLayout(self.h_btn_lay)
        self.setLayout(self.v_main_lay)
        
        
    def Msg(self):
        if self.ok_btn:
           self.msg.setStyleSheet("color: black")
           self.msg.exec_()
    def Ok(self):
        self.Msg()
        app.exit()
    

    def Buy(self):
        self.lbl_btn.hide()
        self.buy_btn.hide
        self.buy_btn.hide()
        self.ok_btn.show()
        self.h_btn_lay.addWidget(self.ok_btn)
        self.v_main_lay.addLayout(self.h_btn_lay)
        self.Ok()

    def Next(self):
        self.o1.hide()
        self.o2.hide()
        self.o3.hide()
        self.o4.hide()
        self.o5.hide()
        self.o6.hide()
        self.o7.hide()
        self.o8.hide()
        self.o9.hide()
        self.submit_btn.hide()
        self.lbl_btn.hide()
        self.lbl1_btn.hide()
        self.next_btn.hide()
        self.h_lbl_lay.addStretch()
        self.h_lbl_lay.addWidget(self.lbl2_btn)
        self.h_lbl_lay.addStretch()
        for j in self.lst1:
            j.setStyleSheet("background-color: lightblue; color: black; font-size: 15px")
            print("Salat")
            self.h_lbl_lay.addWidget(j)
        self.setLayout(self.v1_main_lay)

        sum = 0
        for j in self.lst1:
            if j.isChecked():
                sum += int(j.text().split('$')[-1])
            else:
                j.hide()
        self.lbl3_btn.setText(f"TOTAL: ${sum}")
        self.h_btn_lay.addWidget(self.buy_btn)
        self.v1_main_lay.addLayout(self.h_btn_lay)
        self.setLayout(self.v1_main_lay)
        self.Submit()
    
app = QApplication([])
win = MyRestoran()
win.show()
app.exec_()