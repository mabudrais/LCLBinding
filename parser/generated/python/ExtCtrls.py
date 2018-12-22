from ImgList import *
from Menus import *
from LCLClasses import *
from customtimer import *
from Graphics import *
from GraphType import *
from StdCtrls import *
from Forms import *
from Controls import *
from Classes import *
from MainPasObject import *
import LCLBindingUtil
#import end
def CreateTBandPaintOptionsFromInt(i):
    dic={1:"bpoGrabber",2:"bpoFrame",4:"bpoGradient",8:"bpoRoundRect"}
    return CreateSetFormint(i,dic)
#class TCustomTrayIcon start
class TCustomTrayIcon(TLCLComponent):
#    pointer=c_void_p()
    def __init__(self):#TCustomTrayIcon
        TLCLComponent.__init__(self)
#constructorExtCtrls_TCustomTrayIcon_Create
    @staticmethod
    def Create(TheOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.ExtCtrls_TCustomTrayIcon_Create((TheOwner.pointer)),TCustomTrayIcon)
#Procedure ExtCtrls_TCustomTrayIcon_InternalUpdate
    @staticmethod
    def InternalUpdate(self,):
        LCLBinding.ExtCtrls_TCustomTrayIcon_InternalUpdate()
#Procedure ExtCtrls_TCustomTrayIcon_ShowBalloonHint
    @staticmethod
    def ShowBalloonHint(self,):
        LCLBinding.ExtCtrls_TCustomTrayIcon_ShowBalloonHint()
    def getAnimate(self):
        r=LCLBinding.get_ExtCtrls_TCustomTrayIcon_Animate(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setAnimate(self,v):
        LCLBinding.set_ExtCtrls_TCustomTrayIcon_Animate(self.pointer,v)
    Animate=property(getAnimate,setAnimate)
    def getBalloonFlags(self):
        r=LCLBinding.get_ExtCtrls_TCustomTrayIcon_BalloonFlags(self.pointer)
        return r
    def setBalloonFlags(self,v):
        LCLBinding.set_ExtCtrls_TCustomTrayIcon_BalloonFlags(self.pointer,v.pointer)
    BalloonFlags=property(getBalloonFlags,setBalloonFlags)
    def getBalloonHint(self):
        r=LCLBinding.get_ExtCtrls_TCustomTrayIcon_BalloonHint(self.pointer)
        return LCLBindingUtil.ConvertPascalstring(r)
    def setBalloonHint(self,v):
        LCLBinding.set_ExtCtrls_TCustomTrayIcon_BalloonHint(self.pointer,v)
    BalloonHint=property(getBalloonHint,setBalloonHint)
    def getBalloonTimeout(self):
        r=LCLBinding.get_ExtCtrls_TCustomTrayIcon_BalloonTimeout(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setBalloonTimeout(self,v):
        LCLBinding.set_ExtCtrls_TCustomTrayIcon_BalloonTimeout(self.pointer,v)
    BalloonTimeout=property(getBalloonTimeout,setBalloonTimeout)
    def getBalloonTitle(self):
        r=LCLBinding.get_ExtCtrls_TCustomTrayIcon_BalloonTitle(self.pointer)
        return LCLBindingUtil.ConvertPascalstring(r)
    def setBalloonTitle(self,v):
        LCLBinding.set_ExtCtrls_TCustomTrayIcon_BalloonTitle(self.pointer,v)
    BalloonTitle=property(getBalloonTitle,setBalloonTitle)
    def getCanvas(self):
        r=LCLBinding.get_ExtCtrls_TCustomTrayIcon_Canvas(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TCanvas)
    Canvas=property(getCanvas)
    def getPopUpMenu(self):
        r=LCLBinding.get_ExtCtrls_TCustomTrayIcon_PopUpMenu(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TPopupMenu)
    def setPopUpMenu(self,v):
        LCLBinding.set_ExtCtrls_TCustomTrayIcon_PopUpMenu(self.pointer,v.pointer)
    PopUpMenu=property(getPopUpMenu,setPopUpMenu)
    def getIcon(self):
        r=LCLBinding.get_ExtCtrls_TCustomTrayIcon_Icon(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TIcon)
    def setIcon(self,v):
        LCLBinding.set_ExtCtrls_TCustomTrayIcon_Icon(self.pointer,v.pointer)
    Icon=property(getIcon,setIcon)
    def getIcons(self):
        r=LCLBinding.get_ExtCtrls_TCustomTrayIcon_Icons(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TCustomImageList)
    def setIcons(self,v):
        LCLBinding.set_ExtCtrls_TCustomTrayIcon_Icons(self.pointer,v.pointer)
    Icons=property(getIcons,setIcons)
    def getHint(self):
        r=LCLBinding.get_ExtCtrls_TCustomTrayIcon_Hint(self.pointer)
        return LCLBindingUtil.ConvertPascalstring(r)
    def setHint(self,v):
        LCLBinding.set_ExtCtrls_TCustomTrayIcon_Hint(self.pointer,v)
    Hint=property(getHint,setHint)
    def getShowIcon(self):
        r=LCLBinding.get_ExtCtrls_TCustomTrayIcon_ShowIcon(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setShowIcon(self,v):
        LCLBinding.set_ExtCtrls_TCustomTrayIcon_ShowIcon(self.pointer,v)
    ShowIcon=property(getShowIcon,setShowIcon)
    def getVisible(self):
        r=LCLBinding.get_ExtCtrls_TCustomTrayIcon_Visible(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setVisible(self,v):
        LCLBinding.set_ExtCtrls_TCustomTrayIcon_Visible(self.pointer,v)
    Visible=property(getVisible,setVisible)
    def _Warper_OnClick(self,Sender):
        self.OnClickcall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnClick(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnClickcall'):
            FreeOldEvent=1
            oldobj=self.OnClickPasObject
        self.OnClickcall=v 
        self.PasOnClick=FunctionForm(self._Warper_OnClick)
        self.OnClickPasObject=LCLBinding.set_ExtCtrls_TCustomTrayIcon_OnClick(self.pointer,self.PasOnClick,oldobj,FreeOldEvent)
    def getOnClick(self):
        return OnClickcall
    OnClick=property(getOnClick,setOnClick)
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
        self.OnDblClickPasObject=LCLBinding.set_ExtCtrls_TCustomTrayIcon_OnDblClick(self.pointer,self.PasOnDblClick,oldobj,FreeOldEvent)
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
        self.OnMouseDownPasObject=LCLBinding.set_ExtCtrls_TCustomTrayIcon_OnMouseDown(self.pointer,self.PasOnMouseDown,oldobj,FreeOldEvent)
    def getOnMouseDown(self):
        return OnMouseDowncall
    OnMouseDown=property(getOnMouseDown,setOnMouseDown)
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
        self.OnMouseUpPasObject=LCLBinding.set_ExtCtrls_TCustomTrayIcon_OnMouseUp(self.pointer,self.PasOnMouseUp,oldobj,FreeOldEvent)
    def getOnMouseUp(self):
        return OnMouseUpcall
    OnMouseUp=property(getOnMouseUp,setOnMouseUp)
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
        self.OnMouseMovePasObject=LCLBinding.set_ExtCtrls_TCustomTrayIcon_OnMouseMove(self.pointer,self.PasOnMouseMove,oldobj,FreeOldEvent)
    def getOnMouseMove(self):
        return OnMouseMovecall
    OnMouseMove=property(getOnMouseMove,setOnMouseMove)
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
        self.OnPaintPasObject=LCLBinding.set_ExtCtrls_TCustomTrayIcon_OnPaint(self.pointer,self.PasOnPaint,oldobj,FreeOldEvent)
    def getOnPaint(self):
        return OnPaintcall
    OnPaint=property(getOnPaint,setOnPaint)
#class TCustomTrayIcon end
#class TTrayIcon start
class TTrayIcon(TCustomTrayIcon):
#    pointer=c_void_p()
    def __init__(self):#TTrayIcon
        TCustomTrayIcon.__init__(self)
#constructorExtCtrls_TTrayIcon_Create
    @staticmethod
    def Create(TheOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.ExtCtrls_TTrayIcon_Create((TheOwner.pointer)),TTrayIcon)
#class TTrayIcon end
#class TCustomSplitter start
class TCustomSplitter(TCustomControl):
#    pointer=c_void_p()
    def __init__(self):#TCustomSplitter
        TCustomControl.__init__(self)
#constructorExtCtrls_TCustomSplitter_Create
    @staticmethod
    def Create(TheOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.ExtCtrls_TCustomSplitter_Create((TheOwner.pointer)),TCustomSplitter)
#Procedure ExtCtrls_TCustomSplitter_AnchorSplitter
    @staticmethod
    def AnchorSplitter(self,Kind,AControl):
        LCLBinding.ExtCtrls_TCustomSplitter_AnchorSplitter((Kind.pointer),(AControl.pointer))
    def getResizeControl(self):
        r=LCLBinding.get_ExtCtrls_TCustomSplitter_ResizeControl(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TControl)
    def setResizeControl(self,v):
        LCLBinding.set_ExtCtrls_TCustomSplitter_ResizeControl(self.pointer,v.pointer)
    ResizeControl=property(getResizeControl,setResizeControl)
#Procedure ExtCtrls_TCustomSplitter_MoveSplitter
    @staticmethod
    def MoveSplitter(self,Offset):
        LCLBinding.ExtCtrls_TCustomSplitter_MoveSplitter((Offset))
#Procedure ExtCtrls_TCustomSplitter_SetSplitterPosition
    @staticmethod
    def SetSplitterPosition(self,NewPosition):
        LCLBinding.ExtCtrls_TCustomSplitter_SetSplitterPosition((NewPosition))
    def getAutoSnap(self):
        r=LCLBinding.get_ExtCtrls_TCustomSplitter_AutoSnap(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setAutoSnap(self,v):
        LCLBinding.set_ExtCtrls_TCustomSplitter_AutoSnap(self.pointer,v)
    AutoSnap=property(getAutoSnap,setAutoSnap)
    def getBeveled(self):
        r=LCLBinding.get_ExtCtrls_TCustomSplitter_Beveled(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setBeveled(self,v):
        LCLBinding.set_ExtCtrls_TCustomSplitter_Beveled(self.pointer,v)
    Beveled=property(getBeveled,setBeveled)
    def getMinSize(self):
        r=LCLBinding.get_ExtCtrls_TCustomSplitter_MinSize(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setMinSize(self,v):
        LCLBinding.set_ExtCtrls_TCustomSplitter_MinSize(self.pointer,v)
    MinSize=property(getMinSize,setMinSize)
    def _Warper_OnCanOffset(self,Sender,NewOffset,Accept):
        self.OnCanOffsetcall(LCLBindingUtil.GetPytonObject(Sender,TObject),NewOffset,LCLBindingUtil.IntToBoolean(Accept))
    def setOnCanOffset(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnCanOffsetcall'):
            FreeOldEvent=1
            oldobj=self.OnCanOffsetPasObject
        self.OnCanOffsetcall=v 
        self.PasOnCanOffset=FunctionForm(self._Warper_OnCanOffset)
        self.OnCanOffsetPasObject=LCLBinding.set_ExtCtrls_TCustomSplitter_OnCanOffset(self.pointer,self.PasOnCanOffset,oldobj,FreeOldEvent)
    def getOnCanOffset(self):
        return OnCanOffsetcall
    OnCanOffset=property(getOnCanOffset,setOnCanOffset)
    def _Warper_OnCanResize(self,Sender,NewSize,Accept):
        self.OnCanResizecall(LCLBindingUtil.GetPytonObject(Sender,TObject),NewSize,LCLBindingUtil.IntToBoolean(Accept))
    def setOnCanResize(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnCanResizecall'):
            FreeOldEvent=1
            oldobj=self.OnCanResizePasObject
        self.OnCanResizecall=v 
        self.PasOnCanResize=FunctionForm(self._Warper_OnCanResize)
        self.OnCanResizePasObject=LCLBinding.set_ExtCtrls_TCustomSplitter_OnCanResize(self.pointer,self.PasOnCanResize,oldobj,FreeOldEvent)
    def getOnCanResize(self):
        return OnCanResizecall
    OnCanResize=property(getOnCanResize,setOnCanResize)
    def _Warper_OnMoved(self,Sender):
        self.OnMovedcall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnMoved(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnMovedcall'):
            FreeOldEvent=1
            oldobj=self.OnMovedPasObject
        self.OnMovedcall=v 
        self.PasOnMoved=FunctionForm(self._Warper_OnMoved)
        self.OnMovedPasObject=LCLBinding.set_ExtCtrls_TCustomSplitter_OnMoved(self.pointer,self.PasOnMoved,oldobj,FreeOldEvent)
    def getOnMoved(self):
        return OnMovedcall
    OnMoved=property(getOnMoved,setOnMoved)
    def getResizeAnchor(self):
        r=LCLBinding.get_ExtCtrls_TCustomSplitter_ResizeAnchor(self.pointer)
        return r
    def setResizeAnchor(self,v):
        LCLBinding.set_ExtCtrls_TCustomSplitter_ResizeAnchor(self.pointer,v.pointer)
    ResizeAnchor=property(getResizeAnchor,setResizeAnchor)
    def getResizeStyle(self):
        r=LCLBinding.get_ExtCtrls_TCustomSplitter_ResizeStyle(self.pointer)
        return r
    def setResizeStyle(self,v):
        LCLBinding.set_ExtCtrls_TCustomSplitter_ResizeStyle(self.pointer,v.pointer)
    ResizeStyle=property(getResizeStyle,setResizeStyle)
#class TCustomSplitter end
#class TSplitter start
class TSplitter(TCustomSplitter):
#    pointer=c_void_p()
    def __init__(self):#TSplitter
        TCustomSplitter.__init__(self)
    def getParentColor(self):
        r=LCLBinding.get_ExtCtrls_TSplitter_ParentColor(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentColor(self,v):
        LCLBinding.set_ExtCtrls_TSplitter_ParentColor(self.pointer,v)
    ParentColor=property(getParentColor,setParentColor)
    def getParentShowHint(self):
        r=LCLBinding.get_ExtCtrls_TSplitter_ParentShowHint(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentShowHint(self,v):
        LCLBinding.set_ExtCtrls_TSplitter_ParentShowHint(self.pointer,v)
    ParentShowHint=property(getParentShowHint,setParentShowHint)
#constructorExtCtrls_TSplitter_Create
    @staticmethod
    def Create(TheOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.ExtCtrls_TSplitter_Create((TheOwner.pointer)),TSplitter)
#class TSplitter end
#class TShape start
class TShape(TGraphicControl):
#    pointer=c_void_p()
    def __init__(self):#TShape
        TGraphicControl.__init__(self)
#constructorExtCtrls_TShape_Create
    @staticmethod
    def Create(TheOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.ExtCtrls_TShape_Create((TheOwner.pointer)),TShape)
#Procedure ExtCtrls_TShape_Paint
    @staticmethod
    def Paint(self,):
        LCLBinding.ExtCtrls_TShape_Paint()
#Procedure ExtCtrls_TShape_StyleChanged
    @staticmethod
    def StyleChanged(self,Sender):
        LCLBinding.ExtCtrls_TShape_StyleChanged((Sender.pointer))
    def getBrush(self):
        r=LCLBinding.get_ExtCtrls_TShape_Brush(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TBrush)
    def setBrush(self,v):
        LCLBinding.set_ExtCtrls_TShape_Brush(self.pointer,v.pointer)
    Brush=property(getBrush,setBrush)
    def getDragKind(self):
        r=LCLBinding.get_ExtCtrls_TShape_DragKind(self.pointer)
        return r
    def setDragKind(self,v):
        LCLBinding.set_ExtCtrls_TShape_DragKind(self.pointer,v.pointer)
    DragKind=property(getDragKind,setDragKind)
    def getDragMode(self):
        r=LCLBinding.get_ExtCtrls_TShape_DragMode(self.pointer)
        return r
    def setDragMode(self,v):
        LCLBinding.set_ExtCtrls_TShape_DragMode(self.pointer,v.pointer)
    DragMode=property(getDragMode,setDragMode)
    def getParentShowHint(self):
        r=LCLBinding.get_ExtCtrls_TShape_ParentShowHint(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentShowHint(self,v):
        LCLBinding.set_ExtCtrls_TShape_ParentShowHint(self.pointer,v)
    ParentShowHint=property(getParentShowHint,setParentShowHint)
    def getPen(self):
        r=LCLBinding.get_ExtCtrls_TShape_Pen(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TPen)
    def setPen(self,v):
        LCLBinding.set_ExtCtrls_TShape_Pen(self.pointer,v.pointer)
    Pen=property(getPen,setPen)
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
        self.OnDragDropPasObject=LCLBinding.set_ExtCtrls_TShape_OnDragDrop(self.pointer,self.PasOnDragDrop,oldobj,FreeOldEvent)
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
        self.OnDragOverPasObject=LCLBinding.set_ExtCtrls_TShape_OnDragOver(self.pointer,self.PasOnDragOver,oldobj,FreeOldEvent)
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
            oldobj=self.OnEndDockPasObject
        self.OnEndDockcall=v 
        self.PasOnEndDock=FunctionForm(self._Warper_OnEndDock)
        self.OnEndDockPasObject=LCLBinding.set_ExtCtrls_TShape_OnEndDock(self.pointer,self.PasOnEndDock,oldobj,FreeOldEvent)
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
        self.OnEndDragPasObject=LCLBinding.set_ExtCtrls_TShape_OnEndDrag(self.pointer,self.PasOnEndDrag,oldobj,FreeOldEvent)
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
        self.OnMouseDownPasObject=LCLBinding.set_ExtCtrls_TShape_OnMouseDown(self.pointer,self.PasOnMouseDown,oldobj,FreeOldEvent)
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
        self.OnMouseEnterPasObject=LCLBinding.set_ExtCtrls_TShape_OnMouseEnter(self.pointer,self.PasOnMouseEnter,oldobj,FreeOldEvent)
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
        self.OnMouseLeavePasObject=LCLBinding.set_ExtCtrls_TShape_OnMouseLeave(self.pointer,self.PasOnMouseLeave,oldobj,FreeOldEvent)
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
        self.OnMouseMovePasObject=LCLBinding.set_ExtCtrls_TShape_OnMouseMove(self.pointer,self.PasOnMouseMove,oldobj,FreeOldEvent)
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
        self.OnMouseUpPasObject=LCLBinding.set_ExtCtrls_TShape_OnMouseUp(self.pointer,self.PasOnMouseUp,oldobj,FreeOldEvent)
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
        self.OnPaintPasObject=LCLBinding.set_ExtCtrls_TShape_OnPaint(self.pointer,self.PasOnPaint,oldobj,FreeOldEvent)
    def getOnPaint(self):
        return OnPaintcall
    OnPaint=property(getOnPaint,setOnPaint)
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
        self.OnStartDockPasObject=LCLBinding.set_ExtCtrls_TShape_OnStartDock(self.pointer,self.PasOnStartDock,oldobj,FreeOldEvent)
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
        self.OnStartDragPasObject=LCLBinding.set_ExtCtrls_TShape_OnStartDrag(self.pointer,self.PasOnStartDrag,oldobj,FreeOldEvent)
    def getOnStartDrag(self):
        return OnStartDragcall
    OnStartDrag=property(getOnStartDrag,setOnStartDrag)
    def getShape(self):
        r=LCLBinding.get_ExtCtrls_TShape_Shape(self.pointer)
        return r
    def setShape(self,v):
        LCLBinding.set_ExtCtrls_TShape_Shape(self.pointer,v.pointer)
    Shape=property(getShape,setShape)
#class TShape end
#class TPaintBox start
class TPaintBox(TGraphicControl):
#    pointer=c_void_p()
    def __init__(self):#TPaintBox
        TGraphicControl.__init__(self)
#constructorExtCtrls_TPaintBox_Create
    @staticmethod
    def Create(AOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.ExtCtrls_TPaintBox_Create((AOwner.pointer)),TPaintBox)
    def getDragMode(self):
        r=LCLBinding.get_ExtCtrls_TPaintBox_DragMode(self.pointer)
        return r
    def setDragMode(self,v):
        LCLBinding.set_ExtCtrls_TPaintBox_DragMode(self.pointer,v.pointer)
    DragMode=property(getDragMode,setDragMode)
    def getParentColor(self):
        r=LCLBinding.get_ExtCtrls_TPaintBox_ParentColor(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentColor(self,v):
        LCLBinding.set_ExtCtrls_TPaintBox_ParentColor(self.pointer,v)
    ParentColor=property(getParentColor,setParentColor)
    def getParentFont(self):
        r=LCLBinding.get_ExtCtrls_TPaintBox_ParentFont(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentFont(self,v):
        LCLBinding.set_ExtCtrls_TPaintBox_ParentFont(self.pointer,v)
    ParentFont=property(getParentFont,setParentFont)
    def getParentShowHint(self):
        r=LCLBinding.get_ExtCtrls_TPaintBox_ParentShowHint(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentShowHint(self,v):
        LCLBinding.set_ExtCtrls_TPaintBox_ParentShowHint(self.pointer,v)
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
        self.OnDblClickPasObject=LCLBinding.set_ExtCtrls_TPaintBox_OnDblClick(self.pointer,self.PasOnDblClick,oldobj,FreeOldEvent)
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
        self.OnDragDropPasObject=LCLBinding.set_ExtCtrls_TPaintBox_OnDragDrop(self.pointer,self.PasOnDragDrop,oldobj,FreeOldEvent)
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
        self.OnDragOverPasObject=LCLBinding.set_ExtCtrls_TPaintBox_OnDragOver(self.pointer,self.PasOnDragOver,oldobj,FreeOldEvent)
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
        self.OnEndDragPasObject=LCLBinding.set_ExtCtrls_TPaintBox_OnEndDrag(self.pointer,self.PasOnEndDrag,oldobj,FreeOldEvent)
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
        self.OnMouseDownPasObject=LCLBinding.set_ExtCtrls_TPaintBox_OnMouseDown(self.pointer,self.PasOnMouseDown,oldobj,FreeOldEvent)
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
        self.OnMouseEnterPasObject=LCLBinding.set_ExtCtrls_TPaintBox_OnMouseEnter(self.pointer,self.PasOnMouseEnter,oldobj,FreeOldEvent)
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
        self.OnMouseLeavePasObject=LCLBinding.set_ExtCtrls_TPaintBox_OnMouseLeave(self.pointer,self.PasOnMouseLeave,oldobj,FreeOldEvent)
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
        self.OnMouseMovePasObject=LCLBinding.set_ExtCtrls_TPaintBox_OnMouseMove(self.pointer,self.PasOnMouseMove,oldobj,FreeOldEvent)
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
        self.OnMouseUpPasObject=LCLBinding.set_ExtCtrls_TPaintBox_OnMouseUp(self.pointer,self.PasOnMouseUp,oldobj,FreeOldEvent)
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
        self.OnPaintPasObject=LCLBinding.set_ExtCtrls_TPaintBox_OnPaint(self.pointer,self.PasOnPaint,oldobj,FreeOldEvent)
    def getOnPaint(self):
        return OnPaintcall
    OnPaint=property(getOnPaint,setOnPaint)
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
        self.OnStartDragPasObject=LCLBinding.set_ExtCtrls_TPaintBox_OnStartDrag(self.pointer,self.PasOnStartDrag,oldobj,FreeOldEvent)
    def getOnStartDrag(self):
        return OnStartDragcall
    OnStartDrag=property(getOnStartDrag,setOnStartDrag)
#class TPaintBox end
#class TPage start
class TPage(TCustomControl):
#    pointer=c_void_p()
    def __init__(self):#TPage
        TCustomControl.__init__(self)
#constructorExtCtrls_TPage_Create
    @staticmethod
    def Create(TheOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.ExtCtrls_TPage_Create((TheOwner.pointer)),TPage)
    def getPageIndex(self):
        r=LCLBinding.get_ExtCtrls_TPage_PageIndex(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    PageIndex=property(getPageIndex)
    def _Warper_OnBeforeShow(self,ASender,ANewPage,ANewIndex):
        self.OnBeforeShowcall(LCLBindingUtil.GetPytonObject(ASender,TObject),LCLBindingUtil.GetPytonObject(ANewPage,TPage),ANewIndex)
    def setOnBeforeShow(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnBeforeShowcall'):
            FreeOldEvent=1
            oldobj=self.OnBeforeShowPasObject
        self.OnBeforeShowcall=v 
        self.PasOnBeforeShow=FunctionForm(self._Warper_OnBeforeShow)
        self.OnBeforeShowPasObject=LCLBinding.set_ExtCtrls_TPage_OnBeforeShow(self.pointer,self.PasOnBeforeShow,oldobj,FreeOldEvent)
    def getOnBeforeShow(self):
        return OnBeforeShowcall
    OnBeforeShow=property(getOnBeforeShow,setOnBeforeShow)
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
        self.OnMouseDownPasObject=LCLBinding.set_ExtCtrls_TPage_OnMouseDown(self.pointer,self.PasOnMouseDown,oldobj,FreeOldEvent)
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
        self.OnMouseEnterPasObject=LCLBinding.set_ExtCtrls_TPage_OnMouseEnter(self.pointer,self.PasOnMouseEnter,oldobj,FreeOldEvent)
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
        self.OnMouseLeavePasObject=LCLBinding.set_ExtCtrls_TPage_OnMouseLeave(self.pointer,self.PasOnMouseLeave,oldobj,FreeOldEvent)
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
        self.OnMouseMovePasObject=LCLBinding.set_ExtCtrls_TPage_OnMouseMove(self.pointer,self.PasOnMouseMove,oldobj,FreeOldEvent)
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
        self.OnMouseUpPasObject=LCLBinding.set_ExtCtrls_TPage_OnMouseUp(self.pointer,self.PasOnMouseUp,oldobj,FreeOldEvent)
    def getOnMouseUp(self):
        return OnMouseUpcall
    OnMouseUp=property(getOnMouseUp,setOnMouseUp)
    def getParentShowHint(self):
        r=LCLBinding.get_ExtCtrls_TPage_ParentShowHint(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentShowHint(self,v):
        LCLBinding.set_ExtCtrls_TPage_ParentShowHint(self.pointer,v)
    ParentShowHint=property(getParentShowHint,setParentShowHint)
#class TPage end
#class TNotebook start
class TNotebook(TCustomControl):
#    pointer=c_void_p()
    def __init__(self):#TNotebook
        TCustomControl.__init__(self)
#constructorExtCtrls_TNotebook_Create
    @staticmethod
    def Create(TheOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.ExtCtrls_TNotebook_Create((TheOwner.pointer)),TNotebook)
#Procedure ExtCtrls_TNotebook_ShowControl
    @staticmethod
    def ShowControl(self,AControl):
        LCLBinding.ExtCtrls_TNotebook_ShowControl((AControl.pointer))
    def getActivePage(self):
        r=LCLBinding.get_ExtCtrls_TNotebook_ActivePage(self.pointer)
        return LCLBindingUtil.ConvertPascalstring(r)
    ActivePage=property(getActivePage)
    def getActivePageComponent(self):
        r=LCLBinding.get_ExtCtrls_TNotebook_ActivePageComponent(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TPage)
    ActivePageComponent=property(getActivePageComponent)
    def getPage(self,Index):
        r=LCLBinding.get_ExtCtrls_TNotebook_Page(self.pointer,Index)
        return LCLBindingUtil.GetPytonObject(r,TPage)
    def getPageCount(self):
        r=LCLBinding.get_ExtCtrls_TNotebook_PageCount(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    PageCount=property(getPageCount)
    def getPageIndex(self):
        r=LCLBinding.get_ExtCtrls_TNotebook_PageIndex(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setPageIndex(self,v):
        LCLBinding.set_ExtCtrls_TNotebook_PageIndex(self.pointer,v)
    PageIndex=property(getPageIndex,setPageIndex)
    def getPages(self):
        r=LCLBinding.get_ExtCtrls_TNotebook_Pages(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TStrings)
    def setPages(self,v):
        LCLBinding.set_ExtCtrls_TNotebook_Pages(self.pointer,v.pointer)
    Pages=property(getPages,setPages)
    def getDragMode(self):
        r=LCLBinding.get_ExtCtrls_TNotebook_DragMode(self.pointer)
        return r
    def setDragMode(self,v):
        LCLBinding.set_ExtCtrls_TNotebook_DragMode(self.pointer,v.pointer)
    DragMode=property(getDragMode,setDragMode)
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
        self.OnDragDropPasObject=LCLBinding.set_ExtCtrls_TNotebook_OnDragDrop(self.pointer,self.PasOnDragDrop,oldobj,FreeOldEvent)
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
        self.OnDragOverPasObject=LCLBinding.set_ExtCtrls_TNotebook_OnDragOver(self.pointer,self.PasOnDragOver,oldobj,FreeOldEvent)
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
        self.OnEndDragPasObject=LCLBinding.set_ExtCtrls_TNotebook_OnEndDrag(self.pointer,self.PasOnEndDrag,oldobj,FreeOldEvent)
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
        self.OnMouseDownPasObject=LCLBinding.set_ExtCtrls_TNotebook_OnMouseDown(self.pointer,self.PasOnMouseDown,oldobj,FreeOldEvent)
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
        self.OnMouseEnterPasObject=LCLBinding.set_ExtCtrls_TNotebook_OnMouseEnter(self.pointer,self.PasOnMouseEnter,oldobj,FreeOldEvent)
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
        self.OnMouseLeavePasObject=LCLBinding.set_ExtCtrls_TNotebook_OnMouseLeave(self.pointer,self.PasOnMouseLeave,oldobj,FreeOldEvent)
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
        self.OnMouseMovePasObject=LCLBinding.set_ExtCtrls_TNotebook_OnMouseMove(self.pointer,self.PasOnMouseMove,oldobj,FreeOldEvent)
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
        self.OnMouseUpPasObject=LCLBinding.set_ExtCtrls_TNotebook_OnMouseUp(self.pointer,self.PasOnMouseUp,oldobj,FreeOldEvent)
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
        self.OnStartDragPasObject=LCLBinding.set_ExtCtrls_TNotebook_OnStartDrag(self.pointer,self.PasOnStartDrag,oldobj,FreeOldEvent)
    def getOnStartDrag(self):
        return OnStartDragcall
    OnStartDrag=property(getOnStartDrag,setOnStartDrag)
#class TNotebook end
#class TBoundLabel start
class TBoundLabel(TCustomLabel):
#    pointer=c_void_p()
    def __init__(self):#TBoundLabel
        TCustomLabel.__init__(self)
#constructorExtCtrls_TBoundLabel_Create
    @staticmethod
    def Create(TheOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.ExtCtrls_TBoundLabel_Create((TheOwner.pointer)),TBoundLabel)
    def getFocusControl(self):
        r=LCLBinding.get_ExtCtrls_TBoundLabel_FocusControl(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TWinControl)
    def setFocusControl(self,v):
        LCLBinding.set_ExtCtrls_TBoundLabel_FocusControl(self.pointer,v.pointer)
    FocusControl=property(getFocusControl,setFocusControl)
    def getDragMode(self):
        r=LCLBinding.get_ExtCtrls_TBoundLabel_DragMode(self.pointer)
        return r
    def setDragMode(self,v):
        LCLBinding.set_ExtCtrls_TBoundLabel_DragMode(self.pointer,v.pointer)
    DragMode=property(getDragMode,setDragMode)
    def getParentColor(self):
        r=LCLBinding.get_ExtCtrls_TBoundLabel_ParentColor(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentColor(self,v):
        LCLBinding.set_ExtCtrls_TBoundLabel_ParentColor(self.pointer,v)
    ParentColor=property(getParentColor,setParentColor)
    def getParentFont(self):
        r=LCLBinding.get_ExtCtrls_TBoundLabel_ParentFont(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentFont(self,v):
        LCLBinding.set_ExtCtrls_TBoundLabel_ParentFont(self.pointer,v)
    ParentFont=property(getParentFont,setParentFont)
    def getParentShowHint(self):
        r=LCLBinding.get_ExtCtrls_TBoundLabel_ParentShowHint(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentShowHint(self,v):
        LCLBinding.set_ExtCtrls_TBoundLabel_ParentShowHint(self.pointer,v)
    ParentShowHint=property(getParentShowHint,setParentShowHint)
    def getShowAccelChar(self):
        r=LCLBinding.get_ExtCtrls_TBoundLabel_ShowAccelChar(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setShowAccelChar(self,v):
        LCLBinding.set_ExtCtrls_TBoundLabel_ShowAccelChar(self.pointer,v)
    ShowAccelChar=property(getShowAccelChar,setShowAccelChar)
    def getLayout(self):
        r=LCLBinding.get_ExtCtrls_TBoundLabel_Layout(self.pointer)
        return r
    def setLayout(self,v):
        LCLBinding.set_ExtCtrls_TBoundLabel_Layout(self.pointer,v.pointer)
    Layout=property(getLayout,setLayout)
    def getWordWrap(self):
        r=LCLBinding.get_ExtCtrls_TBoundLabel_WordWrap(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setWordWrap(self,v):
        LCLBinding.set_ExtCtrls_TBoundLabel_WordWrap(self.pointer,v)
    WordWrap=property(getWordWrap,setWordWrap)
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
        self.OnDblClickPasObject=LCLBinding.set_ExtCtrls_TBoundLabel_OnDblClick(self.pointer,self.PasOnDblClick,oldobj,FreeOldEvent)
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
        self.OnDragDropPasObject=LCLBinding.set_ExtCtrls_TBoundLabel_OnDragDrop(self.pointer,self.PasOnDragDrop,oldobj,FreeOldEvent)
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
        self.OnDragOverPasObject=LCLBinding.set_ExtCtrls_TBoundLabel_OnDragOver(self.pointer,self.PasOnDragOver,oldobj,FreeOldEvent)
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
        self.OnEndDragPasObject=LCLBinding.set_ExtCtrls_TBoundLabel_OnEndDrag(self.pointer,self.PasOnEndDrag,oldobj,FreeOldEvent)
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
        self.OnMouseDownPasObject=LCLBinding.set_ExtCtrls_TBoundLabel_OnMouseDown(self.pointer,self.PasOnMouseDown,oldobj,FreeOldEvent)
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
        self.OnMouseEnterPasObject=LCLBinding.set_ExtCtrls_TBoundLabel_OnMouseEnter(self.pointer,self.PasOnMouseEnter,oldobj,FreeOldEvent)
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
        self.OnMouseLeavePasObject=LCLBinding.set_ExtCtrls_TBoundLabel_OnMouseLeave(self.pointer,self.PasOnMouseLeave,oldobj,FreeOldEvent)
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
        self.OnMouseMovePasObject=LCLBinding.set_ExtCtrls_TBoundLabel_OnMouseMove(self.pointer,self.PasOnMouseMove,oldobj,FreeOldEvent)
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
        self.OnMouseUpPasObject=LCLBinding.set_ExtCtrls_TBoundLabel_OnMouseUp(self.pointer,self.PasOnMouseUp,oldobj,FreeOldEvent)
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
        self.OnStartDragPasObject=LCLBinding.set_ExtCtrls_TBoundLabel_OnStartDrag(self.pointer,self.PasOnStartDrag,oldobj,FreeOldEvent)
    def getOnStartDrag(self):
        return OnStartDragcall
    OnStartDrag=property(getOnStartDrag,setOnStartDrag)
#class TBoundLabel end
#class TCustomLabeledEdit start
class TCustomLabeledEdit(TCustomEdit):
#    pointer=c_void_p()
    def __init__(self):#TCustomLabeledEdit
        TCustomEdit.__init__(self)
#constructorExtCtrls_TCustomLabeledEdit_Create
    @staticmethod
    def Create(TheOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.ExtCtrls_TCustomLabeledEdit_Create((TheOwner.pointer)),TCustomLabeledEdit)
    def getEditLabel(self):
        r=LCLBinding.get_ExtCtrls_TCustomLabeledEdit_EditLabel(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TBoundLabel)
    EditLabel=property(getEditLabel)
    def getLabelPosition(self):
        r=LCLBinding.get_ExtCtrls_TCustomLabeledEdit_LabelPosition(self.pointer)
        return r
    def setLabelPosition(self,v):
        LCLBinding.set_ExtCtrls_TCustomLabeledEdit_LabelPosition(self.pointer,v.pointer)
    LabelPosition=property(getLabelPosition,setLabelPosition)
    def getLabelSpacing(self):
        r=LCLBinding.get_ExtCtrls_TCustomLabeledEdit_LabelSpacing(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setLabelSpacing(self,v):
        LCLBinding.set_ExtCtrls_TCustomLabeledEdit_LabelSpacing(self.pointer,v)
    LabelSpacing=property(getLabelSpacing,setLabelSpacing)
#class TCustomLabeledEdit end
#class TLabeledEdit start
class TLabeledEdit(TCustomLabeledEdit):
#    pointer=c_void_p()
    def __init__(self):#TLabeledEdit
        TCustomLabeledEdit.__init__(self)
    def getAutoSelect(self):
        r=LCLBinding.get_ExtCtrls_TLabeledEdit_AutoSelect(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setAutoSelect(self,v):
        LCLBinding.set_ExtCtrls_TLabeledEdit_AutoSelect(self.pointer,v)
    AutoSelect=property(getAutoSelect,setAutoSelect)
    def getDragMode(self):
        r=LCLBinding.get_ExtCtrls_TLabeledEdit_DragMode(self.pointer)
        return r
    def setDragMode(self,v):
        LCLBinding.set_ExtCtrls_TLabeledEdit_DragMode(self.pointer,v.pointer)
    DragMode=property(getDragMode,setDragMode)
    def getParentColor(self):
        r=LCLBinding.get_ExtCtrls_TLabeledEdit_ParentColor(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentColor(self,v):
        LCLBinding.set_ExtCtrls_TLabeledEdit_ParentColor(self.pointer,v)
    ParentColor=property(getParentColor,setParentColor)
    def getParentFont(self):
        r=LCLBinding.get_ExtCtrls_TLabeledEdit_ParentFont(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentFont(self,v):
        LCLBinding.set_ExtCtrls_TLabeledEdit_ParentFont(self.pointer,v)
    ParentFont=property(getParentFont,setParentFont)
    def getParentShowHint(self):
        r=LCLBinding.get_ExtCtrls_TLabeledEdit_ParentShowHint(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentShowHint(self,v):
        LCLBinding.set_ExtCtrls_TLabeledEdit_ParentShowHint(self.pointer,v)
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
        self.OnDblClickPasObject=LCLBinding.set_ExtCtrls_TLabeledEdit_OnDblClick(self.pointer,self.PasOnDblClick,oldobj,FreeOldEvent)
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
        self.OnDragDropPasObject=LCLBinding.set_ExtCtrls_TLabeledEdit_OnDragDrop(self.pointer,self.PasOnDragDrop,oldobj,FreeOldEvent)
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
        self.OnDragOverPasObject=LCLBinding.set_ExtCtrls_TLabeledEdit_OnDragOver(self.pointer,self.PasOnDragOver,oldobj,FreeOldEvent)
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
        self.OnEditingDonePasObject=LCLBinding.set_ExtCtrls_TLabeledEdit_OnEditingDone(self.pointer,self.PasOnEditingDone,oldobj,FreeOldEvent)
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
            oldobj=self.OnEndDragPasObject
        self.OnEndDragcall=v 
        self.PasOnEndDrag=FunctionForm(self._Warper_OnEndDrag)
        self.OnEndDragPasObject=LCLBinding.set_ExtCtrls_TLabeledEdit_OnEndDrag(self.pointer,self.PasOnEndDrag,oldobj,FreeOldEvent)
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
        self.OnMouseDownPasObject=LCLBinding.set_ExtCtrls_TLabeledEdit_OnMouseDown(self.pointer,self.PasOnMouseDown,oldobj,FreeOldEvent)
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
        self.OnMouseEnterPasObject=LCLBinding.set_ExtCtrls_TLabeledEdit_OnMouseEnter(self.pointer,self.PasOnMouseEnter,oldobj,FreeOldEvent)
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
        self.OnMouseLeavePasObject=LCLBinding.set_ExtCtrls_TLabeledEdit_OnMouseLeave(self.pointer,self.PasOnMouseLeave,oldobj,FreeOldEvent)
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
        self.OnMouseMovePasObject=LCLBinding.set_ExtCtrls_TLabeledEdit_OnMouseMove(self.pointer,self.PasOnMouseMove,oldobj,FreeOldEvent)
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
        self.OnMouseUpPasObject=LCLBinding.set_ExtCtrls_TLabeledEdit_OnMouseUp(self.pointer,self.PasOnMouseUp,oldobj,FreeOldEvent)
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
        self.OnStartDragPasObject=LCLBinding.set_ExtCtrls_TLabeledEdit_OnStartDrag(self.pointer,self.PasOnStartDrag,oldobj,FreeOldEvent)
    def getOnStartDrag(self):
        return OnStartDragcall
    OnStartDrag=property(getOnStartDrag,setOnStartDrag)
#constructorExtCtrls_TLabeledEdit_Create
    @staticmethod
    def Create(TheOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.ExtCtrls_TLabeledEdit_Create((TheOwner.pointer)),TLabeledEdit)
#class TLabeledEdit end
#class TCustomImage start
class TCustomImage(TGraphicControl):
#    pointer=c_void_p()
    def __init__(self):#TCustomImage
        TGraphicControl.__init__(self)
#constructorExtCtrls_TCustomImage_Create
    @staticmethod
    def Create(AOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.ExtCtrls_TCustomImage_Create((AOwner.pointer)),TCustomImage)
    def getCanvas(self):
        r=LCLBinding.get_ExtCtrls_TCustomImage_Canvas(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TCanvas)
    Canvas=property(getCanvas)
#Procedure ExtCtrls_TCustomImage_Invalidate
    @staticmethod
    def Invalidate(self,):
        LCLBinding.ExtCtrls_TCustomImage_Invalidate()
    def getAntialiasingMode(self):
        r=LCLBinding.get_ExtCtrls_TCustomImage_AntialiasingMode(self.pointer)
        return r
    def setAntialiasingMode(self,v):
        LCLBinding.set_ExtCtrls_TCustomImage_AntialiasingMode(self.pointer,v.pointer)
    AntialiasingMode=property(getAntialiasingMode,setAntialiasingMode)
    def getCenter(self):
        r=LCLBinding.get_ExtCtrls_TCustomImage_Center(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setCenter(self,v):
        LCLBinding.set_ExtCtrls_TCustomImage_Center(self.pointer,v)
    Center=property(getCenter,setCenter)
    def getKeepOriginXWhenClipped(self):
        r=LCLBinding.get_ExtCtrls_TCustomImage_KeepOriginXWhenClipped(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setKeepOriginXWhenClipped(self,v):
        LCLBinding.set_ExtCtrls_TCustomImage_KeepOriginXWhenClipped(self.pointer,v)
    KeepOriginXWhenClipped=property(getKeepOriginXWhenClipped,setKeepOriginXWhenClipped)
    def getKeepOriginYWhenClipped(self):
        r=LCLBinding.get_ExtCtrls_TCustomImage_KeepOriginYWhenClipped(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setKeepOriginYWhenClipped(self,v):
        LCLBinding.set_ExtCtrls_TCustomImage_KeepOriginYWhenClipped(self.pointer,v)
    KeepOriginYWhenClipped=property(getKeepOriginYWhenClipped,setKeepOriginYWhenClipped)
    def getPicture(self):
        r=LCLBinding.get_ExtCtrls_TCustomImage_Picture(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TPicture)
    def setPicture(self,v):
        LCLBinding.set_ExtCtrls_TCustomImage_Picture(self.pointer,v.pointer)
    Picture=property(getPicture,setPicture)
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
        self.OnMouseDownPasObject=LCLBinding.set_ExtCtrls_TCustomImage_OnMouseDown(self.pointer,self.PasOnMouseDown,oldobj,FreeOldEvent)
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
        self.OnMouseEnterPasObject=LCLBinding.set_ExtCtrls_TCustomImage_OnMouseEnter(self.pointer,self.PasOnMouseEnter,oldobj,FreeOldEvent)
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
        self.OnMouseLeavePasObject=LCLBinding.set_ExtCtrls_TCustomImage_OnMouseLeave(self.pointer,self.PasOnMouseLeave,oldobj,FreeOldEvent)
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
        self.OnMouseMovePasObject=LCLBinding.set_ExtCtrls_TCustomImage_OnMouseMove(self.pointer,self.PasOnMouseMove,oldobj,FreeOldEvent)
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
        self.OnMouseUpPasObject=LCLBinding.set_ExtCtrls_TCustomImage_OnMouseUp(self.pointer,self.PasOnMouseUp,oldobj,FreeOldEvent)
    def getOnMouseUp(self):
        return OnMouseUpcall
    OnMouseUp=property(getOnMouseUp,setOnMouseUp)
    def getStretch(self):
        r=LCLBinding.get_ExtCtrls_TCustomImage_Stretch(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setStretch(self,v):
        LCLBinding.set_ExtCtrls_TCustomImage_Stretch(self.pointer,v)
    Stretch=property(getStretch,setStretch)
    def getStretchOutEnabled(self):
        r=LCLBinding.get_ExtCtrls_TCustomImage_StretchOutEnabled(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setStretchOutEnabled(self,v):
        LCLBinding.set_ExtCtrls_TCustomImage_StretchOutEnabled(self.pointer,v)
    StretchOutEnabled=property(getStretchOutEnabled,setStretchOutEnabled)
    def getStretchInEnabled(self):
        r=LCLBinding.get_ExtCtrls_TCustomImage_StretchInEnabled(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setStretchInEnabled(self,v):
        LCLBinding.set_ExtCtrls_TCustomImage_StretchInEnabled(self.pointer,v)
    StretchInEnabled=property(getStretchInEnabled,setStretchInEnabled)
    def getTransparent(self):
        r=LCLBinding.get_ExtCtrls_TCustomImage_Transparent(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setTransparent(self,v):
        LCLBinding.set_ExtCtrls_TCustomImage_Transparent(self.pointer,v)
    Transparent=property(getTransparent,setTransparent)
    def getProportional(self):
        r=LCLBinding.get_ExtCtrls_TCustomImage_Proportional(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setProportional(self,v):
        LCLBinding.set_ExtCtrls_TCustomImage_Proportional(self.pointer,v)
    Proportional=property(getProportional,setProportional)
    def _Warper_OnPictureChanged(self,Sender):
        self.OnPictureChangedcall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnPictureChanged(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnPictureChangedcall'):
            FreeOldEvent=1
            oldobj=self.OnPictureChangedPasObject
        self.OnPictureChangedcall=v 
        self.PasOnPictureChanged=FunctionForm(self._Warper_OnPictureChanged)
        self.OnPictureChangedPasObject=LCLBinding.set_ExtCtrls_TCustomImage_OnPictureChanged(self.pointer,self.PasOnPictureChanged,oldobj,FreeOldEvent)
    def getOnPictureChanged(self):
        return OnPictureChangedcall
    OnPictureChanged=property(getOnPictureChanged,setOnPictureChanged)
#class TCustomImage end
#class TImage start
class TImage(TCustomImage):
#    pointer=c_void_p()
    def __init__(self):#TImage
        TCustomImage.__init__(self)
    def getDragMode(self):
        r=LCLBinding.get_ExtCtrls_TImage_DragMode(self.pointer)
        return r
    def setDragMode(self,v):
        LCLBinding.set_ExtCtrls_TImage_DragMode(self.pointer,v.pointer)
    DragMode=property(getDragMode,setDragMode)
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
        self.OnDblClickPasObject=LCLBinding.set_ExtCtrls_TImage_OnDblClick(self.pointer,self.PasOnDblClick,oldobj,FreeOldEvent)
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
        self.OnDragDropPasObject=LCLBinding.set_ExtCtrls_TImage_OnDragDrop(self.pointer,self.PasOnDragDrop,oldobj,FreeOldEvent)
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
        self.OnDragOverPasObject=LCLBinding.set_ExtCtrls_TImage_OnDragOver(self.pointer,self.PasOnDragOver,oldobj,FreeOldEvent)
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
        self.OnEndDragPasObject=LCLBinding.set_ExtCtrls_TImage_OnEndDrag(self.pointer,self.PasOnEndDrag,oldobj,FreeOldEvent)
    def getOnEndDrag(self):
        return OnEndDragcall
    OnEndDrag=property(getOnEndDrag,setOnEndDrag)
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
        self.OnPaintPasObject=LCLBinding.set_ExtCtrls_TImage_OnPaint(self.pointer,self.PasOnPaint,oldobj,FreeOldEvent)
    def getOnPaint(self):
        return OnPaintcall
    OnPaint=property(getOnPaint,setOnPaint)
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
        self.OnStartDragPasObject=LCLBinding.set_ExtCtrls_TImage_OnStartDrag(self.pointer,self.PasOnStartDrag,oldobj,FreeOldEvent)
    def getOnStartDrag(self):
        return OnStartDragcall
    OnStartDrag=property(getOnStartDrag,setOnStartDrag)
    def getParentShowHint(self):
        r=LCLBinding.get_ExtCtrls_TImage_ParentShowHint(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentShowHint(self,v):
        LCLBinding.set_ExtCtrls_TImage_ParentShowHint(self.pointer,v)
    ParentShowHint=property(getParentShowHint,setParentShowHint)
#constructorExtCtrls_TImage_Create
    @staticmethod
    def Create(AOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.ExtCtrls_TImage_Create((AOwner.pointer)),TImage)
#class TImage end
#class TFlowPanelControl start
class TFlowPanelControl(TCollectionItem):
#    pointer=c_void_p()
    def __init__(self):#TFlowPanelControl
        TCollectionItem.__init__(self)
    def getControl(self):
        r=LCLBinding.get_ExtCtrls_TFlowPanelControl_Control(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TControl)
    def setControl(self,v):
        LCLBinding.set_ExtCtrls_TFlowPanelControl_Control(self.pointer,v.pointer)
    Control=property(getControl,setControl)
    def getWrapAfter(self):
        r=LCLBinding.get_ExtCtrls_TFlowPanelControl_WrapAfter(self.pointer)
        return r
    def setWrapAfter(self,v):
        LCLBinding.set_ExtCtrls_TFlowPanelControl_WrapAfter(self.pointer,v.pointer)
    WrapAfter=property(getWrapAfter,setWrapAfter)
#constructorExtCtrls_TFlowPanelControl_Create
    @staticmethod
    def Create(ACollection):
        return LCLBindingUtil.GetPytonObject(LCLBinding.ExtCtrls_TFlowPanelControl_Create((ACollection.pointer)),TFlowPanelControl)
#class TFlowPanelControl end
#class TFlowPanelControlList start
class TFlowPanelControlList(TOwnedCollection):
#    pointer=c_void_p()
    def __init__(self):#TFlowPanelControlList
        TOwnedCollection.__init__(self)
#constructorExtCtrls_TFlowPanelControlList_Create
    @staticmethod
    def Create(AOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.ExtCtrls_TFlowPanelControlList_Create((AOwner.pointer)),TFlowPanelControlList)
    def getItems(self,Index):
        r=LCLBinding.get_ExtCtrls_TFlowPanelControlList_Items(self.pointer,Index)
        return LCLBindingUtil.GetPytonObject(r,TFlowPanelControl)
    def setItems(self,Index,v):
        LCLBinding.set_ExtCtrls_TFlowPanelControlList_Items(self.pointer,Index,v.pointer)
#class TFlowPanelControlList end
#class TCustomPanel start
class TCustomPanel(TCustomControl):
#    pointer=c_void_p()
    def __init__(self):#TCustomPanel
        TCustomControl.__init__(self)
#constructorExtCtrls_TCustomPanel_Create
    @staticmethod
    def Create(TheOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.ExtCtrls_TCustomPanel_Create((TheOwner.pointer)),TCustomPanel)
    def getAlignment(self):
        r=LCLBinding.get_ExtCtrls_TCustomPanel_Alignment(self.pointer)
        return r
    def setAlignment(self,v):
        LCLBinding.set_ExtCtrls_TCustomPanel_Alignment(self.pointer,v.pointer)
    Alignment=property(getAlignment,setAlignment)
    def getFullRepaint(self):
        r=LCLBinding.get_ExtCtrls_TCustomPanel_FullRepaint(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setFullRepaint(self,v):
        LCLBinding.set_ExtCtrls_TCustomPanel_FullRepaint(self.pointer,v)
    FullRepaint=property(getFullRepaint,setFullRepaint)
    def getParentColor(self):
        r=LCLBinding.get_ExtCtrls_TCustomPanel_ParentColor(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentColor(self,v):
        LCLBinding.set_ExtCtrls_TCustomPanel_ParentColor(self.pointer,v)
    ParentColor=property(getParentColor,setParentColor)
#class TCustomPanel end
#class TCustomFlowPanel start
class TCustomFlowPanel(TCustomPanel):
#    pointer=c_void_p()
    def __init__(self):#TCustomFlowPanel
        TCustomPanel.__init__(self)
#constructorExtCtrls_TCustomFlowPanel_Create
    @staticmethod
    def Create(AOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.ExtCtrls_TCustomFlowPanel_Create((AOwner.pointer)),TCustomFlowPanel)
#Procedure ExtCtrls_TCustomFlowPanel_SetControlIndex
    @staticmethod
    def SetControlIndex(self,AControl,Index):
        LCLBinding.ExtCtrls_TCustomFlowPanel_SetControlIndex((AControl.pointer),(Index))
    def getAutoWrap(self):
        r=LCLBinding.get_ExtCtrls_TCustomFlowPanel_AutoWrap(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setAutoWrap(self,v):
        LCLBinding.set_ExtCtrls_TCustomFlowPanel_AutoWrap(self.pointer,v)
    AutoWrap=property(getAutoWrap,setAutoWrap)
    def getControlList(self):
        r=LCLBinding.get_ExtCtrls_TCustomFlowPanel_ControlList(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TFlowPanelControlList)
    def setControlList(self,v):
        LCLBinding.set_ExtCtrls_TCustomFlowPanel_ControlList(self.pointer,v.pointer)
    ControlList=property(getControlList,setControlList)
    def getFlowStyle(self):
        r=LCLBinding.get_ExtCtrls_TCustomFlowPanel_FlowStyle(self.pointer)
        return r
    def setFlowStyle(self,v):
        LCLBinding.set_ExtCtrls_TCustomFlowPanel_FlowStyle(self.pointer,v.pointer)
    FlowStyle=property(getFlowStyle,setFlowStyle)
    def getFlowLayout(self):
        r=LCLBinding.get_ExtCtrls_TCustomFlowPanel_FlowLayout(self.pointer)
        return r
    def setFlowLayout(self,v):
        LCLBinding.set_ExtCtrls_TCustomFlowPanel_FlowLayout(self.pointer,v.pointer)
    FlowLayout=property(getFlowLayout,setFlowLayout)
#class TCustomFlowPanel end
#class TCustomControlBar start
class TCustomControlBar(TCustomPanel):
#    pointer=c_void_p()
    def __init__(self):#TCustomControlBar
        TCustomPanel.__init__(self)
#constructorExtCtrls_TCustomControlBar_Create
    @staticmethod
    def Create(AOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.ExtCtrls_TCustomControlBar_Create((AOwner.pointer)),TCustomControlBar)
#Procedure ExtCtrls_TCustomControlBar_BeginUpdate
    @staticmethod
    def BeginUpdate(self,):
        LCLBinding.ExtCtrls_TCustomControlBar_BeginUpdate()
#Procedure ExtCtrls_TCustomControlBar_EndUpdate
    @staticmethod
    def EndUpdate(self,):
        LCLBinding.ExtCtrls_TCustomControlBar_EndUpdate()
#Procedure ExtCtrls_TCustomControlBar_FlipChildren
    @staticmethod
    def FlipChildren(self,AllLevels):
        LCLBinding.ExtCtrls_TCustomControlBar_FlipChildren((booleantoint(AllLevels)))
#Procedure ExtCtrls_TCustomControlBar_InsertControl
    @staticmethod
    def InsertControl(self,AControl,Index):
        LCLBinding.ExtCtrls_TCustomControlBar_InsertControl((AControl.pointer),(Index))
#Procedure ExtCtrls_TCustomControlBar_RemoveControl
    @staticmethod
    def RemoveControl(self,AControl):
        LCLBinding.ExtCtrls_TCustomControlBar_RemoveControl((AControl.pointer))
#Procedure ExtCtrls_TCustomControlBar_StickControls
    @staticmethod
    def StickControls(self,):
        LCLBinding.ExtCtrls_TCustomControlBar_StickControls()
    def getAutoDock(self):
        r=LCLBinding.get_ExtCtrls_TCustomControlBar_AutoDock(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setAutoDock(self,v):
        LCLBinding.set_ExtCtrls_TCustomControlBar_AutoDock(self.pointer,v)
    AutoDock=property(getAutoDock,setAutoDock)
    def getAutoDrag(self):
        r=LCLBinding.get_ExtCtrls_TCustomControlBar_AutoDrag(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setAutoDrag(self,v):
        LCLBinding.set_ExtCtrls_TCustomControlBar_AutoDrag(self.pointer,v)
    AutoDrag=property(getAutoDrag,setAutoDrag)
    def getDrawingStyle(self):
        r=LCLBinding.get_ExtCtrls_TCustomControlBar_DrawingStyle(self.pointer)
        return r
    def setDrawingStyle(self,v):
        LCLBinding.set_ExtCtrls_TCustomControlBar_DrawingStyle(self.pointer,v.pointer)
    DrawingStyle=property(getDrawingStyle,setDrawingStyle)
    def getGradientDirection(self):
        r=LCLBinding.get_ExtCtrls_TCustomControlBar_GradientDirection(self.pointer)
        return r
    def setGradientDirection(self,v):
        LCLBinding.set_ExtCtrls_TCustomControlBar_GradientDirection(self.pointer,v.pointer)
    GradientDirection=property(getGradientDirection,setGradientDirection)
    def getPicture(self):
        r=LCLBinding.get_ExtCtrls_TCustomControlBar_Picture(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TPicture)
    def setPicture(self,v):
        LCLBinding.set_ExtCtrls_TCustomControlBar_Picture(self.pointer,v.pointer)
    Picture=property(getPicture,setPicture)
    def getRowSnap(self):
        r=LCLBinding.get_ExtCtrls_TCustomControlBar_RowSnap(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setRowSnap(self,v):
        LCLBinding.set_ExtCtrls_TCustomControlBar_RowSnap(self.pointer,v)
    RowSnap=property(getRowSnap,setRowSnap)
    def _Warper_OnBandDrag(self,Sender,Control,Drag):
        self.OnBandDragcall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.GetPytonObject(Control,TControl),LCLBindingUtil.IntToBoolean(Drag))
    def setOnBandDrag(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnBandDragcall'):
            FreeOldEvent=1
            oldobj=self.OnBandDragPasObject
        self.OnBandDragcall=v 
        self.PasOnBandDrag=FunctionForm(self._Warper_OnBandDrag)
        self.OnBandDragPasObject=LCLBinding.set_ExtCtrls_TCustomControlBar_OnBandDrag(self.pointer,self.PasOnBandDrag,oldobj,FreeOldEvent)
    def getOnBandDrag(self):
        return OnBandDragcall
    OnBandDrag=property(getOnBandDrag,setOnBandDrag)
    def _Warper_OnCanResize(self,Sender,NewSize,Accept):
        self.OnCanResizecall(LCLBindingUtil.GetPytonObject(Sender,TObject),NewSize,LCLBindingUtil.IntToBoolean(Accept))
    def setOnCanResize(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnCanResizecall'):
            FreeOldEvent=1
            oldobj=self.OnCanResizePasObject
        self.OnCanResizecall=v 
        self.PasOnCanResize=FunctionForm(self._Warper_OnCanResize)
        self.OnCanResizePasObject=LCLBinding.set_ExtCtrls_TCustomControlBar_OnCanResize(self.pointer,self.PasOnCanResize,oldobj,FreeOldEvent)
    def getOnCanResize(self):
        return OnCanResizecall
    OnCanResize=property(getOnCanResize,setOnCanResize)
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
        self.OnPaintPasObject=LCLBinding.set_ExtCtrls_TCustomControlBar_OnPaint(self.pointer,self.PasOnPaint,oldobj,FreeOldEvent)
    def getOnPaint(self):
        return OnPaintcall
    OnPaint=property(getOnPaint,setOnPaint)
#class TCustomControlBar end
#class TControlBar start
class TControlBar(TCustomControlBar):
#    pointer=c_void_p()
    def __init__(self):#TControlBar
        TCustomControlBar.__init__(self)
    def getDragKind(self):
        r=LCLBinding.get_ExtCtrls_TControlBar_DragKind(self.pointer)
        return r
    def setDragKind(self,v):
        LCLBinding.set_ExtCtrls_TControlBar_DragKind(self.pointer,v.pointer)
    DragKind=property(getDragKind,setDragKind)
    def getDragMode(self):
        r=LCLBinding.get_ExtCtrls_TControlBar_DragMode(self.pointer)
        return r
    def setDragMode(self,v):
        LCLBinding.set_ExtCtrls_TControlBar_DragMode(self.pointer,v.pointer)
    DragMode=property(getDragMode,setDragMode)
    def getParentFont(self):
        r=LCLBinding.get_ExtCtrls_TControlBar_ParentFont(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentFont(self,v):
        LCLBinding.set_ExtCtrls_TControlBar_ParentFont(self.pointer,v)
    ParentFont=property(getParentFont,setParentFont)
    def getParentShowHint(self):
        r=LCLBinding.get_ExtCtrls_TControlBar_ParentShowHint(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentShowHint(self,v):
        LCLBinding.set_ExtCtrls_TControlBar_ParentShowHint(self.pointer,v)
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
        self.OnDblClickPasObject=LCLBinding.set_ExtCtrls_TControlBar_OnDblClick(self.pointer,self.PasOnDblClick,oldobj,FreeOldEvent)
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
        self.OnDragDropPasObject=LCLBinding.set_ExtCtrls_TControlBar_OnDragDrop(self.pointer,self.PasOnDragDrop,oldobj,FreeOldEvent)
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
        self.OnDragOverPasObject=LCLBinding.set_ExtCtrls_TControlBar_OnDragOver(self.pointer,self.PasOnDragOver,oldobj,FreeOldEvent)
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
            oldobj=self.OnEndDockPasObject
        self.OnEndDockcall=v 
        self.PasOnEndDock=FunctionForm(self._Warper_OnEndDock)
        self.OnEndDockPasObject=LCLBinding.set_ExtCtrls_TControlBar_OnEndDock(self.pointer,self.PasOnEndDock,oldobj,FreeOldEvent)
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
        self.OnEndDragPasObject=LCLBinding.set_ExtCtrls_TControlBar_OnEndDrag(self.pointer,self.PasOnEndDrag,oldobj,FreeOldEvent)
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
        self.OnMouseDownPasObject=LCLBinding.set_ExtCtrls_TControlBar_OnMouseDown(self.pointer,self.PasOnMouseDown,oldobj,FreeOldEvent)
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
        self.OnMouseEnterPasObject=LCLBinding.set_ExtCtrls_TControlBar_OnMouseEnter(self.pointer,self.PasOnMouseEnter,oldobj,FreeOldEvent)
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
        self.OnMouseLeavePasObject=LCLBinding.set_ExtCtrls_TControlBar_OnMouseLeave(self.pointer,self.PasOnMouseLeave,oldobj,FreeOldEvent)
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
        self.OnMouseMovePasObject=LCLBinding.set_ExtCtrls_TControlBar_OnMouseMove(self.pointer,self.PasOnMouseMove,oldobj,FreeOldEvent)
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
        self.OnMouseUpPasObject=LCLBinding.set_ExtCtrls_TControlBar_OnMouseUp(self.pointer,self.PasOnMouseUp,oldobj,FreeOldEvent)
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
        self.OnStartDockPasObject=LCLBinding.set_ExtCtrls_TControlBar_OnStartDock(self.pointer,self.PasOnStartDock,oldobj,FreeOldEvent)
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
        self.OnStartDragPasObject=LCLBinding.set_ExtCtrls_TControlBar_OnStartDrag(self.pointer,self.PasOnStartDrag,oldobj,FreeOldEvent)
    def getOnStartDrag(self):
        return OnStartDragcall
    OnStartDrag=property(getOnStartDrag,setOnStartDrag)
#constructorExtCtrls_TControlBar_Create
    @staticmethod
    def Create(AOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.ExtCtrls_TControlBar_Create((AOwner.pointer)),TControlBar)
#class TControlBar end
#class TBevel start
class TBevel(TGraphicControl):
#    pointer=c_void_p()
    def __init__(self):#TBevel
        TGraphicControl.__init__(self)
#constructorExtCtrls_TBevel_Create
    @staticmethod
    def Create(AOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.ExtCtrls_TBevel_Create((AOwner.pointer)),TBevel)
#Procedure ExtCtrls_TBevel_Assign
    @staticmethod
    def Assign(self,Source):
        LCLBinding.ExtCtrls_TBevel_Assign((Source.pointer))
    def getParentShowHint(self):
        r=LCLBinding.get_ExtCtrls_TBevel_ParentShowHint(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentShowHint(self,v):
        LCLBinding.set_ExtCtrls_TBevel_ParentShowHint(self.pointer,v)
    ParentShowHint=property(getParentShowHint,setParentShowHint)
    def getShape(self):
        r=LCLBinding.get_ExtCtrls_TBevel_Shape(self.pointer)
        return r
    def setShape(self,v):
        LCLBinding.set_ExtCtrls_TBevel_Shape(self.pointer,v.pointer)
    Shape=property(getShape,setShape)
    def getStyle(self):
        r=LCLBinding.get_ExtCtrls_TBevel_Style(self.pointer)
        return r
    def setStyle(self,v):
        LCLBinding.set_ExtCtrls_TBevel_Style(self.pointer,v.pointer)
    Style=property(getStyle,setStyle)
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
        self.OnMouseDownPasObject=LCLBinding.set_ExtCtrls_TBevel_OnMouseDown(self.pointer,self.PasOnMouseDown,oldobj,FreeOldEvent)
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
        self.OnMouseEnterPasObject=LCLBinding.set_ExtCtrls_TBevel_OnMouseEnter(self.pointer,self.PasOnMouseEnter,oldobj,FreeOldEvent)
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
        self.OnMouseLeavePasObject=LCLBinding.set_ExtCtrls_TBevel_OnMouseLeave(self.pointer,self.PasOnMouseLeave,oldobj,FreeOldEvent)
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
        self.OnMouseMovePasObject=LCLBinding.set_ExtCtrls_TBevel_OnMouseMove(self.pointer,self.PasOnMouseMove,oldobj,FreeOldEvent)
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
        self.OnMouseUpPasObject=LCLBinding.set_ExtCtrls_TBevel_OnMouseUp(self.pointer,self.PasOnMouseUp,oldobj,FreeOldEvent)
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
        self.OnPaintPasObject=LCLBinding.set_ExtCtrls_TBevel_OnPaint(self.pointer,self.PasOnPaint,oldobj,FreeOldEvent)
    def getOnPaint(self):
        return OnPaintcall
    OnPaint=property(getOnPaint,setOnPaint)
#class TBevel end
#class TFlowPanel start
class TFlowPanel(TCustomFlowPanel):
#    pointer=c_void_p()
    def __init__(self):#TFlowPanel
        TCustomFlowPanel.__init__(self)
    def getDragKind(self):
        r=LCLBinding.get_ExtCtrls_TFlowPanel_DragKind(self.pointer)
        return r
    def setDragKind(self,v):
        LCLBinding.set_ExtCtrls_TFlowPanel_DragKind(self.pointer,v.pointer)
    DragKind=property(getDragKind,setDragKind)
    def getDragMode(self):
        r=LCLBinding.get_ExtCtrls_TFlowPanel_DragMode(self.pointer)
        return r
    def setDragMode(self,v):
        LCLBinding.set_ExtCtrls_TFlowPanel_DragMode(self.pointer,v.pointer)
    DragMode=property(getDragMode,setDragMode)
    def getParentFont(self):
        r=LCLBinding.get_ExtCtrls_TFlowPanel_ParentFont(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentFont(self,v):
        LCLBinding.set_ExtCtrls_TFlowPanel_ParentFont(self.pointer,v)
    ParentFont=property(getParentFont,setParentFont)
    def getParentShowHint(self):
        r=LCLBinding.get_ExtCtrls_TFlowPanel_ParentShowHint(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentShowHint(self,v):
        LCLBinding.set_ExtCtrls_TFlowPanel_ParentShowHint(self.pointer,v)
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
        self.OnDblClickPasObject=LCLBinding.set_ExtCtrls_TFlowPanel_OnDblClick(self.pointer,self.PasOnDblClick,oldobj,FreeOldEvent)
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
        self.OnDragDropPasObject=LCLBinding.set_ExtCtrls_TFlowPanel_OnDragDrop(self.pointer,self.PasOnDragDrop,oldobj,FreeOldEvent)
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
        self.OnDragOverPasObject=LCLBinding.set_ExtCtrls_TFlowPanel_OnDragOver(self.pointer,self.PasOnDragOver,oldobj,FreeOldEvent)
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
            oldobj=self.OnEndDockPasObject
        self.OnEndDockcall=v 
        self.PasOnEndDock=FunctionForm(self._Warper_OnEndDock)
        self.OnEndDockPasObject=LCLBinding.set_ExtCtrls_TFlowPanel_OnEndDock(self.pointer,self.PasOnEndDock,oldobj,FreeOldEvent)
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
        self.OnEndDragPasObject=LCLBinding.set_ExtCtrls_TFlowPanel_OnEndDrag(self.pointer,self.PasOnEndDrag,oldobj,FreeOldEvent)
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
        self.OnMouseDownPasObject=LCLBinding.set_ExtCtrls_TFlowPanel_OnMouseDown(self.pointer,self.PasOnMouseDown,oldobj,FreeOldEvent)
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
        self.OnMouseEnterPasObject=LCLBinding.set_ExtCtrls_TFlowPanel_OnMouseEnter(self.pointer,self.PasOnMouseEnter,oldobj,FreeOldEvent)
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
        self.OnMouseLeavePasObject=LCLBinding.set_ExtCtrls_TFlowPanel_OnMouseLeave(self.pointer,self.PasOnMouseLeave,oldobj,FreeOldEvent)
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
        self.OnMouseMovePasObject=LCLBinding.set_ExtCtrls_TFlowPanel_OnMouseMove(self.pointer,self.PasOnMouseMove,oldobj,FreeOldEvent)
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
        self.OnMouseUpPasObject=LCLBinding.set_ExtCtrls_TFlowPanel_OnMouseUp(self.pointer,self.PasOnMouseUp,oldobj,FreeOldEvent)
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
        self.OnStartDockPasObject=LCLBinding.set_ExtCtrls_TFlowPanel_OnStartDock(self.pointer,self.PasOnStartDock,oldobj,FreeOldEvent)
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
        self.OnStartDragPasObject=LCLBinding.set_ExtCtrls_TFlowPanel_OnStartDrag(self.pointer,self.PasOnStartDrag,oldobj,FreeOldEvent)
    def getOnStartDrag(self):
        return OnStartDragcall
    OnStartDrag=property(getOnStartDrag,setOnStartDrag)
#constructorExtCtrls_TFlowPanel_Create
    @staticmethod
    def Create(AOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.ExtCtrls_TFlowPanel_Create((AOwner.pointer)),TFlowPanel)
#class TFlowPanel end
#class TPanel start
class TPanel(TCustomPanel):
#    pointer=c_void_p()
    def __init__(self):#TPanel
        TCustomPanel.__init__(self)
    def getDragKind(self):
        r=LCLBinding.get_ExtCtrls_TPanel_DragKind(self.pointer)
        return r
    def setDragKind(self,v):
        LCLBinding.set_ExtCtrls_TPanel_DragKind(self.pointer,v.pointer)
    DragKind=property(getDragKind,setDragKind)
    def getDragMode(self):
        r=LCLBinding.get_ExtCtrls_TPanel_DragMode(self.pointer)
        return r
    def setDragMode(self,v):
        LCLBinding.set_ExtCtrls_TPanel_DragMode(self.pointer,v.pointer)
    DragMode=property(getDragMode,setDragMode)
    def getParentFont(self):
        r=LCLBinding.get_ExtCtrls_TPanel_ParentFont(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentFont(self,v):
        LCLBinding.set_ExtCtrls_TPanel_ParentFont(self.pointer,v)
    ParentFont=property(getParentFont,setParentFont)
    def getParentShowHint(self):
        r=LCLBinding.get_ExtCtrls_TPanel_ParentShowHint(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentShowHint(self,v):
        LCLBinding.set_ExtCtrls_TPanel_ParentShowHint(self.pointer,v)
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
        self.OnDblClickPasObject=LCLBinding.set_ExtCtrls_TPanel_OnDblClick(self.pointer,self.PasOnDblClick,oldobj,FreeOldEvent)
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
        self.OnDragDropPasObject=LCLBinding.set_ExtCtrls_TPanel_OnDragDrop(self.pointer,self.PasOnDragDrop,oldobj,FreeOldEvent)
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
        self.OnDragOverPasObject=LCLBinding.set_ExtCtrls_TPanel_OnDragOver(self.pointer,self.PasOnDragOver,oldobj,FreeOldEvent)
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
            oldobj=self.OnEndDockPasObject
        self.OnEndDockcall=v 
        self.PasOnEndDock=FunctionForm(self._Warper_OnEndDock)
        self.OnEndDockPasObject=LCLBinding.set_ExtCtrls_TPanel_OnEndDock(self.pointer,self.PasOnEndDock,oldobj,FreeOldEvent)
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
        self.OnEndDragPasObject=LCLBinding.set_ExtCtrls_TPanel_OnEndDrag(self.pointer,self.PasOnEndDrag,oldobj,FreeOldEvent)
    def getOnEndDrag(self):
        return OnEndDragcall
    OnEndDrag=property(getOnEndDrag,setOnEndDrag)
    def _Warper_OnGetDockCaption(self,Sender,AControl,ACaption):
        self.OnGetDockCaptioncall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.GetPytonObject(AControl,TControl),ACaption)
    def setOnGetDockCaption(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p,c_char_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnGetDockCaptioncall'):
            FreeOldEvent=1
            oldobj=self.OnGetDockCaptionPasObject
        self.OnGetDockCaptioncall=v 
        self.PasOnGetDockCaption=FunctionForm(self._Warper_OnGetDockCaption)
        self.OnGetDockCaptionPasObject=LCLBinding.set_ExtCtrls_TPanel_OnGetDockCaption(self.pointer,self.PasOnGetDockCaption,oldobj,FreeOldEvent)
    def getOnGetDockCaption(self):
        return OnGetDockCaptioncall
    OnGetDockCaption=property(getOnGetDockCaption,setOnGetDockCaption)
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
        self.OnMouseDownPasObject=LCLBinding.set_ExtCtrls_TPanel_OnMouseDown(self.pointer,self.PasOnMouseDown,oldobj,FreeOldEvent)
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
        self.OnMouseEnterPasObject=LCLBinding.set_ExtCtrls_TPanel_OnMouseEnter(self.pointer,self.PasOnMouseEnter,oldobj,FreeOldEvent)
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
        self.OnMouseLeavePasObject=LCLBinding.set_ExtCtrls_TPanel_OnMouseLeave(self.pointer,self.PasOnMouseLeave,oldobj,FreeOldEvent)
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
        self.OnMouseMovePasObject=LCLBinding.set_ExtCtrls_TPanel_OnMouseMove(self.pointer,self.PasOnMouseMove,oldobj,FreeOldEvent)
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
        self.OnMouseUpPasObject=LCLBinding.set_ExtCtrls_TPanel_OnMouseUp(self.pointer,self.PasOnMouseUp,oldobj,FreeOldEvent)
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
        self.OnStartDockPasObject=LCLBinding.set_ExtCtrls_TPanel_OnStartDock(self.pointer,self.PasOnStartDock,oldobj,FreeOldEvent)
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
        self.OnStartDragPasObject=LCLBinding.set_ExtCtrls_TPanel_OnStartDrag(self.pointer,self.PasOnStartDrag,oldobj,FreeOldEvent)
    def getOnStartDrag(self):
        return OnStartDragcall
    OnStartDrag=property(getOnStartDrag,setOnStartDrag)
#constructorExtCtrls_TPanel_Create
    @staticmethod
    def Create(TheOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.ExtCtrls_TPanel_Create((TheOwner.pointer)),TPanel)
#class TPanel end
