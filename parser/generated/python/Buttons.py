from Menus import *
from Forms import *
from StdCtrls import *
from Controls import *
from ActnList import *
from ImgList import *
from Graphics import *
from GraphType import *
from Classes import *
from MainPasObject import *
import LCLBindingUtil
#import end
#class TCustomSpeedButton start
class TCustomSpeedButton(TGraphicControl):
#    pointer=c_void_p()
    def __init__(self):#TCustomSpeedButton
        TGraphicControl.__init__(self)
#constructorButtons_TCustomSpeedButton_Create
    @staticmethod
    def Create(AOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.Buttons_TCustomSpeedButton_Create((AOwner.pointer)),TCustomSpeedButton)
#Procedure Buttons_TCustomSpeedButton_Click
    @staticmethod
    def Click(self,):
        LCLBinding.Buttons_TCustomSpeedButton_Click()
#Procedure Buttons_TCustomSpeedButton_LoadGlyphFromLazarusResource
    @staticmethod
    def LoadGlyphFromLazarusResource(self,AName):
        LCLBinding.Buttons_TCustomSpeedButton_LoadGlyphFromLazarusResource((AName))
    def getAllowAllUp(self):
        r=LCLBinding.get_Buttons_TCustomSpeedButton_AllowAllUp(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setAllowAllUp(self,v):
        LCLBinding.set_Buttons_TCustomSpeedButton_AllowAllUp(self.pointer,v)
    AllowAllUp=property(getAllowAllUp,setAllowAllUp)
    def getDown(self):
        r=LCLBinding.get_Buttons_TCustomSpeedButton_Down(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setDown(self,v):
        LCLBinding.set_Buttons_TCustomSpeedButton_Down(self.pointer,v)
    Down=property(getDown,setDown)
    def getFlat(self):
        r=LCLBinding.get_Buttons_TCustomSpeedButton_Flat(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setFlat(self,v):
        LCLBinding.set_Buttons_TCustomSpeedButton_Flat(self.pointer,v)
    Flat=property(getFlat,setFlat)
    def getGlyph(self):
        r=LCLBinding.get_Buttons_TCustomSpeedButton_Glyph(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TBitmap)
    def setGlyph(self,v):
        LCLBinding.set_Buttons_TCustomSpeedButton_Glyph(self.pointer,v.pointer)
    Glyph=property(getGlyph,setGlyph)
    def getGroupIndex(self):
        r=LCLBinding.get_Buttons_TCustomSpeedButton_GroupIndex(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setGroupIndex(self,v):
        LCLBinding.set_Buttons_TCustomSpeedButton_GroupIndex(self.pointer,v)
    GroupIndex=property(getGroupIndex,setGroupIndex)
    def getLayout(self):
        r=LCLBinding.get_Buttons_TCustomSpeedButton_Layout(self.pointer)
        return r
    def setLayout(self,v):
        LCLBinding.set_Buttons_TCustomSpeedButton_Layout(self.pointer,v.pointer)
    Layout=property(getLayout,setLayout)
    def getMargin(self):
        r=LCLBinding.get_Buttons_TCustomSpeedButton_Margin(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setMargin(self,v):
        LCLBinding.set_Buttons_TCustomSpeedButton_Margin(self.pointer,v)
    Margin=property(getMargin,setMargin)
    def getNumGlyphs(self):
        r=LCLBinding.get_Buttons_TCustomSpeedButton_NumGlyphs(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setNumGlyphs(self,v):
        LCLBinding.set_Buttons_TCustomSpeedButton_NumGlyphs(self.pointer,v)
    NumGlyphs=property(getNumGlyphs,setNumGlyphs)
    def getShowAccelChar(self):
        r=LCLBinding.get_Buttons_TCustomSpeedButton_ShowAccelChar(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setShowAccelChar(self,v):
        LCLBinding.set_Buttons_TCustomSpeedButton_ShowAccelChar(self.pointer,v)
    ShowAccelChar=property(getShowAccelChar,setShowAccelChar)
    def getShowCaption(self):
        r=LCLBinding.get_Buttons_TCustomSpeedButton_ShowCaption(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setShowCaption(self,v):
        LCLBinding.set_Buttons_TCustomSpeedButton_ShowCaption(self.pointer,v)
    ShowCaption=property(getShowCaption,setShowCaption)
    def getSpacing(self):
        r=LCLBinding.get_Buttons_TCustomSpeedButton_Spacing(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setSpacing(self,v):
        LCLBinding.set_Buttons_TCustomSpeedButton_Spacing(self.pointer,v)
    Spacing=property(getSpacing,setSpacing)
    def getTransparent(self):
        r=LCLBinding.get_Buttons_TCustomSpeedButton_Transparent(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setTransparent(self,v):
        LCLBinding.set_Buttons_TCustomSpeedButton_Transparent(self.pointer,v)
    Transparent=property(getTransparent,setTransparent)
#class TCustomSpeedButton end
#class TSpeedButton start
class TSpeedButton(TCustomSpeedButton):
#    pointer=c_void_p()
    def __init__(self):#TSpeedButton
        TCustomSpeedButton.__init__(self)
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
        self.OnDblClickPasObject=LCLBinding.set_Buttons_TSpeedButton_OnDblClick(self.pointer,self.PasOnDblClick,oldobj,FreeOldEvent)
    def getOnDblClick(self):
        return OnDblClickcall
    OnDblClick=property(getOnDblClick,setOnDblClick)
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
        self.OnMouseDownPasObject=LCLBinding.set_Buttons_TSpeedButton_OnMouseDown(self.pointer,self.PasOnMouseDown,oldobj,FreeOldEvent)
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
        self.OnMouseEnterPasObject=LCLBinding.set_Buttons_TSpeedButton_OnMouseEnter(self.pointer,self.PasOnMouseEnter,oldobj,FreeOldEvent)
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
        self.OnMouseLeavePasObject=LCLBinding.set_Buttons_TSpeedButton_OnMouseLeave(self.pointer,self.PasOnMouseLeave,oldobj,FreeOldEvent)
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
        self.OnMouseMovePasObject=LCLBinding.set_Buttons_TSpeedButton_OnMouseMove(self.pointer,self.PasOnMouseMove,oldobj,FreeOldEvent)
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
        self.OnMouseUpPasObject=LCLBinding.set_Buttons_TSpeedButton_OnMouseUp(self.pointer,self.PasOnMouseUp,oldobj,FreeOldEvent)
    def getOnMouseUp(self):
        return OnMouseUpcall
    OnMouseUp=property(getOnMouseUp,setOnMouseUp)
    def _Warper_OnPaint(self,Sender):
        self.OnPaintcall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnPaint(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnPaintcall'):
            FreeOldEvent=1
            oldobj=self.OnPaintPasObject
        self.OnPaintcall=v 
        self.PasOnPaint=FunctionForm(self._Warper_OnPaint)
        self.OnPaintPasObject=LCLBinding.set_Buttons_TSpeedButton_OnPaint(self.pointer,self.PasOnPaint,oldobj,FreeOldEvent)
    def getOnPaint(self):
        return OnPaintcall
    OnPaint=property(getOnPaint,setOnPaint)
    def getParentFont(self):
        r=LCLBinding.get_Buttons_TSpeedButton_ParentFont(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentFont(self,v):
        LCLBinding.set_Buttons_TSpeedButton_ParentFont(self.pointer,v)
    ParentFont=property(getParentFont,setParentFont)
    def getParentShowHint(self):
        r=LCLBinding.get_Buttons_TSpeedButton_ParentShowHint(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentShowHint(self,v):
        LCLBinding.set_Buttons_TSpeedButton_ParentShowHint(self.pointer,v)
    ParentShowHint=property(getParentShowHint,setParentShowHint)
#constructorButtons_TSpeedButton_Create
    @staticmethod
    def Create(AOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.Buttons_TSpeedButton_Create((AOwner.pointer)),TSpeedButton)
#class TSpeedButton end
#class TCustomBitBtn start
class TCustomBitBtn(TCustomButton):
#    pointer=c_void_p()
    def __init__(self):#TCustomBitBtn
        TCustomButton.__init__(self)
#constructorButtons_TCustomBitBtn_Create
    @staticmethod
    def Create(TheOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.Buttons_TCustomBitBtn_Create((TheOwner.pointer)),TCustomBitBtn)
#Procedure Buttons_TCustomBitBtn_Click
    @staticmethod
    def Click(self,):
        LCLBinding.Buttons_TCustomBitBtn_Click()
#Procedure Buttons_TCustomBitBtn_LoadGlyphFromLazarusResource
    @staticmethod
    def LoadGlyphFromLazarusResource(self,AName):
        LCLBinding.Buttons_TCustomBitBtn_LoadGlyphFromLazarusResource((AName))
#Procedure Buttons_TCustomBitBtn_LoadGlyphFromStock
    @staticmethod
    def LoadGlyphFromStock(self,idButton):
        LCLBinding.Buttons_TCustomBitBtn_LoadGlyphFromStock((idButton))
    def getDefaultCaption(self):
        r=LCLBinding.get_Buttons_TCustomBitBtn_DefaultCaption(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setDefaultCaption(self,v):
        LCLBinding.set_Buttons_TCustomBitBtn_DefaultCaption(self.pointer,v)
    DefaultCaption=property(getDefaultCaption,setDefaultCaption)
    def getGlyph(self):
        r=LCLBinding.get_Buttons_TCustomBitBtn_Glyph(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TBitmap)
    def setGlyph(self,v):
        LCLBinding.set_Buttons_TCustomBitBtn_Glyph(self.pointer,v.pointer)
    Glyph=property(getGlyph,setGlyph)
    def getNumGlyphs(self):
        r=LCLBinding.get_Buttons_TCustomBitBtn_NumGlyphs(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setNumGlyphs(self,v):
        LCLBinding.set_Buttons_TCustomBitBtn_NumGlyphs(self.pointer,v)
    NumGlyphs=property(getNumGlyphs,setNumGlyphs)
    def getKind(self):
        r=LCLBinding.get_Buttons_TCustomBitBtn_Kind(self.pointer)
        return r
    def setKind(self,v):
        LCLBinding.set_Buttons_TCustomBitBtn_Kind(self.pointer,v.pointer)
    Kind=property(getKind,setKind)
    def getLayout(self):
        r=LCLBinding.get_Buttons_TCustomBitBtn_Layout(self.pointer)
        return r
    def setLayout(self,v):
        LCLBinding.set_Buttons_TCustomBitBtn_Layout(self.pointer,v.pointer)
    Layout=property(getLayout,setLayout)
    def getMargin(self):
        r=LCLBinding.get_Buttons_TCustomBitBtn_Margin(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setMargin(self,v):
        LCLBinding.set_Buttons_TCustomBitBtn_Margin(self.pointer,v)
    Margin=property(getMargin,setMargin)
    def getSpacing(self):
        r=LCLBinding.get_Buttons_TCustomBitBtn_Spacing(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setSpacing(self,v):
        LCLBinding.set_Buttons_TCustomBitBtn_Spacing(self.pointer,v)
    Spacing=property(getSpacing,setSpacing)
    def getGlyphShowMode(self):
        r=LCLBinding.get_Buttons_TCustomBitBtn_GlyphShowMode(self.pointer)
        return r
    def setGlyphShowMode(self,v):
        LCLBinding.set_Buttons_TCustomBitBtn_GlyphShowMode(self.pointer,v.pointer)
    GlyphShowMode=property(getGlyphShowMode,setGlyphShowMode)
#class TCustomBitBtn end
#class TBitBtn start
class TBitBtn(TCustomBitBtn):
#    pointer=c_void_p()
    def __init__(self):#TBitBtn
        TCustomBitBtn.__init__(self)
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
        self.OnDragDropPasObject=LCLBinding.set_Buttons_TBitBtn_OnDragDrop(self.pointer,self.PasOnDragDrop,oldobj,FreeOldEvent)
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
        self.OnDragOverPasObject=LCLBinding.set_Buttons_TBitBtn_OnDragOver(self.pointer,self.PasOnDragOver,oldobj,FreeOldEvent)
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
            oldobj=self.OnEndDragPasObject
        self.OnEndDragcall=v 
        self.PasOnEndDrag=FunctionForm(self._Warper_OnEndDrag)
        self.OnEndDragPasObject=LCLBinding.set_Buttons_TBitBtn_OnEndDrag(self.pointer,self.PasOnEndDrag,oldobj,FreeOldEvent)
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
        self.OnMouseDownPasObject=LCLBinding.set_Buttons_TBitBtn_OnMouseDown(self.pointer,self.PasOnMouseDown,oldobj,FreeOldEvent)
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
        self.OnMouseEnterPasObject=LCLBinding.set_Buttons_TBitBtn_OnMouseEnter(self.pointer,self.PasOnMouseEnter,oldobj,FreeOldEvent)
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
        self.OnMouseLeavePasObject=LCLBinding.set_Buttons_TBitBtn_OnMouseLeave(self.pointer,self.PasOnMouseLeave,oldobj,FreeOldEvent)
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
        self.OnMouseMovePasObject=LCLBinding.set_Buttons_TBitBtn_OnMouseMove(self.pointer,self.PasOnMouseMove,oldobj,FreeOldEvent)
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
        self.OnMouseUpPasObject=LCLBinding.set_Buttons_TBitBtn_OnMouseUp(self.pointer,self.PasOnMouseUp,oldobj,FreeOldEvent)
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
            oldobj=self.OnStartDragPasObject
        self.OnStartDragcall=v 
        self.PasOnStartDrag=FunctionForm(self._Warper_OnStartDrag)
        self.OnStartDragPasObject=LCLBinding.set_Buttons_TBitBtn_OnStartDrag(self.pointer,self.PasOnStartDrag,oldobj,FreeOldEvent)
    def getOnStartDrag(self):
        return OnStartDragcall
    OnStartDrag=property(getOnStartDrag,setOnStartDrag)
    def getParentFont(self):
        r=LCLBinding.get_Buttons_TBitBtn_ParentFont(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentFont(self,v):
        LCLBinding.set_Buttons_TBitBtn_ParentFont(self.pointer,v)
    ParentFont=property(getParentFont,setParentFont)
    def getParentShowHint(self):
        r=LCLBinding.get_Buttons_TBitBtn_ParentShowHint(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentShowHint(self,v):
        LCLBinding.set_Buttons_TBitBtn_ParentShowHint(self.pointer,v)
    ParentShowHint=property(getParentShowHint,setParentShowHint)
#constructorButtons_TBitBtn_Create
    @staticmethod
    def Create(TheOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.Buttons_TBitBtn_Create((TheOwner.pointer)),TBitBtn)
#class TBitBtn end
