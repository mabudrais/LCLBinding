from MainPasObject import *
#import end
#class TCustomCheckListBox start
class TCustomCheckListBox(TCustomListBox):
#    pointer=c_void_p()
    def __init__(self):#TCustomCheckListBox
        TCustomListBox.__init__(self)
#constructorCheckLst_TCustomCheckListBox_Create
    @staticmethod
    def Create(AOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.CheckLst_TCustomCheckListBox_Create((AOwner.pointer)),TCustomCheckListBox)
    def getAllowGrayed(self):
        r=LCLBinding.get_CheckLst_TCustomCheckListBox_AllowGrayed(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setAllowGrayed(self,v):
        LCLBinding.set_CheckLst_TCustomCheckListBox_AllowGrayed(self.pointer,v)
    AllowGrayed=property(getAllowGrayed,setAllowGrayed)
    def getChecked(self,AIndex):
        r=LCLBinding.get_CheckLst_TCustomCheckListBox_Checked(self.pointer,AIndex)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setChecked(self,AIndex,v):
        LCLBinding.set_CheckLst_TCustomCheckListBox_Checked(self.pointer,AIndex,v)
    def getHeader(self,AIndex):
        r=LCLBinding.get_CheckLst_TCustomCheckListBox_Header(self.pointer,AIndex)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setHeader(self,AIndex,v):
        LCLBinding.set_CheckLst_TCustomCheckListBox_Header(self.pointer,AIndex,v)
    def getItemEnabled(self,AIndex):
        r=LCLBinding.get_CheckLst_TCustomCheckListBox_ItemEnabled(self.pointer,AIndex)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setItemEnabled(self,AIndex,v):
        LCLBinding.set_CheckLst_TCustomCheckListBox_ItemEnabled(self.pointer,AIndex,v)
    def getState(self,AIndex):
        r=LCLBinding.get_CheckLst_TCustomCheckListBox_State(self.pointer,AIndex)
        return r
    def setState(self,AIndex,v):
        LCLBinding.set_CheckLst_TCustomCheckListBox_State(self.pointer,AIndex,v.pointer)
    def _Warper_OnClickCheck(self,Sender):
        self.OnClickCheckcall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnClickCheck(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnClickCheckcall'):
            FreeOldEvent=1
            oldobj=OnClickCheckPasObject
        self.OnClickCheckcall=v 
        self.PasOnClickCheck=FunctionForm(self._Warper_OnClickCheck)
        self.OnClickCheckPasObject=LCLBinding.set_CheckLst_TCustomCheckListBox_OnClickCheck(self.pointer,self.PasOnClickCheck,oldobj,FreeOldEvent)
    def getOnClickCheck(self):
        return OnClickCheckcall
    OnClickCheck=property(getOnClickCheck,setOnClickCheck)
    def _Warper_OnItemClick(self,Sender,Index):
        self.OnItemClickcall(LCLBindingUtil.GetPytonObject(Sender,TObject),Index)
    def setOnItemClick(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnItemClickcall'):
            FreeOldEvent=1
            oldobj=OnItemClickPasObject
        self.OnItemClickcall=v 
        self.PasOnItemClick=FunctionForm(self._Warper_OnItemClick)
        self.OnItemClickPasObject=LCLBinding.set_CheckLst_TCustomCheckListBox_OnItemClick(self.pointer,self.PasOnItemClick,oldobj,FreeOldEvent)
    def getOnItemClick(self):
        return OnItemClickcall
    OnItemClick=property(getOnItemClick,setOnItemClick)
#class TCustomCheckListBox end
#class TCheckListBox start
class TCheckListBox(TCustomCheckListBox):
#    pointer=c_void_p()
    def __init__(self):#TCheckListBox
        TCustomCheckListBox.__init__(self)
    def getDragMode(self):
        r=LCLBinding.get_CheckLst_TCheckListBox_DragMode(self.pointer)
        return r
    def setDragMode(self,v):
        LCLBinding.set_CheckLst_TCheckListBox_DragMode(self.pointer,v.pointer)
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
        self.OnDragDropPasObject=LCLBinding.set_CheckLst_TCheckListBox_OnDragDrop(self.pointer,self.PasOnDragDrop,oldobj,FreeOldEvent)
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
        self.OnDragOverPasObject=LCLBinding.set_CheckLst_TCheckListBox_OnDragOver(self.pointer,self.PasOnDragOver,oldobj,FreeOldEvent)
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
        self.OnEndDragPasObject=LCLBinding.set_CheckLst_TCheckListBox_OnEndDrag(self.pointer,self.PasOnEndDrag,oldobj,FreeOldEvent)
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
        self.OnStartDragPasObject=LCLBinding.set_CheckLst_TCheckListBox_OnStartDrag(self.pointer,self.PasOnStartDrag,oldobj,FreeOldEvent)
    def getOnStartDrag(self):
        return OnStartDragcall
    OnStartDrag=property(getOnStartDrag,setOnStartDrag)
#constructorCheckLst_TCheckListBox_Create
    @staticmethod
    def Create(AOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.CheckLst_TCheckListBox_Create((AOwner.pointer)),TCheckListBox)
#class TCheckListBox end
