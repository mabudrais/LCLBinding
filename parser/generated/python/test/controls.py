from LCLClasses import *
from ActnList import *
from Menus import *
from ImgList import *
from Graphics import *
from GraphType import *
from Classes import *
from MainPasObject import *
import LCLBindingUtil
#import end
def CreateTControlStyleFromInt(i):
    dic={1:"csAcceptsControls",2:"csCaptureMouse",4:"csDesignInteractive",8:"csClickEvents",16:"csFramed",32:"csSetCaption",64:"csOpaque",128:"csDoubleClicks",256:"csTripleClicks",512:"csQuadClicks",1024:"csFixedWidth",2048:"csFixedHeight",4096:"csNoDesignVisible",8192:"csReplicatable",16384:"csNoStdEvents",32768:"csDisplayDragImage",65536:"csReflector",131072:"csActionClient",262144:"csMenuEvents",524288:"csNoFocus",1048576:"csNeedsBorderPaint",2097152:"csParentBackground",4194304:"csDesignNoSmoothResize",8388608:"csDesignFixedBounds",16777216:"csHasDefaultAction",33554432:"csHasCancelAction",67108864:"csNoDesignSelectable",134217728:"csOwnedChildrenNotSelectable",268435456:"csAutoSize0x0",536870912:"csAutoSizeKeepChildLeft",1073741824:"csAutoSizeKeepChildTop",2147483648:"csRequiresKeyboardInput"}
    return CreateSetFormint(i,dic)
def CreateTControlStateFromInt(i):
    dic={1:"csLButtonDown",2:"csClicked",4:"csPalette",8:"csReadingState",16:"csFocusing",32:"csCreating",64:"csPaintCopy",128:"csCustomPaint",256:"csDestroyingHandle",512:"csDocking",1024:"csVisibleSetInLoading"}
    return CreateSetFormint(i,dic)
def CreateTSizeConstraintsOptionsFromInt(i):
    dic={1:"scoAdviceWidthAsMin",2:"scoAdviceWidthAsMax",4:"scoAdviceHeightAsMin",8:"scoAdviceHeightAsMax"}
    return CreateSetFormint(i,dic)
def CreateTCaptureMouseButtonsFromInt(i):
    dic={1:"mbLeft",2:"mbRight",4:"mbMiddle",8:"mbExtra1",16:"mbExtra2"}
    return CreateSetFormint(i,dic)
def CreateTAnchorsFromInt(i):
    dic={1:"akTop",2:"akLeft",4:"akRight",8:"akBottom"}
    return CreateSetFormint(i,dic)
#class TDragImageList start
class TDragImageList(TCustomImageList):
#    pointer=c_void_p()
    def __init__(self):#TDragImageList
        TCustomImageList.__init__(self)
#Procedure Controls_TDragImageList_DragUnlock
    @staticmethod
    def DragUnlock(self,):
        LCLBinding.Controls_TDragImageList_DragUnlock()
#Procedure Controls_TDragImageList_HideDragImage
    @staticmethod
    def HideDragImage(self,):
        LCLBinding.Controls_TDragImageList_HideDragImage()
#Procedure Controls_TDragImageList_ShowDragImage
    @staticmethod
    def ShowDragImage(self,):
        LCLBinding.Controls_TDragImageList_ShowDragImage()
    def getDragging(self):
        r=LCLBinding.get_Controls_TDragImageList_Dragging(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    Dragging=property(getDragging)
#constructorControls_TDragImageList_Create
    @staticmethod
    def Create(AOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.Controls_TDragImageList_Create((AOwner.pointer)),TDragImageList)
#class TDragImageList end
#class TImageList start
class TImageList(TDragImageList):
#    pointer=c_void_p()
    def __init__(self):#TImageList
        TDragImageList.__init__(self)
#constructorControls_TImageList_Create
    @staticmethod
    def Create(AOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.Controls_TImageList_Create((AOwner.pointer)),TImageList)
#class TImageList end
#class TControl start
class TControl(TLCLComponent):
#    pointer=c_void_p()
    def __init__(self):#TControl
        TLCLComponent.__init__(self)
#Procedure Controls_TControl_DragDrop
    @staticmethod
    def DragDrop(self,Source,X,Y):
        LCLBinding.Controls_TControl_DragDrop((Source.pointer),(X),(Y))
#Procedure Controls_TControl_AdjustSize
    @staticmethod
    def AdjustSize(self,):
        LCLBinding.Controls_TControl_AdjustSize()
#Procedure Controls_TControl_AnchorHorizontalCenterTo
    @staticmethod
    def AnchorHorizontalCenterTo(self,Sibling):
        LCLBinding.Controls_TControl_AnchorHorizontalCenterTo((Sibling.pointer))
#Procedure Controls_TControl_AnchorVerticalCenterTo
    @staticmethod
    def AnchorVerticalCenterTo(self,Sibling):
        LCLBinding.Controls_TControl_AnchorVerticalCenterTo((Sibling.pointer))
#Procedure Controls_TControl_AnchorSame
    @staticmethod
    def AnchorSame(self,Side,Sibling):
        LCLBinding.Controls_TControl_AnchorSame((Side.pointer),(Sibling.pointer))
    def getAnchoredControls(self,Index):
        r=LCLBinding.get_Controls_TControl_AnchoredControls(self.pointer,Index)
        return LCLBindingUtil.GetPytonObject(r,TControl)
#Procedure Controls_TControl_SetBounds
    @staticmethod
    def SetBounds(self,aLeft,aTop,aWidth,aHeight):
        LCLBinding.Controls_TControl_SetBounds((aLeft),(aTop),(aWidth),(aHeight))
#Procedure Controls_TControl_SetInitialBounds
    @staticmethod
    def SetInitialBounds(self,aLeft,aTop,aWidth,aHeight):
        LCLBinding.Controls_TControl_SetInitialBounds((aLeft),(aTop),(aWidth),(aHeight))
#Procedure Controls_TControl_SetBoundsKeepBase
    @staticmethod
    def SetBoundsKeepBase(self,aLeft,aTop,aWidth,aHeight):
        LCLBinding.Controls_TControl_SetBoundsKeepBase((aLeft),(aTop),(aWidth),(aHeight))
#Procedure Controls_TControl_CNPreferredSizeChanged
    @staticmethod
    def CNPreferredSizeChanged(self,):
        LCLBinding.Controls_TControl_CNPreferredSizeChanged()
#Procedure Controls_TControl_InvalidatePreferredSize
    @staticmethod
    def InvalidatePreferredSize(self,):
        LCLBinding.Controls_TControl_InvalidatePreferredSize()
#Procedure Controls_TControl_DisableAutoSizing
    @staticmethod
    def DisableAutoSizing(self,):
        LCLBinding.Controls_TControl_DisableAutoSizing()
#Procedure Controls_TControl_EnableAutoSizing
    @staticmethod
    def EnableAutoSizing(self,):
        LCLBinding.Controls_TControl_EnableAutoSizing()
#Procedure Controls_TControl_UpdateBaseBounds
    @staticmethod
    def UpdateBaseBounds(self,StoreBounds,StoreParentClientSize,UseLoadedValues):
        LCLBinding.Controls_TControl_UpdateBaseBounds((booleantoint(StoreBounds)),(booleantoint(StoreParentClientSize)),(booleantoint(UseLoadedValues)))
#Procedure Controls_TControl_WriteLayoutDebugReport
    @staticmethod
    def WriteLayoutDebugReport(self,Prefix):
        LCLBinding.Controls_TControl_WriteLayoutDebugReport((Prefix))
#Procedure Controls_TControl_AutoAdjustLayout
    @staticmethod
    def AutoAdjustLayout(self,AMode,AFromPPI,AToPPI,AOldFormWidth,ANewFormWidth):
        LCLBinding.Controls_TControl_AutoAdjustLayout((AMode.pointer),(AFromPPI),(AToPPI),(AOldFormWidth),(ANewFormWidth))
#Procedure Controls_TControl_FixDesignFontsPPI
    @staticmethod
    def FixDesignFontsPPI(self,ADesignTimePPI):
        LCLBinding.Controls_TControl_FixDesignFontsPPI((ADesignTimePPI))
#Procedure Controls_TControl_ScaleFontsPPI
    @staticmethod
    def ScaleFontsPPI(self,AToPPI,AProportion):
        LCLBinding.Controls_TControl_ScaleFontsPPI((AToPPI),(AProportion.pointer))
#constructorControls_TControl_Create
    @staticmethod
    def Create(TheOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.Controls_TControl_Create((TheOwner.pointer)),TControl)
#Procedure Controls_TControl_BeforeDestruction
    @staticmethod
    def BeforeDestruction(self,):
        LCLBinding.Controls_TControl_BeforeDestruction()
#Procedure Controls_TControl_EditingDone
    @staticmethod
    def EditingDone(self,):
        LCLBinding.Controls_TControl_EditingDone()
#Procedure Controls_TControl_ExecuteDefaultAction
    @staticmethod
    def ExecuteDefaultAction(self,):
        LCLBinding.Controls_TControl_ExecuteDefaultAction()
#Procedure Controls_TControl_ExecuteCancelAction
    @staticmethod
    def ExecuteCancelAction(self,):
        LCLBinding.Controls_TControl_ExecuteCancelAction()
#Procedure Controls_TControl_BeginDrag
    @staticmethod
    def BeginDrag(self,Immediate,Threshold):
        LCLBinding.Controls_TControl_BeginDrag((booleantoint(Immediate)),(Threshold))
#Procedure Controls_TControl_EndDrag
    @staticmethod
    def EndDrag(self,Drop):
        LCLBinding.Controls_TControl_EndDrag((booleantoint(Drop)))
#Procedure Controls_TControl_BringToFront
    @staticmethod
    def BringToFront(self,):
        LCLBinding.Controls_TControl_BringToFront()
#Procedure Controls_TControl_Hide
    @staticmethod
    def Hide(self,):
        LCLBinding.Controls_TControl_Hide()
#Procedure Controls_TControl_Refresh
    @staticmethod
    def Refresh(self,):
        LCLBinding.Controls_TControl_Refresh()
#Procedure Controls_TControl_Repaint
    @staticmethod
    def Repaint(self,):
        LCLBinding.Controls_TControl_Repaint()
#Procedure Controls_TControl_Invalidate
    @staticmethod
    def Invalidate(self,):
        LCLBinding.Controls_TControl_Invalidate()
#Procedure Controls_TControl_CheckNewParent
    @staticmethod
    def CheckNewParent(self,AParent):
        LCLBinding.Controls_TControl_CheckNewParent((AParent.pointer))
#Procedure Controls_TControl_SendToBack
    @staticmethod
    def SendToBack(self,):
        LCLBinding.Controls_TControl_SendToBack()
#Procedure Controls_TControl_UpdateRolesForForm
    @staticmethod
    def UpdateRolesForForm(self,):
        LCLBinding.Controls_TControl_UpdateRolesForForm()
#Procedure Controls_TControl_ActiveDefaultControlChanged
    @staticmethod
    def ActiveDefaultControlChanged(self,NewControl):
        LCLBinding.Controls_TControl_ActiveDefaultControlChanged((NewControl.pointer))
#Procedure Controls_TControl_Show
    @staticmethod
    def Show(self,):
        LCLBinding.Controls_TControl_Show()
#Procedure Controls_TControl_Update
    @staticmethod
    def Update(self,):
        LCLBinding.Controls_TControl_Update()
#Procedure Controls_TControl_InitiateAction
    @staticmethod
    def InitiateAction(self,):
        LCLBinding.Controls_TControl_InitiateAction()
#Procedure Controls_TControl_ShowHelp
    @staticmethod
    def ShowHelp(self,):
        LCLBinding.Controls_TControl_ShowHelp()
#Procedure Controls_TControl_RemoveAllHandlersOfObject
    @staticmethod
    def RemoveAllHandlersOfObject(self,AnObject):
        LCLBinding.Controls_TControl_RemoveAllHandlersOfObject((AnObject.pointer))
#Procedure Controls_TControl_AddHandlerOnResize
    @staticmethod
    def AddHandlerOnResize(self,OnResizeEvent,AsFirst):
        LCLBinding.Controls_TControl_AddHandlerOnResize((OnResizeEvent.pointer),(booleantoint(AsFirst)))
#Procedure Controls_TControl_RemoveHandlerOnResize
    @staticmethod
    def RemoveHandlerOnResize(self,OnResizeEvent):
        LCLBinding.Controls_TControl_RemoveHandlerOnResize((OnResizeEvent.pointer))
#Procedure Controls_TControl_AddHandlerOnChangeBounds
    @staticmethod
    def AddHandlerOnChangeBounds(self,OnChangeBoundsEvent,AsFirst):
        LCLBinding.Controls_TControl_AddHandlerOnChangeBounds((OnChangeBoundsEvent.pointer),(booleantoint(AsFirst)))
#Procedure Controls_TControl_RemoveHandlerOnChangeBounds
    @staticmethod
    def RemoveHandlerOnChangeBounds(self,OnChangeBoundsEvent):
        LCLBinding.Controls_TControl_RemoveHandlerOnChangeBounds((OnChangeBoundsEvent.pointer))
#Procedure Controls_TControl_AddHandlerOnVisibleChanging
    @staticmethod
    def AddHandlerOnVisibleChanging(self,OnVisibleChangingEvent,AsFirst):
        LCLBinding.Controls_TControl_AddHandlerOnVisibleChanging((OnVisibleChangingEvent.pointer),(booleantoint(AsFirst)))
#Procedure Controls_TControl_RemoveHandlerOnVisibleChanging
    @staticmethod
    def RemoveHandlerOnVisibleChanging(self,OnVisibleChangingEvent):
        LCLBinding.Controls_TControl_RemoveHandlerOnVisibleChanging((OnVisibleChangingEvent.pointer))
#Procedure Controls_TControl_AddHandlerOnVisibleChanged
    @staticmethod
    def AddHandlerOnVisibleChanged(self,OnVisibleChangedEvent,AsFirst):
        LCLBinding.Controls_TControl_AddHandlerOnVisibleChanged((OnVisibleChangedEvent.pointer),(booleantoint(AsFirst)))
#Procedure Controls_TControl_RemoveHandlerOnVisibleChanged
    @staticmethod
    def RemoveHandlerOnVisibleChanged(self,OnVisibleChangedEvent):
        LCLBinding.Controls_TControl_RemoveHandlerOnVisibleChanged((OnVisibleChangedEvent.pointer))
#Procedure Controls_TControl_AddHandlerOnEnabledChanged
    @staticmethod
    def AddHandlerOnEnabledChanged(self,OnEnabledChangedEvent,AsFirst):
        LCLBinding.Controls_TControl_AddHandlerOnEnabledChanged((OnEnabledChangedEvent.pointer),(booleantoint(AsFirst)))
#Procedure Controls_TControl_RemoveHandlerOnEnableChanging
    @staticmethod
    def RemoveHandlerOnEnableChanging(self,OnEnableChangingEvent):
        LCLBinding.Controls_TControl_RemoveHandlerOnEnableChanging((OnEnableChangingEvent.pointer))
#Procedure Controls_TControl_AddHandlerOnBeforeDestruction
    @staticmethod
    def AddHandlerOnBeforeDestruction(self,OnBeforeDestructionEvent,AsFirst):
        LCLBinding.Controls_TControl_AddHandlerOnBeforeDestruction((OnBeforeDestructionEvent.pointer),(booleantoint(AsFirst)))
#Procedure Controls_TControl_RemoveHandlerOnBeforeDestruction
    @staticmethod
    def RemoveHandlerOnBeforeDestruction(self,OnBeforeDestructionEvent):
        LCLBinding.Controls_TControl_RemoveHandlerOnBeforeDestruction((OnBeforeDestructionEvent.pointer))
#Procedure Controls_TControl_AddHandlerOnMouseWheel
    @staticmethod
    def AddHandlerOnMouseWheel(self,OnMouseWheelEvent,AsFirst):
        LCLBinding.Controls_TControl_AddHandlerOnMouseWheel((OnMouseWheelEvent.pointer),(booleantoint(AsFirst)))
#Procedure Controls_TControl_RemoveHandlerOnMouseWheel
    @staticmethod
    def RemoveHandlerOnMouseWheel(self,OnMouseWheelEvent):
        LCLBinding.Controls_TControl_RemoveHandlerOnMouseWheel((OnMouseWheelEvent.pointer))
    def getAccessibleDescription(self):
        r=LCLBinding.get_Controls_TControl_AccessibleDescription(self.pointer)
        return LCLBindingUtil.ConvertPascalTCaption(r)
    def setAccessibleDescription(self,v):
        LCLBinding.set_Controls_TControl_AccessibleDescription(self.pointer,v)
    AccessibleDescription=property(getAccessibleDescription,setAccessibleDescription)
    def getAccessibleValue(self):
        r=LCLBinding.get_Controls_TControl_AccessibleValue(self.pointer)
        return LCLBindingUtil.ConvertPascalTCaption(r)
    def setAccessibleValue(self,v):
        LCLBinding.set_Controls_TControl_AccessibleValue(self.pointer,v)
    AccessibleValue=property(getAccessibleValue,setAccessibleValue)
    def getAccessibleRole(self):
        r=LCLBinding.get_Controls_TControl_AccessibleRole(self.pointer)
        return r
    def setAccessibleRole(self,v):
        LCLBinding.set_Controls_TControl_AccessibleRole(self.pointer,v.pointer)
    AccessibleRole=property(getAccessibleRole,setAccessibleRole)
    def getAction(self):
        r=LCLBinding.get_Controls_TControl_Action(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TBasicAction)
    def setAction(self,v):
        LCLBinding.set_Controls_TControl_Action(self.pointer,v.pointer)
    Action=property(getAction,setAction)
    def getAlign(self):
        r=LCLBinding.get_Controls_TControl_Align(self.pointer)
        return r
    def setAlign(self,v):
        LCLBinding.set_Controls_TControl_Align(self.pointer,v.pointer)
    Align=property(getAlign,setAlign)
    def getAnchors(self):
        r=LCLBinding.get_Controls_TControl_Anchors(self.pointer)
        return r
    def setAnchors(self,v):
        LCLBinding.set_Controls_TControl_Anchors(self.pointer,v.pointer)
    Anchors=property(getAnchors,setAnchors)
    def getAutoSize(self):
        r=LCLBinding.get_Controls_TControl_AutoSize(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setAutoSize(self,v):
        LCLBinding.set_Controls_TControl_AutoSize(self.pointer,v)
    AutoSize=property(getAutoSize,setAutoSize)
    def getBorderSpacing(self):
        r=LCLBinding.get_Controls_TControl_BorderSpacing(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TControlBorderSpacing)
    def setBorderSpacing(self,v):
        LCLBinding.set_Controls_TControl_BorderSpacing(self.pointer,v.pointer)
    BorderSpacing=property(getBorderSpacing,setBorderSpacing)
    def getCaption(self):
        r=LCLBinding.get_Controls_TControl_Caption(self.pointer)
        return LCLBindingUtil.ConvertPascalTCaption(r)
    def setCaption(self,v):
        LCLBinding.set_Controls_TControl_Caption(self.pointer,v)
    Caption=property(getCaption,setCaption)
    def getCaptureMouseButtons(self):
        r=LCLBinding.get_Controls_TControl_CaptureMouseButtons(self.pointer)
        return r
    def setCaptureMouseButtons(self,v):
        LCLBinding.set_Controls_TControl_CaptureMouseButtons(self.pointer,v.pointer)
    CaptureMouseButtons=property(getCaptureMouseButtons,setCaptureMouseButtons)
    def getClientHeight(self):
        r=LCLBinding.get_Controls_TControl_ClientHeight(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setClientHeight(self,v):
        LCLBinding.set_Controls_TControl_ClientHeight(self.pointer,v)
    ClientHeight=property(getClientHeight,setClientHeight)
    def getClientWidth(self):
        r=LCLBinding.get_Controls_TControl_ClientWidth(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setClientWidth(self,v):
        LCLBinding.set_Controls_TControl_ClientWidth(self.pointer,v)
    ClientWidth=property(getClientWidth,setClientWidth)
    def getConstraints(self):
        r=LCLBinding.get_Controls_TControl_Constraints(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TSizeConstraints)
    def setConstraints(self,v):
        LCLBinding.set_Controls_TControl_Constraints(self.pointer,v.pointer)
    Constraints=property(getConstraints,setConstraints)
    def getControlState(self):
        r=LCLBinding.get_Controls_TControl_ControlState(self.pointer)
        return r
    def setControlState(self,v):
        LCLBinding.set_Controls_TControl_ControlState(self.pointer,v.pointer)
    ControlState=property(getControlState,setControlState)
    def getControlStyle(self):
        r=LCLBinding.get_Controls_TControl_ControlStyle(self.pointer)
        return r
    def setControlStyle(self,v):
        LCLBinding.set_Controls_TControl_ControlStyle(self.pointer,v.pointer)
    ControlStyle=property(getControlStyle,setControlStyle)
    def getEnabled(self):
        r=LCLBinding.get_Controls_TControl_Enabled(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setEnabled(self,v):
        LCLBinding.set_Controls_TControl_Enabled(self.pointer,v)
    Enabled=property(getEnabled,setEnabled)
    def getFont(self):
        r=LCLBinding.get_Controls_TControl_Font(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TFont)
    def setFont(self,v):
        LCLBinding.set_Controls_TControl_Font(self.pointer,v.pointer)
    Font=property(getFont,setFont)
    def getIsControl(self):
        r=LCLBinding.get_Controls_TControl_IsControl(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setIsControl(self,v):
        LCLBinding.set_Controls_TControl_IsControl(self.pointer,v)
    IsControl=property(getIsControl,setIsControl)
    def getMouseEntered(self):
        r=LCLBinding.get_Controls_TControl_MouseEntered(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    MouseEntered=property(getMouseEntered)
    def _Warper_OnChangeBounds(self,Sender):
        self.OnChangeBoundscall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnChangeBounds(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnChangeBoundscall'):
            FreeOldEvent=1
            oldobj=OnChangeBoundsPasObject
        self.OnChangeBoundscall=v 
        self.PasOnChangeBounds=FunctionForm(self._Warper_OnChangeBounds)
        self.OnChangeBoundsPasObject=LCLBinding.set_Controls_TControl_OnChangeBounds(self.pointer,self.PasOnChangeBounds,oldobj,FreeOldEvent)
    def getOnChangeBounds(self):
        return OnChangeBoundscall
    OnChangeBounds=property(getOnChangeBounds,setOnChangeBounds)
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
        self.OnClickPasObject=LCLBinding.set_Controls_TControl_OnClick(self.pointer,self.PasOnClick,oldobj,FreeOldEvent)
    def getOnClick(self):
        return OnClickcall
    OnClick=property(getOnClick,setOnClick)
    def _Warper_OnResize(self,Sender):
        self.OnResizecall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnResize(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnResizecall'):
            FreeOldEvent=1
            oldobj=OnResizePasObject
        self.OnResizecall=v 
        self.PasOnResize=FunctionForm(self._Warper_OnResize)
        self.OnResizePasObject=LCLBinding.set_Controls_TControl_OnResize(self.pointer,self.PasOnResize,oldobj,FreeOldEvent)
    def getOnResize(self):
        return OnResizecall
    OnResize=property(getOnResize,setOnResize)
    def getParent(self):
        r=LCLBinding.get_Controls_TControl_Parent(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TWinControl)
    def setParent(self,v):
        LCLBinding.set_Controls_TControl_Parent(self.pointer,v.pointer)
    Parent=property(getParent,setParent)
    def getPopupMenu(self):
        r=LCLBinding.get_Controls_TControl_PopupMenu(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TPopupmenu)
    def setPopupMenu(self,v):
        LCLBinding.set_Controls_TControl_PopupMenu(self.pointer,v.pointer)
    PopupMenu=property(getPopupMenu,setPopupMenu)
    def getShowHint(self):
        r=LCLBinding.get_Controls_TControl_ShowHint(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setShowHint(self,v):
        LCLBinding.set_Controls_TControl_ShowHint(self.pointer,v)
    ShowHint=property(getShowHint,setShowHint)
    def getVisible(self):
        r=LCLBinding.get_Controls_TControl_Visible(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setVisible(self,v):
        LCLBinding.set_Controls_TControl_Visible(self.pointer,v)
    Visible=property(getVisible,setVisible)
    def getDockOrientation(self):
        r=LCLBinding.get_Controls_TControl_DockOrientation(self.pointer)
        return r
    def setDockOrientation(self,v):
        LCLBinding.set_Controls_TControl_DockOrientation(self.pointer,v.pointer)
    DockOrientation=property(getDockOrientation,setDockOrientation)
    def getFloating(self):
        r=LCLBinding.get_Controls_TControl_Floating(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    Floating=property(getFloating)
    def getHostDockSite(self):
        r=LCLBinding.get_Controls_TControl_HostDockSite(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TWinControl)
    def setHostDockSite(self,v):
        LCLBinding.set_Controls_TControl_HostDockSite(self.pointer,v.pointer)
    HostDockSite=property(getHostDockSite,setHostDockSite)
    def getLRDockWidth(self):
        r=LCLBinding.get_Controls_TControl_LRDockWidth(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setLRDockWidth(self,v):
        LCLBinding.set_Controls_TControl_LRDockWidth(self.pointer,v)
    LRDockWidth=property(getLRDockWidth,setLRDockWidth)
    def getTBDockHeight(self):
        r=LCLBinding.get_Controls_TControl_TBDockHeight(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setTBDockHeight(self,v):
        LCLBinding.set_Controls_TControl_TBDockHeight(self.pointer,v)
    TBDockHeight=property(getTBDockHeight,setTBDockHeight)
    def getUndockHeight(self):
        r=LCLBinding.get_Controls_TControl_UndockHeight(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setUndockHeight(self,v):
        LCLBinding.set_Controls_TControl_UndockHeight(self.pointer,v)
    UndockHeight=property(getUndockHeight,setUndockHeight)
    def getUndockWidth(self):
        r=LCLBinding.get_Controls_TControl_UndockWidth(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setUndockWidth(self,v):
        LCLBinding.set_Controls_TControl_UndockWidth(self.pointer,v)
    UndockWidth=property(getUndockWidth,setUndockWidth)
    def getBiDiMode(self):
        r=LCLBinding.get_Controls_TControl_BiDiMode(self.pointer)
        return r
    def setBiDiMode(self,v):
        LCLBinding.set_Controls_TControl_BiDiMode(self.pointer,v.pointer)
    BiDiMode=property(getBiDiMode,setBiDiMode)
    def getParentBiDiMode(self):
        r=LCLBinding.get_Controls_TControl_ParentBiDiMode(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentBiDiMode(self,v):
        LCLBinding.set_Controls_TControl_ParentBiDiMode(self.pointer,v)
    ParentBiDiMode=property(getParentBiDiMode,setParentBiDiMode)
    def getAnchorSideLeft(self):
        r=LCLBinding.get_Controls_TControl_AnchorSideLeft(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TAnchorSide)
    def setAnchorSideLeft(self,v):
        LCLBinding.set_Controls_TControl_AnchorSideLeft(self.pointer,v.pointer)
    AnchorSideLeft=property(getAnchorSideLeft,setAnchorSideLeft)
    def getAnchorSideTop(self):
        r=LCLBinding.get_Controls_TControl_AnchorSideTop(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TAnchorSide)
    def setAnchorSideTop(self,v):
        LCLBinding.set_Controls_TControl_AnchorSideTop(self.pointer,v.pointer)
    AnchorSideTop=property(getAnchorSideTop,setAnchorSideTop)
    def getAnchorSideRight(self):
        r=LCLBinding.get_Controls_TControl_AnchorSideRight(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TAnchorSide)
    def setAnchorSideRight(self,v):
        LCLBinding.set_Controls_TControl_AnchorSideRight(self.pointer,v.pointer)
    AnchorSideRight=property(getAnchorSideRight,setAnchorSideRight)
    def getAnchorSideBottom(self):
        r=LCLBinding.get_Controls_TControl_AnchorSideBottom(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TAnchorSide)
    def setAnchorSideBottom(self,v):
        LCLBinding.set_Controls_TControl_AnchorSideBottom(self.pointer,v.pointer)
    AnchorSideBottom=property(getAnchorSideBottom,setAnchorSideBottom)
    def getLeft(self):
        r=LCLBinding.get_Controls_TControl_Left(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setLeft(self,v):
        LCLBinding.set_Controls_TControl_Left(self.pointer,v)
    Left=property(getLeft,setLeft)
    def getHeight(self):
        r=LCLBinding.get_Controls_TControl_Height(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setHeight(self,v):
        LCLBinding.set_Controls_TControl_Height(self.pointer,v)
    Height=property(getHeight,setHeight)
    def getTop(self):
        r=LCLBinding.get_Controls_TControl_Top(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setTop(self,v):
        LCLBinding.set_Controls_TControl_Top(self.pointer,v)
    Top=property(getTop,setTop)
    def getWidth(self):
        r=LCLBinding.get_Controls_TControl_Width(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setWidth(self,v):
        LCLBinding.set_Controls_TControl_Width(self.pointer,v)
    Width=property(getWidth,setWidth)
    def getHelpType(self):
        r=LCLBinding.get_Controls_TControl_HelpType(self.pointer)
        return r
    def setHelpType(self,v):
        LCLBinding.set_Controls_TControl_HelpType(self.pointer,v.pointer)
    HelpType=property(getHelpType,setHelpType)
    def getHelpKeyword(self):
        r=LCLBinding.get_Controls_TControl_HelpKeyword(self.pointer)
        return LCLBindingUtil.ConvertPascalstring(r)
    def setHelpKeyword(self,v):
        LCLBinding.set_Controls_TControl_HelpKeyword(self.pointer,v)
    HelpKeyword=property(getHelpKeyword,setHelpKeyword)
#class TControl end
#class TDockManager start
class TDockManager(TPersistent):
#    pointer=c_void_p()
    def __init__(self):#TDockManager
        TPersistent.__init__(self)
#constructorControls_TDockManager_Create
    @staticmethod
    def Create(ADockSite):
        return LCLBindingUtil.GetPytonObject(LCLBinding.Controls_TDockManager_Create((ADockSite.pointer)),TDockManager)
#Procedure Controls_TDockManager_BeginUpdate
    @staticmethod
    def BeginUpdate(self,):
        LCLBinding.Controls_TDockManager_BeginUpdate()
#Procedure Controls_TDockManager_EndUpdate
    @staticmethod
    def EndUpdate(self,):
        LCLBinding.Controls_TDockManager_EndUpdate()
#Procedure Controls_TDockManager_LoadFromStream
    @staticmethod
    def LoadFromStream(self,Stream):
        LCLBinding.Controls_TDockManager_LoadFromStream((Stream.pointer))
#Procedure Controls_TDockManager_RemoveControl
    @staticmethod
    def RemoveControl(self,Control):
        LCLBinding.Controls_TDockManager_RemoveControl((Control.pointer))
#Procedure Controls_TDockManager_ResetBounds
    @staticmethod
    def ResetBounds(self,Force):
        LCLBinding.Controls_TDockManager_ResetBounds((booleantoint(Force)))
#Procedure Controls_TDockManager_SaveToStream
    @staticmethod
    def SaveToStream(self,Stream):
        LCLBinding.Controls_TDockManager_SaveToStream((Stream.pointer))
#Procedure Controls_TDockManager_SetReplacingControl
    @staticmethod
    def SetReplacingControl(self,Control):
        LCLBinding.Controls_TDockManager_SetReplacingControl((Control.pointer))
#class TDockManager end
#class TControlChildSizing start
class TControlChildSizing(TPersistent):
#    pointer=c_void_p()
    def __init__(self):#TControlChildSizing
        TPersistent.__init__(self)
#constructorControls_TControlChildSizing_Create
    @staticmethod
    def Create(OwnerControl):
        return LCLBindingUtil.GetPytonObject(LCLBinding.Controls_TControlChildSizing_Create((OwnerControl.pointer)),TControlChildSizing)
#Procedure Controls_TControlChildSizing_Assign
    @staticmethod
    def Assign(self,Source):
        LCLBinding.Controls_TControlChildSizing_Assign((Source.pointer))
#Procedure Controls_TControlChildSizing_AssignTo
    @staticmethod
    def AssignTo(self,Dest):
        LCLBinding.Controls_TControlChildSizing_AssignTo((Dest.pointer))
#Procedure Controls_TControlChildSizing_SetGridSpacing
    @staticmethod
    def SetGridSpacing(self,Spacing):
        LCLBinding.Controls_TControlChildSizing_SetGridSpacing((Spacing))
    def getControl(self):
        r=LCLBinding.get_Controls_TControlChildSizing_Control(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TWinControl)
    Control=property(getControl)
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
        self.OnChangePasObject=LCLBinding.set_Controls_TControlChildSizing_OnChange(self.pointer,self.PasOnChange,oldobj,FreeOldEvent)
    def getOnChange(self):
        return OnChangecall
    OnChange=property(getOnChange,setOnChange)
    def getLeftRightSpacing(self):
        r=LCLBinding.get_Controls_TControlChildSizing_LeftRightSpacing(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setLeftRightSpacing(self,v):
        LCLBinding.set_Controls_TControlChildSizing_LeftRightSpacing(self.pointer,v)
    LeftRightSpacing=property(getLeftRightSpacing,setLeftRightSpacing)
    def getTopBottomSpacing(self):
        r=LCLBinding.get_Controls_TControlChildSizing_TopBottomSpacing(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setTopBottomSpacing(self,v):
        LCLBinding.set_Controls_TControlChildSizing_TopBottomSpacing(self.pointer,v)
    TopBottomSpacing=property(getTopBottomSpacing,setTopBottomSpacing)
    def getHorizontalSpacing(self):
        r=LCLBinding.get_Controls_TControlChildSizing_HorizontalSpacing(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setHorizontalSpacing(self,v):
        LCLBinding.set_Controls_TControlChildSizing_HorizontalSpacing(self.pointer,v)
    HorizontalSpacing=property(getHorizontalSpacing,setHorizontalSpacing)
    def getVerticalSpacing(self):
        r=LCLBinding.get_Controls_TControlChildSizing_VerticalSpacing(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setVerticalSpacing(self,v):
        LCLBinding.set_Controls_TControlChildSizing_VerticalSpacing(self.pointer,v)
    VerticalSpacing=property(getVerticalSpacing,setVerticalSpacing)
    def getEnlargeHorizontal(self):
        r=LCLBinding.get_Controls_TControlChildSizing_EnlargeHorizontal(self.pointer)
        return r
    def setEnlargeHorizontal(self,v):
        LCLBinding.set_Controls_TControlChildSizing_EnlargeHorizontal(self.pointer,v.pointer)
    EnlargeHorizontal=property(getEnlargeHorizontal,setEnlargeHorizontal)
    def getEnlargeVertical(self):
        r=LCLBinding.get_Controls_TControlChildSizing_EnlargeVertical(self.pointer)
        return r
    def setEnlargeVertical(self,v):
        LCLBinding.set_Controls_TControlChildSizing_EnlargeVertical(self.pointer,v.pointer)
    EnlargeVertical=property(getEnlargeVertical,setEnlargeVertical)
    def getShrinkHorizontal(self):
        r=LCLBinding.get_Controls_TControlChildSizing_ShrinkHorizontal(self.pointer)
        return r
    def setShrinkHorizontal(self,v):
        LCLBinding.set_Controls_TControlChildSizing_ShrinkHorizontal(self.pointer,v.pointer)
    ShrinkHorizontal=property(getShrinkHorizontal,setShrinkHorizontal)
    def getShrinkVertical(self):
        r=LCLBinding.get_Controls_TControlChildSizing_ShrinkVertical(self.pointer)
        return r
    def setShrinkVertical(self,v):
        LCLBinding.set_Controls_TControlChildSizing_ShrinkVertical(self.pointer,v.pointer)
    ShrinkVertical=property(getShrinkVertical,setShrinkVertical)
    def getLayout(self):
        r=LCLBinding.get_Controls_TControlChildSizing_Layout(self.pointer)
        return r
    def setLayout(self,v):
        LCLBinding.set_Controls_TControlChildSizing_Layout(self.pointer,v.pointer)
    Layout=property(getLayout,setLayout)
    def getControlsPerLine(self):
        r=LCLBinding.get_Controls_TControlChildSizing_ControlsPerLine(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setControlsPerLine(self,v):
        LCLBinding.set_Controls_TControlChildSizing_ControlsPerLine(self.pointer,v)
    ControlsPerLine=property(getControlsPerLine,setControlsPerLine)
#class TControlChildSizing end
#class TSizeConstraints start
class TSizeConstraints(TPersistent):
#    pointer=c_void_p()
    def __init__(self):#TSizeConstraints
        TPersistent.__init__(self)
#constructorControls_TSizeConstraints_Create
    @staticmethod
    def Create(AControl):
        return LCLBindingUtil.GetPytonObject(LCLBinding.Controls_TSizeConstraints_Create((AControl.pointer)),TSizeConstraints)
#Procedure Controls_TSizeConstraints_UpdateInterfaceConstraints
    @staticmethod
    def UpdateInterfaceConstraints(self,):
        LCLBinding.Controls_TSizeConstraints_UpdateInterfaceConstraints()
#Procedure Controls_TSizeConstraints_SetInterfaceConstraints
    @staticmethod
    def SetInterfaceConstraints(self,MinW,MinH,MaxW,MaxH):
        LCLBinding.Controls_TSizeConstraints_SetInterfaceConstraints((MinW),(MinH),(MaxW),(MaxH))
#Procedure Controls_TSizeConstraints_AutoAdjustLayout
    @staticmethod
    def AutoAdjustLayout(self,AXProportion,AYProportion):
        LCLBinding.Controls_TSizeConstraints_AutoAdjustLayout((AXProportion.pointer),(AYProportion.pointer))
    def getMaxInterfaceHeight(self):
        r=LCLBinding.get_Controls_TSizeConstraints_MaxInterfaceHeight(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    MaxInterfaceHeight=property(getMaxInterfaceHeight)
    def getMaxInterfaceWidth(self):
        r=LCLBinding.get_Controls_TSizeConstraints_MaxInterfaceWidth(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    MaxInterfaceWidth=property(getMaxInterfaceWidth)
    def getMinInterfaceHeight(self):
        r=LCLBinding.get_Controls_TSizeConstraints_MinInterfaceHeight(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    MinInterfaceHeight=property(getMinInterfaceHeight)
    def getMinInterfaceWidth(self):
        r=LCLBinding.get_Controls_TSizeConstraints_MinInterfaceWidth(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    MinInterfaceWidth=property(getMinInterfaceWidth)
    def getControl(self):
        r=LCLBinding.get_Controls_TSizeConstraints_Control(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TControl)
    Control=property(getControl)
    def getOptions(self):
        r=LCLBinding.get_Controls_TSizeConstraints_Options(self.pointer)
        return r
    def setOptions(self,v):
        LCLBinding.set_Controls_TSizeConstraints_Options(self.pointer,v.pointer)
    Options=property(getOptions,setOptions)
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
        self.OnChangePasObject=LCLBinding.set_Controls_TSizeConstraints_OnChange(self.pointer,self.PasOnChange,oldobj,FreeOldEvent)
    def getOnChange(self):
        return OnChangecall
    OnChange=property(getOnChange,setOnChange)
#class TSizeConstraints end
#class TControlBorderSpacing start
class TControlBorderSpacing(TPersistent):
#    pointer=c_void_p()
    def __init__(self):#TControlBorderSpacing
        TPersistent.__init__(self)
#Procedure Controls_TControlBorderSpacing_Assign
    @staticmethod
    def Assign(self,Source):
        LCLBinding.Controls_TControlBorderSpacing_Assign((Source.pointer))
#Procedure Controls_TControlBorderSpacing_AssignTo
    @staticmethod
    def AssignTo(self,Dest):
        LCLBinding.Controls_TControlBorderSpacing_AssignTo((Dest.pointer))
#Procedure Controls_TControlBorderSpacing_AutoAdjustLayout
    @staticmethod
    def AutoAdjustLayout(self,AXProportion,AYProportion):
        LCLBinding.Controls_TControlBorderSpacing_AutoAdjustLayout((AXProportion.pointer),(AYProportion.pointer))
    def getControl(self):
        r=LCLBinding.get_Controls_TControlBorderSpacing_Control(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TControl)
    Control=property(getControl)
    def getAroundLeft(self):
        r=LCLBinding.get_Controls_TControlBorderSpacing_AroundLeft(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    AroundLeft=property(getAroundLeft)
    def getAroundTop(self):
        r=LCLBinding.get_Controls_TControlBorderSpacing_AroundTop(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    AroundTop=property(getAroundTop)
    def getAroundRight(self):
        r=LCLBinding.get_Controls_TControlBorderSpacing_AroundRight(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    AroundRight=property(getAroundRight)
    def getAroundBottom(self):
        r=LCLBinding.get_Controls_TControlBorderSpacing_AroundBottom(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    AroundBottom=property(getAroundBottom)
    def getControlLeft(self):
        r=LCLBinding.get_Controls_TControlBorderSpacing_ControlLeft(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    ControlLeft=property(getControlLeft)
    def getControlTop(self):
        r=LCLBinding.get_Controls_TControlBorderSpacing_ControlTop(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    ControlTop=property(getControlTop)
    def getControlWidth(self):
        r=LCLBinding.get_Controls_TControlBorderSpacing_ControlWidth(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    ControlWidth=property(getControlWidth)
    def getControlHeight(self):
        r=LCLBinding.get_Controls_TControlBorderSpacing_ControlHeight(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    ControlHeight=property(getControlHeight)
    def getControlRight(self):
        r=LCLBinding.get_Controls_TControlBorderSpacing_ControlRight(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    ControlRight=property(getControlRight)
    def getControlBottom(self):
        r=LCLBinding.get_Controls_TControlBorderSpacing_ControlBottom(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    ControlBottom=property(getControlBottom)
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
        self.OnChangePasObject=LCLBinding.set_Controls_TControlBorderSpacing_OnChange(self.pointer,self.PasOnChange,oldobj,FreeOldEvent)
    def getOnChange(self):
        return OnChangecall
    OnChange=property(getOnChange,setOnChange)
    def getInnerBorder(self):
        r=LCLBinding.get_Controls_TControlBorderSpacing_InnerBorder(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setInnerBorder(self,v):
        LCLBinding.set_Controls_TControlBorderSpacing_InnerBorder(self.pointer,v)
    InnerBorder=property(getInnerBorder,setInnerBorder)
    def getCellAlignHorizontal(self):
        r=LCLBinding.get_Controls_TControlBorderSpacing_CellAlignHorizontal(self.pointer)
        return r
    def setCellAlignHorizontal(self,v):
        LCLBinding.set_Controls_TControlBorderSpacing_CellAlignHorizontal(self.pointer,v.pointer)
    CellAlignHorizontal=property(getCellAlignHorizontal,setCellAlignHorizontal)
    def getCellAlignVertical(self):
        r=LCLBinding.get_Controls_TControlBorderSpacing_CellAlignVertical(self.pointer)
        return r
    def setCellAlignVertical(self,v):
        LCLBinding.set_Controls_TControlBorderSpacing_CellAlignVertical(self.pointer,v.pointer)
    CellAlignVertical=property(getCellAlignVertical,setCellAlignVertical)
#class TControlBorderSpacing end
#class TAnchorSide start
class TAnchorSide(TPersistent):
#    pointer=c_void_p()
    def __init__(self):#TAnchorSide
        TPersistent.__init__(self)
#constructorControls_TAnchorSide_Create
    @staticmethod
    def Create(TheOwner,TheKind):
        return LCLBindingUtil.GetPytonObject(LCLBinding.Controls_TAnchorSide_Create((TheOwner.pointer),(TheKind.pointer)),TAnchorSide)
#Procedure Controls_TAnchorSide_Assign
    @staticmethod
    def Assign(self,Source):
        LCLBinding.Controls_TAnchorSide_Assign((Source.pointer))
#Procedure Controls_TAnchorSide_FixCenterAnchoring
    @staticmethod
    def FixCenterAnchoring(self,):
        LCLBinding.Controls_TAnchorSide_FixCenterAnchoring()
    def getOwner(self):
        r=LCLBinding.get_Controls_TAnchorSide_Owner(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TControl)
    Owner=property(getOwner)
    def getKind(self):
        r=LCLBinding.get_Controls_TAnchorSide_Kind(self.pointer)
        return r
    Kind=property(getKind)
    def getControl(self):
        r=LCLBinding.get_Controls_TAnchorSide_Control(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TControl)
    def setControl(self,v):
        LCLBinding.set_Controls_TAnchorSide_Control(self.pointer,v.pointer)
    Control=property(getControl,setControl)
    def getSide(self):
        r=LCLBinding.get_Controls_TAnchorSide_Side(self.pointer)
        return r
    def setSide(self,v):
        LCLBinding.set_Controls_TAnchorSide_Side(self.pointer,v.pointer)
    Side=property(getSide,setSide)
#class TAnchorSide end
#class TDragObject start
class TDragObject(TObject):
#    pointer=c_void_p()
    def __init__(self):#TDragObject
        TObject.__init__(self)
#constructorControls_TDragObject_Create
    @staticmethod
    def Create(AControl):
        return LCLBindingUtil.GetPytonObject(LCLBinding.Controls_TDragObject_Create((AControl.pointer)),TDragObject)
#constructorControls_TDragObject_AutoCreate
    @staticmethod
    def AutoCreate(AControl):
        return LCLBindingUtil.GetPytonObject(LCLBinding.Controls_TDragObject_AutoCreate((AControl.pointer)),TDragObject)
#Procedure Controls_TDragObject_HideDragImage
    @staticmethod
    def HideDragImage(self,):
        LCLBinding.Controls_TDragObject_HideDragImage()
#Procedure Controls_TDragObject_ShowDragImage
    @staticmethod
    def ShowDragImage(self,):
        LCLBinding.Controls_TDragObject_ShowDragImage()
    def getAlwaysShowDragImages(self):
        r=LCLBinding.get_Controls_TDragObject_AlwaysShowDragImages(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setAlwaysShowDragImages(self,v):
        LCLBinding.set_Controls_TDragObject_AlwaysShowDragImages(self.pointer,v)
    AlwaysShowDragImages=property(getAlwaysShowDragImages,setAlwaysShowDragImages)
    def getAutoCreated(self):
        r=LCLBinding.get_Controls_TDragObject_AutoCreated(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    AutoCreated=property(getAutoCreated)
    def getAutoFree(self):
        r=LCLBinding.get_Controls_TDragObject_AutoFree(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    AutoFree=property(getAutoFree)
    def getControl(self):
        r=LCLBinding.get_Controls_TDragObject_Control(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TControl)
    def setControl(self,v):
        LCLBinding.set_Controls_TDragObject_Control(self.pointer,v.pointer)
    Control=property(getControl,setControl)
    def getDragTarget(self):
        r=LCLBinding.get_Controls_TDragObject_DragTarget(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TControl)
    def setDragTarget(self,v):
        LCLBinding.set_Controls_TDragObject_DragTarget(self.pointer,v.pointer)
    DragTarget=property(getDragTarget,setDragTarget)
    def getDropped(self):
        r=LCLBinding.get_Controls_TDragObject_Dropped(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    Dropped=property(getDropped)
#class TDragObject end
#class TDragDockObject start
class TDragDockObject(TDragObject):
#    pointer=c_void_p()
    def __init__(self):#TDragDockObject
        TDragObject.__init__(self)
    def getDropAlign(self):
        r=LCLBinding.get_Controls_TDragDockObject_DropAlign(self.pointer)
        return r
    def setDropAlign(self,v):
        LCLBinding.set_Controls_TDragDockObject_DropAlign(self.pointer,v.pointer)
    DropAlign=property(getDropAlign,setDropAlign)
    def getDropOnControl(self):
        r=LCLBinding.get_Controls_TDragDockObject_DropOnControl(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TControl)
    def setDropOnControl(self,v):
        LCLBinding.set_Controls_TDragDockObject_DropOnControl(self.pointer,v.pointer)
    DropOnControl=property(getDropOnControl,setDropOnControl)
    def getFloating(self):
        r=LCLBinding.get_Controls_TDragDockObject_Floating(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setFloating(self,v):
        LCLBinding.set_Controls_TDragDockObject_Floating(self.pointer,v)
    Floating=property(getFloating,setFloating)
    def getIncreaseDockArea(self):
        r=LCLBinding.get_Controls_TDragDockObject_IncreaseDockArea(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    IncreaseDockArea=property(getIncreaseDockArea)
#constructorControls_TDragDockObject_AutoCreate
    @staticmethod
    def AutoCreate(AControl):
        return LCLBindingUtil.GetPytonObject(LCLBinding.Controls_TDragDockObject_AutoCreate((AControl.pointer)),TDragDockObject)
#class TDragDockObject end
#class TControlActionLink start
class TControlActionLink(TActionLink):
#    pointer=c_void_p()
    def __init__(self):#TControlActionLink
        TActionLink.__init__(self)
#constructorControls_TControlActionLink_Create
    @staticmethod
    def Create(AClient):
        return LCLBindingUtil.GetPytonObject(LCLBinding.Controls_TControlActionLink_Create((AClient.pointer)),TControlActionLink)
#class TControlActionLink end
#class TGraphicControl start
class TGraphicControl(TControl):
#    pointer=c_void_p()
    def __init__(self):#TGraphicControl
        TControl.__init__(self)
#constructorControls_TGraphicControl_Create
    @staticmethod
    def Create(AOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.Controls_TGraphicControl_Create((AOwner.pointer)),TGraphicControl)
    def getCanvas(self):
        r=LCLBinding.get_Controls_TGraphicControl_Canvas(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TCanvas)
    Canvas=property(getCanvas)
#class TGraphicControl end
#class TWinControl start
class TWinControl(TControl):
#    pointer=c_void_p()
    def __init__(self):#TWinControl
        TControl.__init__(self)
    def getBoundsLockCount(self):
        r=LCLBinding.get_Controls_TWinControl_BoundsLockCount(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    BoundsLockCount=property(getBoundsLockCount)
    def getBrush(self):
        r=LCLBinding.get_Controls_TWinControl_Brush(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TBrush)
    Brush=property(getBrush)
    def getCachedClientHeight(self):
        r=LCLBinding.get_Controls_TWinControl_CachedClientHeight(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    CachedClientHeight=property(getCachedClientHeight)
    def getCachedClientWidth(self):
        r=LCLBinding.get_Controls_TWinControl_CachedClientWidth(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    CachedClientWidth=property(getCachedClientWidth)
    def getChildSizing(self):
        r=LCLBinding.get_Controls_TWinControl_ChildSizing(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TControlChildSizing)
    def setChildSizing(self,v):
        LCLBinding.set_Controls_TWinControl_ChildSizing(self.pointer,v.pointer)
    ChildSizing=property(getChildSizing,setChildSizing)
    def getControlCount(self):
        r=LCLBinding.get_Controls_TWinControl_ControlCount(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    ControlCount=property(getControlCount)
    def getControls(self,Index):
        r=LCLBinding.get_Controls_TWinControl_Controls(self.pointer,Index)
        return LCLBindingUtil.GetPytonObject(r,TControl)
    def getDockClientCount(self):
        r=LCLBinding.get_Controls_TWinControl_DockClientCount(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    DockClientCount=property(getDockClientCount)
    def getDockClients(self,Index):
        r=LCLBinding.get_Controls_TWinControl_DockClients(self.pointer,Index)
        return LCLBindingUtil.GetPytonObject(r,TControl)
    def getDockManager(self):
        r=LCLBinding.get_Controls_TWinControl_DockManager(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TDockManager)
    def setDockManager(self,v):
        LCLBinding.set_Controls_TWinControl_DockManager(self.pointer,v.pointer)
    DockManager=property(getDockManager,setDockManager)
    def getDockSite(self):
        r=LCLBinding.get_Controls_TWinControl_DockSite(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setDockSite(self,v):
        LCLBinding.set_Controls_TWinControl_DockSite(self.pointer,v)
    DockSite=property(getDockSite,setDockSite)
    def getDoubleBuffered(self):
        r=LCLBinding.get_Controls_TWinControl_DoubleBuffered(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setDoubleBuffered(self,v):
        LCLBinding.set_Controls_TWinControl_DoubleBuffered(self.pointer,v)
    DoubleBuffered=property(getDoubleBuffered,setDoubleBuffered)
    def getIsResizing(self):
        r=LCLBinding.get_Controls_TWinControl_IsResizing(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    IsResizing=property(getIsResizing)
    def getTabStop(self):
        r=LCLBinding.get_Controls_TWinControl_TabStop(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setTabStop(self,v):
        LCLBinding.set_Controls_TWinControl_TabStop(self.pointer,v)
    TabStop=property(getTabStop,setTabStop)
    def _Warper_OnAlignInsertBefore(self,Sender,Control1,Control2):
        self.OnAlignInsertBeforecall(LCLBindingUtil.GetPytonObject(Sender,TWinControl),LCLBindingUtil.GetPytonObject(Control1,TControl),LCLBindingUtil.GetPytonObject(Control2,TControl))
    def setOnAlignInsertBefore(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnAlignInsertBeforecall'):
            FreeOldEvent=1
            oldobj=OnAlignInsertBeforePasObject
        self.OnAlignInsertBeforecall=v 
        self.PasOnAlignInsertBefore=FunctionForm(self._Warper_OnAlignInsertBefore)
        self.OnAlignInsertBeforePasObject=LCLBinding.set_Controls_TWinControl_OnAlignInsertBefore(self.pointer,self.PasOnAlignInsertBefore,oldobj,FreeOldEvent)
    def getOnAlignInsertBefore(self):
        return OnAlignInsertBeforecall
    OnAlignInsertBefore=property(getOnAlignInsertBefore,setOnAlignInsertBefore)
    def _Warper_OnDockDrop(self,Sender,Source,X,Y):
        self.OnDockDropcall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.GetPytonObject(Source,TDragDockObject),X,Y)
    def setOnDockDrop(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnDockDropcall'):
            FreeOldEvent=1
            oldobj=OnDockDropPasObject
        self.OnDockDropcall=v 
        self.PasOnDockDrop=FunctionForm(self._Warper_OnDockDrop)
        self.OnDockDropPasObject=LCLBinding.set_Controls_TWinControl_OnDockDrop(self.pointer,self.PasOnDockDrop,oldobj,FreeOldEvent)
    def getOnDockDrop(self):
        return OnDockDropcall
    OnDockDrop=property(getOnDockDrop,setOnDockDrop)
    def _Warper_OnDockOver(self,Sender,Source,X,Y,State,Accept):
        self.OnDockOvercall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.GetPytonObject(Source,TDragDockObject),X,Y,State,LCLBindingUtil.IntToBoolean(Accept))
    def setOnDockOver(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p,c_int,c_int,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnDockOvercall'):
            FreeOldEvent=1
            oldobj=OnDockOverPasObject
        self.OnDockOvercall=v 
        self.PasOnDockOver=FunctionForm(self._Warper_OnDockOver)
        self.OnDockOverPasObject=LCLBinding.set_Controls_TWinControl_OnDockOver(self.pointer,self.PasOnDockOver,oldobj,FreeOldEvent)
    def getOnDockOver(self):
        return OnDockOvercall
    OnDockOver=property(getOnDockOver,setOnDockOver)
    def _Warper_OnEnter(self,Sender):
        self.OnEntercall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnEnter(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnEntercall'):
            FreeOldEvent=1
            oldobj=OnEnterPasObject
        self.OnEntercall=v 
        self.PasOnEnter=FunctionForm(self._Warper_OnEnter)
        self.OnEnterPasObject=LCLBinding.set_Controls_TWinControl_OnEnter(self.pointer,self.PasOnEnter,oldobj,FreeOldEvent)
    def getOnEnter(self):
        return OnEntercall
    OnEnter=property(getOnEnter,setOnEnter)
    def _Warper_OnExit(self,Sender):
        self.OnExitcall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnExit(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnExitcall'):
            FreeOldEvent=1
            oldobj=OnExitPasObject
        self.OnExitcall=v 
        self.PasOnExit=FunctionForm(self._Warper_OnExit)
        self.OnExitPasObject=LCLBinding.set_Controls_TWinControl_OnExit(self.pointer,self.PasOnExit,oldobj,FreeOldEvent)
    def getOnExit(self):
        return OnExitcall
    OnExit=property(getOnExit,setOnExit)
    def _Warper_OnUnDock(self,Sender,Client,NewTarget,Allow):
        self.OnUnDockcall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.GetPytonObject(Client,TControl),LCLBindingUtil.GetPytonObject(NewTarget,TWinControl),LCLBindingUtil.IntToBoolean(Allow))
    def setOnUnDock(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p,c_void_p,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnUnDockcall'):
            FreeOldEvent=1
            oldobj=OnUnDockPasObject
        self.OnUnDockcall=v 
        self.PasOnUnDock=FunctionForm(self._Warper_OnUnDock)
        self.OnUnDockPasObject=LCLBinding.set_Controls_TWinControl_OnUnDock(self.pointer,self.PasOnUnDock,oldobj,FreeOldEvent)
    def getOnUnDock(self):
        return OnUnDockcall
    OnUnDock=property(getOnUnDock,setOnUnDock)
    def getShowing(self):
        r=LCLBinding.get_Controls_TWinControl_Showing(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    Showing=property(getShowing)
    def getUseDockManager(self):
        r=LCLBinding.get_Controls_TWinControl_UseDockManager(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setUseDockManager(self,v):
        LCLBinding.set_Controls_TWinControl_UseDockManager(self.pointer,v)
    UseDockManager=property(getUseDockManager,setUseDockManager)
    def getDesignerDeleting(self):
        r=LCLBinding.get_Controls_TWinControl_DesignerDeleting(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setDesignerDeleting(self,v):
        LCLBinding.set_Controls_TWinControl_DesignerDeleting(self.pointer,v)
    DesignerDeleting=property(getDesignerDeleting,setDesignerDeleting)
    def getVisibleDockClientCount(self):
        r=LCLBinding.get_Controls_TWinControl_VisibleDockClientCount(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    VisibleDockClientCount=property(getVisibleDockClientCount)
#Procedure Controls_TWinControl_BeginUpdateBounds
    @staticmethod
    def BeginUpdateBounds(self,):
        LCLBinding.Controls_TWinControl_BeginUpdateBounds()
#Procedure Controls_TWinControl_EndUpdateBounds
    @staticmethod
    def EndUpdateBounds(self,):
        LCLBinding.Controls_TWinControl_EndUpdateBounds()
#Procedure Controls_TWinControl_LockRealizeBounds
    @staticmethod
    def LockRealizeBounds(self,):
        LCLBinding.Controls_TWinControl_LockRealizeBounds()
#Procedure Controls_TWinControl_UnlockRealizeBounds
    @staticmethod
    def UnlockRealizeBounds(self,):
        LCLBinding.Controls_TWinControl_UnlockRealizeBounds()
#Procedure Controls_TWinControl_DoAdjustClientRectChange
    @staticmethod
    def DoAdjustClientRectChange(self,InvalidateRect):
        LCLBinding.Controls_TWinControl_DoAdjustClientRectChange((booleantoint(InvalidateRect)))
#Procedure Controls_TWinControl_InvalidateClientRectCache
    @staticmethod
    def InvalidateClientRectCache(self,WithChildControls):
        LCLBinding.Controls_TWinControl_InvalidateClientRectCache((booleantoint(WithChildControls)))
#Procedure Controls_TWinControl_SetBounds
    @staticmethod
    def SetBounds(self,ALeft,ATop,AWidth,AHeight):
        LCLBinding.Controls_TWinControl_SetBounds((ALeft),(ATop),(AWidth),(AHeight))
#Procedure Controls_TWinControl_DisableAlign
    @staticmethod
    def DisableAlign(self,):
        LCLBinding.Controls_TWinControl_DisableAlign()
#Procedure Controls_TWinControl_EnableAlign
    @staticmethod
    def EnableAlign(self,):
        LCLBinding.Controls_TWinControl_EnableAlign()
#Procedure Controls_TWinControl_ReAlign
    @staticmethod
    def ReAlign(self,):
        LCLBinding.Controls_TWinControl_ReAlign()
#Procedure Controls_TWinControl_ScrollBy_WS
    @staticmethod
    def ScrollBy_WS(self,DeltaX,DeltaY):
        LCLBinding.Controls_TWinControl_ScrollBy_WS((DeltaX),(DeltaY))
#Procedure Controls_TWinControl_ScrollBy
    @staticmethod
    def ScrollBy(self,DeltaX,DeltaY):
        LCLBinding.Controls_TWinControl_ScrollBy((DeltaX),(DeltaY))
#Procedure Controls_TWinControl_WriteLayoutDebugReport
    @staticmethod
    def WriteLayoutDebugReport(self,Prefix):
        LCLBinding.Controls_TWinControl_WriteLayoutDebugReport((Prefix))
#Procedure Controls_TWinControl_AutoAdjustLayout
    @staticmethod
    def AutoAdjustLayout(self,AMode,AFromPPI,AToPPI,AOldFormWidth,ANewFormWidth):
        LCLBinding.Controls_TWinControl_AutoAdjustLayout((AMode.pointer),(AFromPPI),(AToPPI),(AOldFormWidth),(ANewFormWidth))
#constructorControls_TWinControl_Create
    @staticmethod
    def Create(TheOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.Controls_TWinControl_Create((TheOwner.pointer)),TWinControl)
#Procedure Controls_TWinControl_DockDrop
    @staticmethod
    def DockDrop(self,DragDockObject,X,Y):
        LCLBinding.Controls_TWinControl_DockDrop((DragDockObject.pointer),(X),(Y))
#Procedure Controls_TWinControl_SetControlIndex
    @staticmethod
    def SetControlIndex(self,AControl,NewIndex):
        LCLBinding.Controls_TWinControl_SetControlIndex((AControl.pointer),(NewIndex))
#Procedure Controls_TWinControl_SelectNext
    @staticmethod
    def SelectNext(self,CurControl,GoForward,CheckTabStop):
        LCLBinding.Controls_TWinControl_SelectNext((CurControl.pointer),(booleantoint(GoForward)),(booleantoint(CheckTabStop)))
#Procedure Controls_TWinControl_Invalidate
    @staticmethod
    def Invalidate(self,):
        LCLBinding.Controls_TWinControl_Invalidate()
#Procedure Controls_TWinControl_AddControl
    @staticmethod
    def AddControl(self,):
        LCLBinding.Controls_TWinControl_AddControl()
#Procedure Controls_TWinControl_RemoveControl
    @staticmethod
    def RemoveControl(self,AControl):
        LCLBinding.Controls_TWinControl_RemoveControl((AControl.pointer))
#Procedure Controls_TWinControl_Repaint
    @staticmethod
    def Repaint(self,):
        LCLBinding.Controls_TWinControl_Repaint()
#Procedure Controls_TWinControl_Update
    @staticmethod
    def Update(self,):
        LCLBinding.Controls_TWinControl_Update()
#Procedure Controls_TWinControl_SetFocus
    @staticmethod
    def SetFocus(self,):
        LCLBinding.Controls_TWinControl_SetFocus()
#Procedure Controls_TWinControl_FlipChildren
    @staticmethod
    def FlipChildren(self,AllLevels):
        LCLBinding.Controls_TWinControl_FlipChildren((booleantoint(AllLevels)))
#Procedure Controls_TWinControl_ScaleBy
    @staticmethod
    def ScaleBy(self,Multiplier,Divider):
        LCLBinding.Controls_TWinControl_ScaleBy((Multiplier),(Divider))
#Procedure Controls_TWinControl_UpdateDockCaption
    @staticmethod
    def UpdateDockCaption(self,Exclude):
        LCLBinding.Controls_TWinControl_UpdateDockCaption((Exclude.pointer))
#Procedure Controls_TWinControl_GetTabOrderList
    @staticmethod
    def GetTabOrderList(self,List):
        LCLBinding.Controls_TWinControl_GetTabOrderList((List.pointer))
#Procedure Controls_TWinControl_HandleNeeded
    @staticmethod
    def HandleNeeded(self,):
        LCLBinding.Controls_TWinControl_HandleNeeded()
#class TWinControl end
#class TCustomControl start
class TCustomControl(TWinControl):
#    pointer=c_void_p()
    def __init__(self):#TCustomControl
        TWinControl.__init__(self)
#constructorControls_TCustomControl_Create
    @staticmethod
    def Create(AOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.Controls_TCustomControl_Create((AOwner.pointer)),TCustomControl)
    def getCanvas(self):
        r=LCLBinding.get_Controls_TCustomControl_Canvas(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TCanvas)
    def setCanvas(self,v):
        LCLBinding.set_Controls_TCustomControl_Canvas(self.pointer,v.pointer)
    Canvas=property(getCanvas,setCanvas)
    def _Warper_OnPaint(self,Sender):
        self.OnPaintcall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnPaint(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnPaintcall'):
            FreeOldEvent=1
            oldobj=OnPaintPasObject
        self.OnPaintcall=v 
        self.PasOnPaint=FunctionForm(self._Warper_OnPaint)
        self.OnPaintPasObject=LCLBinding.set_Controls_TCustomControl_OnPaint(self.pointer,self.PasOnPaint,oldobj,FreeOldEvent)
    def getOnPaint(self):
        return OnPaintcall
    OnPaint=property(getOnPaint,setOnPaint)
#class TCustomControl end
