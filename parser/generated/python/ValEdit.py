from MainPasObject import *
#import end
def CreateTKeyOptionsFromInt(i):
    dic={1:"keyEdit",2:"keyAdd",4:"keyDelete",8:"keyUnique"}
    return CreateSetFormint(i,dic)
def CreateTDisplayOptionsFromInt(i):
    dic={1:"doColumnTitles",2:"doAutoColResize",4:"doKeyColFixed"}
    return CreateSetFormint(i,dic)
#class TValueListStrings start
class TValueListStrings(TStringList):
#    pointer=c_void_p()
    def __init__(self):#TValueListStrings
        TStringList.__init__(self)
#class TValueListStrings end
#class TItemProp start
class TItemProp(TPersistent):
#    pointer=c_void_p()
    def __init__(self):#TItemProp
        TPersistent.__init__(self)
    def getEditMask(self):
        r=LCLBinding.get_ValEdit_TItemProp_EditMask(self.pointer)
        return LCLBindingUtil.ConvertPascalstring(r)
    def setEditMask(self,v):
        LCLBinding.set_ValEdit_TItemProp_EditMask(self.pointer,v)
    EditMask=property(getEditMask,setEditMask)
    def getEditStyle(self):
        r=LCLBinding.get_ValEdit_TItemProp_EditStyle(self.pointer)
        return r
    def setEditStyle(self,v):
        LCLBinding.set_ValEdit_TItemProp_EditStyle(self.pointer,v.pointer)
    EditStyle=property(getEditStyle,setEditStyle)
    def getKeyDesc(self):
        r=LCLBinding.get_ValEdit_TItemProp_KeyDesc(self.pointer)
        return LCLBindingUtil.ConvertPascalstring(r)
    def setKeyDesc(self,v):
        LCLBinding.set_ValEdit_TItemProp_KeyDesc(self.pointer,v)
    KeyDesc=property(getKeyDesc,setKeyDesc)
    def getPickList(self):
        r=LCLBinding.get_ValEdit_TItemProp_PickList(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TStrings)
    def setPickList(self,v):
        LCLBinding.set_ValEdit_TItemProp_PickList(self.pointer,v.pointer)
    PickList=property(getPickList,setPickList)
    def getMaxLength(self):
        r=LCLBinding.get_ValEdit_TItemProp_MaxLength(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setMaxLength(self,v):
        LCLBinding.set_ValEdit_TItemProp_MaxLength(self.pointer,v)
    MaxLength=property(getMaxLength,setMaxLength)
    def getReadOnly(self):
        r=LCLBinding.get_ValEdit_TItemProp_ReadOnly(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setReadOnly(self,v):
        LCLBinding.set_ValEdit_TItemProp_ReadOnly(self.pointer,v)
    ReadOnly=property(getReadOnly,setReadOnly)
#class TItemProp end
#class TValueListEditor start
class TValueListEditor(TCustomStringGrid):
#    pointer=c_void_p()
    def __init__(self):#TValueListEditor
        TCustomStringGrid.__init__(self)
#constructorValEdit_TValueListEditor_Create
    @staticmethod
    def Create(AOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.ValEdit_TValueListEditor_Create((AOwner.pointer)),TValueListEditor)
    def getModified(self):
        r=LCLBinding.get_ValEdit_TValueListEditor_Modified(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setModified(self,v):
        LCLBinding.set_ValEdit_TValueListEditor_Modified(self.pointer,v)
    Modified=property(getModified,setModified)
    def getKeys(self,Index):
        r=LCLBinding.get_ValEdit_TValueListEditor_Keys(self.pointer,Index)
        return LCLBindingUtil.ConvertPascalstring(r)
    def setKeys(self,Index,v):
        LCLBinding.set_ValEdit_TValueListEditor_Keys(self.pointer,Index,v)
    def getAutoEdit(self):
        r=LCLBinding.get_ValEdit_TValueListEditor_AutoEdit(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setAutoEdit(self,v):
        LCLBinding.set_ValEdit_TValueListEditor_AutoEdit(self.pointer,v)
    AutoEdit=property(getAutoEdit,setAutoEdit)
    def getDragKind(self):
        r=LCLBinding.get_ValEdit_TValueListEditor_DragKind(self.pointer)
        return r
    def setDragKind(self,v):
        LCLBinding.set_ValEdit_TValueListEditor_DragKind(self.pointer,v.pointer)
    DragKind=property(getDragKind,setDragKind)
    def getDragMode(self):
        r=LCLBinding.get_ValEdit_TValueListEditor_DragMode(self.pointer)
        return r
    def setDragMode(self,v):
        LCLBinding.set_ValEdit_TValueListEditor_DragMode(self.pointer,v.pointer)
    DragMode=property(getDragMode,setDragMode)
    def getHeaderHotZones(self):
        r=LCLBinding.get_ValEdit_TValueListEditor_HeaderHotZones(self.pointer)
        return r
    def setHeaderHotZones(self,v):
        LCLBinding.set_ValEdit_TValueListEditor_HeaderHotZones(self.pointer,v.pointer)
    HeaderHotZones=property(getHeaderHotZones,setHeaderHotZones)
    def getHeaderPushZones(self):
        r=LCLBinding.get_ValEdit_TValueListEditor_HeaderPushZones(self.pointer)
        return r
    def setHeaderPushZones(self,v):
        LCLBinding.set_ValEdit_TValueListEditor_HeaderPushZones(self.pointer,v.pointer)
    HeaderPushZones=property(getHeaderPushZones,setHeaderPushZones)
    def getMouseWheelOption(self):
        r=LCLBinding.get_ValEdit_TValueListEditor_MouseWheelOption(self.pointer)
        return r
    def setMouseWheelOption(self,v):
        LCLBinding.set_ValEdit_TValueListEditor_MouseWheelOption(self.pointer,v.pointer)
    MouseWheelOption=property(getMouseWheelOption,setMouseWheelOption)
    def getParentColor(self):
        r=LCLBinding.get_ValEdit_TValueListEditor_ParentColor(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentColor(self,v):
        LCLBinding.set_ValEdit_TValueListEditor_ParentColor(self.pointer,v)
    ParentColor=property(getParentColor,setParentColor)
    def getParentFont(self):
        r=LCLBinding.get_ValEdit_TValueListEditor_ParentFont(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentFont(self,v):
        LCLBinding.set_ValEdit_TValueListEditor_ParentFont(self.pointer,v)
    ParentFont=property(getParentFont,setParentFont)
    def getRowCount(self):
        r=LCLBinding.get_ValEdit_TValueListEditor_RowCount(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setRowCount(self,v):
        LCLBinding.set_ValEdit_TValueListEditor_RowCount(self.pointer,v)
    RowCount=property(getRowCount,setRowCount)
    def getTitleFont(self):
        r=LCLBinding.get_ValEdit_TValueListEditor_TitleFont(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TFont)
    def setTitleFont(self,v):
        LCLBinding.set_ValEdit_TValueListEditor_TitleFont(self.pointer,v.pointer)
    TitleFont=property(getTitleFont,setTitleFont)
    def getTitleImageList(self):
        r=LCLBinding.get_ValEdit_TValueListEditor_TitleImageList(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TImageList)
    def setTitleImageList(self,v):
        LCLBinding.set_ValEdit_TValueListEditor_TitleImageList(self.pointer,v.pointer)
    TitleImageList=property(getTitleImageList,setTitleImageList)
    def getTitleStyle(self):
        r=LCLBinding.get_ValEdit_TValueListEditor_TitleStyle(self.pointer)
        return r
    def setTitleStyle(self,v):
        LCLBinding.set_ValEdit_TValueListEditor_TitleStyle(self.pointer,v.pointer)
    TitleStyle=property(getTitleStyle,setTitleStyle)
    def _Warper_OnCheckboxToggled(self,sender,aCol,aRow,aState):
        self.OnCheckboxToggledcall(LCLBindingUtil.GetPytonObject(sender,TObject),aCol,aRow,aState)
    def setOnCheckboxToggled(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnCheckboxToggledcall'):
            FreeOldEvent=1
            oldobj=OnCheckboxToggledPasObject
        self.OnCheckboxToggledcall=v 
        self.PasOnCheckboxToggled=FunctionForm(self._Warper_OnCheckboxToggled)
        self.OnCheckboxToggledPasObject=LCLBinding.set_ValEdit_TValueListEditor_OnCheckboxToggled(self.pointer,self.PasOnCheckboxToggled,oldobj,FreeOldEvent)
    def getOnCheckboxToggled(self):
        return OnCheckboxToggledcall
    OnCheckboxToggled=property(getOnCheckboxToggled,setOnCheckboxToggled)
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
        self.OnEditingDonePasObject=LCLBinding.set_ValEdit_TValueListEditor_OnEditingDone(self.pointer,self.PasOnEditingDone,oldobj,FreeOldEvent)
    def getOnEditingDone(self):
        return OnEditingDonecall
    OnEditingDone=property(getOnEditingDone,setOnEditingDone)
    def _Warper_OnTopLeftChanged(self,Sender):
        self.OnTopLeftChangedcall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnTopLeftChanged(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnTopLeftChangedcall'):
            FreeOldEvent=1
            oldobj=OnTopLeftChangedPasObject
        self.OnTopLeftChangedcall=v 
        self.PasOnTopLeftChanged=FunctionForm(self._Warper_OnTopLeftChanged)
        self.OnTopLeftChangedPasObject=LCLBinding.set_ValEdit_TValueListEditor_OnTopLeftChanged(self.pointer,self.PasOnTopLeftChanged,oldobj,FreeOldEvent)
    def getOnTopLeftChanged(self):
        return OnTopLeftChangedcall
    OnTopLeftChanged=property(getOnTopLeftChanged,setOnTopLeftChanged)
    def _Warper_OnUserCheckboxBitmap(self,Sender,aCol,aRow,CheckedState,ABitmap):
        self.OnUserCheckboxBitmapcall(LCLBindingUtil.GetPytonObject(Sender,TObject),aCol,aRow,CheckedState,LCLBindingUtil.GetPytonObject(ABitmap,TBitmap))
    def setOnUserCheckboxBitmap(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int,c_int,c_int,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnUserCheckboxBitmapcall'):
            FreeOldEvent=1
            oldobj=OnUserCheckboxBitmapPasObject
        self.OnUserCheckboxBitmapcall=v 
        self.PasOnUserCheckboxBitmap=FunctionForm(self._Warper_OnUserCheckboxBitmap)
        self.OnUserCheckboxBitmapPasObject=LCLBinding.set_ValEdit_TValueListEditor_OnUserCheckboxBitmap(self.pointer,self.PasOnUserCheckboxBitmap,oldobj,FreeOldEvent)
    def getOnUserCheckboxBitmap(self):
        return OnUserCheckboxBitmapcall
    OnUserCheckboxBitmap=property(getOnUserCheckboxBitmap,setOnUserCheckboxBitmap)
    def _Warper_OnValidateEntry(self,sender,aCol,aRow,OldValue,NewValue):
        self.OnValidateEntrycall(LCLBindingUtil.GetPytonObject(sender,TObject),aCol,aRow,OldValue,NewValue)
    def setOnValidateEntry(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int,c_int,c_char_p,c_char_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnValidateEntrycall'):
            FreeOldEvent=1
            oldobj=OnValidateEntryPasObject
        self.OnValidateEntrycall=v 
        self.PasOnValidateEntry=FunctionForm(self._Warper_OnValidateEntry)
        self.OnValidateEntryPasObject=LCLBinding.set_ValEdit_TValueListEditor_OnValidateEntry(self.pointer,self.PasOnValidateEntry,oldobj,FreeOldEvent)
    def getOnValidateEntry(self):
        return OnValidateEntrycall
    OnValidateEntry=property(getOnValidateEntry,setOnValidateEntry)
    def getDisplayOptions(self):
        r=LCLBinding.get_ValEdit_TValueListEditor_DisplayOptions(self.pointer)
        return r
    def setDisplayOptions(self,v):
        LCLBinding.set_ValEdit_TValueListEditor_DisplayOptions(self.pointer,v.pointer)
    DisplayOptions=property(getDisplayOptions,setDisplayOptions)
    def getDropDownRows(self):
        r=LCLBinding.get_ValEdit_TValueListEditor_DropDownRows(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setDropDownRows(self,v):
        LCLBinding.set_ValEdit_TValueListEditor_DropDownRows(self.pointer,v)
    DropDownRows=property(getDropDownRows,setDropDownRows)
    def getKeyOptions(self):
        r=LCLBinding.get_ValEdit_TValueListEditor_KeyOptions(self.pointer)
        return r
    def setKeyOptions(self,v):
        LCLBinding.set_ValEdit_TValueListEditor_KeyOptions(self.pointer,v.pointer)
    KeyOptions=property(getKeyOptions,setKeyOptions)
    def getOptions(self):
        r=LCLBinding.get_ValEdit_TValueListEditor_Options(self.pointer)
        return r
    def setOptions(self,v):
        LCLBinding.set_ValEdit_TValueListEditor_Options(self.pointer,v.pointer)
    Options=property(getOptions,setOptions)
    def getStrings(self):
        r=LCLBinding.get_ValEdit_TValueListEditor_Strings(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TValueListStrings)
    def setStrings(self,v):
        LCLBinding.set_ValEdit_TValueListEditor_Strings(self.pointer,v.pointer)
    Strings=property(getStrings,setStrings)
    def getTitleCaptions(self):
        r=LCLBinding.get_ValEdit_TValueListEditor_TitleCaptions(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TStrings)
    def setTitleCaptions(self,v):
        LCLBinding.set_ValEdit_TValueListEditor_TitleCaptions(self.pointer,v.pointer)
    TitleCaptions=property(getTitleCaptions,setTitleCaptions)
    def _Warper_OnGetPickList(self,Sender,KeyName,Values):
        self.OnGetPickListcall(LCLBindingUtil.GetPytonObject(Sender,TObject),KeyName,LCLBindingUtil.GetPytonObject(Values,TStrings))
    def setOnGetPickList(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_char_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnGetPickListcall'):
            FreeOldEvent=1
            oldobj=OnGetPickListPasObject
        self.OnGetPickListcall=v 
        self.PasOnGetPickList=FunctionForm(self._Warper_OnGetPickList)
        self.OnGetPickListPasObject=LCLBinding.set_ValEdit_TValueListEditor_OnGetPickList(self.pointer,self.PasOnGetPickList,oldobj,FreeOldEvent)
    def getOnGetPickList(self):
        return OnGetPickListcall
    OnGetPickList=property(getOnGetPickList,setOnGetPickList)
    def _Warper_OnStringsChange(self,Sender):
        self.OnStringsChangecall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnStringsChange(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnStringsChangecall'):
            FreeOldEvent=1
            oldobj=OnStringsChangePasObject
        self.OnStringsChangecall=v 
        self.PasOnStringsChange=FunctionForm(self._Warper_OnStringsChange)
        self.OnStringsChangePasObject=LCLBinding.set_ValEdit_TValueListEditor_OnStringsChange(self.pointer,self.PasOnStringsChange,oldobj,FreeOldEvent)
    def getOnStringsChange(self):
        return OnStringsChangecall
    OnStringsChange=property(getOnStringsChange,setOnStringsChange)
    def _Warper_OnStringsChanging(self,Sender):
        self.OnStringsChangingcall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnStringsChanging(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnStringsChangingcall'):
            FreeOldEvent=1
            oldobj=OnStringsChangingPasObject
        self.OnStringsChangingcall=v 
        self.PasOnStringsChanging=FunctionForm(self._Warper_OnStringsChanging)
        self.OnStringsChangingPasObject=LCLBinding.set_ValEdit_TValueListEditor_OnStringsChanging(self.pointer,self.PasOnStringsChanging,oldobj,FreeOldEvent)
    def getOnStringsChanging(self):
        return OnStringsChangingcall
    OnStringsChanging=property(getOnStringsChanging,setOnStringsChanging)
#class TValueListEditor end
