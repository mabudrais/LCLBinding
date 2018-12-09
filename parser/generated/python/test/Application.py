#Application
from ctypes import *
from Forms import *
from LCLBindingUtil import *
from ReturnTypeDec import *
def Application_Initialize():
    LCLBinding.Forms_Application_Initialize()
def Application_CreateForm():
    return GetPytonObject(LCLBinding.Forms_Application_CreateForm(),TForm)
def Forms_Application_CreateFormLFM(MainFormType,MainFormName):
    LCLBinding.Forms_Application_CreateFormLFM.restype=c_char_p    
    r=LCLBinding.Forms_Application_CreateFormLFM("P",MainFormName)
    F=MainFormType()
    d=filter(None,r.split('*'))
    l=len(d)
    print l
    F.pointer=d[3]
   # F.show()
    k=4
    while k<l:
        if d[k]=="Pointer":
            print d[k]
            print d[k+1]
            print d[k+2]
            print d[k+3]
            obj=getattr(F,d[k+2])
            obj.pointer=int(d[k+3])
            SetPytonObject(obj.pointer,obj)
        if d[k]=="Event":
            print d[k]
            print d[k+1]
            print d[k+2]
            print d[k+3]
            obj=GetPytonObject2(int(d[k+3]))
            eh=getattr(F,d[k+2])#event Handle
            setattr(obj,d[k+1],eh)
        k=k+4
def Application_Run():
    LCLBinding.Forms_Application_Run()
