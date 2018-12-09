from ctypes import *
from Application import *
from MainPasObject import *
from stdctrls import *
class Form1:
    def OnClickH(self,Sender):
        #F=GetPytonObject(sender)
        print (Sender.Top)
        print (Sender.Caption)
    
    def OnButton1Click(self,Sender):
        Sender.Top=Sender.Top+1

    def OnMouseMove2(self,Sender,i,i2,i3):
        print (i,i2,i3)
        print(Sender.Left)
        print(CreateSetFormint(i,{1:"ssShift",2:"ssAlt", 4:"ssCtrl",8:"ssLeft", 5:"ssRight", 6:"ssMiddle", 7:"ssDouble",8:"ssMeta",9:"ssSuper", 10:"ssHyper", 11:"ssAltGr", 12:"ssCaps", 13:"ssNum",14:"ssScroll",15:"ssTriple",16:"ssQuad",17:"ssExtra1",18:"ssExtra2"}))
        #F=GetPytonObject(sender,TObject)

F2=Form1()    
Application_Initialize()
F=Application_CreateForm()
Forms_Application_CreateFormLFM
F.Top=330
F.Caption="kfdgdk"
B1=TButton.Create(F)
B1.Parent=F
B1.Parent.Caption="kkk"
B1.Caption="click me"
B1.OnClick=F2.OnButton1Click
B1.Top=80
B1.Left=90
C1=TComboBox.Create(F)
C1.Parent=F
C1.Text="hello"
#print F.Caption
print F.pointer
F.OnClick=F2.OnClickH
CK=TCheckBox.Create(F)
CK.Parent=F
CK.Top=100
#PasOnMouseForm = CFUNCTYPE(c_void_p,c_int,c_int,c_int,c_void_p,c_void_p)
#PasOnMouseMove=PasOnMouseForm(OnMouseMove2)
t2=TObject()
#t2.pointer=PasOnMouseMove
#LCLBinding.Set_Forms_TForm_FormMouseMove(F.pointer,t2.pointer)
F.OnMouseMove=F2.OnMouseMove2
Application_Run()
