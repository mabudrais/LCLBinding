from ImgList import *
from Controls import *
from clipbrd import *
from ActnList import *
from customtimer import *
from Menus import *
from Graphics import *
from GraphType import *
from LCLClasses import *
from Classes import *
from MainPasObject import *
import LCLBindingUtil
#import end
def CreateTFormStateFromInt(i):
    dic={1:"fsCreating",2:"fsVisible",4:"fsShowing",8:"fsModal",16:"fsCreatedMDIChild",32:"fsBorderStyleChanged",64:"fsFormStyleChanged",128:"fsFirstShow",256:"fsDisableAutoSize"}
    return CreateSetFormint(i,dic)
def CreateTBorderIconsFromInt(i):
    dic={1:"biSystemMenu",2:"biMinimize",4:"biMaximize",8:"biHelp"}
    return CreateSetFormint(i,dic)
#class TScrollingWinControl start
class TScrollingWinControl(TCustomControl):
#    pointer=c_void_p()
    def __init__(self):#TScrollingWinControl
        TCustomControl.__init__(self)
#constructorForms_TScrollingWinControl_Create
    @staticmethod
    def Create(TheOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.Forms_TScrollingWinControl_Create((TheOwner.pointer)),TScrollingWinControl)
#Procedure Forms_TScrollingWinControl_UpdateScrollbars
    @staticmethod
    def UpdateScrollbars(self,):
        LCLBinding.Forms_TScrollingWinControl_UpdateScrollbars()
#Procedure Forms_TScrollingWinControl_ScrollBy
    @staticmethod
    def ScrollBy(self,DeltaX,DeltaY):
        LCLBinding.Forms_TScrollingWinControl_ScrollBy((DeltaX),(DeltaY))
#Procedure Forms_TScrollingWinControl_ScrollInView
    @staticmethod
    def ScrollInView(self,AControl):
        LCLBinding.Forms_TScrollingWinControl_ScrollInView((AControl.pointer))
    def getHorzScrollBar(self):
        r=LCLBinding.get_Forms_TScrollingWinControl_HorzScrollBar(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TControlScrollBar)
    def setHorzScrollBar(self,v):
        LCLBinding.set_Forms_TScrollingWinControl_HorzScrollBar(self.pointer,v.pointer)
    HorzScrollBar=property(getHorzScrollBar,setHorzScrollBar)
    def getVertScrollBar(self):
        r=LCLBinding.get_Forms_TScrollingWinControl_VertScrollBar(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TControlScrollBar)
    def setVertScrollBar(self,v):
        LCLBinding.set_Forms_TScrollingWinControl_VertScrollBar(self.pointer,v.pointer)
    VertScrollBar=property(getVertScrollBar,setVertScrollBar)
#class TScrollingWinControl end
#class TApplicationProperties start
class TApplicationProperties(TLCLComponent):
#    pointer=c_void_p()
    def __init__(self):#TApplicationProperties
        TLCLComponent.__init__(self)
#constructorForms_TApplicationProperties_Create
    @staticmethod
    def Create(AOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.Forms_TApplicationProperties_Create((AOwner.pointer)),TApplicationProperties)
    def getCaptureExceptions(self):
        r=LCLBinding.get_Forms_TApplicationProperties_CaptureExceptions(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setCaptureExceptions(self,v):
        LCLBinding.set_Forms_TApplicationProperties_CaptureExceptions(self.pointer,v)
    CaptureExceptions=property(getCaptureExceptions,setCaptureExceptions)
    def getExceptionDialog(self):
        r=LCLBinding.get_Forms_TApplicationProperties_ExceptionDialog(self.pointer)
        return r
    def setExceptionDialog(self,v):
        LCLBinding.set_Forms_TApplicationProperties_ExceptionDialog(self.pointer,v.pointer)
    ExceptionDialog=property(getExceptionDialog,setExceptionDialog)
    def getHelpFile(self):
        r=LCLBinding.get_Forms_TApplicationProperties_HelpFile(self.pointer)
        return LCLBindingUtil.ConvertPascalstring(r)
    def setHelpFile(self,v):
        LCLBinding.set_Forms_TApplicationProperties_HelpFile(self.pointer,v)
    HelpFile=property(getHelpFile,setHelpFile)
    def getHint(self):
        r=LCLBinding.get_Forms_TApplicationProperties_Hint(self.pointer)
        return LCLBindingUtil.ConvertPascalstring(r)
    def setHint(self,v):
        LCLBinding.set_Forms_TApplicationProperties_Hint(self.pointer,v)
    Hint=property(getHint,setHint)
    def getHintHidePause(self):
        r=LCLBinding.get_Forms_TApplicationProperties_HintHidePause(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setHintHidePause(self,v):
        LCLBinding.set_Forms_TApplicationProperties_HintHidePause(self.pointer,v)
    HintHidePause=property(getHintHidePause,setHintHidePause)
    def getHintPause(self):
        r=LCLBinding.get_Forms_TApplicationProperties_HintPause(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setHintPause(self,v):
        LCLBinding.set_Forms_TApplicationProperties_HintPause(self.pointer,v)
    HintPause=property(getHintPause,setHintPause)
    def getHintShortCuts(self):
        r=LCLBinding.get_Forms_TApplicationProperties_HintShortCuts(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setHintShortCuts(self,v):
        LCLBinding.set_Forms_TApplicationProperties_HintShortCuts(self.pointer,v)
    HintShortCuts=property(getHintShortCuts,setHintShortCuts)
    def getHintShortPause(self):
        r=LCLBinding.get_Forms_TApplicationProperties_HintShortPause(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setHintShortPause(self,v):
        LCLBinding.set_Forms_TApplicationProperties_HintShortPause(self.pointer,v)
    HintShortPause=property(getHintShortPause,setHintShortPause)
    def getShowButtonGlyphs(self):
        r=LCLBinding.get_Forms_TApplicationProperties_ShowButtonGlyphs(self.pointer)
        return r
    def setShowButtonGlyphs(self,v):
        LCLBinding.set_Forms_TApplicationProperties_ShowButtonGlyphs(self.pointer,v.pointer)
    ShowButtonGlyphs=property(getShowButtonGlyphs,setShowButtonGlyphs)
    def getShowMenuGlyphs(self):
        r=LCLBinding.get_Forms_TApplicationProperties_ShowMenuGlyphs(self.pointer)
        return r
    def setShowMenuGlyphs(self,v):
        LCLBinding.set_Forms_TApplicationProperties_ShowMenuGlyphs(self.pointer,v.pointer)
    ShowMenuGlyphs=property(getShowMenuGlyphs,setShowMenuGlyphs)
    def getShowHint(self):
        r=LCLBinding.get_Forms_TApplicationProperties_ShowHint(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setShowHint(self,v):
        LCLBinding.set_Forms_TApplicationProperties_ShowHint(self.pointer,v)
    ShowHint=property(getShowHint,setShowHint)
    def getShowMainForm(self):
        r=LCLBinding.get_Forms_TApplicationProperties_ShowMainForm(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setShowMainForm(self,v):
        LCLBinding.set_Forms_TApplicationProperties_ShowMainForm(self.pointer,v)
    ShowMainForm=property(getShowMainForm,setShowMainForm)
    def getTitle(self):
        r=LCLBinding.get_Forms_TApplicationProperties_Title(self.pointer)
        return LCLBindingUtil.ConvertPascalstring(r)
    def setTitle(self,v):
        LCLBinding.set_Forms_TApplicationProperties_Title(self.pointer,v)
    Title=property(getTitle,setTitle)
    def _Warper_OnActivate(self,Sender):
        self.OnActivatecall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnActivate(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnActivatecall'):
            FreeOldEvent=1
            oldobj=OnActivatePasObject
        self.OnActivatecall=v 
        self.PasOnActivate=FunctionForm(self._Warper_OnActivate)
        self.OnActivatePasObject=LCLBinding.set_Forms_TApplicationProperties_OnActivate(self.pointer,self.PasOnActivate,oldobj,FreeOldEvent)
    def getOnActivate(self):
        return OnActivatecall
    OnActivate=property(getOnActivate,setOnActivate)
    def _Warper_OnDeactivate(self,Sender):
        self.OnDeactivatecall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnDeactivate(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnDeactivatecall'):
            FreeOldEvent=1
            oldobj=OnDeactivatePasObject
        self.OnDeactivatecall=v 
        self.PasOnDeactivate=FunctionForm(self._Warper_OnDeactivate)
        self.OnDeactivatePasObject=LCLBinding.set_Forms_TApplicationProperties_OnDeactivate(self.pointer,self.PasOnDeactivate,oldobj,FreeOldEvent)
    def getOnDeactivate(self):
        return OnDeactivatecall
    OnDeactivate=property(getOnDeactivate,setOnDeactivate)
    def _Warper_OnIdle(self,Sender,Done):
        self.OnIdlecall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.IntToBoolean(Done))
    def setOnIdle(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnIdlecall'):
            FreeOldEvent=1
            oldobj=OnIdlePasObject
        self.OnIdlecall=v 
        self.PasOnIdle=FunctionForm(self._Warper_OnIdle)
        self.OnIdlePasObject=LCLBinding.set_Forms_TApplicationProperties_OnIdle(self.pointer,self.PasOnIdle,oldobj,FreeOldEvent)
    def getOnIdle(self):
        return OnIdlecall
    OnIdle=property(getOnIdle,setOnIdle)
    def _Warper_OnIdleEnd(self,Sender):
        self.OnIdleEndcall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnIdleEnd(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnIdleEndcall'):
            FreeOldEvent=1
            oldobj=OnIdleEndPasObject
        self.OnIdleEndcall=v 
        self.PasOnIdleEnd=FunctionForm(self._Warper_OnIdleEnd)
        self.OnIdleEndPasObject=LCLBinding.set_Forms_TApplicationProperties_OnIdleEnd(self.pointer,self.PasOnIdleEnd,oldobj,FreeOldEvent)
    def getOnIdleEnd(self):
        return OnIdleEndcall
    OnIdleEnd=property(getOnIdleEnd,setOnIdleEnd)
    def _Warper_OnEndSession(self,Sender):
        self.OnEndSessioncall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnEndSession(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnEndSessioncall'):
            FreeOldEvent=1
            oldobj=OnEndSessionPasObject
        self.OnEndSessioncall=v 
        self.PasOnEndSession=FunctionForm(self._Warper_OnEndSession)
        self.OnEndSessionPasObject=LCLBinding.set_Forms_TApplicationProperties_OnEndSession(self.pointer,self.PasOnEndSession,oldobj,FreeOldEvent)
    def getOnEndSession(self):
        return OnEndSessioncall
    OnEndSession=property(getOnEndSession,setOnEndSession)
    def _Warper_OnQueryEndSession(self,Cancel):
        self.OnQueryEndSessioncall(LCLBindingUtil.IntToBoolean(Cancel))
    def setOnQueryEndSession(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnQueryEndSessioncall'):
            FreeOldEvent=1
            oldobj=OnQueryEndSessionPasObject
        self.OnQueryEndSessioncall=v 
        self.PasOnQueryEndSession=FunctionForm(self._Warper_OnQueryEndSession)
        self.OnQueryEndSessionPasObject=LCLBinding.set_Forms_TApplicationProperties_OnQueryEndSession(self.pointer,self.PasOnQueryEndSession,oldobj,FreeOldEvent)
    def getOnQueryEndSession(self):
        return OnQueryEndSessioncall
    OnQueryEndSession=property(getOnQueryEndSession,setOnQueryEndSession)
    def _Warper_OnMinimize(self,Sender):
        self.OnMinimizecall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnMinimize(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnMinimizecall'):
            FreeOldEvent=1
            oldobj=OnMinimizePasObject
        self.OnMinimizecall=v 
        self.PasOnMinimize=FunctionForm(self._Warper_OnMinimize)
        self.OnMinimizePasObject=LCLBinding.set_Forms_TApplicationProperties_OnMinimize(self.pointer,self.PasOnMinimize,oldobj,FreeOldEvent)
    def getOnMinimize(self):
        return OnMinimizecall
    OnMinimize=property(getOnMinimize,setOnMinimize)
    def _Warper_OnModalBegin(self,Sender):
        self.OnModalBegincall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnModalBegin(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnModalBegincall'):
            FreeOldEvent=1
            oldobj=OnModalBeginPasObject
        self.OnModalBegincall=v 
        self.PasOnModalBegin=FunctionForm(self._Warper_OnModalBegin)
        self.OnModalBeginPasObject=LCLBinding.set_Forms_TApplicationProperties_OnModalBegin(self.pointer,self.PasOnModalBegin,oldobj,FreeOldEvent)
    def getOnModalBegin(self):
        return OnModalBegincall
    OnModalBegin=property(getOnModalBegin,setOnModalBegin)
    def _Warper_OnModalEnd(self,Sender):
        self.OnModalEndcall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnModalEnd(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnModalEndcall'):
            FreeOldEvent=1
            oldobj=OnModalEndPasObject
        self.OnModalEndcall=v 
        self.PasOnModalEnd=FunctionForm(self._Warper_OnModalEnd)
        self.OnModalEndPasObject=LCLBinding.set_Forms_TApplicationProperties_OnModalEnd(self.pointer,self.PasOnModalEnd,oldobj,FreeOldEvent)
    def getOnModalEnd(self):
        return OnModalEndcall
    OnModalEnd=property(getOnModalEnd,setOnModalEnd)
    def _Warper_OnRestore(self,Sender):
        self.OnRestorecall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnRestore(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnRestorecall'):
            FreeOldEvent=1
            oldobj=OnRestorePasObject
        self.OnRestorecall=v 
        self.PasOnRestore=FunctionForm(self._Warper_OnRestore)
        self.OnRestorePasObject=LCLBinding.set_Forms_TApplicationProperties_OnRestore(self.pointer,self.PasOnRestore,oldobj,FreeOldEvent)
    def getOnRestore(self):
        return OnRestorecall
    OnRestore=property(getOnRestore,setOnRestore)
    def _Warper_OnHint(self,Sender):
        self.OnHintcall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnHint(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnHintcall'):
            FreeOldEvent=1
            oldobj=OnHintPasObject
        self.OnHintcall=v 
        self.PasOnHint=FunctionForm(self._Warper_OnHint)
        self.OnHintPasObject=LCLBinding.set_Forms_TApplicationProperties_OnHint(self.pointer,self.PasOnHint,oldobj,FreeOldEvent)
    def getOnHint(self):
        return OnHintcall
    OnHint=property(getOnHint,setOnHint)
#class TApplicationProperties end
#class TIDesigner start
class TIDesigner(TObject):
#    pointer=c_void_p()
    def __init__(self):#TIDesigner
        TObject.__init__(self)
#Procedure Forms_TIDesigner_Modified
    @staticmethod
    def Modified(self,):
        LCLBinding.Forms_TIDesigner_Modified()
#Procedure Forms_TIDesigner_Notification
    @staticmethod
    def Notification(self,AComponent,Operation):
        LCLBinding.Forms_TIDesigner_Notification((AComponent.pointer),(Operation.pointer))
#Procedure Forms_TIDesigner_PaintGrid
    @staticmethod
    def PaintGrid(self,):
        LCLBinding.Forms_TIDesigner_PaintGrid()
#Procedure Forms_TIDesigner_ValidateRename
    @staticmethod
    def ValidateRename(self,AComponent,CurName,NewName):
        LCLBinding.Forms_TIDesigner_ValidateRename((AComponent.pointer),(CurName),(NewName))
#Procedure Forms_TIDesigner_SelectOnlyThisComponent
    @staticmethod
    def SelectOnlyThisComponent(self,AComponent):
        LCLBinding.Forms_TIDesigner_SelectOnlyThisComponent((AComponent.pointer))
#Procedure Forms_TIDesigner_PrepareFreeDesigner
    @staticmethod
    def PrepareFreeDesigner(self,AFreeComponent):
        LCLBinding.Forms_TIDesigner_PrepareFreeDesigner((booleantoint(AFreeComponent)))
    def getLookupRoot(self):
        r=LCLBinding.get_Forms_TIDesigner_LookupRoot(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TComponent)
    LookupRoot=property(getLookupRoot)
    def getDefaultFormBoundsValid(self):
        r=LCLBinding.get_Forms_TIDesigner_DefaultFormBoundsValid(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setDefaultFormBoundsValid(self,v):
        LCLBinding.set_Forms_TIDesigner_DefaultFormBoundsValid(self.pointer,v)
    DefaultFormBoundsValid=property(getDefaultFormBoundsValid,setDefaultFormBoundsValid)
#class TIDesigner end
#class TMonitor start
class TMonitor(TObject):
#    pointer=c_void_p()
    def __init__(self):#TMonitor
        TObject.__init__(self)
    def getMonitorNum(self):
        r=LCLBinding.get_Forms_TMonitor_MonitorNum(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    MonitorNum=property(getMonitorNum)
    def getLeft(self):
        r=LCLBinding.get_Forms_TMonitor_Left(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    Left=property(getLeft)
    def getHeight(self):
        r=LCLBinding.get_Forms_TMonitor_Height(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    Height=property(getHeight)
    def getTop(self):
        r=LCLBinding.get_Forms_TMonitor_Top(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    Top=property(getTop)
    def getWidth(self):
        r=LCLBinding.get_Forms_TMonitor_Width(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    Width=property(getWidth)
    def getPrimary(self):
        r=LCLBinding.get_Forms_TMonitor_Primary(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    Primary=property(getPrimary)
    def getPixelsPerInch(self):
        r=LCLBinding.get_Forms_TMonitor_PixelsPerInch(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    PixelsPerInch=property(getPixelsPerInch)
#class TMonitor end
#class TControlScrollBar start
class TControlScrollBar(TPersistent):
#    pointer=c_void_p()
    def __init__(self):#TControlScrollBar
        TPersistent.__init__(self)
#constructorForms_TControlScrollBar_Create
    @staticmethod
    def Create(AControl,AKind):
        return LCLBindingUtil.GetPytonObject(LCLBinding.Forms_TControlScrollBar_Create((AControl.pointer),(AKind.pointer)),TControlScrollBar)
#Procedure Forms_TControlScrollBar_Assign
    @staticmethod
    def Assign(self,Source):
        LCLBinding.Forms_TControlScrollBar_Assign((Source.pointer))
    def getKind(self):
        r=LCLBinding.get_Forms_TControlScrollBar_Kind(self.pointer)
        return r
    Kind=property(getKind)
    def getSize(self):
        r=LCLBinding.get_Forms_TControlScrollBar_Size(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    Size=property(getSize)
    def getSmooth(self):
        r=LCLBinding.get_Forms_TControlScrollBar_Smooth(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setSmooth(self,v):
        LCLBinding.set_Forms_TControlScrollBar_Smooth(self.pointer,v)
    Smooth=property(getSmooth,setSmooth)
    def getPosition(self):
        r=LCLBinding.get_Forms_TControlScrollBar_Position(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setPosition(self,v):
        LCLBinding.set_Forms_TControlScrollBar_Position(self.pointer,v)
    Position=property(getPosition,setPosition)
    def getRange(self):
        r=LCLBinding.get_Forms_TControlScrollBar_Range(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setRange(self,v):
        LCLBinding.set_Forms_TControlScrollBar_Range(self.pointer,v)
    Range=property(getRange,setRange)
    def getTracking(self):
        r=LCLBinding.get_Forms_TControlScrollBar_Tracking(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setTracking(self,v):
        LCLBinding.set_Forms_TControlScrollBar_Tracking(self.pointer,v)
    Tracking=property(getTracking,setTracking)
    def getVisible(self):
        r=LCLBinding.get_Forms_TControlScrollBar_Visible(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setVisible(self,v):
        LCLBinding.set_Forms_TControlScrollBar_Visible(self.pointer,v)
    Visible=property(getVisible,setVisible)
#class TControlScrollBar end
#class TScrollBox start
class TScrollBox(TScrollingWinControl):
#    pointer=c_void_p()
    def __init__(self):#TScrollBox
        TScrollingWinControl.__init__(self)
#constructorForms_TScrollBox_Create
    @staticmethod
    def Create(AOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.Forms_TScrollBox_Create((AOwner.pointer)),TScrollBox)
    def getAutoScroll(self):
        r=LCLBinding.get_Forms_TScrollBox_AutoScroll(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setAutoScroll(self,v):
        LCLBinding.set_Forms_TScrollBox_AutoScroll(self.pointer,v)
    AutoScroll=property(getAutoScroll,setAutoScroll)
    def getDragKind(self):
        r=LCLBinding.get_Forms_TScrollBox_DragKind(self.pointer)
        return r
    def setDragKind(self,v):
        LCLBinding.set_Forms_TScrollBox_DragKind(self.pointer,v.pointer)
    DragKind=property(getDragKind,setDragKind)
    def getDragMode(self):
        r=LCLBinding.get_Forms_TScrollBox_DragMode(self.pointer)
        return r
    def setDragMode(self,v):
        LCLBinding.set_Forms_TScrollBox_DragMode(self.pointer,v.pointer)
    DragMode=property(getDragMode,setDragMode)
    def getParentColor(self):
        r=LCLBinding.get_Forms_TScrollBox_ParentColor(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentColor(self,v):
        LCLBinding.set_Forms_TScrollBox_ParentColor(self.pointer,v)
    ParentColor=property(getParentColor,setParentColor)
    def getParentFont(self):
        r=LCLBinding.get_Forms_TScrollBox_ParentFont(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentFont(self,v):
        LCLBinding.set_Forms_TScrollBox_ParentFont(self.pointer,v)
    ParentFont=property(getParentFont,setParentFont)
    def getParentShowHint(self):
        r=LCLBinding.get_Forms_TScrollBox_ParentShowHint(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentShowHint(self,v):
        LCLBinding.set_Forms_TScrollBox_ParentShowHint(self.pointer,v)
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
        self.OnDblClickPasObject=LCLBinding.set_Forms_TScrollBox_OnDblClick(self.pointer,self.PasOnDblClick,oldobj,FreeOldEvent)
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
        self.OnDragDropPasObject=LCLBinding.set_Forms_TScrollBox_OnDragDrop(self.pointer,self.PasOnDragDrop,oldobj,FreeOldEvent)
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
        self.OnDragOverPasObject=LCLBinding.set_Forms_TScrollBox_OnDragOver(self.pointer,self.PasOnDragOver,oldobj,FreeOldEvent)
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
        self.OnEndDockPasObject=LCLBinding.set_Forms_TScrollBox_OnEndDock(self.pointer,self.PasOnEndDock,oldobj,FreeOldEvent)
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
        self.OnEndDragPasObject=LCLBinding.set_Forms_TScrollBox_OnEndDrag(self.pointer,self.PasOnEndDrag,oldobj,FreeOldEvent)
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
        self.OnMouseDownPasObject=LCLBinding.set_Forms_TScrollBox_OnMouseDown(self.pointer,self.PasOnMouseDown,oldobj,FreeOldEvent)
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
        self.OnMouseEnterPasObject=LCLBinding.set_Forms_TScrollBox_OnMouseEnter(self.pointer,self.PasOnMouseEnter,oldobj,FreeOldEvent)
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
        self.OnMouseLeavePasObject=LCLBinding.set_Forms_TScrollBox_OnMouseLeave(self.pointer,self.PasOnMouseLeave,oldobj,FreeOldEvent)
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
        self.OnMouseMovePasObject=LCLBinding.set_Forms_TScrollBox_OnMouseMove(self.pointer,self.PasOnMouseMove,oldobj,FreeOldEvent)
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
        self.OnMouseUpPasObject=LCLBinding.set_Forms_TScrollBox_OnMouseUp(self.pointer,self.PasOnMouseUp,oldobj,FreeOldEvent)
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
        self.OnStartDockPasObject=LCLBinding.set_Forms_TScrollBox_OnStartDock(self.pointer,self.PasOnStartDock,oldobj,FreeOldEvent)
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
        self.OnStartDragPasObject=LCLBinding.set_Forms_TScrollBox_OnStartDrag(self.pointer,self.PasOnStartDrag,oldobj,FreeOldEvent)
    def getOnStartDrag(self):
        return OnStartDragcall
    OnStartDrag=property(getOnStartDrag,setOnStartDrag)
#class TScrollBox end
#class TCustomDesignControl start
class TCustomDesignControl(TScrollingWinControl):
#    pointer=c_void_p()
    def __init__(self):#TCustomDesignControl
        TScrollingWinControl.__init__(self)
#constructorForms_TCustomDesignControl_Create
    @staticmethod
    def Create(TheOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.Forms_TCustomDesignControl_Create((TheOwner.pointer)),TCustomDesignControl)
#Procedure Forms_TCustomDesignControl_AutoAdjustLayout
    @staticmethod
    def AutoAdjustLayout(self,AMode,AFromPPI,AToPPI,AOldFormWidth,ANewFormWidth):
        LCLBinding.Forms_TCustomDesignControl_AutoAdjustLayout((AMode.pointer),(AFromPPI),(AToPPI),(AOldFormWidth),(ANewFormWidth))
    def getDesignTimeDPI(self):
        r=LCLBinding.get_Forms_TCustomDesignControl_DesignTimeDPI(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setDesignTimeDPI(self,v):
        LCLBinding.set_Forms_TCustomDesignControl_DesignTimeDPI(self.pointer,v)
    DesignTimeDPI=property(getDesignTimeDPI,setDesignTimeDPI)
    def getDesignTimePPI(self):
        r=LCLBinding.get_Forms_TCustomDesignControl_DesignTimePPI(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setDesignTimePPI(self,v):
        LCLBinding.set_Forms_TCustomDesignControl_DesignTimePPI(self.pointer,v)
    DesignTimePPI=property(getDesignTimePPI,setDesignTimePPI)
    def getPixelsPerInch(self):
        r=LCLBinding.get_Forms_TCustomDesignControl_PixelsPerInch(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setPixelsPerInch(self,v):
        LCLBinding.set_Forms_TCustomDesignControl_PixelsPerInch(self.pointer,v)
    PixelsPerInch=property(getPixelsPerInch,setPixelsPerInch)
    def getScaled(self):
        r=LCLBinding.get_Forms_TCustomDesignControl_Scaled(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setScaled(self,v):
        LCLBinding.set_Forms_TCustomDesignControl_Scaled(self.pointer,v)
    Scaled=property(getScaled,setScaled)
#class TCustomDesignControl end
#class TCustomForm start
class TCustomForm(TCustomDesignControl):
#    pointer=c_void_p()
    def __init__(self):#TCustomForm
        TCustomDesignControl.__init__(self)
#constructorForms_TCustomForm_Create
    @staticmethod
    def Create(AOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.Forms_TCustomForm_Create((AOwner.pointer)),TCustomForm)
#constructorForms_TCustomForm_CreateNew
    @staticmethod
    def CreateNew(AOwner,Num):
        return LCLBindingUtil.GetPytonObject(LCLBinding.Forms_TCustomForm_CreateNew((AOwner.pointer),(Num)),TCustomForm)
#Procedure Forms_TCustomForm_AfterConstruction
    @staticmethod
    def AfterConstruction(self,):
        LCLBinding.Forms_TCustomForm_AfterConstruction()
#Procedure Forms_TCustomForm_BeforeDestruction
    @staticmethod
    def BeforeDestruction(self,):
        LCLBinding.Forms_TCustomForm_BeforeDestruction()
#Procedure Forms_TCustomForm_Close
    @staticmethod
    def Close(self,):
        LCLBinding.Forms_TCustomForm_Close()
#Procedure Forms_TCustomForm_DefocusControl
    @staticmethod
    def DefocusControl(self,Control,Removing):
        LCLBinding.Forms_TCustomForm_DefocusControl((Control.pointer),(booleantoint(Removing)))
#Procedure Forms_TCustomForm_DestroyWnd
    @staticmethod
    def DestroyWnd(self,):
        LCLBinding.Forms_TCustomForm_DestroyWnd()
#Procedure Forms_TCustomForm_EnsureVisible
    @staticmethod
    def EnsureVisible(self,AMoveToTop):
        LCLBinding.Forms_TCustomForm_EnsureVisible((booleantoint(AMoveToTop)))
#Procedure Forms_TCustomForm_FocusControl
    @staticmethod
    def FocusControl(self,WinControl):
        LCLBinding.Forms_TCustomForm_FocusControl((WinControl.pointer))
#Procedure Forms_TCustomForm_Hide
    @staticmethod
    def Hide(self,):
        LCLBinding.Forms_TCustomForm_Hide()
#Procedure Forms_TCustomForm_IntfHelp
    @staticmethod
    def IntfHelp(self,AComponent):
        LCLBinding.Forms_TCustomForm_IntfHelp((AComponent.pointer))
#Procedure Forms_TCustomForm_MakeFullyVisible
    @staticmethod
    def MakeFullyVisible(self,AMonitor,UseWorkarea):
        LCLBinding.Forms_TCustomForm_MakeFullyVisible((AMonitor.pointer),(booleantoint(UseWorkarea)))
#Procedure Forms_TCustomForm_Release
    @staticmethod
    def Release(self,):
        LCLBinding.Forms_TCustomForm_Release()
#Procedure Forms_TCustomForm_SetFocus
    @staticmethod
    def SetFocus(self,):
        LCLBinding.Forms_TCustomForm_SetFocus()
#Procedure Forms_TCustomForm_SetRestoredBounds
    @staticmethod
    def SetRestoredBounds(self,ALeft,ATop,AWidth,AHeight):
        LCLBinding.Forms_TCustomForm_SetRestoredBounds((ALeft),(ATop),(AWidth),(AHeight))
#Procedure Forms_TCustomForm_Show
    @staticmethod
    def Show(self,):
        LCLBinding.Forms_TCustomForm_Show()
#Procedure Forms_TCustomForm_ShowOnTop
    @staticmethod
    def ShowOnTop(self,):
        LCLBinding.Forms_TCustomForm_ShowOnTop()
#Procedure Forms_TCustomForm_GetChildren
    @staticmethod
    def GetChildren(self,Proc,Root):
        LCLBinding.Forms_TCustomForm_GetChildren((Proc.pointer),(Root.pointer))
#Procedure Forms_TCustomForm_RemoveAllHandlersOfObject
    @staticmethod
    def RemoveAllHandlersOfObject(self,AnObject):
        LCLBinding.Forms_TCustomForm_RemoveAllHandlersOfObject((AnObject.pointer))
#Procedure Forms_TCustomForm_AddHandlerFirstShow
    @staticmethod
    def AddHandlerFirstShow(self,OnFirstShowHandler,AsFirst):
        LCLBinding.Forms_TCustomForm_AddHandlerFirstShow((OnFirstShowHandler.pointer),(booleantoint(AsFirst)))
#Procedure Forms_TCustomForm_RemoveHandlerFirstShow
    @staticmethod
    def RemoveHandlerFirstShow(self,OnFirstShowHandler):
        LCLBinding.Forms_TCustomForm_RemoveHandlerFirstShow((OnFirstShowHandler.pointer))
#Procedure Forms_TCustomForm_AddHandlerClose
    @staticmethod
    def AddHandlerClose(self,OnCloseHandler,AsFirst):
        LCLBinding.Forms_TCustomForm_AddHandlerClose((OnCloseHandler.pointer),(booleantoint(AsFirst)))
#Procedure Forms_TCustomForm_RemoveHandlerClose
    @staticmethod
    def RemoveHandlerClose(self,OnCloseHandler):
        LCLBinding.Forms_TCustomForm_RemoveHandlerClose((OnCloseHandler.pointer))
#Procedure Forms_TCustomForm_AddHandlerCreate
    @staticmethod
    def AddHandlerCreate(self,OnCreateHandler,AsFirst):
        LCLBinding.Forms_TCustomForm_AddHandlerCreate((OnCreateHandler.pointer),(booleantoint(AsFirst)))
#Procedure Forms_TCustomForm_RemoveHandlerCreate
    @staticmethod
    def RemoveHandlerCreate(self,OnCreateHandler):
        LCLBinding.Forms_TCustomForm_RemoveHandlerCreate((OnCreateHandler.pointer))
#Procedure Forms_TCustomForm_AutoScale
    @staticmethod
    def AutoScale(self,):
        LCLBinding.Forms_TCustomForm_AutoScale()
#Procedure Forms_TCustomForm_UpdateDockCaption
    @staticmethod
    def UpdateDockCaption(self,Exclude):
        LCLBinding.Forms_TCustomForm_UpdateDockCaption((Exclude.pointer))
    def getActive(self):
        r=LCLBinding.get_Forms_TCustomForm_Active(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    Active=property(getActive)
    def getActiveControl(self):
        r=LCLBinding.get_Forms_TCustomForm_ActiveControl(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TWinControl)
    def setActiveControl(self,v):
        LCLBinding.set_Forms_TCustomForm_ActiveControl(self.pointer,v.pointer)
    ActiveControl=property(getActiveControl,setActiveControl)
    def getActiveDefaultControl(self):
        r=LCLBinding.get_Forms_TCustomForm_ActiveDefaultControl(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TControl)
    def setActiveDefaultControl(self,v):
        LCLBinding.set_Forms_TCustomForm_ActiveDefaultControl(self.pointer,v.pointer)
    ActiveDefaultControl=property(getActiveDefaultControl,setActiveDefaultControl)
    def getAllowDropFiles(self):
        r=LCLBinding.get_Forms_TCustomForm_AllowDropFiles(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setAllowDropFiles(self,v):
        LCLBinding.set_Forms_TCustomForm_AllowDropFiles(self.pointer,v)
    AllowDropFiles=property(getAllowDropFiles,setAllowDropFiles)
    def getAlphaBlend(self):
        r=LCLBinding.get_Forms_TCustomForm_AlphaBlend(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setAlphaBlend(self,v):
        LCLBinding.set_Forms_TCustomForm_AlphaBlend(self.pointer,v)
    AlphaBlend=property(getAlphaBlend,setAlphaBlend)
    def getAutoScroll(self):
        r=LCLBinding.get_Forms_TCustomForm_AutoScroll(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setAutoScroll(self,v):
        LCLBinding.set_Forms_TCustomForm_AutoScroll(self.pointer,v)
    AutoScroll=property(getAutoScroll,setAutoScroll)
    def getBorderIcons(self):
        r=LCLBinding.get_Forms_TCustomForm_BorderIcons(self.pointer)
        return r
    def setBorderIcons(self,v):
        LCLBinding.set_Forms_TCustomForm_BorderIcons(self.pointer,v.pointer)
    BorderIcons=property(getBorderIcons,setBorderIcons)
    def getBorderStyle(self):
        r=LCLBinding.get_Forms_TCustomForm_BorderStyle(self.pointer)
        return r
    def setBorderStyle(self,v):
        LCLBinding.set_Forms_TCustomForm_BorderStyle(self.pointer,v.pointer)
    BorderStyle=property(getBorderStyle,setBorderStyle)
    def getCancelControl(self):
        r=LCLBinding.get_Forms_TCustomForm_CancelControl(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TControl)
    def setCancelControl(self,v):
        LCLBinding.set_Forms_TCustomForm_CancelControl(self.pointer,v.pointer)
    CancelControl=property(getCancelControl,setCancelControl)
    def getDefaultControl(self):
        r=LCLBinding.get_Forms_TCustomForm_DefaultControl(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TControl)
    def setDefaultControl(self,v):
        LCLBinding.set_Forms_TCustomForm_DefaultControl(self.pointer,v.pointer)
    DefaultControl=property(getDefaultControl,setDefaultControl)
    def getDefaultMonitor(self):
        r=LCLBinding.get_Forms_TCustomForm_DefaultMonitor(self.pointer)
        return r
    def setDefaultMonitor(self,v):
        LCLBinding.set_Forms_TCustomForm_DefaultMonitor(self.pointer,v.pointer)
    DefaultMonitor=property(getDefaultMonitor,setDefaultMonitor)
    def getDesigner(self):
        r=LCLBinding.get_Forms_TCustomForm_Designer(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TIDesigner)
    def setDesigner(self,v):
        LCLBinding.set_Forms_TCustomForm_Designer(self.pointer,v.pointer)
    Designer=property(getDesigner,setDesigner)
    def getEffectiveShowInTaskBar(self):
        r=LCLBinding.get_Forms_TCustomForm_EffectiveShowInTaskBar(self.pointer)
        return r
    EffectiveShowInTaskBar=property(getEffectiveShowInTaskBar)
    def getFormState(self):
        r=LCLBinding.get_Forms_TCustomForm_FormState(self.pointer)
        return r
    FormState=property(getFormState)
    def getFormStyle(self):
        r=LCLBinding.get_Forms_TCustomForm_FormStyle(self.pointer)
        return r
    def setFormStyle(self,v):
        LCLBinding.set_Forms_TCustomForm_FormStyle(self.pointer,v.pointer)
    FormStyle=property(getFormStyle,setFormStyle)
    def getHelpFile(self):
        r=LCLBinding.get_Forms_TCustomForm_HelpFile(self.pointer)
        return LCLBindingUtil.ConvertPascalstring(r)
    def setHelpFile(self,v):
        LCLBinding.set_Forms_TCustomForm_HelpFile(self.pointer,v)
    HelpFile=property(getHelpFile,setHelpFile)
    def getIcon(self):
        r=LCLBinding.get_Forms_TCustomForm_Icon(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TIcon)
    def setIcon(self,v):
        LCLBinding.set_Forms_TCustomForm_Icon(self.pointer,v.pointer)
    Icon=property(getIcon,setIcon)
    def getKeyPreview(self):
        r=LCLBinding.get_Forms_TCustomForm_KeyPreview(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setKeyPreview(self,v):
        LCLBinding.set_Forms_TCustomForm_KeyPreview(self.pointer,v)
    KeyPreview=property(getKeyPreview,setKeyPreview)
    def getMDIChildren(self,I):
        r=LCLBinding.get_Forms_TCustomForm_MDIChildren(self.pointer,I)
        return LCLBindingUtil.GetPytonObject(r,TCustomForm)
    def getMenu(self):
        r=LCLBinding.get_Forms_TCustomForm_Menu(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TMainMenu)
    def setMenu(self,v):
        LCLBinding.set_Forms_TCustomForm_Menu(self.pointer,v.pointer)
    Menu=property(getMenu,setMenu)
    def getMonitor(self):
        r=LCLBinding.get_Forms_TCustomForm_Monitor(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TMonitor)
    Monitor=property(getMonitor)
    def getPopupMode(self):
        r=LCLBinding.get_Forms_TCustomForm_PopupMode(self.pointer)
        return r
    def setPopupMode(self,v):
        LCLBinding.set_Forms_TCustomForm_PopupMode(self.pointer,v.pointer)
    PopupMode=property(getPopupMode,setPopupMode)
    def getPopupParent(self):
        r=LCLBinding.get_Forms_TCustomForm_PopupParent(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TCustomForm)
    def setPopupParent(self,v):
        LCLBinding.set_Forms_TCustomForm_PopupParent(self.pointer,v.pointer)
    PopupParent=property(getPopupParent,setPopupParent)
    def _Warper_OnActivate(self,Sender):
        self.OnActivatecall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnActivate(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnActivatecall'):
            FreeOldEvent=1
            oldobj=OnActivatePasObject
        self.OnActivatecall=v 
        self.PasOnActivate=FunctionForm(self._Warper_OnActivate)
        self.OnActivatePasObject=LCLBinding.set_Forms_TCustomForm_OnActivate(self.pointer,self.PasOnActivate,oldobj,FreeOldEvent)
    def getOnActivate(self):
        return OnActivatecall
    OnActivate=property(getOnActivate,setOnActivate)
    def _Warper_OnClose(self,Sender,CloseAction):
        self.OnClosecall(LCLBindingUtil.GetPytonObject(Sender,TObject),CloseAction)
    def setOnClose(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnClosecall'):
            FreeOldEvent=1
            oldobj=OnClosePasObject
        self.OnClosecall=v 
        self.PasOnClose=FunctionForm(self._Warper_OnClose)
        self.OnClosePasObject=LCLBinding.set_Forms_TCustomForm_OnClose(self.pointer,self.PasOnClose,oldobj,FreeOldEvent)
    def getOnClose(self):
        return OnClosecall
    OnClose=property(getOnClose,setOnClose)
    def _Warper_OnCloseQuery(self,Sender,CanClose):
        self.OnCloseQuerycall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.IntToBoolean(CanClose))
    def setOnCloseQuery(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnCloseQuerycall'):
            FreeOldEvent=1
            oldobj=OnCloseQueryPasObject
        self.OnCloseQuerycall=v 
        self.PasOnCloseQuery=FunctionForm(self._Warper_OnCloseQuery)
        self.OnCloseQueryPasObject=LCLBinding.set_Forms_TCustomForm_OnCloseQuery(self.pointer,self.PasOnCloseQuery,oldobj,FreeOldEvent)
    def getOnCloseQuery(self):
        return OnCloseQuerycall
    OnCloseQuery=property(getOnCloseQuery,setOnCloseQuery)
    def _Warper_OnCreate(self,Sender):
        self.OnCreatecall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnCreate(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnCreatecall'):
            FreeOldEvent=1
            oldobj=OnCreatePasObject
        self.OnCreatecall=v 
        self.PasOnCreate=FunctionForm(self._Warper_OnCreate)
        self.OnCreatePasObject=LCLBinding.set_Forms_TCustomForm_OnCreate(self.pointer,self.PasOnCreate,oldobj,FreeOldEvent)
    def getOnCreate(self):
        return OnCreatecall
    OnCreate=property(getOnCreate,setOnCreate)
    def _Warper_OnDeactivate(self,Sender):
        self.OnDeactivatecall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnDeactivate(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnDeactivatecall'):
            FreeOldEvent=1
            oldobj=OnDeactivatePasObject
        self.OnDeactivatecall=v 
        self.PasOnDeactivate=FunctionForm(self._Warper_OnDeactivate)
        self.OnDeactivatePasObject=LCLBinding.set_Forms_TCustomForm_OnDeactivate(self.pointer,self.PasOnDeactivate,oldobj,FreeOldEvent)
    def getOnDeactivate(self):
        return OnDeactivatecall
    OnDeactivate=property(getOnDeactivate,setOnDeactivate)
    def _Warper_OnDestroy(self,Sender):
        self.OnDestroycall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnDestroy(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnDestroycall'):
            FreeOldEvent=1
            oldobj=OnDestroyPasObject
        self.OnDestroycall=v 
        self.PasOnDestroy=FunctionForm(self._Warper_OnDestroy)
        self.OnDestroyPasObject=LCLBinding.set_Forms_TCustomForm_OnDestroy(self.pointer,self.PasOnDestroy,oldobj,FreeOldEvent)
    def getOnDestroy(self):
        return OnDestroycall
    OnDestroy=property(getOnDestroy,setOnDestroy)
    def _Warper_OnHide(self,Sender):
        self.OnHidecall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnHide(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnHidecall'):
            FreeOldEvent=1
            oldobj=OnHidePasObject
        self.OnHidecall=v 
        self.PasOnHide=FunctionForm(self._Warper_OnHide)
        self.OnHidePasObject=LCLBinding.set_Forms_TCustomForm_OnHide(self.pointer,self.PasOnHide,oldobj,FreeOldEvent)
    def getOnHide(self):
        return OnHidecall
    OnHide=property(getOnHide,setOnHide)
    def _Warper_OnShow(self,Sender):
        self.OnShowcall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnShow(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnShowcall'):
            FreeOldEvent=1
            oldobj=OnShowPasObject
        self.OnShowcall=v 
        self.PasOnShow=FunctionForm(self._Warper_OnShow)
        self.OnShowPasObject=LCLBinding.set_Forms_TCustomForm_OnShow(self.pointer,self.PasOnShow,oldobj,FreeOldEvent)
    def getOnShow(self):
        return OnShowcall
    OnShow=property(getOnShow,setOnShow)
    def _Warper_OnShowModalFinished(self,Sender,AResult):
        self.OnShowModalFinishedcall(LCLBindingUtil.GetPytonObject(Sender,TObject),AResult)
    def setOnShowModalFinished(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnShowModalFinishedcall'):
            FreeOldEvent=1
            oldobj=OnShowModalFinishedPasObject
        self.OnShowModalFinishedcall=v 
        self.PasOnShowModalFinished=FunctionForm(self._Warper_OnShowModalFinished)
        self.OnShowModalFinishedPasObject=LCLBinding.set_Forms_TCustomForm_OnShowModalFinished(self.pointer,self.PasOnShowModalFinished,oldobj,FreeOldEvent)
    def getOnShowModalFinished(self):
        return OnShowModalFinishedcall
    OnShowModalFinished=property(getOnShowModalFinished,setOnShowModalFinished)
    def _Warper_OnWindowStateChange(self,Sender):
        self.OnWindowStateChangecall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnWindowStateChange(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnWindowStateChangecall'):
            FreeOldEvent=1
            oldobj=OnWindowStateChangePasObject
        self.OnWindowStateChangecall=v 
        self.PasOnWindowStateChange=FunctionForm(self._Warper_OnWindowStateChange)
        self.OnWindowStateChangePasObject=LCLBinding.set_Forms_TCustomForm_OnWindowStateChange(self.pointer,self.PasOnWindowStateChange,oldobj,FreeOldEvent)
    def getOnWindowStateChange(self):
        return OnWindowStateChangecall
    OnWindowStateChange=property(getOnWindowStateChange,setOnWindowStateChange)
    def getParentFont(self):
        r=LCLBinding.get_Forms_TCustomForm_ParentFont(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentFont(self,v):
        LCLBinding.set_Forms_TCustomForm_ParentFont(self.pointer,v)
    ParentFont=property(getParentFont,setParentFont)
    def getPosition(self):
        r=LCLBinding.get_Forms_TCustomForm_Position(self.pointer)
        return r
    def setPosition(self,v):
        LCLBinding.set_Forms_TCustomForm_Position(self.pointer,v.pointer)
    Position=property(getPosition,setPosition)
    def getRestoredLeft(self):
        r=LCLBinding.get_Forms_TCustomForm_RestoredLeft(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    RestoredLeft=property(getRestoredLeft)
    def getRestoredTop(self):
        r=LCLBinding.get_Forms_TCustomForm_RestoredTop(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    RestoredTop=property(getRestoredTop)
    def getRestoredWidth(self):
        r=LCLBinding.get_Forms_TCustomForm_RestoredWidth(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    RestoredWidth=property(getRestoredWidth)
    def getRestoredHeight(self):
        r=LCLBinding.get_Forms_TCustomForm_RestoredHeight(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    RestoredHeight=property(getRestoredHeight)
    def getShowInTaskBar(self):
        r=LCLBinding.get_Forms_TCustomForm_ShowInTaskBar(self.pointer)
        return r
    def setShowInTaskBar(self,v):
        LCLBinding.set_Forms_TCustomForm_ShowInTaskBar(self.pointer,v.pointer)
    ShowInTaskBar=property(getShowInTaskBar,setShowInTaskBar)
    def getWindowState(self):
        r=LCLBinding.get_Forms_TCustomForm_WindowState(self.pointer)
        return r
    def setWindowState(self,v):
        LCLBinding.set_Forms_TCustomForm_WindowState(self.pointer,v.pointer)
    WindowState=property(getWindowState,setWindowState)
#class TCustomForm end
#class TForm start
class TForm(TCustomForm):
#    pointer=c_void_p()
    def __init__(self):#TForm
        TCustomForm.__init__(self)
#constructorForms_TForm_Create
    @staticmethod
    def Create(TheOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.Forms_TForm_Create((TheOwner.pointer)),TForm)
#Procedure Forms_TForm_Cascade
    @staticmethod
    def Cascade(self,):
        LCLBinding.Forms_TForm_Cascade()
#Procedure Forms_TForm_Next
    @staticmethod
    def Next(self,):
        LCLBinding.Forms_TForm_Next()
#Procedure Forms_TForm_Previous
    @staticmethod
    def Previous(self,):
        LCLBinding.Forms_TForm_Previous()
#Procedure Forms_TForm_Tile
    @staticmethod
    def Tile(self,):
        LCLBinding.Forms_TForm_Tile()
    def getDragKind(self):
        r=LCLBinding.get_Forms_TForm_DragKind(self.pointer)
        return r
    def setDragKind(self,v):
        LCLBinding.set_Forms_TForm_DragKind(self.pointer,v.pointer)
    DragKind=property(getDragKind,setDragKind)
    def getDragMode(self):
        r=LCLBinding.get_Forms_TForm_DragMode(self.pointer)
        return r
    def setDragMode(self,v):
        LCLBinding.set_Forms_TForm_DragMode(self.pointer,v.pointer)
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
        self.OnDblClickPasObject=LCLBinding.set_Forms_TForm_OnDblClick(self.pointer,self.PasOnDblClick,oldobj,FreeOldEvent)
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
        self.OnDragDropPasObject=LCLBinding.set_Forms_TForm_OnDragDrop(self.pointer,self.PasOnDragDrop,oldobj,FreeOldEvent)
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
        self.OnDragOverPasObject=LCLBinding.set_Forms_TForm_OnDragOver(self.pointer,self.PasOnDragOver,oldobj,FreeOldEvent)
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
        self.OnEndDockPasObject=LCLBinding.set_Forms_TForm_OnEndDock(self.pointer,self.PasOnEndDock,oldobj,FreeOldEvent)
    def getOnEndDock(self):
        return OnEndDockcall
    OnEndDock=property(getOnEndDock,setOnEndDock)
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
        self.OnMouseDownPasObject=LCLBinding.set_Forms_TForm_OnMouseDown(self.pointer,self.PasOnMouseDown,oldobj,FreeOldEvent)
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
        self.OnMouseEnterPasObject=LCLBinding.set_Forms_TForm_OnMouseEnter(self.pointer,self.PasOnMouseEnter,oldobj,FreeOldEvent)
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
        self.OnMouseLeavePasObject=LCLBinding.set_Forms_TForm_OnMouseLeave(self.pointer,self.PasOnMouseLeave,oldobj,FreeOldEvent)
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
        self.OnMouseMovePasObject=LCLBinding.set_Forms_TForm_OnMouseMove(self.pointer,self.PasOnMouseMove,oldobj,FreeOldEvent)
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
        self.OnMouseUpPasObject=LCLBinding.set_Forms_TForm_OnMouseUp(self.pointer,self.PasOnMouseUp,oldobj,FreeOldEvent)
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
        self.OnStartDockPasObject=LCLBinding.set_Forms_TForm_OnStartDock(self.pointer,self.PasOnStartDock,oldobj,FreeOldEvent)
    def getOnStartDock(self):
        return OnStartDockcall
    OnStartDock=property(getOnStartDock,setOnStartDock)
    def getSessionProperties(self):
        r=LCLBinding.get_Forms_TForm_SessionProperties(self.pointer)
        return LCLBindingUtil.ConvertPascalstring(r)
    def setSessionProperties(self,v):
        LCLBinding.set_Forms_TForm_SessionProperties(self.pointer,v)
    SessionProperties=property(getSessionProperties,setSessionProperties)
    def getLCLVersion(self):
        r=LCLBinding.get_Forms_TForm_LCLVersion(self.pointer)
        return LCLBindingUtil.ConvertPascalstring(r)
    def setLCLVersion(self,v):
        LCLBinding.set_Forms_TForm_LCLVersion(self.pointer,v)
    LCLVersion=property(getLCLVersion,setLCLVersion)
#class TForm end
