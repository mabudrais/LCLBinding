from MainPasObject import *
#import end
#class TMainMenu start
class TMainMenu(TMenu):
#    pointer=c_void_p()
    def __init__(self):#TMainMenu
        TMenu.__init__(self)
#constructorMenus_TMainMenu_Create
    def Create(cls,AOwner):
        r=LCLBindingUtil.GetPytonObject(LCLBinding.Menus_TMainMenu_Create((AOwner.pointer)),TMainMenu)
    def getHeight(self):
        r=LCLBinding.Menus_TMainMenu_Height(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    Height=property(getHeight)
#class TMainMenu end
#class TMenuItem start
class TMenuItem(TLCLComponent):
#    pointer=c_void_p()
    def __init__(self):#TMenuItem
        TLCLComponent.__init__(self)
#constructorMenus_TMenuItem_Create
    def Create(cls,TheOwner):
        r=LCLBindingUtil.GetPytonObject(LCLBinding.Menus_TMenuItem_Create((TheOwner.pointer)),TMenuItem)
    def getCount(self):
        r=LCLBinding.Menus_TMenuItem_Count(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    Count=property(getCount)
    def getMenuIndex(self):
        r=LCLBinding.Menus_TMenuItem_MenuIndex(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    MenuIndex=property(getMenuIndex)
    def getAction(self):
        r=LCLBinding.Menus_TMenuItem_Action(self.pointer)
        return LCLBindingUtil.ConvertPascalpointer(r,TBasicAction)
    Action=property(getAction)
    def getAutoCheck(self):
        r=LCLBinding.Menus_TMenuItem_AutoCheck(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    AutoCheck=property(getAutoCheck)
    def getChecked(self):
        r=LCLBinding.Menus_TMenuItem_Checked(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    Checked=property(getChecked)
    def getDefault(self):
        r=LCLBinding.Menus_TMenuItem_Default(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    Default=property(getDefault)
    def getEnabled(self):
        r=LCLBinding.Menus_TMenuItem_Enabled(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    Enabled=property(getEnabled)
    def getBitmap(self):
        r=LCLBinding.Menus_TMenuItem_Bitmap(self.pointer)
        return LCLBindingUtil.ConvertPascalpointer(r,TBitmap)
    Bitmap=property(getBitmap)
    def getRadioItem(self):
        r=LCLBinding.Menus_TMenuItem_RadioItem(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    RadioItem=property(getRadioItem)
    def getRightJustify(self):
        r=LCLBinding.Menus_TMenuItem_RightJustify(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    RightJustify=property(getRightJustify)
    def getShowAlwaysCheckable(self):
        r=LCLBinding.Menus_TMenuItem_ShowAlwaysCheckable(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    ShowAlwaysCheckable=property(getShowAlwaysCheckable)
    def getSubMenuImages(self):
        r=LCLBinding.Menus_TMenuItem_SubMenuImages(self.pointer)
        return LCLBindingUtil.ConvertPascalpointer(r,TCustomImageList)
    SubMenuImages=property(getSubMenuImages)
    def getVisible(self):
        r=LCLBinding.Menus_TMenuItem_Visible(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    Visible=property(getVisible)
#class TMenuItem end
#class TMenu start
class TMenu(TLCLComponent):
#    pointer=c_void_p()
    def __init__(self):#TMenu
        TLCLComponent.__init__(self)
#constructorMenus_TMenu_Create
    def Create(cls,AOwner):
        r=LCLBindingUtil.GetPytonObject(LCLBinding.Menus_TMenu_Create((AOwner.pointer)),TMenu)
    def getParent(self):
        r=LCLBinding.Menus_TMenu_Parent(self.pointer)
        return LCLBindingUtil.ConvertPascalpointer(r,TComponent)
    Parent=property(getParent)
    def getShortcutHandled(self):
        r=LCLBinding.Menus_TMenu_ShortcutHandled(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    ShortcutHandled=property(getShortcutHandled)
    def getParentBidiMode(self):
        r=LCLBinding.Menus_TMenu_ParentBidiMode(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    ParentBidiMode=property(getParentBidiMode)
    def getItems(self):
        r=LCLBinding.Menus_TMenu_Items(self.pointer)
        return LCLBindingUtil.ConvertPascalpointer(r,TMenuItem)
    Items=property(getItems)
    def getImages(self):
        r=LCLBinding.Menus_TMenu_Images(self.pointer)
        return LCLBindingUtil.ConvertPascalpointer(r,TCustomImageList)
    Images=property(getImages)
    def getOwnerDraw(self):
        r=LCLBinding.Menus_TMenu_OwnerDraw(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    OwnerDraw=property(getOwnerDraw)
#class TMenu end
#class TPopupMenu start
class TPopupMenu(TMenu):
#    pointer=c_void_p()
    def __init__(self):#TPopupMenu
        TMenu.__init__(self)
#constructorMenus_TPopupMenu_Create
    def Create(cls,AOwner):
        r=LCLBindingUtil.GetPytonObject(LCLBinding.Menus_TPopupMenu_Create((AOwner.pointer)),TPopupMenu)
    def getPopupComponent(self):
        r=LCLBinding.Menus_TPopupMenu_PopupComponent(self.pointer)
        return LCLBindingUtil.ConvertPascalpointer(r,TComponent)
    PopupComponent=property(getPopupComponent)
    def getAutoPopup(self):
        r=LCLBinding.Menus_TPopupMenu_AutoPopup(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    AutoPopup=property(getAutoPopup)
#class TPopupMenu end
