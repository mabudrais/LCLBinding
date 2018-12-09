from MainPasObject import *
#import end
def CreateTListBoxOptionsFromInt(i):
    dic={1:"lboDrawFocusRect"}
    return CreateSetFormint(i,dic)
def CreateTComboBoxAutoCompleteTextFromInt(i):
    dic={1:"cbactEnabled",2:"cbactEndOfLineComplete",4:"cbactRetainPrefixCase",8:"cbactSearchCaseSensitive",16:"cbactSearchAscending"}
    return CreateSetFormint(i,dic)
#class TCustomStaticText start
class TCustomStaticText(TWinControl):
#    pointer=c_void_p()
    def __init__(self):#TCustomStaticText
        TWinControl.__init__(self)
#constructorStdCtrls_TCustomStaticText_Create
    @staticmethod
    def Create(AOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.StdCtrls_TCustomStaticText_Create((AOwner.pointer)),TCustomStaticText)
    def getAlignment(self):
        r=LCLBinding.get_StdCtrls_TCustomStaticText_Alignment(self.pointer)
        return r
    def setAlignment(self,v):
        LCLBinding.set_StdCtrls_TCustomStaticText_Alignment(self.pointer,v.pointer)
    Alignment=property(getAlignment,setAlignment)
    def getBorderStyle(self):
        r=LCLBinding.get_StdCtrls_TCustomStaticText_BorderStyle(self.pointer)
        return r
    def setBorderStyle(self,v):
        LCLBinding.set_StdCtrls_TCustomStaticText_BorderStyle(self.pointer,v.pointer)
    BorderStyle=property(getBorderStyle,setBorderStyle)
    def getFocusControl(self):
        r=LCLBinding.get_StdCtrls_TCustomStaticText_FocusControl(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TWinControl)
    def setFocusControl(self,v):
        LCLBinding.set_StdCtrls_TCustomStaticText_FocusControl(self.pointer,v.pointer)
    FocusControl=property(getFocusControl,setFocusControl)
    def getShowAccelChar(self):
        r=LCLBinding.get_StdCtrls_TCustomStaticText_ShowAccelChar(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setShowAccelChar(self,v):
        LCLBinding.set_StdCtrls_TCustomStaticText_ShowAccelChar(self.pointer,v)
    ShowAccelChar=property(getShowAccelChar,setShowAccelChar)
    def getTransparent(self):
        r=LCLBinding.get_StdCtrls_TCustomStaticText_Transparent(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setTransparent(self,v):
        LCLBinding.set_StdCtrls_TCustomStaticText_Transparent(self.pointer,v)
    Transparent=property(getTransparent,setTransparent)
#class TCustomStaticText end
#class TStaticText start
class TStaticText(TCustomStaticText):
#    pointer=c_void_p()
    def __init__(self):#TStaticText
        TCustomStaticText.__init__(self)
    def getDragKind(self):
        r=LCLBinding.get_StdCtrls_TStaticText_DragKind(self.pointer)
        return r
    def setDragKind(self,v):
        LCLBinding.set_StdCtrls_TStaticText_DragKind(self.pointer,v.pointer)
    DragKind=property(getDragKind,setDragKind)
    def getDragMode(self):
        r=LCLBinding.get_StdCtrls_TStaticText_DragMode(self.pointer)
        return r
    def setDragMode(self,v):
        LCLBinding.set_StdCtrls_TStaticText_DragMode(self.pointer,v.pointer)
    DragMode=property(getDragMode,setDragMode)
    def _Warper_OnDblClick(self,Sender):
        self.OnDblClickcall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnDblClick(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnDblClickcall'):
            FreeOldEvent=1
            oldobj=OnDblClickPasObject
        self.OnDblClickcall=v 
        self.PasOnDblClick=FunctionForm(self._Warper_OnDblClick)
        self.OnDblClickPasObject=LCLBinding.set_StdCtrls_TStaticText_OnDblClick(self.pointer,self.PasOnDblClick,oldobj,FreeOldEvent)
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
            oldobj=OnDragDropPasObject
        self.OnDragDropcall=v 
        self.PasOnDragDrop=FunctionForm(self._Warper_OnDragDrop)
        self.OnDragDropPasObject=LCLBinding.set_StdCtrls_TStaticText_OnDragDrop(self.pointer,self.PasOnDragDrop,oldobj,FreeOldEvent)
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
            oldobj=OnDragOverPasObject
        self.OnDragOvercall=v 
        self.PasOnDragOver=FunctionForm(self._Warper_OnDragOver)
        self.OnDragOverPasObject=LCLBinding.set_StdCtrls_TStaticText_OnDragOver(self.pointer,self.PasOnDragOver,oldobj,FreeOldEvent)
    def getOnDragOver(self):
        return OnDragOvercall
    OnDragOver=property(getOnDragOver,setOnDragOver)
    def _Warper_OnEndDrag(self,Sender,Target,X,Y):
        self.OnEndDragcall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.GetPytonObject(Target,TObject),X,Y)
    def setOnEndDrag(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnEndDragcall'):
            FreeOldEvent=1
            oldobj=OnEndDragPasObject
        self.OnEndDragcall=v 
        self.PasOnEndDrag=FunctionForm(self._Warper_OnEndDrag)
        self.OnEndDragPasObject=LCLBinding.set_StdCtrls_TStaticText_OnEndDrag(self.pointer,self.PasOnEndDrag,oldobj,FreeOldEvent)
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
            oldobj=OnMouseDownPasObject
        self.OnMouseDowncall=v 
        self.PasOnMouseDown=FunctionForm(self._Warper_OnMouseDown)
        self.OnMouseDownPasObject=LCLBinding.set_StdCtrls_TStaticText_OnMouseDown(self.pointer,self.PasOnMouseDown,oldobj,FreeOldEvent)
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
            oldobj=OnMouseEnterPasObject
        self.OnMouseEntercall=v 
        self.PasOnMouseEnter=FunctionForm(self._Warper_OnMouseEnter)
        self.OnMouseEnterPasObject=LCLBinding.set_StdCtrls_TStaticText_OnMouseEnter(self.pointer,self.PasOnMouseEnter,oldobj,FreeOldEvent)
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
            oldobj=OnMouseLeavePasObject
        self.OnMouseLeavecall=v 
        self.PasOnMouseLeave=FunctionForm(self._Warper_OnMouseLeave)
        self.OnMouseLeavePasObject=LCLBinding.set_StdCtrls_TStaticText_OnMouseLeave(self.pointer,self.PasOnMouseLeave,oldobj,FreeOldEvent)
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
            oldobj=OnMouseMovePasObject
        self.OnMouseMovecall=v 
        self.PasOnMouseMove=FunctionForm(self._Warper_OnMouseMove)
        self.OnMouseMovePasObject=LCLBinding.set_StdCtrls_TStaticText_OnMouseMove(self.pointer,self.PasOnMouseMove,oldobj,FreeOldEvent)
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
            oldobj=OnMouseUpPasObject
        self.OnMouseUpcall=v 
        self.PasOnMouseUp=FunctionForm(self._Warper_OnMouseUp)
        self.OnMouseUpPasObject=LCLBinding.set_StdCtrls_TStaticText_OnMouseUp(self.pointer,self.PasOnMouseUp,oldobj,FreeOldEvent)
    def getOnMouseUp(self):
        return OnMouseUpcall
    OnMouseUp=property(getOnMouseUp,setOnMouseUp)
    def _Warper_OnStartDrag(self,Sender,DragObject):
        self.OnStartDragcall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.GetPytonObject(DragObject,TDragObject))
    def setOnStartDrag(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnStartDragcall'):
            FreeOldEvent=1
            oldobj=OnStartDragPasObject
        self.OnStartDragcall=v 
        self.PasOnStartDrag=FunctionForm(self._Warper_OnStartDrag)
        self.OnStartDragPasObject=LCLBinding.set_StdCtrls_TStaticText_OnStartDrag(self.pointer,self.PasOnStartDrag,oldobj,FreeOldEvent)
    def getOnStartDrag(self):
        return OnStartDragcall
    OnStartDrag=property(getOnStartDrag,setOnStartDrag)
    def getParentFont(self):
        r=LCLBinding.get_StdCtrls_TStaticText_ParentFont(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentFont(self,v):
        LCLBinding.set_StdCtrls_TStaticText_ParentFont(self.pointer,v)
    ParentFont=property(getParentFont,setParentFont)
    def getParentColor(self):
        r=LCLBinding.get_StdCtrls_TStaticText_ParentColor(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentColor(self,v):
        LCLBinding.set_StdCtrls_TStaticText_ParentColor(self.pointer,v)
    ParentColor=property(getParentColor,setParentColor)
    def getParentShowHint(self):
        r=LCLBinding.get_StdCtrls_TStaticText_ParentShowHint(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentShowHint(self,v):
        LCLBinding.set_StdCtrls_TStaticText_ParentShowHint(self.pointer,v)
    ParentShowHint=property(getParentShowHint,setParentShowHint)
#constructorStdCtrls_TStaticText_Create
    @staticmethod
    def Create(AOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.StdCtrls_TStaticText_Create((AOwner.pointer)),TStaticText)
#class TStaticText end
#class TCustomScrollBar start
class TCustomScrollBar(TWinControl):
#    pointer=c_void_p()
    def __init__(self):#TCustomScrollBar
        TWinControl.__init__(self)
#constructorStdCtrls_TCustomScrollBar_Create
    @staticmethod
    def Create(AOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.StdCtrls_TCustomScrollBar_Create((AOwner.pointer)),TCustomScrollBar)
    def getKind(self):
        r=LCLBinding.get_StdCtrls_TCustomScrollBar_Kind(self.pointer)
        return r
    def setKind(self,v):
        LCLBinding.set_StdCtrls_TCustomScrollBar_Kind(self.pointer,v.pointer)
    Kind=property(getKind,setKind)
    def getMax(self):
        r=LCLBinding.get_StdCtrls_TCustomScrollBar_Max(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setMax(self,v):
        LCLBinding.set_StdCtrls_TCustomScrollBar_Max(self.pointer,v)
    Max=property(getMax,setMax)
    def getMin(self):
        r=LCLBinding.get_StdCtrls_TCustomScrollBar_Min(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setMin(self,v):
        LCLBinding.set_StdCtrls_TCustomScrollBar_Min(self.pointer,v)
    Min=property(getMin,setMin)
    def getPageSize(self):
        r=LCLBinding.get_StdCtrls_TCustomScrollBar_PageSize(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setPageSize(self,v):
        LCLBinding.set_StdCtrls_TCustomScrollBar_PageSize(self.pointer,v)
    PageSize=property(getPageSize,setPageSize)
    def getPosition(self):
        r=LCLBinding.get_StdCtrls_TCustomScrollBar_Position(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setPosition(self,v):
        LCLBinding.set_StdCtrls_TCustomScrollBar_Position(self.pointer,v)
    Position=property(getPosition,setPosition)
    def _Warper_OnChange(self,Sender):
        self.OnChangecall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnChange(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnChangecall'):
            FreeOldEvent=1
            oldobj=OnChangePasObject
        self.OnChangecall=v 
        self.PasOnChange=FunctionForm(self._Warper_OnChange)
        self.OnChangePasObject=LCLBinding.set_StdCtrls_TCustomScrollBar_OnChange(self.pointer,self.PasOnChange,oldobj,FreeOldEvent)
    def getOnChange(self):
        return OnChangecall
    OnChange=property(getOnChange,setOnChange)
    def _Warper_OnScroll(self,Sender,ScrollCode,ScrollPos):
        self.OnScrollcall(LCLBindingUtil.GetPytonObject(Sender,TObject),ScrollCode,ScrollPos)
    def setOnScroll(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnScrollcall'):
            FreeOldEvent=1
            oldobj=OnScrollPasObject
        self.OnScrollcall=v 
        self.PasOnScroll=FunctionForm(self._Warper_OnScroll)
        self.OnScrollPasObject=LCLBinding.set_StdCtrls_TCustomScrollBar_OnScroll(self.pointer,self.PasOnScroll,oldobj,FreeOldEvent)
    def getOnScroll(self):
        return OnScrollcall
    OnScroll=property(getOnScroll,setOnScroll)
#class TCustomScrollBar end
#class TScrollBar start
class TScrollBar(TCustomScrollBar):
#    pointer=c_void_p()
    def __init__(self):#TScrollBar
        TCustomScrollBar.__init__(self)
    def getDragKind(self):
        r=LCLBinding.get_StdCtrls_TScrollBar_DragKind(self.pointer)
        return r
    def setDragKind(self,v):
        LCLBinding.set_StdCtrls_TScrollBar_DragKind(self.pointer,v.pointer)
    DragKind=property(getDragKind,setDragKind)
    def getDragMode(self):
        r=LCLBinding.get_StdCtrls_TScrollBar_DragMode(self.pointer)
        return r
    def setDragMode(self,v):
        LCLBinding.set_StdCtrls_TScrollBar_DragMode(self.pointer,v.pointer)
    DragMode=property(getDragMode,setDragMode)
    def getParentShowHint(self):
        r=LCLBinding.get_StdCtrls_TScrollBar_ParentShowHint(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentShowHint(self,v):
        LCLBinding.set_StdCtrls_TScrollBar_ParentShowHint(self.pointer,v)
    ParentShowHint=property(getParentShowHint,setParentShowHint)
    def _Warper_OnDragDrop(self,Sender,Source,X,Y):
        self.OnDragDropcall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.GetPytonObject(Source,TObject),X,Y)
    def setOnDragDrop(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnDragDropcall'):
            FreeOldEvent=1
            oldobj=OnDragDropPasObject
        self.OnDragDropcall=v 
        self.PasOnDragDrop=FunctionForm(self._Warper_OnDragDrop)
        self.OnDragDropPasObject=LCLBinding.set_StdCtrls_TScrollBar_OnDragDrop(self.pointer,self.PasOnDragDrop,oldobj,FreeOldEvent)
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
            oldobj=OnDragOverPasObject
        self.OnDragOvercall=v 
        self.PasOnDragOver=FunctionForm(self._Warper_OnDragOver)
        self.OnDragOverPasObject=LCLBinding.set_StdCtrls_TScrollBar_OnDragOver(self.pointer,self.PasOnDragOver,oldobj,FreeOldEvent)
    def getOnDragOver(self):
        return OnDragOvercall
    OnDragOver=property(getOnDragOver,setOnDragOver)
    def _Warper_OnEndDrag(self,Sender,Target,X,Y):
        self.OnEndDragcall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.GetPytonObject(Target,TObject),X,Y)
    def setOnEndDrag(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnEndDragcall'):
            FreeOldEvent=1
            oldobj=OnEndDragPasObject
        self.OnEndDragcall=v 
        self.PasOnEndDrag=FunctionForm(self._Warper_OnEndDrag)
        self.OnEndDragPasObject=LCLBinding.set_StdCtrls_TScrollBar_OnEndDrag(self.pointer,self.PasOnEndDrag,oldobj,FreeOldEvent)
    def getOnEndDrag(self):
        return OnEndDragcall
    OnEndDrag=property(getOnEndDrag,setOnEndDrag)
    def _Warper_OnStartDrag(self,Sender,DragObject):
        self.OnStartDragcall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.GetPytonObject(DragObject,TDragObject))
    def setOnStartDrag(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnStartDragcall'):
            FreeOldEvent=1
            oldobj=OnStartDragPasObject
        self.OnStartDragcall=v 
        self.PasOnStartDrag=FunctionForm(self._Warper_OnStartDrag)
        self.OnStartDragPasObject=LCLBinding.set_StdCtrls_TScrollBar_OnStartDrag(self.pointer,self.PasOnStartDrag,oldobj,FreeOldEvent)
    def getOnStartDrag(self):
        return OnStartDragcall
    OnStartDrag=property(getOnStartDrag,setOnStartDrag)
#constructorStdCtrls_TScrollBar_Create
    @staticmethod
    def Create(AOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.StdCtrls_TScrollBar_Create((AOwner.pointer)),TScrollBar)
#class TScrollBar end
#class TCustomListBox start
class TCustomListBox(TWinControl):
#    pointer=c_void_p()
    def __init__(self):#TCustomListBox
        TWinControl.__init__(self)
#constructorStdCtrls_TCustomListBox_Create
    @staticmethod
    def Create(TheOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.StdCtrls_TCustomListBox_Create((TheOwner.pointer)),TCustomListBox)
    def getCanvas(self):
        r=LCLBinding.get_StdCtrls_TCustomListBox_Canvas(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TCanvas)
    Canvas=property(getCanvas)
    def getClickOnSelChange(self):
        r=LCLBinding.get_StdCtrls_TCustomListBox_ClickOnSelChange(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setClickOnSelChange(self,v):
        LCLBinding.set_StdCtrls_TCustomListBox_ClickOnSelChange(self.pointer,v)
    ClickOnSelChange=property(getClickOnSelChange,setClickOnSelChange)
    def getColumns(self):
        r=LCLBinding.get_StdCtrls_TCustomListBox_Columns(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setColumns(self,v):
        LCLBinding.set_StdCtrls_TCustomListBox_Columns(self.pointer,v)
    Columns=property(getColumns,setColumns)
    def getCount(self):
        r=LCLBinding.get_StdCtrls_TCustomListBox_Count(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    Count=property(getCount)
    def getExtendedSelect(self):
        r=LCLBinding.get_StdCtrls_TCustomListBox_ExtendedSelect(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setExtendedSelect(self,v):
        LCLBinding.set_StdCtrls_TCustomListBox_ExtendedSelect(self.pointer,v)
    ExtendedSelect=property(getExtendedSelect,setExtendedSelect)
    def getIntegralHeight(self):
        r=LCLBinding.get_StdCtrls_TCustomListBox_IntegralHeight(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setIntegralHeight(self,v):
        LCLBinding.set_StdCtrls_TCustomListBox_IntegralHeight(self.pointer,v)
    IntegralHeight=property(getIntegralHeight,setIntegralHeight)
    def getItemHeight(self):
        r=LCLBinding.get_StdCtrls_TCustomListBox_ItemHeight(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setItemHeight(self,v):
        LCLBinding.set_StdCtrls_TCustomListBox_ItemHeight(self.pointer,v)
    ItemHeight=property(getItemHeight,setItemHeight)
    def getItemIndex(self):
        r=LCLBinding.get_StdCtrls_TCustomListBox_ItemIndex(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setItemIndex(self,v):
        LCLBinding.set_StdCtrls_TCustomListBox_ItemIndex(self.pointer,v)
    ItemIndex=property(getItemIndex,setItemIndex)
    def getItems(self):
        r=LCLBinding.get_StdCtrls_TCustomListBox_Items(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TStrings)
    def setItems(self,v):
        LCLBinding.set_StdCtrls_TCustomListBox_Items(self.pointer,v.pointer)
    Items=property(getItems,setItems)
    def getMultiSelect(self):
        r=LCLBinding.get_StdCtrls_TCustomListBox_MultiSelect(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setMultiSelect(self,v):
        LCLBinding.set_StdCtrls_TCustomListBox_MultiSelect(self.pointer,v)
    MultiSelect=property(getMultiSelect,setMultiSelect)
    def _Warper_OnDblClick(self,Sender):
        self.OnDblClickcall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnDblClick(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnDblClickcall'):
            FreeOldEvent=1
            oldobj=OnDblClickPasObject
        self.OnDblClickcall=v 
        self.PasOnDblClick=FunctionForm(self._Warper_OnDblClick)
        self.OnDblClickPasObject=LCLBinding.set_StdCtrls_TCustomListBox_OnDblClick(self.pointer,self.PasOnDblClick,oldobj,FreeOldEvent)
    def getOnDblClick(self):
        return OnDblClickcall
    OnDblClick=property(getOnDblClick,setOnDblClick)
    def _Warper_OnMeasureItem(self,Control,Index,AHeight):
        self.OnMeasureItemcall(LCLBindingUtil.GetPytonObject(Control,TWinControl),Index,AHeight)
    def setOnMeasureItem(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnMeasureItemcall'):
            FreeOldEvent=1
            oldobj=OnMeasureItemPasObject
        self.OnMeasureItemcall=v 
        self.PasOnMeasureItem=FunctionForm(self._Warper_OnMeasureItem)
        self.OnMeasureItemPasObject=LCLBinding.set_StdCtrls_TCustomListBox_OnMeasureItem(self.pointer,self.PasOnMeasureItem,oldobj,FreeOldEvent)
    def getOnMeasureItem(self):
        return OnMeasureItemcall
    OnMeasureItem=property(getOnMeasureItem,setOnMeasureItem)
    def _Warper_OnMouseDown(self,Sender,Button,Shift,X,Y):
        self.OnMouseDowncall(LCLBindingUtil.GetPytonObject(Sender,TObject),Button,Shift,X,Y)
    def setOnMouseDown(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int,c_int,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnMouseDowncall'):
            FreeOldEvent=1
            oldobj=OnMouseDownPasObject
        self.OnMouseDowncall=v 
        self.PasOnMouseDown=FunctionForm(self._Warper_OnMouseDown)
        self.OnMouseDownPasObject=LCLBinding.set_StdCtrls_TCustomListBox_OnMouseDown(self.pointer,self.PasOnMouseDown,oldobj,FreeOldEvent)
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
            oldobj=OnMouseEnterPasObject
        self.OnMouseEntercall=v 
        self.PasOnMouseEnter=FunctionForm(self._Warper_OnMouseEnter)
        self.OnMouseEnterPasObject=LCLBinding.set_StdCtrls_TCustomListBox_OnMouseEnter(self.pointer,self.PasOnMouseEnter,oldobj,FreeOldEvent)
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
            oldobj=OnMouseLeavePasObject
        self.OnMouseLeavecall=v 
        self.PasOnMouseLeave=FunctionForm(self._Warper_OnMouseLeave)
        self.OnMouseLeavePasObject=LCLBinding.set_StdCtrls_TCustomListBox_OnMouseLeave(self.pointer,self.PasOnMouseLeave,oldobj,FreeOldEvent)
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
            oldobj=OnMouseMovePasObject
        self.OnMouseMovecall=v 
        self.PasOnMouseMove=FunctionForm(self._Warper_OnMouseMove)
        self.OnMouseMovePasObject=LCLBinding.set_StdCtrls_TCustomListBox_OnMouseMove(self.pointer,self.PasOnMouseMove,oldobj,FreeOldEvent)
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
            oldobj=OnMouseUpPasObject
        self.OnMouseUpcall=v 
        self.PasOnMouseUp=FunctionForm(self._Warper_OnMouseUp)
        self.OnMouseUpPasObject=LCLBinding.set_StdCtrls_TCustomListBox_OnMouseUp(self.pointer,self.PasOnMouseUp,oldobj,FreeOldEvent)
    def getOnMouseUp(self):
        return OnMouseUpcall
    OnMouseUp=property(getOnMouseUp,setOnMouseUp)
    def _Warper_OnSelectionChange(self,Sender,User):
        self.OnSelectionChangecall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.IntToBoolean(User))
    def setOnSelectionChange(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnSelectionChangecall'):
            FreeOldEvent=1
            oldobj=OnSelectionChangePasObject
        self.OnSelectionChangecall=v 
        self.PasOnSelectionChange=FunctionForm(self._Warper_OnSelectionChange)
        self.OnSelectionChangePasObject=LCLBinding.set_StdCtrls_TCustomListBox_OnSelectionChange(self.pointer,self.PasOnSelectionChange,oldobj,FreeOldEvent)
    def getOnSelectionChange(self):
        return OnSelectionChangecall
    OnSelectionChange=property(getOnSelectionChange,setOnSelectionChange)
    def getOptions(self):
        r=LCLBinding.get_StdCtrls_TCustomListBox_Options(self.pointer)
        return r
    def setOptions(self,v):
        LCLBinding.set_StdCtrls_TCustomListBox_Options(self.pointer,v.pointer)
    Options=property(getOptions,setOptions)
    def getParentColor(self):
        r=LCLBinding.get_StdCtrls_TCustomListBox_ParentColor(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentColor(self,v):
        LCLBinding.set_StdCtrls_TCustomListBox_ParentColor(self.pointer,v)
    ParentColor=property(getParentColor,setParentColor)
    def getParentFont(self):
        r=LCLBinding.get_StdCtrls_TCustomListBox_ParentFont(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentFont(self,v):
        LCLBinding.set_StdCtrls_TCustomListBox_ParentFont(self.pointer,v)
    ParentFont=property(getParentFont,setParentFont)
    def getParentShowHint(self):
        r=LCLBinding.get_StdCtrls_TCustomListBox_ParentShowHint(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentShowHint(self,v):
        LCLBinding.set_StdCtrls_TCustomListBox_ParentShowHint(self.pointer,v)
    ParentShowHint=property(getParentShowHint,setParentShowHint)
    def getScrollWidth(self):
        r=LCLBinding.get_StdCtrls_TCustomListBox_ScrollWidth(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setScrollWidth(self,v):
        LCLBinding.set_StdCtrls_TCustomListBox_ScrollWidth(self.pointer,v)
    ScrollWidth=property(getScrollWidth,setScrollWidth)
    def getSelCount(self):
        r=LCLBinding.get_StdCtrls_TCustomListBox_SelCount(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    SelCount=property(getSelCount)
    def getSelected(self,Index):
        r=LCLBinding.get_StdCtrls_TCustomListBox_Selected(self.pointer,Index)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setSelected(self,Index,v):
        LCLBinding.set_StdCtrls_TCustomListBox_Selected(self.pointer,Index,v)
    def getSorted(self):
        r=LCLBinding.get_StdCtrls_TCustomListBox_Sorted(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setSorted(self,v):
        LCLBinding.set_StdCtrls_TCustomListBox_Sorted(self.pointer,v)
    Sorted=property(getSorted,setSorted)
    def getStyle(self):
        r=LCLBinding.get_StdCtrls_TCustomListBox_Style(self.pointer)
        return r
    def setStyle(self,v):
        LCLBinding.set_StdCtrls_TCustomListBox_Style(self.pointer,v.pointer)
    Style=property(getStyle,setStyle)
    def getTopIndex(self):
        r=LCLBinding.get_StdCtrls_TCustomListBox_TopIndex(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setTopIndex(self,v):
        LCLBinding.set_StdCtrls_TCustomListBox_TopIndex(self.pointer,v)
    TopIndex=property(getTopIndex,setTopIndex)
#class TCustomListBox end
#class TListBox start
class TListBox(TCustomListBox):
#    pointer=c_void_p()
    def __init__(self):#TListBox
        TCustomListBox.__init__(self)
    def getDragKind(self):
        r=LCLBinding.get_StdCtrls_TListBox_DragKind(self.pointer)
        return r
    def setDragKind(self,v):
        LCLBinding.set_StdCtrls_TListBox_DragKind(self.pointer,v.pointer)
    DragKind=property(getDragKind,setDragKind)
    def getDragMode(self):
        r=LCLBinding.get_StdCtrls_TListBox_DragMode(self.pointer)
        return r
    def setDragMode(self,v):
        LCLBinding.set_StdCtrls_TListBox_DragMode(self.pointer,v.pointer)
    DragMode=property(getDragMode,setDragMode)
    def _Warper_OnDragDrop(self,Sender,Source,X,Y):
        self.OnDragDropcall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.GetPytonObject(Source,TObject),X,Y)
    def setOnDragDrop(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnDragDropcall'):
            FreeOldEvent=1
            oldobj=OnDragDropPasObject
        self.OnDragDropcall=v 
        self.PasOnDragDrop=FunctionForm(self._Warper_OnDragDrop)
        self.OnDragDropPasObject=LCLBinding.set_StdCtrls_TListBox_OnDragDrop(self.pointer,self.PasOnDragDrop,oldobj,FreeOldEvent)
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
            oldobj=OnDragOverPasObject
        self.OnDragOvercall=v 
        self.PasOnDragOver=FunctionForm(self._Warper_OnDragOver)
        self.OnDragOverPasObject=LCLBinding.set_StdCtrls_TListBox_OnDragOver(self.pointer,self.PasOnDragOver,oldobj,FreeOldEvent)
    def getOnDragOver(self):
        return OnDragOvercall
    OnDragOver=property(getOnDragOver,setOnDragOver)
    def _Warper_OnEndDrag(self,Sender,Target,X,Y):
        self.OnEndDragcall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.GetPytonObject(Target,TObject),X,Y)
    def setOnEndDrag(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnEndDragcall'):
            FreeOldEvent=1
            oldobj=OnEndDragPasObject
        self.OnEndDragcall=v 
        self.PasOnEndDrag=FunctionForm(self._Warper_OnEndDrag)
        self.OnEndDragPasObject=LCLBinding.set_StdCtrls_TListBox_OnEndDrag(self.pointer,self.PasOnEndDrag,oldobj,FreeOldEvent)
    def getOnEndDrag(self):
        return OnEndDragcall
    OnEndDrag=property(getOnEndDrag,setOnEndDrag)
    def _Warper_OnStartDrag(self,Sender,DragObject):
        self.OnStartDragcall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.GetPytonObject(DragObject,TDragObject))
    def setOnStartDrag(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnStartDragcall'):
            FreeOldEvent=1
            oldobj=OnStartDragPasObject
        self.OnStartDragcall=v 
        self.PasOnStartDrag=FunctionForm(self._Warper_OnStartDrag)
        self.OnStartDragPasObject=LCLBinding.set_StdCtrls_TListBox_OnStartDrag(self.pointer,self.PasOnStartDrag,oldobj,FreeOldEvent)
    def getOnStartDrag(self):
        return OnStartDragcall
    OnStartDrag=property(getOnStartDrag,setOnStartDrag)
#constructorStdCtrls_TListBox_Create
    @staticmethod
    def Create(TheOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.StdCtrls_TListBox_Create((TheOwner.pointer)),TListBox)
#class TListBox end
#class TCustomLabel start
class TCustomLabel(TGraphicControl):
#    pointer=c_void_p()
    def __init__(self):#TCustomLabel
        TGraphicControl.__init__(self)
#constructorStdCtrls_TCustomLabel_Create
    @staticmethod
    def Create(TheOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.StdCtrls_TCustomLabel_Create((TheOwner.pointer)),TCustomLabel)
#class TCustomLabel end
#class TLabel start
class TLabel(TCustomLabel):
#    pointer=c_void_p()
    def __init__(self):#TLabel
        TCustomLabel.__init__(self)
    def getAlignment(self):
        r=LCLBinding.get_StdCtrls_TLabel_Alignment(self.pointer)
        return r
    def setAlignment(self,v):
        LCLBinding.set_StdCtrls_TLabel_Alignment(self.pointer,v.pointer)
    Alignment=property(getAlignment,setAlignment)
    def getDragKind(self):
        r=LCLBinding.get_StdCtrls_TLabel_DragKind(self.pointer)
        return r
    def setDragKind(self,v):
        LCLBinding.set_StdCtrls_TLabel_DragKind(self.pointer,v.pointer)
    DragKind=property(getDragKind,setDragKind)
    def getDragMode(self):
        r=LCLBinding.get_StdCtrls_TLabel_DragMode(self.pointer)
        return r
    def setDragMode(self,v):
        LCLBinding.set_StdCtrls_TLabel_DragMode(self.pointer,v.pointer)
    DragMode=property(getDragMode,setDragMode)
    def getFocusControl(self):
        r=LCLBinding.get_StdCtrls_TLabel_FocusControl(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TWinControl)
    def setFocusControl(self,v):
        LCLBinding.set_StdCtrls_TLabel_FocusControl(self.pointer,v.pointer)
    FocusControl=property(getFocusControl,setFocusControl)
    def getLayout(self):
        r=LCLBinding.get_StdCtrls_TLabel_Layout(self.pointer)
        return r
    def setLayout(self,v):
        LCLBinding.set_StdCtrls_TLabel_Layout(self.pointer,v.pointer)
    Layout=property(getLayout,setLayout)
    def getParentColor(self):
        r=LCLBinding.get_StdCtrls_TLabel_ParentColor(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentColor(self,v):
        LCLBinding.set_StdCtrls_TLabel_ParentColor(self.pointer,v)
    ParentColor=property(getParentColor,setParentColor)
    def getParentFont(self):
        r=LCLBinding.get_StdCtrls_TLabel_ParentFont(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentFont(self,v):
        LCLBinding.set_StdCtrls_TLabel_ParentFont(self.pointer,v)
    ParentFont=property(getParentFont,setParentFont)
    def getParentShowHint(self):
        r=LCLBinding.get_StdCtrls_TLabel_ParentShowHint(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentShowHint(self,v):
        LCLBinding.set_StdCtrls_TLabel_ParentShowHint(self.pointer,v)
    ParentShowHint=property(getParentShowHint,setParentShowHint)
    def getShowAccelChar(self):
        r=LCLBinding.get_StdCtrls_TLabel_ShowAccelChar(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setShowAccelChar(self,v):
        LCLBinding.set_StdCtrls_TLabel_ShowAccelChar(self.pointer,v)
    ShowAccelChar=property(getShowAccelChar,setShowAccelChar)
    def getTransparent(self):
        r=LCLBinding.get_StdCtrls_TLabel_Transparent(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setTransparent(self,v):
        LCLBinding.set_StdCtrls_TLabel_Transparent(self.pointer,v)
    Transparent=property(getTransparent,setTransparent)
    def getWordWrap(self):
        r=LCLBinding.get_StdCtrls_TLabel_WordWrap(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setWordWrap(self,v):
        LCLBinding.set_StdCtrls_TLabel_WordWrap(self.pointer,v)
    WordWrap=property(getWordWrap,setWordWrap)
    def _Warper_OnDblClick(self,Sender):
        self.OnDblClickcall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnDblClick(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnDblClickcall'):
            FreeOldEvent=1
            oldobj=OnDblClickPasObject
        self.OnDblClickcall=v 
        self.PasOnDblClick=FunctionForm(self._Warper_OnDblClick)
        self.OnDblClickPasObject=LCLBinding.set_StdCtrls_TLabel_OnDblClick(self.pointer,self.PasOnDblClick,oldobj,FreeOldEvent)
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
            oldobj=OnDragDropPasObject
        self.OnDragDropcall=v 
        self.PasOnDragDrop=FunctionForm(self._Warper_OnDragDrop)
        self.OnDragDropPasObject=LCLBinding.set_StdCtrls_TLabel_OnDragDrop(self.pointer,self.PasOnDragDrop,oldobj,FreeOldEvent)
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
            oldobj=OnDragOverPasObject
        self.OnDragOvercall=v 
        self.PasOnDragOver=FunctionForm(self._Warper_OnDragOver)
        self.OnDragOverPasObject=LCLBinding.set_StdCtrls_TLabel_OnDragOver(self.pointer,self.PasOnDragOver,oldobj,FreeOldEvent)
    def getOnDragOver(self):
        return OnDragOvercall
    OnDragOver=property(getOnDragOver,setOnDragOver)
    def _Warper_OnEndDrag(self,Sender,Target,X,Y):
        self.OnEndDragcall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.GetPytonObject(Target,TObject),X,Y)
    def setOnEndDrag(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnEndDragcall'):
            FreeOldEvent=1
            oldobj=OnEndDragPasObject
        self.OnEndDragcall=v 
        self.PasOnEndDrag=FunctionForm(self._Warper_OnEndDrag)
        self.OnEndDragPasObject=LCLBinding.set_StdCtrls_TLabel_OnEndDrag(self.pointer,self.PasOnEndDrag,oldobj,FreeOldEvent)
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
            oldobj=OnMouseDownPasObject
        self.OnMouseDowncall=v 
        self.PasOnMouseDown=FunctionForm(self._Warper_OnMouseDown)
        self.OnMouseDownPasObject=LCLBinding.set_StdCtrls_TLabel_OnMouseDown(self.pointer,self.PasOnMouseDown,oldobj,FreeOldEvent)
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
            oldobj=OnMouseEnterPasObject
        self.OnMouseEntercall=v 
        self.PasOnMouseEnter=FunctionForm(self._Warper_OnMouseEnter)
        self.OnMouseEnterPasObject=LCLBinding.set_StdCtrls_TLabel_OnMouseEnter(self.pointer,self.PasOnMouseEnter,oldobj,FreeOldEvent)
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
            oldobj=OnMouseLeavePasObject
        self.OnMouseLeavecall=v 
        self.PasOnMouseLeave=FunctionForm(self._Warper_OnMouseLeave)
        self.OnMouseLeavePasObject=LCLBinding.set_StdCtrls_TLabel_OnMouseLeave(self.pointer,self.PasOnMouseLeave,oldobj,FreeOldEvent)
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
            oldobj=OnMouseMovePasObject
        self.OnMouseMovecall=v 
        self.PasOnMouseMove=FunctionForm(self._Warper_OnMouseMove)
        self.OnMouseMovePasObject=LCLBinding.set_StdCtrls_TLabel_OnMouseMove(self.pointer,self.PasOnMouseMove,oldobj,FreeOldEvent)
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
            oldobj=OnMouseUpPasObject
        self.OnMouseUpcall=v 
        self.PasOnMouseUp=FunctionForm(self._Warper_OnMouseUp)
        self.OnMouseUpPasObject=LCLBinding.set_StdCtrls_TLabel_OnMouseUp(self.pointer,self.PasOnMouseUp,oldobj,FreeOldEvent)
    def getOnMouseUp(self):
        return OnMouseUpcall
    OnMouseUp=property(getOnMouseUp,setOnMouseUp)
    def _Warper_OnStartDrag(self,Sender,DragObject):
        self.OnStartDragcall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.GetPytonObject(DragObject,TDragObject))
    def setOnStartDrag(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnStartDragcall'):
            FreeOldEvent=1
            oldobj=OnStartDragPasObject
        self.OnStartDragcall=v 
        self.PasOnStartDrag=FunctionForm(self._Warper_OnStartDrag)
        self.OnStartDragPasObject=LCLBinding.set_StdCtrls_TLabel_OnStartDrag(self.pointer,self.PasOnStartDrag,oldobj,FreeOldEvent)
    def getOnStartDrag(self):
        return OnStartDragcall
    OnStartDrag=property(getOnStartDrag,setOnStartDrag)
    def getOptimalFill(self):
        r=LCLBinding.get_StdCtrls_TLabel_OptimalFill(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setOptimalFill(self,v):
        LCLBinding.set_StdCtrls_TLabel_OptimalFill(self.pointer,v)
    OptimalFill=property(getOptimalFill,setOptimalFill)
#constructorStdCtrls_TLabel_Create
    @staticmethod
    def Create(TheOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.StdCtrls_TLabel_Create((TheOwner.pointer)),TLabel)
#class TLabel end
#class TCustomGroupBox start
class TCustomGroupBox(TWinControl):
#    pointer=c_void_p()
    def __init__(self):#TCustomGroupBox
        TWinControl.__init__(self)
#constructorStdCtrls_TCustomGroupBox_Create
    @staticmethod
    def Create(AOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.StdCtrls_TCustomGroupBox_Create((AOwner.pointer)),TCustomGroupBox)
#class TCustomGroupBox end
#class TGroupBox start
class TGroupBox(TCustomGroupBox):
#    pointer=c_void_p()
    def __init__(self):#TGroupBox
        TCustomGroupBox.__init__(self)
    def getDragKind(self):
        r=LCLBinding.get_StdCtrls_TGroupBox_DragKind(self.pointer)
        return r
    def setDragKind(self,v):
        LCLBinding.set_StdCtrls_TGroupBox_DragKind(self.pointer,v.pointer)
    DragKind=property(getDragKind,setDragKind)
    def getDragMode(self):
        r=LCLBinding.get_StdCtrls_TGroupBox_DragMode(self.pointer)
        return r
    def setDragMode(self,v):
        LCLBinding.set_StdCtrls_TGroupBox_DragMode(self.pointer,v.pointer)
    DragMode=property(getDragMode,setDragMode)
    def getParentColor(self):
        r=LCLBinding.get_StdCtrls_TGroupBox_ParentColor(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentColor(self,v):
        LCLBinding.set_StdCtrls_TGroupBox_ParentColor(self.pointer,v)
    ParentColor=property(getParentColor,setParentColor)
    def getParentFont(self):
        r=LCLBinding.get_StdCtrls_TGroupBox_ParentFont(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentFont(self,v):
        LCLBinding.set_StdCtrls_TGroupBox_ParentFont(self.pointer,v)
    ParentFont=property(getParentFont,setParentFont)
    def getParentShowHint(self):
        r=LCLBinding.get_StdCtrls_TGroupBox_ParentShowHint(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentShowHint(self,v):
        LCLBinding.set_StdCtrls_TGroupBox_ParentShowHint(self.pointer,v)
    ParentShowHint=property(getParentShowHint,setParentShowHint)
    def _Warper_OnDblClick(self,Sender):
        self.OnDblClickcall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnDblClick(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnDblClickcall'):
            FreeOldEvent=1
            oldobj=OnDblClickPasObject
        self.OnDblClickcall=v 
        self.PasOnDblClick=FunctionForm(self._Warper_OnDblClick)
        self.OnDblClickPasObject=LCLBinding.set_StdCtrls_TGroupBox_OnDblClick(self.pointer,self.PasOnDblClick,oldobj,FreeOldEvent)
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
            oldobj=OnDragDropPasObject
        self.OnDragDropcall=v 
        self.PasOnDragDrop=FunctionForm(self._Warper_OnDragDrop)
        self.OnDragDropPasObject=LCLBinding.set_StdCtrls_TGroupBox_OnDragDrop(self.pointer,self.PasOnDragDrop,oldobj,FreeOldEvent)
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
            oldobj=OnDragOverPasObject
        self.OnDragOvercall=v 
        self.PasOnDragOver=FunctionForm(self._Warper_OnDragOver)
        self.OnDragOverPasObject=LCLBinding.set_StdCtrls_TGroupBox_OnDragOver(self.pointer,self.PasOnDragOver,oldobj,FreeOldEvent)
    def getOnDragOver(self):
        return OnDragOvercall
    OnDragOver=property(getOnDragOver,setOnDragOver)
    def _Warper_OnEndDock(self,Sender,Target,X,Y):
        self.OnEndDockcall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.GetPytonObject(Target,TObject),X,Y)
    def setOnEndDock(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnEndDockcall'):
            FreeOldEvent=1
            oldobj=OnEndDockPasObject
        self.OnEndDockcall=v 
        self.PasOnEndDock=FunctionForm(self._Warper_OnEndDock)
        self.OnEndDockPasObject=LCLBinding.set_StdCtrls_TGroupBox_OnEndDock(self.pointer,self.PasOnEndDock,oldobj,FreeOldEvent)
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
            oldobj=OnEndDragPasObject
        self.OnEndDragcall=v 
        self.PasOnEndDrag=FunctionForm(self._Warper_OnEndDrag)
        self.OnEndDragPasObject=LCLBinding.set_StdCtrls_TGroupBox_OnEndDrag(self.pointer,self.PasOnEndDrag,oldobj,FreeOldEvent)
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
            oldobj=OnMouseDownPasObject
        self.OnMouseDowncall=v 
        self.PasOnMouseDown=FunctionForm(self._Warper_OnMouseDown)
        self.OnMouseDownPasObject=LCLBinding.set_StdCtrls_TGroupBox_OnMouseDown(self.pointer,self.PasOnMouseDown,oldobj,FreeOldEvent)
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
            oldobj=OnMouseEnterPasObject
        self.OnMouseEntercall=v 
        self.PasOnMouseEnter=FunctionForm(self._Warper_OnMouseEnter)
        self.OnMouseEnterPasObject=LCLBinding.set_StdCtrls_TGroupBox_OnMouseEnter(self.pointer,self.PasOnMouseEnter,oldobj,FreeOldEvent)
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
            oldobj=OnMouseLeavePasObject
        self.OnMouseLeavecall=v 
        self.PasOnMouseLeave=FunctionForm(self._Warper_OnMouseLeave)
        self.OnMouseLeavePasObject=LCLBinding.set_StdCtrls_TGroupBox_OnMouseLeave(self.pointer,self.PasOnMouseLeave,oldobj,FreeOldEvent)
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
            oldobj=OnMouseMovePasObject
        self.OnMouseMovecall=v 
        self.PasOnMouseMove=FunctionForm(self._Warper_OnMouseMove)
        self.OnMouseMovePasObject=LCLBinding.set_StdCtrls_TGroupBox_OnMouseMove(self.pointer,self.PasOnMouseMove,oldobj,FreeOldEvent)
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
            oldobj=OnMouseUpPasObject
        self.OnMouseUpcall=v 
        self.PasOnMouseUp=FunctionForm(self._Warper_OnMouseUp)
        self.OnMouseUpPasObject=LCLBinding.set_StdCtrls_TGroupBox_OnMouseUp(self.pointer,self.PasOnMouseUp,oldobj,FreeOldEvent)
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
            oldobj=OnStartDockPasObject
        self.OnStartDockcall=v 
        self.PasOnStartDock=FunctionForm(self._Warper_OnStartDock)
        self.OnStartDockPasObject=LCLBinding.set_StdCtrls_TGroupBox_OnStartDock(self.pointer,self.PasOnStartDock,oldobj,FreeOldEvent)
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
            oldobj=OnStartDragPasObject
        self.OnStartDragcall=v 
        self.PasOnStartDrag=FunctionForm(self._Warper_OnStartDrag)
        self.OnStartDragPasObject=LCLBinding.set_StdCtrls_TGroupBox_OnStartDrag(self.pointer,self.PasOnStartDrag,oldobj,FreeOldEvent)
    def getOnStartDrag(self):
        return OnStartDragcall
    OnStartDrag=property(getOnStartDrag,setOnStartDrag)
#constructorStdCtrls_TGroupBox_Create
    @staticmethod
    def Create(AOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.StdCtrls_TGroupBox_Create((AOwner.pointer)),TGroupBox)
#class TGroupBox end
#class TMemoScrollbar start
class TMemoScrollbar(TControlScrollBar):
#    pointer=c_void_p()
    def __init__(self):#TMemoScrollbar
        TControlScrollBar.__init__(self)
#constructorStdCtrls_TMemoScrollbar_Create
    @staticmethod
    def Create(AControl,AKind):
        return LCLBindingUtil.GetPytonObject(LCLBinding.StdCtrls_TMemoScrollbar_Create((AControl.pointer),(AKind.pointer)),TMemoScrollbar)
#class TMemoScrollbar end
#class TCustomEdit start
class TCustomEdit(TWinControl):
#    pointer=c_void_p()
    def __init__(self):#TCustomEdit
        TWinControl.__init__(self)
#constructorStdCtrls_TCustomEdit_Create
    @staticmethod
    def Create(AOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.StdCtrls_TCustomEdit_Create((AOwner.pointer)),TCustomEdit)
    def getAlignment(self):
        r=LCLBinding.get_StdCtrls_TCustomEdit_Alignment(self.pointer)
        return r
    def setAlignment(self,v):
        LCLBinding.set_StdCtrls_TCustomEdit_Alignment(self.pointer,v.pointer)
    Alignment=property(getAlignment,setAlignment)
    def getCanUndo(self):
        r=LCLBinding.get_StdCtrls_TCustomEdit_CanUndo(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    CanUndo=property(getCanUndo)
    def getCharCase(self):
        r=LCLBinding.get_StdCtrls_TCustomEdit_CharCase(self.pointer)
        return r
    def setCharCase(self,v):
        LCLBinding.set_StdCtrls_TCustomEdit_CharCase(self.pointer,v.pointer)
    CharCase=property(getCharCase,setCharCase)
    def getEchoMode(self):
        r=LCLBinding.get_StdCtrls_TCustomEdit_EchoMode(self.pointer)
        return r
    def setEchoMode(self,v):
        LCLBinding.set_StdCtrls_TCustomEdit_EchoMode(self.pointer,v.pointer)
    EchoMode=property(getEchoMode,setEchoMode)
    def getHideSelection(self):
        r=LCLBinding.get_StdCtrls_TCustomEdit_HideSelection(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setHideSelection(self,v):
        LCLBinding.set_StdCtrls_TCustomEdit_HideSelection(self.pointer,v)
    HideSelection=property(getHideSelection,setHideSelection)
    def getMaxLength(self):
        r=LCLBinding.get_StdCtrls_TCustomEdit_MaxLength(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setMaxLength(self,v):
        LCLBinding.set_StdCtrls_TCustomEdit_MaxLength(self.pointer,v)
    MaxLength=property(getMaxLength,setMaxLength)
    def getModified(self):
        r=LCLBinding.get_StdCtrls_TCustomEdit_Modified(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setModified(self,v):
        LCLBinding.set_StdCtrls_TCustomEdit_Modified(self.pointer,v)
    Modified=property(getModified,setModified)
    def getNumbersOnly(self):
        r=LCLBinding.get_StdCtrls_TCustomEdit_NumbersOnly(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setNumbersOnly(self,v):
        LCLBinding.set_StdCtrls_TCustomEdit_NumbersOnly(self.pointer,v)
    NumbersOnly=property(getNumbersOnly,setNumbersOnly)
    def _Warper_OnChange(self,Sender):
        self.OnChangecall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnChange(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnChangecall'):
            FreeOldEvent=1
            oldobj=OnChangePasObject
        self.OnChangecall=v 
        self.PasOnChange=FunctionForm(self._Warper_OnChange)
        self.OnChangePasObject=LCLBinding.set_StdCtrls_TCustomEdit_OnChange(self.pointer,self.PasOnChange,oldobj,FreeOldEvent)
    def getOnChange(self):
        return OnChangecall
    OnChange=property(getOnChange,setOnChange)
    def getReadOnly(self):
        r=LCLBinding.get_StdCtrls_TCustomEdit_ReadOnly(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setReadOnly(self,v):
        LCLBinding.set_StdCtrls_TCustomEdit_ReadOnly(self.pointer,v)
    ReadOnly=property(getReadOnly,setReadOnly)
    def getSelLength(self):
        r=LCLBinding.get_StdCtrls_TCustomEdit_SelLength(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setSelLength(self,v):
        LCLBinding.set_StdCtrls_TCustomEdit_SelLength(self.pointer,v)
    SelLength=property(getSelLength,setSelLength)
    def getSelStart(self):
        r=LCLBinding.get_StdCtrls_TCustomEdit_SelStart(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setSelStart(self,v):
        LCLBinding.set_StdCtrls_TCustomEdit_SelStart(self.pointer,v)
    SelStart=property(getSelStart,setSelStart)
    def getSelText(self):
        r=LCLBinding.get_StdCtrls_TCustomEdit_SelText(self.pointer)
        return LCLBindingUtil.ConvertPascalstring(r)
    def setSelText(self,v):
        LCLBinding.set_StdCtrls_TCustomEdit_SelText(self.pointer,v)
    SelText=property(getSelText,setSelText)
    def getText(self):
        r=LCLBinding.get_StdCtrls_TCustomEdit_Text(self.pointer)
        return LCLBindingUtil.ConvertPascalTCaption(r)
    def setText(self,v):
        LCLBinding.set_StdCtrls_TCustomEdit_Text(self.pointer,v)
    Text=property(getText,setText)
    def getTextHintFontStyle(self):
        r=LCLBinding.get_StdCtrls_TCustomEdit_TextHintFontStyle(self.pointer)
        return r
    def setTextHintFontStyle(self,v):
        LCLBinding.set_StdCtrls_TCustomEdit_TextHintFontStyle(self.pointer,v.pointer)
    TextHintFontStyle=property(getTextHintFontStyle,setTextHintFontStyle)
#class TCustomEdit end
#class TCustomMemo start
class TCustomMemo(TCustomEdit):
#    pointer=c_void_p()
    def __init__(self):#TCustomMemo
        TCustomEdit.__init__(self)
#constructorStdCtrls_TCustomMemo_Create
    @staticmethod
    def Create(AOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.StdCtrls_TCustomMemo_Create((AOwner.pointer)),TCustomMemo)
    def getLines(self):
        r=LCLBinding.get_StdCtrls_TCustomMemo_Lines(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TStrings)
    def setLines(self,v):
        LCLBinding.set_StdCtrls_TCustomMemo_Lines(self.pointer,v.pointer)
    Lines=property(getLines,setLines)
    def getHorzScrollBar(self):
        r=LCLBinding.get_StdCtrls_TCustomMemo_HorzScrollBar(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TMemoScrollBar)
    def setHorzScrollBar(self,v):
        LCLBinding.set_StdCtrls_TCustomMemo_HorzScrollBar(self.pointer,v.pointer)
    HorzScrollBar=property(getHorzScrollBar,setHorzScrollBar)
    def getVertScrollBar(self):
        r=LCLBinding.get_StdCtrls_TCustomMemo_VertScrollBar(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TMemoScrollBar)
    def setVertScrollBar(self,v):
        LCLBinding.set_StdCtrls_TCustomMemo_VertScrollBar(self.pointer,v.pointer)
    VertScrollBar=property(getVertScrollBar,setVertScrollBar)
    def getScrollBars(self):
        r=LCLBinding.get_StdCtrls_TCustomMemo_ScrollBars(self.pointer)
        return r
    def setScrollBars(self,v):
        LCLBinding.set_StdCtrls_TCustomMemo_ScrollBars(self.pointer,v.pointer)
    ScrollBars=property(getScrollBars,setScrollBars)
    def getWantReturns(self):
        r=LCLBinding.get_StdCtrls_TCustomMemo_WantReturns(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setWantReturns(self,v):
        LCLBinding.set_StdCtrls_TCustomMemo_WantReturns(self.pointer,v)
    WantReturns=property(getWantReturns,setWantReturns)
    def getWantTabs(self):
        r=LCLBinding.get_StdCtrls_TCustomMemo_WantTabs(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setWantTabs(self,v):
        LCLBinding.set_StdCtrls_TCustomMemo_WantTabs(self.pointer,v)
    WantTabs=property(getWantTabs,setWantTabs)
    def getWordWrap(self):
        r=LCLBinding.get_StdCtrls_TCustomMemo_WordWrap(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setWordWrap(self,v):
        LCLBinding.set_StdCtrls_TCustomMemo_WordWrap(self.pointer,v)
    WordWrap=property(getWordWrap,setWordWrap)
#class TCustomMemo end
#class TMemo start
class TMemo(TCustomMemo):
#    pointer=c_void_p()
    def __init__(self):#TMemo
        TCustomMemo.__init__(self)
    def getDragKind(self):
        r=LCLBinding.get_StdCtrls_TMemo_DragKind(self.pointer)
        return r
    def setDragKind(self,v):
        LCLBinding.set_StdCtrls_TMemo_DragKind(self.pointer,v.pointer)
    DragKind=property(getDragKind,setDragKind)
    def getDragMode(self):
        r=LCLBinding.get_StdCtrls_TMemo_DragMode(self.pointer)
        return r
    def setDragMode(self,v):
        LCLBinding.set_StdCtrls_TMemo_DragMode(self.pointer,v.pointer)
    DragMode=property(getDragMode,setDragMode)
    def _Warper_OnDblClick(self,Sender):
        self.OnDblClickcall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnDblClick(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnDblClickcall'):
            FreeOldEvent=1
            oldobj=OnDblClickPasObject
        self.OnDblClickcall=v 
        self.PasOnDblClick=FunctionForm(self._Warper_OnDblClick)
        self.OnDblClickPasObject=LCLBinding.set_StdCtrls_TMemo_OnDblClick(self.pointer,self.PasOnDblClick,oldobj,FreeOldEvent)
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
            oldobj=OnDragDropPasObject
        self.OnDragDropcall=v 
        self.PasOnDragDrop=FunctionForm(self._Warper_OnDragDrop)
        self.OnDragDropPasObject=LCLBinding.set_StdCtrls_TMemo_OnDragDrop(self.pointer,self.PasOnDragDrop,oldobj,FreeOldEvent)
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
            oldobj=OnDragOverPasObject
        self.OnDragOvercall=v 
        self.PasOnDragOver=FunctionForm(self._Warper_OnDragOver)
        self.OnDragOverPasObject=LCLBinding.set_StdCtrls_TMemo_OnDragOver(self.pointer,self.PasOnDragOver,oldobj,FreeOldEvent)
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
            oldobj=OnEditingDonePasObject
        self.OnEditingDonecall=v 
        self.PasOnEditingDone=FunctionForm(self._Warper_OnEditingDone)
        self.OnEditingDonePasObject=LCLBinding.set_StdCtrls_TMemo_OnEditingDone(self.pointer,self.PasOnEditingDone,oldobj,FreeOldEvent)
    def getOnEditingDone(self):
        return OnEditingDonecall
    OnEditingDone=property(getOnEditingDone,setOnEditingDone)
    def _Warper_OnEndDrag(self,Sender,Target,X,Y):
        self.OnEndDragcall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.GetPytonObject(Target,TObject),X,Y)
    def setOnEndDrag(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnEndDragcall'):
            FreeOldEvent=1
            oldobj=OnEndDragPasObject
        self.OnEndDragcall=v 
        self.PasOnEndDrag=FunctionForm(self._Warper_OnEndDrag)
        self.OnEndDragPasObject=LCLBinding.set_StdCtrls_TMemo_OnEndDrag(self.pointer,self.PasOnEndDrag,oldobj,FreeOldEvent)
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
            oldobj=OnMouseDownPasObject
        self.OnMouseDowncall=v 
        self.PasOnMouseDown=FunctionForm(self._Warper_OnMouseDown)
        self.OnMouseDownPasObject=LCLBinding.set_StdCtrls_TMemo_OnMouseDown(self.pointer,self.PasOnMouseDown,oldobj,FreeOldEvent)
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
            oldobj=OnMouseEnterPasObject
        self.OnMouseEntercall=v 
        self.PasOnMouseEnter=FunctionForm(self._Warper_OnMouseEnter)
        self.OnMouseEnterPasObject=LCLBinding.set_StdCtrls_TMemo_OnMouseEnter(self.pointer,self.PasOnMouseEnter,oldobj,FreeOldEvent)
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
            oldobj=OnMouseLeavePasObject
        self.OnMouseLeavecall=v 
        self.PasOnMouseLeave=FunctionForm(self._Warper_OnMouseLeave)
        self.OnMouseLeavePasObject=LCLBinding.set_StdCtrls_TMemo_OnMouseLeave(self.pointer,self.PasOnMouseLeave,oldobj,FreeOldEvent)
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
            oldobj=OnMouseMovePasObject
        self.OnMouseMovecall=v 
        self.PasOnMouseMove=FunctionForm(self._Warper_OnMouseMove)
        self.OnMouseMovePasObject=LCLBinding.set_StdCtrls_TMemo_OnMouseMove(self.pointer,self.PasOnMouseMove,oldobj,FreeOldEvent)
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
            oldobj=OnMouseUpPasObject
        self.OnMouseUpcall=v 
        self.PasOnMouseUp=FunctionForm(self._Warper_OnMouseUp)
        self.OnMouseUpPasObject=LCLBinding.set_StdCtrls_TMemo_OnMouseUp(self.pointer,self.PasOnMouseUp,oldobj,FreeOldEvent)
    def getOnMouseUp(self):
        return OnMouseUpcall
    OnMouseUp=property(getOnMouseUp,setOnMouseUp)
    def _Warper_OnStartDrag(self,Sender,DragObject):
        self.OnStartDragcall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.GetPytonObject(DragObject,TDragObject))
    def setOnStartDrag(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnStartDragcall'):
            FreeOldEvent=1
            oldobj=OnStartDragPasObject
        self.OnStartDragcall=v 
        self.PasOnStartDrag=FunctionForm(self._Warper_OnStartDrag)
        self.OnStartDragPasObject=LCLBinding.set_StdCtrls_TMemo_OnStartDrag(self.pointer,self.PasOnStartDrag,oldobj,FreeOldEvent)
    def getOnStartDrag(self):
        return OnStartDragcall
    OnStartDrag=property(getOnStartDrag,setOnStartDrag)
    def getParentColor(self):
        r=LCLBinding.get_StdCtrls_TMemo_ParentColor(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentColor(self,v):
        LCLBinding.set_StdCtrls_TMemo_ParentColor(self.pointer,v)
    ParentColor=property(getParentColor,setParentColor)
    def getParentFont(self):
        r=LCLBinding.get_StdCtrls_TMemo_ParentFont(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentFont(self,v):
        LCLBinding.set_StdCtrls_TMemo_ParentFont(self.pointer,v)
    ParentFont=property(getParentFont,setParentFont)
    def getParentShowHint(self):
        r=LCLBinding.get_StdCtrls_TMemo_ParentShowHint(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentShowHint(self,v):
        LCLBinding.set_StdCtrls_TMemo_ParentShowHint(self.pointer,v)
    ParentShowHint=property(getParentShowHint,setParentShowHint)
#constructorStdCtrls_TMemo_Create
    @staticmethod
    def Create(AOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.StdCtrls_TMemo_Create((AOwner.pointer)),TMemo)
#class TMemo end
#class TEdit start
class TEdit(TCustomEdit):
#    pointer=c_void_p()
    def __init__(self):#TEdit
        TCustomEdit.__init__(self)
    def getAutoSelected(self):
        r=LCLBinding.get_StdCtrls_TEdit_AutoSelected(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setAutoSelected(self,v):
        LCLBinding.set_StdCtrls_TEdit_AutoSelected(self.pointer,v)
    AutoSelected=property(getAutoSelected,setAutoSelected)
    def getAutoSelect(self):
        r=LCLBinding.get_StdCtrls_TEdit_AutoSelect(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setAutoSelect(self,v):
        LCLBinding.set_StdCtrls_TEdit_AutoSelect(self.pointer,v)
    AutoSelect=property(getAutoSelect,setAutoSelect)
    def getDragKind(self):
        r=LCLBinding.get_StdCtrls_TEdit_DragKind(self.pointer)
        return r
    def setDragKind(self,v):
        LCLBinding.set_StdCtrls_TEdit_DragKind(self.pointer,v.pointer)
    DragKind=property(getDragKind,setDragKind)
    def getDragMode(self):
        r=LCLBinding.get_StdCtrls_TEdit_DragMode(self.pointer)
        return r
    def setDragMode(self,v):
        LCLBinding.set_StdCtrls_TEdit_DragMode(self.pointer,v.pointer)
    DragMode=property(getDragMode,setDragMode)
    def _Warper_OnDblClick(self,Sender):
        self.OnDblClickcall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnDblClick(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnDblClickcall'):
            FreeOldEvent=1
            oldobj=OnDblClickPasObject
        self.OnDblClickcall=v 
        self.PasOnDblClick=FunctionForm(self._Warper_OnDblClick)
        self.OnDblClickPasObject=LCLBinding.set_StdCtrls_TEdit_OnDblClick(self.pointer,self.PasOnDblClick,oldobj,FreeOldEvent)
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
            oldobj=OnDragDropPasObject
        self.OnDragDropcall=v 
        self.PasOnDragDrop=FunctionForm(self._Warper_OnDragDrop)
        self.OnDragDropPasObject=LCLBinding.set_StdCtrls_TEdit_OnDragDrop(self.pointer,self.PasOnDragDrop,oldobj,FreeOldEvent)
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
            oldobj=OnDragOverPasObject
        self.OnDragOvercall=v 
        self.PasOnDragOver=FunctionForm(self._Warper_OnDragOver)
        self.OnDragOverPasObject=LCLBinding.set_StdCtrls_TEdit_OnDragOver(self.pointer,self.PasOnDragOver,oldobj,FreeOldEvent)
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
            oldobj=OnEditingDonePasObject
        self.OnEditingDonecall=v 
        self.PasOnEditingDone=FunctionForm(self._Warper_OnEditingDone)
        self.OnEditingDonePasObject=LCLBinding.set_StdCtrls_TEdit_OnEditingDone(self.pointer,self.PasOnEditingDone,oldobj,FreeOldEvent)
    def getOnEditingDone(self):
        return OnEditingDonecall
    OnEditingDone=property(getOnEditingDone,setOnEditingDone)
    def _Warper_OnEndDrag(self,Sender,Target,X,Y):
        self.OnEndDragcall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.GetPytonObject(Target,TObject),X,Y)
    def setOnEndDrag(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnEndDragcall'):
            FreeOldEvent=1
            oldobj=OnEndDragPasObject
        self.OnEndDragcall=v 
        self.PasOnEndDrag=FunctionForm(self._Warper_OnEndDrag)
        self.OnEndDragPasObject=LCLBinding.set_StdCtrls_TEdit_OnEndDrag(self.pointer,self.PasOnEndDrag,oldobj,FreeOldEvent)
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
            oldobj=OnMouseDownPasObject
        self.OnMouseDowncall=v 
        self.PasOnMouseDown=FunctionForm(self._Warper_OnMouseDown)
        self.OnMouseDownPasObject=LCLBinding.set_StdCtrls_TEdit_OnMouseDown(self.pointer,self.PasOnMouseDown,oldobj,FreeOldEvent)
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
            oldobj=OnMouseEnterPasObject
        self.OnMouseEntercall=v 
        self.PasOnMouseEnter=FunctionForm(self._Warper_OnMouseEnter)
        self.OnMouseEnterPasObject=LCLBinding.set_StdCtrls_TEdit_OnMouseEnter(self.pointer,self.PasOnMouseEnter,oldobj,FreeOldEvent)
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
            oldobj=OnMouseLeavePasObject
        self.OnMouseLeavecall=v 
        self.PasOnMouseLeave=FunctionForm(self._Warper_OnMouseLeave)
        self.OnMouseLeavePasObject=LCLBinding.set_StdCtrls_TEdit_OnMouseLeave(self.pointer,self.PasOnMouseLeave,oldobj,FreeOldEvent)
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
            oldobj=OnMouseMovePasObject
        self.OnMouseMovecall=v 
        self.PasOnMouseMove=FunctionForm(self._Warper_OnMouseMove)
        self.OnMouseMovePasObject=LCLBinding.set_StdCtrls_TEdit_OnMouseMove(self.pointer,self.PasOnMouseMove,oldobj,FreeOldEvent)
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
            oldobj=OnMouseUpPasObject
        self.OnMouseUpcall=v 
        self.PasOnMouseUp=FunctionForm(self._Warper_OnMouseUp)
        self.OnMouseUpPasObject=LCLBinding.set_StdCtrls_TEdit_OnMouseUp(self.pointer,self.PasOnMouseUp,oldobj,FreeOldEvent)
    def getOnMouseUp(self):
        return OnMouseUpcall
    OnMouseUp=property(getOnMouseUp,setOnMouseUp)
    def _Warper_OnStartDrag(self,Sender,DragObject):
        self.OnStartDragcall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.GetPytonObject(DragObject,TDragObject))
    def setOnStartDrag(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnStartDragcall'):
            FreeOldEvent=1
            oldobj=OnStartDragPasObject
        self.OnStartDragcall=v 
        self.PasOnStartDrag=FunctionForm(self._Warper_OnStartDrag)
        self.OnStartDragPasObject=LCLBinding.set_StdCtrls_TEdit_OnStartDrag(self.pointer,self.PasOnStartDrag,oldobj,FreeOldEvent)
    def getOnStartDrag(self):
        return OnStartDragcall
    OnStartDrag=property(getOnStartDrag,setOnStartDrag)
    def getParentColor(self):
        r=LCLBinding.get_StdCtrls_TEdit_ParentColor(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentColor(self,v):
        LCLBinding.set_StdCtrls_TEdit_ParentColor(self.pointer,v)
    ParentColor=property(getParentColor,setParentColor)
    def getParentFont(self):
        r=LCLBinding.get_StdCtrls_TEdit_ParentFont(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentFont(self,v):
        LCLBinding.set_StdCtrls_TEdit_ParentFont(self.pointer,v)
    ParentFont=property(getParentFont,setParentFont)
    def getParentShowHint(self):
        r=LCLBinding.get_StdCtrls_TEdit_ParentShowHint(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentShowHint(self,v):
        LCLBinding.set_StdCtrls_TEdit_ParentShowHint(self.pointer,v)
    ParentShowHint=property(getParentShowHint,setParentShowHint)
#constructorStdCtrls_TEdit_Create
    @staticmethod
    def Create(AOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.StdCtrls_TEdit_Create((AOwner.pointer)),TEdit)
#class TEdit end
#class TCustomComboBox start
class TCustomComboBox(TWinControl):
#    pointer=c_void_p()
    def __init__(self):#TCustomComboBox
        TWinControl.__init__(self)
#constructorStdCtrls_TCustomComboBox_Create
    @staticmethod
    def Create(TheOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.StdCtrls_TCustomComboBox_Create((TheOwner.pointer)),TCustomComboBox)
    def getCharCase(self):
        r=LCLBinding.get_StdCtrls_TCustomComboBox_CharCase(self.pointer)
        return r
    def setCharCase(self,v):
        LCLBinding.set_StdCtrls_TCustomComboBox_CharCase(self.pointer,v.pointer)
    CharCase=property(getCharCase,setCharCase)
    def getDroppedDown(self):
        r=LCLBinding.get_StdCtrls_TCustomComboBox_DroppedDown(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setDroppedDown(self,v):
        LCLBinding.set_StdCtrls_TCustomComboBox_DroppedDown(self.pointer,v)
    DroppedDown=property(getDroppedDown,setDroppedDown)
    def getDroppingDown(self):
        r=LCLBinding.get_StdCtrls_TCustomComboBox_DroppingDown(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setDroppingDown(self,v):
        LCLBinding.set_StdCtrls_TCustomComboBox_DroppingDown(self.pointer,v)
    DroppingDown=property(getDroppingDown,setDroppingDown)
    def getAutoComplete(self):
        r=LCLBinding.get_StdCtrls_TCustomComboBox_AutoComplete(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setAutoComplete(self,v):
        LCLBinding.set_StdCtrls_TCustomComboBox_AutoComplete(self.pointer,v)
    AutoComplete=property(getAutoComplete,setAutoComplete)
    def getAutoCompleteText(self):
        r=LCLBinding.get_StdCtrls_TCustomComboBox_AutoCompleteText(self.pointer)
        return r
    def setAutoCompleteText(self,v):
        LCLBinding.set_StdCtrls_TCustomComboBox_AutoCompleteText(self.pointer,v.pointer)
    AutoCompleteText=property(getAutoCompleteText,setAutoCompleteText)
    def getAutoDropDown(self):
        r=LCLBinding.get_StdCtrls_TCustomComboBox_AutoDropDown(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setAutoDropDown(self,v):
        LCLBinding.set_StdCtrls_TCustomComboBox_AutoDropDown(self.pointer,v)
    AutoDropDown=property(getAutoDropDown,setAutoDropDown)
    def getAutoSelect(self):
        r=LCLBinding.get_StdCtrls_TCustomComboBox_AutoSelect(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setAutoSelect(self,v):
        LCLBinding.set_StdCtrls_TCustomComboBox_AutoSelect(self.pointer,v)
    AutoSelect=property(getAutoSelect,setAutoSelect)
    def getAutoSelected(self):
        r=LCLBinding.get_StdCtrls_TCustomComboBox_AutoSelected(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setAutoSelected(self,v):
        LCLBinding.set_StdCtrls_TCustomComboBox_AutoSelected(self.pointer,v)
    AutoSelected=property(getAutoSelected,setAutoSelected)
    def getArrowKeysTraverseList(self):
        r=LCLBinding.get_StdCtrls_TCustomComboBox_ArrowKeysTraverseList(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setArrowKeysTraverseList(self,v):
        LCLBinding.set_StdCtrls_TCustomComboBox_ArrowKeysTraverseList(self.pointer,v)
    ArrowKeysTraverseList=property(getArrowKeysTraverseList,setArrowKeysTraverseList)
    def getCanvas(self):
        r=LCLBinding.get_StdCtrls_TCustomComboBox_Canvas(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TCanvas)
    Canvas=property(getCanvas)
    def getDropDownCount(self):
        r=LCLBinding.get_StdCtrls_TCustomComboBox_DropDownCount(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setDropDownCount(self,v):
        LCLBinding.set_StdCtrls_TCustomComboBox_DropDownCount(self.pointer,v)
    DropDownCount=property(getDropDownCount,setDropDownCount)
    def getItems(self):
        r=LCLBinding.get_StdCtrls_TCustomComboBox_Items(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TStrings)
    def setItems(self,v):
        LCLBinding.set_StdCtrls_TCustomComboBox_Items(self.pointer,v.pointer)
    Items=property(getItems,setItems)
    def getItemIndex(self):
        r=LCLBinding.get_StdCtrls_TCustomComboBox_ItemIndex(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setItemIndex(self,v):
        LCLBinding.set_StdCtrls_TCustomComboBox_ItemIndex(self.pointer,v)
    ItemIndex=property(getItemIndex,setItemIndex)
    def getReadOnly(self):
        r=LCLBinding.get_StdCtrls_TCustomComboBox_ReadOnly(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setReadOnly(self,v):
        LCLBinding.set_StdCtrls_TCustomComboBox_ReadOnly(self.pointer,v)
    ReadOnly=property(getReadOnly,setReadOnly)
    def getSelLength(self):
        r=LCLBinding.get_StdCtrls_TCustomComboBox_SelLength(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setSelLength(self,v):
        LCLBinding.set_StdCtrls_TCustomComboBox_SelLength(self.pointer,v)
    SelLength=property(getSelLength,setSelLength)
    def getSelStart(self):
        r=LCLBinding.get_StdCtrls_TCustomComboBox_SelStart(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setSelStart(self,v):
        LCLBinding.set_StdCtrls_TCustomComboBox_SelStart(self.pointer,v)
    SelStart=property(getSelStart,setSelStart)
    def getSelText(self):
        r=LCLBinding.get_StdCtrls_TCustomComboBox_SelText(self.pointer)
        return LCLBindingUtil.ConvertPascalstring(r)
    def setSelText(self,v):
        LCLBinding.set_StdCtrls_TCustomComboBox_SelText(self.pointer,v)
    SelText=property(getSelText,setSelText)
    def getStyle(self):
        r=LCLBinding.get_StdCtrls_TCustomComboBox_Style(self.pointer)
        return r
    def setStyle(self,v):
        LCLBinding.set_StdCtrls_TCustomComboBox_Style(self.pointer,v.pointer)
    Style=property(getStyle,setStyle)
    def getText(self):
        r=LCLBinding.get_StdCtrls_TCustomComboBox_Text(self.pointer)
        return LCLBindingUtil.ConvertPascalTCaption(r)
    def setText(self,v):
        LCLBinding.set_StdCtrls_TCustomComboBox_Text(self.pointer,v)
    Text=property(getText,setText)
#class TCustomComboBox end
#class TComboBox start
class TComboBox(TCustomComboBox):
#    pointer=c_void_p()
    def __init__(self):#TComboBox
        TCustomComboBox.__init__(self)
    def getDragKind(self):
        r=LCLBinding.get_StdCtrls_TComboBox_DragKind(self.pointer)
        return r
    def setDragKind(self,v):
        LCLBinding.set_StdCtrls_TComboBox_DragKind(self.pointer,v.pointer)
    DragKind=property(getDragKind,setDragKind)
    def getDragMode(self):
        r=LCLBinding.get_StdCtrls_TComboBox_DragMode(self.pointer)
        return r
    def setDragMode(self,v):
        LCLBinding.set_StdCtrls_TComboBox_DragMode(self.pointer,v.pointer)
    DragMode=property(getDragMode,setDragMode)
    def getItemHeight(self):
        r=LCLBinding.get_StdCtrls_TComboBox_ItemHeight(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setItemHeight(self,v):
        LCLBinding.set_StdCtrls_TComboBox_ItemHeight(self.pointer,v)
    ItemHeight=property(getItemHeight,setItemHeight)
    def getItemWidth(self):
        r=LCLBinding.get_StdCtrls_TComboBox_ItemWidth(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setItemWidth(self,v):
        LCLBinding.set_StdCtrls_TComboBox_ItemWidth(self.pointer,v)
    ItemWidth=property(getItemWidth,setItemWidth)
    def getMaxLength(self):
        r=LCLBinding.get_StdCtrls_TComboBox_MaxLength(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setMaxLength(self,v):
        LCLBinding.set_StdCtrls_TComboBox_MaxLength(self.pointer,v)
    MaxLength=property(getMaxLength,setMaxLength)
    def _Warper_OnChange(self,Sender):
        self.OnChangecall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnChange(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnChangecall'):
            FreeOldEvent=1
            oldobj=OnChangePasObject
        self.OnChangecall=v 
        self.PasOnChange=FunctionForm(self._Warper_OnChange)
        self.OnChangePasObject=LCLBinding.set_StdCtrls_TComboBox_OnChange(self.pointer,self.PasOnChange,oldobj,FreeOldEvent)
    def getOnChange(self):
        return OnChangecall
    OnChange=property(getOnChange,setOnChange)
    def _Warper_OnCloseUp(self,Sender):
        self.OnCloseUpcall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnCloseUp(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnCloseUpcall'):
            FreeOldEvent=1
            oldobj=OnCloseUpPasObject
        self.OnCloseUpcall=v 
        self.PasOnCloseUp=FunctionForm(self._Warper_OnCloseUp)
        self.OnCloseUpPasObject=LCLBinding.set_StdCtrls_TComboBox_OnCloseUp(self.pointer,self.PasOnCloseUp,oldobj,FreeOldEvent)
    def getOnCloseUp(self):
        return OnCloseUpcall
    OnCloseUp=property(getOnCloseUp,setOnCloseUp)
    def _Warper_OnDblClick(self,Sender):
        self.OnDblClickcall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnDblClick(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnDblClickcall'):
            FreeOldEvent=1
            oldobj=OnDblClickPasObject
        self.OnDblClickcall=v 
        self.PasOnDblClick=FunctionForm(self._Warper_OnDblClick)
        self.OnDblClickPasObject=LCLBinding.set_StdCtrls_TComboBox_OnDblClick(self.pointer,self.PasOnDblClick,oldobj,FreeOldEvent)
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
            oldobj=OnDragDropPasObject
        self.OnDragDropcall=v 
        self.PasOnDragDrop=FunctionForm(self._Warper_OnDragDrop)
        self.OnDragDropPasObject=LCLBinding.set_StdCtrls_TComboBox_OnDragDrop(self.pointer,self.PasOnDragDrop,oldobj,FreeOldEvent)
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
            oldobj=OnDragOverPasObject
        self.OnDragOvercall=v 
        self.PasOnDragOver=FunctionForm(self._Warper_OnDragOver)
        self.OnDragOverPasObject=LCLBinding.set_StdCtrls_TComboBox_OnDragOver(self.pointer,self.PasOnDragOver,oldobj,FreeOldEvent)
    def getOnDragOver(self):
        return OnDragOvercall
    OnDragOver=property(getOnDragOver,setOnDragOver)
    def _Warper_OnEndDrag(self,Sender,Target,X,Y):
        self.OnEndDragcall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.GetPytonObject(Target,TObject),X,Y)
    def setOnEndDrag(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnEndDragcall'):
            FreeOldEvent=1
            oldobj=OnEndDragPasObject
        self.OnEndDragcall=v 
        self.PasOnEndDrag=FunctionForm(self._Warper_OnEndDrag)
        self.OnEndDragPasObject=LCLBinding.set_StdCtrls_TComboBox_OnEndDrag(self.pointer,self.PasOnEndDrag,oldobj,FreeOldEvent)
    def getOnEndDrag(self):
        return OnEndDragcall
    OnEndDrag=property(getOnEndDrag,setOnEndDrag)
    def _Warper_OnDropDown(self,Sender):
        self.OnDropDowncall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnDropDown(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnDropDowncall'):
            FreeOldEvent=1
            oldobj=OnDropDownPasObject
        self.OnDropDowncall=v 
        self.PasOnDropDown=FunctionForm(self._Warper_OnDropDown)
        self.OnDropDownPasObject=LCLBinding.set_StdCtrls_TComboBox_OnDropDown(self.pointer,self.PasOnDropDown,oldobj,FreeOldEvent)
    def getOnDropDown(self):
        return OnDropDowncall
    OnDropDown=property(getOnDropDown,setOnDropDown)
    def _Warper_OnEditingDone(self,Sender):
        self.OnEditingDonecall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnEditingDone(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnEditingDonecall'):
            FreeOldEvent=1
            oldobj=OnEditingDonePasObject
        self.OnEditingDonecall=v 
        self.PasOnEditingDone=FunctionForm(self._Warper_OnEditingDone)
        self.OnEditingDonePasObject=LCLBinding.set_StdCtrls_TComboBox_OnEditingDone(self.pointer,self.PasOnEditingDone,oldobj,FreeOldEvent)
    def getOnEditingDone(self):
        return OnEditingDonecall
    OnEditingDone=property(getOnEditingDone,setOnEditingDone)
    def _Warper_OnGetItems(self,Sender):
        self.OnGetItemscall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnGetItems(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnGetItemscall'):
            FreeOldEvent=1
            oldobj=OnGetItemsPasObject
        self.OnGetItemscall=v 
        self.PasOnGetItems=FunctionForm(self._Warper_OnGetItems)
        self.OnGetItemsPasObject=LCLBinding.set_StdCtrls_TComboBox_OnGetItems(self.pointer,self.PasOnGetItems,oldobj,FreeOldEvent)
    def getOnGetItems(self):
        return OnGetItemscall
    OnGetItems=property(getOnGetItems,setOnGetItems)
    def _Warper_OnMeasureItem(self,Control,Index,AHeight):
        self.OnMeasureItemcall(LCLBindingUtil.GetPytonObject(Control,TWinControl),Index,AHeight)
    def setOnMeasureItem(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnMeasureItemcall'):
            FreeOldEvent=1
            oldobj=OnMeasureItemPasObject
        self.OnMeasureItemcall=v 
        self.PasOnMeasureItem=FunctionForm(self._Warper_OnMeasureItem)
        self.OnMeasureItemPasObject=LCLBinding.set_StdCtrls_TComboBox_OnMeasureItem(self.pointer,self.PasOnMeasureItem,oldobj,FreeOldEvent)
    def getOnMeasureItem(self):
        return OnMeasureItemcall
    OnMeasureItem=property(getOnMeasureItem,setOnMeasureItem)
    def _Warper_OnMouseDown(self,Sender,Button,Shift,X,Y):
        self.OnMouseDowncall(LCLBindingUtil.GetPytonObject(Sender,TObject),Button,Shift,X,Y)
    def setOnMouseDown(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int,c_int,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnMouseDowncall'):
            FreeOldEvent=1
            oldobj=OnMouseDownPasObject
        self.OnMouseDowncall=v 
        self.PasOnMouseDown=FunctionForm(self._Warper_OnMouseDown)
        self.OnMouseDownPasObject=LCLBinding.set_StdCtrls_TComboBox_OnMouseDown(self.pointer,self.PasOnMouseDown,oldobj,FreeOldEvent)
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
            oldobj=OnMouseEnterPasObject
        self.OnMouseEntercall=v 
        self.PasOnMouseEnter=FunctionForm(self._Warper_OnMouseEnter)
        self.OnMouseEnterPasObject=LCLBinding.set_StdCtrls_TComboBox_OnMouseEnter(self.pointer,self.PasOnMouseEnter,oldobj,FreeOldEvent)
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
            oldobj=OnMouseLeavePasObject
        self.OnMouseLeavecall=v 
        self.PasOnMouseLeave=FunctionForm(self._Warper_OnMouseLeave)
        self.OnMouseLeavePasObject=LCLBinding.set_StdCtrls_TComboBox_OnMouseLeave(self.pointer,self.PasOnMouseLeave,oldobj,FreeOldEvent)
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
            oldobj=OnMouseMovePasObject
        self.OnMouseMovecall=v 
        self.PasOnMouseMove=FunctionForm(self._Warper_OnMouseMove)
        self.OnMouseMovePasObject=LCLBinding.set_StdCtrls_TComboBox_OnMouseMove(self.pointer,self.PasOnMouseMove,oldobj,FreeOldEvent)
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
            oldobj=OnMouseUpPasObject
        self.OnMouseUpcall=v 
        self.PasOnMouseUp=FunctionForm(self._Warper_OnMouseUp)
        self.OnMouseUpPasObject=LCLBinding.set_StdCtrls_TComboBox_OnMouseUp(self.pointer,self.PasOnMouseUp,oldobj,FreeOldEvent)
    def getOnMouseUp(self):
        return OnMouseUpcall
    OnMouseUp=property(getOnMouseUp,setOnMouseUp)
    def _Warper_OnSelect(self,Sender):
        self.OnSelectcall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnSelect(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnSelectcall'):
            FreeOldEvent=1
            oldobj=OnSelectPasObject
        self.OnSelectcall=v 
        self.PasOnSelect=FunctionForm(self._Warper_OnSelect)
        self.OnSelectPasObject=LCLBinding.set_StdCtrls_TComboBox_OnSelect(self.pointer,self.PasOnSelect,oldobj,FreeOldEvent)
    def getOnSelect(self):
        return OnSelectcall
    OnSelect=property(getOnSelect,setOnSelect)
    def _Warper_OnStartDrag(self,Sender,DragObject):
        self.OnStartDragcall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.GetPytonObject(DragObject,TDragObject))
    def setOnStartDrag(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnStartDragcall'):
            FreeOldEvent=1
            oldobj=OnStartDragPasObject
        self.OnStartDragcall=v 
        self.PasOnStartDrag=FunctionForm(self._Warper_OnStartDrag)
        self.OnStartDragPasObject=LCLBinding.set_StdCtrls_TComboBox_OnStartDrag(self.pointer,self.PasOnStartDrag,oldobj,FreeOldEvent)
    def getOnStartDrag(self):
        return OnStartDragcall
    OnStartDrag=property(getOnStartDrag,setOnStartDrag)
    def getParentColor(self):
        r=LCLBinding.get_StdCtrls_TComboBox_ParentColor(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentColor(self,v):
        LCLBinding.set_StdCtrls_TComboBox_ParentColor(self.pointer,v)
    ParentColor=property(getParentColor,setParentColor)
    def getParentFont(self):
        r=LCLBinding.get_StdCtrls_TComboBox_ParentFont(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentFont(self,v):
        LCLBinding.set_StdCtrls_TComboBox_ParentFont(self.pointer,v)
    ParentFont=property(getParentFont,setParentFont)
    def getParentShowHint(self):
        r=LCLBinding.get_StdCtrls_TComboBox_ParentShowHint(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentShowHint(self,v):
        LCLBinding.set_StdCtrls_TComboBox_ParentShowHint(self.pointer,v)
    ParentShowHint=property(getParentShowHint,setParentShowHint)
    def getSorted(self):
        r=LCLBinding.get_StdCtrls_TComboBox_Sorted(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setSorted(self,v):
        LCLBinding.set_StdCtrls_TComboBox_Sorted(self.pointer,v)
    Sorted=property(getSorted,setSorted)
#constructorStdCtrls_TComboBox_Create
    @staticmethod
    def Create(TheOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.StdCtrls_TComboBox_Create((TheOwner.pointer)),TComboBox)
#class TComboBox end
#class TButtonControl start
class TButtonControl(TWinControl):
#    pointer=c_void_p()
    def __init__(self):#TButtonControl
        TWinControl.__init__(self)
#constructorStdCtrls_TButtonControl_Create
    @staticmethod
    def Create(TheOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.StdCtrls_TButtonControl_Create((TheOwner.pointer)),TButtonControl)
#class TButtonControl end
#class TCustomCheckBox start
class TCustomCheckBox(TButtonControl):
#    pointer=c_void_p()
    def __init__(self):#TCustomCheckBox
        TButtonControl.__init__(self)
#constructorStdCtrls_TCustomCheckBox_Create
    @staticmethod
    def Create(TheOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.StdCtrls_TCustomCheckBox_Create((TheOwner.pointer)),TCustomCheckBox)
    def getAllowGrayed(self):
        r=LCLBinding.get_StdCtrls_TCustomCheckBox_AllowGrayed(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setAllowGrayed(self,v):
        LCLBinding.set_StdCtrls_TCustomCheckBox_AllowGrayed(self.pointer,v)
    AllowGrayed=property(getAllowGrayed,setAllowGrayed)
    def getState(self):
        r=LCLBinding.get_StdCtrls_TCustomCheckBox_State(self.pointer)
        return r
    def setState(self,v):
        LCLBinding.set_StdCtrls_TCustomCheckBox_State(self.pointer,v.pointer)
    State=property(getState,setState)
    def _Warper_OnChange(self,Sender):
        self.OnChangecall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnChange(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnChangecall'):
            FreeOldEvent=1
            oldobj=OnChangePasObject
        self.OnChangecall=v 
        self.PasOnChange=FunctionForm(self._Warper_OnChange)
        self.OnChangePasObject=LCLBinding.set_StdCtrls_TCustomCheckBox_OnChange(self.pointer,self.PasOnChange,oldobj,FreeOldEvent)
    def getOnChange(self):
        return OnChangecall
    OnChange=property(getOnChange,setOnChange)
#class TCustomCheckBox end
#class TToggleBox start
class TToggleBox(TCustomCheckBox):
#    pointer=c_void_p()
    def __init__(self):#TToggleBox
        TCustomCheckBox.__init__(self)
#constructorStdCtrls_TToggleBox_Create
    @staticmethod
    def Create(TheOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.StdCtrls_TToggleBox_Create((TheOwner.pointer)),TToggleBox)
    def getChecked(self):
        r=LCLBinding.get_StdCtrls_TToggleBox_Checked(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setChecked(self,v):
        LCLBinding.set_StdCtrls_TToggleBox_Checked(self.pointer,v)
    Checked=property(getChecked,setChecked)
    def getDragKind(self):
        r=LCLBinding.get_StdCtrls_TToggleBox_DragKind(self.pointer)
        return r
    def setDragKind(self,v):
        LCLBinding.set_StdCtrls_TToggleBox_DragKind(self.pointer,v.pointer)
    DragKind=property(getDragKind,setDragKind)
    def getDragMode(self):
        r=LCLBinding.get_StdCtrls_TToggleBox_DragMode(self.pointer)
        return r
    def setDragMode(self,v):
        LCLBinding.set_StdCtrls_TToggleBox_DragMode(self.pointer,v.pointer)
    DragMode=property(getDragMode,setDragMode)
    def _Warper_OnDragDrop(self,Sender,Source,X,Y):
        self.OnDragDropcall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.GetPytonObject(Source,TObject),X,Y)
    def setOnDragDrop(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnDragDropcall'):
            FreeOldEvent=1
            oldobj=OnDragDropPasObject
        self.OnDragDropcall=v 
        self.PasOnDragDrop=FunctionForm(self._Warper_OnDragDrop)
        self.OnDragDropPasObject=LCLBinding.set_StdCtrls_TToggleBox_OnDragDrop(self.pointer,self.PasOnDragDrop,oldobj,FreeOldEvent)
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
            oldobj=OnDragOverPasObject
        self.OnDragOvercall=v 
        self.PasOnDragOver=FunctionForm(self._Warper_OnDragOver)
        self.OnDragOverPasObject=LCLBinding.set_StdCtrls_TToggleBox_OnDragOver(self.pointer,self.PasOnDragOver,oldobj,FreeOldEvent)
    def getOnDragOver(self):
        return OnDragOvercall
    OnDragOver=property(getOnDragOver,setOnDragOver)
    def _Warper_OnEndDrag(self,Sender,Target,X,Y):
        self.OnEndDragcall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.GetPytonObject(Target,TObject),X,Y)
    def setOnEndDrag(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnEndDragcall'):
            FreeOldEvent=1
            oldobj=OnEndDragPasObject
        self.OnEndDragcall=v 
        self.PasOnEndDrag=FunctionForm(self._Warper_OnEndDrag)
        self.OnEndDragPasObject=LCLBinding.set_StdCtrls_TToggleBox_OnEndDrag(self.pointer,self.PasOnEndDrag,oldobj,FreeOldEvent)
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
            oldobj=OnMouseDownPasObject
        self.OnMouseDowncall=v 
        self.PasOnMouseDown=FunctionForm(self._Warper_OnMouseDown)
        self.OnMouseDownPasObject=LCLBinding.set_StdCtrls_TToggleBox_OnMouseDown(self.pointer,self.PasOnMouseDown,oldobj,FreeOldEvent)
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
            oldobj=OnMouseEnterPasObject
        self.OnMouseEntercall=v 
        self.PasOnMouseEnter=FunctionForm(self._Warper_OnMouseEnter)
        self.OnMouseEnterPasObject=LCLBinding.set_StdCtrls_TToggleBox_OnMouseEnter(self.pointer,self.PasOnMouseEnter,oldobj,FreeOldEvent)
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
            oldobj=OnMouseLeavePasObject
        self.OnMouseLeavecall=v 
        self.PasOnMouseLeave=FunctionForm(self._Warper_OnMouseLeave)
        self.OnMouseLeavePasObject=LCLBinding.set_StdCtrls_TToggleBox_OnMouseLeave(self.pointer,self.PasOnMouseLeave,oldobj,FreeOldEvent)
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
            oldobj=OnMouseMovePasObject
        self.OnMouseMovecall=v 
        self.PasOnMouseMove=FunctionForm(self._Warper_OnMouseMove)
        self.OnMouseMovePasObject=LCLBinding.set_StdCtrls_TToggleBox_OnMouseMove(self.pointer,self.PasOnMouseMove,oldobj,FreeOldEvent)
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
            oldobj=OnMouseUpPasObject
        self.OnMouseUpcall=v 
        self.PasOnMouseUp=FunctionForm(self._Warper_OnMouseUp)
        self.OnMouseUpPasObject=LCLBinding.set_StdCtrls_TToggleBox_OnMouseUp(self.pointer,self.PasOnMouseUp,oldobj,FreeOldEvent)
    def getOnMouseUp(self):
        return OnMouseUpcall
    OnMouseUp=property(getOnMouseUp,setOnMouseUp)
    def _Warper_OnStartDrag(self,Sender,DragObject):
        self.OnStartDragcall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.GetPytonObject(DragObject,TDragObject))
    def setOnStartDrag(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnStartDragcall'):
            FreeOldEvent=1
            oldobj=OnStartDragPasObject
        self.OnStartDragcall=v 
        self.PasOnStartDrag=FunctionForm(self._Warper_OnStartDrag)
        self.OnStartDragPasObject=LCLBinding.set_StdCtrls_TToggleBox_OnStartDrag(self.pointer,self.PasOnStartDrag,oldobj,FreeOldEvent)
    def getOnStartDrag(self):
        return OnStartDragcall
    OnStartDrag=property(getOnStartDrag,setOnStartDrag)
    def getParentFont(self):
        r=LCLBinding.get_StdCtrls_TToggleBox_ParentFont(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentFont(self,v):
        LCLBinding.set_StdCtrls_TToggleBox_ParentFont(self.pointer,v)
    ParentFont=property(getParentFont,setParentFont)
    def getParentShowHint(self):
        r=LCLBinding.get_StdCtrls_TToggleBox_ParentShowHint(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentShowHint(self,v):
        LCLBinding.set_StdCtrls_TToggleBox_ParentShowHint(self.pointer,v)
    ParentShowHint=property(getParentShowHint,setParentShowHint)
#class TToggleBox end
#class TRadioButton start
class TRadioButton(TCustomCheckBox):
#    pointer=c_void_p()
    def __init__(self):#TRadioButton
        TCustomCheckBox.__init__(self)
#constructorStdCtrls_TRadioButton_Create
    @staticmethod
    def Create(TheOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.StdCtrls_TRadioButton_Create((TheOwner.pointer)),TRadioButton)
    def getChecked(self):
        r=LCLBinding.get_StdCtrls_TRadioButton_Checked(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setChecked(self,v):
        LCLBinding.set_StdCtrls_TRadioButton_Checked(self.pointer,v)
    Checked=property(getChecked,setChecked)
    def getDragKind(self):
        r=LCLBinding.get_StdCtrls_TRadioButton_DragKind(self.pointer)
        return r
    def setDragKind(self,v):
        LCLBinding.set_StdCtrls_TRadioButton_DragKind(self.pointer,v.pointer)
    DragKind=property(getDragKind,setDragKind)
    def getDragMode(self):
        r=LCLBinding.get_StdCtrls_TRadioButton_DragMode(self.pointer)
        return r
    def setDragMode(self,v):
        LCLBinding.set_StdCtrls_TRadioButton_DragMode(self.pointer,v.pointer)
    DragMode=property(getDragMode,setDragMode)
    def _Warper_OnDragDrop(self,Sender,Source,X,Y):
        self.OnDragDropcall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.GetPytonObject(Source,TObject),X,Y)
    def setOnDragDrop(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnDragDropcall'):
            FreeOldEvent=1
            oldobj=OnDragDropPasObject
        self.OnDragDropcall=v 
        self.PasOnDragDrop=FunctionForm(self._Warper_OnDragDrop)
        self.OnDragDropPasObject=LCLBinding.set_StdCtrls_TRadioButton_OnDragDrop(self.pointer,self.PasOnDragDrop,oldobj,FreeOldEvent)
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
            oldobj=OnDragOverPasObject
        self.OnDragOvercall=v 
        self.PasOnDragOver=FunctionForm(self._Warper_OnDragOver)
        self.OnDragOverPasObject=LCLBinding.set_StdCtrls_TRadioButton_OnDragOver(self.pointer,self.PasOnDragOver,oldobj,FreeOldEvent)
    def getOnDragOver(self):
        return OnDragOvercall
    OnDragOver=property(getOnDragOver,setOnDragOver)
    def _Warper_OnEndDrag(self,Sender,Target,X,Y):
        self.OnEndDragcall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.GetPytonObject(Target,TObject),X,Y)
    def setOnEndDrag(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnEndDragcall'):
            FreeOldEvent=1
            oldobj=OnEndDragPasObject
        self.OnEndDragcall=v 
        self.PasOnEndDrag=FunctionForm(self._Warper_OnEndDrag)
        self.OnEndDragPasObject=LCLBinding.set_StdCtrls_TRadioButton_OnEndDrag(self.pointer,self.PasOnEndDrag,oldobj,FreeOldEvent)
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
            oldobj=OnMouseDownPasObject
        self.OnMouseDowncall=v 
        self.PasOnMouseDown=FunctionForm(self._Warper_OnMouseDown)
        self.OnMouseDownPasObject=LCLBinding.set_StdCtrls_TRadioButton_OnMouseDown(self.pointer,self.PasOnMouseDown,oldobj,FreeOldEvent)
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
            oldobj=OnMouseEnterPasObject
        self.OnMouseEntercall=v 
        self.PasOnMouseEnter=FunctionForm(self._Warper_OnMouseEnter)
        self.OnMouseEnterPasObject=LCLBinding.set_StdCtrls_TRadioButton_OnMouseEnter(self.pointer,self.PasOnMouseEnter,oldobj,FreeOldEvent)
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
            oldobj=OnMouseLeavePasObject
        self.OnMouseLeavecall=v 
        self.PasOnMouseLeave=FunctionForm(self._Warper_OnMouseLeave)
        self.OnMouseLeavePasObject=LCLBinding.set_StdCtrls_TRadioButton_OnMouseLeave(self.pointer,self.PasOnMouseLeave,oldobj,FreeOldEvent)
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
            oldobj=OnMouseMovePasObject
        self.OnMouseMovecall=v 
        self.PasOnMouseMove=FunctionForm(self._Warper_OnMouseMove)
        self.OnMouseMovePasObject=LCLBinding.set_StdCtrls_TRadioButton_OnMouseMove(self.pointer,self.PasOnMouseMove,oldobj,FreeOldEvent)
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
            oldobj=OnMouseUpPasObject
        self.OnMouseUpcall=v 
        self.PasOnMouseUp=FunctionForm(self._Warper_OnMouseUp)
        self.OnMouseUpPasObject=LCLBinding.set_StdCtrls_TRadioButton_OnMouseUp(self.pointer,self.PasOnMouseUp,oldobj,FreeOldEvent)
    def getOnMouseUp(self):
        return OnMouseUpcall
    OnMouseUp=property(getOnMouseUp,setOnMouseUp)
    def _Warper_OnStartDrag(self,Sender,DragObject):
        self.OnStartDragcall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.GetPytonObject(DragObject,TDragObject))
    def setOnStartDrag(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnStartDragcall'):
            FreeOldEvent=1
            oldobj=OnStartDragPasObject
        self.OnStartDragcall=v 
        self.PasOnStartDrag=FunctionForm(self._Warper_OnStartDrag)
        self.OnStartDragPasObject=LCLBinding.set_StdCtrls_TRadioButton_OnStartDrag(self.pointer,self.PasOnStartDrag,oldobj,FreeOldEvent)
    def getOnStartDrag(self):
        return OnStartDragcall
    OnStartDrag=property(getOnStartDrag,setOnStartDrag)
    def getParentColor(self):
        r=LCLBinding.get_StdCtrls_TRadioButton_ParentColor(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentColor(self,v):
        LCLBinding.set_StdCtrls_TRadioButton_ParentColor(self.pointer,v)
    ParentColor=property(getParentColor,setParentColor)
    def getParentFont(self):
        r=LCLBinding.get_StdCtrls_TRadioButton_ParentFont(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentFont(self,v):
        LCLBinding.set_StdCtrls_TRadioButton_ParentFont(self.pointer,v)
    ParentFont=property(getParentFont,setParentFont)
    def getParentShowHint(self):
        r=LCLBinding.get_StdCtrls_TRadioButton_ParentShowHint(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentShowHint(self,v):
        LCLBinding.set_StdCtrls_TRadioButton_ParentShowHint(self.pointer,v)
    ParentShowHint=property(getParentShowHint,setParentShowHint)
#class TRadioButton end
#class TCheckBox start
class TCheckBox(TCustomCheckBox):
#    pointer=c_void_p()
    def __init__(self):#TCheckBox
        TCustomCheckBox.__init__(self)
#constructorStdCtrls_TCheckBox_Create
    @staticmethod
    def Create(TheOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.StdCtrls_TCheckBox_Create((TheOwner.pointer)),TCheckBox)
    def getChecked(self):
        r=LCLBinding.get_StdCtrls_TCheckBox_Checked(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setChecked(self,v):
        LCLBinding.set_StdCtrls_TCheckBox_Checked(self.pointer,v)
    Checked=property(getChecked,setChecked)
    def getDragKind(self):
        r=LCLBinding.get_StdCtrls_TCheckBox_DragKind(self.pointer)
        return r
    def setDragKind(self,v):
        LCLBinding.set_StdCtrls_TCheckBox_DragKind(self.pointer,v.pointer)
    DragKind=property(getDragKind,setDragKind)
    def getDragMode(self):
        r=LCLBinding.get_StdCtrls_TCheckBox_DragMode(self.pointer)
        return r
    def setDragMode(self,v):
        LCLBinding.set_StdCtrls_TCheckBox_DragMode(self.pointer,v.pointer)
    DragMode=property(getDragMode,setDragMode)
    def _Warper_OnDragDrop(self,Sender,Source,X,Y):
        self.OnDragDropcall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.GetPytonObject(Source,TObject),X,Y)
    def setOnDragDrop(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnDragDropcall'):
            FreeOldEvent=1
            oldobj=OnDragDropPasObject
        self.OnDragDropcall=v 
        self.PasOnDragDrop=FunctionForm(self._Warper_OnDragDrop)
        self.OnDragDropPasObject=LCLBinding.set_StdCtrls_TCheckBox_OnDragDrop(self.pointer,self.PasOnDragDrop,oldobj,FreeOldEvent)
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
            oldobj=OnDragOverPasObject
        self.OnDragOvercall=v 
        self.PasOnDragOver=FunctionForm(self._Warper_OnDragOver)
        self.OnDragOverPasObject=LCLBinding.set_StdCtrls_TCheckBox_OnDragOver(self.pointer,self.PasOnDragOver,oldobj,FreeOldEvent)
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
            oldobj=OnEditingDonePasObject
        self.OnEditingDonecall=v 
        self.PasOnEditingDone=FunctionForm(self._Warper_OnEditingDone)
        self.OnEditingDonePasObject=LCLBinding.set_StdCtrls_TCheckBox_OnEditingDone(self.pointer,self.PasOnEditingDone,oldobj,FreeOldEvent)
    def getOnEditingDone(self):
        return OnEditingDonecall
    OnEditingDone=property(getOnEditingDone,setOnEditingDone)
    def _Warper_OnEndDrag(self,Sender,Target,X,Y):
        self.OnEndDragcall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.GetPytonObject(Target,TObject),X,Y)
    def setOnEndDrag(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnEndDragcall'):
            FreeOldEvent=1
            oldobj=OnEndDragPasObject
        self.OnEndDragcall=v 
        self.PasOnEndDrag=FunctionForm(self._Warper_OnEndDrag)
        self.OnEndDragPasObject=LCLBinding.set_StdCtrls_TCheckBox_OnEndDrag(self.pointer,self.PasOnEndDrag,oldobj,FreeOldEvent)
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
            oldobj=OnMouseDownPasObject
        self.OnMouseDowncall=v 
        self.PasOnMouseDown=FunctionForm(self._Warper_OnMouseDown)
        self.OnMouseDownPasObject=LCLBinding.set_StdCtrls_TCheckBox_OnMouseDown(self.pointer,self.PasOnMouseDown,oldobj,FreeOldEvent)
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
            oldobj=OnMouseEnterPasObject
        self.OnMouseEntercall=v 
        self.PasOnMouseEnter=FunctionForm(self._Warper_OnMouseEnter)
        self.OnMouseEnterPasObject=LCLBinding.set_StdCtrls_TCheckBox_OnMouseEnter(self.pointer,self.PasOnMouseEnter,oldobj,FreeOldEvent)
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
            oldobj=OnMouseLeavePasObject
        self.OnMouseLeavecall=v 
        self.PasOnMouseLeave=FunctionForm(self._Warper_OnMouseLeave)
        self.OnMouseLeavePasObject=LCLBinding.set_StdCtrls_TCheckBox_OnMouseLeave(self.pointer,self.PasOnMouseLeave,oldobj,FreeOldEvent)
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
            oldobj=OnMouseMovePasObject
        self.OnMouseMovecall=v 
        self.PasOnMouseMove=FunctionForm(self._Warper_OnMouseMove)
        self.OnMouseMovePasObject=LCLBinding.set_StdCtrls_TCheckBox_OnMouseMove(self.pointer,self.PasOnMouseMove,oldobj,FreeOldEvent)
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
            oldobj=OnMouseUpPasObject
        self.OnMouseUpcall=v 
        self.PasOnMouseUp=FunctionForm(self._Warper_OnMouseUp)
        self.OnMouseUpPasObject=LCLBinding.set_StdCtrls_TCheckBox_OnMouseUp(self.pointer,self.PasOnMouseUp,oldobj,FreeOldEvent)
    def getOnMouseUp(self):
        return OnMouseUpcall
    OnMouseUp=property(getOnMouseUp,setOnMouseUp)
    def _Warper_OnStartDrag(self,Sender,DragObject):
        self.OnStartDragcall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.GetPytonObject(DragObject,TDragObject))
    def setOnStartDrag(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnStartDragcall'):
            FreeOldEvent=1
            oldobj=OnStartDragPasObject
        self.OnStartDragcall=v 
        self.PasOnStartDrag=FunctionForm(self._Warper_OnStartDrag)
        self.OnStartDragPasObject=LCLBinding.set_StdCtrls_TCheckBox_OnStartDrag(self.pointer,self.PasOnStartDrag,oldobj,FreeOldEvent)
    def getOnStartDrag(self):
        return OnStartDragcall
    OnStartDrag=property(getOnStartDrag,setOnStartDrag)
    def getParentColor(self):
        r=LCLBinding.get_StdCtrls_TCheckBox_ParentColor(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentColor(self,v):
        LCLBinding.set_StdCtrls_TCheckBox_ParentColor(self.pointer,v)
    ParentColor=property(getParentColor,setParentColor)
    def getParentFont(self):
        r=LCLBinding.get_StdCtrls_TCheckBox_ParentFont(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentFont(self,v):
        LCLBinding.set_StdCtrls_TCheckBox_ParentFont(self.pointer,v)
    ParentFont=property(getParentFont,setParentFont)
    def getParentShowHint(self):
        r=LCLBinding.get_StdCtrls_TCheckBox_ParentShowHint(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentShowHint(self,v):
        LCLBinding.set_StdCtrls_TCheckBox_ParentShowHint(self.pointer,v)
    ParentShowHint=property(getParentShowHint,setParentShowHint)
#class TCheckBox end
#class TCustomButton start
class TCustomButton(TButtonControl):
#    pointer=c_void_p()
    def __init__(self):#TCustomButton
        TButtonControl.__init__(self)
#constructorStdCtrls_TCustomButton_Create
    @staticmethod
    def Create(TheOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.StdCtrls_TCustomButton_Create((TheOwner.pointer)),TCustomButton)
    def getActive(self):
        r=LCLBinding.get_StdCtrls_TCustomButton_Active(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    Active=property(getActive)
    def getDefault(self):
        r=LCLBinding.get_StdCtrls_TCustomButton_Default(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setDefault(self,v):
        LCLBinding.set_StdCtrls_TCustomButton_Default(self.pointer,v)
    Default=property(getDefault,setDefault)
    def getCancel(self):
        r=LCLBinding.get_StdCtrls_TCustomButton_Cancel(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setCancel(self,v):
        LCLBinding.set_StdCtrls_TCustomButton_Cancel(self.pointer,v)
    Cancel=property(getCancel,setCancel)
#class TCustomButton end
#class TButton start
class TButton(TCustomButton):
#    pointer=c_void_p()
    def __init__(self):#TButton
        TCustomButton.__init__(self)
    def getDragKind(self):
        r=LCLBinding.get_StdCtrls_TButton_DragKind(self.pointer)
        return r
    def setDragKind(self,v):
        LCLBinding.set_StdCtrls_TButton_DragKind(self.pointer,v.pointer)
    DragKind=property(getDragKind,setDragKind)
    def getDragMode(self):
        r=LCLBinding.get_StdCtrls_TButton_DragMode(self.pointer)
        return r
    def setDragMode(self,v):
        LCLBinding.set_StdCtrls_TButton_DragMode(self.pointer,v.pointer)
    DragMode=property(getDragMode,setDragMode)
    def _Warper_OnDragDrop(self,Sender,Source,X,Y):
        self.OnDragDropcall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.GetPytonObject(Source,TObject),X,Y)
    def setOnDragDrop(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnDragDropcall'):
            FreeOldEvent=1
            oldobj=OnDragDropPasObject
        self.OnDragDropcall=v 
        self.PasOnDragDrop=FunctionForm(self._Warper_OnDragDrop)
        self.OnDragDropPasObject=LCLBinding.set_StdCtrls_TButton_OnDragDrop(self.pointer,self.PasOnDragDrop,oldobj,FreeOldEvent)
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
            oldobj=OnDragOverPasObject
        self.OnDragOvercall=v 
        self.PasOnDragOver=FunctionForm(self._Warper_OnDragOver)
        self.OnDragOverPasObject=LCLBinding.set_StdCtrls_TButton_OnDragOver(self.pointer,self.PasOnDragOver,oldobj,FreeOldEvent)
    def getOnDragOver(self):
        return OnDragOvercall
    OnDragOver=property(getOnDragOver,setOnDragOver)
    def _Warper_OnEndDrag(self,Sender,Target,X,Y):
        self.OnEndDragcall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.GetPytonObject(Target,TObject),X,Y)
    def setOnEndDrag(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnEndDragcall'):
            FreeOldEvent=1
            oldobj=OnEndDragPasObject
        self.OnEndDragcall=v 
        self.PasOnEndDrag=FunctionForm(self._Warper_OnEndDrag)
        self.OnEndDragPasObject=LCLBinding.set_StdCtrls_TButton_OnEndDrag(self.pointer,self.PasOnEndDrag,oldobj,FreeOldEvent)
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
            oldobj=OnMouseDownPasObject
        self.OnMouseDowncall=v 
        self.PasOnMouseDown=FunctionForm(self._Warper_OnMouseDown)
        self.OnMouseDownPasObject=LCLBinding.set_StdCtrls_TButton_OnMouseDown(self.pointer,self.PasOnMouseDown,oldobj,FreeOldEvent)
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
            oldobj=OnMouseEnterPasObject
        self.OnMouseEntercall=v 
        self.PasOnMouseEnter=FunctionForm(self._Warper_OnMouseEnter)
        self.OnMouseEnterPasObject=LCLBinding.set_StdCtrls_TButton_OnMouseEnter(self.pointer,self.PasOnMouseEnter,oldobj,FreeOldEvent)
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
            oldobj=OnMouseLeavePasObject
        self.OnMouseLeavecall=v 
        self.PasOnMouseLeave=FunctionForm(self._Warper_OnMouseLeave)
        self.OnMouseLeavePasObject=LCLBinding.set_StdCtrls_TButton_OnMouseLeave(self.pointer,self.PasOnMouseLeave,oldobj,FreeOldEvent)
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
            oldobj=OnMouseMovePasObject
        self.OnMouseMovecall=v 
        self.PasOnMouseMove=FunctionForm(self._Warper_OnMouseMove)
        self.OnMouseMovePasObject=LCLBinding.set_StdCtrls_TButton_OnMouseMove(self.pointer,self.PasOnMouseMove,oldobj,FreeOldEvent)
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
            oldobj=OnMouseUpPasObject
        self.OnMouseUpcall=v 
        self.PasOnMouseUp=FunctionForm(self._Warper_OnMouseUp)
        self.OnMouseUpPasObject=LCLBinding.set_StdCtrls_TButton_OnMouseUp(self.pointer,self.PasOnMouseUp,oldobj,FreeOldEvent)
    def getOnMouseUp(self):
        return OnMouseUpcall
    OnMouseUp=property(getOnMouseUp,setOnMouseUp)
    def _Warper_OnStartDrag(self,Sender,DragObject):
        self.OnStartDragcall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.GetPytonObject(DragObject,TDragObject))
    def setOnStartDrag(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnStartDragcall'):
            FreeOldEvent=1
            oldobj=OnStartDragPasObject
        self.OnStartDragcall=v 
        self.PasOnStartDrag=FunctionForm(self._Warper_OnStartDrag)
        self.OnStartDragPasObject=LCLBinding.set_StdCtrls_TButton_OnStartDrag(self.pointer,self.PasOnStartDrag,oldobj,FreeOldEvent)
    def getOnStartDrag(self):
        return OnStartDragcall
    OnStartDrag=property(getOnStartDrag,setOnStartDrag)
    def getParentFont(self):
        r=LCLBinding.get_StdCtrls_TButton_ParentFont(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentFont(self,v):
        LCLBinding.set_StdCtrls_TButton_ParentFont(self.pointer,v)
    ParentFont=property(getParentFont,setParentFont)
    def getParentShowHint(self):
        r=LCLBinding.get_StdCtrls_TButton_ParentShowHint(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentShowHint(self,v):
        LCLBinding.set_StdCtrls_TButton_ParentShowHint(self.pointer,v)
    ParentShowHint=property(getParentShowHint,setParentShowHint)
#constructorStdCtrls_TButton_Create
    @staticmethod
    def Create(TheOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.StdCtrls_TButton_Create((TheOwner.pointer)),TButton)
#class TButton end
