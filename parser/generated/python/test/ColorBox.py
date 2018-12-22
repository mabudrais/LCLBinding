from StdCtrls import *
from Forms import *
from Controls import *
from Graphics import *
from Classes import *
from MainPasObject import *
#import end
def CreateTColorBoxStyleFromInt(i):
    dic={1:"cbStandardColors",2:"cbExtendedColors",4:"cbSystemColors",8:"cbIncludeNone",16:"cbIncludeDefault",32:"cbCustomColor",64:"cbPrettyNames",128:"cbCustomColors"}
    return CreateSetFormint(i,dic)
#class TCustomColorListBox start
class TCustomColorListBox(TCustomListBox):
#    pointer=c_void_p()
    def __init__(self):#TCustomColorListBox
        TCustomListBox.__init__(self)
#constructorColorBox_TCustomColorListBox_Create
    @staticmethod
    def Create(AOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.ColorBox_TCustomColorListBox_Create((AOwner.pointer)),TCustomColorListBox)
    def getColorRectWidth(self):
        r=LCLBinding.get_ColorBox_TCustomColorListBox_ColorRectWidth(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setColorRectWidth(self,v):
        LCLBinding.set_ColorBox_TCustomColorListBox_ColorRectWidth(self.pointer,v)
    ColorRectWidth=property(getColorRectWidth,setColorRectWidth)
    def getColorRectOffset(self):
        r=LCLBinding.get_ColorBox_TCustomColorListBox_ColorRectOffset(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setColorRectOffset(self,v):
        LCLBinding.set_ColorBox_TCustomColorListBox_ColorRectOffset(self.pointer,v)
    ColorRectOffset=property(getColorRectOffset,setColorRectOffset)
    def getStyle(self):
        r=LCLBinding.get_ColorBox_TCustomColorListBox_Style(self.pointer)
        return r
    def setStyle(self,v):
        LCLBinding.set_ColorBox_TCustomColorListBox_Style(self.pointer,v.pointer)
    Style=property(getStyle,setStyle)
    def getColorNames(self,Index):
        r=LCLBinding.get_ColorBox_TCustomColorListBox_ColorNames(self.pointer,Index)
        return LCLBindingUtil.ConvertPascalstring(r)
    def _Warper_OnGetColors(self,Sender,Items):
        self.OnGetColorscall(LCLBindingUtil.GetPytonObject(Sender,TCustomColorListBox),LCLBindingUtil.GetPytonObject(Items,TStrings))
    def setOnGetColors(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnGetColorscall'):
            FreeOldEvent=1
            oldobj=OnGetColorsPasObject
        self.OnGetColorscall=v 
        self.PasOnGetColors=FunctionForm(self._Warper_OnGetColors)
        self.OnGetColorsPasObject=LCLBinding.set_ColorBox_TCustomColorListBox_OnGetColors(self.pointer,self.PasOnGetColors,oldobj,FreeOldEvent)
    def getOnGetColors(self):
        return OnGetColorscall
    OnGetColors=property(getOnGetColors,setOnGetColors)
#class TCustomColorListBox end
#class TColorListBox start
class TColorListBox(TCustomColorListBox):
#    pointer=c_void_p()
    def __init__(self):#TColorListBox
        TCustomColorListBox.__init__(self)
    def getDragKind(self):
        r=LCLBinding.get_ColorBox_TColorListBox_DragKind(self.pointer)
        return r
    def setDragKind(self,v):
        LCLBinding.set_ColorBox_TColorListBox_DragKind(self.pointer,v.pointer)
    DragKind=property(getDragKind,setDragKind)
    def getDragMode(self):
        r=LCLBinding.get_ColorBox_TColorListBox_DragMode(self.pointer)
        return r
    def setDragMode(self,v):
        LCLBinding.set_ColorBox_TColorListBox_DragMode(self.pointer,v.pointer)
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
        self.OnDragDropPasObject=LCLBinding.set_ColorBox_TColorListBox_OnDragDrop(self.pointer,self.PasOnDragDrop,oldobj,FreeOldEvent)
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
        self.OnDragOverPasObject=LCLBinding.set_ColorBox_TColorListBox_OnDragOver(self.pointer,self.PasOnDragOver,oldobj,FreeOldEvent)
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
        self.OnEndDragPasObject=LCLBinding.set_ColorBox_TColorListBox_OnEndDrag(self.pointer,self.PasOnEndDrag,oldobj,FreeOldEvent)
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
        self.OnStartDragPasObject=LCLBinding.set_ColorBox_TColorListBox_OnStartDrag(self.pointer,self.PasOnStartDrag,oldobj,FreeOldEvent)
    def getOnStartDrag(self):
        return OnStartDragcall
    OnStartDrag=property(getOnStartDrag,setOnStartDrag)
#constructorColorBox_TColorListBox_Create
    @staticmethod
    def Create(AOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.ColorBox_TColorListBox_Create((AOwner.pointer)),TColorListBox)
#class TColorListBox end
#class TCustomColorBox start
class TCustomColorBox(TCustomComboBox):
#    pointer=c_void_p()
    def __init__(self):#TCustomColorBox
        TCustomComboBox.__init__(self)
#constructorColorBox_TCustomColorBox_Create
    @staticmethod
    def Create(AOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.ColorBox_TCustomColorBox_Create((AOwner.pointer)),TCustomColorBox)
    def getColorRectWidth(self):
        r=LCLBinding.get_ColorBox_TCustomColorBox_ColorRectWidth(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setColorRectWidth(self,v):
        LCLBinding.set_ColorBox_TCustomColorBox_ColorRectWidth(self.pointer,v)
    ColorRectWidth=property(getColorRectWidth,setColorRectWidth)
    def getColorRectOffset(self):
        r=LCLBinding.get_ColorBox_TCustomColorBox_ColorRectOffset(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setColorRectOffset(self,v):
        LCLBinding.set_ColorBox_TCustomColorBox_ColorRectOffset(self.pointer,v)
    ColorRectOffset=property(getColorRectOffset,setColorRectOffset)
    def getStyle(self):
        r=LCLBinding.get_ColorBox_TCustomColorBox_Style(self.pointer)
        return r
    def setStyle(self,v):
        LCLBinding.set_ColorBox_TCustomColorBox_Style(self.pointer,v.pointer)
    Style=property(getStyle,setStyle)
    def getColorNames(self,Index):
        r=LCLBinding.get_ColorBox_TCustomColorBox_ColorNames(self.pointer,Index)
        return LCLBindingUtil.ConvertPascalstring(r)
    def _Warper_OnGetColors(self,Sender,Items):
        self.OnGetColorscall(LCLBindingUtil.GetPytonObject(Sender,TCustomColorBox),LCLBindingUtil.GetPytonObject(Items,TStrings))
    def setOnGetColors(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnGetColorscall'):
            FreeOldEvent=1
            oldobj=OnGetColorsPasObject
        self.OnGetColorscall=v 
        self.PasOnGetColors=FunctionForm(self._Warper_OnGetColors)
        self.OnGetColorsPasObject=LCLBinding.set_ColorBox_TCustomColorBox_OnGetColors(self.pointer,self.PasOnGetColors,oldobj,FreeOldEvent)
    def getOnGetColors(self):
        return OnGetColorscall
    OnGetColors=property(getOnGetColors,setOnGetColors)
#class TCustomColorBox end
#class TColorBox start
class TColorBox(TCustomColorBox):
#    pointer=c_void_p()
    def __init__(self):#TColorBox
        TCustomColorBox.__init__(self)
    def getDragMode(self):
        r=LCLBinding.get_ColorBox_TColorBox_DragMode(self.pointer)
        return r
    def setDragMode(self,v):
        LCLBinding.set_ColorBox_TColorBox_DragMode(self.pointer,v.pointer)
    DragMode=property(getDragMode,setDragMode)
    def getItemHeight(self):
        r=LCLBinding.get_ColorBox_TColorBox_ItemHeight(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setItemHeight(self,v):
        LCLBinding.set_ColorBox_TColorBox_ItemHeight(self.pointer,v)
    ItemHeight=property(getItemHeight,setItemHeight)
    def getItemWidth(self):
        r=LCLBinding.get_ColorBox_TColorBox_ItemWidth(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setItemWidth(self,v):
        LCLBinding.set_ColorBox_TColorBox_ItemWidth(self.pointer,v)
    ItemWidth=property(getItemWidth,setItemWidth)
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
        self.OnChangePasObject=LCLBinding.set_ColorBox_TColorBox_OnChange(self.pointer,self.PasOnChange,oldobj,FreeOldEvent)
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
        self.OnCloseUpPasObject=LCLBinding.set_ColorBox_TColorBox_OnCloseUp(self.pointer,self.PasOnCloseUp,oldobj,FreeOldEvent)
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
        self.OnDblClickPasObject=LCLBinding.set_ColorBox_TColorBox_OnDblClick(self.pointer,self.PasOnDblClick,oldobj,FreeOldEvent)
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
        self.OnDragDropPasObject=LCLBinding.set_ColorBox_TColorBox_OnDragDrop(self.pointer,self.PasOnDragDrop,oldobj,FreeOldEvent)
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
        self.OnDragOverPasObject=LCLBinding.set_ColorBox_TColorBox_OnDragOver(self.pointer,self.PasOnDragOver,oldobj,FreeOldEvent)
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
        self.OnEndDragPasObject=LCLBinding.set_ColorBox_TColorBox_OnEndDrag(self.pointer,self.PasOnEndDrag,oldobj,FreeOldEvent)
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
        self.OnDropDownPasObject=LCLBinding.set_ColorBox_TColorBox_OnDropDown(self.pointer,self.PasOnDropDown,oldobj,FreeOldEvent)
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
        self.OnEditingDonePasObject=LCLBinding.set_ColorBox_TColorBox_OnEditingDone(self.pointer,self.PasOnEditingDone,oldobj,FreeOldEvent)
    def getOnEditingDone(self):
        return OnEditingDonecall
    OnEditingDone=property(getOnEditingDone,setOnEditingDone)
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
        self.OnMouseDownPasObject=LCLBinding.set_ColorBox_TColorBox_OnMouseDown(self.pointer,self.PasOnMouseDown,oldobj,FreeOldEvent)
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
        self.OnMouseEnterPasObject=LCLBinding.set_ColorBox_TColorBox_OnMouseEnter(self.pointer,self.PasOnMouseEnter,oldobj,FreeOldEvent)
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
        self.OnMouseLeavePasObject=LCLBinding.set_ColorBox_TColorBox_OnMouseLeave(self.pointer,self.PasOnMouseLeave,oldobj,FreeOldEvent)
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
        self.OnMouseMovePasObject=LCLBinding.set_ColorBox_TColorBox_OnMouseMove(self.pointer,self.PasOnMouseMove,oldobj,FreeOldEvent)
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
        self.OnMouseUpPasObject=LCLBinding.set_ColorBox_TColorBox_OnMouseUp(self.pointer,self.PasOnMouseUp,oldobj,FreeOldEvent)
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
        self.OnStartDragPasObject=LCLBinding.set_ColorBox_TColorBox_OnStartDrag(self.pointer,self.PasOnStartDrag,oldobj,FreeOldEvent)
    def getOnStartDrag(self):
        return OnStartDragcall
    OnStartDrag=property(getOnStartDrag,setOnStartDrag)
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
        self.OnSelectPasObject=LCLBinding.set_ColorBox_TColorBox_OnSelect(self.pointer,self.PasOnSelect,oldobj,FreeOldEvent)
    def getOnSelect(self):
        return OnSelectcall
    OnSelect=property(getOnSelect,setOnSelect)
    def getParentColor(self):
        r=LCLBinding.get_ColorBox_TColorBox_ParentColor(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentColor(self,v):
        LCLBinding.set_ColorBox_TColorBox_ParentColor(self.pointer,v)
    ParentColor=property(getParentColor,setParentColor)
    def getParentFont(self):
        r=LCLBinding.get_ColorBox_TColorBox_ParentFont(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentFont(self,v):
        LCLBinding.set_ColorBox_TColorBox_ParentFont(self.pointer,v)
    ParentFont=property(getParentFont,setParentFont)
    def getParentShowHint(self):
        r=LCLBinding.get_ColorBox_TColorBox_ParentShowHint(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentShowHint(self,v):
        LCLBinding.set_ColorBox_TColorBox_ParentShowHint(self.pointer,v)
    ParentShowHint=property(getParentShowHint,setParentShowHint)
#constructorColorBox_TColorBox_Create
    @staticmethod
    def Create(AOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.ColorBox_TColorBox_Create((AOwner.pointer)),TColorBox)
#class TColorBox end
