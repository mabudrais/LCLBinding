from clipbrd import *
from Buttons import *
from MaskEdit import *
from StdCtrls import *
from Forms import *
from Graphics import *
from GraphType import *
from Controls import *
from Classes import *
from MainPasObject import *
#import end
def CreateTGridDrawStateFromInt(i):
    dic={1:"gdSelected",2:"gdFocused",4:"gdFixed",8:"gdHot",16:"gdPushed",32:"gdRowHighlight"}
    return CreateSetFormint(i,dic)
def CreateTSaveOptionsFromInt(i):
    dic={1:"soDesign",2:"soAttributes",4:"soContent",8:"soPosition"}
    return CreateSetFormint(i,dic)
def CreateTGridOptions2FromInt(i):
    dic={1:"goScrollToLastCol",2:"goScrollToLastRow"}
    return CreateSetFormint(i,dic)
def CreateTGridOptionsFromInt(i):
    dic={1:"goFixedVertLine",2:"goFixedHorzLine",4:"goVertLine",8:"goHorzLine",16:"goRangeSelect",32:"goDrawFocusSelected",64:"goRowSizing",128:"goColSizing",256:"goRowMoving",512:"goColMoving",1024:"goEditing",2048:"goAutoAddRows",4096:"goTabs",8192:"goRowSelect",16384:"goAlwaysShowEditor",32768:"goThumbTracking",65536:"goColSpanning",131072:"goRelaxedRowSelect",262144:"goDblClickAutoSize",524288:"goSmoothScroll",1048576:"goFixedRowNumbering",2097152:"goScrollKeepVisible",4194304:"goHeaderHotTracking",8388608:"goHeaderPushedLook",16777216:"goSelectionActive",33554432:"goFixedColSizing",67108864:"goDontScrollPartCell",134217728:"goCellHints",268435456:"goTruncCellHints",536870912:"goCellEllipsis",1073741824:"goAutoAddRowsSkipContentCheck",2147483648:"goRowHighlight"}
    return CreateSetFormint(i,dic)
def CreateTGridZoneSetFromInt(i):
    dic={1:"gzNormal",2:"gzFixedCols",4:"gzFixedRows",8:"gzFixedCells",16:"gzInvalid"}
    return CreateSetFormint(i,dic)
def CreateTGridFlagsFromInt(i):
    dic={1:"gfEditorUpdateLock",2:"gfNeedsSelectActive",4:"gfEditorTab",8:"gfRevEditorTab",16:"gfVisualChange",32:"gfColumnsLocked",64:"gfEditingDone",128:"gfSizingStarted",256:"gfPainting",512:"gfUpdatingSize",1024:"gfClientRectChange",2048:"gfAutoEditPending",4096:"gfUpdatingScrollbar"}
    return CreateSetFormint(i,dic)
#class TCustomGrid start
class TCustomGrid(TCustomControl):
#    pointer=c_void_p()
    def __init__(self):#TCustomGrid
        TCustomControl.__init__(self)
#constructorGrids_TCustomGrid_Create
    @staticmethod
    def Create(AOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.Grids_TCustomGrid_Create((AOwner.pointer)),TCustomGrid)
#Procedure Grids_TCustomGrid_Invalidate
    @staticmethod
    def Invalidate(self,):
        LCLBinding.Grids_TCustomGrid_Invalidate()
#Procedure Grids_TCustomGrid_EditingDone
    @staticmethod
    def EditingDone(self,):
        LCLBinding.Grids_TCustomGrid_EditingDone()
#Procedure Grids_TCustomGrid_AutoAdjustColumns
    @staticmethod
    def AutoAdjustColumns(self,):
        LCLBinding.Grids_TCustomGrid_AutoAdjustColumns()
#Procedure Grids_TCustomGrid_BeginUpdate
    @staticmethod
    def BeginUpdate(self,):
        LCLBinding.Grids_TCustomGrid_BeginUpdate()
#Procedure Grids_TCustomGrid_CheckPosition
    @staticmethod
    def CheckPosition(self,):
        LCLBinding.Grids_TCustomGrid_CheckPosition()
#Procedure Grids_TCustomGrid_Clear
    @staticmethod
    def Clear(self,):
        LCLBinding.Grids_TCustomGrid_Clear()
#Procedure Grids_TCustomGrid_ClearSelections
    @staticmethod
    def ClearSelections(self,):
        LCLBinding.Grids_TCustomGrid_ClearSelections()
#Procedure Grids_TCustomGrid_EndUpdate
    @staticmethod
    def EndUpdate(self,aRefresh):
        LCLBinding.Grids_TCustomGrid_EndUpdate((booleantoint(aRefresh)))
#Procedure Grids_TCustomGrid_InvalidateCol
    @staticmethod
    def InvalidateCol(self,ACol):
        LCLBinding.Grids_TCustomGrid_InvalidateCol((ACol))
#Procedure Grids_TCustomGrid_InvalidateRow
    @staticmethod
    def InvalidateRow(self,ARow):
        LCLBinding.Grids_TCustomGrid_InvalidateRow((ARow))
#Procedure Grids_TCustomGrid_LoadFromFile
    @staticmethod
    def LoadFromFile(self,FileName):
        LCLBinding.Grids_TCustomGrid_LoadFromFile((FileName))
#Procedure Grids_TCustomGrid_LoadFromStream
    @staticmethod
    def LoadFromStream(self,AStream):
        LCLBinding.Grids_TCustomGrid_LoadFromStream((AStream.pointer))
#Procedure Grids_TCustomGrid_SaveToFile
    @staticmethod
    def SaveToFile(self,FileName):
        LCLBinding.Grids_TCustomGrid_SaveToFile((FileName))
#Procedure Grids_TCustomGrid_SaveToStream
    @staticmethod
    def SaveToStream(self,AStream):
        LCLBinding.Grids_TCustomGrid_SaveToStream((AStream.pointer))
#Procedure Grids_TCustomGrid_SetFocus
    @staticmethod
    def SetFocus(self,):
        LCLBinding.Grids_TCustomGrid_SetFocus()
    def getSelectedRangeCount(self):
        r=LCLBinding.get_Grids_TCustomGrid_SelectedRangeCount(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    SelectedRangeCount=property(getSelectedRangeCount)
    def getSortOrder(self):
        r=LCLBinding.get_Grids_TCustomGrid_SortOrder(self.pointer)
        return r
    def setSortOrder(self,v):
        LCLBinding.set_Grids_TCustomGrid_SortOrder(self.pointer,v.pointer)
    SortOrder=property(getSortOrder,setSortOrder)
    def getSortColumn(self):
        r=LCLBinding.get_Grids_TCustomGrid_SortColumn(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    SortColumn=property(getSortColumn)
#class TCustomGrid end
#class TCustomDrawGrid start
class TCustomDrawGrid(TCustomGrid):
#    pointer=c_void_p()
    def __init__(self):#TCustomDrawGrid
        TCustomGrid.__init__(self)
#constructorGrids_TCustomDrawGrid_Create
    @staticmethod
    def Create(AOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.Grids_TCustomDrawGrid_Create((AOwner.pointer)),TCustomDrawGrid)
#Procedure Grids_TCustomDrawGrid_DeleteColRow
    @staticmethod
    def DeleteColRow(self,IsColumn,index):
        LCLBinding.Grids_TCustomDrawGrid_DeleteColRow((booleantoint(IsColumn)),(index))
#Procedure Grids_TCustomDrawGrid_DeleteCol
    @staticmethod
    def DeleteCol(self,Index):
        LCLBinding.Grids_TCustomDrawGrid_DeleteCol((Index))
#Procedure Grids_TCustomDrawGrid_DeleteRow
    @staticmethod
    def DeleteRow(self,Index):
        LCLBinding.Grids_TCustomDrawGrid_DeleteRow((Index))
#Procedure Grids_TCustomDrawGrid_ExchangeColRow
    @staticmethod
    def ExchangeColRow(self,IsColumn,index,WithIndex):
        LCLBinding.Grids_TCustomDrawGrid_ExchangeColRow((booleantoint(IsColumn)),(index),(WithIndex))
#Procedure Grids_TCustomDrawGrid_InsertColRow
    @staticmethod
    def InsertColRow(self,IsColumn,index):
        LCLBinding.Grids_TCustomDrawGrid_InsertColRow((booleantoint(IsColumn)),(index))
#Procedure Grids_TCustomDrawGrid_MoveColRow
    @staticmethod
    def MoveColRow(self,IsColumn,FromIndex,ToIndex):
        LCLBinding.Grids_TCustomDrawGrid_MoveColRow((booleantoint(IsColumn)),(FromIndex),(ToIndex))
    def getAllowOutboundEvents(self):
        r=LCLBinding.get_Grids_TCustomDrawGrid_AllowOutboundEvents(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setAllowOutboundEvents(self,v):
        LCLBinding.set_Grids_TCustomDrawGrid_AllowOutboundEvents(self.pointer,v)
    AllowOutboundEvents=property(getAllowOutboundEvents,setAllowOutboundEvents)
    def getCol(self):
        r=LCLBinding.get_Grids_TCustomDrawGrid_Col(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setCol(self,v):
        LCLBinding.set_Grids_TCustomDrawGrid_Col(self.pointer,v)
    Col=property(getCol,setCol)
    def getColWidths(self,aCol):
        r=LCLBinding.get_Grids_TCustomDrawGrid_ColWidths(self.pointer,aCol)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setColWidths(self,aCol,v):
        LCLBinding.set_Grids_TCustomDrawGrid_ColWidths(self.pointer,aCol,v)
    def getEditor(self):
        r=LCLBinding.get_Grids_TCustomDrawGrid_Editor(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TWinControl)
    def setEditor(self,v):
        LCLBinding.set_Grids_TCustomDrawGrid_Editor(self.pointer,v.pointer)
    Editor=property(getEditor,setEditor)
    def getEditorMode(self):
        r=LCLBinding.get_Grids_TCustomDrawGrid_EditorMode(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setEditorMode(self,v):
        LCLBinding.set_Grids_TCustomDrawGrid_EditorMode(self.pointer,v)
    EditorMode=property(getEditorMode,setEditorMode)
    def getExtendedColSizing(self):
        r=LCLBinding.get_Grids_TCustomDrawGrid_ExtendedColSizing(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setExtendedColSizing(self,v):
        LCLBinding.set_Grids_TCustomDrawGrid_ExtendedColSizing(self.pointer,v)
    ExtendedColSizing=property(getExtendedColSizing,setExtendedColSizing)
    def getAltColorStartNormal(self):
        r=LCLBinding.get_Grids_TCustomDrawGrid_AltColorStartNormal(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setAltColorStartNormal(self,v):
        LCLBinding.set_Grids_TCustomDrawGrid_AltColorStartNormal(self.pointer,v)
    AltColorStartNormal=property(getAltColorStartNormal,setAltColorStartNormal)
    def getFastEditing(self):
        r=LCLBinding.get_Grids_TCustomDrawGrid_FastEditing(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setFastEditing(self,v):
        LCLBinding.set_Grids_TCustomDrawGrid_FastEditing(self.pointer,v)
    FastEditing=property(getFastEditing,setFastEditing)
    def getFocusRectVisible(self):
        r=LCLBinding.get_Grids_TCustomDrawGrid_FocusRectVisible(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setFocusRectVisible(self,v):
        LCLBinding.set_Grids_TCustomDrawGrid_FocusRectVisible(self.pointer,v)
    FocusRectVisible=property(getFocusRectVisible,setFocusRectVisible)
    def getGridHeight(self):
        r=LCLBinding.get_Grids_TCustomDrawGrid_GridHeight(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    GridHeight=property(getGridHeight)
    def getGridWidth(self):
        r=LCLBinding.get_Grids_TCustomDrawGrid_GridWidth(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    GridWidth=property(getGridWidth)
    def getIsCellSelected(self,aCol,aRow):
        r=LCLBinding.get_Grids_TCustomDrawGrid_IsCellSelected(self.pointer,aCol,aRow)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def getLeftCol(self):
        r=LCLBinding.get_Grids_TCustomDrawGrid_LeftCol(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setLeftCol(self,v):
        LCLBinding.set_Grids_TCustomDrawGrid_LeftCol(self.pointer,v)
    LeftCol=property(getLeftCol,setLeftCol)
    def getRow(self):
        r=LCLBinding.get_Grids_TCustomDrawGrid_Row(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setRow(self,v):
        LCLBinding.set_Grids_TCustomDrawGrid_Row(self.pointer,v)
    Row=property(getRow,setRow)
    def getRowHeights(self,aRow):
        r=LCLBinding.get_Grids_TCustomDrawGrid_RowHeights(self.pointer,aRow)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setRowHeights(self,aRow,v):
        LCLBinding.set_Grids_TCustomDrawGrid_RowHeights(self.pointer,aRow,v)
    def getSaveOptions(self):
        r=LCLBinding.get_Grids_TCustomDrawGrid_SaveOptions(self.pointer)
        return r
    def setSaveOptions(self,v):
        LCLBinding.set_Grids_TCustomDrawGrid_SaveOptions(self.pointer,v.pointer)
    SaveOptions=property(getSaveOptions,setSaveOptions)
    def getSelectedColumn(self):
        r=LCLBinding.get_Grids_TCustomDrawGrid_SelectedColumn(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TGridColumn)
    SelectedColumn=property(getSelectedColumn)
    def getStrictSort(self):
        r=LCLBinding.get_Grids_TCustomDrawGrid_StrictSort(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setStrictSort(self,v):
        LCLBinding.set_Grids_TCustomDrawGrid_StrictSort(self.pointer,v)
    StrictSort=property(getStrictSort,setStrictSort)
    def getTopRow(self):
        r=LCLBinding.get_Grids_TCustomDrawGrid_TopRow(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setTopRow(self,v):
        LCLBinding.set_Grids_TCustomDrawGrid_TopRow(self.pointer,v)
    TopRow=property(getTopRow,setTopRow)
    def getUseXORFeatures(self):
        r=LCLBinding.get_Grids_TCustomDrawGrid_UseXORFeatures(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setUseXORFeatures(self,v):
        LCLBinding.set_Grids_TCustomDrawGrid_UseXORFeatures(self.pointer,v)
    UseXORFeatures=property(getUseXORFeatures,setUseXORFeatures)
    def getAutoAdvance(self):
        r=LCLBinding.get_Grids_TCustomDrawGrid_AutoAdvance(self.pointer)
        return r
    def setAutoAdvance(self,v):
        LCLBinding.set_Grids_TCustomDrawGrid_AutoAdvance(self.pointer,v.pointer)
    AutoAdvance=property(getAutoAdvance,setAutoAdvance)
    def getAutoFillColumns(self):
        r=LCLBinding.get_Grids_TCustomDrawGrid_AutoFillColumns(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setAutoFillColumns(self,v):
        LCLBinding.set_Grids_TCustomDrawGrid_AutoFillColumns(self.pointer,v)
    AutoFillColumns=property(getAutoFillColumns,setAutoFillColumns)
    def getColCount(self):
        r=LCLBinding.get_Grids_TCustomDrawGrid_ColCount(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setColCount(self,v):
        LCLBinding.set_Grids_TCustomDrawGrid_ColCount(self.pointer,v)
    ColCount=property(getColCount,setColCount)
    def getColumns(self):
        r=LCLBinding.get_Grids_TCustomDrawGrid_Columns(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TGridColumns)
    def setColumns(self,v):
        LCLBinding.set_Grids_TCustomDrawGrid_Columns(self.pointer,v.pointer)
    Columns=property(getColumns,setColumns)
    def getDefaultColWidth(self):
        r=LCLBinding.get_Grids_TCustomDrawGrid_DefaultColWidth(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setDefaultColWidth(self,v):
        LCLBinding.set_Grids_TCustomDrawGrid_DefaultColWidth(self.pointer,v)
    DefaultColWidth=property(getDefaultColWidth,setDefaultColWidth)
    def getDefaultDrawing(self):
        r=LCLBinding.get_Grids_TCustomDrawGrid_DefaultDrawing(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setDefaultDrawing(self,v):
        LCLBinding.set_Grids_TCustomDrawGrid_DefaultDrawing(self.pointer,v)
    DefaultDrawing=property(getDefaultDrawing,setDefaultDrawing)
    def getDefaultRowHeight(self):
        r=LCLBinding.get_Grids_TCustomDrawGrid_DefaultRowHeight(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setDefaultRowHeight(self,v):
        LCLBinding.set_Grids_TCustomDrawGrid_DefaultRowHeight(self.pointer,v)
    DefaultRowHeight=property(getDefaultRowHeight,setDefaultRowHeight)
    def getFixedCols(self):
        r=LCLBinding.get_Grids_TCustomDrawGrid_FixedCols(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setFixedCols(self,v):
        LCLBinding.set_Grids_TCustomDrawGrid_FixedCols(self.pointer,v)
    FixedCols=property(getFixedCols,setFixedCols)
    def getFixedRows(self):
        r=LCLBinding.get_Grids_TCustomDrawGrid_FixedRows(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setFixedRows(self,v):
        LCLBinding.set_Grids_TCustomDrawGrid_FixedRows(self.pointer,v)
    FixedRows=property(getFixedRows,setFixedRows)
    def getFlat(self):
        r=LCLBinding.get_Grids_TCustomDrawGrid_Flat(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setFlat(self,v):
        LCLBinding.set_Grids_TCustomDrawGrid_Flat(self.pointer,v)
    Flat=property(getFlat,setFlat)
    def getGridLineWidth(self):
        r=LCLBinding.get_Grids_TCustomDrawGrid_GridLineWidth(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setGridLineWidth(self,v):
        LCLBinding.set_Grids_TCustomDrawGrid_GridLineWidth(self.pointer,v)
    GridLineWidth=property(getGridLineWidth,setGridLineWidth)
    def getOptions(self):
        r=LCLBinding.get_Grids_TCustomDrawGrid_Options(self.pointer)
        return r
    def setOptions(self,v):
        LCLBinding.set_Grids_TCustomDrawGrid_Options(self.pointer,v.pointer)
    Options=property(getOptions,setOptions)
    def getOptions2(self):
        r=LCLBinding.get_Grids_TCustomDrawGrid_Options2(self.pointer)
        return r
    def setOptions2(self,v):
        LCLBinding.set_Grids_TCustomDrawGrid_Options2(self.pointer,v.pointer)
    Options2=property(getOptions2,setOptions2)
    def getParentShowHint(self):
        r=LCLBinding.get_Grids_TCustomDrawGrid_ParentShowHint(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentShowHint(self,v):
        LCLBinding.set_Grids_TCustomDrawGrid_ParentShowHint(self.pointer,v)
    ParentShowHint=property(getParentShowHint,setParentShowHint)
    def getRowCount(self):
        r=LCLBinding.get_Grids_TCustomDrawGrid_RowCount(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setRowCount(self,v):
        LCLBinding.set_Grids_TCustomDrawGrid_RowCount(self.pointer,v)
    RowCount=property(getRowCount,setRowCount)
    def getScrollBars(self):
        r=LCLBinding.get_Grids_TCustomDrawGrid_ScrollBars(self.pointer)
        return r
    def setScrollBars(self,v):
        LCLBinding.set_Grids_TCustomDrawGrid_ScrollBars(self.pointer,v.pointer)
    ScrollBars=property(getScrollBars,setScrollBars)
    def getTabAdvance(self):
        r=LCLBinding.get_Grids_TCustomDrawGrid_TabAdvance(self.pointer)
        return r
    def setTabAdvance(self,v):
        LCLBinding.set_Grids_TCustomDrawGrid_TabAdvance(self.pointer,v.pointer)
    TabAdvance=property(getTabAdvance,setTabAdvance)
    def getVisibleColCount(self):
        r=LCLBinding.get_Grids_TCustomDrawGrid_VisibleColCount(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    VisibleColCount=property(getVisibleColCount)
    def getVisibleRowCount(self):
        r=LCLBinding.get_Grids_TCustomDrawGrid_VisibleRowCount(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    VisibleRowCount=property(getVisibleRowCount)
    def _Warper_OnAfterSelection(self,Sender,aCol,aRow):
        self.OnAfterSelectioncall(LCLBindingUtil.GetPytonObject(Sender,TObject),aCol,aRow)
    def setOnAfterSelection(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnAfterSelectioncall'):
            FreeOldEvent=1
            oldobj=OnAfterSelectionPasObject
        self.OnAfterSelectioncall=v 
        self.PasOnAfterSelection=FunctionForm(self._Warper_OnAfterSelection)
        self.OnAfterSelectionPasObject=LCLBinding.set_Grids_TCustomDrawGrid_OnAfterSelection(self.pointer,self.PasOnAfterSelection,oldobj,FreeOldEvent)
    def getOnAfterSelection(self):
        return OnAfterSelectioncall
    OnAfterSelection=property(getOnAfterSelection,setOnAfterSelection)
    def _Warper_OnBeforeSelection(self,Sender,aCol,aRow):
        self.OnBeforeSelectioncall(LCLBindingUtil.GetPytonObject(Sender,TObject),aCol,aRow)
    def setOnBeforeSelection(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnBeforeSelectioncall'):
            FreeOldEvent=1
            oldobj=OnBeforeSelectionPasObject
        self.OnBeforeSelectioncall=v 
        self.PasOnBeforeSelection=FunctionForm(self._Warper_OnBeforeSelection)
        self.OnBeforeSelectionPasObject=LCLBinding.set_Grids_TCustomDrawGrid_OnBeforeSelection(self.pointer,self.PasOnBeforeSelection,oldobj,FreeOldEvent)
    def getOnBeforeSelection(self):
        return OnBeforeSelectioncall
    OnBeforeSelection=property(getOnBeforeSelection,setOnBeforeSelection)
    def _Warper_OnColRowDeleted(self,Sender,IsColumn,sIndex,tIndex):
        self.OnColRowDeletedcall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.IntToBoolean(IsColumn),sIndex,tIndex)
    def setOnColRowDeleted(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnColRowDeletedcall'):
            FreeOldEvent=1
            oldobj=OnColRowDeletedPasObject
        self.OnColRowDeletedcall=v 
        self.PasOnColRowDeleted=FunctionForm(self._Warper_OnColRowDeleted)
        self.OnColRowDeletedPasObject=LCLBinding.set_Grids_TCustomDrawGrid_OnColRowDeleted(self.pointer,self.PasOnColRowDeleted,oldobj,FreeOldEvent)
    def getOnColRowDeleted(self):
        return OnColRowDeletedcall
    OnColRowDeleted=property(getOnColRowDeleted,setOnColRowDeleted)
    def _Warper_OnColRowExchanged(self,Sender,IsColumn,sIndex,tIndex):
        self.OnColRowExchangedcall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.IntToBoolean(IsColumn),sIndex,tIndex)
    def setOnColRowExchanged(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnColRowExchangedcall'):
            FreeOldEvent=1
            oldobj=OnColRowExchangedPasObject
        self.OnColRowExchangedcall=v 
        self.PasOnColRowExchanged=FunctionForm(self._Warper_OnColRowExchanged)
        self.OnColRowExchangedPasObject=LCLBinding.set_Grids_TCustomDrawGrid_OnColRowExchanged(self.pointer,self.PasOnColRowExchanged,oldobj,FreeOldEvent)
    def getOnColRowExchanged(self):
        return OnColRowExchangedcall
    OnColRowExchanged=property(getOnColRowExchanged,setOnColRowExchanged)
    def _Warper_OnColRowInserted(self,Sender,IsColumn,sIndex,tIndex):
        self.OnColRowInsertedcall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.IntToBoolean(IsColumn),sIndex,tIndex)
    def setOnColRowInserted(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnColRowInsertedcall'):
            FreeOldEvent=1
            oldobj=OnColRowInsertedPasObject
        self.OnColRowInsertedcall=v 
        self.PasOnColRowInserted=FunctionForm(self._Warper_OnColRowInserted)
        self.OnColRowInsertedPasObject=LCLBinding.set_Grids_TCustomDrawGrid_OnColRowInserted(self.pointer,self.PasOnColRowInserted,oldobj,FreeOldEvent)
    def getOnColRowInserted(self):
        return OnColRowInsertedcall
    OnColRowInserted=property(getOnColRowInserted,setOnColRowInserted)
    def _Warper_OnColRowMoved(self,Sender,IsColumn,sIndex,tIndex):
        self.OnColRowMovedcall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.IntToBoolean(IsColumn),sIndex,tIndex)
    def setOnColRowMoved(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnColRowMovedcall'):
            FreeOldEvent=1
            oldobj=OnColRowMovedPasObject
        self.OnColRowMovedcall=v 
        self.PasOnColRowMoved=FunctionForm(self._Warper_OnColRowMoved)
        self.OnColRowMovedPasObject=LCLBinding.set_Grids_TCustomDrawGrid_OnColRowMoved(self.pointer,self.PasOnColRowMoved,oldobj,FreeOldEvent)
    def getOnColRowMoved(self):
        return OnColRowMovedcall
    OnColRowMoved=property(getOnColRowMoved,setOnColRowMoved)
    def _Warper_OnCompareCells(self,Sender,ACol,ARow,BCol,BRow,Result):
        self.OnCompareCellscall(LCLBindingUtil.GetPytonObject(Sender,TObject),ACol,ARow,BCol,BRow,Result)
    def setOnCompareCells(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int,c_int,c_int,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnCompareCellscall'):
            FreeOldEvent=1
            oldobj=OnCompareCellsPasObject
        self.OnCompareCellscall=v 
        self.PasOnCompareCells=FunctionForm(self._Warper_OnCompareCells)
        self.OnCompareCellsPasObject=LCLBinding.set_Grids_TCustomDrawGrid_OnCompareCells(self.pointer,self.PasOnCompareCells,oldobj,FreeOldEvent)
    def getOnCompareCells(self):
        return OnCompareCellscall
    OnCompareCells=property(getOnCompareCells,setOnCompareCells)
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
        self.OnDblClickPasObject=LCLBinding.set_Grids_TCustomDrawGrid_OnDblClick(self.pointer,self.PasOnDblClick,oldobj,FreeOldEvent)
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
        self.OnDragDropPasObject=LCLBinding.set_Grids_TCustomDrawGrid_OnDragDrop(self.pointer,self.PasOnDragDrop,oldobj,FreeOldEvent)
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
        self.OnDragOverPasObject=LCLBinding.set_Grids_TCustomDrawGrid_OnDragOver(self.pointer,self.PasOnDragOver,oldobj,FreeOldEvent)
    def getOnDragOver(self):
        return OnDragOvercall
    OnDragOver=property(getOnDragOver,setOnDragOver)
    def _Warper_OnEditButtonClick(self,Sender):
        self.OnEditButtonClickcall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnEditButtonClick(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnEditButtonClickcall'):
            FreeOldEvent=1
            oldobj=OnEditButtonClickPasObject
        self.OnEditButtonClickcall=v 
        self.PasOnEditButtonClick=FunctionForm(self._Warper_OnEditButtonClick)
        self.OnEditButtonClickPasObject=LCLBinding.set_Grids_TCustomDrawGrid_OnEditButtonClick(self.pointer,self.PasOnEditButtonClick,oldobj,FreeOldEvent)
    def getOnEditButtonClick(self):
        return OnEditButtonClickcall
    OnEditButtonClick=property(getOnEditButtonClick,setOnEditButtonClick)
    def _Warper_OnButtonClick(self,Sender,aCol,aRow):
        self.OnButtonClickcall(LCLBindingUtil.GetPytonObject(Sender,TObject),aCol,aRow)
    def setOnButtonClick(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnButtonClickcall'):
            FreeOldEvent=1
            oldobj=OnButtonClickPasObject
        self.OnButtonClickcall=v 
        self.PasOnButtonClick=FunctionForm(self._Warper_OnButtonClick)
        self.OnButtonClickPasObject=LCLBinding.set_Grids_TCustomDrawGrid_OnButtonClick(self.pointer,self.PasOnButtonClick,oldobj,FreeOldEvent)
    def getOnButtonClick(self):
        return OnButtonClickcall
    OnButtonClick=property(getOnButtonClick,setOnButtonClick)
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
        self.OnEndDockPasObject=LCLBinding.set_Grids_TCustomDrawGrid_OnEndDock(self.pointer,self.PasOnEndDock,oldobj,FreeOldEvent)
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
        self.OnEndDragPasObject=LCLBinding.set_Grids_TCustomDrawGrid_OnEndDrag(self.pointer,self.PasOnEndDrag,oldobj,FreeOldEvent)
    def getOnEndDrag(self):
        return OnEndDragcall
    OnEndDrag=property(getOnEndDrag,setOnEndDrag)
    def _Warper_OnGetEditMask(self,Sender,ACol,ARow,Value):
        self.OnGetEditMaskcall(LCLBindingUtil.GetPytonObject(Sender,TObject),ACol,ARow,Value)
    def setOnGetEditMask(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int,c_int,c_char_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnGetEditMaskcall'):
            FreeOldEvent=1
            oldobj=OnGetEditMaskPasObject
        self.OnGetEditMaskcall=v 
        self.PasOnGetEditMask=FunctionForm(self._Warper_OnGetEditMask)
        self.OnGetEditMaskPasObject=LCLBinding.set_Grids_TCustomDrawGrid_OnGetEditMask(self.pointer,self.PasOnGetEditMask,oldobj,FreeOldEvent)
    def getOnGetEditMask(self):
        return OnGetEditMaskcall
    OnGetEditMask=property(getOnGetEditMask,setOnGetEditMask)
    def _Warper_OnGetEditText(self,Sender,ACol,ARow,Value):
        self.OnGetEditTextcall(LCLBindingUtil.GetPytonObject(Sender,TObject),ACol,ARow,Value)
    def setOnGetEditText(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int,c_int,c_char_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnGetEditTextcall'):
            FreeOldEvent=1
            oldobj=OnGetEditTextPasObject
        self.OnGetEditTextcall=v 
        self.PasOnGetEditText=FunctionForm(self._Warper_OnGetEditText)
        self.OnGetEditTextPasObject=LCLBinding.set_Grids_TCustomDrawGrid_OnGetEditText(self.pointer,self.PasOnGetEditText,oldobj,FreeOldEvent)
    def getOnGetEditText(self):
        return OnGetEditTextcall
    OnGetEditText=property(getOnGetEditText,setOnGetEditText)
    def _Warper_OnHeaderClick(self,Sender,IsColumn,Index):
        self.OnHeaderClickcall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.IntToBoolean(IsColumn),Index)
    def setOnHeaderClick(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnHeaderClickcall'):
            FreeOldEvent=1
            oldobj=OnHeaderClickPasObject
        self.OnHeaderClickcall=v 
        self.PasOnHeaderClick=FunctionForm(self._Warper_OnHeaderClick)
        self.OnHeaderClickPasObject=LCLBinding.set_Grids_TCustomDrawGrid_OnHeaderClick(self.pointer,self.PasOnHeaderClick,oldobj,FreeOldEvent)
    def getOnHeaderClick(self):
        return OnHeaderClickcall
    OnHeaderClick=property(getOnHeaderClick,setOnHeaderClick)
    def _Warper_OnHeaderSized(self,Sender,IsColumn,Index):
        self.OnHeaderSizedcall(LCLBindingUtil.GetPytonObject(Sender,TObject),LCLBindingUtil.IntToBoolean(IsColumn),Index)
    def setOnHeaderSized(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnHeaderSizedcall'):
            FreeOldEvent=1
            oldobj=OnHeaderSizedPasObject
        self.OnHeaderSizedcall=v 
        self.PasOnHeaderSized=FunctionForm(self._Warper_OnHeaderSized)
        self.OnHeaderSizedPasObject=LCLBinding.set_Grids_TCustomDrawGrid_OnHeaderSized(self.pointer,self.PasOnHeaderSized,oldobj,FreeOldEvent)
    def getOnHeaderSized(self):
        return OnHeaderSizedcall
    OnHeaderSized=property(getOnHeaderSized,setOnHeaderSized)
    def _Warper_OnHeaderSizing(self,sender,IsColumn,aIndex,aSize):
        self.OnHeaderSizingcall(LCLBindingUtil.GetPytonObject(sender,TObject),LCLBindingUtil.IntToBoolean(IsColumn),aIndex,aSize)
    def setOnHeaderSizing(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnHeaderSizingcall'):
            FreeOldEvent=1
            oldobj=OnHeaderSizingPasObject
        self.OnHeaderSizingcall=v 
        self.PasOnHeaderSizing=FunctionForm(self._Warper_OnHeaderSizing)
        self.OnHeaderSizingPasObject=LCLBinding.set_Grids_TCustomDrawGrid_OnHeaderSizing(self.pointer,self.PasOnHeaderSizing,oldobj,FreeOldEvent)
    def getOnHeaderSizing(self):
        return OnHeaderSizingcall
    OnHeaderSizing=property(getOnHeaderSizing,setOnHeaderSizing)
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
        self.OnMouseDownPasObject=LCLBinding.set_Grids_TCustomDrawGrid_OnMouseDown(self.pointer,self.PasOnMouseDown,oldobj,FreeOldEvent)
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
        self.OnMouseEnterPasObject=LCLBinding.set_Grids_TCustomDrawGrid_OnMouseEnter(self.pointer,self.PasOnMouseEnter,oldobj,FreeOldEvent)
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
        self.OnMouseLeavePasObject=LCLBinding.set_Grids_TCustomDrawGrid_OnMouseLeave(self.pointer,self.PasOnMouseLeave,oldobj,FreeOldEvent)
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
        self.OnMouseMovePasObject=LCLBinding.set_Grids_TCustomDrawGrid_OnMouseMove(self.pointer,self.PasOnMouseMove,oldobj,FreeOldEvent)
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
        self.OnMouseUpPasObject=LCLBinding.set_Grids_TCustomDrawGrid_OnMouseUp(self.pointer,self.PasOnMouseUp,oldobj,FreeOldEvent)
    def getOnMouseUp(self):
        return OnMouseUpcall
    OnMouseUp=property(getOnMouseUp,setOnMouseUp)
    def _Warper_OnPickListSelect(self,Sender):
        self.OnPickListSelectcall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnPickListSelect(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnPickListSelectcall'):
            FreeOldEvent=1
            oldobj=OnPickListSelectPasObject
        self.OnPickListSelectcall=v 
        self.PasOnPickListSelect=FunctionForm(self._Warper_OnPickListSelect)
        self.OnPickListSelectPasObject=LCLBinding.set_Grids_TCustomDrawGrid_OnPickListSelect(self.pointer,self.PasOnPickListSelect,oldobj,FreeOldEvent)
    def getOnPickListSelect(self):
        return OnPickListSelectcall
    OnPickListSelect=property(getOnPickListSelect,setOnPickListSelect)
    def _Warper_OnPrepareCanvas(self,sender,aCol,aRow,aState):
        self.OnPrepareCanvascall(LCLBindingUtil.GetPytonObject(sender,TObject),aCol,aRow,aState)
    def setOnPrepareCanvas(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnPrepareCanvascall'):
            FreeOldEvent=1
            oldobj=OnPrepareCanvasPasObject
        self.OnPrepareCanvascall=v 
        self.PasOnPrepareCanvas=FunctionForm(self._Warper_OnPrepareCanvas)
        self.OnPrepareCanvasPasObject=LCLBinding.set_Grids_TCustomDrawGrid_OnPrepareCanvas(self.pointer,self.PasOnPrepareCanvas,oldobj,FreeOldEvent)
    def getOnPrepareCanvas(self):
        return OnPrepareCanvascall
    OnPrepareCanvas=property(getOnPrepareCanvas,setOnPrepareCanvas)
    def _Warper_OnSelectEditor(self,Sender,aCol,aRow,Editor):
        self.OnSelectEditorcall(LCLBindingUtil.GetPytonObject(Sender,TObject),aCol,aRow,LCLBindingUtil.GetPytonObject(Editor,TWinControl))
    def setOnSelectEditor(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int,c_int,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnSelectEditorcall'):
            FreeOldEvent=1
            oldobj=OnSelectEditorPasObject
        self.OnSelectEditorcall=v 
        self.PasOnSelectEditor=FunctionForm(self._Warper_OnSelectEditor)
        self.OnSelectEditorPasObject=LCLBinding.set_Grids_TCustomDrawGrid_OnSelectEditor(self.pointer,self.PasOnSelectEditor,oldobj,FreeOldEvent)
    def getOnSelectEditor(self):
        return OnSelectEditorcall
    OnSelectEditor=property(getOnSelectEditor,setOnSelectEditor)
    def _Warper_OnSelection(self,Sender,aCol,aRow):
        self.OnSelectioncall(LCLBindingUtil.GetPytonObject(Sender,TObject),aCol,aRow)
    def setOnSelection(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnSelectioncall'):
            FreeOldEvent=1
            oldobj=OnSelectionPasObject
        self.OnSelectioncall=v 
        self.PasOnSelection=FunctionForm(self._Warper_OnSelection)
        self.OnSelectionPasObject=LCLBinding.set_Grids_TCustomDrawGrid_OnSelection(self.pointer,self.PasOnSelection,oldobj,FreeOldEvent)
    def getOnSelection(self):
        return OnSelectioncall
    OnSelection=property(getOnSelection,setOnSelection)
    def _Warper_OnSelectCell(self,Sender,aCol,aRow,CanSelect):
        self.OnSelectCellcall(LCLBindingUtil.GetPytonObject(Sender,TObject),aCol,aRow,LCLBindingUtil.IntToBoolean(CanSelect))
    def setOnSelectCell(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnSelectCellcall'):
            FreeOldEvent=1
            oldobj=OnSelectCellPasObject
        self.OnSelectCellcall=v 
        self.PasOnSelectCell=FunctionForm(self._Warper_OnSelectCell)
        self.OnSelectCellPasObject=LCLBinding.set_Grids_TCustomDrawGrid_OnSelectCell(self.pointer,self.PasOnSelectCell,oldobj,FreeOldEvent)
    def getOnSelectCell(self):
        return OnSelectCellcall
    OnSelectCell=property(getOnSelectCell,setOnSelectCell)
    def _Warper_OnSetEditText(self,Sender,ACol,ARow,Value):
        self.OnSetEditTextcall(LCLBindingUtil.GetPytonObject(Sender,TObject),ACol,ARow,Value)
    def setOnSetEditText(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int,c_int,c_char_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnSetEditTextcall'):
            FreeOldEvent=1
            oldobj=OnSetEditTextPasObject
        self.OnSetEditTextcall=v 
        self.PasOnSetEditText=FunctionForm(self._Warper_OnSetEditText)
        self.OnSetEditTextPasObject=LCLBinding.set_Grids_TCustomDrawGrid_OnSetEditText(self.pointer,self.PasOnSetEditText,oldobj,FreeOldEvent)
    def getOnSetEditText(self):
        return OnSetEditTextcall
    OnSetEditText=property(getOnSetEditText,setOnSetEditText)
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
        self.OnStartDockPasObject=LCLBinding.set_Grids_TCustomDrawGrid_OnStartDock(self.pointer,self.PasOnStartDock,oldobj,FreeOldEvent)
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
        self.OnStartDragPasObject=LCLBinding.set_Grids_TCustomDrawGrid_OnStartDrag(self.pointer,self.PasOnStartDrag,oldobj,FreeOldEvent)
    def getOnStartDrag(self):
        return OnStartDragcall
    OnStartDrag=property(getOnStartDrag,setOnStartDrag)
#class TCustomDrawGrid end
#class TGridColumnTitle start
class TGridColumnTitle(TPersistent):
#    pointer=c_void_p()
    def __init__(self):#TGridColumnTitle
        TPersistent.__init__(self)
#constructorGrids_TGridColumnTitle_Create
    @staticmethod
    def Create(TheColumn):
        return LCLBindingUtil.GetPytonObject(LCLBinding.Grids_TGridColumnTitle_Create((TheColumn.pointer)),TGridColumnTitle)
#Procedure Grids_TGridColumnTitle_Assign
    @staticmethod
    def Assign(self,Source):
        LCLBinding.Grids_TGridColumnTitle_Assign((Source.pointer))
#Procedure Grids_TGridColumnTitle_FillTitleDefaultFont
    @staticmethod
    def FillTitleDefaultFont(self,):
        LCLBinding.Grids_TGridColumnTitle_FillTitleDefaultFont()
    def getColumn(self):
        r=LCLBinding.get_Grids_TGridColumnTitle_Column(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TGridColumn)
    Column=property(getColumn)
    def getAlignment(self):
        r=LCLBinding.get_Grids_TGridColumnTitle_Alignment(self.pointer)
        return r
    def setAlignment(self,v):
        LCLBinding.set_Grids_TGridColumnTitle_Alignment(self.pointer,v.pointer)
    Alignment=property(getAlignment,setAlignment)
    def getCaption(self):
        r=LCLBinding.get_Grids_TGridColumnTitle_Caption(self.pointer)
        return LCLBindingUtil.ConvertPascalTCaption(r)
    def setCaption(self,v):
        LCLBinding.set_Grids_TGridColumnTitle_Caption(self.pointer,v)
    Caption=property(getCaption,setCaption)
    def getFont(self):
        r=LCLBinding.get_Grids_TGridColumnTitle_Font(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TFont)
    def setFont(self,v):
        LCLBinding.set_Grids_TGridColumnTitle_Font(self.pointer,v.pointer)
    Font=property(getFont,setFont)
    def getImageIndex(self):
        r=LCLBinding.get_Grids_TGridColumnTitle_ImageIndex(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setImageIndex(self,v):
        LCLBinding.set_Grids_TGridColumnTitle_ImageIndex(self.pointer,v)
    ImageIndex=property(getImageIndex,setImageIndex)
    def getImageLayout(self):
        r=LCLBinding.get_Grids_TGridColumnTitle_ImageLayout(self.pointer)
        return r
    def setImageLayout(self,v):
        LCLBinding.set_Grids_TGridColumnTitle_ImageLayout(self.pointer,v.pointer)
    ImageLayout=property(getImageLayout,setImageLayout)
    def getLayout(self):
        r=LCLBinding.get_Grids_TGridColumnTitle_Layout(self.pointer)
        return r
    def setLayout(self,v):
        LCLBinding.set_Grids_TGridColumnTitle_Layout(self.pointer,v.pointer)
    Layout=property(getLayout,setLayout)
    def getMultiLine(self):
        r=LCLBinding.get_Grids_TGridColumnTitle_MultiLine(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setMultiLine(self,v):
        LCLBinding.set_Grids_TGridColumnTitle_MultiLine(self.pointer,v)
    MultiLine=property(getMultiLine,setMultiLine)
    def getPrefixOption(self):
        r=LCLBinding.get_Grids_TGridColumnTitle_PrefixOption(self.pointer)
        return r
    def setPrefixOption(self,v):
        LCLBinding.set_Grids_TGridColumnTitle_PrefixOption(self.pointer,v.pointer)
    PrefixOption=property(getPrefixOption,setPrefixOption)
#class TGridColumnTitle end
#class TGridColumn start
class TGridColumn(TCollectionItem):
#    pointer=c_void_p()
    def __init__(self):#TGridColumn
        TCollectionItem.__init__(self)
#constructorGrids_TGridColumn_Create
    @staticmethod
    def Create(ACollection):
        return LCLBindingUtil.GetPytonObject(LCLBinding.Grids_TGridColumn_Create((ACollection.pointer)),TGridColumn)
#Procedure Grids_TGridColumn_Assign
    @staticmethod
    def Assign(self,Source):
        LCLBinding.Grids_TGridColumn_Assign((Source.pointer))
#Procedure Grids_TGridColumn_FillDefaultFont
    @staticmethod
    def FillDefaultFont(self,):
        LCLBinding.Grids_TGridColumn_FillDefaultFont()
    def getGrid(self):
        r=LCLBinding.get_Grids_TGridColumn_Grid(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TCustomGrid)
    Grid=property(getGrid)
    def getDefaultWidth(self):
        r=LCLBinding.get_Grids_TGridColumn_DefaultWidth(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    DefaultWidth=property(getDefaultWidth)
    def getStoredWidth(self):
        r=LCLBinding.get_Grids_TGridColumn_StoredWidth(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    StoredWidth=property(getStoredWidth)
    def getWidthChanged(self):
        r=LCLBinding.get_Grids_TGridColumn_WidthChanged(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    WidthChanged=property(getWidthChanged)
    def getAlignment(self):
        r=LCLBinding.get_Grids_TGridColumn_Alignment(self.pointer)
        return r
    def setAlignment(self,v):
        LCLBinding.set_Grids_TGridColumn_Alignment(self.pointer,v.pointer)
    Alignment=property(getAlignment,setAlignment)
    def getButtonStyle(self):
        r=LCLBinding.get_Grids_TGridColumn_ButtonStyle(self.pointer)
        return r
    def setButtonStyle(self,v):
        LCLBinding.set_Grids_TGridColumn_ButtonStyle(self.pointer,v.pointer)
    ButtonStyle=property(getButtonStyle,setButtonStyle)
    def getExpanded(self):
        r=LCLBinding.get_Grids_TGridColumn_Expanded(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setExpanded(self,v):
        LCLBinding.set_Grids_TGridColumn_Expanded(self.pointer,v)
    Expanded=property(getExpanded,setExpanded)
    def getFont(self):
        r=LCLBinding.get_Grids_TGridColumn_Font(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TFont)
    def setFont(self,v):
        LCLBinding.set_Grids_TGridColumn_Font(self.pointer,v.pointer)
    Font=property(getFont,setFont)
    def getLayout(self):
        r=LCLBinding.get_Grids_TGridColumn_Layout(self.pointer)
        return r
    def setLayout(self,v):
        LCLBinding.set_Grids_TGridColumn_Layout(self.pointer,v.pointer)
    Layout=property(getLayout,setLayout)
    def getMinSize(self):
        r=LCLBinding.get_Grids_TGridColumn_MinSize(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setMinSize(self,v):
        LCLBinding.set_Grids_TGridColumn_MinSize(self.pointer,v)
    MinSize=property(getMinSize,setMinSize)
    def getMaxSize(self):
        r=LCLBinding.get_Grids_TGridColumn_MaxSize(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setMaxSize(self,v):
        LCLBinding.set_Grids_TGridColumn_MaxSize(self.pointer,v)
    MaxSize=property(getMaxSize,setMaxSize)
    def getPickList(self):
        r=LCLBinding.get_Grids_TGridColumn_PickList(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TStrings)
    def setPickList(self,v):
        LCLBinding.set_Grids_TGridColumn_PickList(self.pointer,v.pointer)
    PickList=property(getPickList,setPickList)
    def getReadOnly(self):
        r=LCLBinding.get_Grids_TGridColumn_ReadOnly(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setReadOnly(self,v):
        LCLBinding.set_Grids_TGridColumn_ReadOnly(self.pointer,v)
    ReadOnly=property(getReadOnly,setReadOnly)
    def getSizePriority(self):
        r=LCLBinding.get_Grids_TGridColumn_SizePriority(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setSizePriority(self,v):
        LCLBinding.set_Grids_TGridColumn_SizePriority(self.pointer,v)
    SizePriority=property(getSizePriority,setSizePriority)
    def getTitle(self):
        r=LCLBinding.get_Grids_TGridColumn_Title(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TGridColumnTitle)
    def setTitle(self,v):
        LCLBinding.set_Grids_TGridColumn_Title(self.pointer,v.pointer)
    Title=property(getTitle,setTitle)
    def getWidth(self):
        r=LCLBinding.get_Grids_TGridColumn_Width(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setWidth(self,v):
        LCLBinding.set_Grids_TGridColumn_Width(self.pointer,v)
    Width=property(getWidth,setWidth)
    def getVisible(self):
        r=LCLBinding.get_Grids_TGridColumn_Visible(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setVisible(self,v):
        LCLBinding.set_Grids_TGridColumn_Visible(self.pointer,v)
    Visible=property(getVisible,setVisible)
    def getValueChecked(self):
        r=LCLBinding.get_Grids_TGridColumn_ValueChecked(self.pointer)
        return LCLBindingUtil.ConvertPascalstring(r)
    def setValueChecked(self,v):
        LCLBinding.set_Grids_TGridColumn_ValueChecked(self.pointer,v)
    ValueChecked=property(getValueChecked,setValueChecked)
    def getValueUnchecked(self):
        r=LCLBinding.get_Grids_TGridColumn_ValueUnchecked(self.pointer)
        return LCLBindingUtil.ConvertPascalstring(r)
    def setValueUnchecked(self,v):
        LCLBinding.set_Grids_TGridColumn_ValueUnchecked(self.pointer,v)
    ValueUnchecked=property(getValueUnchecked,setValueUnchecked)
#class TGridColumn end
#class TGridColumns start
class TGridColumns(TCollection):
#    pointer=c_void_p()
    def __init__(self):#TGridColumns
        TCollection.__init__(self)
#Procedure Grids_TGridColumns_Clear
    @staticmethod
    def Clear(self,):
        LCLBinding.Grids_TGridColumns_Clear()
    def getGrid(self):
        r=LCLBinding.get_Grids_TGridColumns_Grid(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TCustomGrid)
    Grid=property(getGrid)
    def getItems(self,Index):
        r=LCLBinding.get_Grids_TGridColumns_Items(self.pointer,Index)
        return LCLBindingUtil.GetPytonObject(r,TGridColumn)
    def setItems(self,Index,v):
        LCLBinding.set_Grids_TGridColumns_Items(self.pointer,Index,v.pointer)
    def getVisibleCount(self):
        r=LCLBinding.get_Grids_TGridColumns_VisibleCount(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    VisibleCount=property(getVisibleCount)
    def getEnabled(self):
        r=LCLBinding.get_Grids_TGridColumns_Enabled(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    Enabled=property(getEnabled)
#class TGridColumns end
#class TCustomStringGrid start
class TCustomStringGrid(TCustomDrawGrid):
#    pointer=c_void_p()
    def __init__(self):#TCustomStringGrid
        TCustomDrawGrid.__init__(self)
#constructorGrids_TCustomStringGrid_Create
    @staticmethod
    def Create(AOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.Grids_TCustomStringGrid_Create((AOwner.pointer)),TCustomStringGrid)
#Procedure Grids_TCustomStringGrid_AutoSizeColumn
    @staticmethod
    def AutoSizeColumn(self,aCol):
        LCLBinding.Grids_TCustomStringGrid_AutoSizeColumn((aCol))
#Procedure Grids_TCustomStringGrid_AutoSizeColumns
    @staticmethod
    def AutoSizeColumns(self,):
        LCLBinding.Grids_TCustomStringGrid_AutoSizeColumns()
#Procedure Grids_TCustomStringGrid_CopyToClipboard
    @staticmethod
    def CopyToClipboard(self,AUseSelection):
        LCLBinding.Grids_TCustomStringGrid_CopyToClipboard((booleantoint(AUseSelection)))
    def getCells(self,ACol,ARow):
        r=LCLBinding.get_Grids_TCustomStringGrid_Cells(self.pointer,ACol,ARow)
        return LCLBindingUtil.ConvertPascalstring(r)
    def setCells(self,ACol,ARow,v):
        LCLBinding.set_Grids_TCustomStringGrid_Cells(self.pointer,ACol,ARow,v)
    def getCols(self,index):
        r=LCLBinding.get_Grids_TCustomStringGrid_Cols(self.pointer,index)
        return LCLBindingUtil.GetPytonObject(r,TStrings)
    def setCols(self,index,v):
        LCLBinding.set_Grids_TCustomStringGrid_Cols(self.pointer,index,v.pointer)
    def getExtendedSelect(self):
        r=LCLBinding.get_Grids_TCustomStringGrid_ExtendedSelect(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setExtendedSelect(self,v):
        LCLBinding.set_Grids_TCustomStringGrid_ExtendedSelect(self.pointer,v)
    ExtendedSelect=property(getExtendedSelect,setExtendedSelect)
    def getObjects(self,ACol,ARow):
        r=LCLBinding.get_Grids_TCustomStringGrid_Objects(self.pointer,ACol,ARow)
        return LCLBindingUtil.GetPytonObject(r,TObject)
    def setObjects(self,ACol,ARow,v):
        LCLBinding.set_Grids_TCustomStringGrid_Objects(self.pointer,ACol,ARow,v.pointer)
    def getRows(self,index):
        r=LCLBinding.get_Grids_TCustomStringGrid_Rows(self.pointer,index)
        return LCLBindingUtil.GetPytonObject(r,TStrings)
    def setRows(self,index,v):
        LCLBinding.set_Grids_TCustomStringGrid_Rows(self.pointer,index,v.pointer)
#class TCustomStringGrid end
#class TStringGrid start
class TStringGrid(TCustomStringGrid):
#    pointer=c_void_p()
    def __init__(self):#TStringGrid
        TCustomStringGrid.__init__(self)
    def getModified(self):
        r=LCLBinding.get_Grids_TStringGrid_Modified(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setModified(self,v):
        LCLBinding.set_Grids_TStringGrid_Modified(self.pointer,v)
    Modified=property(getModified,setModified)
    def getInplaceEditor(self):
        r=LCLBinding.get_Grids_TStringGrid_InplaceEditor(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TWinControl)
    InplaceEditor=property(getInplaceEditor)
    def getAutoEdit(self):
        r=LCLBinding.get_Grids_TStringGrid_AutoEdit(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setAutoEdit(self,v):
        LCLBinding.set_Grids_TStringGrid_AutoEdit(self.pointer,v)
    AutoEdit=property(getAutoEdit,setAutoEdit)
    def getCellHintPriority(self):
        r=LCLBinding.get_Grids_TStringGrid_CellHintPriority(self.pointer)
        return r
    def setCellHintPriority(self,v):
        LCLBinding.set_Grids_TStringGrid_CellHintPriority(self.pointer,v.pointer)
    CellHintPriority=property(getCellHintPriority,setCellHintPriority)
    def getColumnClickSorts(self):
        r=LCLBinding.get_Grids_TStringGrid_ColumnClickSorts(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setColumnClickSorts(self,v):
        LCLBinding.set_Grids_TStringGrid_ColumnClickSorts(self.pointer,v)
    ColumnClickSorts=property(getColumnClickSorts,setColumnClickSorts)
    def getDragKind(self):
        r=LCLBinding.get_Grids_TStringGrid_DragKind(self.pointer)
        return r
    def setDragKind(self,v):
        LCLBinding.set_Grids_TStringGrid_DragKind(self.pointer,v.pointer)
    DragKind=property(getDragKind,setDragKind)
    def getDragMode(self):
        r=LCLBinding.get_Grids_TStringGrid_DragMode(self.pointer)
        return r
    def setDragMode(self,v):
        LCLBinding.set_Grids_TStringGrid_DragMode(self.pointer,v.pointer)
    DragMode=property(getDragMode,setDragMode)
    def getHeaderHotZones(self):
        r=LCLBinding.get_Grids_TStringGrid_HeaderHotZones(self.pointer)
        return r
    def setHeaderHotZones(self,v):
        LCLBinding.set_Grids_TStringGrid_HeaderHotZones(self.pointer,v.pointer)
    HeaderHotZones=property(getHeaderHotZones,setHeaderHotZones)
    def getHeaderPushZones(self):
        r=LCLBinding.get_Grids_TStringGrid_HeaderPushZones(self.pointer)
        return r
    def setHeaderPushZones(self,v):
        LCLBinding.set_Grids_TStringGrid_HeaderPushZones(self.pointer,v.pointer)
    HeaderPushZones=property(getHeaderPushZones,setHeaderPushZones)
    def getMouseWheelOption(self):
        r=LCLBinding.get_Grids_TStringGrid_MouseWheelOption(self.pointer)
        return r
    def setMouseWheelOption(self,v):
        LCLBinding.set_Grids_TStringGrid_MouseWheelOption(self.pointer,v.pointer)
    MouseWheelOption=property(getMouseWheelOption,setMouseWheelOption)
    def getParentColor(self):
        r=LCLBinding.get_Grids_TStringGrid_ParentColor(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentColor(self,v):
        LCLBinding.set_Grids_TStringGrid_ParentColor(self.pointer,v)
    ParentColor=property(getParentColor,setParentColor)
    def getParentFont(self):
        r=LCLBinding.get_Grids_TStringGrid_ParentFont(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentFont(self,v):
        LCLBinding.set_Grids_TStringGrid_ParentFont(self.pointer,v)
    ParentFont=property(getParentFont,setParentFont)
    def getRangeSelectMode(self):
        r=LCLBinding.get_Grids_TStringGrid_RangeSelectMode(self.pointer)
        return r
    def setRangeSelectMode(self,v):
        LCLBinding.set_Grids_TStringGrid_RangeSelectMode(self.pointer,v.pointer)
    RangeSelectMode=property(getRangeSelectMode,setRangeSelectMode)
    def getTitleFont(self):
        r=LCLBinding.get_Grids_TStringGrid_TitleFont(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TFont)
    def setTitleFont(self,v):
        LCLBinding.set_Grids_TStringGrid_TitleFont(self.pointer,v.pointer)
    TitleFont=property(getTitleFont,setTitleFont)
    def getTitleImageList(self):
        r=LCLBinding.get_Grids_TStringGrid_TitleImageList(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TImageList)
    def setTitleImageList(self,v):
        LCLBinding.set_Grids_TStringGrid_TitleImageList(self.pointer,v.pointer)
    TitleImageList=property(getTitleImageList,setTitleImageList)
    def getTitleStyle(self):
        r=LCLBinding.get_Grids_TStringGrid_TitleStyle(self.pointer)
        return r
    def setTitleStyle(self,v):
        LCLBinding.set_Grids_TStringGrid_TitleStyle(self.pointer,v.pointer)
    TitleStyle=property(getTitleStyle,setTitleStyle)
    def _Warper_OnCellProcess(self,Sender,aCol,aRow,processType,aValue):
        self.OnCellProcesscall(LCLBindingUtil.GetPytonObject(Sender,TObject),aCol,aRow,processType,aValue)
    def setOnCellProcess(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int,c_int,c_int,c_char_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnCellProcesscall'):
            FreeOldEvent=1
            oldobj=OnCellProcessPasObject
        self.OnCellProcesscall=v 
        self.PasOnCellProcess=FunctionForm(self._Warper_OnCellProcess)
        self.OnCellProcessPasObject=LCLBinding.set_Grids_TStringGrid_OnCellProcess(self.pointer,self.PasOnCellProcess,oldobj,FreeOldEvent)
    def getOnCellProcess(self):
        return OnCellProcesscall
    OnCellProcess=property(getOnCellProcess,setOnCellProcess)
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
        self.OnCheckboxToggledPasObject=LCLBinding.set_Grids_TStringGrid_OnCheckboxToggled(self.pointer,self.PasOnCheckboxToggled,oldobj,FreeOldEvent)
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
        self.OnEditingDonePasObject=LCLBinding.set_Grids_TStringGrid_OnEditingDone(self.pointer,self.PasOnEditingDone,oldobj,FreeOldEvent)
    def getOnEditingDone(self):
        return OnEditingDonecall
    OnEditingDone=property(getOnEditingDone,setOnEditingDone)
    def _Warper_OnGetCellHint(self,Sender,ACol,ARow,HintText):
        self.OnGetCellHintcall(LCLBindingUtil.GetPytonObject(Sender,TObject),ACol,ARow,HintText)
    def setOnGetCellHint(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int,c_int,c_char_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnGetCellHintcall'):
            FreeOldEvent=1
            oldobj=OnGetCellHintPasObject
        self.OnGetCellHintcall=v 
        self.PasOnGetCellHint=FunctionForm(self._Warper_OnGetCellHint)
        self.OnGetCellHintPasObject=LCLBinding.set_Grids_TStringGrid_OnGetCellHint(self.pointer,self.PasOnGetCellHint,oldobj,FreeOldEvent)
    def getOnGetCellHint(self):
        return OnGetCellHintcall
    OnGetCellHint=property(getOnGetCellHint,setOnGetCellHint)
    def _Warper_OnGetCheckboxState(self,Sender,ACol,ARow,Value):
        self.OnGetCheckboxStatecall(LCLBindingUtil.GetPytonObject(Sender,TObject),ACol,ARow,Value)
    def setOnGetCheckboxState(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnGetCheckboxStatecall'):
            FreeOldEvent=1
            oldobj=OnGetCheckboxStatePasObject
        self.OnGetCheckboxStatecall=v 
        self.PasOnGetCheckboxState=FunctionForm(self._Warper_OnGetCheckboxState)
        self.OnGetCheckboxStatePasObject=LCLBinding.set_Grids_TStringGrid_OnGetCheckboxState(self.pointer,self.PasOnGetCheckboxState,oldobj,FreeOldEvent)
    def getOnGetCheckboxState(self):
        return OnGetCheckboxStatecall
    OnGetCheckboxState=property(getOnGetCheckboxState,setOnGetCheckboxState)
    def _Warper_OnSetCheckboxState(self,Sender,ACol,ARow,Value):
        self.OnSetCheckboxStatecall(LCLBindingUtil.GetPytonObject(Sender,TObject),ACol,ARow,Value)
    def setOnSetCheckboxState(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnSetCheckboxStatecall'):
            FreeOldEvent=1
            oldobj=OnSetCheckboxStatePasObject
        self.OnSetCheckboxStatecall=v 
        self.PasOnSetCheckboxState=FunctionForm(self._Warper_OnSetCheckboxState)
        self.OnSetCheckboxStatePasObject=LCLBinding.set_Grids_TStringGrid_OnSetCheckboxState(self.pointer,self.PasOnSetCheckboxState,oldobj,FreeOldEvent)
    def getOnSetCheckboxState(self):
        return OnSetCheckboxStatecall
    OnSetCheckboxState=property(getOnSetCheckboxState,setOnSetCheckboxState)
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
        self.OnTopLeftChangedPasObject=LCLBinding.set_Grids_TStringGrid_OnTopLeftChanged(self.pointer,self.PasOnTopLeftChanged,oldobj,FreeOldEvent)
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
        self.OnUserCheckboxBitmapPasObject=LCLBinding.set_Grids_TStringGrid_OnUserCheckboxBitmap(self.pointer,self.PasOnUserCheckboxBitmap,oldobj,FreeOldEvent)
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
        self.OnValidateEntryPasObject=LCLBinding.set_Grids_TStringGrid_OnValidateEntry(self.pointer,self.PasOnValidateEntry,oldobj,FreeOldEvent)
    def getOnValidateEntry(self):
        return OnValidateEntrycall
    OnValidateEntry=property(getOnValidateEntry,setOnValidateEntry)
#constructorGrids_TStringGrid_Create
    @staticmethod
    def Create(AOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.Grids_TStringGrid_Create((AOwner.pointer)),TStringGrid)
#class TStringGrid end
#class TDrawGrid start
class TDrawGrid(TCustomDrawGrid):
#    pointer=c_void_p()
    def __init__(self):#TDrawGrid
        TCustomDrawGrid.__init__(self)
    def getInplaceEditor(self):
        r=LCLBinding.get_Grids_TDrawGrid_InplaceEditor(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TWinControl)
    InplaceEditor=property(getInplaceEditor)
    def getAutoEdit(self):
        r=LCLBinding.get_Grids_TDrawGrid_AutoEdit(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setAutoEdit(self,v):
        LCLBinding.set_Grids_TDrawGrid_AutoEdit(self.pointer,v)
    AutoEdit=property(getAutoEdit,setAutoEdit)
    def getColumnClickSorts(self):
        r=LCLBinding.get_Grids_TDrawGrid_ColumnClickSorts(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setColumnClickSorts(self,v):
        LCLBinding.set_Grids_TDrawGrid_ColumnClickSorts(self.pointer,v)
    ColumnClickSorts=property(getColumnClickSorts,setColumnClickSorts)
    def getDragKind(self):
        r=LCLBinding.get_Grids_TDrawGrid_DragKind(self.pointer)
        return r
    def setDragKind(self,v):
        LCLBinding.set_Grids_TDrawGrid_DragKind(self.pointer,v.pointer)
    DragKind=property(getDragKind,setDragKind)
    def getDragMode(self):
        r=LCLBinding.get_Grids_TDrawGrid_DragMode(self.pointer)
        return r
    def setDragMode(self,v):
        LCLBinding.set_Grids_TDrawGrid_DragMode(self.pointer,v.pointer)
    DragMode=property(getDragMode,setDragMode)
    def getExtendedSelect(self):
        r=LCLBinding.get_Grids_TDrawGrid_ExtendedSelect(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setExtendedSelect(self,v):
        LCLBinding.set_Grids_TDrawGrid_ExtendedSelect(self.pointer,v)
    ExtendedSelect=property(getExtendedSelect,setExtendedSelect)
    def getHeaderHotZones(self):
        r=LCLBinding.get_Grids_TDrawGrid_HeaderHotZones(self.pointer)
        return r
    def setHeaderHotZones(self,v):
        LCLBinding.set_Grids_TDrawGrid_HeaderHotZones(self.pointer,v.pointer)
    HeaderHotZones=property(getHeaderHotZones,setHeaderHotZones)
    def getHeaderPushZones(self):
        r=LCLBinding.get_Grids_TDrawGrid_HeaderPushZones(self.pointer)
        return r
    def setHeaderPushZones(self,v):
        LCLBinding.set_Grids_TDrawGrid_HeaderPushZones(self.pointer,v.pointer)
    HeaderPushZones=property(getHeaderPushZones,setHeaderPushZones)
    def getMouseWheelOption(self):
        r=LCLBinding.get_Grids_TDrawGrid_MouseWheelOption(self.pointer)
        return r
    def setMouseWheelOption(self,v):
        LCLBinding.set_Grids_TDrawGrid_MouseWheelOption(self.pointer,v.pointer)
    MouseWheelOption=property(getMouseWheelOption,setMouseWheelOption)
    def getParentColor(self):
        r=LCLBinding.get_Grids_TDrawGrid_ParentColor(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentColor(self,v):
        LCLBinding.set_Grids_TDrawGrid_ParentColor(self.pointer,v)
    ParentColor=property(getParentColor,setParentColor)
    def getParentFont(self):
        r=LCLBinding.get_Grids_TDrawGrid_ParentFont(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setParentFont(self,v):
        LCLBinding.set_Grids_TDrawGrid_ParentFont(self.pointer,v)
    ParentFont=property(getParentFont,setParentFont)
    def getRangeSelectMode(self):
        r=LCLBinding.get_Grids_TDrawGrid_RangeSelectMode(self.pointer)
        return r
    def setRangeSelectMode(self,v):
        LCLBinding.set_Grids_TDrawGrid_RangeSelectMode(self.pointer,v.pointer)
    RangeSelectMode=property(getRangeSelectMode,setRangeSelectMode)
    def getTitleFont(self):
        r=LCLBinding.get_Grids_TDrawGrid_TitleFont(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TFont)
    def setTitleFont(self,v):
        LCLBinding.set_Grids_TDrawGrid_TitleFont(self.pointer,v.pointer)
    TitleFont=property(getTitleFont,setTitleFont)
    def getTitleImageList(self):
        r=LCLBinding.get_Grids_TDrawGrid_TitleImageList(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TImageList)
    def setTitleImageList(self,v):
        LCLBinding.set_Grids_TDrawGrid_TitleImageList(self.pointer,v.pointer)
    TitleImageList=property(getTitleImageList,setTitleImageList)
    def getTitleStyle(self):
        r=LCLBinding.get_Grids_TDrawGrid_TitleStyle(self.pointer)
        return r
    def setTitleStyle(self,v):
        LCLBinding.set_Grids_TDrawGrid_TitleStyle(self.pointer,v.pointer)
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
        self.OnCheckboxToggledPasObject=LCLBinding.set_Grids_TDrawGrid_OnCheckboxToggled(self.pointer,self.PasOnCheckboxToggled,oldobj,FreeOldEvent)
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
        self.OnEditingDonePasObject=LCLBinding.set_Grids_TDrawGrid_OnEditingDone(self.pointer,self.PasOnEditingDone,oldobj,FreeOldEvent)
    def getOnEditingDone(self):
        return OnEditingDonecall
    OnEditingDone=property(getOnEditingDone,setOnEditingDone)
    def _Warper_OnGetCellHint(self,Sender,ACol,ARow,HintText):
        self.OnGetCellHintcall(LCLBindingUtil.GetPytonObject(Sender,TObject),ACol,ARow,HintText)
    def setOnGetCellHint(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int,c_int,c_char_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnGetCellHintcall'):
            FreeOldEvent=1
            oldobj=OnGetCellHintPasObject
        self.OnGetCellHintcall=v 
        self.PasOnGetCellHint=FunctionForm(self._Warper_OnGetCellHint)
        self.OnGetCellHintPasObject=LCLBinding.set_Grids_TDrawGrid_OnGetCellHint(self.pointer,self.PasOnGetCellHint,oldobj,FreeOldEvent)
    def getOnGetCellHint(self):
        return OnGetCellHintcall
    OnGetCellHint=property(getOnGetCellHint,setOnGetCellHint)
    def _Warper_OnGetCheckboxState(self,Sender,ACol,ARow,Value):
        self.OnGetCheckboxStatecall(LCLBindingUtil.GetPytonObject(Sender,TObject),ACol,ARow,Value)
    def setOnGetCheckboxState(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnGetCheckboxStatecall'):
            FreeOldEvent=1
            oldobj=OnGetCheckboxStatePasObject
        self.OnGetCheckboxStatecall=v 
        self.PasOnGetCheckboxState=FunctionForm(self._Warper_OnGetCheckboxState)
        self.OnGetCheckboxStatePasObject=LCLBinding.set_Grids_TDrawGrid_OnGetCheckboxState(self.pointer,self.PasOnGetCheckboxState,oldobj,FreeOldEvent)
    def getOnGetCheckboxState(self):
        return OnGetCheckboxStatecall
    OnGetCheckboxState=property(getOnGetCheckboxState,setOnGetCheckboxState)
    def _Warper_OnSetCheckboxState(self,Sender,ACol,ARow,Value):
        self.OnSetCheckboxStatecall(LCLBindingUtil.GetPytonObject(Sender,TObject),ACol,ARow,Value)
    def setOnSetCheckboxState(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p,c_int,c_int,c_int)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnSetCheckboxStatecall'):
            FreeOldEvent=1
            oldobj=OnSetCheckboxStatePasObject
        self.OnSetCheckboxStatecall=v 
        self.PasOnSetCheckboxState=FunctionForm(self._Warper_OnSetCheckboxState)
        self.OnSetCheckboxStatePasObject=LCLBinding.set_Grids_TDrawGrid_OnSetCheckboxState(self.pointer,self.PasOnSetCheckboxState,oldobj,FreeOldEvent)
    def getOnSetCheckboxState(self):
        return OnSetCheckboxStatecall
    OnSetCheckboxState=property(getOnSetCheckboxState,setOnSetCheckboxState)
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
        self.OnUserCheckboxBitmapPasObject=LCLBinding.set_Grids_TDrawGrid_OnUserCheckboxBitmap(self.pointer,self.PasOnUserCheckboxBitmap,oldobj,FreeOldEvent)
    def getOnUserCheckboxBitmap(self):
        return OnUserCheckboxBitmapcall
    OnUserCheckboxBitmap=property(getOnUserCheckboxBitmap,setOnUserCheckboxBitmap)
#constructorGrids_TDrawGrid_Create
    @staticmethod
    def Create(AOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.Grids_TDrawGrid_Create((AOwner.pointer)),TDrawGrid)
#class TDrawGrid end
