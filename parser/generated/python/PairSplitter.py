from ExtCtrls import *
from Controls import *
from GraphType import *
from Graphics import *
from lmessages import *
from lclproc import *
from lcltype import *
from Classes import *
from MainPasObject import *
import LCLBindingUtil
#import end
#class TPairSplitterSide start
class TPairSplitterSide(TWinControl):
#    pointer=c_void_p()
    def __init__(self):#TPairSplitterSide
        TWinControl.__init__(self)
#constructorPairSplitter_TPairSplitterSide_Create
    @staticmethod
    def Create(TheOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.PairSplitter_TPairSplitterSide_Create((TheOwner.pointer)),TPairSplitterSide)
    def getSplitter(self):
        r=LCLBinding.get_PairSplitter_TPairSplitterSide_Splitter(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TCustomPairSplitter)
    Splitter=property(getSplitter)
    def _Warper_OnMouseDown(self,Sender,Button,Shift,X,Y):
        self.OnMouseDowncall(LCLBindingUtil.GetPytonObject(Sender,TObject),Button,Shift,X,Y)
    def setOnMouseDown(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int,c_int,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnMouseDowncall'):
            FreeOldEvent=1
            oldobj=self.OnMouseDownPasObject
        self.OnMouseDowncall=v 
        self.PasOnMouseDown=FunctionForm(self._Warper_OnMouseDown)
        self.OnMouseDownPasObject=LCLBinding.set_PairSplitter_TPairSplitterSide_OnMouseDown(self.pointer,self.PasOnMouseDown,oldobj,FreeOldEvent)
    def getOnMouseDown(self):
        return OnMouseDowncall
    OnMouseDown=property(getOnMouseDown,setOnMouseDown)
    def _Warper_OnMouseEnter(self,Sender):
        self.OnMouseEntercall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnMouseEnter(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnMouseEntercall'):
            FreeOldEvent=1
            oldobj=self.OnMouseEnterPasObject
        self.OnMouseEntercall=v 
        self.PasOnMouseEnter=FunctionForm(self._Warper_OnMouseEnter)
        self.OnMouseEnterPasObject=LCLBinding.set_PairSplitter_TPairSplitterSide_OnMouseEnter(self.pointer,self.PasOnMouseEnter,oldobj,FreeOldEvent)
    def getOnMouseEnter(self):
        return OnMouseEntercall
    OnMouseEnter=property(getOnMouseEnter,setOnMouseEnter)
    def _Warper_OnMouseLeave(self,Sender):
        self.OnMouseLeavecall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnMouseLeave(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnMouseLeavecall'):
            FreeOldEvent=1
            oldobj=self.OnMouseLeavePasObject
        self.OnMouseLeavecall=v 
        self.PasOnMouseLeave=FunctionForm(self._Warper_OnMouseLeave)
        self.OnMouseLeavePasObject=LCLBinding.set_PairSplitter_TPairSplitterSide_OnMouseLeave(self.pointer,self.PasOnMouseLeave,oldobj,FreeOldEvent)
    def getOnMouseLeave(self):
        return OnMouseLeavecall
    OnMouseLeave=property(getOnMouseLeave,setOnMouseLeave)
    def _Warper_OnMouseMove(self,Sender,Shift,X,Y):
        self.OnMouseMovecall(LCLBindingUtil.GetPytonObject(Sender,TObject),Shift,X,Y)
    def setOnMouseMove(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnMouseMovecall'):
            FreeOldEvent=1
            oldobj=self.OnMouseMovePasObject
        self.OnMouseMovecall=v 
        self.PasOnMouseMove=FunctionForm(self._Warper_OnMouseMove)
        self.OnMouseMovePasObject=LCLBinding.set_PairSplitter_TPairSplitterSide_OnMouseMove(self.pointer,self.PasOnMouseMove,oldobj,FreeOldEvent)
    def getOnMouseMove(self):
        return OnMouseMovecall
    OnMouseMove=property(getOnMouseMove,setOnMouseMove)
    def _Warper_OnMouseUp(self,Sender,Button,Shift,X,Y):
        self.OnMouseUpcall(LCLBindingUtil.GetPytonObject(Sender,TObject),Button,Shift,X,Y)
    def setOnMouseUp(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int,c_int,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnMouseUpcall'):
            FreeOldEvent=1
            oldobj=self.OnMouseUpPasObject
        self.OnMouseUpcall=v 
        self.PasOnMouseUp=FunctionForm(self._Warper_OnMouseUp)
        self.OnMouseUpPasObject=LCLBinding.set_PairSplitter_TPairSplitterSide_OnMouseUp(self.pointer,self.PasOnMouseUp,oldobj,FreeOldEvent)
    def getOnMouseUp(self):
        return OnMouseUpcall
    OnMouseUp=property(getOnMouseUp,setOnMouseUp)
    def getParentShowHint(self):
        r=LCLBinding.get_PairSplitter_TPairSplitterSide_ParentShowHint(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentShowHint(self,v):
        LCLBinding.set_PairSplitter_TPairSplitterSide_ParentShowHint(self.pointer,v)
    ParentShowHint=property(getParentShowHint,setParentShowHint)
#class TPairSplitterSide end
#class TCustomPairSplitter start
class TCustomPairSplitter(TWinControl):
#    pointer=c_void_p()
    def __init__(self):#TCustomPairSplitter
        TWinControl.__init__(self)
#constructorPairSplitter_TCustomPairSplitter_Create
    @staticmethod
    def Create(TheOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.PairSplitter_TCustomPairSplitter_Create((TheOwner.pointer)),TCustomPairSplitter)
#Procedure PairSplitter_TCustomPairSplitter_CreateWnd
    @staticmethod
    def CreateWnd(self,):
        LCLBinding.PairSplitter_TCustomPairSplitter_CreateWnd()
#Procedure PairSplitter_TCustomPairSplitter_UpdatePosition
    @staticmethod
    def UpdatePosition(self,):
        LCLBinding.PairSplitter_TCustomPairSplitter_UpdatePosition()
#Procedure PairSplitter_TCustomPairSplitter_CreateSides
    @staticmethod
    def CreateSides(self,):
        LCLBinding.PairSplitter_TCustomPairSplitter_CreateSides()
#Procedure PairSplitter_TCustomPairSplitter_Loaded
    @staticmethod
    def Loaded(self,):
        LCLBinding.PairSplitter_TCustomPairSplitter_Loaded()
    def getSides(self,Index):
        r=LCLBinding.get_PairSplitter_TCustomPairSplitter_Sides(self.pointer,Index)
        return LCLBindingUtil.GetPytonObject(r,TPairSplitterSide)
    def getSplitterType(self):
        r=LCLBinding.get_PairSplitter_TCustomPairSplitter_SplitterType(self.pointer)
        return r
    def setSplitterType(self,v):
        LCLBinding.set_PairSplitter_TCustomPairSplitter_SplitterType(self.pointer,v.pointer)
    SplitterType=property(getSplitterType,setSplitterType)
    def getPosition(self):
        r=LCLBinding.get_PairSplitter_TCustomPairSplitter_Position(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setPosition(self,v):
        LCLBinding.set_PairSplitter_TCustomPairSplitter_Position(self.pointer,v)
    Position=property(getPosition,setPosition)
#class TCustomPairSplitter end
#class TPairSplitter start
class TPairSplitter(TCustomPairSplitter):
#    pointer=c_void_p()
    def __init__(self):#TPairSplitter
        TCustomPairSplitter.__init__(self)
    def _Warper_OnMouseDown(self,Sender,Button,Shift,X,Y):
        self.OnMouseDowncall(LCLBindingUtil.GetPytonObject(Sender,TObject),Button,Shift,X,Y)
    def setOnMouseDown(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int,c_int,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnMouseDowncall'):
            FreeOldEvent=1
            oldobj=self.OnMouseDownPasObject
        self.OnMouseDowncall=v 
        self.PasOnMouseDown=FunctionForm(self._Warper_OnMouseDown)
        self.OnMouseDownPasObject=LCLBinding.set_PairSplitter_TPairSplitter_OnMouseDown(self.pointer,self.PasOnMouseDown,oldobj,FreeOldEvent)
    def getOnMouseDown(self):
        return OnMouseDowncall
    OnMouseDown=property(getOnMouseDown,setOnMouseDown)
    def _Warper_OnMouseEnter(self,Sender):
        self.OnMouseEntercall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnMouseEnter(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnMouseEntercall'):
            FreeOldEvent=1
            oldobj=self.OnMouseEnterPasObject
        self.OnMouseEntercall=v 
        self.PasOnMouseEnter=FunctionForm(self._Warper_OnMouseEnter)
        self.OnMouseEnterPasObject=LCLBinding.set_PairSplitter_TPairSplitter_OnMouseEnter(self.pointer,self.PasOnMouseEnter,oldobj,FreeOldEvent)
    def getOnMouseEnter(self):
        return OnMouseEntercall
    OnMouseEnter=property(getOnMouseEnter,setOnMouseEnter)
    def _Warper_OnMouseLeave(self,Sender):
        self.OnMouseLeavecall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnMouseLeave(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnMouseLeavecall'):
            FreeOldEvent=1
            oldobj=self.OnMouseLeavePasObject
        self.OnMouseLeavecall=v 
        self.PasOnMouseLeave=FunctionForm(self._Warper_OnMouseLeave)
        self.OnMouseLeavePasObject=LCLBinding.set_PairSplitter_TPairSplitter_OnMouseLeave(self.pointer,self.PasOnMouseLeave,oldobj,FreeOldEvent)
    def getOnMouseLeave(self):
        return OnMouseLeavecall
    OnMouseLeave=property(getOnMouseLeave,setOnMouseLeave)
    def _Warper_OnMouseMove(self,Sender,Shift,X,Y):
        self.OnMouseMovecall(LCLBindingUtil.GetPytonObject(Sender,TObject),Shift,X,Y)
    def setOnMouseMove(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnMouseMovecall'):
            FreeOldEvent=1
            oldobj=self.OnMouseMovePasObject
        self.OnMouseMovecall=v 
        self.PasOnMouseMove=FunctionForm(self._Warper_OnMouseMove)
        self.OnMouseMovePasObject=LCLBinding.set_PairSplitter_TPairSplitter_OnMouseMove(self.pointer,self.PasOnMouseMove,oldobj,FreeOldEvent)
    def getOnMouseMove(self):
        return OnMouseMovecall
    OnMouseMove=property(getOnMouseMove,setOnMouseMove)
    def _Warper_OnMouseUp(self,Sender,Button,Shift,X,Y):
        self.OnMouseUpcall(LCLBindingUtil.GetPytonObject(Sender,TObject),Button,Shift,X,Y)
    def setOnMouseUp(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int,c_int,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnMouseUpcall'):
            FreeOldEvent=1
            oldobj=self.OnMouseUpPasObject
        self.OnMouseUpcall=v 
        self.PasOnMouseUp=FunctionForm(self._Warper_OnMouseUp)
        self.OnMouseUpPasObject=LCLBinding.set_PairSplitter_TPairSplitter_OnMouseUp(self.pointer,self.PasOnMouseUp,oldobj,FreeOldEvent)
    def getOnMouseUp(self):
        return OnMouseUpcall
    OnMouseUp=property(getOnMouseUp,setOnMouseUp)
    def getParentShowHint(self):
        r=LCLBinding.get_PairSplitter_TPairSplitter_ParentShowHint(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentShowHint(self,v):
        LCLBinding.set_PairSplitter_TPairSplitter_ParentShowHint(self.pointer,v)
    ParentShowHint=property(getParentShowHint,setParentShowHint)
#constructorPairSplitter_TPairSplitter_Create
    @staticmethod
    def Create(TheOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.PairSplitter_TPairSplitter_Create((TheOwner.pointer)),TPairSplitter)
#class TPairSplitter end
