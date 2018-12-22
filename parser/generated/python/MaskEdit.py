from lclstrconsts import *
from lclproc import *
from lcltype import *
from clipbrd import *
from lmessages import *
from StdCtrls import *
from ExtCtrls import *
from dialogs import *
from Graphics import *
from Controls import *
from Forms import *
from lresources import *
from Classes import *
from MainPasObject import *
import LCLBindingUtil
#import end
#class TCustomMaskEdit start
class TCustomMaskEdit(TCustomEdit):
#    pointer=c_void_p()
    def __init__(self):#TCustomMaskEdit
        TCustomEdit.__init__(self)
#Procedure MaskEdit_TCustomMaskEdit_CutToClipBoard
    @staticmethod
    def CutToClipBoard(self,):
        LCLBinding.MaskEdit_TCustomMaskEdit_CutToClipBoard()
#Procedure MaskEdit_TCustomMaskEdit_PasteFromClipBoard
    @staticmethod
    def PasteFromClipBoard(self,):
        LCLBinding.MaskEdit_TCustomMaskEdit_PasteFromClipBoard()
#constructorMaskEdit_TCustomMaskEdit_Create
    @staticmethod
    def Create(TheOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.MaskEdit_TCustomMaskEdit_Create((TheOwner.pointer)),TCustomMaskEdit)
#Procedure MaskEdit_TCustomMaskEdit_Clear
    @staticmethod
    def Clear(self,):
        LCLBinding.MaskEdit_TCustomMaskEdit_Clear()
#Procedure MaskEdit_TCustomMaskEdit_ValidateEdit
    @staticmethod
    def ValidateEdit(self,):
        LCLBinding.MaskEdit_TCustomMaskEdit_ValidateEdit()
    def getModified(self):
        r=LCLBinding.get_MaskEdit_TCustomMaskEdit_Modified(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setModified(self,v):
        LCLBinding.set_MaskEdit_TCustomMaskEdit_Modified(self.pointer,v)
    Modified=property(getModified,setModified)
#class TCustomMaskEdit end
#class TMaskEdit start
class TMaskEdit(TCustomMaskEdit):
#    pointer=c_void_p()
    def __init__(self):#TMaskEdit
        TCustomMaskEdit.__init__(self)
    def getIsMasked(self):
        r=LCLBinding.get_MaskEdit_TMaskEdit_IsMasked(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    IsMasked=property(getIsMasked)
    def getEditText(self):
        r=LCLBinding.get_MaskEdit_TMaskEdit_EditText(self.pointer)
        return LCLBindingUtil.ConvertPascalstring(r)
    def setEditText(self,v):
        LCLBinding.set_MaskEdit_TMaskEdit_EditText(self.pointer,v)
    EditText=property(getEditText,setEditText)
    def getAutoSelect(self):
        r=LCLBinding.get_MaskEdit_TMaskEdit_AutoSelect(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setAutoSelect(self,v):
        LCLBinding.set_MaskEdit_TMaskEdit_AutoSelect(self.pointer,v)
    AutoSelect=property(getAutoSelect,setAutoSelect)
    def getCharCase(self):
        r=LCLBinding.get_MaskEdit_TMaskEdit_CharCase(self.pointer)
        return r
    def setCharCase(self,v):
        LCLBinding.set_MaskEdit_TMaskEdit_CharCase(self.pointer,v.pointer)
    CharCase=property(getCharCase,setCharCase)
    def getDragKind(self):
        r=LCLBinding.get_MaskEdit_TMaskEdit_DragKind(self.pointer)
        return r
    def setDragKind(self,v):
        LCLBinding.set_MaskEdit_TMaskEdit_DragKind(self.pointer,v.pointer)
    DragKind=property(getDragKind,setDragKind)
    def getDragMode(self):
        r=LCLBinding.get_MaskEdit_TMaskEdit_DragMode(self.pointer)
        return r
    def setDragMode(self,v):
        LCLBinding.set_MaskEdit_TMaskEdit_DragMode(self.pointer,v.pointer)
    DragMode=property(getDragMode,setDragMode)
    def getMaxLength(self):
        r=LCLBinding.get_MaskEdit_TMaskEdit_MaxLength(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setMaxLength(self,v):
        LCLBinding.set_MaskEdit_TMaskEdit_MaxLength(self.pointer,v)
    MaxLength=property(getMaxLength,setMaxLength)
    def getParentColor(self):
        r=LCLBinding.get_MaskEdit_TMaskEdit_ParentColor(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentColor(self,v):
        LCLBinding.set_MaskEdit_TMaskEdit_ParentColor(self.pointer,v)
    ParentColor=property(getParentColor,setParentColor)
    def getParentFont(self):
        r=LCLBinding.get_MaskEdit_TMaskEdit_ParentFont(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentFont(self,v):
        LCLBinding.set_MaskEdit_TMaskEdit_ParentFont(self.pointer,v)
    ParentFont=property(getParentFont,setParentFont)
    def getParentShowHint(self):
        r=LCLBinding.get_MaskEdit_TMaskEdit_ParentShowHint(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentShowHint(self,v):
        LCLBinding.set_MaskEdit_TMaskEdit_ParentShowHint(self.pointer,v)
    ParentShowHint=property(getParentShowHint,setParentShowHint)
    def _Warper_OnDblClick(self,Sender):
        self.OnDblClickcall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnDblClick(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnDblClickcall'):
            FreeOldEvent=1
            oldobj=self.OnDblClickPasObject
        self.OnDblClickcall=v 
        self.PasOnDblClick=FunctionForm(self._Warper_OnDblClick)
        self.OnDblClickPasObject=LCLBinding.set_MaskEdit_TMaskEdit_OnDblClick(self.pointer,self.PasOnDblClick,oldobj,FreeOldEvent)
    def getOnDblClick(self):
        return OnDblClickcall
    OnDblClick=property(getOnDblClick,setOnDblClick)
    def _Warper_OnDragDrop(self,Sender,Source,X,Y):
        self.OnDragDropcall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.GetPytonObject(Source,TObject),X,Y)
    def setOnDragDrop(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnDragDropcall'):
            FreeOldEvent=1
            oldobj=self.OnDragDropPasObject
        self.OnDragDropcall=v 
        self.PasOnDragDrop=FunctionForm(self._Warper_OnDragDrop)
        self.OnDragDropPasObject=LCLBinding.set_MaskEdit_TMaskEdit_OnDragDrop(self.pointer,self.PasOnDragDrop,oldobj,FreeOldEvent)
    def getOnDragDrop(self):
        return OnDragDropcall
    OnDragDrop=property(getOnDragDrop,setOnDragDrop)
    def _Warper_OnDragOver(self,Sender,Source,X,Y,State,Accept):
        self.OnDragOvercall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.GetPytonObject(Source,TObject),X,Y,State,LCLBindingUtil.IntToBoolean(Accept))
    def setOnDragOver(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p,c_int,c_int,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnDragOvercall'):
            FreeOldEvent=1
            oldobj=self.OnDragOverPasObject
        self.OnDragOvercall=v 
        self.PasOnDragOver=FunctionForm(self._Warper_OnDragOver)
        self.OnDragOverPasObject=LCLBinding.set_MaskEdit_TMaskEdit_OnDragOver(self.pointer,self.PasOnDragOver,oldobj,FreeOldEvent)
    def getOnDragOver(self):
        return OnDragOvercall
    OnDragOver=property(getOnDragOver,setOnDragOver)
    def _Warper_OnEditingDone(self,Sender):
        self.OnEditingDonecall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnEditingDone(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnEditingDonecall'):
            FreeOldEvent=1
            oldobj=self.OnEditingDonePasObject
        self.OnEditingDonecall=v 
        self.PasOnEditingDone=FunctionForm(self._Warper_OnEditingDone)
        self.OnEditingDonePasObject=LCLBinding.set_MaskEdit_TMaskEdit_OnEditingDone(self.pointer,self.PasOnEditingDone,oldobj,FreeOldEvent)
    def getOnEditingDone(self):
        return OnEditingDonecall
    OnEditingDone=property(getOnEditingDone,setOnEditingDone)
    def _Warper_OnEndDock(self,Sender,Target,X,Y):
        self.OnEndDockcall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.GetPytonObject(Target,TObject),X,Y)
    def setOnEndDock(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnEndDockcall'):
            FreeOldEvent=1
            oldobj=self.OnEndDockPasObject
        self.OnEndDockcall=v 
        self.PasOnEndDock=FunctionForm(self._Warper_OnEndDock)
        self.OnEndDockPasObject=LCLBinding.set_MaskEdit_TMaskEdit_OnEndDock(self.pointer,self.PasOnEndDock,oldobj,FreeOldEvent)
    def getOnEndDock(self):
        return OnEndDockcall
    OnEndDock=property(getOnEndDock,setOnEndDock)
    def _Warper_OnEndDrag(self,Sender,Target,X,Y):
        self.OnEndDragcall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.GetPytonObject(Target,TObject),X,Y)
    def setOnEndDrag(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnEndDragcall'):
            FreeOldEvent=1
            oldobj=self.OnEndDragPasObject
        self.OnEndDragcall=v 
        self.PasOnEndDrag=FunctionForm(self._Warper_OnEndDrag)
        self.OnEndDragPasObject=LCLBinding.set_MaskEdit_TMaskEdit_OnEndDrag(self.pointer,self.PasOnEndDrag,oldobj,FreeOldEvent)
    def getOnEndDrag(self):
        return OnEndDragcall
    OnEndDrag=property(getOnEndDrag,setOnEndDrag)
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
        self.OnMouseDownPasObject=LCLBinding.set_MaskEdit_TMaskEdit_OnMouseDown(self.pointer,self.PasOnMouseDown,oldobj,FreeOldEvent)
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
        self.OnMouseEnterPasObject=LCLBinding.set_MaskEdit_TMaskEdit_OnMouseEnter(self.pointer,self.PasOnMouseEnter,oldobj,FreeOldEvent)
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
        self.OnMouseLeavePasObject=LCLBinding.set_MaskEdit_TMaskEdit_OnMouseLeave(self.pointer,self.PasOnMouseLeave,oldobj,FreeOldEvent)
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
        self.OnMouseMovePasObject=LCLBinding.set_MaskEdit_TMaskEdit_OnMouseMove(self.pointer,self.PasOnMouseMove,oldobj,FreeOldEvent)
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
        self.OnMouseUpPasObject=LCLBinding.set_MaskEdit_TMaskEdit_OnMouseUp(self.pointer,self.PasOnMouseUp,oldobj,FreeOldEvent)
    def getOnMouseUp(self):
        return OnMouseUpcall
    OnMouseUp=property(getOnMouseUp,setOnMouseUp)
    def _Warper_OnStartDock(self,Sender,DragObject):
        self.OnStartDockcall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.GetPytonObject(DragObject,TDragDockObject))
    def setOnStartDock(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnStartDockcall'):
            FreeOldEvent=1
            oldobj=self.OnStartDockPasObject
        self.OnStartDockcall=v 
        self.PasOnStartDock=FunctionForm(self._Warper_OnStartDock)
        self.OnStartDockPasObject=LCLBinding.set_MaskEdit_TMaskEdit_OnStartDock(self.pointer,self.PasOnStartDock,oldobj,FreeOldEvent)
    def getOnStartDock(self):
        return OnStartDockcall
    OnStartDock=property(getOnStartDock,setOnStartDock)
    def _Warper_OnStartDrag(self,Sender,DragObject):
        self.OnStartDragcall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.GetPytonObject(DragObject,TDragObject))
    def setOnStartDrag(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnStartDragcall'):
            FreeOldEvent=1
            oldobj=self.OnStartDragPasObject
        self.OnStartDragcall=v 
        self.PasOnStartDrag=FunctionForm(self._Warper_OnStartDrag)
        self.OnStartDragPasObject=LCLBinding.set_MaskEdit_TMaskEdit_OnStartDrag(self.pointer,self.PasOnStartDrag,oldobj,FreeOldEvent)
    def getOnStartDrag(self):
        return OnStartDragcall
    OnStartDrag=property(getOnStartDrag,setOnStartDrag)
    def getEditMask(self):
        r=LCLBinding.get_MaskEdit_TMaskEdit_EditMask(self.pointer)
        return LCLBindingUtil.ConvertPascalstring(r)
    def setEditMask(self,v):
        LCLBinding.set_MaskEdit_TMaskEdit_EditMask(self.pointer,v)
    EditMask=property(getEditMask,setEditMask)
#constructorMaskEdit_TMaskEdit_Create
    @staticmethod
    def Create(TheOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.MaskEdit_TMaskEdit_Create((TheOwner.pointer)),TMaskEdit)
#class TMaskEdit end
