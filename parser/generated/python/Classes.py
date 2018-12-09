from MainPasObject import *
#import end
def CreateTShiftStateFromInt(i):
    dic={1:"ssShift",2:"ssAlt",4:"ssCtrl",8:"ssLeft",16:"ssRight",32:"ssMiddle",64:"ssDouble",128:"ssMeta",256:"ssSuper",512:"ssHyper",1024:"ssAltGr",2048:"ssCaps",4096:"ssNum",8192:"ssScroll",16384:"ssTriple",32768:"ssQuad",65536:"ssExtra1",131072:"ssExtra2"}
    return CreateSetFormint(i,dic)
def CreateTComponentStyleFromInt(i):
    dic={1:"csInheritable",2:"csCheckPropAvail",4:"csSubComponent",8:"csTransient"}
    return CreateSetFormint(i,dic)
def CreateTComponentStateFromInt(i):
    dic={1:"csLoading",2:"csReading",4:"csWriting",8:"csDestroying",16:"csDesigning",32:"csAncestor",64:"csUpdating",128:"csFixups",256:"csFreeNotification",512:"csInline",1024:"csDesignInstance"}
    return CreateSetFormint(i,dic)
#class TPersistent start
class TPersistent(TObject):
#    pointer=c_void_p()
    def __init__(self):#TPersistent
        TObject.__init__(self)
#class TPersistent end
#class TCollection start
class TCollection(TPersistent):
#    pointer=c_void_p()
    def __init__(self):#TCollection
        TPersistent.__init__(self)
    def getCount(self):
        r=LCLBinding.get_Classes_TCollection_Count(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    Count=property(getCount)
    def getItems(self,Index):
        r=LCLBinding.get_Classes_TCollection_Items(self.pointer,Index)
        return LCLBindingUtil.GetPytonObject(r,TCollectionItem)
    def setItems(self,Index,v):
        LCLBinding.set_Classes_TCollection_Items(self.pointer,Index,v.pointer)
#class TCollection end
#class TStrings start
class TStrings(TPersistent):
#    pointer=c_void_p()
    def __init__(self):#TStrings
        TPersistent.__init__(self)
    def getDelimitedText(self):
        r=LCLBinding.get_Classes_TStrings_DelimitedText(self.pointer)
        return LCLBindingUtil.ConvertPascalstring(r)
    def setDelimitedText(self,v):
        LCLBinding.set_Classes_TStrings_DelimitedText(self.pointer,v)
    DelimitedText=property(getDelimitedText,setDelimitedText)
    def getLineBreak(self):
        r=LCLBinding.get_Classes_TStrings_LineBreak(self.pointer)
        return LCLBindingUtil.ConvertPascalstring(r)
    def setLineBreak(self,v):
        LCLBinding.set_Classes_TStrings_LineBreak(self.pointer,v)
    LineBreak=property(getLineBreak,setLineBreak)
    def getStrictDelimiter(self):
        r=LCLBinding.get_Classes_TStrings_StrictDelimiter(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setStrictDelimiter(self,v):
        LCLBinding.set_Classes_TStrings_StrictDelimiter(self.pointer,v)
    StrictDelimiter=property(getStrictDelimiter,setStrictDelimiter)
    def getValueFromIndex(self,Index):
        r=LCLBinding.get_Classes_TStrings_ValueFromIndex(self.pointer,Index)
        return LCLBindingUtil.ConvertPascalstring(r)
    def setValueFromIndex(self,Index,v):
        LCLBinding.set_Classes_TStrings_ValueFromIndex(self.pointer,Index,v)
    def getCapacity(self):
        r=LCLBinding.get_Classes_TStrings_Capacity(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setCapacity(self,v):
        LCLBinding.set_Classes_TStrings_Capacity(self.pointer,v)
    Capacity=property(getCapacity,setCapacity)
    def getCommaText(self):
        r=LCLBinding.get_Classes_TStrings_CommaText(self.pointer)
        return LCLBindingUtil.ConvertPascalstring(r)
    def setCommaText(self,v):
        LCLBinding.set_Classes_TStrings_CommaText(self.pointer,v)
    CommaText=property(getCommaText,setCommaText)
    def getCount(self):
        r=LCLBinding.get_Classes_TStrings_Count(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    Count=property(getCount)
    def getNames(self,Index):
        r=LCLBinding.get_Classes_TStrings_Names(self.pointer,Index)
        return LCLBindingUtil.ConvertPascalstring(r)
    def getObjects(self,Index):
        r=LCLBinding.get_Classes_TStrings_Objects(self.pointer,Index)
        return LCLBindingUtil.GetPytonObject(r,TObject)
    def setObjects(self,Index,v):
        LCLBinding.set_Classes_TStrings_Objects(self.pointer,Index,v.pointer)
    def getStrings(self,Index):
        r=LCLBinding.get_Classes_TStrings_Strings(self.pointer,Index)
        return LCLBindingUtil.ConvertPascalstring(r)
    def setStrings(self,Index,v):
        LCLBinding.set_Classes_TStrings_Strings(self.pointer,Index,v)
    def getText(self):
        r=LCLBinding.get_Classes_TStrings_Text(self.pointer)
        return LCLBindingUtil.ConvertPascalstring(r)
    def setText(self,v):
        LCLBinding.set_Classes_TStrings_Text(self.pointer,v)
    Text=property(getText,setText)
    def getStringsAdapter(self):
        r=LCLBinding.get_Classes_TStrings_StringsAdapter(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,IStringsAdapter)
    def setStringsAdapter(self,v):
        LCLBinding.set_Classes_TStrings_StringsAdapter(self.pointer,v.pointer)
    StringsAdapter=property(getStringsAdapter,setStringsAdapter)
    def getSkipLastLineBreak(self):
        r=LCLBinding.get_Classes_TStrings_SkipLastLineBreak(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setSkipLastLineBreak(self,v):
        LCLBinding.set_Classes_TStrings_SkipLastLineBreak(self.pointer,v)
    SkipLastLineBreak=property(getSkipLastLineBreak,setSkipLastLineBreak)
#class TStrings end
#class TOwnedCollection start
class TOwnedCollection(TCollection):
#    pointer=c_void_p()
    def __init__(self):#TOwnedCollection
        TCollection.__init__(self)
#class TOwnedCollection end
#class IStringsAdapter start
class IStringsAdapter(TObject):
#    pointer=c_void_p()
    def __init__(self):#IStringsAdapter
        TObject.__init__(self)
#class IStringsAdapter end
#class TStringList start
class TStringList(TStrings):
#    pointer=c_void_p()
    def __init__(self):#TStringList
        TStrings.__init__(self)
    def getSorted(self):
        r=LCLBinding.get_Classes_TStringList_Sorted(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setSorted(self,v):
        LCLBinding.set_Classes_TStringList_Sorted(self.pointer,v)
    Sorted=property(getSorted,setSorted)
    def getCaseSensitive(self):
        r=LCLBinding.get_Classes_TStringList_CaseSensitive(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setCaseSensitive(self,v):
        LCLBinding.set_Classes_TStringList_CaseSensitive(self.pointer,v)
    CaseSensitive=property(getCaseSensitive,setCaseSensitive)
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
        self.OnChangePasObject=LCLBinding.set_Classes_TStringList_OnChange(self.pointer,self.PasOnChange,oldobj,FreeOldEvent)
    def getOnChange(self):
        return OnChangecall
    OnChange=property(getOnChange,setOnChange)
    def _Warper_OnChanging(self,Sender):
        self.OnChangingcall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnChanging(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnChangingcall'):
            FreeOldEvent=1
            oldobj=OnChangingPasObject
        self.OnChangingcall=v 
        self.PasOnChanging=FunctionForm(self._Warper_OnChanging)
        self.OnChangingPasObject=LCLBinding.set_Classes_TStringList_OnChanging(self.pointer,self.PasOnChanging,oldobj,FreeOldEvent)
    def getOnChanging(self):
        return OnChangingcall
    OnChanging=property(getOnChanging,setOnChanging)
    def getOwnsObjects(self):
        r=LCLBinding.get_Classes_TStringList_OwnsObjects(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setOwnsObjects(self,v):
        LCLBinding.set_Classes_TStringList_OwnsObjects(self.pointer,v)
    OwnsObjects=property(getOwnsObjects,setOwnsObjects)
    def getSortStyle(self):
        r=LCLBinding.get_Classes_TStringList_SortStyle(self.pointer)
        return r
    def setSortStyle(self,v):
        LCLBinding.set_Classes_TStringList_SortStyle(self.pointer,v.pointer)
    SortStyle=property(getSortStyle,setSortStyle)
#class TStringList end
#class TComponent start
class TComponent(TPersistent):
#    pointer=c_void_p()
    def __init__(self):#TComponent
        TPersistent.__init__(self)
    def getComponents(self,Index):
        r=LCLBinding.get_Classes_TComponent_Components(self.pointer,Index)
        return LCLBindingUtil.GetPytonObject(r,TComponent)
    def getComponentCount(self):
        r=LCLBinding.get_Classes_TComponent_ComponentCount(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    ComponentCount=property(getComponentCount)
    def getComponentIndex(self):
        r=LCLBinding.get_Classes_TComponent_ComponentIndex(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setComponentIndex(self,v):
        LCLBinding.set_Classes_TComponent_ComponentIndex(self.pointer,v)
    ComponentIndex=property(getComponentIndex,setComponentIndex)
    def getComponentState(self):
        r=LCLBinding.get_Classes_TComponent_ComponentState(self.pointer)
        return r
    ComponentState=property(getComponentState)
    def getComponentStyle(self):
        r=LCLBinding.get_Classes_TComponent_ComponentStyle(self.pointer)
        return r
    ComponentStyle=property(getComponentStyle)
    def getOwner(self):
        r=LCLBinding.get_Classes_TComponent_Owner(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TComponent)
    Owner=property(getOwner)
#class TComponent end
#class TBasicActionLink start
class TBasicActionLink(TObject):
#    pointer=c_void_p()
    def __init__(self):#TBasicActionLink
        TObject.__init__(self)
#constructorClasses_TBasicActionLink_Create
    @staticmethod
    def Create(AClient):
        return LCLBindingUtil.GetPytonObject(LCLBinding.Classes_TBasicActionLink_Create((AClient.pointer)),TBasicActionLink)
    def getAction(self):
        r=LCLBinding.get_Classes_TBasicActionLink_Action(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TBasicAction)
    def setAction(self,v):
        LCLBinding.set_Classes_TBasicActionLink_Action(self.pointer,v.pointer)
    Action=property(getAction,setAction)
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
        self.OnChangePasObject=LCLBinding.set_Classes_TBasicActionLink_OnChange(self.pointer,self.PasOnChange,oldobj,FreeOldEvent)
    def getOnChange(self):
        return OnChangecall
    OnChange=property(getOnChange,setOnChange)
#class TBasicActionLink end
#class TCollectionItem start
class TCollectionItem(TPersistent):
#    pointer=c_void_p()
    def __init__(self):#TCollectionItem
        TPersistent.__init__(self)
    def getCollection(self):
        r=LCLBinding.get_Classes_TCollectionItem_Collection(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TCollection)
    def setCollection(self,v):
        LCLBinding.set_Classes_TCollectionItem_Collection(self.pointer,v.pointer)
    Collection=property(getCollection,setCollection)
    def getID(self):
        r=LCLBinding.get_Classes_TCollectionItem_ID(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    ID=property(getID)
    def getIndex(self):
        r=LCLBinding.get_Classes_TCollectionItem_Index(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setIndex(self,v):
        LCLBinding.set_Classes_TCollectionItem_Index(self.pointer,v)
    Index=property(getIndex,setIndex)
    def getDisplayName(self):
        r=LCLBinding.get_Classes_TCollectionItem_DisplayName(self.pointer)
        return LCLBindingUtil.ConvertPascalstring(r)
    def setDisplayName(self,v):
        LCLBinding.set_Classes_TCollectionItem_DisplayName(self.pointer,v)
    DisplayName=property(getDisplayName,setDisplayName)
#class TCollectionItem end
#class TBasicAction start
class TBasicAction(TComponent):
#    pointer=c_void_p()
    def __init__(self):#TBasicAction
        TComponent.__init__(self)
#constructorClasses_TBasicAction_Create
    @staticmethod
    def Create(AOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.Classes_TBasicAction_Create((AOwner.pointer)),TBasicAction)
    def getActionComponent(self):
        r=LCLBinding.get_Classes_TBasicAction_ActionComponent(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TComponent)
    def setActionComponent(self,v):
        LCLBinding.set_Classes_TBasicAction_ActionComponent(self.pointer,v.pointer)
    ActionComponent=property(getActionComponent,setActionComponent)
    def _Warper_OnExecute(self,Sender):
        self.OnExecutecall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnExecute(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnExecutecall'):
            FreeOldEvent=1
            oldobj=OnExecutePasObject
        self.OnExecutecall=v 
        self.PasOnExecute=FunctionForm(self._Warper_OnExecute)
        self.OnExecutePasObject=LCLBinding.set_Classes_TBasicAction_OnExecute(self.pointer,self.PasOnExecute,oldobj,FreeOldEvent)
    def getOnExecute(self):
        return OnExecutecall
    OnExecute=property(getOnExecute,setOnExecute)
    def _Warper_OnUpdate(self,Sender):
        self.OnUpdatecall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnUpdate(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnUpdatecall'):
            FreeOldEvent=1
            oldobj=OnUpdatePasObject
        self.OnUpdatecall=v 
        self.PasOnUpdate=FunctionForm(self._Warper_OnUpdate)
        self.OnUpdatePasObject=LCLBinding.set_Classes_TBasicAction_OnUpdate(self.pointer,self.PasOnUpdate,oldobj,FreeOldEvent)
    def getOnUpdate(self):
        return OnUpdatecall
    OnUpdate=property(getOnUpdate,setOnUpdate)
#class TBasicAction end
