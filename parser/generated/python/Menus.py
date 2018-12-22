from LCLClasses import *
from ImgList import *
from Graphics import *
from ActnList import *
from lmessages import *
from lresources import *
from lclproc import *
from lcltype import *
from lclstrconsts import *
from Classes import *
from MainPasObject import *
import LCLBindingUtil
#import end
#class TMenu start
class TMenu(TLCLComponent):
#    pointer=c_void_p()
    def __init__(self):#TMenu
        TLCLComponent.__init__(self)
#constructorMenus_TMenu_Create
    @staticmethod
    def Create(AOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.Menus_TMenu_Create((AOwner.pointer)),TMenu)
#Procedure Menus_TMenu_DestroyHandle
    @staticmethod
    def DestroyHandle(self,):
        LCLBinding.Menus_TMenu_DestroyHandle()
#Procedure Menus_TMenu_HandleNeeded
    @staticmethod
    def HandleNeeded(self,):
        LCLBinding.Menus_TMenu_HandleNeeded()
    def getParent(self):
        r=LCLBinding.get_Menus_TMenu_Parent(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TComponent)
    def setParent(self,v):
        LCLBinding.set_Menus_TMenu_Parent(self.pointer,v.pointer)
    Parent=property(getParent,setParent)
    def getShortcutHandled(self):
        r=LCLBinding.get_Menus_TMenu_ShortcutHandled(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setShortcutHandled(self,v):
        LCLBinding.set_Menus_TMenu_ShortcutHandled(self.pointer,v)
    ShortcutHandled=property(getShortcutHandled,setShortcutHandled)
    def getBidiMode(self):
        r=LCLBinding.get_Menus_TMenu_BidiMode(self.pointer)
        return r
    def setBidiMode(self,v):
        LCLBinding.set_Menus_TMenu_BidiMode(self.pointer,v.pointer)
    BidiMode=property(getBidiMode,setBidiMode)
    def getParentBidiMode(self):
        r=LCLBinding.get_Menus_TMenu_ParentBidiMode(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentBidiMode(self,v):
        LCLBinding.set_Menus_TMenu_ParentBidiMode(self.pointer,v)
    ParentBidiMode=property(getParentBidiMode,setParentBidiMode)
    def getItems(self):
        r=LCLBinding.get_Menus_TMenu_Items(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TMenuItem)
    Items=property(getItems)
    def getImages(self):
        r=LCLBinding.get_Menus_TMenu_Images(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TCustomImageList)
    def setImages(self,v):
        LCLBinding.set_Menus_TMenu_Images(self.pointer,v.pointer)
    Images=property(getImages,setImages)
    def getOwnerDraw(self):
        r=LCLBinding.get_Menus_TMenu_OwnerDraw(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setOwnerDraw(self,v):
        LCLBinding.set_Menus_TMenu_OwnerDraw(self.pointer,v)
    OwnerDraw=property(getOwnerDraw,setOwnerDraw)
    def _Warper_OnMeasureItem(self,Sender,ACanvas,AWidth,AHeight):
        self.OnMeasureItemcall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.GetPytonObject(ACanvas,TCanvas),AWidth,AHeight)
    def setOnMeasureItem(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnMeasureItemcall'):
            FreeOldEvent=1
            oldobj=self.OnMeasureItemPasObject
        self.OnMeasureItemcall=v 
        self.PasOnMeasureItem=FunctionForm(self._Warper_OnMeasureItem)
        self.OnMeasureItemPasObject=LCLBinding.set_Menus_TMenu_OnMeasureItem(self.pointer,self.PasOnMeasureItem,oldobj,FreeOldEvent)
    def getOnMeasureItem(self):
        return OnMeasureItemcall
    OnMeasureItem=property(getOnMeasureItem,setOnMeasureItem)
#class TMenu end
#class TMenuActionLink start
class TMenuActionLink(TActionLink):
#    pointer=c_void_p()
    def __init__(self):#TMenuActionLink
        TActionLink.__init__(self)
#constructorMenus_TMenuActionLink_Create
    @staticmethod
    def Create(AClient):
        return LCLBindingUtil.GetPytonObject(LCLBinding.Menus_TMenuActionLink_Create((AClient.pointer)),TMenuActionLink)
#class TMenuActionLink end
#class TMenuItem start
class TMenuItem(TLCLComponent):
#    pointer=c_void_p()
    def __init__(self):#TMenuItem
        TLCLComponent.__init__(self)
#constructorMenus_TMenuItem_Create
    @staticmethod
    def Create(TheOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.Menus_TMenuItem_Create((TheOwner.pointer)),TMenuItem)
#Procedure Menus_TMenuItem_InitiateAction
    @staticmethod
    def InitiateAction(self,):
        LCLBinding.Menus_TMenuItem_InitiateAction()
#Procedure Menus_TMenuItem_IntfDoSelect
    @staticmethod
    def IntfDoSelect(self,):
        LCLBinding.Menus_TMenuItem_IntfDoSelect()
#Procedure Menus_TMenuItem_AddSeparator
    @staticmethod
    def AddSeparator(self,):
        LCLBinding.Menus_TMenuItem_AddSeparator()
#Procedure Menus_TMenuItem_Click
    @staticmethod
    def Click(self,):
        LCLBinding.Menus_TMenuItem_Click()
#Procedure Menus_TMenuItem_Delete
    @staticmethod
    def Delete(self,Index):
        LCLBinding.Menus_TMenuItem_Delete((Index))
#Procedure Menus_TMenuItem_HandleNeeded
    @staticmethod
    def HandleNeeded(self,):
        LCLBinding.Menus_TMenuItem_HandleNeeded()
#Procedure Menus_TMenuItem_Insert
    @staticmethod
    def Insert(self,Index,Item):
        LCLBinding.Menus_TMenuItem_Insert((Index),(Item.pointer))
#Procedure Menus_TMenuItem_RecreateHandle
    @staticmethod
    def RecreateHandle(self,):
        LCLBinding.Menus_TMenuItem_RecreateHandle()
#Procedure Menus_TMenuItem_Remove
    @staticmethod
    def Remove(self,Item):
        LCLBinding.Menus_TMenuItem_Remove((Item.pointer))
#Procedure Menus_TMenuItem_Clear
    @staticmethod
    def Clear(self,):
        LCLBinding.Menus_TMenuItem_Clear()
#Procedure Menus_TMenuItem_RemoveAllHandlersOfObject
    @staticmethod
    def RemoveAllHandlersOfObject(self,AnObject):
        LCLBinding.Menus_TMenuItem_RemoveAllHandlersOfObject((AnObject.pointer))
#Procedure Menus_TMenuItem_AddHandlerOnDestroy
    @staticmethod
    def AddHandlerOnDestroy(self,OnDestroyEvent,AsFirst):
        LCLBinding.Menus_TMenuItem_AddHandlerOnDestroy((OnDestroyEvent.pointer),(booleantoint(AsFirst)))
#Procedure Menus_TMenuItem_RemoveHandlerOnDestroy
    @staticmethod
    def RemoveHandlerOnDestroy(self,OnDestroyEvent):
        LCLBinding.Menus_TMenuItem_RemoveHandlerOnDestroy((OnDestroyEvent.pointer))
    def getCount(self):
        r=LCLBinding.get_Menus_TMenuItem_Count(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    Count=property(getCount)
    def getItems(self,Index):
        r=LCLBinding.get_Menus_TMenuItem_Items(self.pointer,Index)
        return LCLBindingUtil.GetPytonObject(r,TMenuItem)
    def getMenuIndex(self):
        r=LCLBinding.get_Menus_TMenuItem_MenuIndex(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setMenuIndex(self,v):
        LCLBinding.set_Menus_TMenuItem_MenuIndex(self.pointer,v)
    MenuIndex=property(getMenuIndex,setMenuIndex)
    def getMenu(self):
        r=LCLBinding.get_Menus_TMenuItem_Menu(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TMenu)
    Menu=property(getMenu)
    def getParent(self):
        r=LCLBinding.get_Menus_TMenuItem_Parent(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TMenuItem)
    Parent=property(getParent)
#Procedure Menus_TMenuItem_WriteDebugReport
    @staticmethod
    def WriteDebugReport(self,Prefix):
        LCLBinding.Menus_TMenuItem_WriteDebugReport((Prefix))
    def getAction(self):
        r=LCLBinding.get_Menus_TMenuItem_Action(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TBasicAction)
    def setAction(self,v):
        LCLBinding.set_Menus_TMenuItem_Action(self.pointer,v.pointer)
    Action=property(getAction,setAction)
    def getAutoCheck(self):
        r=LCLBinding.get_Menus_TMenuItem_AutoCheck(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setAutoCheck(self,v):
        LCLBinding.set_Menus_TMenuItem_AutoCheck(self.pointer,v)
    AutoCheck=property(getAutoCheck,setAutoCheck)
    def getChecked(self):
        r=LCLBinding.get_Menus_TMenuItem_Checked(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setChecked(self,v):
        LCLBinding.set_Menus_TMenuItem_Checked(self.pointer,v)
    Checked=property(getChecked,setChecked)
    def getDefault(self):
        r=LCLBinding.get_Menus_TMenuItem_Default(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setDefault(self,v):
        LCLBinding.set_Menus_TMenuItem_Default(self.pointer,v)
    Default=property(getDefault,setDefault)
    def getEnabled(self):
        r=LCLBinding.get_Menus_TMenuItem_Enabled(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setEnabled(self,v):
        LCLBinding.set_Menus_TMenuItem_Enabled(self.pointer,v)
    Enabled=property(getEnabled,setEnabled)
    def getBitmap(self):
        r=LCLBinding.get_Menus_TMenuItem_Bitmap(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TBitmap)
    def setBitmap(self,v):
        LCLBinding.set_Menus_TMenuItem_Bitmap(self.pointer,v.pointer)
    Bitmap=property(getBitmap,setBitmap)
    def getGlyphShowMode(self):
        r=LCLBinding.get_Menus_TMenuItem_GlyphShowMode(self.pointer)
        return r
    def setGlyphShowMode(self,v):
        LCLBinding.set_Menus_TMenuItem_GlyphShowMode(self.pointer,v.pointer)
    GlyphShowMode=property(getGlyphShowMode,setGlyphShowMode)
    def getRadioItem(self):
        r=LCLBinding.get_Menus_TMenuItem_RadioItem(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setRadioItem(self,v):
        LCLBinding.set_Menus_TMenuItem_RadioItem(self.pointer,v)
    RadioItem=property(getRadioItem,setRadioItem)
    def getRightJustify(self):
        r=LCLBinding.get_Menus_TMenuItem_RightJustify(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setRightJustify(self,v):
        LCLBinding.set_Menus_TMenuItem_RightJustify(self.pointer,v)
    RightJustify=property(getRightJustify,setRightJustify)
    def getShowAlwaysCheckable(self):
        r=LCLBinding.get_Menus_TMenuItem_ShowAlwaysCheckable(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setShowAlwaysCheckable(self,v):
        LCLBinding.set_Menus_TMenuItem_ShowAlwaysCheckable(self.pointer,v)
    ShowAlwaysCheckable=property(getShowAlwaysCheckable,setShowAlwaysCheckable)
    def getSubMenuImages(self):
        r=LCLBinding.get_Menus_TMenuItem_SubMenuImages(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TCustomImageList)
    def setSubMenuImages(self,v):
        LCLBinding.set_Menus_TMenuItem_SubMenuImages(self.pointer,v.pointer)
    SubMenuImages=property(getSubMenuImages,setSubMenuImages)
    def getVisible(self):
        r=LCLBinding.get_Menus_TMenuItem_Visible(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setVisible(self,v):
        LCLBinding.set_Menus_TMenuItem_Visible(self.pointer,v)
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
        self.OnClickPasObject=LCLBinding.set_Menus_TMenuItem_OnClick(self.pointer,self.PasOnClick,oldobj,FreeOldEvent)
    def getOnClick(self):
        return OnClickcall
    OnClick=property(getOnClick,setOnClick)
    def _Warper_OnMeasureItem(self,Sender,ACanvas,AWidth,AHeight):
        self.OnMeasureItemcall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.GetPytonObject(ACanvas,TCanvas),AWidth,AHeight)
    def setOnMeasureItem(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnMeasureItemcall'):
            FreeOldEvent=1
            oldobj=self.OnMeasureItemPasObject
        self.OnMeasureItemcall=v 
        self.PasOnMeasureItem=FunctionForm(self._Warper_OnMeasureItem)
        self.OnMeasureItemPasObject=LCLBinding.set_Menus_TMenuItem_OnMeasureItem(self.pointer,self.PasOnMeasureItem,oldobj,FreeOldEvent)
    def getOnMeasureItem(self):
        return OnMeasureItemcall
    OnMeasureItem=property(getOnMeasureItem,setOnMeasureItem)
#class TMenuItem end
#class TMainMenu start
class TMainMenu(TMenu):
#    pointer=c_void_p()
    def __init__(self):#TMainMenu
        TMenu.__init__(self)
#constructorMenus_TMainMenu_Create
    @staticmethod
    def Create(AOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.Menus_TMainMenu_Create((AOwner.pointer)),TMainMenu)
    def getHeight(self):
        r=LCLBinding.get_Menus_TMainMenu_Height(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    Height=property(getHeight)
    def _Warper_OnChange(self,Sender,Source,Rebuild):
        self.OnChangecall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.GetPytonObject(Source,TMenuItem),LCLBindingUtil.IntToBoolean(Rebuild))
    def setOnChange(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnChangecall'):
            FreeOldEvent=1
            oldobj=self.OnChangePasObject
        self.OnChangecall=v 
        self.PasOnChange=FunctionForm(self._Warper_OnChange)
        self.OnChangePasObject=LCLBinding.set_Menus_TMainMenu_OnChange(self.pointer,self.PasOnChange,oldobj,FreeOldEvent)
    def getOnChange(self):
        return OnChangecall
    OnChange=property(getOnChange,setOnChange)
#class TMainMenu end
#class TPopupMenu start
class TPopupMenu(TMenu):
#    pointer=c_void_p()
    def __init__(self):#TPopupMenu
        TMenu.__init__(self)
#constructorMenus_TPopupMenu_Create
    @staticmethod
    def Create(AOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.Menus_TPopupMenu_Create((AOwner.pointer)),TPopupMenu)
    def getPopupComponent(self):
        r=LCLBinding.get_Menus_TPopupMenu_PopupComponent(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TComponent)
    def setPopupComponent(self,v):
        LCLBinding.set_Menus_TPopupMenu_PopupComponent(self.pointer,v.pointer)
    PopupComponent=property(getPopupComponent,setPopupComponent)
#Procedure Menus_TPopupMenu_Close
    @staticmethod
    def Close(self,):
        LCLBinding.Menus_TPopupMenu_Close()
    def getAlignment(self):
        r=LCLBinding.get_Menus_TPopupMenu_Alignment(self.pointer)
        return r
    def setAlignment(self,v):
        LCLBinding.set_Menus_TPopupMenu_Alignment(self.pointer,v.pointer)
    Alignment=property(getAlignment,setAlignment)
    def getAutoPopup(self):
        r=LCLBinding.get_Menus_TPopupMenu_AutoPopup(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setAutoPopup(self,v):
        LCLBinding.set_Menus_TPopupMenu_AutoPopup(self.pointer,v)
    AutoPopup=property(getAutoPopup,setAutoPopup)
    def getTrackButton(self):
        r=LCLBinding.get_Menus_TPopupMenu_TrackButton(self.pointer)
        return r
    def setTrackButton(self,v):
        LCLBinding.set_Menus_TPopupMenu_TrackButton(self.pointer,v.pointer)
    TrackButton=property(getTrackButton,setTrackButton)
    def _Warper_OnPopup(self,Sender):
        self.OnPopupcall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnPopup(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnPopupcall'):
            FreeOldEvent=1
            oldobj=self.OnPopupPasObject
        self.OnPopupcall=v 
        self.PasOnPopup=FunctionForm(self._Warper_OnPopup)
        self.OnPopupPasObject=LCLBinding.set_Menus_TPopupMenu_OnPopup(self.pointer,self.PasOnPopup,oldobj,FreeOldEvent)
    def getOnPopup(self):
        return OnPopupcall
    OnPopup=property(getOnPopup,setOnPopup)
    def _Warper_OnClose(self,Sender):
        self.OnClosecall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnClose(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnClosecall'):
            FreeOldEvent=1
            oldobj=self.OnClosePasObject
        self.OnClosecall=v 
        self.PasOnClose=FunctionForm(self._Warper_OnClose)
        self.OnClosePasObject=LCLBinding.set_Menus_TPopupMenu_OnClose(self.pointer,self.PasOnClose,oldobj,FreeOldEvent)
    def getOnClose(self):
        return OnClosecall
    OnClose=property(getOnClose,setOnClose)
#class TPopupMenu end
