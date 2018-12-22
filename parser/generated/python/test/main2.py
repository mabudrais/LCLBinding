from ctypes import *
from Application import *
from MainPasObject import *
from Forms import *
from StdCtrls import *
from Grids import *
class Form1(TForm):
    Button1=TButton()
    Edit1=TEdit()
    StringGrid1=TStringGrid()
    def Button1Click(self,Sender):
        #F=GetPytonObject(sender)
        print (Sender.Top)
        print (Sender.Caption)
        print self.StringGrid1.getCells(1,1)
    def OnButton1Click(self,Sender):
        Sender.Top=Sender.Top+1

    def OnMouseMove2(self,Sender,i,i2,i3):
        print (i,i2,i3)
        print(Sender.Left)
        print(CreateSetFormint(i,{1:"ssShift",2:"ssAlt", 4:"ssCtrl",8:"ssLeft", 5:"ssRight", 6:"ssMiddle", 7:"ssDouble",8:"ssMeta",9:"ssSuper", 10:"ssHyper", 11:"ssAltGr", 12:"ssCaps", 13:"ssNum",14:"ssScroll",15:"ssTriple",16:"ssQuad",17:"ssExtra1",18:"ssExtra2"}))
        #F=GetPytonObject(sender,TObject)

F2=Form1()    
Application_Initialize()
#F=Application_CreateForm()
F1=Forms_Application_CreateFormLFM(Form1,"TForm1")

Application_Run()
