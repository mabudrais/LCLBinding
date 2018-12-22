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
def CreateTFilerFlagsFromInt(i):
    dic={1:"ffInherited",2:"ffChildPos",4:"ffInline"}
    return CreateSetFormint(i,dic)
#class TPersistent start
class TPersistent(TObject):
#    pointer=c_void_p()
    def __init__(self):#TPersistent
        TObject.__init__(self)
#Procedure Classes_TPersistent_Assign
    @staticmethod
    def Assign(self,Source):
        LCLBinding.Classes_TPersistent_Assign((Source.pointer))
#Procedure Classes_TPersistent_FPOAttachObserver
    @staticmethod
    def FPOAttachObserver(self,AObserver):
        LCLBinding.Classes_TPersistent_FPOAttachObserver((AObserver.pointer))
#Procedure Classes_TPersistent_FPODetachObserver
    @staticmethod
    def FPODetachObserver(self,AObserver):
        LCLBinding.Classes_TPersistent_FPODetachObserver((AObserver.pointer))
#class TPersistent end
#class TCollection start
class TCollection(TPersistent):
#    pointer=c_void_p()
    def __init__(self):#TCollection
        TPersistent.__init__(self)
#Procedure Classes_TCollection_Assign
    @staticmethod
    def Assign(self,Source):
        LCLBinding.Classes_TCollection_Assign((Source.pointer))
#Procedure Classes_TCollection_BeginUpdate
    @staticmethod
    def BeginUpdate(self,):
        LCLBinding.Classes_TCollection_BeginUpdate()
#Procedure Classes_TCollection_Clear
    @staticmethod
    def Clear(self,):
        LCLBinding.Classes_TCollection_Clear()
#Procedure Classes_TCollection_EndUpdate
    @staticmethod
    def EndUpdate(self,):
        LCLBinding.Classes_TCollection_EndUpdate()
#Procedure Classes_TCollection_Delete
    @staticmethod
    def Delete(self,Index):
        LCLBinding.Classes_TCollection_Delete((Index))
#Procedure Classes_TCollection_Exchange
    @staticmethod
    def Exchange(self,Index1,index2):
        LCLBinding.Classes_TCollection_Exchange((Index1),(index2))
#Procedure Classes_TCollection_Sort
    @staticmethod
    def Sort(self,Compare):
        LCLBinding.Classes_TCollection_Sort((Compare.pointer))
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
#class TFPList start
class TFPList(TObject):
#    pointer=c_void_p()
    def __init__(self):#TFPList
        TObject.__init__(self)
#Procedure Classes_TFPList_AddList
    @staticmethod
    def AddList(self,AList):
        LCLBinding.Classes_TFPList_AddList((AList.pointer))
#Procedure Classes_TFPList_Clear
    @staticmethod
    def Clear(self,):
        LCLBinding.Classes_TFPList_Clear()
#Procedure Classes_TFPList_Delete
    @staticmethod
    def Delete(self,Index):
        LCLBinding.Classes_TFPList_Delete((Index))
#Procedure Classes_TFPList_Exchange
    @staticmethod
    def Exchange(self,Index1,Index2):
        LCLBinding.Classes_TFPList_Exchange((Index1),(Index2))
#Procedure Classes_TFPList_Move
    @staticmethod
    def Move(self,CurIndex,NewIndex):
        LCLBinding.Classes_TFPList_Move((CurIndex),(NewIndex))
#Procedure Classes_TFPList_Assign
    @staticmethod
    def Assign(self,ListA,AOperator,ListB):
        LCLBinding.Classes_TFPList_Assign((ListA.pointer),(AOperator.pointer),(ListB.pointer))
#Procedure Classes_TFPList_Pack
    @staticmethod
    def Pack(self,):
        LCLBinding.Classes_TFPList_Pack()
    def getCapacity(self):
        r=LCLBinding.get_Classes_TFPList_Capacity(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setCapacity(self,v):
        LCLBinding.set_Classes_TFPList_Capacity(self.pointer,v)
    Capacity=property(getCapacity,setCapacity)
    def getCount(self):
        r=LCLBinding.get_Classes_TFPList_Count(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setCount(self,v):
        LCLBinding.set_Classes_TFPList_Count(self.pointer,v)
    Count=property(getCount,setCount)
#class TFPList end
#class IStringsAdapter start
class IStringsAdapter(TObject):
#    pointer=c_void_p()
    def __init__(self):#IStringsAdapter
        TObject.__init__(self)
#class IStringsAdapter end
#class TStrings start
class TStrings(TPersistent):
#    pointer=c_void_p()
    def __init__(self):#TStrings
        TPersistent.__init__(self)
#Procedure Classes_TStrings_Append
    @staticmethod
    def Append(self,S):
        LCLBinding.Classes_TStrings_Append((S))
#Procedure Classes_TStrings_AddText
    @staticmethod
    def AddText(self,S):
        LCLBinding.Classes_TStrings_AddText((S))
#Procedure Classes_TStrings_Assign
    @staticmethod
    def Assign(self,Source):
        LCLBinding.Classes_TStrings_Assign((Source.pointer))
#Procedure Classes_TStrings_BeginUpdate
    @staticmethod
    def BeginUpdate(self,):
        LCLBinding.Classes_TStrings_BeginUpdate()
#Procedure Classes_TStrings_Clear
    @staticmethod
    def Clear(self,):
        LCLBinding.Classes_TStrings_Clear()
#Procedure Classes_TStrings_Delete
    @staticmethod
    def Delete(self,Index):
        LCLBinding.Classes_TStrings_Delete((Index))
#Procedure Classes_TStrings_EndUpdate
    @staticmethod
    def EndUpdate(self,):
        LCLBinding.Classes_TStrings_EndUpdate()
#Procedure Classes_TStrings_Exchange
    @staticmethod
    def Exchange(self,Index1,Index2):
        LCLBinding.Classes_TStrings_Exchange((Index1),(Index2))
#Procedure Classes_TStrings_Insert
    @staticmethod
    def Insert(self,Index,S):
        LCLBinding.Classes_TStrings_Insert((Index),(S))
#Procedure Classes_TStrings_InsertObject
    @staticmethod
    def InsertObject(self,Index,S,AObject):
        LCLBinding.Classes_TStrings_InsertObject((Index),(S),(AObject.pointer))
#Procedure Classes_TStrings_LoadFromFile
    @staticmethod
    def LoadFromFile(self,FileName):
        LCLBinding.Classes_TStrings_LoadFromFile((FileName))
#Procedure Classes_TStrings_LoadFromStream
    @staticmethod
    def LoadFromStream(self,Stream):
        LCLBinding.Classes_TStrings_LoadFromStream((Stream.pointer))
#Procedure Classes_TStrings_Move
    @staticmethod
    def Move(self,CurIndex,NewIndex):
        LCLBinding.Classes_TStrings_Move((CurIndex),(NewIndex))
#Procedure Classes_TStrings_SaveToFile
    @staticmethod
    def SaveToFile(self,FileName):
        LCLBinding.Classes_TStrings_SaveToFile((FileName))
#Procedure Classes_TStrings_SaveToStream
    @staticmethod
    def SaveToStream(self,Stream):
        LCLBinding.Classes_TStrings_SaveToStream((Stream.pointer))
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
#class TComponent start
class TComponent(TPersistent):
#    pointer=c_void_p()
    def __init__(self):#TComponent
        TPersistent.__init__(self)
#Procedure Classes_TComponent_WriteState
    @staticmethod
    def WriteState(self,Writer):
        LCLBinding.Classes_TComponent_WriteState((Writer.pointer))
#constructorClasses_TComponent_Create
    @staticmethod
    def Create(AOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.Classes_TComponent_Create((AOwner.pointer)),TComponent)
#Procedure Classes_TComponent_BeforeDestruction
    @staticmethod
    def BeforeDestruction(self,):
        LCLBinding.Classes_TComponent_BeforeDestruction()
#Procedure Classes_TComponent_DestroyComponents
    @staticmethod
    def DestroyComponents(self,):
        LCLBinding.Classes_TComponent_DestroyComponents()
#Procedure Classes_TComponent_Destroying
    @staticmethod
    def Destroying(self,):
        LCLBinding.Classes_TComponent_Destroying()
#Procedure Classes_TComponent_FreeNotification
    @staticmethod
    def FreeNotification(self,AComponent):
        LCLBinding.Classes_TComponent_FreeNotification((AComponent.pointer))
#Procedure Classes_TComponent_RemoveFreeNotification
    @staticmethod
    def RemoveFreeNotification(self,AComponent):
        LCLBinding.Classes_TComponent_RemoveFreeNotification((AComponent.pointer))
#Procedure Classes_TComponent_FreeOnRelease
    @staticmethod
    def FreeOnRelease(self,):
        LCLBinding.Classes_TComponent_FreeOnRelease()
#Procedure Classes_TComponent_InsertComponent
    @staticmethod
    def InsertComponent(self,AComponent):
        LCLBinding.Classes_TComponent_InsertComponent((AComponent.pointer))
#Procedure Classes_TComponent_RemoveComponent
    @staticmethod
    def RemoveComponent(self,AComponent):
        LCLBinding.Classes_TComponent_RemoveComponent((AComponent.pointer))
#Procedure Classes_TComponent_SetSubComponent
    @staticmethod
    def SetSubComponent(self,ASubComponent):
        LCLBinding.Classes_TComponent_SetSubComponent((booleantoint(ASubComponent)))
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
#class TAbstractObjectWriter start
class TAbstractObjectWriter(TObject):
#    pointer=c_void_p()
    def __init__(self):#TAbstractObjectWriter
        TObject.__init__(self)
#Procedure Classes_TAbstractObjectWriter_BeginCollection
    @staticmethod
    def BeginCollection(self,):
        LCLBinding.Classes_TAbstractObjectWriter_BeginCollection()
#Procedure Classes_TAbstractObjectWriter_BeginComponent
    @staticmethod
    def BeginComponent(self,Component,Flags,ChildPos):
        LCLBinding.Classes_TAbstractObjectWriter_BeginComponent((Component.pointer),(Flags.pointer),(ChildPos))
#Procedure Classes_TAbstractObjectWriter_WriteSignature
    @staticmethod
    def WriteSignature(self,):
        LCLBinding.Classes_TAbstractObjectWriter_WriteSignature()
#Procedure Classes_TAbstractObjectWriter_BeginList
    @staticmethod
    def BeginList(self,):
        LCLBinding.Classes_TAbstractObjectWriter_BeginList()
#Procedure Classes_TAbstractObjectWriter_EndList
    @staticmethod
    def EndList(self,):
        LCLBinding.Classes_TAbstractObjectWriter_EndList()
#Procedure Classes_TAbstractObjectWriter_BeginProperty
    @staticmethod
    def BeginProperty(self,PropName):
        LCLBinding.Classes_TAbstractObjectWriter_BeginProperty((PropName))
#Procedure Classes_TAbstractObjectWriter_EndProperty
    @staticmethod
    def EndProperty(self,):
        LCLBinding.Classes_TAbstractObjectWriter_EndProperty()
#Procedure Classes_TAbstractObjectWriter_WriteBoolean
    @staticmethod
    def WriteBoolean(self,Value):
        LCLBinding.Classes_TAbstractObjectWriter_WriteBoolean((booleantoint(Value)))
#Procedure Classes_TAbstractObjectWriter_WriteIdent
    @staticmethod
    def WriteIdent(self,Ident):
        LCLBinding.Classes_TAbstractObjectWriter_WriteIdent((Ident))
#Procedure Classes_TAbstractObjectWriter_WriteMethodName
    @staticmethod
    def WriteMethodName(self,Name):
        LCLBinding.Classes_TAbstractObjectWriter_WriteMethodName((Name))
#Procedure Classes_TAbstractObjectWriter_WriteString
    @staticmethod
    def WriteString(self,Value):
        LCLBinding.Classes_TAbstractObjectWriter_WriteString((Value))
#class TAbstractObjectWriter end
#class TStream start
class TStream(TObject):
#    pointer=c_void_p()
    def __init__(self):#TStream
        TObject.__init__(self)
#Procedure Classes_TStream_WriteComponent
    @staticmethod
    def WriteComponent(self,Instance):
        LCLBinding.Classes_TStream_WriteComponent((Instance.pointer))
#Procedure Classes_TStream_WriteComponentRes
    @staticmethod
    def WriteComponentRes(self,ResName,Instance):
        LCLBinding.Classes_TStream_WriteComponentRes((ResName),(Instance.pointer))
#Procedure Classes_TStream_WriteDescendent
    @staticmethod
    def WriteDescendent(self,Instance,Ancestor):
        LCLBinding.Classes_TStream_WriteDescendent((Instance.pointer),(Ancestor.pointer))
#Procedure Classes_TStream_WriteDescendentRes
    @staticmethod
    def WriteDescendentRes(self,ResName,Instance,Ancestor):
        LCLBinding.Classes_TStream_WriteDescendentRes((ResName),(Instance.pointer),(Ancestor.pointer))
#Procedure Classes_TStream_ReadResHeader
    @staticmethod
    def ReadResHeader(self,):
        LCLBinding.Classes_TStream_ReadResHeader()
#Procedure Classes_TStream_WriteAnsiString
    @staticmethod
    def WriteAnsiString(self,S):
        LCLBinding.Classes_TStream_WriteAnsiString((S))
#class TStream end
#class TCustomMemoryStream start
class TCustomMemoryStream(TStream):
#    pointer=c_void_p()
    def __init__(self):#TCustomMemoryStream
        TStream.__init__(self)
#Procedure Classes_TCustomMemoryStream_SaveToStream
    @staticmethod
    def SaveToStream(self,Stream):
        LCLBinding.Classes_TCustomMemoryStream_SaveToStream((Stream.pointer))
#Procedure Classes_TCustomMemoryStream_SaveToFile
    @staticmethod
    def SaveToFile(self,FileName):
        LCLBinding.Classes_TCustomMemoryStream_SaveToFile((FileName))
#class TCustomMemoryStream end
#class TAbstractObjectReader start
class TAbstractObjectReader(TObject):
#    pointer=c_void_p()
    def __init__(self):#TAbstractObjectReader
        TObject.__init__(self)
#Procedure Classes_TAbstractObjectReader_BeginRootComponent
    @staticmethod
    def BeginRootComponent(self,):
        LCLBinding.Classes_TAbstractObjectReader_BeginRootComponent()
#Procedure Classes_TAbstractObjectReader_ReadBinary
    @staticmethod
    def ReadBinary(self,DestData):
        LCLBinding.Classes_TAbstractObjectReader_ReadBinary((DestData.pointer))
#Procedure Classes_TAbstractObjectReader_ReadSignature
    @staticmethod
    def ReadSignature(self,):
        LCLBinding.Classes_TAbstractObjectReader_ReadSignature()
#Procedure Classes_TAbstractObjectReader_SkipComponent
    @staticmethod
    def SkipComponent(self,SkipComponentInfos):
        LCLBinding.Classes_TAbstractObjectReader_SkipComponent((booleantoint(SkipComponentInfos)))
#Procedure Classes_TAbstractObjectReader_SkipValue
    @staticmethod
    def SkipValue(self,):
        LCLBinding.Classes_TAbstractObjectReader_SkipValue()
#class TAbstractObjectReader end
#class TStringList start
class TStringList(TStrings):
#    pointer=c_void_p()
    def __init__(self):#TStringList
        TStrings.__init__(self)
#Procedure Classes_TStringList_Clear
    @staticmethod
    def Clear(self,):
        LCLBinding.Classes_TStringList_Clear()
#Procedure Classes_TStringList_Delete
    @staticmethod
    def Delete(self,Index):
        LCLBinding.Classes_TStringList_Delete((Index))
#Procedure Classes_TStringList_Exchange
    @staticmethod
    def Exchange(self,Index1,Index2):
        LCLBinding.Classes_TStringList_Exchange((Index1),(Index2))
#Procedure Classes_TStringList_Insert
    @staticmethod
    def Insert(self,Index,S):
        LCLBinding.Classes_TStringList_Insert((Index),(S))
#Procedure Classes_TStringList_Sort
    @staticmethod
    def Sort(self,):
        LCLBinding.Classes_TStringList_Sort()
#Procedure Classes_TStringList_CustomSort
    @staticmethod
    def CustomSort(self,CompareFn):
        LCLBinding.Classes_TStringList_CustomSort((CompareFn.pointer))
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
#class TOwnedCollection start
class TOwnedCollection(TCollection):
#    pointer=c_void_p()
    def __init__(self):#TOwnedCollection
        TCollection.__init__(self)
#class TOwnedCollection end
#class TMemoryStream start
class TMemoryStream(TCustomMemoryStream):
#    pointer=c_void_p()
    def __init__(self):#TMemoryStream
        TCustomMemoryStream.__init__(self)
#Procedure Classes_TMemoryStream_Clear
    @staticmethod
    def Clear(self,):
        LCLBinding.Classes_TMemoryStream_Clear()
#Procedure Classes_TMemoryStream_LoadFromStream
    @staticmethod
    def LoadFromStream(self,Stream):
        LCLBinding.Classes_TMemoryStream_LoadFromStream((Stream.pointer))
#Procedure Classes_TMemoryStream_LoadFromFile
    @staticmethod
    def LoadFromFile(self,FileName):
        LCLBinding.Classes_TMemoryStream_LoadFromFile((FileName))
#class TMemoryStream end
#class TReader start
class TReader(TObject):
#    pointer=c_void_p()
    def __init__(self):#TReader
        TObject.__init__(self)
#constructorClasses_TReader_Create
    @staticmethod
    def Create(Stream,BufSize):
        return LCLBindingUtil.GetPytonObject(LCLBinding.Classes_TReader_Create((Stream.pointer),(BufSize)),TReader)
#Procedure Classes_TReader_BeginReferences
    @staticmethod
    def BeginReferences(self,):
        LCLBinding.Classes_TReader_BeginReferences()
#Procedure Classes_TReader_CheckValue
    @staticmethod
    def CheckValue(self,Value):
        LCLBinding.Classes_TReader_CheckValue((Value.pointer))
#Procedure Classes_TReader_DefineProperty
    @staticmethod
    def DefineProperty(self,Name,AReadData,WriteData,HasData):
        LCLBinding.Classes_TReader_DefineProperty((Name),(AReadData.pointer),(WriteData.pointer),(booleantoint(HasData)))
#Procedure Classes_TReader_DefineBinaryProperty
    @staticmethod
    def DefineBinaryProperty(self,Name,AReadData,WriteData,HasData):
        LCLBinding.Classes_TReader_DefineBinaryProperty((Name),(AReadData.pointer),(WriteData.pointer),(booleantoint(HasData)))
#Procedure Classes_TReader_EndReferences
    @staticmethod
    def EndReferences(self,):
        LCLBinding.Classes_TReader_EndReferences()
#Procedure Classes_TReader_FixupReferences
    @staticmethod
    def FixupReferences(self,):
        LCLBinding.Classes_TReader_FixupReferences()
#Procedure Classes_TReader_ReadCollection
    @staticmethod
    def ReadCollection(self,Collection):
        LCLBinding.Classes_TReader_ReadCollection((Collection.pointer))
#Procedure Classes_TReader_ReadComponents
    @staticmethod
    def ReadComponents(self,AOwner,AParent,Proc):
        LCLBinding.Classes_TReader_ReadComponents((AOwner.pointer),(AParent.pointer),(Proc.pointer))
#Procedure Classes_TReader_ReadListBegin
    @staticmethod
    def ReadListBegin(self,):
        LCLBinding.Classes_TReader_ReadListBegin()
#Procedure Classes_TReader_ReadListEnd
    @staticmethod
    def ReadListEnd(self,):
        LCLBinding.Classes_TReader_ReadListEnd()
#Procedure Classes_TReader_ReadSignature
    @staticmethod
    def ReadSignature(self,):
        LCLBinding.Classes_TReader_ReadSignature()
#Procedure Classes_TReader_CopyValue
    @staticmethod
    def CopyValue(self,Writer):
        LCLBinding.Classes_TReader_CopyValue((Writer.pointer))
    def getDriver(self):
        r=LCLBinding.get_Classes_TReader_Driver(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TAbstractObjectReader)
    Driver=property(getDriver)
    def getOwner(self):
        r=LCLBinding.get_Classes_TReader_Owner(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TComponent)
    def setOwner(self,v):
        LCLBinding.set_Classes_TReader_Owner(self.pointer,v.pointer)
    Owner=property(getOwner,setOwner)
    def getParent(self):
        r=LCLBinding.get_Classes_TReader_Parent(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TComponent)
    def setParent(self,v):
        LCLBinding.set_Classes_TReader_Parent(self.pointer,v.pointer)
    Parent=property(getParent,setParent)
    def _Warper_OnError(self,Reader,Message,Handled):
        self.OnErrorcall(LCLBindingUtil.GetPytonObject(Reader,TReader),Message,LCLBindingUtil.IntToBoolean(Handled))
    def setOnError(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_char_p,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnErrorcall'):
            FreeOldEvent=1
            oldobj=OnErrorPasObject
        self.OnErrorcall=v 
        self.PasOnError=FunctionForm(self._Warper_OnError)
        self.OnErrorPasObject=LCLBinding.set_Classes_TReader_OnError(self.pointer,self.PasOnError,oldobj,FreeOldEvent)
    def getOnError(self):
        return OnErrorcall
    OnError=property(getOnError,setOnError)
    def _Warper_OnPropertyNotFound(self,Reader,Instance,PropName,IsPath,Handled,Skip):
        self.OnPropertyNotFoundcall(LCLBindingUtil.GetPytonObject(Reader,TReader),LCLBindingUtil.GetPytonObject(Instance,TPersistent),PropName,LCLBindingUtil.IntToBoolean(IsPath),LCLBindingUtil.IntToBoolean(Handled),LCLBindingUtil.IntToBoolean(Skip))
    def setOnPropertyNotFound(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p,c_char_p,c_int,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnPropertyNotFoundcall'):
            FreeOldEvent=1
            oldobj=OnPropertyNotFoundPasObject
        self.OnPropertyNotFoundcall=v 
        self.PasOnPropertyNotFound=FunctionForm(self._Warper_OnPropertyNotFound)
        self.OnPropertyNotFoundPasObject=LCLBinding.set_Classes_TReader_OnPropertyNotFound(self.pointer,self.PasOnPropertyNotFound,oldobj,FreeOldEvent)
    def getOnPropertyNotFound(self):
        return OnPropertyNotFoundcall
    OnPropertyNotFound=property(getOnPropertyNotFound,setOnPropertyNotFound)
    def _Warper_OnSetName(self,Reader,Component,Name):
        self.OnSetNamecall(LCLBindingUtil.GetPytonObject(Reader,TReader),LCLBindingUtil.GetPytonObject(Component,TComponent),Name)
    def setOnSetName(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p,c_char_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnSetNamecall'):
            FreeOldEvent=1
            oldobj=OnSetNamePasObject
        self.OnSetNamecall=v 
        self.PasOnSetName=FunctionForm(self._Warper_OnSetName)
        self.OnSetNamePasObject=LCLBinding.set_Classes_TReader_OnSetName(self.pointer,self.PasOnSetName,oldobj,FreeOldEvent)
    def getOnSetName(self):
        return OnSetNamecall
    OnSetName=property(getOnSetName,setOnSetName)
    def _Warper_OnReferenceName(self,Reader,Name):
        self.OnReferenceNamecall(LCLBindingUtil.GetPytonObject(Reader,TReader),Name)
    def setOnReferenceName(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_char_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnReferenceNamecall'):
            FreeOldEvent=1
            oldobj=OnReferenceNamePasObject
        self.OnReferenceNamecall=v 
        self.PasOnReferenceName=FunctionForm(self._Warper_OnReferenceName)
        self.OnReferenceNamePasObject=LCLBinding.set_Classes_TReader_OnReferenceName(self.pointer,self.PasOnReferenceName,oldobj,FreeOldEvent)
    def getOnReferenceName(self):
        return OnReferenceNamecall
    OnReferenceName=property(getOnReferenceName,setOnReferenceName)
#class TReader end
#class TFiler start
class TFiler(TObject):
#    pointer=c_void_p()
    def __init__(self):#TFiler
        TObject.__init__(self)
#Procedure Classes_TFiler_DefineProperty
    @staticmethod
    def DefineProperty(self,Name,ReadData,WriteData,HasData):
        LCLBinding.Classes_TFiler_DefineProperty((Name),(ReadData.pointer),(WriteData.pointer),(booleantoint(HasData)))
#Procedure Classes_TFiler_DefineBinaryProperty
    @staticmethod
    def DefineBinaryProperty(self,Name,ReadData,WriteData,HasData):
        LCLBinding.Classes_TFiler_DefineBinaryProperty((Name),(ReadData.pointer),(WriteData.pointer),(booleantoint(HasData)))
    def getRoot(self):
        r=LCLBinding.get_Classes_TFiler_Root(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TComponent)
    def setRoot(self,v):
        LCLBinding.set_Classes_TFiler_Root(self.pointer,v.pointer)
    Root=property(getRoot,setRoot)
    def getLookupRoot(self):
        r=LCLBinding.get_Classes_TFiler_LookupRoot(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TComponent)
    LookupRoot=property(getLookupRoot)
    def getAncestor(self):
        r=LCLBinding.get_Classes_TFiler_Ancestor(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TPersistent)
    def setAncestor(self,v):
        LCLBinding.set_Classes_TFiler_Ancestor(self.pointer,v.pointer)
    Ancestor=property(getAncestor,setAncestor)
    def getIgnoreChildren(self):
        r=LCLBinding.get_Classes_TFiler_IgnoreChildren(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setIgnoreChildren(self,v):
        LCLBinding.set_Classes_TFiler_IgnoreChildren(self.pointer,v)
    IgnoreChildren=property(getIgnoreChildren,setIgnoreChildren)
#class TFiler end
#class TWriter start
class TWriter(TFiler):
#    pointer=c_void_p()
    def __init__(self):#TWriter
        TFiler.__init__(self)
#Procedure Classes_TWriter_DefineProperty
    @staticmethod
    def DefineProperty(self,Name,ReadData,AWriteData,HasData):
        LCLBinding.Classes_TWriter_DefineProperty((Name),(ReadData.pointer),(AWriteData.pointer),(booleantoint(HasData)))
#Procedure Classes_TWriter_DefineBinaryProperty
    @staticmethod
    def DefineBinaryProperty(self,Name,ReadData,AWriteData,HasData):
        LCLBinding.Classes_TWriter_DefineBinaryProperty((Name),(ReadData.pointer),(AWriteData.pointer),(booleantoint(HasData)))
#Procedure Classes_TWriter_WriteBoolean
    @staticmethod
    def WriteBoolean(self,Value):
        LCLBinding.Classes_TWriter_WriteBoolean((booleantoint(Value)))
#Procedure Classes_TWriter_WriteCollection
    @staticmethod
    def WriteCollection(self,Value):
        LCLBinding.Classes_TWriter_WriteCollection((Value.pointer))
#Procedure Classes_TWriter_WriteComponent
    @staticmethod
    def WriteComponent(self,Component):
        LCLBinding.Classes_TWriter_WriteComponent((Component.pointer))
#Procedure Classes_TWriter_WriteDescendent
    @staticmethod
    def WriteDescendent(self,ARoot,AAncestor):
        LCLBinding.Classes_TWriter_WriteDescendent((ARoot.pointer),(AAncestor.pointer))
#Procedure Classes_TWriter_WriteIdent
    @staticmethod
    def WriteIdent(self,Ident):
        LCLBinding.Classes_TWriter_WriteIdent((Ident))
#Procedure Classes_TWriter_WriteListBegin
    @staticmethod
    def WriteListBegin(self,):
        LCLBinding.Classes_TWriter_WriteListBegin()
#Procedure Classes_TWriter_WriteListEnd
    @staticmethod
    def WriteListEnd(self,):
        LCLBinding.Classes_TWriter_WriteListEnd()
#Procedure Classes_TWriter_WriteSignature
    @staticmethod
    def WriteSignature(self,):
        LCLBinding.Classes_TWriter_WriteSignature()
#Procedure Classes_TWriter_WriteRootComponent
    @staticmethod
    def WriteRootComponent(self,ARoot):
        LCLBinding.Classes_TWriter_WriteRootComponent((ARoot.pointer))
#Procedure Classes_TWriter_WriteString
    @staticmethod
    def WriteString(self,Value):
        LCLBinding.Classes_TWriter_WriteString((Value))
    def getRootAncestor(self):
        r=LCLBinding.get_Classes_TWriter_RootAncestor(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TComponent)
    def setRootAncestor(self,v):
        LCLBinding.set_Classes_TWriter_RootAncestor(self.pointer,v.pointer)
    RootAncestor=property(getRootAncestor,setRootAncestor)
    def _Warper_OnFindAncestor(self,Writer,Component,Name,Ancestor,RootAncestor):
        self.OnFindAncestorcall(LCLBindingUtil.GetPytonObject(Writer,TWriter),LCLBindingUtil.GetPytonObject(Component,TComponent),Name,LCLBindingUtil.GetPytonObject(Ancestor,TComponent),LCLBindingUtil.GetPytonObject(RootAncestor,TComponent))
    def setOnFindAncestor(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_void_p,c_char_p,c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnFindAncestorcall'):
            FreeOldEvent=1
            oldobj=OnFindAncestorPasObject
        self.OnFindAncestorcall=v 
        self.PasOnFindAncestor=FunctionForm(self._Warper_OnFindAncestor)
        self.OnFindAncestorPasObject=LCLBinding.set_Classes_TWriter_OnFindAncestor(self.pointer,self.PasOnFindAncestor,oldobj,FreeOldEvent)
    def getOnFindAncestor(self):
        return OnFindAncestorcall
    OnFindAncestor=property(getOnFindAncestor,setOnFindAncestor)
    def getDriver(self):
        r=LCLBinding.get_Classes_TWriter_Driver(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TAbstractObjectWriter)
    Driver=property(getDriver)
    def getPropertyPath(self):
        r=LCLBinding.get_Classes_TWriter_PropertyPath(self.pointer)
        return LCLBindingUtil.ConvertPascalstring(r)
    PropertyPath=property(getPropertyPath)
#class TWriter end
#class TCollectionItem start
class TCollectionItem(TPersistent):
#    pointer=c_void_p()
    def __init__(self):#TCollectionItem
        TPersistent.__init__(self)
#constructorClasses_TCollectionItem_Create
    @staticmethod
    def Create(ACollection):
        return LCLBindingUtil.GetPytonObject(LCLBinding.Classes_TCollectionItem_Create((ACollection.pointer)),TCollectionItem)
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
#Procedure Classes_TBasicAction_UpdateTarget
    @staticmethod
    def UpdateTarget(self,Target):
        LCLBinding.Classes_TBasicAction_UpdateTarget((Target.pointer))
#Procedure Classes_TBasicAction_ExecuteTarget
    @staticmethod
    def ExecuteTarget(self,Target):
        LCLBinding.Classes_TBasicAction_ExecuteTarget((Target.pointer))
#Procedure Classes_TBasicAction_RegisterChanges
    @staticmethod
    def RegisterChanges(self,Value):
        LCLBinding.Classes_TBasicAction_RegisterChanges((Value.pointer))
#Procedure Classes_TBasicAction_UnRegisterChanges
    @staticmethod
    def UnRegisterChanges(self,Value):
        LCLBinding.Classes_TBasicAction_UnRegisterChanges((Value.pointer))
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
