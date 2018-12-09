library lclexports;


  {$mode objfpc}{$H+}


uses
Interfaces,    // Necessary to create the widgetset object

  Classes,
controls,LCLClasses,Forms,ActnList,StdCtrls,Graphics,Menus,GraphType,ImgList,ExtCtrls,Dialogs,  Buttons,
   MaskEdit, CheckLst, Grids, PairSplitter, ColorBox,
  ValEdit,Loadlfmunit;

type
Classes_TNotifyEvent=procedure(Sender:tobject);cdecl;
Controls_TDragDropEvent=procedure(Sender:tobject;Source:tobject;X:Integer;Y:Integer);cdecl;
Controls_TDragOverEvent=procedure(Sender:tobject;Source:tobject;X:Integer;Y:Integer;State:Integer;Accept:Integer);cdecl;
Controls_TEndDragEvent=procedure(Sender:tobject;Target:tobject;X:Integer;Y:Integer);cdecl;
Controls_TMouseEvent=procedure(Sender:tobject;Button:Integer;Shift:Integer;X:Integer;Y:Integer);cdecl;
Controls_TMouseMoveEvent=procedure(Sender:tobject;Shift:Integer;X:Integer;Y:Integer);cdecl;
Controls_TStartDockEvent=procedure(Sender:tobject;DragObject:tdragdockobject);cdecl;
Controls_TStartDragEvent=procedure(Sender:tobject;DragObject:tdragobject);cdecl;
Menus_TMenuMeasureItemEvent=procedure(Sender:tobject;ACanvas:tcanvas;AWidth:Integer;AHeight:Integer);cdecl;
Menus_TMenuChangeEvent=procedure(Sender:tobject;Source:tmenuitem;Rebuild:Integer);cdecl;
Controls_TGetDockCaptionEvent=procedure(Sender:tobject;AControl:tcontrol;ACaption:PChar);cdecl;
Controls_TDockDropEvent=procedure(Sender:tobject;Source:tdragdockobject;X:Integer;Y:Integer);cdecl;
Controls_TDockOverEvent=procedure(Sender:tobject;Source:tdragdockobject;X:Integer;Y:Integer;State:Integer;Accept:Integer);cdecl;
Forms_TCloseEvent=procedure(Sender:tobject;CloseAction:Integer);cdecl;
Forms_TCloseQueryEvent=procedure(Sender:tobject;CanClose:Integer);cdecl;
Forms_TModalDialogFinished=procedure(Sender:tobject;AResult:Integer);cdecl;
StdCtrls_TMeasureItemEvent=procedure(Control:twincontrol;Index:Integer;AHeight:Integer);cdecl;
StdCtrls_TSelectionChangeEvent=procedure(Sender:tobject;User:Integer);cdecl;
StdCtrls_TScrollEvent=procedure(Sender:tobject;ScrollCode:Integer;ScrollPos:Integer);cdecl;
Forms_TIdleEvent=procedure(Sender:tobject;Done:Integer);cdecl;
Forms_TQueryEndSessionEvent=procedure(Cancel:Integer);cdecl;
CheckLst_TCheckListClicked=procedure(Sender:tobject;Index:Integer);cdecl;
ExtCtrls_TBandDragEvent=procedure(Sender:tobject;Control:tcontrol;Drag:Integer);cdecl;
ExtCtrls_TCanResizeEvent=procedure(Sender:tobject;NewSize:Integer;Accept:Integer);cdecl;
Grids_TOnSelectEvent=procedure(Sender:tobject;aCol:Integer;aRow:Integer);cdecl;
Grids_TToggledCheckboxEvent=procedure(sender:tobject;aCol:Integer;aRow:Integer;aState:Integer);cdecl;
Grids_TOnCompareCells=procedure(Sender:tobject;ACol:Integer;ARow:Integer;BCol:Integer;BRow:Integer;Result:Integer);cdecl;
Grids_TOnPrepareCanvasEvent=procedure(sender:tobject;aCol:Integer;aRow:Integer;aState:Integer);cdecl;
Grids_TSelectEditorEvent=procedure(Sender:tobject;aCol:Integer;aRow:Integer;Editor:twincontrol);cdecl;
Grids_TUserCheckBoxBitmapEvent=procedure(Sender:tobject;aCol:Integer;aRow:Integer;CheckedState:Integer;ABitmap:tbitmap);cdecl;
Grids_TValidateEntryEvent=procedure(sender:tobject;aCol:Integer;aRow:Integer;OldValue:PChar;NewValue:PChar);cdecl;
Grids_TGetCellHintEvent=procedure(Sender:tobject;ACol:Integer;ARow:Integer;HintText:PChar);cdecl;
Grids_TGetCheckboxStateEvent=procedure(Sender:tobject;ACol:Integer;ARow:Integer;Value:Integer);cdecl;
Grids_TSetCheckboxStateEvent=procedure(Sender:tobject;ACol:Integer;ARow:Integer;Value:Integer);cdecl;
Grids_TGridOperationEvent=procedure(Sender:tobject;IsColumn:Integer;sIndex:Integer;tIndex:Integer);cdecl;
Grids_TGetEditEvent=procedure(Sender:tobject;ACol:Integer;ARow:Integer;Value:PChar);cdecl;
Grids_THdrEvent=procedure(Sender:tobject;IsColumn:Integer;Index:Integer);cdecl;
Grids_THeaderSizingEvent=procedure(sender:tobject;IsColumn:Integer;aIndex:Integer;aSize:Integer);cdecl;
Grids_TOnSelectCellEvent=procedure(Sender:tobject;aCol:Integer;aRow:Integer;CanSelect:Integer);cdecl;
Grids_TSetEditEvent=procedure(Sender:tobject;ACol:Integer;ARow:Integer;Value:PChar);cdecl;
ExtCtrls_TCanOffsetEvent=procedure(Sender:tobject;NewOffset:Integer;Accept:Integer);cdecl;
Grids_TCellProcessEvent=procedure(Sender:tobject;aCol:Integer;aRow:Integer;processType:Integer;aValue:PChar);cdecl;
ValEdit_TGetPickListEvent=procedure(Sender:tobject;KeyName:PChar;Values:tstrings);cdecl;
ClassesTNotifyEvent_wrapper=class
C:Classes_TNotifyEvent;
procedure call(Sender:TObject);
end;
ControlsTDragDropEvent_wrapper=class
C:Controls_TDragDropEvent;
procedure call(Sender:TObject;Source:TObject;X:Integer;Y:Integer);
end;
ControlsTDragOverEvent_wrapper=class
C:Controls_TDragOverEvent;
procedure call(Sender:TObject;Source:TObject;X:Integer;Y:Integer;State:TDragState;var Accept:Boolean);
end;
ControlsTEndDragEvent_wrapper=class
C:Controls_TEndDragEvent;
procedure call(Sender:TObject;Target:TObject;X:Integer;Y:Integer);
end;
ControlsTMouseEvent_wrapper=class
C:Controls_TMouseEvent;
procedure call(Sender:TObject;Button:TMouseButton;Shift:TShiftState;X:Integer;Y:Integer);
end;
ControlsTMouseMoveEvent_wrapper=class
C:Controls_TMouseMoveEvent;
procedure call(Sender:TObject;Shift:TShiftState;X:Integer;Y:Integer);
end;
ControlsTStartDockEvent_wrapper=class
C:Controls_TStartDockEvent;
procedure call(Sender:TObject;var DragObject:TDragDockObject);
end;
ControlsTStartDragEvent_wrapper=class
C:Controls_TStartDragEvent;
procedure call(Sender:TObject;var DragObject:TDragObject);
end;
MenusTMenuMeasureItemEvent_wrapper=class
C:Menus_TMenuMeasureItemEvent;
procedure call(Sender:TObject;ACanvas:TCanvas;var AWidth:Integer;var AHeight:Integer);
end;
MenusTMenuChangeEvent_wrapper=class
C:Menus_TMenuChangeEvent;
procedure call(Sender:TObject;Source:TMenuItem;Rebuild:Boolean);
end;
ControlsTGetDockCaptionEvent_wrapper=class
C:Controls_TGetDockCaptionEvent;
procedure call(Sender:TObject;AControl:TControl;var ACaption:string);
end;
ControlsTDockDropEvent_wrapper=class
C:Controls_TDockDropEvent;
procedure call(Sender:TObject;Source:TDragDockObject;X:Integer;Y:Integer);
end;
ControlsTDockOverEvent_wrapper=class
C:Controls_TDockOverEvent;
procedure call(Sender:TObject;Source:TDragDockObject;X:Integer;Y:Integer;State:TDragState;var Accept:Boolean);
end;
FormsTCloseEvent_wrapper=class
C:Forms_TCloseEvent;
procedure call(Sender:TObject;var CloseAction:TCloseAction);
end;
FormsTCloseQueryEvent_wrapper=class
C:Forms_TCloseQueryEvent;
procedure call(Sender:TObject;var CanClose:Boolean);
end;
FormsTModalDialogFinished_wrapper=class
C:Forms_TModalDialogFinished;
procedure call(Sender:TObject;AResult:Integer);
end;
StdCtrlsTMeasureItemEvent_wrapper=class
C:StdCtrls_TMeasureItemEvent;
procedure call(Control:TWinControl;Index:Integer;var AHeight:Integer);
end;
StdCtrlsTSelectionChangeEvent_wrapper=class
C:StdCtrls_TSelectionChangeEvent;
procedure call(Sender:TObject;User:Boolean);
end;
StdCtrlsTScrollEvent_wrapper=class
C:StdCtrls_TScrollEvent;
procedure call(Sender:TObject;ScrollCode:TScrollCode;var ScrollPos:Integer);
end;
FormsTIdleEvent_wrapper=class
C:Forms_TIdleEvent;
procedure call(Sender:TObject;var Done:Boolean);
end;
FormsTQueryEndSessionEvent_wrapper=class
C:Forms_TQueryEndSessionEvent;
procedure call(var Cancel:Boolean);
end;
CheckLstTCheckListClicked_wrapper=class
C:CheckLst_TCheckListClicked;
procedure call(Sender:TObject;Index:Integer);
end;
ExtCtrlsTBandDragEvent_wrapper=class
C:ExtCtrls_TBandDragEvent;
procedure call(Sender:TObject;Control:TControl;var Drag:Boolean);
end;
ExtCtrlsTCanResizeEvent_wrapper=class
C:ExtCtrls_TCanResizeEvent;
procedure call(Sender:TObject;var NewSize:Integer;var Accept:Boolean);
end;
GridsTOnSelectEvent_wrapper=class
C:Grids_TOnSelectEvent;
procedure call(Sender:TObject;aCol:Integer;aRow:Integer);
end;
GridsTToggledCheckboxEvent_wrapper=class
C:Grids_TToggledCheckboxEvent;
procedure call(sender:TObject;aCol:Integer;aRow:Integer;aState:TCheckboxState);
end;
GridsTOnCompareCells_wrapper=class
C:Grids_TOnCompareCells;
procedure call(Sender:TObject;ACol:Integer;ARow:Integer;BCol:Integer;BRow:Integer;var Result:Integer);
end;
GridsTOnPrepareCanvasEvent_wrapper=class
C:Grids_TOnPrepareCanvasEvent;
procedure call(sender:TObject;aCol:Integer;aRow:Integer;aState:TGridDrawState);
end;
GridsTSelectEditorEvent_wrapper=class
C:Grids_TSelectEditorEvent;
procedure call(Sender:TObject;aCol:Integer;aRow:Integer;var Editor:TWinControl);
end;
GridsTUserCheckBoxBitmapEvent_wrapper=class
C:Grids_TUserCheckBoxBitmapEvent;
procedure call(Sender:TObject;const aCol:Integer;const aRow:Integer;const CheckedState:TCheckboxState;var ABitmap:TBitmap);
end;
GridsTValidateEntryEvent_wrapper=class
C:Grids_TValidateEntryEvent;
procedure call(sender:TObject;aCol:Integer;aRow:Integer;const OldValue:string;var NewValue:string);
end;
GridsTGetCellHintEvent_wrapper=class
C:Grids_TGetCellHintEvent;
procedure call(Sender:TObject;ACol:Integer;ARow:Integer;var HintText:string);
end;
GridsTGetCheckboxStateEvent_wrapper=class
C:Grids_TGetCheckboxStateEvent;
procedure call(Sender:TObject;ACol:Integer;ARow:Integer;var Value:TCheckboxState);
end;
GridsTSetCheckboxStateEvent_wrapper=class
C:Grids_TSetCheckboxStateEvent;
procedure call(Sender:TObject;ACol:Integer;ARow:Integer;const Value:TCheckboxState);
end;
GridsTGridOperationEvent_wrapper=class
C:Grids_TGridOperationEvent;
procedure call(Sender:TObject;IsColumn:Boolean;sIndex:Integer;tIndex:Integer);
end;
GridsTGetEditEvent_wrapper=class
C:Grids_TGetEditEvent;
procedure call(Sender:TObject;ACol:Integer;ARow:Integer;var Value:string);
end;
GridsTHdrEvent_wrapper=class
C:Grids_THdrEvent;
procedure call(Sender:TObject;IsColumn:Boolean;Index:Integer);
end;
GridsTHeaderSizingEvent_wrapper=class
C:Grids_THeaderSizingEvent;
procedure call(sender:TObject;const IsColumn:Boolean;const aIndex:Integer;const aSize:Integer);
end;
GridsTOnSelectCellEvent_wrapper=class
C:Grids_TOnSelectCellEvent;
procedure call(Sender:TObject;aCol:Integer;aRow:Integer;var CanSelect:Boolean);
end;
GridsTSetEditEvent_wrapper=class
C:Grids_TSetEditEvent;
procedure call(Sender:TObject;ACol:Integer;ARow:Integer;const Value:string);
end;
ExtCtrlsTCanOffsetEvent_wrapper=class
C:ExtCtrls_TCanOffsetEvent;
procedure call(Sender:TObject;var NewOffset:Integer;var Accept:Boolean);
end;
GridsTCellProcessEvent_wrapper=class
C:Grids_TCellProcessEvent;
procedure call(Sender:TObject;aCol:Integer;aRow:Integer;processType:TCellProcessType;var aValue:string);
end;
ValEditTGetPickListEvent_wrapper=class
C:ValEdit_TGetPickListEvent;
procedure call(Sender:TObject;const KeyName:string;Values:TStrings);
end;
function BooleanTointegert(b:Boolean):Integer;
 begin
   if b then
   Result:=1 else
     Result:=0;
 end;
function integertToBoolean(i:Integer):Boolean;
begin
  if i=1 then
  Result:=True
  else
    Result:=False;
end;  
procedure Forms_Application_Initialize;cdecl;
begin
Application.Initialize; 
end;
procedure Forms_Application_Run;cdecl; 
begin
Application.Run; 
end;
function Forms_Application_CreateForm:TForm;cdecl; 
begin
 Application.CreateForm(TForm, Result);
end;
function Forms_Application_CreateFormLFM(FileName,FormClassName: PChar): PChar; cdecl;
  var
    LFM: Loadlfm;
    F: TForm;
  begin
    LFM := Loadlfmunit.Loadlfm.Create;
    Result := LFM.LoadFromText(
      'G:\dev\temp\lclbinding2\parser\generated\python\test\lfmtest\unit1.lfm');
   // Application.UpdateMainForm(F);
    Lfm.Free;
  end;     
//property getterClasses_TComponent_Components
function get_Classes_TComponent_Components(p:TComponent;Index:Integer):tcomponent;cdecl;
begin
Result:=tcomponent(p.Components[Index]);
end;
//property getterClasses_TComponent_ComponentCount
function get_Classes_TComponent_ComponentCount(p:TComponent):Integer;cdecl;
begin
Result:=Integer(p.ComponentCount);
end;
//property getterClasses_TComponent_ComponentIndex
function get_Classes_TComponent_ComponentIndex(p:TComponent):Integer;cdecl;
begin
Result:=Integer(p.ComponentIndex);
end;
//property setterClasses_TComponent_ComponentIndex
procedure set_Classes_TComponent_ComponentIndex(p:TComponent;v:Integer);cdecl; 
begin
p.ComponentIndex:=(v);
end;
//property getterClasses_TComponent_ComponentState
function get_Classes_TComponent_ComponentState(p:TComponent):Integer;cdecl;
begin
Result:=Integer(p.ComponentState);
end;
//property getterClasses_TComponent_ComponentStyle
function get_Classes_TComponent_ComponentStyle(p:TComponent):Integer;cdecl;
begin
Result:=Integer(p.ComponentStyle);
end;
//property getterClasses_TComponent_Owner
function get_Classes_TComponent_Owner(p:TComponent):tcomponent;cdecl;
begin
Result:=tcomponent(p.Owner);
end;
//constructorLCLClasses_TLCLComponent_Create
function LCLClasses_TLCLComponent_Create(TheOwner:tcomponent):TLCLComponent;cdecl;
begin
Result:=TLCLComponent.Create((TheOwner));
end;
//property getterLCLClasses_TLCLComponent_LCLRefCount
function get_LCLClasses_TLCLComponent_LCLRefCount(p:TLCLComponent):Integer;cdecl;
begin
Result:=Integer(p.LCLRefCount);
end;
//constructorClasses_TBasicActionLink_Create
function Classes_TBasicActionLink_Create(AClient:tobject):TBasicActionLink;cdecl;
begin
Result:=TBasicActionLink.Create((AClient));
end;
//constructorClasses_TBasicAction_Create
function Classes_TBasicAction_Create(AOwner:tcomponent):TBasicAction;cdecl;
begin
Result:=TBasicAction.Create((AOwner));
end;
//property getterClasses_TBasicAction_ActionComponent
function get_Classes_TBasicAction_ActionComponent(p:TBasicAction):tcomponent;cdecl;
begin
Result:=tcomponent(p.ActionComponent);
end;
//property setterClasses_TBasicAction_ActionComponent
procedure set_Classes_TBasicAction_ActionComponent(p:TBasicAction;v:tcomponent);cdecl; 
begin
p.ActionComponent:=(v);
end;
//property setterClasses_TBasicAction_OnExecute
function set_Classes_TBasicAction_OnExecute(p:TBasicAction;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnExecute:=@callClass.call;
Result:=callClass;
end;
//property setterClasses_TBasicAction_OnUpdate
function set_Classes_TBasicAction_OnUpdate(p:TBasicAction;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnUpdate:=@callClass.call;
Result:=callClass;
end;
//property getterClasses_TBasicActionLink_Action
function get_Classes_TBasicActionLink_Action(p:TBasicActionLink):tbasicaction;cdecl;
begin
Result:=tbasicaction(p.Action);
end;
//property setterClasses_TBasicActionLink_Action
procedure set_Classes_TBasicActionLink_Action(p:TBasicActionLink;v:tbasicaction);cdecl; 
begin
p.Action:=(v);
end;
//property setterClasses_TBasicActionLink_OnChange
function set_Classes_TBasicActionLink_OnChange(p:TBasicActionLink;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnChange:=@callClass.call;
Result:=callClass;
end;
//constructorActnList_TActionLink_Create
function ActnList_TActionLink_Create(AClient:tobject):TActionLink;cdecl;
begin
Result:=TActionLink.Create((AClient));
end;
//constructorControls_TControlActionLink_Create
function Controls_TControlActionLink_Create(AClient:tobject):TControlActionLink;cdecl;
begin
Result:=TControlActionLink.Create((AClient));
end;
//property getterControls_TDragObject_AlwaysShowDragImages
function get_Controls_TDragObject_AlwaysShowDragImages(p:TDragObject):Integer;cdecl;
begin
Result:=BooleanTointegert(p.AlwaysShowDragImages);
end;
//property setterControls_TDragObject_AlwaysShowDragImages
procedure set_Controls_TDragObject_AlwaysShowDragImages(p:TDragObject;v:Integer);cdecl; 
begin
p.AlwaysShowDragImages:=integertToBoolean(v);
end;
//property getterControls_TDragObject_AutoCreated
function get_Controls_TDragObject_AutoCreated(p:TDragObject):Integer;cdecl;
begin
Result:=BooleanTointegert(p.AutoCreated);
end;
//property getterControls_TDragObject_AutoFree
function get_Controls_TDragObject_AutoFree(p:TDragObject):Integer;cdecl;
begin
Result:=BooleanTointegert(p.AutoFree);
end;
//property getterControls_TDragObject_Control
function get_Controls_TDragObject_Control(p:TDragObject):tcontrol;cdecl;
begin
Result:=tcontrol(p.Control);
end;
//property setterControls_TDragObject_Control
procedure set_Controls_TDragObject_Control(p:TDragObject;v:tcontrol);cdecl; 
begin
p.Control:=(v);
end;
//property getterControls_TDragObject_DragTarget
function get_Controls_TDragObject_DragTarget(p:TDragObject):tcontrol;cdecl;
begin
Result:=tcontrol(p.DragTarget);
end;
//property setterControls_TDragObject_DragTarget
procedure set_Controls_TDragObject_DragTarget(p:TDragObject;v:tcontrol);cdecl; 
begin
p.DragTarget:=(v);
end;
//property getterControls_TDragObject_Dropped
function get_Controls_TDragObject_Dropped(p:TDragObject):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Dropped);
end;
//property getterControls_TDragDockObject_DropAlign
function get_Controls_TDragDockObject_DropAlign(p:TDragDockObject):Integer;cdecl;
begin
Result:=Integer(p.DropAlign);
end;
//property setterControls_TDragDockObject_DropAlign
procedure set_Controls_TDragDockObject_DropAlign(p:TDragDockObject;v:talign);cdecl; 
begin
p.DropAlign:=(v);
end;
//property getterControls_TDragDockObject_DropOnControl
function get_Controls_TDragDockObject_DropOnControl(p:TDragDockObject):tcontrol;cdecl;
begin
Result:=tcontrol(p.DropOnControl);
end;
//property setterControls_TDragDockObject_DropOnControl
procedure set_Controls_TDragDockObject_DropOnControl(p:TDragDockObject;v:tcontrol);cdecl; 
begin
p.DropOnControl:=(v);
end;
//property getterControls_TDragDockObject_Floating
function get_Controls_TDragDockObject_Floating(p:TDragDockObject):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Floating);
end;
//property setterControls_TDragDockObject_Floating
procedure set_Controls_TDragDockObject_Floating(p:TDragDockObject;v:Integer);cdecl; 
begin
p.Floating:=integertToBoolean(v);
end;
//property getterControls_TDragDockObject_IncreaseDockArea
function get_Controls_TDragDockObject_IncreaseDockArea(p:TDragDockObject):Integer;cdecl;
begin
Result:=BooleanTointegert(p.IncreaseDockArea);
end;
//property getterControls_TControl_AnchoredControls
function get_Controls_TControl_AnchoredControls(p:TControl;Index:Integer):tcontrol;cdecl;
begin
Result:=tcontrol(p.AnchoredControls[Index]);
end;
//constructorControls_TControl_Create
function Controls_TControl_Create(TheOwner:tcomponent):TControl;cdecl;
begin
Result:=TControl.Create((TheOwner));
end;
//property getterControls_TControl_AccessibleDescription
function get_Controls_TControl_AccessibleDescription(p:TControl):PChar;cdecl;
begin
Result:=PChar(p.AccessibleDescription);
end;
//property setterControls_TControl_AccessibleDescription
procedure set_Controls_TControl_AccessibleDescription(p:TControl;v:PChar);cdecl; 
begin
p.AccessibleDescription:=(v);
end;
//property getterControls_TControl_AccessibleValue
function get_Controls_TControl_AccessibleValue(p:TControl):PChar;cdecl;
begin
Result:=PChar(p.AccessibleValue);
end;
//property setterControls_TControl_AccessibleValue
procedure set_Controls_TControl_AccessibleValue(p:TControl;v:PChar);cdecl; 
begin
p.AccessibleValue:=(v);
end;
//property getterControls_TControl_AccessibleRole
function get_Controls_TControl_AccessibleRole(p:TControl):Integer;cdecl;
begin
Result:=Integer(p.AccessibleRole);
end;
//property setterControls_TControl_AccessibleRole
procedure set_Controls_TControl_AccessibleRole(p:TControl;v:tlazaccessibilityrole);cdecl; 
begin
p.AccessibleRole:=(v);
end;
//property getterControls_TControl_Action
function get_Controls_TControl_Action(p:TControl):tbasicaction;cdecl;
begin
Result:=tbasicaction(p.Action);
end;
//property setterControls_TControl_Action
procedure set_Controls_TControl_Action(p:TControl;v:tbasicaction);cdecl; 
begin
p.Action:=(v);
end;
//property getterControls_TControl_Align
function get_Controls_TControl_Align(p:TControl):Integer;cdecl;
begin
Result:=Integer(p.Align);
end;
//property setterControls_TControl_Align
procedure set_Controls_TControl_Align(p:TControl;v:talign);cdecl; 
begin
p.Align:=(v);
end;
//property getterControls_TControl_Anchors
function get_Controls_TControl_Anchors(p:TControl):Integer;cdecl;
begin
Result:=Integer(p.Anchors);
end;
//property setterControls_TControl_Anchors
procedure set_Controls_TControl_Anchors(p:TControl;v:tanchors);cdecl; 
begin
p.Anchors:=(v);
end;
//property getterControls_TAnchorSide_Owner
function get_Controls_TAnchorSide_Owner(p:TAnchorSide):tcontrol;cdecl;
begin
Result:=tcontrol(p.Owner);
end;
//property getterControls_TAnchorSide_Kind
function get_Controls_TAnchorSide_Kind(p:TAnchorSide):Integer;cdecl;
begin
Result:=Integer(p.Kind);
end;
//property getterControls_TAnchorSide_Control
function get_Controls_TAnchorSide_Control(p:TAnchorSide):tcontrol;cdecl;
begin
Result:=tcontrol(p.Control);
end;
//property setterControls_TAnchorSide_Control
procedure set_Controls_TAnchorSide_Control(p:TAnchorSide;v:tcontrol);cdecl; 
begin
p.Control:=(v);
end;
//property getterControls_TAnchorSide_Side
function get_Controls_TAnchorSide_Side(p:TAnchorSide):Integer;cdecl;
begin
Result:=Integer(p.Side);
end;
//property setterControls_TAnchorSide_Side
procedure set_Controls_TAnchorSide_Side(p:TAnchorSide;v:tanchorsidereference);cdecl; 
begin
p.Side:=(v);
end;
//property getterControls_TControl_AutoSize
function get_Controls_TControl_AutoSize(p:TControl):Integer;cdecl;
begin
Result:=BooleanTointegert(p.AutoSize);
end;
//property setterControls_TControl_AutoSize
procedure set_Controls_TControl_AutoSize(p:TControl;v:Integer);cdecl; 
begin
p.AutoSize:=integertToBoolean(v);
end;
//property getterControls_TControlBorderSpacing_Control
function get_Controls_TControlBorderSpacing_Control(p:TControlBorderSpacing):tcontrol;cdecl;
begin
Result:=tcontrol(p.Control);
end;
//property getterControls_TControlBorderSpacing_AroundLeft
function get_Controls_TControlBorderSpacing_AroundLeft(p:TControlBorderSpacing):Integer;cdecl;
begin
Result:=Integer(p.AroundLeft);
end;
//property getterControls_TControlBorderSpacing_AroundTop
function get_Controls_TControlBorderSpacing_AroundTop(p:TControlBorderSpacing):Integer;cdecl;
begin
Result:=Integer(p.AroundTop);
end;
//property getterControls_TControlBorderSpacing_AroundRight
function get_Controls_TControlBorderSpacing_AroundRight(p:TControlBorderSpacing):Integer;cdecl;
begin
Result:=Integer(p.AroundRight);
end;
//property getterControls_TControlBorderSpacing_AroundBottom
function get_Controls_TControlBorderSpacing_AroundBottom(p:TControlBorderSpacing):Integer;cdecl;
begin
Result:=Integer(p.AroundBottom);
end;
//property getterControls_TControlBorderSpacing_ControlLeft
function get_Controls_TControlBorderSpacing_ControlLeft(p:TControlBorderSpacing):Integer;cdecl;
begin
Result:=Integer(p.ControlLeft);
end;
//property getterControls_TControlBorderSpacing_ControlTop
function get_Controls_TControlBorderSpacing_ControlTop(p:TControlBorderSpacing):Integer;cdecl;
begin
Result:=Integer(p.ControlTop);
end;
//property getterControls_TControlBorderSpacing_ControlWidth
function get_Controls_TControlBorderSpacing_ControlWidth(p:TControlBorderSpacing):Integer;cdecl;
begin
Result:=Integer(p.ControlWidth);
end;
//property getterControls_TControlBorderSpacing_ControlHeight
function get_Controls_TControlBorderSpacing_ControlHeight(p:TControlBorderSpacing):Integer;cdecl;
begin
Result:=Integer(p.ControlHeight);
end;
//property getterControls_TControlBorderSpacing_ControlRight
function get_Controls_TControlBorderSpacing_ControlRight(p:TControlBorderSpacing):Integer;cdecl;
begin
Result:=Integer(p.ControlRight);
end;
//property getterControls_TControlBorderSpacing_ControlBottom
function get_Controls_TControlBorderSpacing_ControlBottom(p:TControlBorderSpacing):Integer;cdecl;
begin
Result:=Integer(p.ControlBottom);
end;
//property setterControls_TControlBorderSpacing_OnChange
function set_Controls_TControlBorderSpacing_OnChange(p:TControlBorderSpacing;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnChange:=@callClass.call;
Result:=callClass;
end;
//property getterControls_TControlBorderSpacing_InnerBorder
function get_Controls_TControlBorderSpacing_InnerBorder(p:TControlBorderSpacing):Integer;cdecl;
begin
Result:=Integer(p.InnerBorder);
end;
//property setterControls_TControlBorderSpacing_InnerBorder
procedure set_Controls_TControlBorderSpacing_InnerBorder(p:TControlBorderSpacing;v:Integer);cdecl; 
begin
p.InnerBorder:=(v);
end;
//property getterControls_TControlBorderSpacing_CellAlignHorizontal
function get_Controls_TControlBorderSpacing_CellAlignHorizontal(p:TControlBorderSpacing):Integer;cdecl;
begin
Result:=Integer(p.CellAlignHorizontal);
end;
//property setterControls_TControlBorderSpacing_CellAlignHorizontal
procedure set_Controls_TControlBorderSpacing_CellAlignHorizontal(p:TControlBorderSpacing;v:tcontrolcellalign);cdecl; 
begin
p.CellAlignHorizontal:=(v);
end;
//property getterControls_TControlBorderSpacing_CellAlignVertical
function get_Controls_TControlBorderSpacing_CellAlignVertical(p:TControlBorderSpacing):Integer;cdecl;
begin
Result:=Integer(p.CellAlignVertical);
end;
//property setterControls_TControlBorderSpacing_CellAlignVertical
procedure set_Controls_TControlBorderSpacing_CellAlignVertical(p:TControlBorderSpacing;v:tcontrolcellalign);cdecl; 
begin
p.CellAlignVertical:=(v);
end;
//property getterControls_TControl_BorderSpacing
function get_Controls_TControl_BorderSpacing(p:TControl):tcontrolborderspacing;cdecl;
begin
Result:=tcontrolborderspacing(p.BorderSpacing);
end;
//property setterControls_TControl_BorderSpacing
procedure set_Controls_TControl_BorderSpacing(p:TControl;v:tcontrolborderspacing);cdecl; 
begin
p.BorderSpacing:=(v);
end;
//property getterControls_TControl_Caption
function get_Controls_TControl_Caption(p:TControl):PChar;cdecl;
begin
Result:=PChar(p.Caption);
end;
//property setterControls_TControl_Caption
procedure set_Controls_TControl_Caption(p:TControl;v:PChar);cdecl; 
begin
p.Caption:=(v);
end;
//property getterControls_TControl_CaptureMouseButtons
function get_Controls_TControl_CaptureMouseButtons(p:TControl):Integer;cdecl;
begin
Result:=Integer(p.CaptureMouseButtons);
end;
//property setterControls_TControl_CaptureMouseButtons
procedure set_Controls_TControl_CaptureMouseButtons(p:TControl;v:tcapturemousebuttons);cdecl; 
begin
p.CaptureMouseButtons:=(v);
end;
//property getterControls_TControl_ClientHeight
function get_Controls_TControl_ClientHeight(p:TControl):Integer;cdecl;
begin
Result:=Integer(p.ClientHeight);
end;
//property setterControls_TControl_ClientHeight
procedure set_Controls_TControl_ClientHeight(p:TControl;v:Integer);cdecl; 
begin
p.ClientHeight:=(v);
end;
//property getterControls_TControl_ClientWidth
function get_Controls_TControl_ClientWidth(p:TControl):Integer;cdecl;
begin
Result:=Integer(p.ClientWidth);
end;
//property setterControls_TControl_ClientWidth
procedure set_Controls_TControl_ClientWidth(p:TControl;v:Integer);cdecl; 
begin
p.ClientWidth:=(v);
end;
//property getterControls_TSizeConstraints_MaxInterfaceHeight
function get_Controls_TSizeConstraints_MaxInterfaceHeight(p:TSizeConstraints):Integer;cdecl;
begin
Result:=Integer(p.MaxInterfaceHeight);
end;
//property getterControls_TSizeConstraints_MaxInterfaceWidth
function get_Controls_TSizeConstraints_MaxInterfaceWidth(p:TSizeConstraints):Integer;cdecl;
begin
Result:=Integer(p.MaxInterfaceWidth);
end;
//property getterControls_TSizeConstraints_MinInterfaceHeight
function get_Controls_TSizeConstraints_MinInterfaceHeight(p:TSizeConstraints):Integer;cdecl;
begin
Result:=Integer(p.MinInterfaceHeight);
end;
//property getterControls_TSizeConstraints_MinInterfaceWidth
function get_Controls_TSizeConstraints_MinInterfaceWidth(p:TSizeConstraints):Integer;cdecl;
begin
Result:=Integer(p.MinInterfaceWidth);
end;
//property getterControls_TSizeConstraints_Control
function get_Controls_TSizeConstraints_Control(p:TSizeConstraints):tcontrol;cdecl;
begin
Result:=tcontrol(p.Control);
end;
//property getterControls_TSizeConstraints_Options
function get_Controls_TSizeConstraints_Options(p:TSizeConstraints):Integer;cdecl;
begin
Result:=Integer(p.Options);
end;
//property setterControls_TSizeConstraints_Options
procedure set_Controls_TSizeConstraints_Options(p:TSizeConstraints;v:tsizeconstraintsoptions);cdecl; 
begin
p.Options:=(v);
end;
//property setterControls_TSizeConstraints_OnChange
function set_Controls_TSizeConstraints_OnChange(p:TSizeConstraints;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnChange:=@callClass.call;
Result:=callClass;
end;
//property getterControls_TControl_Constraints
function get_Controls_TControl_Constraints(p:TControl):tsizeconstraints;cdecl;
begin
Result:=tsizeconstraints(p.Constraints);
end;
//property setterControls_TControl_Constraints
procedure set_Controls_TControl_Constraints(p:TControl;v:tsizeconstraints);cdecl; 
begin
p.Constraints:=(v);
end;
//property getterControls_TControl_ControlState
function get_Controls_TControl_ControlState(p:TControl):Integer;cdecl;
begin
Result:=Integer(p.ControlState);
end;
//property setterControls_TControl_ControlState
procedure set_Controls_TControl_ControlState(p:TControl;v:tcontrolstate);cdecl; 
begin
p.ControlState:=(v);
end;
//property getterControls_TControl_ControlStyle
function get_Controls_TControl_ControlStyle(p:TControl):Integer;cdecl;
begin
Result:=Integer(p.ControlStyle);
end;
//property setterControls_TControl_ControlStyle
procedure set_Controls_TControl_ControlStyle(p:TControl;v:tcontrolstyle);cdecl; 
begin
p.ControlStyle:=(v);
end;
//property getterControls_TControl_Enabled
function get_Controls_TControl_Enabled(p:TControl):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Enabled);
end;
//property setterControls_TControl_Enabled
procedure set_Controls_TControl_Enabled(p:TControl;v:Integer);cdecl; 
begin
p.Enabled:=integertToBoolean(v);
end;
//constructorGraphics_TFont_Create
function Graphics_TFont_Create():TFont;cdecl;
begin
Result:=TFont.Create();
end;
//property getterGraphics_TFont_IsMonoSpace
function get_Graphics_TFont_IsMonoSpace(p:TFont):Integer;cdecl;
begin
Result:=BooleanTointegert(p.IsMonoSpace);
end;
//property getterGraphics_TFont_CanUTF8
function get_Graphics_TFont_CanUTF8(p:TFont):Integer;cdecl;
begin
Result:=BooleanTointegert(p.CanUTF8);
end;
//property getterGraphics_TFont_PixelsPerInch
function get_Graphics_TFont_PixelsPerInch(p:TFont):Integer;cdecl;
begin
Result:=Integer(p.PixelsPerInch);
end;
//property setterGraphics_TFont_PixelsPerInch
procedure set_Graphics_TFont_PixelsPerInch(p:TFont;v:Integer);cdecl; 
begin
p.PixelsPerInch:=(v);
end;
//property getterGraphics_TFont_Height
function get_Graphics_TFont_Height(p:TFont):Integer;cdecl;
begin
Result:=Integer(p.Height);
end;
//property setterGraphics_TFont_Height
procedure set_Graphics_TFont_Height(p:TFont;v:Integer);cdecl; 
begin
p.Height:=(v);
end;
//property getterGraphics_TFont_Name
function get_Graphics_TFont_Name(p:TFont):PChar;cdecl;
begin
Result:=PChar(p.Name);
end;
//property setterGraphics_TFont_Name
procedure set_Graphics_TFont_Name(p:TFont;v:PChar);cdecl; 
begin
p.Name:=(v);
end;
//property getterGraphics_TFont_Orientation
function get_Graphics_TFont_Orientation(p:TFont):Integer;cdecl;
begin
Result:=Integer(p.Orientation);
end;
//property setterGraphics_TFont_Orientation
procedure set_Graphics_TFont_Orientation(p:TFont;v:Integer);cdecl; 
begin
p.Orientation:=(v);
end;
//property getterGraphics_TFont_Pitch
function get_Graphics_TFont_Pitch(p:TFont):Integer;cdecl;
begin
Result:=Integer(p.Pitch);
end;
//property setterGraphics_TFont_Pitch
procedure set_Graphics_TFont_Pitch(p:TFont;v:tfontpitch);cdecl; 
begin
p.Pitch:=(v);
end;
//property getterGraphics_TFont_Quality
function get_Graphics_TFont_Quality(p:TFont):Integer;cdecl;
begin
Result:=Integer(p.Quality);
end;
//property setterGraphics_TFont_Quality
procedure set_Graphics_TFont_Quality(p:TFont;v:tfontquality);cdecl; 
begin
p.Quality:=(v);
end;
//property getterGraphics_TFont_Size
function get_Graphics_TFont_Size(p:TFont):Integer;cdecl;
begin
Result:=Integer(p.Size);
end;
//property setterGraphics_TFont_Size
procedure set_Graphics_TFont_Size(p:TFont;v:Integer);cdecl; 
begin
p.Size:=(v);
end;
//property getterGraphics_TFont_Style
function get_Graphics_TFont_Style(p:TFont):Integer;cdecl;
begin
Result:=Integer(p.Style);
end;
//property setterGraphics_TFont_Style
procedure set_Graphics_TFont_Style(p:TFont;v:tfontstyles);cdecl; 
begin
p.Style:=(v);
end;
//property getterControls_TControl_Font
function get_Controls_TControl_Font(p:TControl):tfont;cdecl;
begin
Result:=tfont(p.Font);
end;
//property setterControls_TControl_Font
procedure set_Controls_TControl_Font(p:TControl;v:tfont);cdecl; 
begin
p.Font:=(v);
end;
//property getterControls_TControl_IsControl
function get_Controls_TControl_IsControl(p:TControl):Integer;cdecl;
begin
Result:=BooleanTointegert(p.IsControl);
end;
//property setterControls_TControl_IsControl
procedure set_Controls_TControl_IsControl(p:TControl;v:Integer);cdecl; 
begin
p.IsControl:=integertToBoolean(v);
end;
//property getterControls_TControl_MouseEntered
function get_Controls_TControl_MouseEntered(p:TControl):Integer;cdecl;
begin
Result:=BooleanTointegert(p.MouseEntered);
end;
//property setterControls_TControl_OnChangeBounds
function set_Controls_TControl_OnChangeBounds(p:TControl;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnChangeBounds:=@callClass.call;
Result:=callClass;
end;
//property setterControls_TControl_OnClick
function set_Controls_TControl_OnClick(p:TControl;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnClick:=@callClass.call;
Result:=callClass;
end;
//property setterControls_TControl_OnResize
function set_Controls_TControl_OnResize(p:TControl;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnResize:=@callClass.call;
Result:=callClass;
end;
//property getterControls_TControl_Parent
function get_Controls_TControl_Parent(p:TControl):twincontrol;cdecl;
begin
Result:=twincontrol(p.Parent);
end;
//property setterControls_TControl_Parent
procedure set_Controls_TControl_Parent(p:TControl;v:twincontrol);cdecl; 
begin
p.Parent:=(v);
end;
//constructorMenus_TMenuActionLink_Create
function Menus_TMenuActionLink_Create(AClient:tobject):TMenuActionLink;cdecl;
begin
Result:=TMenuActionLink.Create((AClient));
end;
//constructorMenus_TMenuItem_Create
function Menus_TMenuItem_Create(TheOwner:tcomponent):TMenuItem;cdecl;
begin
Result:=TMenuItem.Create((TheOwner));
end;
//property getterMenus_TMenuItem_Count
function get_Menus_TMenuItem_Count(p:TMenuItem):Integer;cdecl;
begin
Result:=Integer(p.Count);
end;
//property getterMenus_TMenuItem_Items
function get_Menus_TMenuItem_Items(p:TMenuItem;Index:Integer):tmenuitem;cdecl;
begin
Result:=tmenuitem(p.Items[Index]);
end;
//property getterMenus_TMenuItem_MenuIndex
function get_Menus_TMenuItem_MenuIndex(p:TMenuItem):Integer;cdecl;
begin
Result:=Integer(p.MenuIndex);
end;
//property setterMenus_TMenuItem_MenuIndex
procedure set_Menus_TMenuItem_MenuIndex(p:TMenuItem;v:Integer);cdecl; 
begin
p.MenuIndex:=(v);
end;
//property getterMenus_TMenuItem_Menu
function get_Menus_TMenuItem_Menu(p:TMenuItem):tmenu;cdecl;
begin
Result:=tmenu(p.Menu);
end;
//property getterMenus_TMenuItem_Parent
function get_Menus_TMenuItem_Parent(p:TMenuItem):tmenuitem;cdecl;
begin
Result:=tmenuitem(p.Parent);
end;
//property getterMenus_TMenuItem_Action
function get_Menus_TMenuItem_Action(p:TMenuItem):tbasicaction;cdecl;
begin
Result:=tbasicaction(p.Action);
end;
//property setterMenus_TMenuItem_Action
procedure set_Menus_TMenuItem_Action(p:TMenuItem;v:tbasicaction);cdecl; 
begin
p.Action:=(v);
end;
//property getterMenus_TMenuItem_AutoCheck
function get_Menus_TMenuItem_AutoCheck(p:TMenuItem):Integer;cdecl;
begin
Result:=BooleanTointegert(p.AutoCheck);
end;
//property setterMenus_TMenuItem_AutoCheck
procedure set_Menus_TMenuItem_AutoCheck(p:TMenuItem;v:Integer);cdecl; 
begin
p.AutoCheck:=integertToBoolean(v);
end;
//property getterMenus_TMenuItem_Checked
function get_Menus_TMenuItem_Checked(p:TMenuItem):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Checked);
end;
//property setterMenus_TMenuItem_Checked
procedure set_Menus_TMenuItem_Checked(p:TMenuItem;v:Integer);cdecl; 
begin
p.Checked:=integertToBoolean(v);
end;
//property getterMenus_TMenuItem_Default
function get_Menus_TMenuItem_Default(p:TMenuItem):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Default);
end;
//property setterMenus_TMenuItem_Default
procedure set_Menus_TMenuItem_Default(p:TMenuItem;v:Integer);cdecl; 
begin
p.Default:=integertToBoolean(v);
end;
//property getterMenus_TMenuItem_Enabled
function get_Menus_TMenuItem_Enabled(p:TMenuItem):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Enabled);
end;
//property setterMenus_TMenuItem_Enabled
procedure set_Menus_TMenuItem_Enabled(p:TMenuItem;v:Integer);cdecl; 
begin
p.Enabled:=integertToBoolean(v);
end;
//constructorGraphics_TGraphic_Create
function Graphics_TGraphic_Create():TGraphic;cdecl;
begin
Result:=TGraphic.Create();
end;
//property getterGraphics_TGraphic_Empty
function get_Graphics_TGraphic_Empty(p:TGraphic):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Empty);
end;
//property getterGraphics_TGraphic_Height
function get_Graphics_TGraphic_Height(p:TGraphic):Integer;cdecl;
begin
Result:=Integer(p.Height);
end;
//property setterGraphics_TGraphic_Height
procedure set_Graphics_TGraphic_Height(p:TGraphic;v:Integer);cdecl; 
begin
p.Height:=(v);
end;
//property getterGraphics_TGraphic_Modified
function get_Graphics_TGraphic_Modified(p:TGraphic):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Modified);
end;
//property setterGraphics_TGraphic_Modified
procedure set_Graphics_TGraphic_Modified(p:TGraphic;v:Integer);cdecl; 
begin
p.Modified:=integertToBoolean(v);
end;
//property getterGraphics_TGraphic_MimeType
function get_Graphics_TGraphic_MimeType(p:TGraphic):PChar;cdecl;
begin
Result:=PChar(p.MimeType);
end;
//property setterGraphics_TGraphic_OnChange
function set_Graphics_TGraphic_OnChange(p:TGraphic;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnChange:=@callClass.call;
Result:=callClass;
end;
//property getterGraphics_TGraphic_PaletteModified
function get_Graphics_TGraphic_PaletteModified(p:TGraphic):Integer;cdecl;
begin
Result:=BooleanTointegert(p.PaletteModified);
end;
//property setterGraphics_TGraphic_PaletteModified
procedure set_Graphics_TGraphic_PaletteModified(p:TGraphic;v:Integer);cdecl; 
begin
p.PaletteModified:=integertToBoolean(v);
end;
//property getterGraphics_TGraphic_Transparent
function get_Graphics_TGraphic_Transparent(p:TGraphic):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Transparent);
end;
//property setterGraphics_TGraphic_Transparent
procedure set_Graphics_TGraphic_Transparent(p:TGraphic;v:Integer);cdecl; 
begin
p.Transparent:=integertToBoolean(v);
end;
//property getterGraphics_TGraphic_Width
function get_Graphics_TGraphic_Width(p:TGraphic):Integer;cdecl;
begin
Result:=Integer(p.Width);
end;
//property setterGraphics_TGraphic_Width
procedure set_Graphics_TGraphic_Width(p:TGraphic;v:Integer);cdecl; 
begin
p.Width:=(v);
end;
//constructorGraphics_TRasterImage_Create
function Graphics_TRasterImage_Create():TRasterImage;cdecl;
begin
Result:=TRasterImage.Create();
end;
//constructorGraphics_TCanvas_Create
function Graphics_TCanvas_Create():TCanvas;cdecl;
begin
Result:=TCanvas.Create();
end;
//property getterGraphics_TCanvas_AntialiasingMode
function get_Graphics_TCanvas_AntialiasingMode(p:TCanvas):Integer;cdecl;
begin
Result:=Integer(p.AntialiasingMode);
end;
//property setterGraphics_TCanvas_AntialiasingMode
procedure set_Graphics_TCanvas_AntialiasingMode(p:TCanvas;v:tantialiasingmode);cdecl; 
begin
p.AntialiasingMode:=(v);
end;
//property getterGraphics_TCanvas_AutoRedraw
function get_Graphics_TCanvas_AutoRedraw(p:TCanvas):Integer;cdecl;
begin
Result:=BooleanTointegert(p.AutoRedraw);
end;
//property setterGraphics_TCanvas_AutoRedraw
procedure set_Graphics_TCanvas_AutoRedraw(p:TCanvas;v:Integer);cdecl; 
begin
p.AutoRedraw:=integertToBoolean(v);
end;
//constructorGraphics_TBrush_Create
function Graphics_TBrush_Create():TBrush;cdecl;
begin
Result:=TBrush.Create();
end;
//property getterGraphics_TBrush_Bitmap
function get_Graphics_TBrush_Bitmap(p:TBrush):tcustombitmap;cdecl;
begin
Result:=tcustombitmap(p.Bitmap);
end;
//property setterGraphics_TBrush_Bitmap
procedure set_Graphics_TBrush_Bitmap(p:TBrush;v:tcustombitmap);cdecl; 
begin
p.Bitmap:=(v);
end;
//property getterGraphics_TCanvas_Brush
function get_Graphics_TCanvas_Brush(p:TCanvas):tbrush;cdecl;
begin
Result:=tbrush(p.Brush);
end;
//property setterGraphics_TCanvas_Brush
procedure set_Graphics_TCanvas_Brush(p:TCanvas;v:tbrush);cdecl; 
begin
p.Brush:=(v);
end;
//property getterGraphics_TCanvas_Font
function get_Graphics_TCanvas_Font(p:TCanvas):tfont;cdecl;
begin
Result:=tfont(p.Font);
end;
//property setterGraphics_TCanvas_Font
procedure set_Graphics_TCanvas_Font(p:TCanvas;v:tfont);cdecl; 
begin
p.Font:=(v);
end;
//property getterGraphics_TCanvas_Height
function get_Graphics_TCanvas_Height(p:TCanvas):Integer;cdecl;
begin
Result:=Integer(p.Height);
end;
//constructorGraphics_TPen_Create
function Graphics_TPen_Create():TPen;cdecl;
begin
Result:=TPen.Create();
end;
//property getterGraphics_TPen_Cosmetic
function get_Graphics_TPen_Cosmetic(p:TPen):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Cosmetic);
end;
//property setterGraphics_TPen_Cosmetic
procedure set_Graphics_TPen_Cosmetic(p:TPen;v:Integer);cdecl; 
begin
p.Cosmetic:=integertToBoolean(v);
end;
//property getterGraphics_TPen_EndCap
function get_Graphics_TPen_EndCap(p:TPen):Integer;cdecl;
begin
Result:=Integer(p.EndCap);
end;
//property setterGraphics_TPen_EndCap
procedure set_Graphics_TPen_EndCap(p:TPen;v:tpenendcap);cdecl; 
begin
p.EndCap:=(v);
end;
//property getterGraphics_TPen_JoinStyle
function get_Graphics_TPen_JoinStyle(p:TPen):Integer;cdecl;
begin
Result:=Integer(p.JoinStyle);
end;
//property setterGraphics_TPen_JoinStyle
procedure set_Graphics_TPen_JoinStyle(p:TPen;v:tpenjoinstyle);cdecl; 
begin
p.JoinStyle:=(v);
end;
//property getterGraphics_TCanvas_Pen
function get_Graphics_TCanvas_Pen(p:TCanvas):tpen;cdecl;
begin
Result:=tpen(p.Pen);
end;
//property setterGraphics_TCanvas_Pen
procedure set_Graphics_TCanvas_Pen(p:TCanvas;v:tpen);cdecl; 
begin
p.Pen:=(v);
end;
//property setterGraphics_TGraphicsObject_OnChanging
function set_Graphics_TGraphicsObject_OnChanging(p:TGraphicsObject;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnChanging:=@callClass.call;
Result:=callClass;
end;
//property setterGraphics_TGraphicsObject_OnChange
function set_Graphics_TGraphicsObject_OnChange(p:TGraphicsObject;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnChange:=@callClass.call;
Result:=callClass;
end;
//constructorGraphics_TRegion_Create
function Graphics_TRegion_Create():TRegion;cdecl;
begin
Result:=TRegion.Create();
end;
//property getterGraphics_TCanvas_Region
function get_Graphics_TCanvas_Region(p:TCanvas):tregion;cdecl;
begin
Result:=tregion(p.Region);
end;
//property setterGraphics_TCanvas_Region
procedure set_Graphics_TCanvas_Region(p:TCanvas;v:tregion);cdecl; 
begin
p.Region:=(v);
end;
//property getterGraphics_TCanvas_Width
function get_Graphics_TCanvas_Width(p:TCanvas):Integer;cdecl;
begin
Result:=Integer(p.Width);
end;
//property setterGraphics_TCanvas_OnChange
function set_Graphics_TCanvas_OnChange(p:TCanvas;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnChange:=@callClass.call;
Result:=callClass;
end;
//property setterGraphics_TCanvas_OnChanging
function set_Graphics_TCanvas_OnChanging(p:TCanvas;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnChanging:=@callClass.call;
Result:=callClass;
end;
//property getterGraphics_TRasterImage_Canvas
function get_Graphics_TRasterImage_Canvas(p:TRasterImage):tcanvas;cdecl;
begin
Result:=tcanvas(p.Canvas);
end;
//property getterGraphics_TRasterImage_Masked
function get_Graphics_TRasterImage_Masked(p:TRasterImage):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Masked);
end;
//property setterGraphics_TRasterImage_Masked
procedure set_Graphics_TRasterImage_Masked(p:TRasterImage;v:Integer);cdecl; 
begin
p.Masked:=integertToBoolean(v);
end;
//property getterGraphics_TRasterImage_PixelFormat
function get_Graphics_TRasterImage_PixelFormat(p:TRasterImage):Integer;cdecl;
begin
Result:=Integer(p.PixelFormat);
end;
//property setterGraphics_TRasterImage_PixelFormat
procedure set_Graphics_TRasterImage_PixelFormat(p:TRasterImage;v:tpixelformat);cdecl; 
begin
p.PixelFormat:=(v);
end;
//property getterGraphics_TRasterImage_RawImage
function get_Graphics_TRasterImage_RawImage(p:TRasterImage):trawimage;cdecl;
begin
Result:=trawimage(p.RawImage);
end;
//property getterGraphics_TRasterImage_TransparentMode
function get_Graphics_TRasterImage_TransparentMode(p:TRasterImage):Integer;cdecl;
begin
Result:=Integer(p.TransparentMode);
end;
//property setterGraphics_TRasterImage_TransparentMode
procedure set_Graphics_TRasterImage_TransparentMode(p:TRasterImage;v:ttransparentmode);cdecl; 
begin
p.TransparentMode:=(v);
end;
//constructorGraphics_TCustomBitmap_Create
function Graphics_TCustomBitmap_Create():TCustomBitmap;cdecl;
begin
Result:=TCustomBitmap.Create();
end;
//property getterGraphics_TCustomBitmap_HandleType
function get_Graphics_TCustomBitmap_HandleType(p:TCustomBitmap):Integer;cdecl;
begin
Result:=Integer(p.HandleType);
end;
//property setterGraphics_TCustomBitmap_HandleType
procedure set_Graphics_TCustomBitmap_HandleType(p:TCustomBitmap;v:tbitmaphandletype);cdecl; 
begin
p.HandleType:=(v);
end;
//property getterGraphics_TCustomBitmap_Monochrome
function get_Graphics_TCustomBitmap_Monochrome(p:TCustomBitmap):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Monochrome);
end;
//property setterGraphics_TCustomBitmap_Monochrome
procedure set_Graphics_TCustomBitmap_Monochrome(p:TCustomBitmap;v:Integer);cdecl; 
begin
p.Monochrome:=integertToBoolean(v);
end;
//constructorGraphics_TFPImageBitmap_Create
function Graphics_TFPImageBitmap_Create():TFPImageBitmap;cdecl;
begin
Result:=TFPImageBitmap.Create();
end;
//constructorGraphics_TBitmap_Create
function Graphics_TBitmap_Create():TBitmap;cdecl;
begin
Result:=TBitmap.Create();
end;
//property getterMenus_TMenuItem_Bitmap
function get_Menus_TMenuItem_Bitmap(p:TMenuItem):tbitmap;cdecl;
begin
Result:=tbitmap(p.Bitmap);
end;
//property setterMenus_TMenuItem_Bitmap
procedure set_Menus_TMenuItem_Bitmap(p:TMenuItem;v:tbitmap);cdecl; 
begin
p.Bitmap:=(v);
end;
//property getterMenus_TMenuItem_GlyphShowMode
function get_Menus_TMenuItem_GlyphShowMode(p:TMenuItem):Integer;cdecl;
begin
Result:=Integer(p.GlyphShowMode);
end;
//property setterMenus_TMenuItem_GlyphShowMode
procedure set_Menus_TMenuItem_GlyphShowMode(p:TMenuItem;v:tglyphshowmode);cdecl; 
begin
p.GlyphShowMode:=(v);
end;
//property getterMenus_TMenuItem_RadioItem
function get_Menus_TMenuItem_RadioItem(p:TMenuItem):Integer;cdecl;
begin
Result:=BooleanTointegert(p.RadioItem);
end;
//property setterMenus_TMenuItem_RadioItem
procedure set_Menus_TMenuItem_RadioItem(p:TMenuItem;v:Integer);cdecl; 
begin
p.RadioItem:=integertToBoolean(v);
end;
//property getterMenus_TMenuItem_RightJustify
function get_Menus_TMenuItem_RightJustify(p:TMenuItem):Integer;cdecl;
begin
Result:=BooleanTointegert(p.RightJustify);
end;
//property setterMenus_TMenuItem_RightJustify
procedure set_Menus_TMenuItem_RightJustify(p:TMenuItem;v:Integer);cdecl; 
begin
p.RightJustify:=integertToBoolean(v);
end;
//property getterMenus_TMenuItem_ShowAlwaysCheckable
function get_Menus_TMenuItem_ShowAlwaysCheckable(p:TMenuItem):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ShowAlwaysCheckable);
end;
//property setterMenus_TMenuItem_ShowAlwaysCheckable
procedure set_Menus_TMenuItem_ShowAlwaysCheckable(p:TMenuItem;v:Integer);cdecl; 
begin
p.ShowAlwaysCheckable:=integertToBoolean(v);
end;
//property getterLCLClasses_TLCLReferenceComponent_HandleAllocated
function get_LCLClasses_TLCLReferenceComponent_HandleAllocated(p:TLCLReferenceComponent):Integer;cdecl;
begin
Result:=BooleanTointegert(p.HandleAllocated);
end;
//property getterLCLClasses_TLCLReferenceComponent_ReferenceAllocated
function get_LCLClasses_TLCLReferenceComponent_ReferenceAllocated(p:TLCLReferenceComponent):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ReferenceAllocated);
end;
//constructorLCLClasses_TLCLReferenceComponent_Create
function LCLClasses_TLCLReferenceComponent_Create(TheOwner:tcomponent):TLCLReferenceComponent;cdecl;
begin
Result:=TLCLReferenceComponent.Create((TheOwner));
end;
//constructorImgList_TCustomImageList_Create
function ImgList_TCustomImageList_Create(AOwner:tcomponent):TCustomImageList;cdecl;
begin
Result:=TCustomImageList.Create((AOwner));
end;
//constructorImgList_TCustomImageList_CreateSize
function ImgList_TCustomImageList_CreateSize(AWidth:Integer;AHeight:Integer):TCustomImageList;cdecl;
begin
Result:=TCustomImageList.CreateSize((AWidth),(AHeight));
end;
//property getterImgList_TCustomImageList_HasOverlays
function get_ImgList_TCustomImageList_HasOverlays(p:TCustomImageList):Integer;cdecl;
begin
Result:=BooleanTointegert(p.HasOverlays);
end;
//property getterImgList_TCustomImageList_AllocBy
function get_ImgList_TCustomImageList_AllocBy(p:TCustomImageList):Integer;cdecl;
begin
Result:=Integer(p.AllocBy);
end;
//property setterImgList_TCustomImageList_AllocBy
procedure set_ImgList_TCustomImageList_AllocBy(p:TCustomImageList;v:Integer);cdecl; 
begin
p.AllocBy:=(v);
end;
//property getterImgList_TCustomImageList_Count
function get_ImgList_TCustomImageList_Count(p:TCustomImageList):Integer;cdecl;
begin
Result:=Integer(p.Count);
end;
//property getterImgList_TCustomImageList_DrawingStyle
function get_ImgList_TCustomImageList_DrawingStyle(p:TCustomImageList):Integer;cdecl;
begin
Result:=Integer(p.DrawingStyle);
end;
//property setterImgList_TCustomImageList_DrawingStyle
procedure set_ImgList_TCustomImageList_DrawingStyle(p:TCustomImageList;v:tdrawingstyle);cdecl; 
begin
p.DrawingStyle:=(v);
end;
//property getterImgList_TCustomImageList_Height
function get_ImgList_TCustomImageList_Height(p:TCustomImageList):Integer;cdecl;
begin
Result:=Integer(p.Height);
end;
//property setterImgList_TCustomImageList_Height
procedure set_ImgList_TCustomImageList_Height(p:TCustomImageList;v:Integer);cdecl; 
begin
p.Height:=(v);
end;
//property getterImgList_TCustomImageList_Width
function get_ImgList_TCustomImageList_Width(p:TCustomImageList):Integer;cdecl;
begin
Result:=Integer(p.Width);
end;
//property setterImgList_TCustomImageList_Width
procedure set_ImgList_TCustomImageList_Width(p:TCustomImageList;v:Integer);cdecl; 
begin
p.Width:=(v);
end;
//property setterImgList_TCustomImageList_OnChange
function set_ImgList_TCustomImageList_OnChange(p:TCustomImageList;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnChange:=@callClass.call;
Result:=callClass;
end;
//property getterImgList_TCustomImageList_Masked
function get_ImgList_TCustomImageList_Masked(p:TCustomImageList):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Masked);
end;
//property setterImgList_TCustomImageList_Masked
procedure set_ImgList_TCustomImageList_Masked(p:TCustomImageList;v:Integer);cdecl; 
begin
p.Masked:=integertToBoolean(v);
end;
//property getterImgList_TCustomImageList_ShareImages
function get_ImgList_TCustomImageList_ShareImages(p:TCustomImageList):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ShareImages);
end;
//property setterImgList_TCustomImageList_ShareImages
procedure set_ImgList_TCustomImageList_ShareImages(p:TCustomImageList;v:Integer);cdecl; 
begin
p.ShareImages:=integertToBoolean(v);
end;
//property getterImgList_TCustomImageList_ImageType
function get_ImgList_TCustomImageList_ImageType(p:TCustomImageList):Integer;cdecl;
begin
Result:=Integer(p.ImageType);
end;
//property setterImgList_TCustomImageList_ImageType
procedure set_ImgList_TCustomImageList_ImageType(p:TCustomImageList;v:timagetype);cdecl; 
begin
p.ImageType:=(v);
end;
//property getterMenus_TMenuItem_SubMenuImages
function get_Menus_TMenuItem_SubMenuImages(p:TMenuItem):tcustomimagelist;cdecl;
begin
Result:=tcustomimagelist(p.SubMenuImages);
end;
//property setterMenus_TMenuItem_SubMenuImages
procedure set_Menus_TMenuItem_SubMenuImages(p:TMenuItem;v:tcustomimagelist);cdecl; 
begin
p.SubMenuImages:=(v);
end;
//property getterMenus_TMenuItem_Visible
function get_Menus_TMenuItem_Visible(p:TMenuItem):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Visible);
end;
//property setterMenus_TMenuItem_Visible
procedure set_Menus_TMenuItem_Visible(p:TMenuItem;v:Integer);cdecl; 
begin
p.Visible:=integertToBoolean(v);
end;
//property setterMenus_TMenuItem_OnClick
function set_Menus_TMenuItem_OnClick(p:TMenuItem;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnClick:=@callClass.call;
Result:=callClass;
end;
//property setterMenus_TMenuItem_OnMeasureItem
function set_Menus_TMenuItem_OnMeasureItem(p:TMenuItem;newMethod:Menus_TMenuMeasureItemEvent;OldEvent:MenusTMenuMeasureItemEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:MenusTMenuMeasureItemEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=MenusTMenuMeasureItemEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMeasureItem:=@callClass.call;
Result:=callClass;
end;
//constructorMenus_TMenu_Create
function Menus_TMenu_Create(AOwner:tcomponent):TMenu;cdecl;
begin
Result:=TMenu.Create((AOwner));
end;
//property getterMenus_TMenu_Parent
function get_Menus_TMenu_Parent(p:TMenu):tcomponent;cdecl;
begin
Result:=tcomponent(p.Parent);
end;
//property setterMenus_TMenu_Parent
procedure set_Menus_TMenu_Parent(p:TMenu;v:tcomponent);cdecl; 
begin
p.Parent:=(v);
end;
//property getterMenus_TMenu_ShortcutHandled
function get_Menus_TMenu_ShortcutHandled(p:TMenu):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ShortcutHandled);
end;
//property setterMenus_TMenu_ShortcutHandled
procedure set_Menus_TMenu_ShortcutHandled(p:TMenu;v:Integer);cdecl; 
begin
p.ShortcutHandled:=integertToBoolean(v);
end;
//property getterMenus_TMenu_BidiMode
function get_Menus_TMenu_BidiMode(p:TMenu):Integer;cdecl;
begin
Result:=Integer(p.BidiMode);
end;
//property setterMenus_TMenu_BidiMode
procedure set_Menus_TMenu_BidiMode(p:TMenu;v:tbidimode);cdecl; 
begin
p.BidiMode:=(v);
end;
//property getterMenus_TMenu_ParentBidiMode
function get_Menus_TMenu_ParentBidiMode(p:TMenu):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentBidiMode);
end;
//property setterMenus_TMenu_ParentBidiMode
procedure set_Menus_TMenu_ParentBidiMode(p:TMenu;v:Integer);cdecl; 
begin
p.ParentBidiMode:=integertToBoolean(v);
end;
//property getterMenus_TMenu_Items
function get_Menus_TMenu_Items(p:TMenu):tmenuitem;cdecl;
begin
Result:=tmenuitem(p.Items);
end;
//property getterMenus_TMenu_Images
function get_Menus_TMenu_Images(p:TMenu):tcustomimagelist;cdecl;
begin
Result:=tcustomimagelist(p.Images);
end;
//property setterMenus_TMenu_Images
procedure set_Menus_TMenu_Images(p:TMenu;v:tcustomimagelist);cdecl; 
begin
p.Images:=(v);
end;
//property getterMenus_TMenu_OwnerDraw
function get_Menus_TMenu_OwnerDraw(p:TMenu):Integer;cdecl;
begin
Result:=BooleanTointegert(p.OwnerDraw);
end;
//property setterMenus_TMenu_OwnerDraw
procedure set_Menus_TMenu_OwnerDraw(p:TMenu;v:Integer);cdecl; 
begin
p.OwnerDraw:=integertToBoolean(v);
end;
//property setterMenus_TMenu_OnMeasureItem
function set_Menus_TMenu_OnMeasureItem(p:TMenu;newMethod:Menus_TMenuMeasureItemEvent;OldEvent:MenusTMenuMeasureItemEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:MenusTMenuMeasureItemEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=MenusTMenuMeasureItemEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMeasureItem:=@callClass.call;
Result:=callClass;
end;
//constructorMenus_TPopupMenu_Create
function Menus_TPopupMenu_Create(AOwner:tcomponent):TPopupMenu;cdecl;
begin
Result:=TPopupMenu.Create((AOwner));
end;
//property getterMenus_TPopupMenu_PopupComponent
function get_Menus_TPopupMenu_PopupComponent(p:TPopupMenu):tcomponent;cdecl;
begin
Result:=tcomponent(p.PopupComponent);
end;
//property setterMenus_TPopupMenu_PopupComponent
procedure set_Menus_TPopupMenu_PopupComponent(p:TPopupMenu;v:tcomponent);cdecl; 
begin
p.PopupComponent:=(v);
end;
//property getterMenus_TPopupMenu_Alignment
function get_Menus_TPopupMenu_Alignment(p:TPopupMenu):Integer;cdecl;
begin
Result:=Integer(p.Alignment);
end;
//property setterMenus_TPopupMenu_Alignment
procedure set_Menus_TPopupMenu_Alignment(p:TPopupMenu;v:tpopupalignment);cdecl; 
begin
p.Alignment:=(v);
end;
//property getterMenus_TPopupMenu_AutoPopup
function get_Menus_TPopupMenu_AutoPopup(p:TPopupMenu):Integer;cdecl;
begin
Result:=BooleanTointegert(p.AutoPopup);
end;
//property setterMenus_TPopupMenu_AutoPopup
procedure set_Menus_TPopupMenu_AutoPopup(p:TPopupMenu;v:Integer);cdecl; 
begin
p.AutoPopup:=integertToBoolean(v);
end;
//property getterMenus_TPopupMenu_TrackButton
function get_Menus_TPopupMenu_TrackButton(p:TPopupMenu):Integer;cdecl;
begin
Result:=Integer(p.TrackButton);
end;
//property setterMenus_TPopupMenu_TrackButton
procedure set_Menus_TPopupMenu_TrackButton(p:TPopupMenu;v:ttrackbutton);cdecl; 
begin
p.TrackButton:=(v);
end;
//property setterMenus_TPopupMenu_OnPopup
function set_Menus_TPopupMenu_OnPopup(p:TPopupMenu;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnPopup:=@callClass.call;
Result:=callClass;
end;
//property setterMenus_TPopupMenu_OnClose
function set_Menus_TPopupMenu_OnClose(p:TPopupMenu;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnClose:=@callClass.call;
Result:=callClass;
end;
//property getterControls_TControl_PopupMenu
function get_Controls_TControl_PopupMenu(p:TControl):tpopupmenu;cdecl;
begin
Result:=tpopupmenu(p.PopupMenu);
end;
//property setterControls_TControl_PopupMenu
procedure set_Controls_TControl_PopupMenu(p:TControl;v:tpopupmenu);cdecl; 
begin
p.PopupMenu:=(v);
end;
//property getterControls_TControl_ShowHint
function get_Controls_TControl_ShowHint(p:TControl):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ShowHint);
end;
//property setterControls_TControl_ShowHint
procedure set_Controls_TControl_ShowHint(p:TControl;v:Integer);cdecl; 
begin
p.ShowHint:=integertToBoolean(v);
end;
//property getterControls_TControl_Visible
function get_Controls_TControl_Visible(p:TControl):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Visible);
end;
//property setterControls_TControl_Visible
procedure set_Controls_TControl_Visible(p:TControl;v:Integer);cdecl; 
begin
p.Visible:=integertToBoolean(v);
end;
//property getterControls_TControl_DockOrientation
function get_Controls_TControl_DockOrientation(p:TControl):Integer;cdecl;
begin
Result:=Integer(p.DockOrientation);
end;
//property setterControls_TControl_DockOrientation
procedure set_Controls_TControl_DockOrientation(p:TControl;v:tdockorientation);cdecl; 
begin
p.DockOrientation:=(v);
end;
//property getterControls_TControl_Floating
function get_Controls_TControl_Floating(p:TControl):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Floating);
end;
//property getterControls_TControl_HostDockSite
function get_Controls_TControl_HostDockSite(p:TControl):twincontrol;cdecl;
begin
Result:=twincontrol(p.HostDockSite);
end;
//property setterControls_TControl_HostDockSite
procedure set_Controls_TControl_HostDockSite(p:TControl;v:twincontrol);cdecl; 
begin
p.HostDockSite:=(v);
end;
//property getterControls_TControl_LRDockWidth
function get_Controls_TControl_LRDockWidth(p:TControl):Integer;cdecl;
begin
Result:=Integer(p.LRDockWidth);
end;
//property setterControls_TControl_LRDockWidth
procedure set_Controls_TControl_LRDockWidth(p:TControl;v:Integer);cdecl; 
begin
p.LRDockWidth:=(v);
end;
//property getterControls_TControl_TBDockHeight
function get_Controls_TControl_TBDockHeight(p:TControl):Integer;cdecl;
begin
Result:=Integer(p.TBDockHeight);
end;
//property setterControls_TControl_TBDockHeight
procedure set_Controls_TControl_TBDockHeight(p:TControl;v:Integer);cdecl; 
begin
p.TBDockHeight:=(v);
end;
//property getterControls_TControl_UndockHeight
function get_Controls_TControl_UndockHeight(p:TControl):Integer;cdecl;
begin
Result:=Integer(p.UndockHeight);
end;
//property setterControls_TControl_UndockHeight
procedure set_Controls_TControl_UndockHeight(p:TControl;v:Integer);cdecl; 
begin
p.UndockHeight:=(v);
end;
//property getterControls_TControl_UndockWidth
function get_Controls_TControl_UndockWidth(p:TControl):Integer;cdecl;
begin
Result:=Integer(p.UndockWidth);
end;
//property setterControls_TControl_UndockWidth
procedure set_Controls_TControl_UndockWidth(p:TControl;v:Integer);cdecl; 
begin
p.UndockWidth:=(v);
end;
//property getterControls_TControl_BiDiMode
function get_Controls_TControl_BiDiMode(p:TControl):Integer;cdecl;
begin
Result:=Integer(p.BiDiMode);
end;
//property setterControls_TControl_BiDiMode
procedure set_Controls_TControl_BiDiMode(p:TControl;v:tbidimode);cdecl; 
begin
p.BiDiMode:=(v);
end;
//property getterControls_TControl_ParentBiDiMode
function get_Controls_TControl_ParentBiDiMode(p:TControl):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentBiDiMode);
end;
//property setterControls_TControl_ParentBiDiMode
procedure set_Controls_TControl_ParentBiDiMode(p:TControl;v:Integer);cdecl; 
begin
p.ParentBiDiMode:=integertToBoolean(v);
end;
//property getterControls_TControl_AnchorSideLeft
function get_Controls_TControl_AnchorSideLeft(p:TControl):tanchorside;cdecl;
begin
Result:=tanchorside(p.AnchorSideLeft);
end;
//property setterControls_TControl_AnchorSideLeft
procedure set_Controls_TControl_AnchorSideLeft(p:TControl;v:tanchorside);cdecl; 
begin
p.AnchorSideLeft:=(v);
end;
//property getterControls_TControl_AnchorSideTop
function get_Controls_TControl_AnchorSideTop(p:TControl):tanchorside;cdecl;
begin
Result:=tanchorside(p.AnchorSideTop);
end;
//property setterControls_TControl_AnchorSideTop
procedure set_Controls_TControl_AnchorSideTop(p:TControl;v:tanchorside);cdecl; 
begin
p.AnchorSideTop:=(v);
end;
//property getterControls_TControl_AnchorSideRight
function get_Controls_TControl_AnchorSideRight(p:TControl):tanchorside;cdecl;
begin
Result:=tanchorside(p.AnchorSideRight);
end;
//property setterControls_TControl_AnchorSideRight
procedure set_Controls_TControl_AnchorSideRight(p:TControl;v:tanchorside);cdecl; 
begin
p.AnchorSideRight:=(v);
end;
//property getterControls_TControl_AnchorSideBottom
function get_Controls_TControl_AnchorSideBottom(p:TControl):tanchorside;cdecl;
begin
Result:=tanchorside(p.AnchorSideBottom);
end;
//property setterControls_TControl_AnchorSideBottom
procedure set_Controls_TControl_AnchorSideBottom(p:TControl;v:tanchorside);cdecl; 
begin
p.AnchorSideBottom:=(v);
end;
//property getterControls_TControl_Left
function get_Controls_TControl_Left(p:TControl):Integer;cdecl;
begin
Result:=Integer(p.Left);
end;
//property setterControls_TControl_Left
procedure set_Controls_TControl_Left(p:TControl;v:Integer);cdecl; 
begin
p.Left:=(v);
end;
//property getterControls_TControl_Height
function get_Controls_TControl_Height(p:TControl):Integer;cdecl;
begin
Result:=Integer(p.Height);
end;
//property setterControls_TControl_Height
procedure set_Controls_TControl_Height(p:TControl;v:Integer);cdecl; 
begin
p.Height:=(v);
end;
//property getterControls_TControl_Top
function get_Controls_TControl_Top(p:TControl):Integer;cdecl;
begin
Result:=Integer(p.Top);
end;
//property setterControls_TControl_Top
procedure set_Controls_TControl_Top(p:TControl;v:Integer);cdecl; 
begin
p.Top:=(v);
end;
//property getterControls_TControl_Width
function get_Controls_TControl_Width(p:TControl):Integer;cdecl;
begin
Result:=Integer(p.Width);
end;
//property setterControls_TControl_Width
procedure set_Controls_TControl_Width(p:TControl;v:Integer);cdecl; 
begin
p.Width:=(v);
end;
//property getterControls_TControl_HelpType
function get_Controls_TControl_HelpType(p:TControl):Integer;cdecl;
begin
Result:=Integer(p.HelpType);
end;
//property setterControls_TControl_HelpType
procedure set_Controls_TControl_HelpType(p:TControl;v:thelptype);cdecl; 
begin
p.HelpType:=(v);
end;
//property getterControls_TControl_HelpKeyword
function get_Controls_TControl_HelpKeyword(p:TControl):PChar;cdecl;
begin
Result:=PChar(p.HelpKeyword);
end;
//property setterControls_TControl_HelpKeyword
procedure set_Controls_TControl_HelpKeyword(p:TControl;v:PChar);cdecl; 
begin
p.HelpKeyword:=(v);
end;
//property getterControls_TWinControl_BoundsLockCount
function get_Controls_TWinControl_BoundsLockCount(p:TWinControl):Integer;cdecl;
begin
Result:=Integer(p.BoundsLockCount);
end;
//property getterControls_TWinControl_Brush
function get_Controls_TWinControl_Brush(p:TWinControl):tbrush;cdecl;
begin
Result:=tbrush(p.Brush);
end;
//property getterControls_TWinControl_CachedClientHeight
function get_Controls_TWinControl_CachedClientHeight(p:TWinControl):Integer;cdecl;
begin
Result:=Integer(p.CachedClientHeight);
end;
//property getterControls_TWinControl_CachedClientWidth
function get_Controls_TWinControl_CachedClientWidth(p:TWinControl):Integer;cdecl;
begin
Result:=Integer(p.CachedClientWidth);
end;
//property getterControls_TControlChildSizing_Control
function get_Controls_TControlChildSizing_Control(p:TControlChildSizing):twincontrol;cdecl;
begin
Result:=twincontrol(p.Control);
end;
//property setterControls_TControlChildSizing_OnChange
function set_Controls_TControlChildSizing_OnChange(p:TControlChildSizing;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnChange:=@callClass.call;
Result:=callClass;
end;
//property getterControls_TControlChildSizing_LeftRightSpacing
function get_Controls_TControlChildSizing_LeftRightSpacing(p:TControlChildSizing):Integer;cdecl;
begin
Result:=Integer(p.LeftRightSpacing);
end;
//property setterControls_TControlChildSizing_LeftRightSpacing
procedure set_Controls_TControlChildSizing_LeftRightSpacing(p:TControlChildSizing;v:Integer);cdecl; 
begin
p.LeftRightSpacing:=(v);
end;
//property getterControls_TControlChildSizing_TopBottomSpacing
function get_Controls_TControlChildSizing_TopBottomSpacing(p:TControlChildSizing):Integer;cdecl;
begin
Result:=Integer(p.TopBottomSpacing);
end;
//property setterControls_TControlChildSizing_TopBottomSpacing
procedure set_Controls_TControlChildSizing_TopBottomSpacing(p:TControlChildSizing;v:Integer);cdecl; 
begin
p.TopBottomSpacing:=(v);
end;
//property getterControls_TControlChildSizing_HorizontalSpacing
function get_Controls_TControlChildSizing_HorizontalSpacing(p:TControlChildSizing):Integer;cdecl;
begin
Result:=Integer(p.HorizontalSpacing);
end;
//property setterControls_TControlChildSizing_HorizontalSpacing
procedure set_Controls_TControlChildSizing_HorizontalSpacing(p:TControlChildSizing;v:Integer);cdecl; 
begin
p.HorizontalSpacing:=(v);
end;
//property getterControls_TControlChildSizing_VerticalSpacing
function get_Controls_TControlChildSizing_VerticalSpacing(p:TControlChildSizing):Integer;cdecl;
begin
Result:=Integer(p.VerticalSpacing);
end;
//property setterControls_TControlChildSizing_VerticalSpacing
procedure set_Controls_TControlChildSizing_VerticalSpacing(p:TControlChildSizing;v:Integer);cdecl; 
begin
p.VerticalSpacing:=(v);
end;
//property getterControls_TControlChildSizing_EnlargeHorizontal
function get_Controls_TControlChildSizing_EnlargeHorizontal(p:TControlChildSizing):Integer;cdecl;
begin
Result:=Integer(p.EnlargeHorizontal);
end;
//property setterControls_TControlChildSizing_EnlargeHorizontal
procedure set_Controls_TControlChildSizing_EnlargeHorizontal(p:TControlChildSizing;v:tchildcontrolresizestyle);cdecl; 
begin
p.EnlargeHorizontal:=(v);
end;
//property getterControls_TControlChildSizing_EnlargeVertical
function get_Controls_TControlChildSizing_EnlargeVertical(p:TControlChildSizing):Integer;cdecl;
begin
Result:=Integer(p.EnlargeVertical);
end;
//property setterControls_TControlChildSizing_EnlargeVertical
procedure set_Controls_TControlChildSizing_EnlargeVertical(p:TControlChildSizing;v:tchildcontrolresizestyle);cdecl; 
begin
p.EnlargeVertical:=(v);
end;
//property getterControls_TControlChildSizing_ShrinkHorizontal
function get_Controls_TControlChildSizing_ShrinkHorizontal(p:TControlChildSizing):Integer;cdecl;
begin
Result:=Integer(p.ShrinkHorizontal);
end;
//property setterControls_TControlChildSizing_ShrinkHorizontal
procedure set_Controls_TControlChildSizing_ShrinkHorizontal(p:TControlChildSizing;v:tchildcontrolresizestyle);cdecl; 
begin
p.ShrinkHorizontal:=(v);
end;
//property getterControls_TControlChildSizing_ShrinkVertical
function get_Controls_TControlChildSizing_ShrinkVertical(p:TControlChildSizing):Integer;cdecl;
begin
Result:=Integer(p.ShrinkVertical);
end;
//property setterControls_TControlChildSizing_ShrinkVertical
procedure set_Controls_TControlChildSizing_ShrinkVertical(p:TControlChildSizing;v:tchildcontrolresizestyle);cdecl; 
begin
p.ShrinkVertical:=(v);
end;
//property getterControls_TControlChildSizing_Layout
function get_Controls_TControlChildSizing_Layout(p:TControlChildSizing):Integer;cdecl;
begin
Result:=Integer(p.Layout);
end;
//property setterControls_TControlChildSizing_Layout
procedure set_Controls_TControlChildSizing_Layout(p:TControlChildSizing;v:tcontrolchildrenlayout);cdecl; 
begin
p.Layout:=(v);
end;
//property getterControls_TControlChildSizing_ControlsPerLine
function get_Controls_TControlChildSizing_ControlsPerLine(p:TControlChildSizing):Integer;cdecl;
begin
Result:=Integer(p.ControlsPerLine);
end;
//property setterControls_TControlChildSizing_ControlsPerLine
procedure set_Controls_TControlChildSizing_ControlsPerLine(p:TControlChildSizing;v:Integer);cdecl; 
begin
p.ControlsPerLine:=(v);
end;
//property getterControls_TWinControl_ChildSizing
function get_Controls_TWinControl_ChildSizing(p:TWinControl):tcontrolchildsizing;cdecl;
begin
Result:=tcontrolchildsizing(p.ChildSizing);
end;
//property setterControls_TWinControl_ChildSizing
procedure set_Controls_TWinControl_ChildSizing(p:TWinControl;v:tcontrolchildsizing);cdecl; 
begin
p.ChildSizing:=(v);
end;
//property getterControls_TWinControl_ControlCount
function get_Controls_TWinControl_ControlCount(p:TWinControl):Integer;cdecl;
begin
Result:=Integer(p.ControlCount);
end;
//property getterControls_TWinControl_Controls
function get_Controls_TWinControl_Controls(p:TWinControl;Index:Integer):tcontrol;cdecl;
begin
Result:=tcontrol(p.Controls[Index]);
end;
//property getterControls_TWinControl_DockClientCount
function get_Controls_TWinControl_DockClientCount(p:TWinControl):Integer;cdecl;
begin
Result:=Integer(p.DockClientCount);
end;
//property getterControls_TWinControl_DockClients
function get_Controls_TWinControl_DockClients(p:TWinControl;Index:Integer):tcontrol;cdecl;
begin
Result:=tcontrol(p.DockClients[Index]);
end;
//property getterControls_TWinControl_DockManager
function get_Controls_TWinControl_DockManager(p:TWinControl):tdockmanager;cdecl;
begin
Result:=tdockmanager(p.DockManager);
end;
//property setterControls_TWinControl_DockManager
procedure set_Controls_TWinControl_DockManager(p:TWinControl;v:tdockmanager);cdecl; 
begin
p.DockManager:=(v);
end;
//property getterControls_TWinControl_DockSite
function get_Controls_TWinControl_DockSite(p:TWinControl):Integer;cdecl;
begin
Result:=BooleanTointegert(p.DockSite);
end;
//property setterControls_TWinControl_DockSite
procedure set_Controls_TWinControl_DockSite(p:TWinControl;v:Integer);cdecl; 
begin
p.DockSite:=integertToBoolean(v);
end;
//property getterControls_TWinControl_DoubleBuffered
function get_Controls_TWinControl_DoubleBuffered(p:TWinControl):Integer;cdecl;
begin
Result:=BooleanTointegert(p.DoubleBuffered);
end;
//property setterControls_TWinControl_DoubleBuffered
procedure set_Controls_TWinControl_DoubleBuffered(p:TWinControl;v:Integer);cdecl; 
begin
p.DoubleBuffered:=integertToBoolean(v);
end;
//property getterControls_TWinControl_IsResizing
function get_Controls_TWinControl_IsResizing(p:TWinControl):Integer;cdecl;
begin
Result:=BooleanTointegert(p.IsResizing);
end;
//property getterControls_TWinControl_TabStop
function get_Controls_TWinControl_TabStop(p:TWinControl):Integer;cdecl;
begin
Result:=BooleanTointegert(p.TabStop);
end;
//property setterControls_TWinControl_TabStop
procedure set_Controls_TWinControl_TabStop(p:TWinControl;v:Integer);cdecl; 
begin
p.TabStop:=integertToBoolean(v);
end;
//property setterControls_TWinControl_OnDockDrop
function set_Controls_TWinControl_OnDockDrop(p:TWinControl;newMethod:Controls_TDockDropEvent;OldEvent:ControlsTDockDropEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDockDropEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDockDropEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDockDrop:=@callClass.call;
Result:=callClass;
end;
//property setterControls_TWinControl_OnDockOver
function set_Controls_TWinControl_OnDockOver(p:TWinControl;newMethod:Controls_TDockOverEvent;OldEvent:ControlsTDockOverEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDockOverEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDockOverEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDockOver:=@callClass.call;
Result:=callClass;
end;
//property setterControls_TWinControl_OnEnter
function set_Controls_TWinControl_OnEnter(p:TWinControl;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEnter:=@callClass.call;
Result:=callClass;
end;
//property setterControls_TWinControl_OnExit
function set_Controls_TWinControl_OnExit(p:TWinControl;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnExit:=@callClass.call;
Result:=callClass;
end;
//property getterControls_TWinControl_Showing
function get_Controls_TWinControl_Showing(p:TWinControl):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Showing);
end;
//property getterControls_TWinControl_UseDockManager
function get_Controls_TWinControl_UseDockManager(p:TWinControl):Integer;cdecl;
begin
Result:=BooleanTointegert(p.UseDockManager);
end;
//property setterControls_TWinControl_UseDockManager
procedure set_Controls_TWinControl_UseDockManager(p:TWinControl;v:Integer);cdecl; 
begin
p.UseDockManager:=integertToBoolean(v);
end;
//property getterControls_TWinControl_DesignerDeleting
function get_Controls_TWinControl_DesignerDeleting(p:TWinControl):Integer;cdecl;
begin
Result:=BooleanTointegert(p.DesignerDeleting);
end;
//property setterControls_TWinControl_DesignerDeleting
procedure set_Controls_TWinControl_DesignerDeleting(p:TWinControl;v:Integer);cdecl; 
begin
p.DesignerDeleting:=integertToBoolean(v);
end;
//property getterControls_TWinControl_VisibleDockClientCount
function get_Controls_TWinControl_VisibleDockClientCount(p:TWinControl):Integer;cdecl;
begin
Result:=Integer(p.VisibleDockClientCount);
end;
//constructorControls_TWinControl_Create
function Controls_TWinControl_Create(TheOwner:tcomponent):TWinControl;cdecl;
begin
Result:=TWinControl.Create((TheOwner));
end;
//constructorControls_TCustomControl_Create
function Controls_TCustomControl_Create(AOwner:tcomponent):TCustomControl;cdecl;
begin
Result:=TCustomControl.Create((AOwner));
end;
//property getterControls_TCustomControl_Canvas
function get_Controls_TCustomControl_Canvas(p:TCustomControl):tcanvas;cdecl;
begin
Result:=tcanvas(p.Canvas);
end;
//property setterControls_TCustomControl_Canvas
procedure set_Controls_TCustomControl_Canvas(p:TCustomControl;v:tcanvas);cdecl; 
begin
p.Canvas:=(v);
end;
//property setterControls_TCustomControl_OnPaint
function set_Controls_TCustomControl_OnPaint(p:TCustomControl;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnPaint:=@callClass.call;
Result:=callClass;
end;
//constructorForms_TScrollingWinControl_Create
function Forms_TScrollingWinControl_Create(TheOwner:tcomponent):TScrollingWinControl;cdecl;
begin
Result:=TScrollingWinControl.Create((TheOwner));
end;
//constructorForms_TControlScrollBar_Create
function Forms_TControlScrollBar_Create(AControl:twincontrol;AKind:tscrollbarkind):TControlScrollBar;cdecl;
begin
Result:=TControlScrollBar.Create((AControl),(AKind));
end;
//property getterForms_TControlScrollBar_Kind
function get_Forms_TControlScrollBar_Kind(p:TControlScrollBar):Integer;cdecl;
begin
Result:=Integer(p.Kind);
end;
//property getterForms_TControlScrollBar_Size
function get_Forms_TControlScrollBar_Size(p:TControlScrollBar):Integer;cdecl;
begin
Result:=Integer(p.Size);
end;
//property getterForms_TControlScrollBar_Smooth
function get_Forms_TControlScrollBar_Smooth(p:TControlScrollBar):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Smooth);
end;
//property setterForms_TControlScrollBar_Smooth
procedure set_Forms_TControlScrollBar_Smooth(p:TControlScrollBar;v:Integer);cdecl; 
begin
p.Smooth:=integertToBoolean(v);
end;
//property getterForms_TControlScrollBar_Position
function get_Forms_TControlScrollBar_Position(p:TControlScrollBar):Integer;cdecl;
begin
Result:=Integer(p.Position);
end;
//property setterForms_TControlScrollBar_Position
procedure set_Forms_TControlScrollBar_Position(p:TControlScrollBar;v:Integer);cdecl; 
begin
p.Position:=(v);
end;
//property getterForms_TControlScrollBar_Range
function get_Forms_TControlScrollBar_Range(p:TControlScrollBar):Integer;cdecl;
begin
Result:=Integer(p.Range);
end;
//property setterForms_TControlScrollBar_Range
procedure set_Forms_TControlScrollBar_Range(p:TControlScrollBar;v:Integer);cdecl; 
begin
p.Range:=(v);
end;
//property getterForms_TControlScrollBar_Tracking
function get_Forms_TControlScrollBar_Tracking(p:TControlScrollBar):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Tracking);
end;
//property setterForms_TControlScrollBar_Tracking
procedure set_Forms_TControlScrollBar_Tracking(p:TControlScrollBar;v:Integer);cdecl; 
begin
p.Tracking:=integertToBoolean(v);
end;
//property getterForms_TControlScrollBar_Visible
function get_Forms_TControlScrollBar_Visible(p:TControlScrollBar):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Visible);
end;
//property setterForms_TControlScrollBar_Visible
procedure set_Forms_TControlScrollBar_Visible(p:TControlScrollBar;v:Integer);cdecl; 
begin
p.Visible:=integertToBoolean(v);
end;
//property getterForms_TScrollingWinControl_HorzScrollBar
function get_Forms_TScrollingWinControl_HorzScrollBar(p:TScrollingWinControl):tcontrolscrollbar;cdecl;
begin
Result:=tcontrolscrollbar(p.HorzScrollBar);
end;
//property setterForms_TScrollingWinControl_HorzScrollBar
procedure set_Forms_TScrollingWinControl_HorzScrollBar(p:TScrollingWinControl;v:tcontrolscrollbar);cdecl; 
begin
p.HorzScrollBar:=(v);
end;
//property getterForms_TScrollingWinControl_VertScrollBar
function get_Forms_TScrollingWinControl_VertScrollBar(p:TScrollingWinControl):tcontrolscrollbar;cdecl;
begin
Result:=tcontrolscrollbar(p.VertScrollBar);
end;
//property setterForms_TScrollingWinControl_VertScrollBar
procedure set_Forms_TScrollingWinControl_VertScrollBar(p:TScrollingWinControl;v:tcontrolscrollbar);cdecl; 
begin
p.VertScrollBar:=(v);
end;
//constructorForms_TCustomDesignControl_Create
function Forms_TCustomDesignControl_Create(TheOwner:tcomponent):TCustomDesignControl;cdecl;
begin
Result:=TCustomDesignControl.Create((TheOwner));
end;
//property getterForms_TCustomDesignControl_DesignTimeDPI
function get_Forms_TCustomDesignControl_DesignTimeDPI(p:TCustomDesignControl):Integer;cdecl;
begin
Result:=Integer(p.DesignTimeDPI);
end;
//property setterForms_TCustomDesignControl_DesignTimeDPI
procedure set_Forms_TCustomDesignControl_DesignTimeDPI(p:TCustomDesignControl;v:Integer);cdecl; 
begin
p.DesignTimeDPI:=(v);
end;
//property getterForms_TCustomDesignControl_DesignTimePPI
function get_Forms_TCustomDesignControl_DesignTimePPI(p:TCustomDesignControl):Integer;cdecl;
begin
Result:=Integer(p.DesignTimePPI);
end;
//property setterForms_TCustomDesignControl_DesignTimePPI
procedure set_Forms_TCustomDesignControl_DesignTimePPI(p:TCustomDesignControl;v:Integer);cdecl; 
begin
p.DesignTimePPI:=(v);
end;
//property getterForms_TCustomDesignControl_PixelsPerInch
function get_Forms_TCustomDesignControl_PixelsPerInch(p:TCustomDesignControl):Integer;cdecl;
begin
Result:=Integer(p.PixelsPerInch);
end;
//property setterForms_TCustomDesignControl_PixelsPerInch
procedure set_Forms_TCustomDesignControl_PixelsPerInch(p:TCustomDesignControl;v:Integer);cdecl; 
begin
p.PixelsPerInch:=(v);
end;
//property getterForms_TCustomDesignControl_Scaled
function get_Forms_TCustomDesignControl_Scaled(p:TCustomDesignControl):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Scaled);
end;
//property setterForms_TCustomDesignControl_Scaled
procedure set_Forms_TCustomDesignControl_Scaled(p:TCustomDesignControl;v:Integer);cdecl; 
begin
p.Scaled:=integertToBoolean(v);
end;
//constructorForms_TCustomForm_Create
function Forms_TCustomForm_Create(AOwner:tcomponent):TCustomForm;cdecl;
begin
Result:=TCustomForm.Create((AOwner));
end;
//constructorForms_TCustomForm_CreateNew
function Forms_TCustomForm_CreateNew(AOwner:tcomponent;Num:Integer):TCustomForm;cdecl;
begin
Result:=TCustomForm.CreateNew((AOwner),(Num));
end;
//property getterForms_TCustomForm_Active
function get_Forms_TCustomForm_Active(p:TCustomForm):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Active);
end;
//property getterForms_TCustomForm_ActiveControl
function get_Forms_TCustomForm_ActiveControl(p:TCustomForm):twincontrol;cdecl;
begin
Result:=twincontrol(p.ActiveControl);
end;
//property setterForms_TCustomForm_ActiveControl
procedure set_Forms_TCustomForm_ActiveControl(p:TCustomForm;v:twincontrol);cdecl; 
begin
p.ActiveControl:=(v);
end;
//property getterForms_TCustomForm_ActiveDefaultControl
function get_Forms_TCustomForm_ActiveDefaultControl(p:TCustomForm):tcontrol;cdecl;
begin
Result:=tcontrol(p.ActiveDefaultControl);
end;
//property setterForms_TCustomForm_ActiveDefaultControl
procedure set_Forms_TCustomForm_ActiveDefaultControl(p:TCustomForm;v:tcontrol);cdecl; 
begin
p.ActiveDefaultControl:=(v);
end;
//property getterForms_TCustomForm_AllowDropFiles
function get_Forms_TCustomForm_AllowDropFiles(p:TCustomForm):Integer;cdecl;
begin
Result:=BooleanTointegert(p.AllowDropFiles);
end;
//property setterForms_TCustomForm_AllowDropFiles
procedure set_Forms_TCustomForm_AllowDropFiles(p:TCustomForm;v:Integer);cdecl; 
begin
p.AllowDropFiles:=integertToBoolean(v);
end;
//property getterForms_TCustomForm_AlphaBlend
function get_Forms_TCustomForm_AlphaBlend(p:TCustomForm):Integer;cdecl;
begin
Result:=BooleanTointegert(p.AlphaBlend);
end;
//property setterForms_TCustomForm_AlphaBlend
procedure set_Forms_TCustomForm_AlphaBlend(p:TCustomForm;v:Integer);cdecl; 
begin
p.AlphaBlend:=integertToBoolean(v);
end;
//property getterForms_TCustomForm_AutoScroll
function get_Forms_TCustomForm_AutoScroll(p:TCustomForm):Integer;cdecl;
begin
Result:=BooleanTointegert(p.AutoScroll);
end;
//property setterForms_TCustomForm_AutoScroll
procedure set_Forms_TCustomForm_AutoScroll(p:TCustomForm;v:Integer);cdecl; 
begin
p.AutoScroll:=integertToBoolean(v);
end;
//property getterForms_TCustomForm_BorderIcons
function get_Forms_TCustomForm_BorderIcons(p:TCustomForm):Integer;cdecl;
begin
Result:=Integer(p.BorderIcons);
end;
//property setterForms_TCustomForm_BorderIcons
procedure set_Forms_TCustomForm_BorderIcons(p:TCustomForm;v:tbordericons);cdecl; 
begin
p.BorderIcons:=(v);
end;
//property getterForms_TCustomForm_BorderStyle
function get_Forms_TCustomForm_BorderStyle(p:TCustomForm):Integer;cdecl;
begin
Result:=Integer(p.BorderStyle);
end;
//property setterForms_TCustomForm_BorderStyle
procedure set_Forms_TCustomForm_BorderStyle(p:TCustomForm;v:tformborderstyle);cdecl; 
begin
p.BorderStyle:=(v);
end;
//property getterForms_TCustomForm_CancelControl
function get_Forms_TCustomForm_CancelControl(p:TCustomForm):tcontrol;cdecl;
begin
Result:=tcontrol(p.CancelControl);
end;
//property setterForms_TCustomForm_CancelControl
procedure set_Forms_TCustomForm_CancelControl(p:TCustomForm;v:tcontrol);cdecl; 
begin
p.CancelControl:=(v);
end;
//property getterForms_TCustomForm_DefaultControl
function get_Forms_TCustomForm_DefaultControl(p:TCustomForm):tcontrol;cdecl;
begin
Result:=tcontrol(p.DefaultControl);
end;
//property setterForms_TCustomForm_DefaultControl
procedure set_Forms_TCustomForm_DefaultControl(p:TCustomForm;v:tcontrol);cdecl; 
begin
p.DefaultControl:=(v);
end;
//property getterForms_TCustomForm_DefaultMonitor
function get_Forms_TCustomForm_DefaultMonitor(p:TCustomForm):Integer;cdecl;
begin
Result:=Integer(p.DefaultMonitor);
end;
//property setterForms_TCustomForm_DefaultMonitor
procedure set_Forms_TCustomForm_DefaultMonitor(p:TCustomForm;v:tdefaultmonitor);cdecl; 
begin
p.DefaultMonitor:=(v);
end;
//property getterForms_TIDesigner_LookupRoot
function get_Forms_TIDesigner_LookupRoot(p:TIDesigner):tcomponent;cdecl;
begin
Result:=tcomponent(p.LookupRoot);
end;
//property getterForms_TIDesigner_DefaultFormBoundsValid
function get_Forms_TIDesigner_DefaultFormBoundsValid(p:TIDesigner):Integer;cdecl;
begin
Result:=BooleanTointegert(p.DefaultFormBoundsValid);
end;
//property setterForms_TIDesigner_DefaultFormBoundsValid
procedure set_Forms_TIDesigner_DefaultFormBoundsValid(p:TIDesigner;v:Integer);cdecl; 
begin
p.DefaultFormBoundsValid:=integertToBoolean(v);
end;
//property getterForms_TCustomForm_Designer
function get_Forms_TCustomForm_Designer(p:TCustomForm):tidesigner;cdecl;
begin
Result:=tidesigner(p.Designer);
end;
//property setterForms_TCustomForm_Designer
procedure set_Forms_TCustomForm_Designer(p:TCustomForm;v:tidesigner);cdecl; 
begin
p.Designer:=(v);
end;
//property getterForms_TCustomForm_EffectiveShowInTaskBar
function get_Forms_TCustomForm_EffectiveShowInTaskBar(p:TCustomForm):Integer;cdecl;
begin
Result:=Integer(p.EffectiveShowInTaskBar);
end;
//property getterForms_TCustomForm_FormState
function get_Forms_TCustomForm_FormState(p:TCustomForm):Integer;cdecl;
begin
Result:=Integer(p.FormState);
end;
//property getterForms_TCustomForm_FormStyle
function get_Forms_TCustomForm_FormStyle(p:TCustomForm):Integer;cdecl;
begin
Result:=Integer(p.FormStyle);
end;
//property setterForms_TCustomForm_FormStyle
procedure set_Forms_TCustomForm_FormStyle(p:TCustomForm;v:tformstyle);cdecl; 
begin
p.FormStyle:=(v);
end;
//property getterForms_TCustomForm_HelpFile
function get_Forms_TCustomForm_HelpFile(p:TCustomForm):PChar;cdecl;
begin
Result:=PChar(p.HelpFile);
end;
//property setterForms_TCustomForm_HelpFile
procedure set_Forms_TCustomForm_HelpFile(p:TCustomForm;v:PChar);cdecl; 
begin
p.HelpFile:=(v);
end;
//constructorGraphics_TCustomIcon_Create
function Graphics_TCustomIcon_Create():TCustomIcon;cdecl;
begin
Result:=TCustomIcon.Create();
end;
//property getterGraphics_TCustomIcon_Current
function get_Graphics_TCustomIcon_Current(p:TCustomIcon):Integer;cdecl;
begin
Result:=Integer(p.Current);
end;
//property setterGraphics_TCustomIcon_Current
procedure set_Graphics_TCustomIcon_Current(p:TCustomIcon;v:Integer);cdecl; 
begin
p.Current:=(v);
end;
//property getterGraphics_TCustomIcon_Count
function get_Graphics_TCustomIcon_Count(p:TCustomIcon):Integer;cdecl;
begin
Result:=Integer(p.Count);
end;
//constructorGraphics_TIcon_Create
function Graphics_TIcon_Create():TIcon;cdecl;
begin
Result:=TIcon.Create();
end;
//property getterForms_TCustomForm_Icon
function get_Forms_TCustomForm_Icon(p:TCustomForm):ticon;cdecl;
begin
Result:=ticon(p.Icon);
end;
//property setterForms_TCustomForm_Icon
procedure set_Forms_TCustomForm_Icon(p:TCustomForm;v:ticon);cdecl; 
begin
p.Icon:=(v);
end;
//property getterForms_TCustomForm_KeyPreview
function get_Forms_TCustomForm_KeyPreview(p:TCustomForm):Integer;cdecl;
begin
Result:=BooleanTointegert(p.KeyPreview);
end;
//property setterForms_TCustomForm_KeyPreview
procedure set_Forms_TCustomForm_KeyPreview(p:TCustomForm;v:Integer);cdecl; 
begin
p.KeyPreview:=integertToBoolean(v);
end;
//property getterForms_TCustomForm_MDIChildren
function get_Forms_TCustomForm_MDIChildren(p:TCustomForm;I:Integer):tcustomform;cdecl;
begin
Result:=tcustomform(p.MDIChildren[I]);
end;
//constructorMenus_TMainMenu_Create
function Menus_TMainMenu_Create(AOwner:tcomponent):TMainMenu;cdecl;
begin
Result:=TMainMenu.Create((AOwner));
end;
//property getterMenus_TMainMenu_Height
function get_Menus_TMainMenu_Height(p:TMainMenu):Integer;cdecl;
begin
Result:=Integer(p.Height);
end;
//property setterMenus_TMainMenu_OnChange
function set_Menus_TMainMenu_OnChange(p:TMainMenu;newMethod:Menus_TMenuChangeEvent;OldEvent:MenusTMenuChangeEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:MenusTMenuChangeEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=MenusTMenuChangeEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnChange:=@callClass.call;
Result:=callClass;
end;
//property getterForms_TCustomForm_Menu
function get_Forms_TCustomForm_Menu(p:TCustomForm):tmainmenu;cdecl;
begin
Result:=tmainmenu(p.Menu);
end;
//property setterForms_TCustomForm_Menu
procedure set_Forms_TCustomForm_Menu(p:TCustomForm;v:tmainmenu);cdecl; 
begin
p.Menu:=(v);
end;
//property getterForms_TMonitor_MonitorNum
function get_Forms_TMonitor_MonitorNum(p:TMonitor):Integer;cdecl;
begin
Result:=Integer(p.MonitorNum);
end;
//property getterForms_TMonitor_Left
function get_Forms_TMonitor_Left(p:TMonitor):Integer;cdecl;
begin
Result:=Integer(p.Left);
end;
//property getterForms_TMonitor_Height
function get_Forms_TMonitor_Height(p:TMonitor):Integer;cdecl;
begin
Result:=Integer(p.Height);
end;
//property getterForms_TMonitor_Top
function get_Forms_TMonitor_Top(p:TMonitor):Integer;cdecl;
begin
Result:=Integer(p.Top);
end;
//property getterForms_TMonitor_Width
function get_Forms_TMonitor_Width(p:TMonitor):Integer;cdecl;
begin
Result:=Integer(p.Width);
end;
//property getterForms_TMonitor_Primary
function get_Forms_TMonitor_Primary(p:TMonitor):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Primary);
end;
//property getterForms_TMonitor_PixelsPerInch
function get_Forms_TMonitor_PixelsPerInch(p:TMonitor):Integer;cdecl;
begin
Result:=Integer(p.PixelsPerInch);
end;
//property getterForms_TCustomForm_Monitor
function get_Forms_TCustomForm_Monitor(p:TCustomForm):tmonitor;cdecl;
begin
Result:=tmonitor(p.Monitor);
end;
//property getterForms_TCustomForm_PopupMode
function get_Forms_TCustomForm_PopupMode(p:TCustomForm):Integer;cdecl;
begin
Result:=Integer(p.PopupMode);
end;
//property setterForms_TCustomForm_PopupMode
procedure set_Forms_TCustomForm_PopupMode(p:TCustomForm;v:tpopupmode);cdecl; 
begin
p.PopupMode:=(v);
end;
//property getterForms_TCustomForm_PopupParent
function get_Forms_TCustomForm_PopupParent(p:TCustomForm):tcustomform;cdecl;
begin
Result:=tcustomform(p.PopupParent);
end;
//property setterForms_TCustomForm_PopupParent
procedure set_Forms_TCustomForm_PopupParent(p:TCustomForm;v:tcustomform);cdecl; 
begin
p.PopupParent:=(v);
end;
//property setterForms_TCustomForm_OnActivate
function set_Forms_TCustomForm_OnActivate(p:TCustomForm;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnActivate:=@callClass.call;
Result:=callClass;
end;
//property setterForms_TCustomForm_OnClose
function set_Forms_TCustomForm_OnClose(p:TCustomForm;newMethod:Forms_TCloseEvent;OldEvent:FormsTCloseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:FormsTCloseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=FormsTCloseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnClose:=@callClass.call;
Result:=callClass;
end;
//property setterForms_TCustomForm_OnCloseQuery
function set_Forms_TCustomForm_OnCloseQuery(p:TCustomForm;newMethod:Forms_TCloseQueryEvent;OldEvent:FormsTCloseQueryEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:FormsTCloseQueryEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=FormsTCloseQueryEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnCloseQuery:=@callClass.call;
Result:=callClass;
end;
//property setterForms_TCustomForm_OnCreate
function set_Forms_TCustomForm_OnCreate(p:TCustomForm;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnCreate:=@callClass.call;
Result:=callClass;
end;
//property setterForms_TCustomForm_OnDeactivate
function set_Forms_TCustomForm_OnDeactivate(p:TCustomForm;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDeactivate:=@callClass.call;
Result:=callClass;
end;
//property setterForms_TCustomForm_OnDestroy
function set_Forms_TCustomForm_OnDestroy(p:TCustomForm;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDestroy:=@callClass.call;
Result:=callClass;
end;
//property setterForms_TCustomForm_OnHide
function set_Forms_TCustomForm_OnHide(p:TCustomForm;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnHide:=@callClass.call;
Result:=callClass;
end;
//property setterForms_TCustomForm_OnShow
function set_Forms_TCustomForm_OnShow(p:TCustomForm;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnShow:=@callClass.call;
Result:=callClass;
end;
//property setterForms_TCustomForm_OnShowModalFinished
function set_Forms_TCustomForm_OnShowModalFinished(p:TCustomForm;newMethod:Forms_TModalDialogFinished;OldEvent:FormsTModalDialogFinished_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:FormsTModalDialogFinished_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=FormsTModalDialogFinished_wrapper.Create;
callClass.c:=newMethod;
p.OnShowModalFinished:=@callClass.call;
Result:=callClass;
end;
//property setterForms_TCustomForm_OnWindowStateChange
function set_Forms_TCustomForm_OnWindowStateChange(p:TCustomForm;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnWindowStateChange:=@callClass.call;
Result:=callClass;
end;
//property getterForms_TCustomForm_ParentFont
function get_Forms_TCustomForm_ParentFont(p:TCustomForm):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentFont);
end;
//property setterForms_TCustomForm_ParentFont
procedure set_Forms_TCustomForm_ParentFont(p:TCustomForm;v:Integer);cdecl; 
begin
p.ParentFont:=integertToBoolean(v);
end;
//property getterForms_TCustomForm_Position
function get_Forms_TCustomForm_Position(p:TCustomForm):Integer;cdecl;
begin
Result:=Integer(p.Position);
end;
//property setterForms_TCustomForm_Position
procedure set_Forms_TCustomForm_Position(p:TCustomForm;v:tposition);cdecl; 
begin
p.Position:=(v);
end;
//property getterForms_TCustomForm_RestoredLeft
function get_Forms_TCustomForm_RestoredLeft(p:TCustomForm):Integer;cdecl;
begin
Result:=Integer(p.RestoredLeft);
end;
//property getterForms_TCustomForm_RestoredTop
function get_Forms_TCustomForm_RestoredTop(p:TCustomForm):Integer;cdecl;
begin
Result:=Integer(p.RestoredTop);
end;
//property getterForms_TCustomForm_RestoredWidth
function get_Forms_TCustomForm_RestoredWidth(p:TCustomForm):Integer;cdecl;
begin
Result:=Integer(p.RestoredWidth);
end;
//property getterForms_TCustomForm_RestoredHeight
function get_Forms_TCustomForm_RestoredHeight(p:TCustomForm):Integer;cdecl;
begin
Result:=Integer(p.RestoredHeight);
end;
//property getterForms_TCustomForm_ShowInTaskBar
function get_Forms_TCustomForm_ShowInTaskBar(p:TCustomForm):Integer;cdecl;
begin
Result:=Integer(p.ShowInTaskBar);
end;
//property setterForms_TCustomForm_ShowInTaskBar
procedure set_Forms_TCustomForm_ShowInTaskBar(p:TCustomForm;v:tshowintaskbar);cdecl; 
begin
p.ShowInTaskBar:=(v);
end;
//property getterForms_TCustomForm_WindowState
function get_Forms_TCustomForm_WindowState(p:TCustomForm):Integer;cdecl;
begin
Result:=Integer(p.WindowState);
end;
//property setterForms_TCustomForm_WindowState
procedure set_Forms_TCustomForm_WindowState(p:TCustomForm;v:twindowstate);cdecl; 
begin
p.WindowState:=(v);
end;
//constructorForms_TForm_Create
function Forms_TForm_Create(TheOwner:tcomponent):TForm;cdecl;
begin
Result:=TForm.Create((TheOwner));
end;
//property getterForms_TForm_DragKind
function get_Forms_TForm_DragKind(p:TForm):Integer;cdecl;
begin
Result:=Integer(p.DragKind);
end;
//property setterForms_TForm_DragKind
procedure set_Forms_TForm_DragKind(p:TForm;v:tdragkind);cdecl; 
begin
p.DragKind:=(v);
end;
//property getterForms_TForm_DragMode
function get_Forms_TForm_DragMode(p:TForm):Integer;cdecl;
begin
Result:=Integer(p.DragMode);
end;
//property setterForms_TForm_DragMode
procedure set_Forms_TForm_DragMode(p:TForm;v:tdragmode);cdecl; 
begin
p.DragMode:=(v);
end;
//property setterForms_TForm_OnDblClick
function set_Forms_TForm_OnDblClick(p:TForm;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDblClick:=@callClass.call;
Result:=callClass;
end;
//property setterForms_TForm_OnDragDrop
function set_Forms_TForm_OnDragDrop(p:TForm;newMethod:Controls_TDragDropEvent;OldEvent:ControlsTDragDropEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragDropEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragDropEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragDrop:=@callClass.call;
Result:=callClass;
end;
//property setterForms_TForm_OnDragOver
function set_Forms_TForm_OnDragOver(p:TForm;newMethod:Controls_TDragOverEvent;OldEvent:ControlsTDragOverEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragOverEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragOverEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragOver:=@callClass.call;
Result:=callClass;
end;
//property setterForms_TForm_OnEndDock
function set_Forms_TForm_OnEndDock(p:TForm;newMethod:Controls_TEndDragEvent;OldEvent:ControlsTEndDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTEndDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTEndDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEndDock:=@callClass.call;
Result:=callClass;
end;
//property setterForms_TForm_OnMouseDown
function set_Forms_TForm_OnMouseDown(p:TForm;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseDown:=@callClass.call;
Result:=callClass;
end;
//property setterForms_TForm_OnMouseEnter
function set_Forms_TForm_OnMouseEnter(p:TForm;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseEnter:=@callClass.call;
Result:=callClass;
end;
//property setterForms_TForm_OnMouseLeave
function set_Forms_TForm_OnMouseLeave(p:TForm;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseLeave:=@callClass.call;
Result:=callClass;
end;
//property setterForms_TForm_OnMouseMove
function set_Forms_TForm_OnMouseMove(p:TForm;newMethod:Controls_TMouseMoveEvent;OldEvent:ControlsTMouseMoveEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseMoveEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseMoveEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseMove:=@callClass.call;
Result:=callClass;
end;
//property setterForms_TForm_OnMouseUp
function set_Forms_TForm_OnMouseUp(p:TForm;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseUp:=@callClass.call;
Result:=callClass;
end;
//property setterForms_TForm_OnStartDock
function set_Forms_TForm_OnStartDock(p:TForm;newMethod:Controls_TStartDockEvent;OldEvent:ControlsTStartDockEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTStartDockEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTStartDockEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnStartDock:=@callClass.call;
Result:=callClass;
end;
//property getterForms_TForm_SessionProperties
function get_Forms_TForm_SessionProperties(p:TForm):PChar;cdecl;
begin
Result:=PChar(p.SessionProperties);
end;
//property setterForms_TForm_SessionProperties
procedure set_Forms_TForm_SessionProperties(p:TForm;v:PChar);cdecl; 
begin
p.SessionProperties:=(v);
end;
//property getterForms_TForm_LCLVersion
function get_Forms_TForm_LCLVersion(p:TForm):PChar;cdecl;
begin
Result:=PChar(p.LCLVersion);
end;
//property setterForms_TForm_LCLVersion
procedure set_Forms_TForm_LCLVersion(p:TForm;v:PChar);cdecl; 
begin
p.LCLVersion:=(v);
end;
//constructorExtCtrls_TCustomPanel_Create
function ExtCtrls_TCustomPanel_Create(TheOwner:tcomponent):TCustomPanel;cdecl;
begin
Result:=TCustomPanel.Create((TheOwner));
end;
//property getterExtCtrls_TCustomPanel_Alignment
function get_ExtCtrls_TCustomPanel_Alignment(p:TCustomPanel):Integer;cdecl;
begin
Result:=Integer(p.Alignment);
end;
//property setterExtCtrls_TCustomPanel_Alignment
procedure set_ExtCtrls_TCustomPanel_Alignment(p:TCustomPanel;v:talignment);cdecl; 
begin
p.Alignment:=(v);
end;
//property getterExtCtrls_TCustomPanel_FullRepaint
function get_ExtCtrls_TCustomPanel_FullRepaint(p:TCustomPanel):Integer;cdecl;
begin
Result:=BooleanTointegert(p.FullRepaint);
end;
//property setterExtCtrls_TCustomPanel_FullRepaint
procedure set_ExtCtrls_TCustomPanel_FullRepaint(p:TCustomPanel;v:Integer);cdecl; 
begin
p.FullRepaint:=integertToBoolean(v);
end;
//property getterExtCtrls_TCustomPanel_ParentColor
function get_ExtCtrls_TCustomPanel_ParentColor(p:TCustomPanel):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentColor);
end;
//property setterExtCtrls_TCustomPanel_ParentColor
procedure set_ExtCtrls_TCustomPanel_ParentColor(p:TCustomPanel;v:Integer);cdecl; 
begin
p.ParentColor:=integertToBoolean(v);
end;
//property getterExtCtrls_TPanel_DragKind
function get_ExtCtrls_TPanel_DragKind(p:TPanel):Integer;cdecl;
begin
Result:=Integer(p.DragKind);
end;
//property setterExtCtrls_TPanel_DragKind
procedure set_ExtCtrls_TPanel_DragKind(p:TPanel;v:tdragkind);cdecl; 
begin
p.DragKind:=(v);
end;
//property getterExtCtrls_TPanel_DragMode
function get_ExtCtrls_TPanel_DragMode(p:TPanel):Integer;cdecl;
begin
Result:=Integer(p.DragMode);
end;
//property setterExtCtrls_TPanel_DragMode
procedure set_ExtCtrls_TPanel_DragMode(p:TPanel;v:tdragmode);cdecl; 
begin
p.DragMode:=(v);
end;
//property getterExtCtrls_TPanel_ParentFont
function get_ExtCtrls_TPanel_ParentFont(p:TPanel):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentFont);
end;
//property setterExtCtrls_TPanel_ParentFont
procedure set_ExtCtrls_TPanel_ParentFont(p:TPanel;v:Integer);cdecl; 
begin
p.ParentFont:=integertToBoolean(v);
end;
//property getterExtCtrls_TPanel_ParentShowHint
function get_ExtCtrls_TPanel_ParentShowHint(p:TPanel):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentShowHint);
end;
//property setterExtCtrls_TPanel_ParentShowHint
procedure set_ExtCtrls_TPanel_ParentShowHint(p:TPanel;v:Integer);cdecl; 
begin
p.ParentShowHint:=integertToBoolean(v);
end;
//property setterExtCtrls_TPanel_OnDblClick
function set_ExtCtrls_TPanel_OnDblClick(p:TPanel;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDblClick:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TPanel_OnDragDrop
function set_ExtCtrls_TPanel_OnDragDrop(p:TPanel;newMethod:Controls_TDragDropEvent;OldEvent:ControlsTDragDropEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragDropEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragDropEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragDrop:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TPanel_OnDragOver
function set_ExtCtrls_TPanel_OnDragOver(p:TPanel;newMethod:Controls_TDragOverEvent;OldEvent:ControlsTDragOverEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragOverEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragOverEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragOver:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TPanel_OnEndDock
function set_ExtCtrls_TPanel_OnEndDock(p:TPanel;newMethod:Controls_TEndDragEvent;OldEvent:ControlsTEndDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTEndDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTEndDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEndDock:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TPanel_OnEndDrag
function set_ExtCtrls_TPanel_OnEndDrag(p:TPanel;newMethod:Controls_TEndDragEvent;OldEvent:ControlsTEndDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTEndDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTEndDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEndDrag:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TPanel_OnGetDockCaption
function set_ExtCtrls_TPanel_OnGetDockCaption(p:TPanel;newMethod:Controls_TGetDockCaptionEvent;OldEvent:ControlsTGetDockCaptionEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTGetDockCaptionEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTGetDockCaptionEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnGetDockCaption:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TPanel_OnMouseDown
function set_ExtCtrls_TPanel_OnMouseDown(p:TPanel;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseDown:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TPanel_OnMouseEnter
function set_ExtCtrls_TPanel_OnMouseEnter(p:TPanel;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseEnter:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TPanel_OnMouseLeave
function set_ExtCtrls_TPanel_OnMouseLeave(p:TPanel;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseLeave:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TPanel_OnMouseMove
function set_ExtCtrls_TPanel_OnMouseMove(p:TPanel;newMethod:Controls_TMouseMoveEvent;OldEvent:ControlsTMouseMoveEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseMoveEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseMoveEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseMove:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TPanel_OnMouseUp
function set_ExtCtrls_TPanel_OnMouseUp(p:TPanel;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseUp:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TPanel_OnStartDock
function set_ExtCtrls_TPanel_OnStartDock(p:TPanel;newMethod:Controls_TStartDockEvent;OldEvent:ControlsTStartDockEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTStartDockEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTStartDockEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnStartDock:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TPanel_OnStartDrag
function set_ExtCtrls_TPanel_OnStartDrag(p:TPanel;newMethod:Controls_TStartDragEvent;OldEvent:ControlsTStartDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTStartDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTStartDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnStartDrag:=@callClass.call;
Result:=callClass;
end;
//constructorExtCtrls_TPanel_Create
function ExtCtrls_TPanel_Create(TheOwner:tcomponent):TPanel;cdecl;
begin
Result:=TPanel.Create((TheOwner));
end;
//constructorStdCtrls_TButtonControl_Create
function StdCtrls_TButtonControl_Create(TheOwner:tcomponent):TButtonControl;cdecl;
begin
Result:=TButtonControl.Create((TheOwner));
end;
//constructorStdCtrls_TCustomButton_Create
function StdCtrls_TCustomButton_Create(TheOwner:tcomponent):TCustomButton;cdecl;
begin
Result:=TCustomButton.Create((TheOwner));
end;
//property getterStdCtrls_TCustomButton_Active
function get_StdCtrls_TCustomButton_Active(p:TCustomButton):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Active);
end;
//property getterStdCtrls_TCustomButton_Default
function get_StdCtrls_TCustomButton_Default(p:TCustomButton):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Default);
end;
//property setterStdCtrls_TCustomButton_Default
procedure set_StdCtrls_TCustomButton_Default(p:TCustomButton;v:Integer);cdecl; 
begin
p.Default:=integertToBoolean(v);
end;
//property getterStdCtrls_TCustomButton_Cancel
function get_StdCtrls_TCustomButton_Cancel(p:TCustomButton):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Cancel);
end;
//property setterStdCtrls_TCustomButton_Cancel
procedure set_StdCtrls_TCustomButton_Cancel(p:TCustomButton;v:Integer);cdecl; 
begin
p.Cancel:=integertToBoolean(v);
end;
//property getterStdCtrls_TButton_DragKind
function get_StdCtrls_TButton_DragKind(p:TButton):Integer;cdecl;
begin
Result:=Integer(p.DragKind);
end;
//property setterStdCtrls_TButton_DragKind
procedure set_StdCtrls_TButton_DragKind(p:TButton;v:tdragkind);cdecl; 
begin
p.DragKind:=(v);
end;
//property getterStdCtrls_TButton_DragMode
function get_StdCtrls_TButton_DragMode(p:TButton):Integer;cdecl;
begin
Result:=Integer(p.DragMode);
end;
//property setterStdCtrls_TButton_DragMode
procedure set_StdCtrls_TButton_DragMode(p:TButton;v:tdragmode);cdecl; 
begin
p.DragMode:=(v);
end;
//property setterStdCtrls_TButton_OnDragDrop
function set_StdCtrls_TButton_OnDragDrop(p:TButton;newMethod:Controls_TDragDropEvent;OldEvent:ControlsTDragDropEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragDropEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragDropEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragDrop:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TButton_OnDragOver
function set_StdCtrls_TButton_OnDragOver(p:TButton;newMethod:Controls_TDragOverEvent;OldEvent:ControlsTDragOverEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragOverEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragOverEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragOver:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TButton_OnEndDrag
function set_StdCtrls_TButton_OnEndDrag(p:TButton;newMethod:Controls_TEndDragEvent;OldEvent:ControlsTEndDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTEndDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTEndDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEndDrag:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TButton_OnMouseDown
function set_StdCtrls_TButton_OnMouseDown(p:TButton;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseDown:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TButton_OnMouseEnter
function set_StdCtrls_TButton_OnMouseEnter(p:TButton;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseEnter:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TButton_OnMouseLeave
function set_StdCtrls_TButton_OnMouseLeave(p:TButton;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseLeave:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TButton_OnMouseMove
function set_StdCtrls_TButton_OnMouseMove(p:TButton;newMethod:Controls_TMouseMoveEvent;OldEvent:ControlsTMouseMoveEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseMoveEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseMoveEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseMove:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TButton_OnMouseUp
function set_StdCtrls_TButton_OnMouseUp(p:TButton;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseUp:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TButton_OnStartDrag
function set_StdCtrls_TButton_OnStartDrag(p:TButton;newMethod:Controls_TStartDragEvent;OldEvent:ControlsTStartDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTStartDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTStartDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnStartDrag:=@callClass.call;
Result:=callClass;
end;
//property getterStdCtrls_TButton_ParentFont
function get_StdCtrls_TButton_ParentFont(p:TButton):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentFont);
end;
//property setterStdCtrls_TButton_ParentFont
procedure set_StdCtrls_TButton_ParentFont(p:TButton;v:Integer);cdecl; 
begin
p.ParentFont:=integertToBoolean(v);
end;
//property getterStdCtrls_TButton_ParentShowHint
function get_StdCtrls_TButton_ParentShowHint(p:TButton):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentShowHint);
end;
//property setterStdCtrls_TButton_ParentShowHint
procedure set_StdCtrls_TButton_ParentShowHint(p:TButton;v:Integer);cdecl; 
begin
p.ParentShowHint:=integertToBoolean(v);
end;
//constructorStdCtrls_TButton_Create
function StdCtrls_TButton_Create(TheOwner:tcomponent):TButton;cdecl;
begin
Result:=TButton.Create((TheOwner));
end;
//constructorStdCtrls_TCustomCheckBox_Create
function StdCtrls_TCustomCheckBox_Create(TheOwner:tcomponent):TCustomCheckBox;cdecl;
begin
Result:=TCustomCheckBox.Create((TheOwner));
end;
//property getterStdCtrls_TCustomCheckBox_AllowGrayed
function get_StdCtrls_TCustomCheckBox_AllowGrayed(p:TCustomCheckBox):Integer;cdecl;
begin
Result:=BooleanTointegert(p.AllowGrayed);
end;
//property setterStdCtrls_TCustomCheckBox_AllowGrayed
procedure set_StdCtrls_TCustomCheckBox_AllowGrayed(p:TCustomCheckBox;v:Integer);cdecl; 
begin
p.AllowGrayed:=integertToBoolean(v);
end;
//property getterStdCtrls_TCustomCheckBox_State
function get_StdCtrls_TCustomCheckBox_State(p:TCustomCheckBox):Integer;cdecl;
begin
Result:=Integer(p.State);
end;
//property setterStdCtrls_TCustomCheckBox_State
procedure set_StdCtrls_TCustomCheckBox_State(p:TCustomCheckBox;v:tcheckboxstate);cdecl; 
begin
p.State:=(v);
end;
//property setterStdCtrls_TCustomCheckBox_OnChange
function set_StdCtrls_TCustomCheckBox_OnChange(p:TCustomCheckBox;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnChange:=@callClass.call;
Result:=callClass;
end;
//constructorStdCtrls_TRadioButton_Create
function StdCtrls_TRadioButton_Create(TheOwner:tcomponent):TRadioButton;cdecl;
begin
Result:=TRadioButton.Create((TheOwner));
end;
//property getterStdCtrls_TRadioButton_Checked
function get_StdCtrls_TRadioButton_Checked(p:TRadioButton):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Checked);
end;
//property setterStdCtrls_TRadioButton_Checked
procedure set_StdCtrls_TRadioButton_Checked(p:TRadioButton;v:Integer);cdecl; 
begin
p.Checked:=integertToBoolean(v);
end;
//property getterStdCtrls_TRadioButton_DragKind
function get_StdCtrls_TRadioButton_DragKind(p:TRadioButton):Integer;cdecl;
begin
Result:=Integer(p.DragKind);
end;
//property setterStdCtrls_TRadioButton_DragKind
procedure set_StdCtrls_TRadioButton_DragKind(p:TRadioButton;v:tdragkind);cdecl; 
begin
p.DragKind:=(v);
end;
//property getterStdCtrls_TRadioButton_DragMode
function get_StdCtrls_TRadioButton_DragMode(p:TRadioButton):Integer;cdecl;
begin
Result:=Integer(p.DragMode);
end;
//property setterStdCtrls_TRadioButton_DragMode
procedure set_StdCtrls_TRadioButton_DragMode(p:TRadioButton;v:tdragmode);cdecl; 
begin
p.DragMode:=(v);
end;
//property setterStdCtrls_TRadioButton_OnDragDrop
function set_StdCtrls_TRadioButton_OnDragDrop(p:TRadioButton;newMethod:Controls_TDragDropEvent;OldEvent:ControlsTDragDropEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragDropEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragDropEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragDrop:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TRadioButton_OnDragOver
function set_StdCtrls_TRadioButton_OnDragOver(p:TRadioButton;newMethod:Controls_TDragOverEvent;OldEvent:ControlsTDragOverEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragOverEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragOverEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragOver:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TRadioButton_OnEndDrag
function set_StdCtrls_TRadioButton_OnEndDrag(p:TRadioButton;newMethod:Controls_TEndDragEvent;OldEvent:ControlsTEndDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTEndDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTEndDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEndDrag:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TRadioButton_OnMouseDown
function set_StdCtrls_TRadioButton_OnMouseDown(p:TRadioButton;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseDown:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TRadioButton_OnMouseEnter
function set_StdCtrls_TRadioButton_OnMouseEnter(p:TRadioButton;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseEnter:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TRadioButton_OnMouseLeave
function set_StdCtrls_TRadioButton_OnMouseLeave(p:TRadioButton;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseLeave:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TRadioButton_OnMouseMove
function set_StdCtrls_TRadioButton_OnMouseMove(p:TRadioButton;newMethod:Controls_TMouseMoveEvent;OldEvent:ControlsTMouseMoveEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseMoveEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseMoveEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseMove:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TRadioButton_OnMouseUp
function set_StdCtrls_TRadioButton_OnMouseUp(p:TRadioButton;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseUp:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TRadioButton_OnStartDrag
function set_StdCtrls_TRadioButton_OnStartDrag(p:TRadioButton;newMethod:Controls_TStartDragEvent;OldEvent:ControlsTStartDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTStartDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTStartDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnStartDrag:=@callClass.call;
Result:=callClass;
end;
//property getterStdCtrls_TRadioButton_ParentColor
function get_StdCtrls_TRadioButton_ParentColor(p:TRadioButton):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentColor);
end;
//property setterStdCtrls_TRadioButton_ParentColor
procedure set_StdCtrls_TRadioButton_ParentColor(p:TRadioButton;v:Integer);cdecl; 
begin
p.ParentColor:=integertToBoolean(v);
end;
//property getterStdCtrls_TRadioButton_ParentFont
function get_StdCtrls_TRadioButton_ParentFont(p:TRadioButton):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentFont);
end;
//property setterStdCtrls_TRadioButton_ParentFont
procedure set_StdCtrls_TRadioButton_ParentFont(p:TRadioButton;v:Integer);cdecl; 
begin
p.ParentFont:=integertToBoolean(v);
end;
//property getterStdCtrls_TRadioButton_ParentShowHint
function get_StdCtrls_TRadioButton_ParentShowHint(p:TRadioButton):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentShowHint);
end;
//property setterStdCtrls_TRadioButton_ParentShowHint
procedure set_StdCtrls_TRadioButton_ParentShowHint(p:TRadioButton;v:Integer);cdecl; 
begin
p.ParentShowHint:=integertToBoolean(v);
end;
//constructorStdCtrls_TCheckBox_Create
function StdCtrls_TCheckBox_Create(TheOwner:tcomponent):TCheckBox;cdecl;
begin
Result:=TCheckBox.Create((TheOwner));
end;
//property getterStdCtrls_TCheckBox_Checked
function get_StdCtrls_TCheckBox_Checked(p:TCheckBox):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Checked);
end;
//property setterStdCtrls_TCheckBox_Checked
procedure set_StdCtrls_TCheckBox_Checked(p:TCheckBox;v:Integer);cdecl; 
begin
p.Checked:=integertToBoolean(v);
end;
//property getterStdCtrls_TCheckBox_DragKind
function get_StdCtrls_TCheckBox_DragKind(p:TCheckBox):Integer;cdecl;
begin
Result:=Integer(p.DragKind);
end;
//property setterStdCtrls_TCheckBox_DragKind
procedure set_StdCtrls_TCheckBox_DragKind(p:TCheckBox;v:tdragkind);cdecl; 
begin
p.DragKind:=(v);
end;
//property getterStdCtrls_TCheckBox_DragMode
function get_StdCtrls_TCheckBox_DragMode(p:TCheckBox):Integer;cdecl;
begin
Result:=Integer(p.DragMode);
end;
//property setterStdCtrls_TCheckBox_DragMode
procedure set_StdCtrls_TCheckBox_DragMode(p:TCheckBox;v:tdragmode);cdecl; 
begin
p.DragMode:=(v);
end;
//property setterStdCtrls_TCheckBox_OnDragDrop
function set_StdCtrls_TCheckBox_OnDragDrop(p:TCheckBox;newMethod:Controls_TDragDropEvent;OldEvent:ControlsTDragDropEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragDropEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragDropEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragDrop:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TCheckBox_OnDragOver
function set_StdCtrls_TCheckBox_OnDragOver(p:TCheckBox;newMethod:Controls_TDragOverEvent;OldEvent:ControlsTDragOverEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragOverEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragOverEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragOver:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TCheckBox_OnEditingDone
function set_StdCtrls_TCheckBox_OnEditingDone(p:TCheckBox;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEditingDone:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TCheckBox_OnEndDrag
function set_StdCtrls_TCheckBox_OnEndDrag(p:TCheckBox;newMethod:Controls_TEndDragEvent;OldEvent:ControlsTEndDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTEndDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTEndDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEndDrag:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TCheckBox_OnMouseDown
function set_StdCtrls_TCheckBox_OnMouseDown(p:TCheckBox;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseDown:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TCheckBox_OnMouseEnter
function set_StdCtrls_TCheckBox_OnMouseEnter(p:TCheckBox;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseEnter:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TCheckBox_OnMouseLeave
function set_StdCtrls_TCheckBox_OnMouseLeave(p:TCheckBox;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseLeave:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TCheckBox_OnMouseMove
function set_StdCtrls_TCheckBox_OnMouseMove(p:TCheckBox;newMethod:Controls_TMouseMoveEvent;OldEvent:ControlsTMouseMoveEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseMoveEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseMoveEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseMove:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TCheckBox_OnMouseUp
function set_StdCtrls_TCheckBox_OnMouseUp(p:TCheckBox;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseUp:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TCheckBox_OnStartDrag
function set_StdCtrls_TCheckBox_OnStartDrag(p:TCheckBox;newMethod:Controls_TStartDragEvent;OldEvent:ControlsTStartDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTStartDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTStartDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnStartDrag:=@callClass.call;
Result:=callClass;
end;
//property getterStdCtrls_TCheckBox_ParentColor
function get_StdCtrls_TCheckBox_ParentColor(p:TCheckBox):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentColor);
end;
//property setterStdCtrls_TCheckBox_ParentColor
procedure set_StdCtrls_TCheckBox_ParentColor(p:TCheckBox;v:Integer);cdecl; 
begin
p.ParentColor:=integertToBoolean(v);
end;
//property getterStdCtrls_TCheckBox_ParentFont
function get_StdCtrls_TCheckBox_ParentFont(p:TCheckBox):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentFont);
end;
//property setterStdCtrls_TCheckBox_ParentFont
procedure set_StdCtrls_TCheckBox_ParentFont(p:TCheckBox;v:Integer);cdecl; 
begin
p.ParentFont:=integertToBoolean(v);
end;
//property getterStdCtrls_TCheckBox_ParentShowHint
function get_StdCtrls_TCheckBox_ParentShowHint(p:TCheckBox):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentShowHint);
end;
//property setterStdCtrls_TCheckBox_ParentShowHint
procedure set_StdCtrls_TCheckBox_ParentShowHint(p:TCheckBox;v:Integer);cdecl; 
begin
p.ParentShowHint:=integertToBoolean(v);
end;
//constructorStdCtrls_TToggleBox_Create
function StdCtrls_TToggleBox_Create(TheOwner:tcomponent):TToggleBox;cdecl;
begin
Result:=TToggleBox.Create((TheOwner));
end;
//property getterStdCtrls_TToggleBox_Checked
function get_StdCtrls_TToggleBox_Checked(p:TToggleBox):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Checked);
end;
//property setterStdCtrls_TToggleBox_Checked
procedure set_StdCtrls_TToggleBox_Checked(p:TToggleBox;v:Integer);cdecl; 
begin
p.Checked:=integertToBoolean(v);
end;
//property getterStdCtrls_TToggleBox_DragKind
function get_StdCtrls_TToggleBox_DragKind(p:TToggleBox):Integer;cdecl;
begin
Result:=Integer(p.DragKind);
end;
//property setterStdCtrls_TToggleBox_DragKind
procedure set_StdCtrls_TToggleBox_DragKind(p:TToggleBox;v:tdragkind);cdecl; 
begin
p.DragKind:=(v);
end;
//property getterStdCtrls_TToggleBox_DragMode
function get_StdCtrls_TToggleBox_DragMode(p:TToggleBox):Integer;cdecl;
begin
Result:=Integer(p.DragMode);
end;
//property setterStdCtrls_TToggleBox_DragMode
procedure set_StdCtrls_TToggleBox_DragMode(p:TToggleBox;v:tdragmode);cdecl; 
begin
p.DragMode:=(v);
end;
//property setterStdCtrls_TToggleBox_OnDragDrop
function set_StdCtrls_TToggleBox_OnDragDrop(p:TToggleBox;newMethod:Controls_TDragDropEvent;OldEvent:ControlsTDragDropEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragDropEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragDropEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragDrop:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TToggleBox_OnDragOver
function set_StdCtrls_TToggleBox_OnDragOver(p:TToggleBox;newMethod:Controls_TDragOverEvent;OldEvent:ControlsTDragOverEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragOverEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragOverEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragOver:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TToggleBox_OnEndDrag
function set_StdCtrls_TToggleBox_OnEndDrag(p:TToggleBox;newMethod:Controls_TEndDragEvent;OldEvent:ControlsTEndDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTEndDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTEndDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEndDrag:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TToggleBox_OnMouseDown
function set_StdCtrls_TToggleBox_OnMouseDown(p:TToggleBox;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseDown:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TToggleBox_OnMouseEnter
function set_StdCtrls_TToggleBox_OnMouseEnter(p:TToggleBox;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseEnter:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TToggleBox_OnMouseLeave
function set_StdCtrls_TToggleBox_OnMouseLeave(p:TToggleBox;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseLeave:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TToggleBox_OnMouseMove
function set_StdCtrls_TToggleBox_OnMouseMove(p:TToggleBox;newMethod:Controls_TMouseMoveEvent;OldEvent:ControlsTMouseMoveEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseMoveEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseMoveEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseMove:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TToggleBox_OnMouseUp
function set_StdCtrls_TToggleBox_OnMouseUp(p:TToggleBox;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseUp:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TToggleBox_OnStartDrag
function set_StdCtrls_TToggleBox_OnStartDrag(p:TToggleBox;newMethod:Controls_TStartDragEvent;OldEvent:ControlsTStartDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTStartDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTStartDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnStartDrag:=@callClass.call;
Result:=callClass;
end;
//property getterStdCtrls_TToggleBox_ParentFont
function get_StdCtrls_TToggleBox_ParentFont(p:TToggleBox):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentFont);
end;
//property setterStdCtrls_TToggleBox_ParentFont
procedure set_StdCtrls_TToggleBox_ParentFont(p:TToggleBox;v:Integer);cdecl; 
begin
p.ParentFont:=integertToBoolean(v);
end;
//property getterStdCtrls_TToggleBox_ParentShowHint
function get_StdCtrls_TToggleBox_ParentShowHint(p:TToggleBox):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentShowHint);
end;
//property setterStdCtrls_TToggleBox_ParentShowHint
procedure set_StdCtrls_TToggleBox_ParentShowHint(p:TToggleBox;v:Integer);cdecl; 
begin
p.ParentShowHint:=integertToBoolean(v);
end;
//constructorStdCtrls_TCustomComboBox_Create
function StdCtrls_TCustomComboBox_Create(TheOwner:tcomponent):TCustomComboBox;cdecl;
begin
Result:=TCustomComboBox.Create((TheOwner));
end;
//property getterStdCtrls_TCustomComboBox_CharCase
function get_StdCtrls_TCustomComboBox_CharCase(p:TCustomComboBox):Integer;cdecl;
begin
Result:=Integer(p.CharCase);
end;
//property setterStdCtrls_TCustomComboBox_CharCase
procedure set_StdCtrls_TCustomComboBox_CharCase(p:TCustomComboBox;v:teditcharcase);cdecl; 
begin
p.CharCase:=(v);
end;
//property getterStdCtrls_TCustomComboBox_DroppedDown
function get_StdCtrls_TCustomComboBox_DroppedDown(p:TCustomComboBox):Integer;cdecl;
begin
Result:=BooleanTointegert(p.DroppedDown);
end;
//property setterStdCtrls_TCustomComboBox_DroppedDown
procedure set_StdCtrls_TCustomComboBox_DroppedDown(p:TCustomComboBox;v:Integer);cdecl; 
begin
p.DroppedDown:=integertToBoolean(v);
end;
//property getterStdCtrls_TCustomComboBox_DroppingDown
function get_StdCtrls_TCustomComboBox_DroppingDown(p:TCustomComboBox):Integer;cdecl;
begin
Result:=BooleanTointegert(p.DroppingDown);
end;
//property setterStdCtrls_TCustomComboBox_DroppingDown
procedure set_StdCtrls_TCustomComboBox_DroppingDown(p:TCustomComboBox;v:Integer);cdecl; 
begin
p.DroppingDown:=integertToBoolean(v);
end;
//property getterStdCtrls_TCustomComboBox_AutoComplete
function get_StdCtrls_TCustomComboBox_AutoComplete(p:TCustomComboBox):Integer;cdecl;
begin
Result:=BooleanTointegert(p.AutoComplete);
end;
//property setterStdCtrls_TCustomComboBox_AutoComplete
procedure set_StdCtrls_TCustomComboBox_AutoComplete(p:TCustomComboBox;v:Integer);cdecl; 
begin
p.AutoComplete:=integertToBoolean(v);
end;
//property getterStdCtrls_TCustomComboBox_AutoCompleteText
function get_StdCtrls_TCustomComboBox_AutoCompleteText(p:TCustomComboBox):Integer;cdecl;
begin
Result:=Integer(p.AutoCompleteText);
end;
//property setterStdCtrls_TCustomComboBox_AutoCompleteText
procedure set_StdCtrls_TCustomComboBox_AutoCompleteText(p:TCustomComboBox;v:tcomboboxautocompletetext);cdecl; 
begin
p.AutoCompleteText:=(v);
end;
//property getterStdCtrls_TCustomComboBox_AutoDropDown
function get_StdCtrls_TCustomComboBox_AutoDropDown(p:TCustomComboBox):Integer;cdecl;
begin
Result:=BooleanTointegert(p.AutoDropDown);
end;
//property setterStdCtrls_TCustomComboBox_AutoDropDown
procedure set_StdCtrls_TCustomComboBox_AutoDropDown(p:TCustomComboBox;v:Integer);cdecl; 
begin
p.AutoDropDown:=integertToBoolean(v);
end;
//property getterStdCtrls_TCustomComboBox_AutoSelect
function get_StdCtrls_TCustomComboBox_AutoSelect(p:TCustomComboBox):Integer;cdecl;
begin
Result:=BooleanTointegert(p.AutoSelect);
end;
//property setterStdCtrls_TCustomComboBox_AutoSelect
procedure set_StdCtrls_TCustomComboBox_AutoSelect(p:TCustomComboBox;v:Integer);cdecl; 
begin
p.AutoSelect:=integertToBoolean(v);
end;
//property getterStdCtrls_TCustomComboBox_AutoSelected
function get_StdCtrls_TCustomComboBox_AutoSelected(p:TCustomComboBox):Integer;cdecl;
begin
Result:=BooleanTointegert(p.AutoSelected);
end;
//property setterStdCtrls_TCustomComboBox_AutoSelected
procedure set_StdCtrls_TCustomComboBox_AutoSelected(p:TCustomComboBox;v:Integer);cdecl; 
begin
p.AutoSelected:=integertToBoolean(v);
end;
//property getterStdCtrls_TCustomComboBox_ArrowKeysTraverseList
function get_StdCtrls_TCustomComboBox_ArrowKeysTraverseList(p:TCustomComboBox):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ArrowKeysTraverseList);
end;
//property setterStdCtrls_TCustomComboBox_ArrowKeysTraverseList
procedure set_StdCtrls_TCustomComboBox_ArrowKeysTraverseList(p:TCustomComboBox;v:Integer);cdecl; 
begin
p.ArrowKeysTraverseList:=integertToBoolean(v);
end;
//property getterStdCtrls_TCustomComboBox_Canvas
function get_StdCtrls_TCustomComboBox_Canvas(p:TCustomComboBox):tcanvas;cdecl;
begin
Result:=tcanvas(p.Canvas);
end;
//property getterStdCtrls_TCustomComboBox_DropDownCount
function get_StdCtrls_TCustomComboBox_DropDownCount(p:TCustomComboBox):Integer;cdecl;
begin
Result:=Integer(p.DropDownCount);
end;
//property setterStdCtrls_TCustomComboBox_DropDownCount
procedure set_StdCtrls_TCustomComboBox_DropDownCount(p:TCustomComboBox;v:Integer);cdecl; 
begin
p.DropDownCount:=(v);
end;
//property getterClasses_TStrings_DelimitedText
function get_Classes_TStrings_DelimitedText(p:TStrings):PChar;cdecl;
begin
Result:=PChar(p.DelimitedText);
end;
//property setterClasses_TStrings_DelimitedText
procedure set_Classes_TStrings_DelimitedText(p:TStrings;v:PChar);cdecl; 
begin
p.DelimitedText:=(v);
end;
//property getterClasses_TStrings_LineBreak
function get_Classes_TStrings_LineBreak(p:TStrings):PChar;cdecl;
begin
Result:=PChar(p.LineBreak);
end;
//property setterClasses_TStrings_LineBreak
procedure set_Classes_TStrings_LineBreak(p:TStrings;v:PChar);cdecl; 
begin
p.LineBreak:=(v);
end;
//property getterClasses_TStrings_StrictDelimiter
function get_Classes_TStrings_StrictDelimiter(p:TStrings):Integer;cdecl;
begin
Result:=BooleanTointegert(p.StrictDelimiter);
end;
//property setterClasses_TStrings_StrictDelimiter
procedure set_Classes_TStrings_StrictDelimiter(p:TStrings;v:Integer);cdecl; 
begin
p.StrictDelimiter:=integertToBoolean(v);
end;
//property getterClasses_TStrings_ValueFromIndex
function get_Classes_TStrings_ValueFromIndex(p:TStrings;Index:Integer):PChar;cdecl;
begin
Result:=PChar(p.ValueFromIndex[Index]);
end;
//property setterClasses_TStrings_ValueFromIndex
procedure set_Classes_TStrings_ValueFromIndex(p:TStrings;Index:Integer;v:PChar);cdecl; 
begin
p.ValueFromIndex[Index]:=(v);
end;
//property getterClasses_TStrings_Capacity
function get_Classes_TStrings_Capacity(p:TStrings):Integer;cdecl;
begin
Result:=Integer(p.Capacity);
end;
//property setterClasses_TStrings_Capacity
procedure set_Classes_TStrings_Capacity(p:TStrings;v:Integer);cdecl; 
begin
p.Capacity:=(v);
end;
//property getterClasses_TStrings_CommaText
function get_Classes_TStrings_CommaText(p:TStrings):PChar;cdecl;
begin
Result:=PChar(p.CommaText);
end;
//property setterClasses_TStrings_CommaText
procedure set_Classes_TStrings_CommaText(p:TStrings;v:PChar);cdecl; 
begin
p.CommaText:=(v);
end;
//property getterClasses_TStrings_Count
function get_Classes_TStrings_Count(p:TStrings):Integer;cdecl;
begin
Result:=Integer(p.Count);
end;
//property getterClasses_TStrings_Names
function get_Classes_TStrings_Names(p:TStrings;Index:Integer):PChar;cdecl;
begin
Result:=PChar(p.Names[Index]);
end;
//property getterClasses_TStrings_Objects
function get_Classes_TStrings_Objects(p:TStrings;Index:Integer):tobject;cdecl;
begin
Result:=tobject(p.Objects[Index]);
end;
//property setterClasses_TStrings_Objects
procedure set_Classes_TStrings_Objects(p:TStrings;Index:Integer;v:tobject);cdecl; 
begin
p.Objects[Index]:=(v);
end;
//property getterClasses_TStrings_Strings
function get_Classes_TStrings_Strings(p:TStrings;Index:Integer):PChar;cdecl;
begin
Result:=PChar(p.Strings[Index]);
end;
//property setterClasses_TStrings_Strings
procedure set_Classes_TStrings_Strings(p:TStrings;Index:Integer;v:PChar);cdecl; 
begin
p.Strings[Index]:=(v);
end;
//property getterClasses_TStrings_Text
function get_Classes_TStrings_Text(p:TStrings):PChar;cdecl;
begin
Result:=PChar(p.Text);
end;
//property setterClasses_TStrings_Text
procedure set_Classes_TStrings_Text(p:TStrings;v:PChar);cdecl; 
begin
p.Text:=(v);
end;
//property getterClasses_TStrings_StringsAdapter
function get_Classes_TStrings_StringsAdapter(p:TStrings):istringsadapter;cdecl;
begin
Result:=istringsadapter(p.StringsAdapter);
end;
//property setterClasses_TStrings_StringsAdapter
procedure set_Classes_TStrings_StringsAdapter(p:TStrings;v:istringsadapter);cdecl; 
begin
p.StringsAdapter:=(v);
end;
//property getterClasses_TStrings_SkipLastLineBreak
function get_Classes_TStrings_SkipLastLineBreak(p:TStrings):Integer;cdecl;
begin
Result:=BooleanTointegert(p.SkipLastLineBreak);
end;
//property setterClasses_TStrings_SkipLastLineBreak
procedure set_Classes_TStrings_SkipLastLineBreak(p:TStrings;v:Integer);cdecl; 
begin
p.SkipLastLineBreak:=integertToBoolean(v);
end;
//property getterStdCtrls_TCustomComboBox_Items
function get_StdCtrls_TCustomComboBox_Items(p:TCustomComboBox):tstrings;cdecl;
begin
Result:=tstrings(p.Items);
end;
//property setterStdCtrls_TCustomComboBox_Items
procedure set_StdCtrls_TCustomComboBox_Items(p:TCustomComboBox;v:tstrings);cdecl; 
begin
p.Items:=(v);
end;
//property getterStdCtrls_TCustomComboBox_ItemIndex
function get_StdCtrls_TCustomComboBox_ItemIndex(p:TCustomComboBox):Integer;cdecl;
begin
Result:=Integer(p.ItemIndex);
end;
//property setterStdCtrls_TCustomComboBox_ItemIndex
procedure set_StdCtrls_TCustomComboBox_ItemIndex(p:TCustomComboBox;v:Integer);cdecl; 
begin
p.ItemIndex:=(v);
end;
//property getterStdCtrls_TCustomComboBox_ReadOnly
function get_StdCtrls_TCustomComboBox_ReadOnly(p:TCustomComboBox):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ReadOnly);
end;
//property setterStdCtrls_TCustomComboBox_ReadOnly
procedure set_StdCtrls_TCustomComboBox_ReadOnly(p:TCustomComboBox;v:Integer);cdecl; 
begin
p.ReadOnly:=integertToBoolean(v);
end;
//property getterStdCtrls_TCustomComboBox_SelLength
function get_StdCtrls_TCustomComboBox_SelLength(p:TCustomComboBox):Integer;cdecl;
begin
Result:=Integer(p.SelLength);
end;
//property setterStdCtrls_TCustomComboBox_SelLength
procedure set_StdCtrls_TCustomComboBox_SelLength(p:TCustomComboBox;v:Integer);cdecl; 
begin
p.SelLength:=(v);
end;
//property getterStdCtrls_TCustomComboBox_SelStart
function get_StdCtrls_TCustomComboBox_SelStart(p:TCustomComboBox):Integer;cdecl;
begin
Result:=Integer(p.SelStart);
end;
//property setterStdCtrls_TCustomComboBox_SelStart
procedure set_StdCtrls_TCustomComboBox_SelStart(p:TCustomComboBox;v:Integer);cdecl; 
begin
p.SelStart:=(v);
end;
//property getterStdCtrls_TCustomComboBox_SelText
function get_StdCtrls_TCustomComboBox_SelText(p:TCustomComboBox):PChar;cdecl;
begin
Result:=PChar(p.SelText);
end;
//property setterStdCtrls_TCustomComboBox_SelText
procedure set_StdCtrls_TCustomComboBox_SelText(p:TCustomComboBox;v:PChar);cdecl; 
begin
p.SelText:=(v);
end;
//property getterStdCtrls_TCustomComboBox_Style
function get_StdCtrls_TCustomComboBox_Style(p:TCustomComboBox):Integer;cdecl;
begin
Result:=Integer(p.Style);
end;
//property setterStdCtrls_TCustomComboBox_Style
procedure set_StdCtrls_TCustomComboBox_Style(p:TCustomComboBox;v:tcomboboxstyle);cdecl; 
begin
p.Style:=(v);
end;
//property getterStdCtrls_TCustomComboBox_Text
function get_StdCtrls_TCustomComboBox_Text(p:TCustomComboBox):PChar;cdecl;
begin
Result:=PChar(p.Text);
end;
//property setterStdCtrls_TCustomComboBox_Text
procedure set_StdCtrls_TCustomComboBox_Text(p:TCustomComboBox;v:PChar);cdecl; 
begin
p.Text:=(v);
end;
//property getterStdCtrls_TComboBox_DragKind
function get_StdCtrls_TComboBox_DragKind(p:TComboBox):Integer;cdecl;
begin
Result:=Integer(p.DragKind);
end;
//property setterStdCtrls_TComboBox_DragKind
procedure set_StdCtrls_TComboBox_DragKind(p:TComboBox;v:tdragkind);cdecl; 
begin
p.DragKind:=(v);
end;
//property getterStdCtrls_TComboBox_DragMode
function get_StdCtrls_TComboBox_DragMode(p:TComboBox):Integer;cdecl;
begin
Result:=Integer(p.DragMode);
end;
//property setterStdCtrls_TComboBox_DragMode
procedure set_StdCtrls_TComboBox_DragMode(p:TComboBox;v:tdragmode);cdecl; 
begin
p.DragMode:=(v);
end;
//property getterStdCtrls_TComboBox_ItemHeight
function get_StdCtrls_TComboBox_ItemHeight(p:TComboBox):Integer;cdecl;
begin
Result:=Integer(p.ItemHeight);
end;
//property setterStdCtrls_TComboBox_ItemHeight
procedure set_StdCtrls_TComboBox_ItemHeight(p:TComboBox;v:Integer);cdecl; 
begin
p.ItemHeight:=(v);
end;
//property getterStdCtrls_TComboBox_ItemWidth
function get_StdCtrls_TComboBox_ItemWidth(p:TComboBox):Integer;cdecl;
begin
Result:=Integer(p.ItemWidth);
end;
//property setterStdCtrls_TComboBox_ItemWidth
procedure set_StdCtrls_TComboBox_ItemWidth(p:TComboBox;v:Integer);cdecl; 
begin
p.ItemWidth:=(v);
end;
//property getterStdCtrls_TComboBox_MaxLength
function get_StdCtrls_TComboBox_MaxLength(p:TComboBox):Integer;cdecl;
begin
Result:=Integer(p.MaxLength);
end;
//property setterStdCtrls_TComboBox_MaxLength
procedure set_StdCtrls_TComboBox_MaxLength(p:TComboBox;v:Integer);cdecl; 
begin
p.MaxLength:=(v);
end;
//property setterStdCtrls_TComboBox_OnChange
function set_StdCtrls_TComboBox_OnChange(p:TComboBox;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnChange:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TComboBox_OnCloseUp
function set_StdCtrls_TComboBox_OnCloseUp(p:TComboBox;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnCloseUp:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TComboBox_OnDblClick
function set_StdCtrls_TComboBox_OnDblClick(p:TComboBox;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDblClick:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TComboBox_OnDragDrop
function set_StdCtrls_TComboBox_OnDragDrop(p:TComboBox;newMethod:Controls_TDragDropEvent;OldEvent:ControlsTDragDropEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragDropEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragDropEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragDrop:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TComboBox_OnDragOver
function set_StdCtrls_TComboBox_OnDragOver(p:TComboBox;newMethod:Controls_TDragOverEvent;OldEvent:ControlsTDragOverEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragOverEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragOverEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragOver:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TComboBox_OnEndDrag
function set_StdCtrls_TComboBox_OnEndDrag(p:TComboBox;newMethod:Controls_TEndDragEvent;OldEvent:ControlsTEndDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTEndDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTEndDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEndDrag:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TComboBox_OnDropDown
function set_StdCtrls_TComboBox_OnDropDown(p:TComboBox;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDropDown:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TComboBox_OnEditingDone
function set_StdCtrls_TComboBox_OnEditingDone(p:TComboBox;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEditingDone:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TComboBox_OnGetItems
function set_StdCtrls_TComboBox_OnGetItems(p:TComboBox;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnGetItems:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TComboBox_OnMeasureItem
function set_StdCtrls_TComboBox_OnMeasureItem(p:TComboBox;newMethod:StdCtrls_TMeasureItemEvent;OldEvent:StdCtrlsTMeasureItemEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:StdCtrlsTMeasureItemEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=StdCtrlsTMeasureItemEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMeasureItem:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TComboBox_OnMouseDown
function set_StdCtrls_TComboBox_OnMouseDown(p:TComboBox;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseDown:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TComboBox_OnMouseEnter
function set_StdCtrls_TComboBox_OnMouseEnter(p:TComboBox;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseEnter:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TComboBox_OnMouseLeave
function set_StdCtrls_TComboBox_OnMouseLeave(p:TComboBox;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseLeave:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TComboBox_OnMouseMove
function set_StdCtrls_TComboBox_OnMouseMove(p:TComboBox;newMethod:Controls_TMouseMoveEvent;OldEvent:ControlsTMouseMoveEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseMoveEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseMoveEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseMove:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TComboBox_OnMouseUp
function set_StdCtrls_TComboBox_OnMouseUp(p:TComboBox;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseUp:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TComboBox_OnSelect
function set_StdCtrls_TComboBox_OnSelect(p:TComboBox;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnSelect:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TComboBox_OnStartDrag
function set_StdCtrls_TComboBox_OnStartDrag(p:TComboBox;newMethod:Controls_TStartDragEvent;OldEvent:ControlsTStartDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTStartDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTStartDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnStartDrag:=@callClass.call;
Result:=callClass;
end;
//property getterStdCtrls_TComboBox_ParentColor
function get_StdCtrls_TComboBox_ParentColor(p:TComboBox):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentColor);
end;
//property setterStdCtrls_TComboBox_ParentColor
procedure set_StdCtrls_TComboBox_ParentColor(p:TComboBox;v:Integer);cdecl; 
begin
p.ParentColor:=integertToBoolean(v);
end;
//property getterStdCtrls_TComboBox_ParentFont
function get_StdCtrls_TComboBox_ParentFont(p:TComboBox):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentFont);
end;
//property setterStdCtrls_TComboBox_ParentFont
procedure set_StdCtrls_TComboBox_ParentFont(p:TComboBox;v:Integer);cdecl; 
begin
p.ParentFont:=integertToBoolean(v);
end;
//property getterStdCtrls_TComboBox_ParentShowHint
function get_StdCtrls_TComboBox_ParentShowHint(p:TComboBox):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentShowHint);
end;
//property setterStdCtrls_TComboBox_ParentShowHint
procedure set_StdCtrls_TComboBox_ParentShowHint(p:TComboBox;v:Integer);cdecl; 
begin
p.ParentShowHint:=integertToBoolean(v);
end;
//property getterStdCtrls_TComboBox_Sorted
function get_StdCtrls_TComboBox_Sorted(p:TComboBox):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Sorted);
end;
//property setterStdCtrls_TComboBox_Sorted
procedure set_StdCtrls_TComboBox_Sorted(p:TComboBox;v:Integer);cdecl; 
begin
p.Sorted:=integertToBoolean(v);
end;
//constructorStdCtrls_TComboBox_Create
function StdCtrls_TComboBox_Create(TheOwner:tcomponent):TComboBox;cdecl;
begin
Result:=TComboBox.Create((TheOwner));
end;
//constructorStdCtrls_TCustomEdit_Create
function StdCtrls_TCustomEdit_Create(AOwner:tcomponent):TCustomEdit;cdecl;
begin
Result:=TCustomEdit.Create((AOwner));
end;
//property getterStdCtrls_TCustomEdit_Alignment
function get_StdCtrls_TCustomEdit_Alignment(p:TCustomEdit):Integer;cdecl;
begin
Result:=Integer(p.Alignment);
end;
//property setterStdCtrls_TCustomEdit_Alignment
procedure set_StdCtrls_TCustomEdit_Alignment(p:TCustomEdit;v:talignment);cdecl; 
begin
p.Alignment:=(v);
end;
//property getterStdCtrls_TCustomEdit_CanUndo
function get_StdCtrls_TCustomEdit_CanUndo(p:TCustomEdit):Integer;cdecl;
begin
Result:=BooleanTointegert(p.CanUndo);
end;
//property getterStdCtrls_TCustomEdit_CharCase
function get_StdCtrls_TCustomEdit_CharCase(p:TCustomEdit):Integer;cdecl;
begin
Result:=Integer(p.CharCase);
end;
//property setterStdCtrls_TCustomEdit_CharCase
procedure set_StdCtrls_TCustomEdit_CharCase(p:TCustomEdit;v:teditcharcase);cdecl; 
begin
p.CharCase:=(v);
end;
//property getterStdCtrls_TCustomEdit_EchoMode
function get_StdCtrls_TCustomEdit_EchoMode(p:TCustomEdit):Integer;cdecl;
begin
Result:=Integer(p.EchoMode);
end;
//property setterStdCtrls_TCustomEdit_EchoMode
procedure set_StdCtrls_TCustomEdit_EchoMode(p:TCustomEdit;v:techomode);cdecl; 
begin
p.EchoMode:=(v);
end;
//property getterStdCtrls_TCustomEdit_HideSelection
function get_StdCtrls_TCustomEdit_HideSelection(p:TCustomEdit):Integer;cdecl;
begin
Result:=BooleanTointegert(p.HideSelection);
end;
//property setterStdCtrls_TCustomEdit_HideSelection
procedure set_StdCtrls_TCustomEdit_HideSelection(p:TCustomEdit;v:Integer);cdecl; 
begin
p.HideSelection:=integertToBoolean(v);
end;
//property getterStdCtrls_TCustomEdit_MaxLength
function get_StdCtrls_TCustomEdit_MaxLength(p:TCustomEdit):Integer;cdecl;
begin
Result:=Integer(p.MaxLength);
end;
//property setterStdCtrls_TCustomEdit_MaxLength
procedure set_StdCtrls_TCustomEdit_MaxLength(p:TCustomEdit;v:Integer);cdecl; 
begin
p.MaxLength:=(v);
end;
//property getterStdCtrls_TCustomEdit_Modified
function get_StdCtrls_TCustomEdit_Modified(p:TCustomEdit):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Modified);
end;
//property setterStdCtrls_TCustomEdit_Modified
procedure set_StdCtrls_TCustomEdit_Modified(p:TCustomEdit;v:Integer);cdecl; 
begin
p.Modified:=integertToBoolean(v);
end;
//property getterStdCtrls_TCustomEdit_NumbersOnly
function get_StdCtrls_TCustomEdit_NumbersOnly(p:TCustomEdit):Integer;cdecl;
begin
Result:=BooleanTointegert(p.NumbersOnly);
end;
//property setterStdCtrls_TCustomEdit_NumbersOnly
procedure set_StdCtrls_TCustomEdit_NumbersOnly(p:TCustomEdit;v:Integer);cdecl; 
begin
p.NumbersOnly:=integertToBoolean(v);
end;
//property setterStdCtrls_TCustomEdit_OnChange
function set_StdCtrls_TCustomEdit_OnChange(p:TCustomEdit;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnChange:=@callClass.call;
Result:=callClass;
end;
//property getterStdCtrls_TCustomEdit_ReadOnly
function get_StdCtrls_TCustomEdit_ReadOnly(p:TCustomEdit):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ReadOnly);
end;
//property setterStdCtrls_TCustomEdit_ReadOnly
procedure set_StdCtrls_TCustomEdit_ReadOnly(p:TCustomEdit;v:Integer);cdecl; 
begin
p.ReadOnly:=integertToBoolean(v);
end;
//property getterStdCtrls_TCustomEdit_SelLength
function get_StdCtrls_TCustomEdit_SelLength(p:TCustomEdit):Integer;cdecl;
begin
Result:=Integer(p.SelLength);
end;
//property setterStdCtrls_TCustomEdit_SelLength
procedure set_StdCtrls_TCustomEdit_SelLength(p:TCustomEdit;v:Integer);cdecl; 
begin
p.SelLength:=(v);
end;
//property getterStdCtrls_TCustomEdit_SelStart
function get_StdCtrls_TCustomEdit_SelStart(p:TCustomEdit):Integer;cdecl;
begin
Result:=Integer(p.SelStart);
end;
//property setterStdCtrls_TCustomEdit_SelStart
procedure set_StdCtrls_TCustomEdit_SelStart(p:TCustomEdit;v:Integer);cdecl; 
begin
p.SelStart:=(v);
end;
//property getterStdCtrls_TCustomEdit_SelText
function get_StdCtrls_TCustomEdit_SelText(p:TCustomEdit):PChar;cdecl;
begin
Result:=PChar(p.SelText);
end;
//property setterStdCtrls_TCustomEdit_SelText
procedure set_StdCtrls_TCustomEdit_SelText(p:TCustomEdit;v:PChar);cdecl; 
begin
p.SelText:=(v);
end;
//property getterStdCtrls_TCustomEdit_Text
function get_StdCtrls_TCustomEdit_Text(p:TCustomEdit):PChar;cdecl;
begin
Result:=PChar(p.Text);
end;
//property setterStdCtrls_TCustomEdit_Text
procedure set_StdCtrls_TCustomEdit_Text(p:TCustomEdit;v:PChar);cdecl; 
begin
p.Text:=(v);
end;
//property getterStdCtrls_TCustomEdit_TextHintFontStyle
function get_StdCtrls_TCustomEdit_TextHintFontStyle(p:TCustomEdit):Integer;cdecl;
begin
Result:=Integer(p.TextHintFontStyle);
end;
//property setterStdCtrls_TCustomEdit_TextHintFontStyle
procedure set_StdCtrls_TCustomEdit_TextHintFontStyle(p:TCustomEdit;v:tfontstyles);cdecl; 
begin
p.TextHintFontStyle:=(v);
end;
//property getterStdCtrls_TEdit_AutoSelected
function get_StdCtrls_TEdit_AutoSelected(p:TEdit):Integer;cdecl;
begin
Result:=BooleanTointegert(p.AutoSelected);
end;
//property setterStdCtrls_TEdit_AutoSelected
procedure set_StdCtrls_TEdit_AutoSelected(p:TEdit;v:Integer);cdecl; 
begin
p.AutoSelected:=integertToBoolean(v);
end;
//property getterStdCtrls_TEdit_AutoSelect
function get_StdCtrls_TEdit_AutoSelect(p:TEdit):Integer;cdecl;
begin
Result:=BooleanTointegert(p.AutoSelect);
end;
//property setterStdCtrls_TEdit_AutoSelect
procedure set_StdCtrls_TEdit_AutoSelect(p:TEdit;v:Integer);cdecl; 
begin
p.AutoSelect:=integertToBoolean(v);
end;
//property getterStdCtrls_TEdit_DragKind
function get_StdCtrls_TEdit_DragKind(p:TEdit):Integer;cdecl;
begin
Result:=Integer(p.DragKind);
end;
//property setterStdCtrls_TEdit_DragKind
procedure set_StdCtrls_TEdit_DragKind(p:TEdit;v:tdragkind);cdecl; 
begin
p.DragKind:=(v);
end;
//property getterStdCtrls_TEdit_DragMode
function get_StdCtrls_TEdit_DragMode(p:TEdit):Integer;cdecl;
begin
Result:=Integer(p.DragMode);
end;
//property setterStdCtrls_TEdit_DragMode
procedure set_StdCtrls_TEdit_DragMode(p:TEdit;v:tdragmode);cdecl; 
begin
p.DragMode:=(v);
end;
//property setterStdCtrls_TEdit_OnDblClick
function set_StdCtrls_TEdit_OnDblClick(p:TEdit;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDblClick:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TEdit_OnDragDrop
function set_StdCtrls_TEdit_OnDragDrop(p:TEdit;newMethod:Controls_TDragDropEvent;OldEvent:ControlsTDragDropEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragDropEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragDropEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragDrop:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TEdit_OnDragOver
function set_StdCtrls_TEdit_OnDragOver(p:TEdit;newMethod:Controls_TDragOverEvent;OldEvent:ControlsTDragOverEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragOverEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragOverEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragOver:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TEdit_OnEditingDone
function set_StdCtrls_TEdit_OnEditingDone(p:TEdit;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEditingDone:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TEdit_OnEndDrag
function set_StdCtrls_TEdit_OnEndDrag(p:TEdit;newMethod:Controls_TEndDragEvent;OldEvent:ControlsTEndDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTEndDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTEndDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEndDrag:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TEdit_OnMouseDown
function set_StdCtrls_TEdit_OnMouseDown(p:TEdit;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseDown:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TEdit_OnMouseEnter
function set_StdCtrls_TEdit_OnMouseEnter(p:TEdit;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseEnter:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TEdit_OnMouseLeave
function set_StdCtrls_TEdit_OnMouseLeave(p:TEdit;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseLeave:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TEdit_OnMouseMove
function set_StdCtrls_TEdit_OnMouseMove(p:TEdit;newMethod:Controls_TMouseMoveEvent;OldEvent:ControlsTMouseMoveEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseMoveEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseMoveEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseMove:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TEdit_OnMouseUp
function set_StdCtrls_TEdit_OnMouseUp(p:TEdit;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseUp:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TEdit_OnStartDrag
function set_StdCtrls_TEdit_OnStartDrag(p:TEdit;newMethod:Controls_TStartDragEvent;OldEvent:ControlsTStartDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTStartDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTStartDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnStartDrag:=@callClass.call;
Result:=callClass;
end;
//property getterStdCtrls_TEdit_ParentColor
function get_StdCtrls_TEdit_ParentColor(p:TEdit):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentColor);
end;
//property setterStdCtrls_TEdit_ParentColor
procedure set_StdCtrls_TEdit_ParentColor(p:TEdit;v:Integer);cdecl; 
begin
p.ParentColor:=integertToBoolean(v);
end;
//property getterStdCtrls_TEdit_ParentFont
function get_StdCtrls_TEdit_ParentFont(p:TEdit):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentFont);
end;
//property setterStdCtrls_TEdit_ParentFont
procedure set_StdCtrls_TEdit_ParentFont(p:TEdit;v:Integer);cdecl; 
begin
p.ParentFont:=integertToBoolean(v);
end;
//property getterStdCtrls_TEdit_ParentShowHint
function get_StdCtrls_TEdit_ParentShowHint(p:TEdit):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentShowHint);
end;
//property setterStdCtrls_TEdit_ParentShowHint
procedure set_StdCtrls_TEdit_ParentShowHint(p:TEdit;v:Integer);cdecl; 
begin
p.ParentShowHint:=integertToBoolean(v);
end;
//constructorStdCtrls_TEdit_Create
function StdCtrls_TEdit_Create(AOwner:tcomponent):TEdit;cdecl;
begin
Result:=TEdit.Create((AOwner));
end;
//constructorStdCtrls_TCustomMemo_Create
function StdCtrls_TCustomMemo_Create(AOwner:tcomponent):TCustomMemo;cdecl;
begin
Result:=TCustomMemo.Create((AOwner));
end;
//property getterStdCtrls_TCustomMemo_Lines
function get_StdCtrls_TCustomMemo_Lines(p:TCustomMemo):tstrings;cdecl;
begin
Result:=tstrings(p.Lines);
end;
//property setterStdCtrls_TCustomMemo_Lines
procedure set_StdCtrls_TCustomMemo_Lines(p:TCustomMemo;v:tstrings);cdecl; 
begin
p.Lines:=(v);
end;
//constructorStdCtrls_TMemoScrollbar_Create
function StdCtrls_TMemoScrollbar_Create(AControl:twincontrol;AKind:tscrollbarkind):TMemoScrollbar;cdecl;
begin
Result:=TMemoScrollbar.Create((AControl),(AKind));
end;
//property getterStdCtrls_TCustomMemo_HorzScrollBar
function get_StdCtrls_TCustomMemo_HorzScrollBar(p:TCustomMemo):tmemoscrollbar;cdecl;
begin
Result:=tmemoscrollbar(p.HorzScrollBar);
end;
//property setterStdCtrls_TCustomMemo_HorzScrollBar
procedure set_StdCtrls_TCustomMemo_HorzScrollBar(p:TCustomMemo;v:tmemoscrollbar);cdecl; 
begin
p.HorzScrollBar:=(v);
end;
//property getterStdCtrls_TCustomMemo_VertScrollBar
function get_StdCtrls_TCustomMemo_VertScrollBar(p:TCustomMemo):tmemoscrollbar;cdecl;
begin
Result:=tmemoscrollbar(p.VertScrollBar);
end;
//property setterStdCtrls_TCustomMemo_VertScrollBar
procedure set_StdCtrls_TCustomMemo_VertScrollBar(p:TCustomMemo;v:tmemoscrollbar);cdecl; 
begin
p.VertScrollBar:=(v);
end;
//property getterStdCtrls_TCustomMemo_ScrollBars
function get_StdCtrls_TCustomMemo_ScrollBars(p:TCustomMemo):Integer;cdecl;
begin
Result:=Integer(p.ScrollBars);
end;
//property setterStdCtrls_TCustomMemo_ScrollBars
procedure set_StdCtrls_TCustomMemo_ScrollBars(p:TCustomMemo;v:tscrollstyle);cdecl; 
begin
p.ScrollBars:=(v);
end;
//property getterStdCtrls_TCustomMemo_WantReturns
function get_StdCtrls_TCustomMemo_WantReturns(p:TCustomMemo):Integer;cdecl;
begin
Result:=BooleanTointegert(p.WantReturns);
end;
//property setterStdCtrls_TCustomMemo_WantReturns
procedure set_StdCtrls_TCustomMemo_WantReturns(p:TCustomMemo;v:Integer);cdecl; 
begin
p.WantReturns:=integertToBoolean(v);
end;
//property getterStdCtrls_TCustomMemo_WantTabs
function get_StdCtrls_TCustomMemo_WantTabs(p:TCustomMemo):Integer;cdecl;
begin
Result:=BooleanTointegert(p.WantTabs);
end;
//property setterStdCtrls_TCustomMemo_WantTabs
procedure set_StdCtrls_TCustomMemo_WantTabs(p:TCustomMemo;v:Integer);cdecl; 
begin
p.WantTabs:=integertToBoolean(v);
end;
//property getterStdCtrls_TCustomMemo_WordWrap
function get_StdCtrls_TCustomMemo_WordWrap(p:TCustomMemo):Integer;cdecl;
begin
Result:=BooleanTointegert(p.WordWrap);
end;
//property setterStdCtrls_TCustomMemo_WordWrap
procedure set_StdCtrls_TCustomMemo_WordWrap(p:TCustomMemo;v:Integer);cdecl; 
begin
p.WordWrap:=integertToBoolean(v);
end;
//property getterStdCtrls_TMemo_DragKind
function get_StdCtrls_TMemo_DragKind(p:TMemo):Integer;cdecl;
begin
Result:=Integer(p.DragKind);
end;
//property setterStdCtrls_TMemo_DragKind
procedure set_StdCtrls_TMemo_DragKind(p:TMemo;v:tdragkind);cdecl; 
begin
p.DragKind:=(v);
end;
//property getterStdCtrls_TMemo_DragMode
function get_StdCtrls_TMemo_DragMode(p:TMemo):Integer;cdecl;
begin
Result:=Integer(p.DragMode);
end;
//property setterStdCtrls_TMemo_DragMode
procedure set_StdCtrls_TMemo_DragMode(p:TMemo;v:tdragmode);cdecl; 
begin
p.DragMode:=(v);
end;
//property setterStdCtrls_TMemo_OnDblClick
function set_StdCtrls_TMemo_OnDblClick(p:TMemo;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDblClick:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TMemo_OnDragDrop
function set_StdCtrls_TMemo_OnDragDrop(p:TMemo;newMethod:Controls_TDragDropEvent;OldEvent:ControlsTDragDropEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragDropEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragDropEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragDrop:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TMemo_OnDragOver
function set_StdCtrls_TMemo_OnDragOver(p:TMemo;newMethod:Controls_TDragOverEvent;OldEvent:ControlsTDragOverEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragOverEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragOverEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragOver:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TMemo_OnEditingDone
function set_StdCtrls_TMemo_OnEditingDone(p:TMemo;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEditingDone:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TMemo_OnEndDrag
function set_StdCtrls_TMemo_OnEndDrag(p:TMemo;newMethod:Controls_TEndDragEvent;OldEvent:ControlsTEndDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTEndDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTEndDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEndDrag:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TMemo_OnMouseDown
function set_StdCtrls_TMemo_OnMouseDown(p:TMemo;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseDown:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TMemo_OnMouseEnter
function set_StdCtrls_TMemo_OnMouseEnter(p:TMemo;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseEnter:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TMemo_OnMouseLeave
function set_StdCtrls_TMemo_OnMouseLeave(p:TMemo;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseLeave:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TMemo_OnMouseMove
function set_StdCtrls_TMemo_OnMouseMove(p:TMemo;newMethod:Controls_TMouseMoveEvent;OldEvent:ControlsTMouseMoveEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseMoveEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseMoveEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseMove:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TMemo_OnMouseUp
function set_StdCtrls_TMemo_OnMouseUp(p:TMemo;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseUp:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TMemo_OnStartDrag
function set_StdCtrls_TMemo_OnStartDrag(p:TMemo;newMethod:Controls_TStartDragEvent;OldEvent:ControlsTStartDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTStartDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTStartDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnStartDrag:=@callClass.call;
Result:=callClass;
end;
//property getterStdCtrls_TMemo_ParentColor
function get_StdCtrls_TMemo_ParentColor(p:TMemo):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentColor);
end;
//property setterStdCtrls_TMemo_ParentColor
procedure set_StdCtrls_TMemo_ParentColor(p:TMemo;v:Integer);cdecl; 
begin
p.ParentColor:=integertToBoolean(v);
end;
//property getterStdCtrls_TMemo_ParentFont
function get_StdCtrls_TMemo_ParentFont(p:TMemo):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentFont);
end;
//property setterStdCtrls_TMemo_ParentFont
procedure set_StdCtrls_TMemo_ParentFont(p:TMemo;v:Integer);cdecl; 
begin
p.ParentFont:=integertToBoolean(v);
end;
//property getterStdCtrls_TMemo_ParentShowHint
function get_StdCtrls_TMemo_ParentShowHint(p:TMemo):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentShowHint);
end;
//property setterStdCtrls_TMemo_ParentShowHint
procedure set_StdCtrls_TMemo_ParentShowHint(p:TMemo;v:Integer);cdecl; 
begin
p.ParentShowHint:=integertToBoolean(v);
end;
//constructorStdCtrls_TMemo_Create
function StdCtrls_TMemo_Create(AOwner:tcomponent):TMemo;cdecl;
begin
Result:=TMemo.Create((AOwner));
end;
//constructorStdCtrls_TCustomGroupBox_Create
function StdCtrls_TCustomGroupBox_Create(AOwner:tcomponent):TCustomGroupBox;cdecl;
begin
Result:=TCustomGroupBox.Create((AOwner));
end;
//property getterStdCtrls_TGroupBox_DragKind
function get_StdCtrls_TGroupBox_DragKind(p:TGroupBox):Integer;cdecl;
begin
Result:=Integer(p.DragKind);
end;
//property setterStdCtrls_TGroupBox_DragKind
procedure set_StdCtrls_TGroupBox_DragKind(p:TGroupBox;v:tdragkind);cdecl; 
begin
p.DragKind:=(v);
end;
//property getterStdCtrls_TGroupBox_DragMode
function get_StdCtrls_TGroupBox_DragMode(p:TGroupBox):Integer;cdecl;
begin
Result:=Integer(p.DragMode);
end;
//property setterStdCtrls_TGroupBox_DragMode
procedure set_StdCtrls_TGroupBox_DragMode(p:TGroupBox;v:tdragmode);cdecl; 
begin
p.DragMode:=(v);
end;
//property getterStdCtrls_TGroupBox_ParentColor
function get_StdCtrls_TGroupBox_ParentColor(p:TGroupBox):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentColor);
end;
//property setterStdCtrls_TGroupBox_ParentColor
procedure set_StdCtrls_TGroupBox_ParentColor(p:TGroupBox;v:Integer);cdecl; 
begin
p.ParentColor:=integertToBoolean(v);
end;
//property getterStdCtrls_TGroupBox_ParentFont
function get_StdCtrls_TGroupBox_ParentFont(p:TGroupBox):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentFont);
end;
//property setterStdCtrls_TGroupBox_ParentFont
procedure set_StdCtrls_TGroupBox_ParentFont(p:TGroupBox;v:Integer);cdecl; 
begin
p.ParentFont:=integertToBoolean(v);
end;
//property getterStdCtrls_TGroupBox_ParentShowHint
function get_StdCtrls_TGroupBox_ParentShowHint(p:TGroupBox):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentShowHint);
end;
//property setterStdCtrls_TGroupBox_ParentShowHint
procedure set_StdCtrls_TGroupBox_ParentShowHint(p:TGroupBox;v:Integer);cdecl; 
begin
p.ParentShowHint:=integertToBoolean(v);
end;
//property setterStdCtrls_TGroupBox_OnDblClick
function set_StdCtrls_TGroupBox_OnDblClick(p:TGroupBox;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDblClick:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TGroupBox_OnDragDrop
function set_StdCtrls_TGroupBox_OnDragDrop(p:TGroupBox;newMethod:Controls_TDragDropEvent;OldEvent:ControlsTDragDropEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragDropEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragDropEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragDrop:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TGroupBox_OnDragOver
function set_StdCtrls_TGroupBox_OnDragOver(p:TGroupBox;newMethod:Controls_TDragOverEvent;OldEvent:ControlsTDragOverEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragOverEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragOverEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragOver:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TGroupBox_OnEndDock
function set_StdCtrls_TGroupBox_OnEndDock(p:TGroupBox;newMethod:Controls_TEndDragEvent;OldEvent:ControlsTEndDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTEndDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTEndDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEndDock:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TGroupBox_OnEndDrag
function set_StdCtrls_TGroupBox_OnEndDrag(p:TGroupBox;newMethod:Controls_TEndDragEvent;OldEvent:ControlsTEndDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTEndDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTEndDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEndDrag:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TGroupBox_OnMouseDown
function set_StdCtrls_TGroupBox_OnMouseDown(p:TGroupBox;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseDown:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TGroupBox_OnMouseEnter
function set_StdCtrls_TGroupBox_OnMouseEnter(p:TGroupBox;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseEnter:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TGroupBox_OnMouseLeave
function set_StdCtrls_TGroupBox_OnMouseLeave(p:TGroupBox;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseLeave:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TGroupBox_OnMouseMove
function set_StdCtrls_TGroupBox_OnMouseMove(p:TGroupBox;newMethod:Controls_TMouseMoveEvent;OldEvent:ControlsTMouseMoveEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseMoveEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseMoveEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseMove:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TGroupBox_OnMouseUp
function set_StdCtrls_TGroupBox_OnMouseUp(p:TGroupBox;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseUp:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TGroupBox_OnStartDock
function set_StdCtrls_TGroupBox_OnStartDock(p:TGroupBox;newMethod:Controls_TStartDockEvent;OldEvent:ControlsTStartDockEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTStartDockEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTStartDockEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnStartDock:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TGroupBox_OnStartDrag
function set_StdCtrls_TGroupBox_OnStartDrag(p:TGroupBox;newMethod:Controls_TStartDragEvent;OldEvent:ControlsTStartDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTStartDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTStartDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnStartDrag:=@callClass.call;
Result:=callClass;
end;
//constructorStdCtrls_TGroupBox_Create
function StdCtrls_TGroupBox_Create(AOwner:tcomponent):TGroupBox;cdecl;
begin
Result:=TGroupBox.Create((AOwner));
end;
//constructorControls_TGraphicControl_Create
function Controls_TGraphicControl_Create(AOwner:tcomponent):TGraphicControl;cdecl;
begin
Result:=TGraphicControl.Create((AOwner));
end;
//property getterControls_TGraphicControl_Canvas
function get_Controls_TGraphicControl_Canvas(p:TGraphicControl):tcanvas;cdecl;
begin
Result:=tcanvas(p.Canvas);
end;
//constructorStdCtrls_TCustomLabel_Create
function StdCtrls_TCustomLabel_Create(TheOwner:tcomponent):TCustomLabel;cdecl;
begin
Result:=TCustomLabel.Create((TheOwner));
end;
//property getterStdCtrls_TLabel_Alignment
function get_StdCtrls_TLabel_Alignment(p:TLabel):Integer;cdecl;
begin
Result:=Integer(p.Alignment);
end;
//property setterStdCtrls_TLabel_Alignment
procedure set_StdCtrls_TLabel_Alignment(p:TLabel;v:talignment);cdecl; 
begin
p.Alignment:=(v);
end;
//property getterStdCtrls_TLabel_DragKind
function get_StdCtrls_TLabel_DragKind(p:TLabel):Integer;cdecl;
begin
Result:=Integer(p.DragKind);
end;
//property setterStdCtrls_TLabel_DragKind
procedure set_StdCtrls_TLabel_DragKind(p:TLabel;v:tdragkind);cdecl; 
begin
p.DragKind:=(v);
end;
//property getterStdCtrls_TLabel_DragMode
function get_StdCtrls_TLabel_DragMode(p:TLabel):Integer;cdecl;
begin
Result:=Integer(p.DragMode);
end;
//property setterStdCtrls_TLabel_DragMode
procedure set_StdCtrls_TLabel_DragMode(p:TLabel;v:tdragmode);cdecl; 
begin
p.DragMode:=(v);
end;
//property getterStdCtrls_TLabel_FocusControl
function get_StdCtrls_TLabel_FocusControl(p:TLabel):twincontrol;cdecl;
begin
Result:=twincontrol(p.FocusControl);
end;
//property setterStdCtrls_TLabel_FocusControl
procedure set_StdCtrls_TLabel_FocusControl(p:TLabel;v:twincontrol);cdecl; 
begin
p.FocusControl:=(v);
end;
//property getterStdCtrls_TLabel_Layout
function get_StdCtrls_TLabel_Layout(p:TLabel):Integer;cdecl;
begin
Result:=Integer(p.Layout);
end;
//property setterStdCtrls_TLabel_Layout
procedure set_StdCtrls_TLabel_Layout(p:TLabel;v:ttextlayout);cdecl; 
begin
p.Layout:=(v);
end;
//property getterStdCtrls_TLabel_ParentColor
function get_StdCtrls_TLabel_ParentColor(p:TLabel):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentColor);
end;
//property setterStdCtrls_TLabel_ParentColor
procedure set_StdCtrls_TLabel_ParentColor(p:TLabel;v:Integer);cdecl; 
begin
p.ParentColor:=integertToBoolean(v);
end;
//property getterStdCtrls_TLabel_ParentFont
function get_StdCtrls_TLabel_ParentFont(p:TLabel):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentFont);
end;
//property setterStdCtrls_TLabel_ParentFont
procedure set_StdCtrls_TLabel_ParentFont(p:TLabel;v:Integer);cdecl; 
begin
p.ParentFont:=integertToBoolean(v);
end;
//property getterStdCtrls_TLabel_ParentShowHint
function get_StdCtrls_TLabel_ParentShowHint(p:TLabel):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentShowHint);
end;
//property setterStdCtrls_TLabel_ParentShowHint
procedure set_StdCtrls_TLabel_ParentShowHint(p:TLabel;v:Integer);cdecl; 
begin
p.ParentShowHint:=integertToBoolean(v);
end;
//property getterStdCtrls_TLabel_ShowAccelChar
function get_StdCtrls_TLabel_ShowAccelChar(p:TLabel):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ShowAccelChar);
end;
//property setterStdCtrls_TLabel_ShowAccelChar
procedure set_StdCtrls_TLabel_ShowAccelChar(p:TLabel;v:Integer);cdecl; 
begin
p.ShowAccelChar:=integertToBoolean(v);
end;
//property getterStdCtrls_TLabel_Transparent
function get_StdCtrls_TLabel_Transparent(p:TLabel):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Transparent);
end;
//property setterStdCtrls_TLabel_Transparent
procedure set_StdCtrls_TLabel_Transparent(p:TLabel;v:Integer);cdecl; 
begin
p.Transparent:=integertToBoolean(v);
end;
//property getterStdCtrls_TLabel_WordWrap
function get_StdCtrls_TLabel_WordWrap(p:TLabel):Integer;cdecl;
begin
Result:=BooleanTointegert(p.WordWrap);
end;
//property setterStdCtrls_TLabel_WordWrap
procedure set_StdCtrls_TLabel_WordWrap(p:TLabel;v:Integer);cdecl; 
begin
p.WordWrap:=integertToBoolean(v);
end;
//property setterStdCtrls_TLabel_OnDblClick
function set_StdCtrls_TLabel_OnDblClick(p:TLabel;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDblClick:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TLabel_OnDragDrop
function set_StdCtrls_TLabel_OnDragDrop(p:TLabel;newMethod:Controls_TDragDropEvent;OldEvent:ControlsTDragDropEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragDropEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragDropEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragDrop:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TLabel_OnDragOver
function set_StdCtrls_TLabel_OnDragOver(p:TLabel;newMethod:Controls_TDragOverEvent;OldEvent:ControlsTDragOverEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragOverEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragOverEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragOver:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TLabel_OnEndDrag
function set_StdCtrls_TLabel_OnEndDrag(p:TLabel;newMethod:Controls_TEndDragEvent;OldEvent:ControlsTEndDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTEndDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTEndDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEndDrag:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TLabel_OnMouseDown
function set_StdCtrls_TLabel_OnMouseDown(p:TLabel;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseDown:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TLabel_OnMouseEnter
function set_StdCtrls_TLabel_OnMouseEnter(p:TLabel;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseEnter:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TLabel_OnMouseLeave
function set_StdCtrls_TLabel_OnMouseLeave(p:TLabel;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseLeave:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TLabel_OnMouseMove
function set_StdCtrls_TLabel_OnMouseMove(p:TLabel;newMethod:Controls_TMouseMoveEvent;OldEvent:ControlsTMouseMoveEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseMoveEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseMoveEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseMove:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TLabel_OnMouseUp
function set_StdCtrls_TLabel_OnMouseUp(p:TLabel;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseUp:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TLabel_OnStartDrag
function set_StdCtrls_TLabel_OnStartDrag(p:TLabel;newMethod:Controls_TStartDragEvent;OldEvent:ControlsTStartDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTStartDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTStartDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnStartDrag:=@callClass.call;
Result:=callClass;
end;
//property getterStdCtrls_TLabel_OptimalFill
function get_StdCtrls_TLabel_OptimalFill(p:TLabel):Integer;cdecl;
begin
Result:=BooleanTointegert(p.OptimalFill);
end;
//property setterStdCtrls_TLabel_OptimalFill
procedure set_StdCtrls_TLabel_OptimalFill(p:TLabel;v:Integer);cdecl; 
begin
p.OptimalFill:=integertToBoolean(v);
end;
//constructorStdCtrls_TLabel_Create
function StdCtrls_TLabel_Create(TheOwner:tcomponent):TLabel;cdecl;
begin
Result:=TLabel.Create((TheOwner));
end;
//constructorStdCtrls_TCustomListBox_Create
function StdCtrls_TCustomListBox_Create(TheOwner:tcomponent):TCustomListBox;cdecl;
begin
Result:=TCustomListBox.Create((TheOwner));
end;
//property getterStdCtrls_TCustomListBox_Canvas
function get_StdCtrls_TCustomListBox_Canvas(p:TCustomListBox):tcanvas;cdecl;
begin
Result:=tcanvas(p.Canvas);
end;
//property getterStdCtrls_TCustomListBox_ClickOnSelChange
function get_StdCtrls_TCustomListBox_ClickOnSelChange(p:TCustomListBox):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ClickOnSelChange);
end;
//property setterStdCtrls_TCustomListBox_ClickOnSelChange
procedure set_StdCtrls_TCustomListBox_ClickOnSelChange(p:TCustomListBox;v:Integer);cdecl; 
begin
p.ClickOnSelChange:=integertToBoolean(v);
end;
//property getterStdCtrls_TCustomListBox_Columns
function get_StdCtrls_TCustomListBox_Columns(p:TCustomListBox):Integer;cdecl;
begin
Result:=Integer(p.Columns);
end;
//property setterStdCtrls_TCustomListBox_Columns
procedure set_StdCtrls_TCustomListBox_Columns(p:TCustomListBox;v:Integer);cdecl; 
begin
p.Columns:=(v);
end;
//property getterStdCtrls_TCustomListBox_Count
function get_StdCtrls_TCustomListBox_Count(p:TCustomListBox):Integer;cdecl;
begin
Result:=Integer(p.Count);
end;
//property getterStdCtrls_TCustomListBox_ExtendedSelect
function get_StdCtrls_TCustomListBox_ExtendedSelect(p:TCustomListBox):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ExtendedSelect);
end;
//property setterStdCtrls_TCustomListBox_ExtendedSelect
procedure set_StdCtrls_TCustomListBox_ExtendedSelect(p:TCustomListBox;v:Integer);cdecl; 
begin
p.ExtendedSelect:=integertToBoolean(v);
end;
//property getterStdCtrls_TCustomListBox_IntegralHeight
function get_StdCtrls_TCustomListBox_IntegralHeight(p:TCustomListBox):Integer;cdecl;
begin
Result:=BooleanTointegert(p.IntegralHeight);
end;
//property setterStdCtrls_TCustomListBox_IntegralHeight
procedure set_StdCtrls_TCustomListBox_IntegralHeight(p:TCustomListBox;v:Integer);cdecl; 
begin
p.IntegralHeight:=integertToBoolean(v);
end;
//property getterStdCtrls_TCustomListBox_ItemHeight
function get_StdCtrls_TCustomListBox_ItemHeight(p:TCustomListBox):Integer;cdecl;
begin
Result:=Integer(p.ItemHeight);
end;
//property setterStdCtrls_TCustomListBox_ItemHeight
procedure set_StdCtrls_TCustomListBox_ItemHeight(p:TCustomListBox;v:Integer);cdecl; 
begin
p.ItemHeight:=(v);
end;
//property getterStdCtrls_TCustomListBox_ItemIndex
function get_StdCtrls_TCustomListBox_ItemIndex(p:TCustomListBox):Integer;cdecl;
begin
Result:=Integer(p.ItemIndex);
end;
//property setterStdCtrls_TCustomListBox_ItemIndex
procedure set_StdCtrls_TCustomListBox_ItemIndex(p:TCustomListBox;v:Integer);cdecl; 
begin
p.ItemIndex:=(v);
end;
//property getterStdCtrls_TCustomListBox_Items
function get_StdCtrls_TCustomListBox_Items(p:TCustomListBox):tstrings;cdecl;
begin
Result:=tstrings(p.Items);
end;
//property setterStdCtrls_TCustomListBox_Items
procedure set_StdCtrls_TCustomListBox_Items(p:TCustomListBox;v:tstrings);cdecl; 
begin
p.Items:=(v);
end;
//property getterStdCtrls_TCustomListBox_MultiSelect
function get_StdCtrls_TCustomListBox_MultiSelect(p:TCustomListBox):Integer;cdecl;
begin
Result:=BooleanTointegert(p.MultiSelect);
end;
//property setterStdCtrls_TCustomListBox_MultiSelect
procedure set_StdCtrls_TCustomListBox_MultiSelect(p:TCustomListBox;v:Integer);cdecl; 
begin
p.MultiSelect:=integertToBoolean(v);
end;
//property setterStdCtrls_TCustomListBox_OnDblClick
function set_StdCtrls_TCustomListBox_OnDblClick(p:TCustomListBox;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDblClick:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TCustomListBox_OnMeasureItem
function set_StdCtrls_TCustomListBox_OnMeasureItem(p:TCustomListBox;newMethod:StdCtrls_TMeasureItemEvent;OldEvent:StdCtrlsTMeasureItemEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:StdCtrlsTMeasureItemEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=StdCtrlsTMeasureItemEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMeasureItem:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TCustomListBox_OnMouseDown
function set_StdCtrls_TCustomListBox_OnMouseDown(p:TCustomListBox;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseDown:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TCustomListBox_OnMouseEnter
function set_StdCtrls_TCustomListBox_OnMouseEnter(p:TCustomListBox;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseEnter:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TCustomListBox_OnMouseLeave
function set_StdCtrls_TCustomListBox_OnMouseLeave(p:TCustomListBox;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseLeave:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TCustomListBox_OnMouseMove
function set_StdCtrls_TCustomListBox_OnMouseMove(p:TCustomListBox;newMethod:Controls_TMouseMoveEvent;OldEvent:ControlsTMouseMoveEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseMoveEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseMoveEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseMove:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TCustomListBox_OnMouseUp
function set_StdCtrls_TCustomListBox_OnMouseUp(p:TCustomListBox;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseUp:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TCustomListBox_OnSelectionChange
function set_StdCtrls_TCustomListBox_OnSelectionChange(p:TCustomListBox;newMethod:StdCtrls_TSelectionChangeEvent;OldEvent:StdCtrlsTSelectionChangeEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:StdCtrlsTSelectionChangeEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=StdCtrlsTSelectionChangeEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnSelectionChange:=@callClass.call;
Result:=callClass;
end;
//property getterStdCtrls_TCustomListBox_Options
function get_StdCtrls_TCustomListBox_Options(p:TCustomListBox):Integer;cdecl;
begin
Result:=Integer(p.Options);
end;
//property setterStdCtrls_TCustomListBox_Options
procedure set_StdCtrls_TCustomListBox_Options(p:TCustomListBox;v:tlistboxoptions);cdecl; 
begin
p.Options:=(v);
end;
//property getterStdCtrls_TCustomListBox_ParentColor
function get_StdCtrls_TCustomListBox_ParentColor(p:TCustomListBox):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentColor);
end;
//property setterStdCtrls_TCustomListBox_ParentColor
procedure set_StdCtrls_TCustomListBox_ParentColor(p:TCustomListBox;v:Integer);cdecl; 
begin
p.ParentColor:=integertToBoolean(v);
end;
//property getterStdCtrls_TCustomListBox_ParentFont
function get_StdCtrls_TCustomListBox_ParentFont(p:TCustomListBox):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentFont);
end;
//property setterStdCtrls_TCustomListBox_ParentFont
procedure set_StdCtrls_TCustomListBox_ParentFont(p:TCustomListBox;v:Integer);cdecl; 
begin
p.ParentFont:=integertToBoolean(v);
end;
//property getterStdCtrls_TCustomListBox_ParentShowHint
function get_StdCtrls_TCustomListBox_ParentShowHint(p:TCustomListBox):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentShowHint);
end;
//property setterStdCtrls_TCustomListBox_ParentShowHint
procedure set_StdCtrls_TCustomListBox_ParentShowHint(p:TCustomListBox;v:Integer);cdecl; 
begin
p.ParentShowHint:=integertToBoolean(v);
end;
//property getterStdCtrls_TCustomListBox_ScrollWidth
function get_StdCtrls_TCustomListBox_ScrollWidth(p:TCustomListBox):Integer;cdecl;
begin
Result:=Integer(p.ScrollWidth);
end;
//property setterStdCtrls_TCustomListBox_ScrollWidth
procedure set_StdCtrls_TCustomListBox_ScrollWidth(p:TCustomListBox;v:Integer);cdecl; 
begin
p.ScrollWidth:=(v);
end;
//property getterStdCtrls_TCustomListBox_SelCount
function get_StdCtrls_TCustomListBox_SelCount(p:TCustomListBox):Integer;cdecl;
begin
Result:=Integer(p.SelCount);
end;
//property getterStdCtrls_TCustomListBox_Selected
function get_StdCtrls_TCustomListBox_Selected(p:TCustomListBox;Index:Integer):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Selected[Index]);
end;
//property setterStdCtrls_TCustomListBox_Selected
procedure set_StdCtrls_TCustomListBox_Selected(p:TCustomListBox;Index:Integer;v:Integer);cdecl; 
begin
p.Selected[Index]:=integertToBoolean(v);
end;
//property getterStdCtrls_TCustomListBox_Sorted
function get_StdCtrls_TCustomListBox_Sorted(p:TCustomListBox):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Sorted);
end;
//property setterStdCtrls_TCustomListBox_Sorted
procedure set_StdCtrls_TCustomListBox_Sorted(p:TCustomListBox;v:Integer);cdecl; 
begin
p.Sorted:=integertToBoolean(v);
end;
//property getterStdCtrls_TCustomListBox_Style
function get_StdCtrls_TCustomListBox_Style(p:TCustomListBox):Integer;cdecl;
begin
Result:=Integer(p.Style);
end;
//property setterStdCtrls_TCustomListBox_Style
procedure set_StdCtrls_TCustomListBox_Style(p:TCustomListBox;v:tlistboxstyle);cdecl; 
begin
p.Style:=(v);
end;
//property getterStdCtrls_TCustomListBox_TopIndex
function get_StdCtrls_TCustomListBox_TopIndex(p:TCustomListBox):Integer;cdecl;
begin
Result:=Integer(p.TopIndex);
end;
//property setterStdCtrls_TCustomListBox_TopIndex
procedure set_StdCtrls_TCustomListBox_TopIndex(p:TCustomListBox;v:Integer);cdecl; 
begin
p.TopIndex:=(v);
end;
//property getterStdCtrls_TListBox_DragKind
function get_StdCtrls_TListBox_DragKind(p:TListBox):Integer;cdecl;
begin
Result:=Integer(p.DragKind);
end;
//property setterStdCtrls_TListBox_DragKind
procedure set_StdCtrls_TListBox_DragKind(p:TListBox;v:tdragkind);cdecl; 
begin
p.DragKind:=(v);
end;
//property getterStdCtrls_TListBox_DragMode
function get_StdCtrls_TListBox_DragMode(p:TListBox):Integer;cdecl;
begin
Result:=Integer(p.DragMode);
end;
//property setterStdCtrls_TListBox_DragMode
procedure set_StdCtrls_TListBox_DragMode(p:TListBox;v:tdragmode);cdecl; 
begin
p.DragMode:=(v);
end;
//property setterStdCtrls_TListBox_OnDragDrop
function set_StdCtrls_TListBox_OnDragDrop(p:TListBox;newMethod:Controls_TDragDropEvent;OldEvent:ControlsTDragDropEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragDropEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragDropEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragDrop:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TListBox_OnDragOver
function set_StdCtrls_TListBox_OnDragOver(p:TListBox;newMethod:Controls_TDragOverEvent;OldEvent:ControlsTDragOverEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragOverEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragOverEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragOver:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TListBox_OnEndDrag
function set_StdCtrls_TListBox_OnEndDrag(p:TListBox;newMethod:Controls_TEndDragEvent;OldEvent:ControlsTEndDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTEndDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTEndDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEndDrag:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TListBox_OnStartDrag
function set_StdCtrls_TListBox_OnStartDrag(p:TListBox;newMethod:Controls_TStartDragEvent;OldEvent:ControlsTStartDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTStartDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTStartDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnStartDrag:=@callClass.call;
Result:=callClass;
end;
//constructorStdCtrls_TListBox_Create
function StdCtrls_TListBox_Create(TheOwner:tcomponent):TListBox;cdecl;
begin
Result:=TListBox.Create((TheOwner));
end;
//constructorStdCtrls_TCustomScrollBar_Create
function StdCtrls_TCustomScrollBar_Create(AOwner:tcomponent):TCustomScrollBar;cdecl;
begin
Result:=TCustomScrollBar.Create((AOwner));
end;
//property getterStdCtrls_TCustomScrollBar_Kind
function get_StdCtrls_TCustomScrollBar_Kind(p:TCustomScrollBar):Integer;cdecl;
begin
Result:=Integer(p.Kind);
end;
//property setterStdCtrls_TCustomScrollBar_Kind
procedure set_StdCtrls_TCustomScrollBar_Kind(p:TCustomScrollBar;v:tscrollbarkind);cdecl; 
begin
p.Kind:=(v);
end;
//property getterStdCtrls_TCustomScrollBar_Max
function get_StdCtrls_TCustomScrollBar_Max(p:TCustomScrollBar):Integer;cdecl;
begin
Result:=Integer(p.Max);
end;
//property setterStdCtrls_TCustomScrollBar_Max
procedure set_StdCtrls_TCustomScrollBar_Max(p:TCustomScrollBar;v:Integer);cdecl; 
begin
p.Max:=(v);
end;
//property getterStdCtrls_TCustomScrollBar_Min
function get_StdCtrls_TCustomScrollBar_Min(p:TCustomScrollBar):Integer;cdecl;
begin
Result:=Integer(p.Min);
end;
//property setterStdCtrls_TCustomScrollBar_Min
procedure set_StdCtrls_TCustomScrollBar_Min(p:TCustomScrollBar;v:Integer);cdecl; 
begin
p.Min:=(v);
end;
//property getterStdCtrls_TCustomScrollBar_PageSize
function get_StdCtrls_TCustomScrollBar_PageSize(p:TCustomScrollBar):Integer;cdecl;
begin
Result:=Integer(p.PageSize);
end;
//property setterStdCtrls_TCustomScrollBar_PageSize
procedure set_StdCtrls_TCustomScrollBar_PageSize(p:TCustomScrollBar;v:Integer);cdecl; 
begin
p.PageSize:=(v);
end;
//property getterStdCtrls_TCustomScrollBar_Position
function get_StdCtrls_TCustomScrollBar_Position(p:TCustomScrollBar):Integer;cdecl;
begin
Result:=Integer(p.Position);
end;
//property setterStdCtrls_TCustomScrollBar_Position
procedure set_StdCtrls_TCustomScrollBar_Position(p:TCustomScrollBar;v:Integer);cdecl; 
begin
p.Position:=(v);
end;
//property setterStdCtrls_TCustomScrollBar_OnChange
function set_StdCtrls_TCustomScrollBar_OnChange(p:TCustomScrollBar;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnChange:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TCustomScrollBar_OnScroll
function set_StdCtrls_TCustomScrollBar_OnScroll(p:TCustomScrollBar;newMethod:StdCtrls_TScrollEvent;OldEvent:StdCtrlsTScrollEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:StdCtrlsTScrollEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=StdCtrlsTScrollEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnScroll:=@callClass.call;
Result:=callClass;
end;
//property getterStdCtrls_TScrollBar_DragKind
function get_StdCtrls_TScrollBar_DragKind(p:TScrollBar):Integer;cdecl;
begin
Result:=Integer(p.DragKind);
end;
//property setterStdCtrls_TScrollBar_DragKind
procedure set_StdCtrls_TScrollBar_DragKind(p:TScrollBar;v:tdragkind);cdecl; 
begin
p.DragKind:=(v);
end;
//property getterStdCtrls_TScrollBar_DragMode
function get_StdCtrls_TScrollBar_DragMode(p:TScrollBar):Integer;cdecl;
begin
Result:=Integer(p.DragMode);
end;
//property setterStdCtrls_TScrollBar_DragMode
procedure set_StdCtrls_TScrollBar_DragMode(p:TScrollBar;v:tdragmode);cdecl; 
begin
p.DragMode:=(v);
end;
//property getterStdCtrls_TScrollBar_ParentShowHint
function get_StdCtrls_TScrollBar_ParentShowHint(p:TScrollBar):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentShowHint);
end;
//property setterStdCtrls_TScrollBar_ParentShowHint
procedure set_StdCtrls_TScrollBar_ParentShowHint(p:TScrollBar;v:Integer);cdecl; 
begin
p.ParentShowHint:=integertToBoolean(v);
end;
//property setterStdCtrls_TScrollBar_OnDragDrop
function set_StdCtrls_TScrollBar_OnDragDrop(p:TScrollBar;newMethod:Controls_TDragDropEvent;OldEvent:ControlsTDragDropEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragDropEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragDropEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragDrop:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TScrollBar_OnDragOver
function set_StdCtrls_TScrollBar_OnDragOver(p:TScrollBar;newMethod:Controls_TDragOverEvent;OldEvent:ControlsTDragOverEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragOverEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragOverEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragOver:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TScrollBar_OnEndDrag
function set_StdCtrls_TScrollBar_OnEndDrag(p:TScrollBar;newMethod:Controls_TEndDragEvent;OldEvent:ControlsTEndDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTEndDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTEndDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEndDrag:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TScrollBar_OnStartDrag
function set_StdCtrls_TScrollBar_OnStartDrag(p:TScrollBar;newMethod:Controls_TStartDragEvent;OldEvent:ControlsTStartDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTStartDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTStartDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnStartDrag:=@callClass.call;
Result:=callClass;
end;
//constructorStdCtrls_TScrollBar_Create
function StdCtrls_TScrollBar_Create(AOwner:tcomponent):TScrollBar;cdecl;
begin
Result:=TScrollBar.Create((AOwner));
end;
//constructorForms_TApplicationProperties_Create
function Forms_TApplicationProperties_Create(AOwner:tcomponent):TApplicationProperties;cdecl;
begin
Result:=TApplicationProperties.Create((AOwner));
end;
//property getterForms_TApplicationProperties_CaptureExceptions
function get_Forms_TApplicationProperties_CaptureExceptions(p:TApplicationProperties):Integer;cdecl;
begin
Result:=BooleanTointegert(p.CaptureExceptions);
end;
//property setterForms_TApplicationProperties_CaptureExceptions
procedure set_Forms_TApplicationProperties_CaptureExceptions(p:TApplicationProperties;v:Integer);cdecl; 
begin
p.CaptureExceptions:=integertToBoolean(v);
end;
//property getterForms_TApplicationProperties_ExceptionDialog
function get_Forms_TApplicationProperties_ExceptionDialog(p:TApplicationProperties):Integer;cdecl;
begin
Result:=Integer(p.ExceptionDialog);
end;
//property setterForms_TApplicationProperties_ExceptionDialog
procedure set_Forms_TApplicationProperties_ExceptionDialog(p:TApplicationProperties;v:tapplicationexceptiondlg);cdecl; 
begin
p.ExceptionDialog:=(v);
end;
//property getterForms_TApplicationProperties_HelpFile
function get_Forms_TApplicationProperties_HelpFile(p:TApplicationProperties):PChar;cdecl;
begin
Result:=PChar(p.HelpFile);
end;
//property setterForms_TApplicationProperties_HelpFile
procedure set_Forms_TApplicationProperties_HelpFile(p:TApplicationProperties;v:PChar);cdecl; 
begin
p.HelpFile:=(v);
end;
//property getterForms_TApplicationProperties_Hint
function get_Forms_TApplicationProperties_Hint(p:TApplicationProperties):PChar;cdecl;
begin
Result:=PChar(p.Hint);
end;
//property setterForms_TApplicationProperties_Hint
procedure set_Forms_TApplicationProperties_Hint(p:TApplicationProperties;v:PChar);cdecl; 
begin
p.Hint:=(v);
end;
//property getterForms_TApplicationProperties_HintHidePause
function get_Forms_TApplicationProperties_HintHidePause(p:TApplicationProperties):Integer;cdecl;
begin
Result:=Integer(p.HintHidePause);
end;
//property setterForms_TApplicationProperties_HintHidePause
procedure set_Forms_TApplicationProperties_HintHidePause(p:TApplicationProperties;v:Integer);cdecl; 
begin
p.HintHidePause:=(v);
end;
//property getterForms_TApplicationProperties_HintPause
function get_Forms_TApplicationProperties_HintPause(p:TApplicationProperties):Integer;cdecl;
begin
Result:=Integer(p.HintPause);
end;
//property setterForms_TApplicationProperties_HintPause
procedure set_Forms_TApplicationProperties_HintPause(p:TApplicationProperties;v:Integer);cdecl; 
begin
p.HintPause:=(v);
end;
//property getterForms_TApplicationProperties_HintShortCuts
function get_Forms_TApplicationProperties_HintShortCuts(p:TApplicationProperties):Integer;cdecl;
begin
Result:=BooleanTointegert(p.HintShortCuts);
end;
//property setterForms_TApplicationProperties_HintShortCuts
procedure set_Forms_TApplicationProperties_HintShortCuts(p:TApplicationProperties;v:Integer);cdecl; 
begin
p.HintShortCuts:=integertToBoolean(v);
end;
//property getterForms_TApplicationProperties_HintShortPause
function get_Forms_TApplicationProperties_HintShortPause(p:TApplicationProperties):Integer;cdecl;
begin
Result:=Integer(p.HintShortPause);
end;
//property setterForms_TApplicationProperties_HintShortPause
procedure set_Forms_TApplicationProperties_HintShortPause(p:TApplicationProperties;v:Integer);cdecl; 
begin
p.HintShortPause:=(v);
end;
//property getterForms_TApplicationProperties_ShowButtonGlyphs
function get_Forms_TApplicationProperties_ShowButtonGlyphs(p:TApplicationProperties):Integer;cdecl;
begin
Result:=Integer(p.ShowButtonGlyphs);
end;
//property setterForms_TApplicationProperties_ShowButtonGlyphs
procedure set_Forms_TApplicationProperties_ShowButtonGlyphs(p:TApplicationProperties;v:tapplicationshowglyphs);cdecl; 
begin
p.ShowButtonGlyphs:=(v);
end;
//property getterForms_TApplicationProperties_ShowMenuGlyphs
function get_Forms_TApplicationProperties_ShowMenuGlyphs(p:TApplicationProperties):Integer;cdecl;
begin
Result:=Integer(p.ShowMenuGlyphs);
end;
//property setterForms_TApplicationProperties_ShowMenuGlyphs
procedure set_Forms_TApplicationProperties_ShowMenuGlyphs(p:TApplicationProperties;v:tapplicationshowglyphs);cdecl; 
begin
p.ShowMenuGlyphs:=(v);
end;
//property getterForms_TApplicationProperties_ShowHint
function get_Forms_TApplicationProperties_ShowHint(p:TApplicationProperties):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ShowHint);
end;
//property setterForms_TApplicationProperties_ShowHint
procedure set_Forms_TApplicationProperties_ShowHint(p:TApplicationProperties;v:Integer);cdecl; 
begin
p.ShowHint:=integertToBoolean(v);
end;
//property getterForms_TApplicationProperties_ShowMainForm
function get_Forms_TApplicationProperties_ShowMainForm(p:TApplicationProperties):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ShowMainForm);
end;
//property setterForms_TApplicationProperties_ShowMainForm
procedure set_Forms_TApplicationProperties_ShowMainForm(p:TApplicationProperties;v:Integer);cdecl; 
begin
p.ShowMainForm:=integertToBoolean(v);
end;
//property getterForms_TApplicationProperties_Title
function get_Forms_TApplicationProperties_Title(p:TApplicationProperties):PChar;cdecl;
begin
Result:=PChar(p.Title);
end;
//property setterForms_TApplicationProperties_Title
procedure set_Forms_TApplicationProperties_Title(p:TApplicationProperties;v:PChar);cdecl; 
begin
p.Title:=(v);
end;
//property setterForms_TApplicationProperties_OnActivate
function set_Forms_TApplicationProperties_OnActivate(p:TApplicationProperties;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnActivate:=@callClass.call;
Result:=callClass;
end;
//property setterForms_TApplicationProperties_OnDeactivate
function set_Forms_TApplicationProperties_OnDeactivate(p:TApplicationProperties;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDeactivate:=@callClass.call;
Result:=callClass;
end;
//property setterForms_TApplicationProperties_OnIdle
function set_Forms_TApplicationProperties_OnIdle(p:TApplicationProperties;newMethod:Forms_TIdleEvent;OldEvent:FormsTIdleEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:FormsTIdleEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=FormsTIdleEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnIdle:=@callClass.call;
Result:=callClass;
end;
//property setterForms_TApplicationProperties_OnIdleEnd
function set_Forms_TApplicationProperties_OnIdleEnd(p:TApplicationProperties;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnIdleEnd:=@callClass.call;
Result:=callClass;
end;
//property setterForms_TApplicationProperties_OnEndSession
function set_Forms_TApplicationProperties_OnEndSession(p:TApplicationProperties;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEndSession:=@callClass.call;
Result:=callClass;
end;
//property setterForms_TApplicationProperties_OnQueryEndSession
function set_Forms_TApplicationProperties_OnQueryEndSession(p:TApplicationProperties;newMethod:Forms_TQueryEndSessionEvent;OldEvent:FormsTQueryEndSessionEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:FormsTQueryEndSessionEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=FormsTQueryEndSessionEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnQueryEndSession:=@callClass.call;
Result:=callClass;
end;
//property setterForms_TApplicationProperties_OnMinimize
function set_Forms_TApplicationProperties_OnMinimize(p:TApplicationProperties;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMinimize:=@callClass.call;
Result:=callClass;
end;
//property setterForms_TApplicationProperties_OnModalBegin
function set_Forms_TApplicationProperties_OnModalBegin(p:TApplicationProperties;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnModalBegin:=@callClass.call;
Result:=callClass;
end;
//property setterForms_TApplicationProperties_OnModalEnd
function set_Forms_TApplicationProperties_OnModalEnd(p:TApplicationProperties;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnModalEnd:=@callClass.call;
Result:=callClass;
end;
//property setterForms_TApplicationProperties_OnRestore
function set_Forms_TApplicationProperties_OnRestore(p:TApplicationProperties;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnRestore:=@callClass.call;
Result:=callClass;
end;
//property setterForms_TApplicationProperties_OnHint
function set_Forms_TApplicationProperties_OnHint(p:TApplicationProperties;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnHint:=@callClass.call;
Result:=callClass;
end;
//constructorExtCtrls_TBevel_Create
function ExtCtrls_TBevel_Create(AOwner:tcomponent):TBevel;cdecl;
begin
Result:=TBevel.Create((AOwner));
end;
//property getterExtCtrls_TBevel_ParentShowHint
function get_ExtCtrls_TBevel_ParentShowHint(p:TBevel):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentShowHint);
end;
//property setterExtCtrls_TBevel_ParentShowHint
procedure set_ExtCtrls_TBevel_ParentShowHint(p:TBevel;v:Integer);cdecl; 
begin
p.ParentShowHint:=integertToBoolean(v);
end;
//property getterExtCtrls_TBevel_Shape
function get_ExtCtrls_TBevel_Shape(p:TBevel):Integer;cdecl;
begin
Result:=Integer(p.Shape);
end;
//property setterExtCtrls_TBevel_Shape
procedure set_ExtCtrls_TBevel_Shape(p:TBevel;v:tbevelshape);cdecl; 
begin
p.Shape:=(v);
end;
//property getterExtCtrls_TBevel_Style
function get_ExtCtrls_TBevel_Style(p:TBevel):Integer;cdecl;
begin
Result:=Integer(p.Style);
end;
//property setterExtCtrls_TBevel_Style
procedure set_ExtCtrls_TBevel_Style(p:TBevel;v:tbevelstyle);cdecl; 
begin
p.Style:=(v);
end;
//property setterExtCtrls_TBevel_OnMouseDown
function set_ExtCtrls_TBevel_OnMouseDown(p:TBevel;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseDown:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TBevel_OnMouseEnter
function set_ExtCtrls_TBevel_OnMouseEnter(p:TBevel;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseEnter:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TBevel_OnMouseLeave
function set_ExtCtrls_TBevel_OnMouseLeave(p:TBevel;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseLeave:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TBevel_OnMouseMove
function set_ExtCtrls_TBevel_OnMouseMove(p:TBevel;newMethod:Controls_TMouseMoveEvent;OldEvent:ControlsTMouseMoveEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseMoveEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseMoveEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseMove:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TBevel_OnMouseUp
function set_ExtCtrls_TBevel_OnMouseUp(p:TBevel;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseUp:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TBevel_OnPaint
function set_ExtCtrls_TBevel_OnPaint(p:TBevel;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnPaint:=@callClass.call;
Result:=callClass;
end;
//constructorButtons_TCustomBitBtn_Create
function Buttons_TCustomBitBtn_Create(TheOwner:tcomponent):TCustomBitBtn;cdecl;
begin
Result:=TCustomBitBtn.Create((TheOwner));
end;
//property getterButtons_TCustomBitBtn_DefaultCaption
function get_Buttons_TCustomBitBtn_DefaultCaption(p:TCustomBitBtn):Integer;cdecl;
begin
Result:=BooleanTointegert(p.DefaultCaption);
end;
//property setterButtons_TCustomBitBtn_DefaultCaption
procedure set_Buttons_TCustomBitBtn_DefaultCaption(p:TCustomBitBtn;v:Integer);cdecl; 
begin
p.DefaultCaption:=integertToBoolean(v);
end;
//property getterButtons_TCustomBitBtn_Glyph
function get_Buttons_TCustomBitBtn_Glyph(p:TCustomBitBtn):tbitmap;cdecl;
begin
Result:=tbitmap(p.Glyph);
end;
//property setterButtons_TCustomBitBtn_Glyph
procedure set_Buttons_TCustomBitBtn_Glyph(p:TCustomBitBtn;v:tbitmap);cdecl; 
begin
p.Glyph:=(v);
end;
//property getterButtons_TCustomBitBtn_NumGlyphs
function get_Buttons_TCustomBitBtn_NumGlyphs(p:TCustomBitBtn):Integer;cdecl;
begin
Result:=Integer(p.NumGlyphs);
end;
//property setterButtons_TCustomBitBtn_NumGlyphs
procedure set_Buttons_TCustomBitBtn_NumGlyphs(p:TCustomBitBtn;v:Integer);cdecl; 
begin
p.NumGlyphs:=(v);
end;
//property getterButtons_TCustomBitBtn_Kind
function get_Buttons_TCustomBitBtn_Kind(p:TCustomBitBtn):Integer;cdecl;
begin
Result:=Integer(p.Kind);
end;
//property setterButtons_TCustomBitBtn_Kind
procedure set_Buttons_TCustomBitBtn_Kind(p:TCustomBitBtn;v:tbitbtnkind);cdecl; 
begin
p.Kind:=(v);
end;
//property getterButtons_TCustomBitBtn_Layout
function get_Buttons_TCustomBitBtn_Layout(p:TCustomBitBtn):Integer;cdecl;
begin
Result:=Integer(p.Layout);
end;
//property setterButtons_TCustomBitBtn_Layout
procedure set_Buttons_TCustomBitBtn_Layout(p:TCustomBitBtn;v:tbuttonlayout);cdecl; 
begin
p.Layout:=(v);
end;
//property getterButtons_TCustomBitBtn_Margin
function get_Buttons_TCustomBitBtn_Margin(p:TCustomBitBtn):Integer;cdecl;
begin
Result:=Integer(p.Margin);
end;
//property setterButtons_TCustomBitBtn_Margin
procedure set_Buttons_TCustomBitBtn_Margin(p:TCustomBitBtn;v:Integer);cdecl; 
begin
p.Margin:=(v);
end;
//property getterButtons_TCustomBitBtn_Spacing
function get_Buttons_TCustomBitBtn_Spacing(p:TCustomBitBtn):Integer;cdecl;
begin
Result:=Integer(p.Spacing);
end;
//property setterButtons_TCustomBitBtn_Spacing
procedure set_Buttons_TCustomBitBtn_Spacing(p:TCustomBitBtn;v:Integer);cdecl; 
begin
p.Spacing:=(v);
end;
//property getterButtons_TCustomBitBtn_GlyphShowMode
function get_Buttons_TCustomBitBtn_GlyphShowMode(p:TCustomBitBtn):Integer;cdecl;
begin
Result:=Integer(p.GlyphShowMode);
end;
//property setterButtons_TCustomBitBtn_GlyphShowMode
procedure set_Buttons_TCustomBitBtn_GlyphShowMode(p:TCustomBitBtn;v:tglyphshowmode);cdecl; 
begin
p.GlyphShowMode:=(v);
end;
//property setterButtons_TBitBtn_OnDragDrop
function set_Buttons_TBitBtn_OnDragDrop(p:TBitBtn;newMethod:Controls_TDragDropEvent;OldEvent:ControlsTDragDropEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragDropEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragDropEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragDrop:=@callClass.call;
Result:=callClass;
end;
//property setterButtons_TBitBtn_OnDragOver
function set_Buttons_TBitBtn_OnDragOver(p:TBitBtn;newMethod:Controls_TDragOverEvent;OldEvent:ControlsTDragOverEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragOverEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragOverEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragOver:=@callClass.call;
Result:=callClass;
end;
//property setterButtons_TBitBtn_OnEndDrag
function set_Buttons_TBitBtn_OnEndDrag(p:TBitBtn;newMethod:Controls_TEndDragEvent;OldEvent:ControlsTEndDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTEndDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTEndDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEndDrag:=@callClass.call;
Result:=callClass;
end;
//property setterButtons_TBitBtn_OnMouseDown
function set_Buttons_TBitBtn_OnMouseDown(p:TBitBtn;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseDown:=@callClass.call;
Result:=callClass;
end;
//property setterButtons_TBitBtn_OnMouseEnter
function set_Buttons_TBitBtn_OnMouseEnter(p:TBitBtn;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseEnter:=@callClass.call;
Result:=callClass;
end;
//property setterButtons_TBitBtn_OnMouseLeave
function set_Buttons_TBitBtn_OnMouseLeave(p:TBitBtn;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseLeave:=@callClass.call;
Result:=callClass;
end;
//property setterButtons_TBitBtn_OnMouseMove
function set_Buttons_TBitBtn_OnMouseMove(p:TBitBtn;newMethod:Controls_TMouseMoveEvent;OldEvent:ControlsTMouseMoveEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseMoveEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseMoveEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseMove:=@callClass.call;
Result:=callClass;
end;
//property setterButtons_TBitBtn_OnMouseUp
function set_Buttons_TBitBtn_OnMouseUp(p:TBitBtn;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseUp:=@callClass.call;
Result:=callClass;
end;
//property setterButtons_TBitBtn_OnStartDrag
function set_Buttons_TBitBtn_OnStartDrag(p:TBitBtn;newMethod:Controls_TStartDragEvent;OldEvent:ControlsTStartDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTStartDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTStartDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnStartDrag:=@callClass.call;
Result:=callClass;
end;
//property getterButtons_TBitBtn_ParentFont
function get_Buttons_TBitBtn_ParentFont(p:TBitBtn):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentFont);
end;
//property setterButtons_TBitBtn_ParentFont
procedure set_Buttons_TBitBtn_ParentFont(p:TBitBtn;v:Integer);cdecl; 
begin
p.ParentFont:=integertToBoolean(v);
end;
//property getterButtons_TBitBtn_ParentShowHint
function get_Buttons_TBitBtn_ParentShowHint(p:TBitBtn):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentShowHint);
end;
//property setterButtons_TBitBtn_ParentShowHint
procedure set_Buttons_TBitBtn_ParentShowHint(p:TBitBtn;v:Integer);cdecl; 
begin
p.ParentShowHint:=integertToBoolean(v);
end;
//constructorButtons_TBitBtn_Create
function Buttons_TBitBtn_Create(TheOwner:tcomponent):TBitBtn;cdecl;
begin
Result:=TBitBtn.Create((TheOwner));
end;
//constructorCheckLst_TCustomCheckListBox_Create
function CheckLst_TCustomCheckListBox_Create(AOwner:tcomponent):TCustomCheckListBox;cdecl;
begin
Result:=TCustomCheckListBox.Create((AOwner));
end;
//property getterCheckLst_TCustomCheckListBox_AllowGrayed
function get_CheckLst_TCustomCheckListBox_AllowGrayed(p:TCustomCheckListBox):Integer;cdecl;
begin
Result:=BooleanTointegert(p.AllowGrayed);
end;
//property setterCheckLst_TCustomCheckListBox_AllowGrayed
procedure set_CheckLst_TCustomCheckListBox_AllowGrayed(p:TCustomCheckListBox;v:Integer);cdecl; 
begin
p.AllowGrayed:=integertToBoolean(v);
end;
//property getterCheckLst_TCustomCheckListBox_Checked
function get_CheckLst_TCustomCheckListBox_Checked(p:TCustomCheckListBox;AIndex:Integer):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Checked[AIndex]);
end;
//property setterCheckLst_TCustomCheckListBox_Checked
procedure set_CheckLst_TCustomCheckListBox_Checked(p:TCustomCheckListBox;AIndex:Integer;v:Integer);cdecl; 
begin
p.Checked[AIndex]:=integertToBoolean(v);
end;
//property getterCheckLst_TCustomCheckListBox_Header
function get_CheckLst_TCustomCheckListBox_Header(p:TCustomCheckListBox;AIndex:Integer):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Header[AIndex]);
end;
//property setterCheckLst_TCustomCheckListBox_Header
procedure set_CheckLst_TCustomCheckListBox_Header(p:TCustomCheckListBox;AIndex:Integer;v:Integer);cdecl; 
begin
p.Header[AIndex]:=integertToBoolean(v);
end;
//property getterCheckLst_TCustomCheckListBox_ItemEnabled
function get_CheckLst_TCustomCheckListBox_ItemEnabled(p:TCustomCheckListBox;AIndex:Integer):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ItemEnabled[AIndex]);
end;
//property setterCheckLst_TCustomCheckListBox_ItemEnabled
procedure set_CheckLst_TCustomCheckListBox_ItemEnabled(p:TCustomCheckListBox;AIndex:Integer;v:Integer);cdecl; 
begin
p.ItemEnabled[AIndex]:=integertToBoolean(v);
end;
//property getterCheckLst_TCustomCheckListBox_State
function get_CheckLst_TCustomCheckListBox_State(p:TCustomCheckListBox;AIndex:Integer):Integer;cdecl;
begin
Result:=Integer(p.State[AIndex]);
end;
//property setterCheckLst_TCustomCheckListBox_State
procedure set_CheckLst_TCustomCheckListBox_State(p:TCustomCheckListBox;AIndex:Integer;v:tcheckboxstate);cdecl; 
begin
p.State[AIndex]:=(v);
end;
//property setterCheckLst_TCustomCheckListBox_OnClickCheck
function set_CheckLst_TCustomCheckListBox_OnClickCheck(p:TCustomCheckListBox;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnClickCheck:=@callClass.call;
Result:=callClass;
end;
//property setterCheckLst_TCustomCheckListBox_OnItemClick
function set_CheckLst_TCustomCheckListBox_OnItemClick(p:TCustomCheckListBox;newMethod:CheckLst_TCheckListClicked;OldEvent:CheckLstTCheckListClicked_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:CheckLstTCheckListClicked_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=CheckLstTCheckListClicked_wrapper.Create;
callClass.c:=newMethod;
p.OnItemClick:=@callClass.call;
Result:=callClass;
end;
//property getterCheckLst_TCheckListBox_DragMode
function get_CheckLst_TCheckListBox_DragMode(p:TCheckListBox):Integer;cdecl;
begin
Result:=Integer(p.DragMode);
end;
//property setterCheckLst_TCheckListBox_DragMode
procedure set_CheckLst_TCheckListBox_DragMode(p:TCheckListBox;v:tdragmode);cdecl; 
begin
p.DragMode:=(v);
end;
//property setterCheckLst_TCheckListBox_OnDragDrop
function set_CheckLst_TCheckListBox_OnDragDrop(p:TCheckListBox;newMethod:Controls_TDragDropEvent;OldEvent:ControlsTDragDropEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragDropEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragDropEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragDrop:=@callClass.call;
Result:=callClass;
end;
//property setterCheckLst_TCheckListBox_OnDragOver
function set_CheckLst_TCheckListBox_OnDragOver(p:TCheckListBox;newMethod:Controls_TDragOverEvent;OldEvent:ControlsTDragOverEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragOverEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragOverEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragOver:=@callClass.call;
Result:=callClass;
end;
//property setterCheckLst_TCheckListBox_OnEndDrag
function set_CheckLst_TCheckListBox_OnEndDrag(p:TCheckListBox;newMethod:Controls_TEndDragEvent;OldEvent:ControlsTEndDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTEndDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTEndDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEndDrag:=@callClass.call;
Result:=callClass;
end;
//property setterCheckLst_TCheckListBox_OnStartDrag
function set_CheckLst_TCheckListBox_OnStartDrag(p:TCheckListBox;newMethod:Controls_TStartDragEvent;OldEvent:ControlsTStartDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTStartDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTStartDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnStartDrag:=@callClass.call;
Result:=callClass;
end;
//constructorCheckLst_TCheckListBox_Create
function CheckLst_TCheckListBox_Create(AOwner:tcomponent):TCheckListBox;cdecl;
begin
Result:=TCheckListBox.Create((AOwner));
end;
//constructorColorBox_TCustomColorBox_Create
function ColorBox_TCustomColorBox_Create(AOwner:tcomponent):TCustomColorBox;cdecl;
begin
Result:=TCustomColorBox.Create((AOwner));
end;
//property getterColorBox_TCustomColorBox_ColorRectWidth
function get_ColorBox_TCustomColorBox_ColorRectWidth(p:TCustomColorBox):Integer;cdecl;
begin
Result:=Integer(p.ColorRectWidth);
end;
//property setterColorBox_TCustomColorBox_ColorRectWidth
procedure set_ColorBox_TCustomColorBox_ColorRectWidth(p:TCustomColorBox;v:Integer);cdecl; 
begin
p.ColorRectWidth:=(v);
end;
//property getterColorBox_TCustomColorBox_ColorRectOffset
function get_ColorBox_TCustomColorBox_ColorRectOffset(p:TCustomColorBox):Integer;cdecl;
begin
Result:=Integer(p.ColorRectOffset);
end;
//property setterColorBox_TCustomColorBox_ColorRectOffset
procedure set_ColorBox_TCustomColorBox_ColorRectOffset(p:TCustomColorBox;v:Integer);cdecl; 
begin
p.ColorRectOffset:=(v);
end;
//property getterColorBox_TCustomColorBox_Style
function get_ColorBox_TCustomColorBox_Style(p:TCustomColorBox):Integer;cdecl;
begin
Result:=Integer(p.Style);
end;
//property setterColorBox_TCustomColorBox_Style
procedure set_ColorBox_TCustomColorBox_Style(p:TCustomColorBox;v:tcolorboxstyle);cdecl; 
begin
p.Style:=(v);
end;
//property getterColorBox_TCustomColorBox_ColorNames
function get_ColorBox_TCustomColorBox_ColorNames(p:TCustomColorBox;Index:Integer):PChar;cdecl;
begin
Result:=PChar(p.ColorNames[Index]);
end;
//property getterColorBox_TColorBox_DragMode
function get_ColorBox_TColorBox_DragMode(p:TColorBox):Integer;cdecl;
begin
Result:=Integer(p.DragMode);
end;
//property setterColorBox_TColorBox_DragMode
procedure set_ColorBox_TColorBox_DragMode(p:TColorBox;v:tdragmode);cdecl; 
begin
p.DragMode:=(v);
end;
//property getterColorBox_TColorBox_ItemHeight
function get_ColorBox_TColorBox_ItemHeight(p:TColorBox):Integer;cdecl;
begin
Result:=Integer(p.ItemHeight);
end;
//property setterColorBox_TColorBox_ItemHeight
procedure set_ColorBox_TColorBox_ItemHeight(p:TColorBox;v:Integer);cdecl; 
begin
p.ItemHeight:=(v);
end;
//property getterColorBox_TColorBox_ItemWidth
function get_ColorBox_TColorBox_ItemWidth(p:TColorBox):Integer;cdecl;
begin
Result:=Integer(p.ItemWidth);
end;
//property setterColorBox_TColorBox_ItemWidth
procedure set_ColorBox_TColorBox_ItemWidth(p:TColorBox;v:Integer);cdecl; 
begin
p.ItemWidth:=(v);
end;
//property setterColorBox_TColorBox_OnChange
function set_ColorBox_TColorBox_OnChange(p:TColorBox;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnChange:=@callClass.call;
Result:=callClass;
end;
//property setterColorBox_TColorBox_OnCloseUp
function set_ColorBox_TColorBox_OnCloseUp(p:TColorBox;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnCloseUp:=@callClass.call;
Result:=callClass;
end;
//property setterColorBox_TColorBox_OnDblClick
function set_ColorBox_TColorBox_OnDblClick(p:TColorBox;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDblClick:=@callClass.call;
Result:=callClass;
end;
//property setterColorBox_TColorBox_OnDragDrop
function set_ColorBox_TColorBox_OnDragDrop(p:TColorBox;newMethod:Controls_TDragDropEvent;OldEvent:ControlsTDragDropEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragDropEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragDropEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragDrop:=@callClass.call;
Result:=callClass;
end;
//property setterColorBox_TColorBox_OnDragOver
function set_ColorBox_TColorBox_OnDragOver(p:TColorBox;newMethod:Controls_TDragOverEvent;OldEvent:ControlsTDragOverEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragOverEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragOverEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragOver:=@callClass.call;
Result:=callClass;
end;
//property setterColorBox_TColorBox_OnEndDrag
function set_ColorBox_TColorBox_OnEndDrag(p:TColorBox;newMethod:Controls_TEndDragEvent;OldEvent:ControlsTEndDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTEndDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTEndDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEndDrag:=@callClass.call;
Result:=callClass;
end;
//property setterColorBox_TColorBox_OnDropDown
function set_ColorBox_TColorBox_OnDropDown(p:TColorBox;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDropDown:=@callClass.call;
Result:=callClass;
end;
//property setterColorBox_TColorBox_OnEditingDone
function set_ColorBox_TColorBox_OnEditingDone(p:TColorBox;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEditingDone:=@callClass.call;
Result:=callClass;
end;
//property setterColorBox_TColorBox_OnMouseDown
function set_ColorBox_TColorBox_OnMouseDown(p:TColorBox;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseDown:=@callClass.call;
Result:=callClass;
end;
//property setterColorBox_TColorBox_OnMouseEnter
function set_ColorBox_TColorBox_OnMouseEnter(p:TColorBox;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseEnter:=@callClass.call;
Result:=callClass;
end;
//property setterColorBox_TColorBox_OnMouseLeave
function set_ColorBox_TColorBox_OnMouseLeave(p:TColorBox;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseLeave:=@callClass.call;
Result:=callClass;
end;
//property setterColorBox_TColorBox_OnMouseMove
function set_ColorBox_TColorBox_OnMouseMove(p:TColorBox;newMethod:Controls_TMouseMoveEvent;OldEvent:ControlsTMouseMoveEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseMoveEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseMoveEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseMove:=@callClass.call;
Result:=callClass;
end;
//property setterColorBox_TColorBox_OnMouseUp
function set_ColorBox_TColorBox_OnMouseUp(p:TColorBox;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseUp:=@callClass.call;
Result:=callClass;
end;
//property setterColorBox_TColorBox_OnStartDrag
function set_ColorBox_TColorBox_OnStartDrag(p:TColorBox;newMethod:Controls_TStartDragEvent;OldEvent:ControlsTStartDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTStartDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTStartDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnStartDrag:=@callClass.call;
Result:=callClass;
end;
//property setterColorBox_TColorBox_OnSelect
function set_ColorBox_TColorBox_OnSelect(p:TColorBox;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnSelect:=@callClass.call;
Result:=callClass;
end;
//property getterColorBox_TColorBox_ParentColor
function get_ColorBox_TColorBox_ParentColor(p:TColorBox):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentColor);
end;
//property setterColorBox_TColorBox_ParentColor
procedure set_ColorBox_TColorBox_ParentColor(p:TColorBox;v:Integer);cdecl; 
begin
p.ParentColor:=integertToBoolean(v);
end;
//property getterColorBox_TColorBox_ParentFont
function get_ColorBox_TColorBox_ParentFont(p:TColorBox):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentFont);
end;
//property setterColorBox_TColorBox_ParentFont
procedure set_ColorBox_TColorBox_ParentFont(p:TColorBox;v:Integer);cdecl; 
begin
p.ParentFont:=integertToBoolean(v);
end;
//property getterColorBox_TColorBox_ParentShowHint
function get_ColorBox_TColorBox_ParentShowHint(p:TColorBox):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentShowHint);
end;
//property setterColorBox_TColorBox_ParentShowHint
procedure set_ColorBox_TColorBox_ParentShowHint(p:TColorBox;v:Integer);cdecl; 
begin
p.ParentShowHint:=integertToBoolean(v);
end;
//constructorColorBox_TColorBox_Create
function ColorBox_TColorBox_Create(AOwner:tcomponent):TColorBox;cdecl;
begin
Result:=TColorBox.Create((AOwner));
end;
//constructorColorBox_TCustomColorListBox_Create
function ColorBox_TCustomColorListBox_Create(AOwner:tcomponent):TCustomColorListBox;cdecl;
begin
Result:=TCustomColorListBox.Create((AOwner));
end;
//property getterColorBox_TCustomColorListBox_ColorRectWidth
function get_ColorBox_TCustomColorListBox_ColorRectWidth(p:TCustomColorListBox):Integer;cdecl;
begin
Result:=Integer(p.ColorRectWidth);
end;
//property setterColorBox_TCustomColorListBox_ColorRectWidth
procedure set_ColorBox_TCustomColorListBox_ColorRectWidth(p:TCustomColorListBox;v:Integer);cdecl; 
begin
p.ColorRectWidth:=(v);
end;
//property getterColorBox_TCustomColorListBox_ColorRectOffset
function get_ColorBox_TCustomColorListBox_ColorRectOffset(p:TCustomColorListBox):Integer;cdecl;
begin
Result:=Integer(p.ColorRectOffset);
end;
//property setterColorBox_TCustomColorListBox_ColorRectOffset
procedure set_ColorBox_TCustomColorListBox_ColorRectOffset(p:TCustomColorListBox;v:Integer);cdecl; 
begin
p.ColorRectOffset:=(v);
end;
//property getterColorBox_TCustomColorListBox_Style
function get_ColorBox_TCustomColorListBox_Style(p:TCustomColorListBox):Integer;cdecl;
begin
Result:=Integer(p.Style);
end;
//property setterColorBox_TCustomColorListBox_Style
procedure set_ColorBox_TCustomColorListBox_Style(p:TCustomColorListBox;v:tcolorboxstyle);cdecl; 
begin
p.Style:=(v);
end;
//property getterColorBox_TCustomColorListBox_ColorNames
function get_ColorBox_TCustomColorListBox_ColorNames(p:TCustomColorListBox;Index:Integer):PChar;cdecl;
begin
Result:=PChar(p.ColorNames[Index]);
end;
//property getterColorBox_TColorListBox_DragKind
function get_ColorBox_TColorListBox_DragKind(p:TColorListBox):Integer;cdecl;
begin
Result:=Integer(p.DragKind);
end;
//property setterColorBox_TColorListBox_DragKind
procedure set_ColorBox_TColorListBox_DragKind(p:TColorListBox;v:tdragkind);cdecl; 
begin
p.DragKind:=(v);
end;
//property getterColorBox_TColorListBox_DragMode
function get_ColorBox_TColorListBox_DragMode(p:TColorListBox):Integer;cdecl;
begin
Result:=Integer(p.DragMode);
end;
//property setterColorBox_TColorListBox_DragMode
procedure set_ColorBox_TColorListBox_DragMode(p:TColorListBox;v:tdragmode);cdecl; 
begin
p.DragMode:=(v);
end;
//property setterColorBox_TColorListBox_OnDragDrop
function set_ColorBox_TColorListBox_OnDragDrop(p:TColorListBox;newMethod:Controls_TDragDropEvent;OldEvent:ControlsTDragDropEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragDropEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragDropEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragDrop:=@callClass.call;
Result:=callClass;
end;
//property setterColorBox_TColorListBox_OnDragOver
function set_ColorBox_TColorListBox_OnDragOver(p:TColorListBox;newMethod:Controls_TDragOverEvent;OldEvent:ControlsTDragOverEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragOverEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragOverEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragOver:=@callClass.call;
Result:=callClass;
end;
//property setterColorBox_TColorListBox_OnEndDrag
function set_ColorBox_TColorListBox_OnEndDrag(p:TColorListBox;newMethod:Controls_TEndDragEvent;OldEvent:ControlsTEndDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTEndDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTEndDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEndDrag:=@callClass.call;
Result:=callClass;
end;
//property setterColorBox_TColorListBox_OnStartDrag
function set_ColorBox_TColorListBox_OnStartDrag(p:TColorListBox;newMethod:Controls_TStartDragEvent;OldEvent:ControlsTStartDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTStartDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTStartDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnStartDrag:=@callClass.call;
Result:=callClass;
end;
//constructorColorBox_TColorListBox_Create
function ColorBox_TColorListBox_Create(AOwner:tcomponent):TColorListBox;cdecl;
begin
Result:=TColorListBox.Create((AOwner));
end;
//constructorExtCtrls_TCustomControlBar_Create
function ExtCtrls_TCustomControlBar_Create(AOwner:tcomponent):TCustomControlBar;cdecl;
begin
Result:=TCustomControlBar.Create((AOwner));
end;
//property getterExtCtrls_TCustomControlBar_AutoDock
function get_ExtCtrls_TCustomControlBar_AutoDock(p:TCustomControlBar):Integer;cdecl;
begin
Result:=BooleanTointegert(p.AutoDock);
end;
//property setterExtCtrls_TCustomControlBar_AutoDock
procedure set_ExtCtrls_TCustomControlBar_AutoDock(p:TCustomControlBar;v:Integer);cdecl; 
begin
p.AutoDock:=integertToBoolean(v);
end;
//property getterExtCtrls_TCustomControlBar_AutoDrag
function get_ExtCtrls_TCustomControlBar_AutoDrag(p:TCustomControlBar):Integer;cdecl;
begin
Result:=BooleanTointegert(p.AutoDrag);
end;
//property setterExtCtrls_TCustomControlBar_AutoDrag
procedure set_ExtCtrls_TCustomControlBar_AutoDrag(p:TCustomControlBar;v:Integer);cdecl; 
begin
p.AutoDrag:=integertToBoolean(v);
end;
//property getterExtCtrls_TCustomControlBar_DrawingStyle
function get_ExtCtrls_TCustomControlBar_DrawingStyle(p:TCustomControlBar):Integer;cdecl;
begin
Result:=Integer(p.DrawingStyle);
end;
//property setterExtCtrls_TCustomControlBar_DrawingStyle
procedure set_ExtCtrls_TCustomControlBar_DrawingStyle(p:TCustomControlBar;v:tbanddrawingstyle);cdecl; 
begin
p.DrawingStyle:=(v);
end;
//property getterExtCtrls_TCustomControlBar_GradientDirection
function get_ExtCtrls_TCustomControlBar_GradientDirection(p:TCustomControlBar):Integer;cdecl;
begin
Result:=Integer(p.GradientDirection);
end;
//property setterExtCtrls_TCustomControlBar_GradientDirection
procedure set_ExtCtrls_TCustomControlBar_GradientDirection(p:TCustomControlBar;v:tgradientdirection);cdecl; 
begin
p.GradientDirection:=(v);
end;
//constructorGraphics_TPicture_Create
function Graphics_TPicture_Create():TPicture;cdecl;
begin
Result:=TPicture.Create();
end;
//property getterGraphics_TPicture_Bitmap
function get_Graphics_TPicture_Bitmap(p:TPicture):tbitmap;cdecl;
begin
Result:=tbitmap(p.Bitmap);
end;
//property setterGraphics_TPicture_Bitmap
procedure set_Graphics_TPicture_Bitmap(p:TPicture;v:tbitmap);cdecl; 
begin
p.Bitmap:=(v);
end;
//property getterGraphics_TPicture_Icon
function get_Graphics_TPicture_Icon(p:TPicture):ticon;cdecl;
begin
Result:=ticon(p.Icon);
end;
//property setterGraphics_TPicture_Icon
procedure set_Graphics_TPicture_Icon(p:TPicture;v:ticon);cdecl; 
begin
p.Icon:=(v);
end;
//constructorGraphics_TJPEGImage_Create
function Graphics_TJPEGImage_Create():TJPEGImage;cdecl;
begin
Result:=TJPEGImage.Create();
end;
//property getterGraphics_TJPEGImage_GrayScale
function get_Graphics_TJPEGImage_GrayScale(p:TJPEGImage):Integer;cdecl;
begin
Result:=BooleanTointegert(p.GrayScale);
end;
//property getterGraphics_TJPEGImage_ProgressiveEncoding
function get_Graphics_TJPEGImage_ProgressiveEncoding(p:TJPEGImage):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ProgressiveEncoding);
end;
//property getterGraphics_TPicture_Jpeg
function get_Graphics_TPicture_Jpeg(p:TPicture):tjpegimage;cdecl;
begin
Result:=tjpegimage(p.Jpeg);
end;
//property setterGraphics_TPicture_Jpeg
procedure set_Graphics_TPicture_Jpeg(p:TPicture;v:tjpegimage);cdecl; 
begin
p.Jpeg:=(v);
end;
//constructorGraphics_TPixmap_Create
function Graphics_TPixmap_Create():TPixmap;cdecl;
begin
Result:=TPixmap.Create();
end;
//property getterGraphics_TPicture_Pixmap
function get_Graphics_TPicture_Pixmap(p:TPicture):tpixmap;cdecl;
begin
Result:=tpixmap(p.Pixmap);
end;
//property setterGraphics_TPicture_Pixmap
procedure set_Graphics_TPicture_Pixmap(p:TPicture;v:tpixmap);cdecl; 
begin
p.Pixmap:=(v);
end;
//constructorGraphics_TPortableNetworkGraphic_Create
function Graphics_TPortableNetworkGraphic_Create():TPortableNetworkGraphic;cdecl;
begin
Result:=TPortableNetworkGraphic.Create();
end;
//property getterGraphics_TPicture_PNG
function get_Graphics_TPicture_PNG(p:TPicture):tportablenetworkgraphic;cdecl;
begin
Result:=tportablenetworkgraphic(p.PNG);
end;
//property setterGraphics_TPicture_PNG
procedure set_Graphics_TPicture_PNG(p:TPicture;v:tportablenetworkgraphic);cdecl; 
begin
p.PNG:=(v);
end;
//constructorGraphics_TPortableAnyMapGraphic_Create
function Graphics_TPortableAnyMapGraphic_Create():TPortableAnyMapGraphic;cdecl;
begin
Result:=TPortableAnyMapGraphic.Create();
end;
//property getterGraphics_TPicture_PNM
function get_Graphics_TPicture_PNM(p:TPicture):tportableanymapgraphic;cdecl;
begin
Result:=tportableanymapgraphic(p.PNM);
end;
//property setterGraphics_TPicture_PNM
procedure set_Graphics_TPicture_PNM(p:TPicture;v:tportableanymapgraphic);cdecl; 
begin
p.PNM:=(v);
end;
//property getterGraphics_TPicture_Graphic
function get_Graphics_TPicture_Graphic(p:TPicture):tgraphic;cdecl;
begin
Result:=tgraphic(p.Graphic);
end;
//property setterGraphics_TPicture_Graphic
procedure set_Graphics_TPicture_Graphic(p:TPicture;v:tgraphic);cdecl; 
begin
p.Graphic:=(v);
end;
//property getterGraphics_TPicture_Height
function get_Graphics_TPicture_Height(p:TPicture):Integer;cdecl;
begin
Result:=Integer(p.Height);
end;
//property getterGraphics_TPicture_Width
function get_Graphics_TPicture_Width(p:TPicture):Integer;cdecl;
begin
Result:=Integer(p.Width);
end;
//property setterGraphics_TPicture_OnChange
function set_Graphics_TPicture_OnChange(p:TPicture;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnChange:=@callClass.call;
Result:=callClass;
end;
//property getterExtCtrls_TCustomControlBar_Picture
function get_ExtCtrls_TCustomControlBar_Picture(p:TCustomControlBar):tpicture;cdecl;
begin
Result:=tpicture(p.Picture);
end;
//property setterExtCtrls_TCustomControlBar_Picture
procedure set_ExtCtrls_TCustomControlBar_Picture(p:TCustomControlBar;v:tpicture);cdecl; 
begin
p.Picture:=(v);
end;
//property getterExtCtrls_TCustomControlBar_RowSnap
function get_ExtCtrls_TCustomControlBar_RowSnap(p:TCustomControlBar):Integer;cdecl;
begin
Result:=BooleanTointegert(p.RowSnap);
end;
//property setterExtCtrls_TCustomControlBar_RowSnap
procedure set_ExtCtrls_TCustomControlBar_RowSnap(p:TCustomControlBar;v:Integer);cdecl; 
begin
p.RowSnap:=integertToBoolean(v);
end;
//property setterExtCtrls_TCustomControlBar_OnBandDrag
function set_ExtCtrls_TCustomControlBar_OnBandDrag(p:TCustomControlBar;newMethod:ExtCtrls_TBandDragEvent;OldEvent:ExtCtrlsTBandDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ExtCtrlsTBandDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ExtCtrlsTBandDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnBandDrag:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TCustomControlBar_OnCanResize
function set_ExtCtrls_TCustomControlBar_OnCanResize(p:TCustomControlBar;newMethod:ExtCtrls_TCanResizeEvent;OldEvent:ExtCtrlsTCanResizeEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ExtCtrlsTCanResizeEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ExtCtrlsTCanResizeEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnCanResize:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TCustomControlBar_OnPaint
function set_ExtCtrls_TCustomControlBar_OnPaint(p:TCustomControlBar;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnPaint:=@callClass.call;
Result:=callClass;
end;
//property getterExtCtrls_TControlBar_DragKind
function get_ExtCtrls_TControlBar_DragKind(p:TControlBar):Integer;cdecl;
begin
Result:=Integer(p.DragKind);
end;
//property setterExtCtrls_TControlBar_DragKind
procedure set_ExtCtrls_TControlBar_DragKind(p:TControlBar;v:tdragkind);cdecl; 
begin
p.DragKind:=(v);
end;
//property getterExtCtrls_TControlBar_DragMode
function get_ExtCtrls_TControlBar_DragMode(p:TControlBar):Integer;cdecl;
begin
Result:=Integer(p.DragMode);
end;
//property setterExtCtrls_TControlBar_DragMode
procedure set_ExtCtrls_TControlBar_DragMode(p:TControlBar;v:tdragmode);cdecl; 
begin
p.DragMode:=(v);
end;
//property getterExtCtrls_TControlBar_ParentFont
function get_ExtCtrls_TControlBar_ParentFont(p:TControlBar):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentFont);
end;
//property setterExtCtrls_TControlBar_ParentFont
procedure set_ExtCtrls_TControlBar_ParentFont(p:TControlBar;v:Integer);cdecl; 
begin
p.ParentFont:=integertToBoolean(v);
end;
//property getterExtCtrls_TControlBar_ParentShowHint
function get_ExtCtrls_TControlBar_ParentShowHint(p:TControlBar):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentShowHint);
end;
//property setterExtCtrls_TControlBar_ParentShowHint
procedure set_ExtCtrls_TControlBar_ParentShowHint(p:TControlBar;v:Integer);cdecl; 
begin
p.ParentShowHint:=integertToBoolean(v);
end;
//property setterExtCtrls_TControlBar_OnDblClick
function set_ExtCtrls_TControlBar_OnDblClick(p:TControlBar;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDblClick:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TControlBar_OnDragDrop
function set_ExtCtrls_TControlBar_OnDragDrop(p:TControlBar;newMethod:Controls_TDragDropEvent;OldEvent:ControlsTDragDropEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragDropEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragDropEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragDrop:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TControlBar_OnDragOver
function set_ExtCtrls_TControlBar_OnDragOver(p:TControlBar;newMethod:Controls_TDragOverEvent;OldEvent:ControlsTDragOverEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragOverEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragOverEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragOver:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TControlBar_OnEndDock
function set_ExtCtrls_TControlBar_OnEndDock(p:TControlBar;newMethod:Controls_TEndDragEvent;OldEvent:ControlsTEndDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTEndDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTEndDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEndDock:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TControlBar_OnEndDrag
function set_ExtCtrls_TControlBar_OnEndDrag(p:TControlBar;newMethod:Controls_TEndDragEvent;OldEvent:ControlsTEndDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTEndDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTEndDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEndDrag:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TControlBar_OnMouseDown
function set_ExtCtrls_TControlBar_OnMouseDown(p:TControlBar;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseDown:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TControlBar_OnMouseEnter
function set_ExtCtrls_TControlBar_OnMouseEnter(p:TControlBar;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseEnter:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TControlBar_OnMouseLeave
function set_ExtCtrls_TControlBar_OnMouseLeave(p:TControlBar;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseLeave:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TControlBar_OnMouseMove
function set_ExtCtrls_TControlBar_OnMouseMove(p:TControlBar;newMethod:Controls_TMouseMoveEvent;OldEvent:ControlsTMouseMoveEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseMoveEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseMoveEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseMove:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TControlBar_OnMouseUp
function set_ExtCtrls_TControlBar_OnMouseUp(p:TControlBar;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseUp:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TControlBar_OnStartDock
function set_ExtCtrls_TControlBar_OnStartDock(p:TControlBar;newMethod:Controls_TStartDockEvent;OldEvent:ControlsTStartDockEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTStartDockEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTStartDockEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnStartDock:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TControlBar_OnStartDrag
function set_ExtCtrls_TControlBar_OnStartDrag(p:TControlBar;newMethod:Controls_TStartDragEvent;OldEvent:ControlsTStartDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTStartDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTStartDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnStartDrag:=@callClass.call;
Result:=callClass;
end;
//constructorExtCtrls_TControlBar_Create
function ExtCtrls_TControlBar_Create(AOwner:tcomponent):TControlBar;cdecl;
begin
Result:=TControlBar.Create((AOwner));
end;
//property getterClasses_TCollection_Count
function get_Classes_TCollection_Count(p:TCollection):Integer;cdecl;
begin
Result:=Integer(p.Count);
end;
//property getterClasses_TCollectionItem_Collection
function get_Classes_TCollectionItem_Collection(p:TCollectionItem):tcollection;cdecl;
begin
Result:=tcollection(p.Collection);
end;
//property setterClasses_TCollectionItem_Collection
procedure set_Classes_TCollectionItem_Collection(p:TCollectionItem;v:tcollection);cdecl; 
begin
p.Collection:=(v);
end;
//property getterClasses_TCollectionItem_ID
function get_Classes_TCollectionItem_ID(p:TCollectionItem):Integer;cdecl;
begin
Result:=Integer(p.ID);
end;
//property getterClasses_TCollectionItem_Index
function get_Classes_TCollectionItem_Index(p:TCollectionItem):Integer;cdecl;
begin
Result:=Integer(p.Index);
end;
//property setterClasses_TCollectionItem_Index
procedure set_Classes_TCollectionItem_Index(p:TCollectionItem;v:Integer);cdecl; 
begin
p.Index:=(v);
end;
//property getterClasses_TCollectionItem_DisplayName
function get_Classes_TCollectionItem_DisplayName(p:TCollectionItem):PChar;cdecl;
begin
Result:=PChar(p.DisplayName);
end;
//property setterClasses_TCollectionItem_DisplayName
procedure set_Classes_TCollectionItem_DisplayName(p:TCollectionItem;v:PChar);cdecl; 
begin
p.DisplayName:=(v);
end;
//property getterClasses_TCollection_Items
function get_Classes_TCollection_Items(p:TCollection;Index:Integer):tcollectionitem;cdecl;
begin
Result:=tcollectionitem(p.Items[Index]);
end;
//property setterClasses_TCollection_Items
procedure set_Classes_TCollection_Items(p:TCollection;Index:Integer;v:tcollectionitem);cdecl; 
begin
p.Items[Index]:=(v);
end;
//property getterGrids_TGridColumns_Grid
function get_Grids_TGridColumns_Grid(p:TGridColumns):tcustomgrid;cdecl;
begin
Result:=tcustomgrid(p.Grid);
end;
//constructorGrids_TGridColumn_Create
function Grids_TGridColumn_Create(ACollection:tcollection):TGridColumn;cdecl;
begin
Result:=TGridColumn.Create((ACollection));
end;
//property getterGrids_TGridColumn_Grid
function get_Grids_TGridColumn_Grid(p:TGridColumn):tcustomgrid;cdecl;
begin
Result:=tcustomgrid(p.Grid);
end;
//property getterGrids_TGridColumn_DefaultWidth
function get_Grids_TGridColumn_DefaultWidth(p:TGridColumn):Integer;cdecl;
begin
Result:=Integer(p.DefaultWidth);
end;
//property getterGrids_TGridColumn_StoredWidth
function get_Grids_TGridColumn_StoredWidth(p:TGridColumn):Integer;cdecl;
begin
Result:=Integer(p.StoredWidth);
end;
//property getterGrids_TGridColumn_WidthChanged
function get_Grids_TGridColumn_WidthChanged(p:TGridColumn):Integer;cdecl;
begin
Result:=BooleanTointegert(p.WidthChanged);
end;
//property getterGrids_TGridColumn_Alignment
function get_Grids_TGridColumn_Alignment(p:TGridColumn):Integer;cdecl;
begin
Result:=Integer(p.Alignment);
end;
//property setterGrids_TGridColumn_Alignment
procedure set_Grids_TGridColumn_Alignment(p:TGridColumn;v:talignment);cdecl; 
begin
p.Alignment:=(v);
end;
//property getterGrids_TGridColumn_ButtonStyle
function get_Grids_TGridColumn_ButtonStyle(p:TGridColumn):Integer;cdecl;
begin
Result:=Integer(p.ButtonStyle);
end;
//property setterGrids_TGridColumn_ButtonStyle
procedure set_Grids_TGridColumn_ButtonStyle(p:TGridColumn;v:tcolumnbuttonstyle);cdecl; 
begin
p.ButtonStyle:=(v);
end;
//property getterGrids_TGridColumn_Expanded
function get_Grids_TGridColumn_Expanded(p:TGridColumn):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Expanded);
end;
//property setterGrids_TGridColumn_Expanded
procedure set_Grids_TGridColumn_Expanded(p:TGridColumn;v:Integer);cdecl; 
begin
p.Expanded:=integertToBoolean(v);
end;
//property getterGrids_TGridColumn_Font
function get_Grids_TGridColumn_Font(p:TGridColumn):tfont;cdecl;
begin
Result:=tfont(p.Font);
end;
//property setterGrids_TGridColumn_Font
procedure set_Grids_TGridColumn_Font(p:TGridColumn;v:tfont);cdecl; 
begin
p.Font:=(v);
end;
//property getterGrids_TGridColumn_Layout
function get_Grids_TGridColumn_Layout(p:TGridColumn):Integer;cdecl;
begin
Result:=Integer(p.Layout);
end;
//property setterGrids_TGridColumn_Layout
procedure set_Grids_TGridColumn_Layout(p:TGridColumn;v:ttextlayout);cdecl; 
begin
p.Layout:=(v);
end;
//property getterGrids_TGridColumn_MinSize
function get_Grids_TGridColumn_MinSize(p:TGridColumn):Integer;cdecl;
begin
Result:=Integer(p.MinSize);
end;
//property setterGrids_TGridColumn_MinSize
procedure set_Grids_TGridColumn_MinSize(p:TGridColumn;v:Integer);cdecl; 
begin
p.MinSize:=(v);
end;
//property getterGrids_TGridColumn_MaxSize
function get_Grids_TGridColumn_MaxSize(p:TGridColumn):Integer;cdecl;
begin
Result:=Integer(p.MaxSize);
end;
//property setterGrids_TGridColumn_MaxSize
procedure set_Grids_TGridColumn_MaxSize(p:TGridColumn;v:Integer);cdecl; 
begin
p.MaxSize:=(v);
end;
//property getterGrids_TGridColumn_PickList
function get_Grids_TGridColumn_PickList(p:TGridColumn):tstrings;cdecl;
begin
Result:=tstrings(p.PickList);
end;
//property setterGrids_TGridColumn_PickList
procedure set_Grids_TGridColumn_PickList(p:TGridColumn;v:tstrings);cdecl; 
begin
p.PickList:=(v);
end;
//property getterGrids_TGridColumn_ReadOnly
function get_Grids_TGridColumn_ReadOnly(p:TGridColumn):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ReadOnly);
end;
//property setterGrids_TGridColumn_ReadOnly
procedure set_Grids_TGridColumn_ReadOnly(p:TGridColumn;v:Integer);cdecl; 
begin
p.ReadOnly:=integertToBoolean(v);
end;
//property getterGrids_TGridColumn_SizePriority
function get_Grids_TGridColumn_SizePriority(p:TGridColumn):Integer;cdecl;
begin
Result:=Integer(p.SizePriority);
end;
//property setterGrids_TGridColumn_SizePriority
procedure set_Grids_TGridColumn_SizePriority(p:TGridColumn;v:Integer);cdecl; 
begin
p.SizePriority:=(v);
end;
//property getterGrids_TGridColumnTitle_Column
function get_Grids_TGridColumnTitle_Column(p:TGridColumnTitle):tgridcolumn;cdecl;
begin
Result:=tgridcolumn(p.Column);
end;
//property getterGrids_TGridColumnTitle_Alignment
function get_Grids_TGridColumnTitle_Alignment(p:TGridColumnTitle):Integer;cdecl;
begin
Result:=Integer(p.Alignment);
end;
//property setterGrids_TGridColumnTitle_Alignment
procedure set_Grids_TGridColumnTitle_Alignment(p:TGridColumnTitle;v:talignment);cdecl; 
begin
p.Alignment:=(v);
end;
//property getterGrids_TGridColumnTitle_Caption
function get_Grids_TGridColumnTitle_Caption(p:TGridColumnTitle):PChar;cdecl;
begin
Result:=PChar(p.Caption);
end;
//property setterGrids_TGridColumnTitle_Caption
procedure set_Grids_TGridColumnTitle_Caption(p:TGridColumnTitle;v:PChar);cdecl; 
begin
p.Caption:=(v);
end;
//property getterGrids_TGridColumnTitle_Font
function get_Grids_TGridColumnTitle_Font(p:TGridColumnTitle):tfont;cdecl;
begin
Result:=tfont(p.Font);
end;
//property setterGrids_TGridColumnTitle_Font
procedure set_Grids_TGridColumnTitle_Font(p:TGridColumnTitle;v:tfont);cdecl; 
begin
p.Font:=(v);
end;
//property getterGrids_TGridColumnTitle_ImageIndex
function get_Grids_TGridColumnTitle_ImageIndex(p:TGridColumnTitle):Integer;cdecl;
begin
Result:=Integer(p.ImageIndex);
end;
//property setterGrids_TGridColumnTitle_ImageIndex
procedure set_Grids_TGridColumnTitle_ImageIndex(p:TGridColumnTitle;v:Integer);cdecl; 
begin
p.ImageIndex:=(v);
end;
//property getterGrids_TGridColumnTitle_ImageLayout
function get_Grids_TGridColumnTitle_ImageLayout(p:TGridColumnTitle):Integer;cdecl;
begin
Result:=Integer(p.ImageLayout);
end;
//property setterGrids_TGridColumnTitle_ImageLayout
procedure set_Grids_TGridColumnTitle_ImageLayout(p:TGridColumnTitle;v:tbuttonlayout);cdecl; 
begin
p.ImageLayout:=(v);
end;
//property getterGrids_TGridColumnTitle_Layout
function get_Grids_TGridColumnTitle_Layout(p:TGridColumnTitle):Integer;cdecl;
begin
Result:=Integer(p.Layout);
end;
//property setterGrids_TGridColumnTitle_Layout
procedure set_Grids_TGridColumnTitle_Layout(p:TGridColumnTitle;v:ttextlayout);cdecl; 
begin
p.Layout:=(v);
end;
//property getterGrids_TGridColumnTitle_MultiLine
function get_Grids_TGridColumnTitle_MultiLine(p:TGridColumnTitle):Integer;cdecl;
begin
Result:=BooleanTointegert(p.MultiLine);
end;
//property setterGrids_TGridColumnTitle_MultiLine
procedure set_Grids_TGridColumnTitle_MultiLine(p:TGridColumnTitle;v:Integer);cdecl; 
begin
p.MultiLine:=integertToBoolean(v);
end;
//property getterGrids_TGridColumnTitle_PrefixOption
function get_Grids_TGridColumnTitle_PrefixOption(p:TGridColumnTitle):Integer;cdecl;
begin
Result:=Integer(p.PrefixOption);
end;
//property setterGrids_TGridColumnTitle_PrefixOption
procedure set_Grids_TGridColumnTitle_PrefixOption(p:TGridColumnTitle;v:tprefixoption);cdecl; 
begin
p.PrefixOption:=(v);
end;
//property getterGrids_TGridColumn_Title
function get_Grids_TGridColumn_Title(p:TGridColumn):tgridcolumntitle;cdecl;
begin
Result:=tgridcolumntitle(p.Title);
end;
//property setterGrids_TGridColumn_Title
procedure set_Grids_TGridColumn_Title(p:TGridColumn;v:tgridcolumntitle);cdecl; 
begin
p.Title:=(v);
end;
//property getterGrids_TGridColumn_Width
function get_Grids_TGridColumn_Width(p:TGridColumn):Integer;cdecl;
begin
Result:=Integer(p.Width);
end;
//property setterGrids_TGridColumn_Width
procedure set_Grids_TGridColumn_Width(p:TGridColumn;v:Integer);cdecl; 
begin
p.Width:=(v);
end;
//property getterGrids_TGridColumn_Visible
function get_Grids_TGridColumn_Visible(p:TGridColumn):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Visible);
end;
//property setterGrids_TGridColumn_Visible
procedure set_Grids_TGridColumn_Visible(p:TGridColumn;v:Integer);cdecl; 
begin
p.Visible:=integertToBoolean(v);
end;
//property getterGrids_TGridColumn_ValueChecked
function get_Grids_TGridColumn_ValueChecked(p:TGridColumn):PChar;cdecl;
begin
Result:=PChar(p.ValueChecked);
end;
//property setterGrids_TGridColumn_ValueChecked
procedure set_Grids_TGridColumn_ValueChecked(p:TGridColumn;v:PChar);cdecl; 
begin
p.ValueChecked:=(v);
end;
//property getterGrids_TGridColumn_ValueUnchecked
function get_Grids_TGridColumn_ValueUnchecked(p:TGridColumn):PChar;cdecl;
begin
Result:=PChar(p.ValueUnchecked);
end;
//property setterGrids_TGridColumn_ValueUnchecked
procedure set_Grids_TGridColumn_ValueUnchecked(p:TGridColumn;v:PChar);cdecl; 
begin
p.ValueUnchecked:=(v);
end;
//property getterGrids_TGridColumns_Items
function get_Grids_TGridColumns_Items(p:TGridColumns;Index:Integer):tgridcolumn;cdecl;
begin
Result:=tgridcolumn(p.Items[Index]);
end;
//property setterGrids_TGridColumns_Items
procedure set_Grids_TGridColumns_Items(p:TGridColumns;Index:Integer;v:tgridcolumn);cdecl; 
begin
p.Items[Index]:=(v);
end;
//property getterGrids_TGridColumns_VisibleCount
function get_Grids_TGridColumns_VisibleCount(p:TGridColumns):Integer;cdecl;
begin
Result:=Integer(p.VisibleCount);
end;
//property getterGrids_TGridColumns_Enabled
function get_Grids_TGridColumns_Enabled(p:TGridColumns):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Enabled);
end;
//property getterControls_TDragImageList_Dragging
function get_Controls_TDragImageList_Dragging(p:TDragImageList):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Dragging);
end;
//constructorControls_TDragImageList_Create
function Controls_TDragImageList_Create(AOwner:tcomponent):TDragImageList;cdecl;
begin
Result:=TDragImageList.Create((AOwner));
end;
//constructorControls_TImageList_Create
function Controls_TImageList_Create(AOwner:tcomponent):TImageList;cdecl;
begin
Result:=TImageList.Create((AOwner));
end;
//constructorGrids_TCustomGrid_Create
function Grids_TCustomGrid_Create(AOwner:tcomponent):TCustomGrid;cdecl;
begin
Result:=TCustomGrid.Create((AOwner));
end;
//property getterGrids_TCustomGrid_SelectedRangeCount
function get_Grids_TCustomGrid_SelectedRangeCount(p:TCustomGrid):Integer;cdecl;
begin
Result:=Integer(p.SelectedRangeCount);
end;
//property getterGrids_TCustomGrid_SortOrder
function get_Grids_TCustomGrid_SortOrder(p:TCustomGrid):Integer;cdecl;
begin
Result:=Integer(p.SortOrder);
end;
//property setterGrids_TCustomGrid_SortOrder
procedure set_Grids_TCustomGrid_SortOrder(p:TCustomGrid;v:tsortorder);cdecl; 
begin
p.SortOrder:=(v);
end;
//property getterGrids_TCustomGrid_SortColumn
function get_Grids_TCustomGrid_SortColumn(p:TCustomGrid):Integer;cdecl;
begin
Result:=Integer(p.SortColumn);
end;
//constructorGrids_TCustomDrawGrid_Create
function Grids_TCustomDrawGrid_Create(AOwner:tcomponent):TCustomDrawGrid;cdecl;
begin
Result:=TCustomDrawGrid.Create((AOwner));
end;
//property getterGrids_TCustomDrawGrid_AllowOutboundEvents
function get_Grids_TCustomDrawGrid_AllowOutboundEvents(p:TCustomDrawGrid):Integer;cdecl;
begin
Result:=BooleanTointegert(p.AllowOutboundEvents);
end;
//property setterGrids_TCustomDrawGrid_AllowOutboundEvents
procedure set_Grids_TCustomDrawGrid_AllowOutboundEvents(p:TCustomDrawGrid;v:Integer);cdecl; 
begin
p.AllowOutboundEvents:=integertToBoolean(v);
end;
//property getterGrids_TCustomDrawGrid_Col
function get_Grids_TCustomDrawGrid_Col(p:TCustomDrawGrid):Integer;cdecl;
begin
Result:=Integer(p.Col);
end;
//property setterGrids_TCustomDrawGrid_Col
procedure set_Grids_TCustomDrawGrid_Col(p:TCustomDrawGrid;v:Integer);cdecl; 
begin
p.Col:=(v);
end;
//property getterGrids_TCustomDrawGrid_ColWidths
function get_Grids_TCustomDrawGrid_ColWidths(p:TCustomDrawGrid;aCol:Integer):Integer;cdecl;
begin
Result:=Integer(p.ColWidths[aCol]);
end;
//property setterGrids_TCustomDrawGrid_ColWidths
procedure set_Grids_TCustomDrawGrid_ColWidths(p:TCustomDrawGrid;aCol:Integer;v:Integer);cdecl; 
begin
p.ColWidths[aCol]:=(v);
end;
//property getterGrids_TCustomDrawGrid_Editor
function get_Grids_TCustomDrawGrid_Editor(p:TCustomDrawGrid):twincontrol;cdecl;
begin
Result:=twincontrol(p.Editor);
end;
//property setterGrids_TCustomDrawGrid_Editor
procedure set_Grids_TCustomDrawGrid_Editor(p:TCustomDrawGrid;v:twincontrol);cdecl; 
begin
p.Editor:=(v);
end;
//property getterGrids_TCustomDrawGrid_EditorMode
function get_Grids_TCustomDrawGrid_EditorMode(p:TCustomDrawGrid):Integer;cdecl;
begin
Result:=BooleanTointegert(p.EditorMode);
end;
//property setterGrids_TCustomDrawGrid_EditorMode
procedure set_Grids_TCustomDrawGrid_EditorMode(p:TCustomDrawGrid;v:Integer);cdecl; 
begin
p.EditorMode:=integertToBoolean(v);
end;
//property getterGrids_TCustomDrawGrid_ExtendedColSizing
function get_Grids_TCustomDrawGrid_ExtendedColSizing(p:TCustomDrawGrid):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ExtendedColSizing);
end;
//property setterGrids_TCustomDrawGrid_ExtendedColSizing
procedure set_Grids_TCustomDrawGrid_ExtendedColSizing(p:TCustomDrawGrid;v:Integer);cdecl; 
begin
p.ExtendedColSizing:=integertToBoolean(v);
end;
//property getterGrids_TCustomDrawGrid_AltColorStartNormal
function get_Grids_TCustomDrawGrid_AltColorStartNormal(p:TCustomDrawGrid):Integer;cdecl;
begin
Result:=BooleanTointegert(p.AltColorStartNormal);
end;
//property setterGrids_TCustomDrawGrid_AltColorStartNormal
procedure set_Grids_TCustomDrawGrid_AltColorStartNormal(p:TCustomDrawGrid;v:Integer);cdecl; 
begin
p.AltColorStartNormal:=integertToBoolean(v);
end;
//property getterGrids_TCustomDrawGrid_FastEditing
function get_Grids_TCustomDrawGrid_FastEditing(p:TCustomDrawGrid):Integer;cdecl;
begin
Result:=BooleanTointegert(p.FastEditing);
end;
//property setterGrids_TCustomDrawGrid_FastEditing
procedure set_Grids_TCustomDrawGrid_FastEditing(p:TCustomDrawGrid;v:Integer);cdecl; 
begin
p.FastEditing:=integertToBoolean(v);
end;
//property getterGrids_TCustomDrawGrid_FocusRectVisible
function get_Grids_TCustomDrawGrid_FocusRectVisible(p:TCustomDrawGrid):Integer;cdecl;
begin
Result:=BooleanTointegert(p.FocusRectVisible);
end;
//property setterGrids_TCustomDrawGrid_FocusRectVisible
procedure set_Grids_TCustomDrawGrid_FocusRectVisible(p:TCustomDrawGrid;v:Integer);cdecl; 
begin
p.FocusRectVisible:=integertToBoolean(v);
end;
//property getterGrids_TCustomDrawGrid_GridHeight
function get_Grids_TCustomDrawGrid_GridHeight(p:TCustomDrawGrid):Integer;cdecl;
begin
Result:=Integer(p.GridHeight);
end;
//property getterGrids_TCustomDrawGrid_GridWidth
function get_Grids_TCustomDrawGrid_GridWidth(p:TCustomDrawGrid):Integer;cdecl;
begin
Result:=Integer(p.GridWidth);
end;
//property getterGrids_TCustomDrawGrid_IsCellSelected
function get_Grids_TCustomDrawGrid_IsCellSelected(p:TCustomDrawGrid;aCol:Integer;aRow:Integer):Integer;cdecl;
begin
Result:=BooleanTointegert(p.IsCellSelected[aCol,aRow]);
end;
//property getterGrids_TCustomDrawGrid_LeftCol
function get_Grids_TCustomDrawGrid_LeftCol(p:TCustomDrawGrid):Integer;cdecl;
begin
Result:=Integer(p.LeftCol);
end;
//property setterGrids_TCustomDrawGrid_LeftCol
procedure set_Grids_TCustomDrawGrid_LeftCol(p:TCustomDrawGrid;v:Integer);cdecl; 
begin
p.LeftCol:=(v);
end;
//property getterGrids_TCustomDrawGrid_Row
function get_Grids_TCustomDrawGrid_Row(p:TCustomDrawGrid):Integer;cdecl;
begin
Result:=Integer(p.Row);
end;
//property setterGrids_TCustomDrawGrid_Row
procedure set_Grids_TCustomDrawGrid_Row(p:TCustomDrawGrid;v:Integer);cdecl; 
begin
p.Row:=(v);
end;
//property getterGrids_TCustomDrawGrid_RowHeights
function get_Grids_TCustomDrawGrid_RowHeights(p:TCustomDrawGrid;aRow:Integer):Integer;cdecl;
begin
Result:=Integer(p.RowHeights[aRow]);
end;
//property setterGrids_TCustomDrawGrid_RowHeights
procedure set_Grids_TCustomDrawGrid_RowHeights(p:TCustomDrawGrid;aRow:Integer;v:Integer);cdecl; 
begin
p.RowHeights[aRow]:=(v);
end;
//property getterGrids_TCustomDrawGrid_SaveOptions
function get_Grids_TCustomDrawGrid_SaveOptions(p:TCustomDrawGrid):Integer;cdecl;
begin
Result:=Integer(p.SaveOptions);
end;
//property setterGrids_TCustomDrawGrid_SaveOptions
procedure set_Grids_TCustomDrawGrid_SaveOptions(p:TCustomDrawGrid;v:tsaveoptions);cdecl; 
begin
p.SaveOptions:=(v);
end;
//property getterGrids_TCustomDrawGrid_SelectedColumn
function get_Grids_TCustomDrawGrid_SelectedColumn(p:TCustomDrawGrid):tgridcolumn;cdecl;
begin
Result:=tgridcolumn(p.SelectedColumn);
end;
//property getterGrids_TCustomDrawGrid_StrictSort
function get_Grids_TCustomDrawGrid_StrictSort(p:TCustomDrawGrid):Integer;cdecl;
begin
Result:=BooleanTointegert(p.StrictSort);
end;
//property setterGrids_TCustomDrawGrid_StrictSort
procedure set_Grids_TCustomDrawGrid_StrictSort(p:TCustomDrawGrid;v:Integer);cdecl; 
begin
p.StrictSort:=integertToBoolean(v);
end;
//property getterGrids_TCustomDrawGrid_TopRow
function get_Grids_TCustomDrawGrid_TopRow(p:TCustomDrawGrid):Integer;cdecl;
begin
Result:=Integer(p.TopRow);
end;
//property setterGrids_TCustomDrawGrid_TopRow
procedure set_Grids_TCustomDrawGrid_TopRow(p:TCustomDrawGrid;v:Integer);cdecl; 
begin
p.TopRow:=(v);
end;
//property getterGrids_TCustomDrawGrid_UseXORFeatures
function get_Grids_TCustomDrawGrid_UseXORFeatures(p:TCustomDrawGrid):Integer;cdecl;
begin
Result:=BooleanTointegert(p.UseXORFeatures);
end;
//property setterGrids_TCustomDrawGrid_UseXORFeatures
procedure set_Grids_TCustomDrawGrid_UseXORFeatures(p:TCustomDrawGrid;v:Integer);cdecl; 
begin
p.UseXORFeatures:=integertToBoolean(v);
end;
//property getterGrids_TCustomDrawGrid_AutoAdvance
function get_Grids_TCustomDrawGrid_AutoAdvance(p:TCustomDrawGrid):Integer;cdecl;
begin
Result:=Integer(p.AutoAdvance);
end;
//property setterGrids_TCustomDrawGrid_AutoAdvance
procedure set_Grids_TCustomDrawGrid_AutoAdvance(p:TCustomDrawGrid;v:tautoadvance);cdecl; 
begin
p.AutoAdvance:=(v);
end;
//property getterGrids_TCustomDrawGrid_AutoFillColumns
function get_Grids_TCustomDrawGrid_AutoFillColumns(p:TCustomDrawGrid):Integer;cdecl;
begin
Result:=BooleanTointegert(p.AutoFillColumns);
end;
//property setterGrids_TCustomDrawGrid_AutoFillColumns
procedure set_Grids_TCustomDrawGrid_AutoFillColumns(p:TCustomDrawGrid;v:Integer);cdecl; 
begin
p.AutoFillColumns:=integertToBoolean(v);
end;
//property getterGrids_TCustomDrawGrid_ColCount
function get_Grids_TCustomDrawGrid_ColCount(p:TCustomDrawGrid):Integer;cdecl;
begin
Result:=Integer(p.ColCount);
end;
//property setterGrids_TCustomDrawGrid_ColCount
procedure set_Grids_TCustomDrawGrid_ColCount(p:TCustomDrawGrid;v:Integer);cdecl; 
begin
p.ColCount:=(v);
end;
//property getterGrids_TCustomDrawGrid_Columns
function get_Grids_TCustomDrawGrid_Columns(p:TCustomDrawGrid):tgridcolumns;cdecl;
begin
Result:=tgridcolumns(p.Columns);
end;
//property setterGrids_TCustomDrawGrid_Columns
procedure set_Grids_TCustomDrawGrid_Columns(p:TCustomDrawGrid;v:tgridcolumns);cdecl; 
begin
p.Columns:=(v);
end;
//property getterGrids_TCustomDrawGrid_DefaultColWidth
function get_Grids_TCustomDrawGrid_DefaultColWidth(p:TCustomDrawGrid):Integer;cdecl;
begin
Result:=Integer(p.DefaultColWidth);
end;
//property setterGrids_TCustomDrawGrid_DefaultColWidth
procedure set_Grids_TCustomDrawGrid_DefaultColWidth(p:TCustomDrawGrid;v:Integer);cdecl; 
begin
p.DefaultColWidth:=(v);
end;
//property getterGrids_TCustomDrawGrid_DefaultDrawing
function get_Grids_TCustomDrawGrid_DefaultDrawing(p:TCustomDrawGrid):Integer;cdecl;
begin
Result:=BooleanTointegert(p.DefaultDrawing);
end;
//property setterGrids_TCustomDrawGrid_DefaultDrawing
procedure set_Grids_TCustomDrawGrid_DefaultDrawing(p:TCustomDrawGrid;v:Integer);cdecl; 
begin
p.DefaultDrawing:=integertToBoolean(v);
end;
//property getterGrids_TCustomDrawGrid_DefaultRowHeight
function get_Grids_TCustomDrawGrid_DefaultRowHeight(p:TCustomDrawGrid):Integer;cdecl;
begin
Result:=Integer(p.DefaultRowHeight);
end;
//property setterGrids_TCustomDrawGrid_DefaultRowHeight
procedure set_Grids_TCustomDrawGrid_DefaultRowHeight(p:TCustomDrawGrid;v:Integer);cdecl; 
begin
p.DefaultRowHeight:=(v);
end;
//property getterGrids_TCustomDrawGrid_FixedCols
function get_Grids_TCustomDrawGrid_FixedCols(p:TCustomDrawGrid):Integer;cdecl;
begin
Result:=Integer(p.FixedCols);
end;
//property setterGrids_TCustomDrawGrid_FixedCols
procedure set_Grids_TCustomDrawGrid_FixedCols(p:TCustomDrawGrid;v:Integer);cdecl; 
begin
p.FixedCols:=(v);
end;
//property getterGrids_TCustomDrawGrid_FixedRows
function get_Grids_TCustomDrawGrid_FixedRows(p:TCustomDrawGrid):Integer;cdecl;
begin
Result:=Integer(p.FixedRows);
end;
//property setterGrids_TCustomDrawGrid_FixedRows
procedure set_Grids_TCustomDrawGrid_FixedRows(p:TCustomDrawGrid;v:Integer);cdecl; 
begin
p.FixedRows:=(v);
end;
//property getterGrids_TCustomDrawGrid_Flat
function get_Grids_TCustomDrawGrid_Flat(p:TCustomDrawGrid):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Flat);
end;
//property setterGrids_TCustomDrawGrid_Flat
procedure set_Grids_TCustomDrawGrid_Flat(p:TCustomDrawGrid;v:Integer);cdecl; 
begin
p.Flat:=integertToBoolean(v);
end;
//property getterGrids_TCustomDrawGrid_GridLineWidth
function get_Grids_TCustomDrawGrid_GridLineWidth(p:TCustomDrawGrid):Integer;cdecl;
begin
Result:=Integer(p.GridLineWidth);
end;
//property setterGrids_TCustomDrawGrid_GridLineWidth
procedure set_Grids_TCustomDrawGrid_GridLineWidth(p:TCustomDrawGrid;v:Integer);cdecl; 
begin
p.GridLineWidth:=(v);
end;
//property getterGrids_TCustomDrawGrid_Options
function get_Grids_TCustomDrawGrid_Options(p:TCustomDrawGrid):Integer;cdecl;
begin
Result:=Integer(p.Options);
end;
//property setterGrids_TCustomDrawGrid_Options
procedure set_Grids_TCustomDrawGrid_Options(p:TCustomDrawGrid;v:tgridoptions);cdecl; 
begin
p.Options:=(v);
end;
//property getterGrids_TCustomDrawGrid_Options2
function get_Grids_TCustomDrawGrid_Options2(p:TCustomDrawGrid):Integer;cdecl;
begin
Result:=Integer(p.Options2);
end;
//property setterGrids_TCustomDrawGrid_Options2
procedure set_Grids_TCustomDrawGrid_Options2(p:TCustomDrawGrid;v:tgridoptions2);cdecl; 
begin
p.Options2:=(v);
end;
//property getterGrids_TCustomDrawGrid_ParentShowHint
function get_Grids_TCustomDrawGrid_ParentShowHint(p:TCustomDrawGrid):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentShowHint);
end;
//property setterGrids_TCustomDrawGrid_ParentShowHint
procedure set_Grids_TCustomDrawGrid_ParentShowHint(p:TCustomDrawGrid;v:Integer);cdecl; 
begin
p.ParentShowHint:=integertToBoolean(v);
end;
//property getterGrids_TCustomDrawGrid_RowCount
function get_Grids_TCustomDrawGrid_RowCount(p:TCustomDrawGrid):Integer;cdecl;
begin
Result:=Integer(p.RowCount);
end;
//property setterGrids_TCustomDrawGrid_RowCount
procedure set_Grids_TCustomDrawGrid_RowCount(p:TCustomDrawGrid;v:Integer);cdecl; 
begin
p.RowCount:=(v);
end;
//property getterGrids_TCustomDrawGrid_ScrollBars
function get_Grids_TCustomDrawGrid_ScrollBars(p:TCustomDrawGrid):Integer;cdecl;
begin
Result:=Integer(p.ScrollBars);
end;
//property setterGrids_TCustomDrawGrid_ScrollBars
procedure set_Grids_TCustomDrawGrid_ScrollBars(p:TCustomDrawGrid;v:tscrollstyle);cdecl; 
begin
p.ScrollBars:=(v);
end;
//property getterGrids_TCustomDrawGrid_TabAdvance
function get_Grids_TCustomDrawGrid_TabAdvance(p:TCustomDrawGrid):Integer;cdecl;
begin
Result:=Integer(p.TabAdvance);
end;
//property setterGrids_TCustomDrawGrid_TabAdvance
procedure set_Grids_TCustomDrawGrid_TabAdvance(p:TCustomDrawGrid;v:tautoadvance);cdecl; 
begin
p.TabAdvance:=(v);
end;
//property getterGrids_TCustomDrawGrid_VisibleColCount
function get_Grids_TCustomDrawGrid_VisibleColCount(p:TCustomDrawGrid):Integer;cdecl;
begin
Result:=Integer(p.VisibleColCount);
end;
//property getterGrids_TCustomDrawGrid_VisibleRowCount
function get_Grids_TCustomDrawGrid_VisibleRowCount(p:TCustomDrawGrid):Integer;cdecl;
begin
Result:=Integer(p.VisibleRowCount);
end;
//property setterGrids_TCustomDrawGrid_OnAfterSelection
function set_Grids_TCustomDrawGrid_OnAfterSelection(p:TCustomDrawGrid;newMethod:Grids_TOnSelectEvent;OldEvent:GridsTOnSelectEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:GridsTOnSelectEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=GridsTOnSelectEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnAfterSelection:=@callClass.call;
Result:=callClass;
end;
//property setterGrids_TCustomDrawGrid_OnBeforeSelection
function set_Grids_TCustomDrawGrid_OnBeforeSelection(p:TCustomDrawGrid;newMethod:Grids_TOnSelectEvent;OldEvent:GridsTOnSelectEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:GridsTOnSelectEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=GridsTOnSelectEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnBeforeSelection:=@callClass.call;
Result:=callClass;
end;
//property setterGrids_TCustomDrawGrid_OnColRowDeleted
function set_Grids_TCustomDrawGrid_OnColRowDeleted(p:TCustomDrawGrid;newMethod:Grids_TGridOperationEvent;OldEvent:GridsTGridOperationEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:GridsTGridOperationEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=GridsTGridOperationEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnColRowDeleted:=@callClass.call;
Result:=callClass;
end;
//property setterGrids_TCustomDrawGrid_OnColRowExchanged
function set_Grids_TCustomDrawGrid_OnColRowExchanged(p:TCustomDrawGrid;newMethod:Grids_TGridOperationEvent;OldEvent:GridsTGridOperationEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:GridsTGridOperationEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=GridsTGridOperationEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnColRowExchanged:=@callClass.call;
Result:=callClass;
end;
//property setterGrids_TCustomDrawGrid_OnColRowInserted
function set_Grids_TCustomDrawGrid_OnColRowInserted(p:TCustomDrawGrid;newMethod:Grids_TGridOperationEvent;OldEvent:GridsTGridOperationEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:GridsTGridOperationEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=GridsTGridOperationEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnColRowInserted:=@callClass.call;
Result:=callClass;
end;
//property setterGrids_TCustomDrawGrid_OnColRowMoved
function set_Grids_TCustomDrawGrid_OnColRowMoved(p:TCustomDrawGrid;newMethod:Grids_TGridOperationEvent;OldEvent:GridsTGridOperationEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:GridsTGridOperationEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=GridsTGridOperationEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnColRowMoved:=@callClass.call;
Result:=callClass;
end;
//property setterGrids_TCustomDrawGrid_OnCompareCells
function set_Grids_TCustomDrawGrid_OnCompareCells(p:TCustomDrawGrid;newMethod:Grids_TOnCompareCells;OldEvent:GridsTOnCompareCells_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:GridsTOnCompareCells_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=GridsTOnCompareCells_wrapper.Create;
callClass.c:=newMethod;
p.OnCompareCells:=@callClass.call;
Result:=callClass;
end;
//property setterGrids_TCustomDrawGrid_OnDblClick
function set_Grids_TCustomDrawGrid_OnDblClick(p:TCustomDrawGrid;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDblClick:=@callClass.call;
Result:=callClass;
end;
//property setterGrids_TCustomDrawGrid_OnDragDrop
function set_Grids_TCustomDrawGrid_OnDragDrop(p:TCustomDrawGrid;newMethod:Controls_TDragDropEvent;OldEvent:ControlsTDragDropEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragDropEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragDropEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragDrop:=@callClass.call;
Result:=callClass;
end;
//property setterGrids_TCustomDrawGrid_OnDragOver
function set_Grids_TCustomDrawGrid_OnDragOver(p:TCustomDrawGrid;newMethod:Controls_TDragOverEvent;OldEvent:ControlsTDragOverEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragOverEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragOverEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragOver:=@callClass.call;
Result:=callClass;
end;
//property setterGrids_TCustomDrawGrid_OnEditButtonClick
function set_Grids_TCustomDrawGrid_OnEditButtonClick(p:TCustomDrawGrid;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEditButtonClick:=@callClass.call;
Result:=callClass;
end;
//property setterGrids_TCustomDrawGrid_OnButtonClick
function set_Grids_TCustomDrawGrid_OnButtonClick(p:TCustomDrawGrid;newMethod:Grids_TOnSelectEvent;OldEvent:GridsTOnSelectEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:GridsTOnSelectEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=GridsTOnSelectEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnButtonClick:=@callClass.call;
Result:=callClass;
end;
//property setterGrids_TCustomDrawGrid_OnEndDock
function set_Grids_TCustomDrawGrid_OnEndDock(p:TCustomDrawGrid;newMethod:Controls_TEndDragEvent;OldEvent:ControlsTEndDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTEndDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTEndDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEndDock:=@callClass.call;
Result:=callClass;
end;
//property setterGrids_TCustomDrawGrid_OnEndDrag
function set_Grids_TCustomDrawGrid_OnEndDrag(p:TCustomDrawGrid;newMethod:Controls_TEndDragEvent;OldEvent:ControlsTEndDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTEndDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTEndDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEndDrag:=@callClass.call;
Result:=callClass;
end;
//property setterGrids_TCustomDrawGrid_OnGetEditMask
function set_Grids_TCustomDrawGrid_OnGetEditMask(p:TCustomDrawGrid;newMethod:Grids_TGetEditEvent;OldEvent:GridsTGetEditEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:GridsTGetEditEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=GridsTGetEditEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnGetEditMask:=@callClass.call;
Result:=callClass;
end;
//property setterGrids_TCustomDrawGrid_OnGetEditText
function set_Grids_TCustomDrawGrid_OnGetEditText(p:TCustomDrawGrid;newMethod:Grids_TGetEditEvent;OldEvent:GridsTGetEditEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:GridsTGetEditEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=GridsTGetEditEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnGetEditText:=@callClass.call;
Result:=callClass;
end;
//property setterGrids_TCustomDrawGrid_OnHeaderClick
function set_Grids_TCustomDrawGrid_OnHeaderClick(p:TCustomDrawGrid;newMethod:Grids_THdrEvent;OldEvent:GridsTHdrEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:GridsTHdrEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=GridsTHdrEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnHeaderClick:=@callClass.call;
Result:=callClass;
end;
//property setterGrids_TCustomDrawGrid_OnHeaderSized
function set_Grids_TCustomDrawGrid_OnHeaderSized(p:TCustomDrawGrid;newMethod:Grids_THdrEvent;OldEvent:GridsTHdrEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:GridsTHdrEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=GridsTHdrEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnHeaderSized:=@callClass.call;
Result:=callClass;
end;
//property setterGrids_TCustomDrawGrid_OnHeaderSizing
function set_Grids_TCustomDrawGrid_OnHeaderSizing(p:TCustomDrawGrid;newMethod:Grids_THeaderSizingEvent;OldEvent:GridsTHeaderSizingEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:GridsTHeaderSizingEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=GridsTHeaderSizingEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnHeaderSizing:=@callClass.call;
Result:=callClass;
end;
//property setterGrids_TCustomDrawGrid_OnMouseDown
function set_Grids_TCustomDrawGrid_OnMouseDown(p:TCustomDrawGrid;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseDown:=@callClass.call;
Result:=callClass;
end;
//property setterGrids_TCustomDrawGrid_OnMouseEnter
function set_Grids_TCustomDrawGrid_OnMouseEnter(p:TCustomDrawGrid;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseEnter:=@callClass.call;
Result:=callClass;
end;
//property setterGrids_TCustomDrawGrid_OnMouseLeave
function set_Grids_TCustomDrawGrid_OnMouseLeave(p:TCustomDrawGrid;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseLeave:=@callClass.call;
Result:=callClass;
end;
//property setterGrids_TCustomDrawGrid_OnMouseMove
function set_Grids_TCustomDrawGrid_OnMouseMove(p:TCustomDrawGrid;newMethod:Controls_TMouseMoveEvent;OldEvent:ControlsTMouseMoveEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseMoveEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseMoveEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseMove:=@callClass.call;
Result:=callClass;
end;
//property setterGrids_TCustomDrawGrid_OnMouseUp
function set_Grids_TCustomDrawGrid_OnMouseUp(p:TCustomDrawGrid;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseUp:=@callClass.call;
Result:=callClass;
end;
//property setterGrids_TCustomDrawGrid_OnPickListSelect
function set_Grids_TCustomDrawGrid_OnPickListSelect(p:TCustomDrawGrid;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnPickListSelect:=@callClass.call;
Result:=callClass;
end;
//property setterGrids_TCustomDrawGrid_OnPrepareCanvas
function set_Grids_TCustomDrawGrid_OnPrepareCanvas(p:TCustomDrawGrid;newMethod:Grids_TOnPrepareCanvasEvent;OldEvent:GridsTOnPrepareCanvasEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:GridsTOnPrepareCanvasEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=GridsTOnPrepareCanvasEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnPrepareCanvas:=@callClass.call;
Result:=callClass;
end;
//property setterGrids_TCustomDrawGrid_OnSelectEditor
function set_Grids_TCustomDrawGrid_OnSelectEditor(p:TCustomDrawGrid;newMethod:Grids_TSelectEditorEvent;OldEvent:GridsTSelectEditorEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:GridsTSelectEditorEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=GridsTSelectEditorEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnSelectEditor:=@callClass.call;
Result:=callClass;
end;
//property setterGrids_TCustomDrawGrid_OnSelection
function set_Grids_TCustomDrawGrid_OnSelection(p:TCustomDrawGrid;newMethod:Grids_TOnSelectEvent;OldEvent:GridsTOnSelectEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:GridsTOnSelectEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=GridsTOnSelectEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnSelection:=@callClass.call;
Result:=callClass;
end;
//property setterGrids_TCustomDrawGrid_OnSelectCell
function set_Grids_TCustomDrawGrid_OnSelectCell(p:TCustomDrawGrid;newMethod:Grids_TOnSelectCellEvent;OldEvent:GridsTOnSelectCellEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:GridsTOnSelectCellEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=GridsTOnSelectCellEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnSelectCell:=@callClass.call;
Result:=callClass;
end;
//property setterGrids_TCustomDrawGrid_OnSetEditText
function set_Grids_TCustomDrawGrid_OnSetEditText(p:TCustomDrawGrid;newMethod:Grids_TSetEditEvent;OldEvent:GridsTSetEditEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:GridsTSetEditEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=GridsTSetEditEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnSetEditText:=@callClass.call;
Result:=callClass;
end;
//property setterGrids_TCustomDrawGrid_OnStartDock
function set_Grids_TCustomDrawGrid_OnStartDock(p:TCustomDrawGrid;newMethod:Controls_TStartDockEvent;OldEvent:ControlsTStartDockEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTStartDockEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTStartDockEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnStartDock:=@callClass.call;
Result:=callClass;
end;
//property setterGrids_TCustomDrawGrid_OnStartDrag
function set_Grids_TCustomDrawGrid_OnStartDrag(p:TCustomDrawGrid;newMethod:Controls_TStartDragEvent;OldEvent:ControlsTStartDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTStartDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTStartDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnStartDrag:=@callClass.call;
Result:=callClass;
end;
//property getterGrids_TDrawGrid_InplaceEditor
function get_Grids_TDrawGrid_InplaceEditor(p:TDrawGrid):twincontrol;cdecl;
begin
Result:=twincontrol(p.InplaceEditor);
end;
//property getterGrids_TDrawGrid_AutoEdit
function get_Grids_TDrawGrid_AutoEdit(p:TDrawGrid):Integer;cdecl;
begin
Result:=BooleanTointegert(p.AutoEdit);
end;
//property setterGrids_TDrawGrid_AutoEdit
procedure set_Grids_TDrawGrid_AutoEdit(p:TDrawGrid;v:Integer);cdecl; 
begin
p.AutoEdit:=integertToBoolean(v);
end;
//property getterGrids_TDrawGrid_ColumnClickSorts
function get_Grids_TDrawGrid_ColumnClickSorts(p:TDrawGrid):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ColumnClickSorts);
end;
//property setterGrids_TDrawGrid_ColumnClickSorts
procedure set_Grids_TDrawGrid_ColumnClickSorts(p:TDrawGrid;v:Integer);cdecl; 
begin
p.ColumnClickSorts:=integertToBoolean(v);
end;
//property getterGrids_TDrawGrid_DragKind
function get_Grids_TDrawGrid_DragKind(p:TDrawGrid):Integer;cdecl;
begin
Result:=Integer(p.DragKind);
end;
//property setterGrids_TDrawGrid_DragKind
procedure set_Grids_TDrawGrid_DragKind(p:TDrawGrid;v:tdragkind);cdecl; 
begin
p.DragKind:=(v);
end;
//property getterGrids_TDrawGrid_DragMode
function get_Grids_TDrawGrid_DragMode(p:TDrawGrid):Integer;cdecl;
begin
Result:=Integer(p.DragMode);
end;
//property setterGrids_TDrawGrid_DragMode
procedure set_Grids_TDrawGrid_DragMode(p:TDrawGrid;v:tdragmode);cdecl; 
begin
p.DragMode:=(v);
end;
//property getterGrids_TDrawGrid_ExtendedSelect
function get_Grids_TDrawGrid_ExtendedSelect(p:TDrawGrid):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ExtendedSelect);
end;
//property setterGrids_TDrawGrid_ExtendedSelect
procedure set_Grids_TDrawGrid_ExtendedSelect(p:TDrawGrid;v:Integer);cdecl; 
begin
p.ExtendedSelect:=integertToBoolean(v);
end;
//property getterGrids_TDrawGrid_HeaderHotZones
function get_Grids_TDrawGrid_HeaderHotZones(p:TDrawGrid):Integer;cdecl;
begin
Result:=Integer(p.HeaderHotZones);
end;
//property setterGrids_TDrawGrid_HeaderHotZones
procedure set_Grids_TDrawGrid_HeaderHotZones(p:TDrawGrid;v:tgridzoneset);cdecl; 
begin
p.HeaderHotZones:=(v);
end;
//property getterGrids_TDrawGrid_HeaderPushZones
function get_Grids_TDrawGrid_HeaderPushZones(p:TDrawGrid):Integer;cdecl;
begin
Result:=Integer(p.HeaderPushZones);
end;
//property setterGrids_TDrawGrid_HeaderPushZones
procedure set_Grids_TDrawGrid_HeaderPushZones(p:TDrawGrid;v:tgridzoneset);cdecl; 
begin
p.HeaderPushZones:=(v);
end;
//property getterGrids_TDrawGrid_MouseWheelOption
function get_Grids_TDrawGrid_MouseWheelOption(p:TDrawGrid):Integer;cdecl;
begin
Result:=Integer(p.MouseWheelOption);
end;
//property setterGrids_TDrawGrid_MouseWheelOption
procedure set_Grids_TDrawGrid_MouseWheelOption(p:TDrawGrid;v:tmousewheeloption);cdecl; 
begin
p.MouseWheelOption:=(v);
end;
//property getterGrids_TDrawGrid_ParentColor
function get_Grids_TDrawGrid_ParentColor(p:TDrawGrid):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentColor);
end;
//property setterGrids_TDrawGrid_ParentColor
procedure set_Grids_TDrawGrid_ParentColor(p:TDrawGrid;v:Integer);cdecl; 
begin
p.ParentColor:=integertToBoolean(v);
end;
//property getterGrids_TDrawGrid_ParentFont
function get_Grids_TDrawGrid_ParentFont(p:TDrawGrid):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentFont);
end;
//property setterGrids_TDrawGrid_ParentFont
procedure set_Grids_TDrawGrid_ParentFont(p:TDrawGrid;v:Integer);cdecl; 
begin
p.ParentFont:=integertToBoolean(v);
end;
//property getterGrids_TDrawGrid_RangeSelectMode
function get_Grids_TDrawGrid_RangeSelectMode(p:TDrawGrid):Integer;cdecl;
begin
Result:=Integer(p.RangeSelectMode);
end;
//property setterGrids_TDrawGrid_RangeSelectMode
procedure set_Grids_TDrawGrid_RangeSelectMode(p:TDrawGrid;v:trangeselectmode);cdecl; 
begin
p.RangeSelectMode:=(v);
end;
//property getterGrids_TDrawGrid_TitleFont
function get_Grids_TDrawGrid_TitleFont(p:TDrawGrid):tfont;cdecl;
begin
Result:=tfont(p.TitleFont);
end;
//property setterGrids_TDrawGrid_TitleFont
procedure set_Grids_TDrawGrid_TitleFont(p:TDrawGrid;v:tfont);cdecl; 
begin
p.TitleFont:=(v);
end;
//property getterGrids_TDrawGrid_TitleImageList
function get_Grids_TDrawGrid_TitleImageList(p:TDrawGrid):timagelist;cdecl;
begin
Result:=timagelist(p.TitleImageList);
end;
//property setterGrids_TDrawGrid_TitleImageList
procedure set_Grids_TDrawGrid_TitleImageList(p:TDrawGrid;v:timagelist);cdecl; 
begin
p.TitleImageList:=(v);
end;
//property getterGrids_TDrawGrid_TitleStyle
function get_Grids_TDrawGrid_TitleStyle(p:TDrawGrid):Integer;cdecl;
begin
Result:=Integer(p.TitleStyle);
end;
//property setterGrids_TDrawGrid_TitleStyle
procedure set_Grids_TDrawGrid_TitleStyle(p:TDrawGrid;v:ttitlestyle);cdecl; 
begin
p.TitleStyle:=(v);
end;
//property setterGrids_TDrawGrid_OnCheckboxToggled
function set_Grids_TDrawGrid_OnCheckboxToggled(p:TDrawGrid;newMethod:Grids_TToggledCheckboxEvent;OldEvent:GridsTToggledCheckboxEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:GridsTToggledCheckboxEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=GridsTToggledCheckboxEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnCheckboxToggled:=@callClass.call;
Result:=callClass;
end;
//property setterGrids_TDrawGrid_OnEditingDone
function set_Grids_TDrawGrid_OnEditingDone(p:TDrawGrid;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEditingDone:=@callClass.call;
Result:=callClass;
end;
//property setterGrids_TDrawGrid_OnGetCellHint
function set_Grids_TDrawGrid_OnGetCellHint(p:TDrawGrid;newMethod:Grids_TGetCellHintEvent;OldEvent:GridsTGetCellHintEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:GridsTGetCellHintEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=GridsTGetCellHintEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnGetCellHint:=@callClass.call;
Result:=callClass;
end;
//property setterGrids_TDrawGrid_OnGetCheckboxState
function set_Grids_TDrawGrid_OnGetCheckboxState(p:TDrawGrid;newMethod:Grids_TGetCheckboxStateEvent;OldEvent:GridsTGetCheckboxStateEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:GridsTGetCheckboxStateEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=GridsTGetCheckboxStateEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnGetCheckboxState:=@callClass.call;
Result:=callClass;
end;
//property setterGrids_TDrawGrid_OnSetCheckboxState
function set_Grids_TDrawGrid_OnSetCheckboxState(p:TDrawGrid;newMethod:Grids_TSetCheckboxStateEvent;OldEvent:GridsTSetCheckboxStateEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:GridsTSetCheckboxStateEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=GridsTSetCheckboxStateEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnSetCheckboxState:=@callClass.call;
Result:=callClass;
end;
//property setterGrids_TDrawGrid_OnUserCheckboxBitmap
function set_Grids_TDrawGrid_OnUserCheckboxBitmap(p:TDrawGrid;newMethod:Grids_TUserCheckBoxBitmapEvent;OldEvent:GridsTUserCheckBoxBitmapEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:GridsTUserCheckBoxBitmapEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=GridsTUserCheckBoxBitmapEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnUserCheckboxBitmap:=@callClass.call;
Result:=callClass;
end;
//constructorGrids_TDrawGrid_Create
function Grids_TDrawGrid_Create(AOwner:tcomponent):TDrawGrid;cdecl;
begin
Result:=TDrawGrid.Create((AOwner));
end;
//constructorExtCtrls_TCustomFlowPanel_Create
function ExtCtrls_TCustomFlowPanel_Create(AOwner:tcomponent):TCustomFlowPanel;cdecl;
begin
Result:=TCustomFlowPanel.Create((AOwner));
end;
//property getterExtCtrls_TCustomFlowPanel_AutoWrap
function get_ExtCtrls_TCustomFlowPanel_AutoWrap(p:TCustomFlowPanel):Integer;cdecl;
begin
Result:=BooleanTointegert(p.AutoWrap);
end;
//property setterExtCtrls_TCustomFlowPanel_AutoWrap
procedure set_ExtCtrls_TCustomFlowPanel_AutoWrap(p:TCustomFlowPanel;v:Integer);cdecl; 
begin
p.AutoWrap:=integertToBoolean(v);
end;
//constructorExtCtrls_TFlowPanelControlList_Create
function ExtCtrls_TFlowPanelControlList_Create(AOwner:tpersistent):TFlowPanelControlList;cdecl;
begin
Result:=TFlowPanelControlList.Create((AOwner));
end;
//property getterExtCtrls_TFlowPanelControl_Control
function get_ExtCtrls_TFlowPanelControl_Control(p:TFlowPanelControl):tcontrol;cdecl;
begin
Result:=tcontrol(p.Control);
end;
//property setterExtCtrls_TFlowPanelControl_Control
procedure set_ExtCtrls_TFlowPanelControl_Control(p:TFlowPanelControl;v:tcontrol);cdecl; 
begin
p.Control:=(v);
end;
//property getterExtCtrls_TFlowPanelControl_WrapAfter
function get_ExtCtrls_TFlowPanelControl_WrapAfter(p:TFlowPanelControl):Integer;cdecl;
begin
Result:=Integer(p.WrapAfter);
end;
//property setterExtCtrls_TFlowPanelControl_WrapAfter
procedure set_ExtCtrls_TFlowPanelControl_WrapAfter(p:TFlowPanelControl;v:twrapafter);cdecl; 
begin
p.WrapAfter:=(v);
end;
//property getterExtCtrls_TFlowPanelControlList_Items
function get_ExtCtrls_TFlowPanelControlList_Items(p:TFlowPanelControlList;Index:Integer):tflowpanelcontrol;cdecl;
begin
Result:=tflowpanelcontrol(p.Items[Index]);
end;
//property setterExtCtrls_TFlowPanelControlList_Items
procedure set_ExtCtrls_TFlowPanelControlList_Items(p:TFlowPanelControlList;Index:Integer;v:tflowpanelcontrol);cdecl; 
begin
p.Items[Index]:=(v);
end;
//property getterExtCtrls_TCustomFlowPanel_ControlList
function get_ExtCtrls_TCustomFlowPanel_ControlList(p:TCustomFlowPanel):tflowpanelcontrollist;cdecl;
begin
Result:=tflowpanelcontrollist(p.ControlList);
end;
//property setterExtCtrls_TCustomFlowPanel_ControlList
procedure set_ExtCtrls_TCustomFlowPanel_ControlList(p:TCustomFlowPanel;v:tflowpanelcontrollist);cdecl; 
begin
p.ControlList:=(v);
end;
//property getterExtCtrls_TCustomFlowPanel_FlowStyle
function get_ExtCtrls_TCustomFlowPanel_FlowStyle(p:TCustomFlowPanel):Integer;cdecl;
begin
Result:=Integer(p.FlowStyle);
end;
//property setterExtCtrls_TCustomFlowPanel_FlowStyle
procedure set_ExtCtrls_TCustomFlowPanel_FlowStyle(p:TCustomFlowPanel;v:tflowstyle);cdecl; 
begin
p.FlowStyle:=(v);
end;
//property getterExtCtrls_TCustomFlowPanel_FlowLayout
function get_ExtCtrls_TCustomFlowPanel_FlowLayout(p:TCustomFlowPanel):Integer;cdecl;
begin
Result:=Integer(p.FlowLayout);
end;
//property setterExtCtrls_TCustomFlowPanel_FlowLayout
procedure set_ExtCtrls_TCustomFlowPanel_FlowLayout(p:TCustomFlowPanel;v:ttextlayout);cdecl; 
begin
p.FlowLayout:=(v);
end;
//property getterExtCtrls_TFlowPanel_DragKind
function get_ExtCtrls_TFlowPanel_DragKind(p:TFlowPanel):Integer;cdecl;
begin
Result:=Integer(p.DragKind);
end;
//property setterExtCtrls_TFlowPanel_DragKind
procedure set_ExtCtrls_TFlowPanel_DragKind(p:TFlowPanel;v:tdragkind);cdecl; 
begin
p.DragKind:=(v);
end;
//property getterExtCtrls_TFlowPanel_DragMode
function get_ExtCtrls_TFlowPanel_DragMode(p:TFlowPanel):Integer;cdecl;
begin
Result:=Integer(p.DragMode);
end;
//property setterExtCtrls_TFlowPanel_DragMode
procedure set_ExtCtrls_TFlowPanel_DragMode(p:TFlowPanel;v:tdragmode);cdecl; 
begin
p.DragMode:=(v);
end;
//property getterExtCtrls_TFlowPanel_ParentFont
function get_ExtCtrls_TFlowPanel_ParentFont(p:TFlowPanel):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentFont);
end;
//property setterExtCtrls_TFlowPanel_ParentFont
procedure set_ExtCtrls_TFlowPanel_ParentFont(p:TFlowPanel;v:Integer);cdecl; 
begin
p.ParentFont:=integertToBoolean(v);
end;
//property getterExtCtrls_TFlowPanel_ParentShowHint
function get_ExtCtrls_TFlowPanel_ParentShowHint(p:TFlowPanel):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentShowHint);
end;
//property setterExtCtrls_TFlowPanel_ParentShowHint
procedure set_ExtCtrls_TFlowPanel_ParentShowHint(p:TFlowPanel;v:Integer);cdecl; 
begin
p.ParentShowHint:=integertToBoolean(v);
end;
//property setterExtCtrls_TFlowPanel_OnDblClick
function set_ExtCtrls_TFlowPanel_OnDblClick(p:TFlowPanel;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDblClick:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TFlowPanel_OnDragDrop
function set_ExtCtrls_TFlowPanel_OnDragDrop(p:TFlowPanel;newMethod:Controls_TDragDropEvent;OldEvent:ControlsTDragDropEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragDropEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragDropEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragDrop:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TFlowPanel_OnDragOver
function set_ExtCtrls_TFlowPanel_OnDragOver(p:TFlowPanel;newMethod:Controls_TDragOverEvent;OldEvent:ControlsTDragOverEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragOverEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragOverEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragOver:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TFlowPanel_OnEndDock
function set_ExtCtrls_TFlowPanel_OnEndDock(p:TFlowPanel;newMethod:Controls_TEndDragEvent;OldEvent:ControlsTEndDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTEndDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTEndDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEndDock:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TFlowPanel_OnEndDrag
function set_ExtCtrls_TFlowPanel_OnEndDrag(p:TFlowPanel;newMethod:Controls_TEndDragEvent;OldEvent:ControlsTEndDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTEndDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTEndDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEndDrag:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TFlowPanel_OnMouseDown
function set_ExtCtrls_TFlowPanel_OnMouseDown(p:TFlowPanel;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseDown:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TFlowPanel_OnMouseEnter
function set_ExtCtrls_TFlowPanel_OnMouseEnter(p:TFlowPanel;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseEnter:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TFlowPanel_OnMouseLeave
function set_ExtCtrls_TFlowPanel_OnMouseLeave(p:TFlowPanel;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseLeave:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TFlowPanel_OnMouseMove
function set_ExtCtrls_TFlowPanel_OnMouseMove(p:TFlowPanel;newMethod:Controls_TMouseMoveEvent;OldEvent:ControlsTMouseMoveEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseMoveEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseMoveEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseMove:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TFlowPanel_OnMouseUp
function set_ExtCtrls_TFlowPanel_OnMouseUp(p:TFlowPanel;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseUp:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TFlowPanel_OnStartDock
function set_ExtCtrls_TFlowPanel_OnStartDock(p:TFlowPanel;newMethod:Controls_TStartDockEvent;OldEvent:ControlsTStartDockEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTStartDockEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTStartDockEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnStartDock:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TFlowPanel_OnStartDrag
function set_ExtCtrls_TFlowPanel_OnStartDrag(p:TFlowPanel;newMethod:Controls_TStartDragEvent;OldEvent:ControlsTStartDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTStartDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTStartDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnStartDrag:=@callClass.call;
Result:=callClass;
end;
//constructorExtCtrls_TFlowPanel_Create
function ExtCtrls_TFlowPanel_Create(AOwner:tcomponent):TFlowPanel;cdecl;
begin
Result:=TFlowPanel.Create((AOwner));
end;
//constructorExtCtrls_TCustomImage_Create
function ExtCtrls_TCustomImage_Create(AOwner:tcomponent):TCustomImage;cdecl;
begin
Result:=TCustomImage.Create((AOwner));
end;
//property getterExtCtrls_TCustomImage_Canvas
function get_ExtCtrls_TCustomImage_Canvas(p:TCustomImage):tcanvas;cdecl;
begin
Result:=tcanvas(p.Canvas);
end;
//property getterExtCtrls_TCustomImage_AntialiasingMode
function get_ExtCtrls_TCustomImage_AntialiasingMode(p:TCustomImage):Integer;cdecl;
begin
Result:=Integer(p.AntialiasingMode);
end;
//property setterExtCtrls_TCustomImage_AntialiasingMode
procedure set_ExtCtrls_TCustomImage_AntialiasingMode(p:TCustomImage;v:tantialiasingmode);cdecl; 
begin
p.AntialiasingMode:=(v);
end;
//property getterExtCtrls_TCustomImage_Center
function get_ExtCtrls_TCustomImage_Center(p:TCustomImage):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Center);
end;
//property setterExtCtrls_TCustomImage_Center
procedure set_ExtCtrls_TCustomImage_Center(p:TCustomImage;v:Integer);cdecl; 
begin
p.Center:=integertToBoolean(v);
end;
//property getterExtCtrls_TCustomImage_KeepOriginXWhenClipped
function get_ExtCtrls_TCustomImage_KeepOriginXWhenClipped(p:TCustomImage):Integer;cdecl;
begin
Result:=BooleanTointegert(p.KeepOriginXWhenClipped);
end;
//property setterExtCtrls_TCustomImage_KeepOriginXWhenClipped
procedure set_ExtCtrls_TCustomImage_KeepOriginXWhenClipped(p:TCustomImage;v:Integer);cdecl; 
begin
p.KeepOriginXWhenClipped:=integertToBoolean(v);
end;
//property getterExtCtrls_TCustomImage_KeepOriginYWhenClipped
function get_ExtCtrls_TCustomImage_KeepOriginYWhenClipped(p:TCustomImage):Integer;cdecl;
begin
Result:=BooleanTointegert(p.KeepOriginYWhenClipped);
end;
//property setterExtCtrls_TCustomImage_KeepOriginYWhenClipped
procedure set_ExtCtrls_TCustomImage_KeepOriginYWhenClipped(p:TCustomImage;v:Integer);cdecl; 
begin
p.KeepOriginYWhenClipped:=integertToBoolean(v);
end;
//property getterExtCtrls_TCustomImage_Picture
function get_ExtCtrls_TCustomImage_Picture(p:TCustomImage):tpicture;cdecl;
begin
Result:=tpicture(p.Picture);
end;
//property setterExtCtrls_TCustomImage_Picture
procedure set_ExtCtrls_TCustomImage_Picture(p:TCustomImage;v:tpicture);cdecl; 
begin
p.Picture:=(v);
end;
//property setterExtCtrls_TCustomImage_OnMouseDown
function set_ExtCtrls_TCustomImage_OnMouseDown(p:TCustomImage;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseDown:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TCustomImage_OnMouseEnter
function set_ExtCtrls_TCustomImage_OnMouseEnter(p:TCustomImage;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseEnter:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TCustomImage_OnMouseLeave
function set_ExtCtrls_TCustomImage_OnMouseLeave(p:TCustomImage;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseLeave:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TCustomImage_OnMouseMove
function set_ExtCtrls_TCustomImage_OnMouseMove(p:TCustomImage;newMethod:Controls_TMouseMoveEvent;OldEvent:ControlsTMouseMoveEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseMoveEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseMoveEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseMove:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TCustomImage_OnMouseUp
function set_ExtCtrls_TCustomImage_OnMouseUp(p:TCustomImage;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseUp:=@callClass.call;
Result:=callClass;
end;
//property getterExtCtrls_TCustomImage_Stretch
function get_ExtCtrls_TCustomImage_Stretch(p:TCustomImage):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Stretch);
end;
//property setterExtCtrls_TCustomImage_Stretch
procedure set_ExtCtrls_TCustomImage_Stretch(p:TCustomImage;v:Integer);cdecl; 
begin
p.Stretch:=integertToBoolean(v);
end;
//property getterExtCtrls_TCustomImage_StretchOutEnabled
function get_ExtCtrls_TCustomImage_StretchOutEnabled(p:TCustomImage):Integer;cdecl;
begin
Result:=BooleanTointegert(p.StretchOutEnabled);
end;
//property setterExtCtrls_TCustomImage_StretchOutEnabled
procedure set_ExtCtrls_TCustomImage_StretchOutEnabled(p:TCustomImage;v:Integer);cdecl; 
begin
p.StretchOutEnabled:=integertToBoolean(v);
end;
//property getterExtCtrls_TCustomImage_StretchInEnabled
function get_ExtCtrls_TCustomImage_StretchInEnabled(p:TCustomImage):Integer;cdecl;
begin
Result:=BooleanTointegert(p.StretchInEnabled);
end;
//property setterExtCtrls_TCustomImage_StretchInEnabled
procedure set_ExtCtrls_TCustomImage_StretchInEnabled(p:TCustomImage;v:Integer);cdecl; 
begin
p.StretchInEnabled:=integertToBoolean(v);
end;
//property getterExtCtrls_TCustomImage_Transparent
function get_ExtCtrls_TCustomImage_Transparent(p:TCustomImage):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Transparent);
end;
//property setterExtCtrls_TCustomImage_Transparent
procedure set_ExtCtrls_TCustomImage_Transparent(p:TCustomImage;v:Integer);cdecl; 
begin
p.Transparent:=integertToBoolean(v);
end;
//property getterExtCtrls_TCustomImage_Proportional
function get_ExtCtrls_TCustomImage_Proportional(p:TCustomImage):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Proportional);
end;
//property setterExtCtrls_TCustomImage_Proportional
procedure set_ExtCtrls_TCustomImage_Proportional(p:TCustomImage;v:Integer);cdecl; 
begin
p.Proportional:=integertToBoolean(v);
end;
//property setterExtCtrls_TCustomImage_OnPictureChanged
function set_ExtCtrls_TCustomImage_OnPictureChanged(p:TCustomImage;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnPictureChanged:=@callClass.call;
Result:=callClass;
end;
//property getterExtCtrls_TImage_DragMode
function get_ExtCtrls_TImage_DragMode(p:TImage):Integer;cdecl;
begin
Result:=Integer(p.DragMode);
end;
//property setterExtCtrls_TImage_DragMode
procedure set_ExtCtrls_TImage_DragMode(p:TImage;v:tdragmode);cdecl; 
begin
p.DragMode:=(v);
end;
//property setterExtCtrls_TImage_OnDblClick
function set_ExtCtrls_TImage_OnDblClick(p:TImage;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDblClick:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TImage_OnDragDrop
function set_ExtCtrls_TImage_OnDragDrop(p:TImage;newMethod:Controls_TDragDropEvent;OldEvent:ControlsTDragDropEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragDropEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragDropEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragDrop:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TImage_OnDragOver
function set_ExtCtrls_TImage_OnDragOver(p:TImage;newMethod:Controls_TDragOverEvent;OldEvent:ControlsTDragOverEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragOverEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragOverEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragOver:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TImage_OnEndDrag
function set_ExtCtrls_TImage_OnEndDrag(p:TImage;newMethod:Controls_TEndDragEvent;OldEvent:ControlsTEndDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTEndDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTEndDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEndDrag:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TImage_OnPaint
function set_ExtCtrls_TImage_OnPaint(p:TImage;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnPaint:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TImage_OnStartDrag
function set_ExtCtrls_TImage_OnStartDrag(p:TImage;newMethod:Controls_TStartDragEvent;OldEvent:ControlsTStartDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTStartDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTStartDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnStartDrag:=@callClass.call;
Result:=callClass;
end;
//property getterExtCtrls_TImage_ParentShowHint
function get_ExtCtrls_TImage_ParentShowHint(p:TImage):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentShowHint);
end;
//property setterExtCtrls_TImage_ParentShowHint
procedure set_ExtCtrls_TImage_ParentShowHint(p:TImage;v:Integer);cdecl; 
begin
p.ParentShowHint:=integertToBoolean(v);
end;
//constructorExtCtrls_TImage_Create
function ExtCtrls_TImage_Create(AOwner:tcomponent):TImage;cdecl;
begin
Result:=TImage.Create((AOwner));
end;
//constructorExtCtrls_TCustomLabeledEdit_Create
function ExtCtrls_TCustomLabeledEdit_Create(TheOwner:tcomponent):TCustomLabeledEdit;cdecl;
begin
Result:=TCustomLabeledEdit.Create((TheOwner));
end;
//constructorExtCtrls_TBoundLabel_Create
function ExtCtrls_TBoundLabel_Create(TheOwner:tcomponent):TBoundLabel;cdecl;
begin
Result:=TBoundLabel.Create((TheOwner));
end;
//property getterExtCtrls_TBoundLabel_FocusControl
function get_ExtCtrls_TBoundLabel_FocusControl(p:TBoundLabel):twincontrol;cdecl;
begin
Result:=twincontrol(p.FocusControl);
end;
//property setterExtCtrls_TBoundLabel_FocusControl
procedure set_ExtCtrls_TBoundLabel_FocusControl(p:TBoundLabel;v:twincontrol);cdecl; 
begin
p.FocusControl:=(v);
end;
//property getterExtCtrls_TBoundLabel_DragMode
function get_ExtCtrls_TBoundLabel_DragMode(p:TBoundLabel):Integer;cdecl;
begin
Result:=Integer(p.DragMode);
end;
//property setterExtCtrls_TBoundLabel_DragMode
procedure set_ExtCtrls_TBoundLabel_DragMode(p:TBoundLabel;v:tdragmode);cdecl; 
begin
p.DragMode:=(v);
end;
//property getterExtCtrls_TBoundLabel_ParentColor
function get_ExtCtrls_TBoundLabel_ParentColor(p:TBoundLabel):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentColor);
end;
//property setterExtCtrls_TBoundLabel_ParentColor
procedure set_ExtCtrls_TBoundLabel_ParentColor(p:TBoundLabel;v:Integer);cdecl; 
begin
p.ParentColor:=integertToBoolean(v);
end;
//property getterExtCtrls_TBoundLabel_ParentFont
function get_ExtCtrls_TBoundLabel_ParentFont(p:TBoundLabel):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentFont);
end;
//property setterExtCtrls_TBoundLabel_ParentFont
procedure set_ExtCtrls_TBoundLabel_ParentFont(p:TBoundLabel;v:Integer);cdecl; 
begin
p.ParentFont:=integertToBoolean(v);
end;
//property getterExtCtrls_TBoundLabel_ParentShowHint
function get_ExtCtrls_TBoundLabel_ParentShowHint(p:TBoundLabel):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentShowHint);
end;
//property setterExtCtrls_TBoundLabel_ParentShowHint
procedure set_ExtCtrls_TBoundLabel_ParentShowHint(p:TBoundLabel;v:Integer);cdecl; 
begin
p.ParentShowHint:=integertToBoolean(v);
end;
//property getterExtCtrls_TBoundLabel_ShowAccelChar
function get_ExtCtrls_TBoundLabel_ShowAccelChar(p:TBoundLabel):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ShowAccelChar);
end;
//property setterExtCtrls_TBoundLabel_ShowAccelChar
procedure set_ExtCtrls_TBoundLabel_ShowAccelChar(p:TBoundLabel;v:Integer);cdecl; 
begin
p.ShowAccelChar:=integertToBoolean(v);
end;
//property getterExtCtrls_TBoundLabel_Layout
function get_ExtCtrls_TBoundLabel_Layout(p:TBoundLabel):Integer;cdecl;
begin
Result:=Integer(p.Layout);
end;
//property setterExtCtrls_TBoundLabel_Layout
procedure set_ExtCtrls_TBoundLabel_Layout(p:TBoundLabel;v:ttextlayout);cdecl; 
begin
p.Layout:=(v);
end;
//property getterExtCtrls_TBoundLabel_WordWrap
function get_ExtCtrls_TBoundLabel_WordWrap(p:TBoundLabel):Integer;cdecl;
begin
Result:=BooleanTointegert(p.WordWrap);
end;
//property setterExtCtrls_TBoundLabel_WordWrap
procedure set_ExtCtrls_TBoundLabel_WordWrap(p:TBoundLabel;v:Integer);cdecl; 
begin
p.WordWrap:=integertToBoolean(v);
end;
//property setterExtCtrls_TBoundLabel_OnDblClick
function set_ExtCtrls_TBoundLabel_OnDblClick(p:TBoundLabel;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDblClick:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TBoundLabel_OnDragDrop
function set_ExtCtrls_TBoundLabel_OnDragDrop(p:TBoundLabel;newMethod:Controls_TDragDropEvent;OldEvent:ControlsTDragDropEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragDropEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragDropEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragDrop:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TBoundLabel_OnDragOver
function set_ExtCtrls_TBoundLabel_OnDragOver(p:TBoundLabel;newMethod:Controls_TDragOverEvent;OldEvent:ControlsTDragOverEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragOverEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragOverEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragOver:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TBoundLabel_OnEndDrag
function set_ExtCtrls_TBoundLabel_OnEndDrag(p:TBoundLabel;newMethod:Controls_TEndDragEvent;OldEvent:ControlsTEndDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTEndDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTEndDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEndDrag:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TBoundLabel_OnMouseDown
function set_ExtCtrls_TBoundLabel_OnMouseDown(p:TBoundLabel;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseDown:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TBoundLabel_OnMouseEnter
function set_ExtCtrls_TBoundLabel_OnMouseEnter(p:TBoundLabel;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseEnter:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TBoundLabel_OnMouseLeave
function set_ExtCtrls_TBoundLabel_OnMouseLeave(p:TBoundLabel;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseLeave:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TBoundLabel_OnMouseMove
function set_ExtCtrls_TBoundLabel_OnMouseMove(p:TBoundLabel;newMethod:Controls_TMouseMoveEvent;OldEvent:ControlsTMouseMoveEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseMoveEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseMoveEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseMove:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TBoundLabel_OnMouseUp
function set_ExtCtrls_TBoundLabel_OnMouseUp(p:TBoundLabel;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseUp:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TBoundLabel_OnStartDrag
function set_ExtCtrls_TBoundLabel_OnStartDrag(p:TBoundLabel;newMethod:Controls_TStartDragEvent;OldEvent:ControlsTStartDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTStartDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTStartDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnStartDrag:=@callClass.call;
Result:=callClass;
end;
//property getterExtCtrls_TCustomLabeledEdit_EditLabel
function get_ExtCtrls_TCustomLabeledEdit_EditLabel(p:TCustomLabeledEdit):tboundlabel;cdecl;
begin
Result:=tboundlabel(p.EditLabel);
end;
//property getterExtCtrls_TCustomLabeledEdit_LabelPosition
function get_ExtCtrls_TCustomLabeledEdit_LabelPosition(p:TCustomLabeledEdit):Integer;cdecl;
begin
Result:=Integer(p.LabelPosition);
end;
//property setterExtCtrls_TCustomLabeledEdit_LabelPosition
procedure set_ExtCtrls_TCustomLabeledEdit_LabelPosition(p:TCustomLabeledEdit;v:tlabelposition);cdecl; 
begin
p.LabelPosition:=(v);
end;
//property getterExtCtrls_TCustomLabeledEdit_LabelSpacing
function get_ExtCtrls_TCustomLabeledEdit_LabelSpacing(p:TCustomLabeledEdit):Integer;cdecl;
begin
Result:=Integer(p.LabelSpacing);
end;
//property setterExtCtrls_TCustomLabeledEdit_LabelSpacing
procedure set_ExtCtrls_TCustomLabeledEdit_LabelSpacing(p:TCustomLabeledEdit;v:Integer);cdecl; 
begin
p.LabelSpacing:=(v);
end;
//property getterExtCtrls_TLabeledEdit_AutoSelect
function get_ExtCtrls_TLabeledEdit_AutoSelect(p:TLabeledEdit):Integer;cdecl;
begin
Result:=BooleanTointegert(p.AutoSelect);
end;
//property setterExtCtrls_TLabeledEdit_AutoSelect
procedure set_ExtCtrls_TLabeledEdit_AutoSelect(p:TLabeledEdit;v:Integer);cdecl; 
begin
p.AutoSelect:=integertToBoolean(v);
end;
//property getterExtCtrls_TLabeledEdit_DragMode
function get_ExtCtrls_TLabeledEdit_DragMode(p:TLabeledEdit):Integer;cdecl;
begin
Result:=Integer(p.DragMode);
end;
//property setterExtCtrls_TLabeledEdit_DragMode
procedure set_ExtCtrls_TLabeledEdit_DragMode(p:TLabeledEdit;v:tdragmode);cdecl; 
begin
p.DragMode:=(v);
end;
//property getterExtCtrls_TLabeledEdit_ParentColor
function get_ExtCtrls_TLabeledEdit_ParentColor(p:TLabeledEdit):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentColor);
end;
//property setterExtCtrls_TLabeledEdit_ParentColor
procedure set_ExtCtrls_TLabeledEdit_ParentColor(p:TLabeledEdit;v:Integer);cdecl; 
begin
p.ParentColor:=integertToBoolean(v);
end;
//property getterExtCtrls_TLabeledEdit_ParentFont
function get_ExtCtrls_TLabeledEdit_ParentFont(p:TLabeledEdit):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentFont);
end;
//property setterExtCtrls_TLabeledEdit_ParentFont
procedure set_ExtCtrls_TLabeledEdit_ParentFont(p:TLabeledEdit;v:Integer);cdecl; 
begin
p.ParentFont:=integertToBoolean(v);
end;
//property getterExtCtrls_TLabeledEdit_ParentShowHint
function get_ExtCtrls_TLabeledEdit_ParentShowHint(p:TLabeledEdit):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentShowHint);
end;
//property setterExtCtrls_TLabeledEdit_ParentShowHint
procedure set_ExtCtrls_TLabeledEdit_ParentShowHint(p:TLabeledEdit;v:Integer);cdecl; 
begin
p.ParentShowHint:=integertToBoolean(v);
end;
//property setterExtCtrls_TLabeledEdit_OnDblClick
function set_ExtCtrls_TLabeledEdit_OnDblClick(p:TLabeledEdit;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDblClick:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TLabeledEdit_OnDragDrop
function set_ExtCtrls_TLabeledEdit_OnDragDrop(p:TLabeledEdit;newMethod:Controls_TDragDropEvent;OldEvent:ControlsTDragDropEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragDropEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragDropEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragDrop:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TLabeledEdit_OnDragOver
function set_ExtCtrls_TLabeledEdit_OnDragOver(p:TLabeledEdit;newMethod:Controls_TDragOverEvent;OldEvent:ControlsTDragOverEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragOverEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragOverEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragOver:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TLabeledEdit_OnEditingDone
function set_ExtCtrls_TLabeledEdit_OnEditingDone(p:TLabeledEdit;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEditingDone:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TLabeledEdit_OnEndDrag
function set_ExtCtrls_TLabeledEdit_OnEndDrag(p:TLabeledEdit;newMethod:Controls_TEndDragEvent;OldEvent:ControlsTEndDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTEndDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTEndDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEndDrag:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TLabeledEdit_OnMouseDown
function set_ExtCtrls_TLabeledEdit_OnMouseDown(p:TLabeledEdit;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseDown:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TLabeledEdit_OnMouseEnter
function set_ExtCtrls_TLabeledEdit_OnMouseEnter(p:TLabeledEdit;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseEnter:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TLabeledEdit_OnMouseLeave
function set_ExtCtrls_TLabeledEdit_OnMouseLeave(p:TLabeledEdit;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseLeave:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TLabeledEdit_OnMouseMove
function set_ExtCtrls_TLabeledEdit_OnMouseMove(p:TLabeledEdit;newMethod:Controls_TMouseMoveEvent;OldEvent:ControlsTMouseMoveEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseMoveEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseMoveEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseMove:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TLabeledEdit_OnMouseUp
function set_ExtCtrls_TLabeledEdit_OnMouseUp(p:TLabeledEdit;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseUp:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TLabeledEdit_OnStartDrag
function set_ExtCtrls_TLabeledEdit_OnStartDrag(p:TLabeledEdit;newMethod:Controls_TStartDragEvent;OldEvent:ControlsTStartDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTStartDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTStartDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnStartDrag:=@callClass.call;
Result:=callClass;
end;
//constructorExtCtrls_TLabeledEdit_Create
function ExtCtrls_TLabeledEdit_Create(TheOwner:tcomponent):TLabeledEdit;cdecl;
begin
Result:=TLabeledEdit.Create((TheOwner));
end;
//constructorMaskEdit_TCustomMaskEdit_Create
function MaskEdit_TCustomMaskEdit_Create(TheOwner:tcomponent):TCustomMaskEdit;cdecl;
begin
Result:=TCustomMaskEdit.Create((TheOwner));
end;
//property getterMaskEdit_TCustomMaskEdit_Modified
function get_MaskEdit_TCustomMaskEdit_Modified(p:TCustomMaskEdit):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Modified);
end;
//property setterMaskEdit_TCustomMaskEdit_Modified
procedure set_MaskEdit_TCustomMaskEdit_Modified(p:TCustomMaskEdit;v:Integer);cdecl; 
begin
p.Modified:=integertToBoolean(v);
end;
//property getterMaskEdit_TMaskEdit_IsMasked
function get_MaskEdit_TMaskEdit_IsMasked(p:TMaskEdit):Integer;cdecl;
begin
Result:=BooleanTointegert(p.IsMasked);
end;
//property getterMaskEdit_TMaskEdit_EditText
function get_MaskEdit_TMaskEdit_EditText(p:TMaskEdit):PChar;cdecl;
begin
Result:=PChar(p.EditText);
end;
//property setterMaskEdit_TMaskEdit_EditText
procedure set_MaskEdit_TMaskEdit_EditText(p:TMaskEdit;v:PChar);cdecl; 
begin
p.EditText:=(v);
end;
//property getterMaskEdit_TMaskEdit_AutoSelect
function get_MaskEdit_TMaskEdit_AutoSelect(p:TMaskEdit):Integer;cdecl;
begin
Result:=BooleanTointegert(p.AutoSelect);
end;
//property setterMaskEdit_TMaskEdit_AutoSelect
procedure set_MaskEdit_TMaskEdit_AutoSelect(p:TMaskEdit;v:Integer);cdecl; 
begin
p.AutoSelect:=integertToBoolean(v);
end;
//property getterMaskEdit_TMaskEdit_CharCase
function get_MaskEdit_TMaskEdit_CharCase(p:TMaskEdit):Integer;cdecl;
begin
Result:=Integer(p.CharCase);
end;
//property setterMaskEdit_TMaskEdit_CharCase
procedure set_MaskEdit_TMaskEdit_CharCase(p:TMaskEdit;v:teditcharcase);cdecl; 
begin
p.CharCase:=(v);
end;
//property getterMaskEdit_TMaskEdit_DragKind
function get_MaskEdit_TMaskEdit_DragKind(p:TMaskEdit):Integer;cdecl;
begin
Result:=Integer(p.DragKind);
end;
//property setterMaskEdit_TMaskEdit_DragKind
procedure set_MaskEdit_TMaskEdit_DragKind(p:TMaskEdit;v:tdragkind);cdecl; 
begin
p.DragKind:=(v);
end;
//property getterMaskEdit_TMaskEdit_DragMode
function get_MaskEdit_TMaskEdit_DragMode(p:TMaskEdit):Integer;cdecl;
begin
Result:=Integer(p.DragMode);
end;
//property setterMaskEdit_TMaskEdit_DragMode
procedure set_MaskEdit_TMaskEdit_DragMode(p:TMaskEdit;v:tdragmode);cdecl; 
begin
p.DragMode:=(v);
end;
//property getterMaskEdit_TMaskEdit_MaxLength
function get_MaskEdit_TMaskEdit_MaxLength(p:TMaskEdit):Integer;cdecl;
begin
Result:=Integer(p.MaxLength);
end;
//property setterMaskEdit_TMaskEdit_MaxLength
procedure set_MaskEdit_TMaskEdit_MaxLength(p:TMaskEdit;v:Integer);cdecl; 
begin
p.MaxLength:=(v);
end;
//property getterMaskEdit_TMaskEdit_ParentColor
function get_MaskEdit_TMaskEdit_ParentColor(p:TMaskEdit):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentColor);
end;
//property setterMaskEdit_TMaskEdit_ParentColor
procedure set_MaskEdit_TMaskEdit_ParentColor(p:TMaskEdit;v:Integer);cdecl; 
begin
p.ParentColor:=integertToBoolean(v);
end;
//property getterMaskEdit_TMaskEdit_ParentFont
function get_MaskEdit_TMaskEdit_ParentFont(p:TMaskEdit):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentFont);
end;
//property setterMaskEdit_TMaskEdit_ParentFont
procedure set_MaskEdit_TMaskEdit_ParentFont(p:TMaskEdit;v:Integer);cdecl; 
begin
p.ParentFont:=integertToBoolean(v);
end;
//property getterMaskEdit_TMaskEdit_ParentShowHint
function get_MaskEdit_TMaskEdit_ParentShowHint(p:TMaskEdit):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentShowHint);
end;
//property setterMaskEdit_TMaskEdit_ParentShowHint
procedure set_MaskEdit_TMaskEdit_ParentShowHint(p:TMaskEdit;v:Integer);cdecl; 
begin
p.ParentShowHint:=integertToBoolean(v);
end;
//property setterMaskEdit_TMaskEdit_OnDblClick
function set_MaskEdit_TMaskEdit_OnDblClick(p:TMaskEdit;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDblClick:=@callClass.call;
Result:=callClass;
end;
//property setterMaskEdit_TMaskEdit_OnDragDrop
function set_MaskEdit_TMaskEdit_OnDragDrop(p:TMaskEdit;newMethod:Controls_TDragDropEvent;OldEvent:ControlsTDragDropEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragDropEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragDropEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragDrop:=@callClass.call;
Result:=callClass;
end;
//property setterMaskEdit_TMaskEdit_OnDragOver
function set_MaskEdit_TMaskEdit_OnDragOver(p:TMaskEdit;newMethod:Controls_TDragOverEvent;OldEvent:ControlsTDragOverEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragOverEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragOverEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragOver:=@callClass.call;
Result:=callClass;
end;
//property setterMaskEdit_TMaskEdit_OnEditingDone
function set_MaskEdit_TMaskEdit_OnEditingDone(p:TMaskEdit;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEditingDone:=@callClass.call;
Result:=callClass;
end;
//property setterMaskEdit_TMaskEdit_OnEndDock
function set_MaskEdit_TMaskEdit_OnEndDock(p:TMaskEdit;newMethod:Controls_TEndDragEvent;OldEvent:ControlsTEndDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTEndDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTEndDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEndDock:=@callClass.call;
Result:=callClass;
end;
//property setterMaskEdit_TMaskEdit_OnEndDrag
function set_MaskEdit_TMaskEdit_OnEndDrag(p:TMaskEdit;newMethod:Controls_TEndDragEvent;OldEvent:ControlsTEndDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTEndDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTEndDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEndDrag:=@callClass.call;
Result:=callClass;
end;
//property setterMaskEdit_TMaskEdit_OnMouseDown
function set_MaskEdit_TMaskEdit_OnMouseDown(p:TMaskEdit;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseDown:=@callClass.call;
Result:=callClass;
end;
//property setterMaskEdit_TMaskEdit_OnMouseEnter
function set_MaskEdit_TMaskEdit_OnMouseEnter(p:TMaskEdit;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseEnter:=@callClass.call;
Result:=callClass;
end;
//property setterMaskEdit_TMaskEdit_OnMouseLeave
function set_MaskEdit_TMaskEdit_OnMouseLeave(p:TMaskEdit;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseLeave:=@callClass.call;
Result:=callClass;
end;
//property setterMaskEdit_TMaskEdit_OnMouseMove
function set_MaskEdit_TMaskEdit_OnMouseMove(p:TMaskEdit;newMethod:Controls_TMouseMoveEvent;OldEvent:ControlsTMouseMoveEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseMoveEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseMoveEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseMove:=@callClass.call;
Result:=callClass;
end;
//property setterMaskEdit_TMaskEdit_OnMouseUp
function set_MaskEdit_TMaskEdit_OnMouseUp(p:TMaskEdit;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseUp:=@callClass.call;
Result:=callClass;
end;
//property setterMaskEdit_TMaskEdit_OnStartDock
function set_MaskEdit_TMaskEdit_OnStartDock(p:TMaskEdit;newMethod:Controls_TStartDockEvent;OldEvent:ControlsTStartDockEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTStartDockEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTStartDockEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnStartDock:=@callClass.call;
Result:=callClass;
end;
//property setterMaskEdit_TMaskEdit_OnStartDrag
function set_MaskEdit_TMaskEdit_OnStartDrag(p:TMaskEdit;newMethod:Controls_TStartDragEvent;OldEvent:ControlsTStartDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTStartDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTStartDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnStartDrag:=@callClass.call;
Result:=callClass;
end;
//property getterMaskEdit_TMaskEdit_EditMask
function get_MaskEdit_TMaskEdit_EditMask(p:TMaskEdit):PChar;cdecl;
begin
Result:=PChar(p.EditMask);
end;
//property setterMaskEdit_TMaskEdit_EditMask
procedure set_MaskEdit_TMaskEdit_EditMask(p:TMaskEdit;v:PChar);cdecl; 
begin
p.EditMask:=(v);
end;
//constructorMaskEdit_TMaskEdit_Create
function MaskEdit_TMaskEdit_Create(TheOwner:tcomponent):TMaskEdit;cdecl;
begin
Result:=TMaskEdit.Create((TheOwner));
end;
//constructorExtCtrls_TNotebook_Create
function ExtCtrls_TNotebook_Create(TheOwner:tcomponent):TNotebook;cdecl;
begin
Result:=TNotebook.Create((TheOwner));
end;
//property getterExtCtrls_TNotebook_ActivePage
function get_ExtCtrls_TNotebook_ActivePage(p:TNotebook):PChar;cdecl;
begin
Result:=PChar(p.ActivePage);
end;
//constructorExtCtrls_TPage_Create
function ExtCtrls_TPage_Create(TheOwner:tcomponent):TPage;cdecl;
begin
Result:=TPage.Create((TheOwner));
end;
//property getterExtCtrls_TPage_PageIndex
function get_ExtCtrls_TPage_PageIndex(p:TPage):Integer;cdecl;
begin
Result:=Integer(p.PageIndex);
end;
//property setterExtCtrls_TPage_OnMouseDown
function set_ExtCtrls_TPage_OnMouseDown(p:TPage;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseDown:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TPage_OnMouseEnter
function set_ExtCtrls_TPage_OnMouseEnter(p:TPage;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseEnter:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TPage_OnMouseLeave
function set_ExtCtrls_TPage_OnMouseLeave(p:TPage;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseLeave:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TPage_OnMouseMove
function set_ExtCtrls_TPage_OnMouseMove(p:TPage;newMethod:Controls_TMouseMoveEvent;OldEvent:ControlsTMouseMoveEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseMoveEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseMoveEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseMove:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TPage_OnMouseUp
function set_ExtCtrls_TPage_OnMouseUp(p:TPage;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseUp:=@callClass.call;
Result:=callClass;
end;
//property getterExtCtrls_TPage_ParentShowHint
function get_ExtCtrls_TPage_ParentShowHint(p:TPage):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentShowHint);
end;
//property setterExtCtrls_TPage_ParentShowHint
procedure set_ExtCtrls_TPage_ParentShowHint(p:TPage;v:Integer);cdecl; 
begin
p.ParentShowHint:=integertToBoolean(v);
end;
//property getterExtCtrls_TNotebook_ActivePageComponent
function get_ExtCtrls_TNotebook_ActivePageComponent(p:TNotebook):tpage;cdecl;
begin
Result:=tpage(p.ActivePageComponent);
end;
//property getterExtCtrls_TNotebook_Page
function get_ExtCtrls_TNotebook_Page(p:TNotebook;Index:Integer):tpage;cdecl;
begin
Result:=tpage(p.Page[Index]);
end;
//property getterExtCtrls_TNotebook_PageCount
function get_ExtCtrls_TNotebook_PageCount(p:TNotebook):Integer;cdecl;
begin
Result:=Integer(p.PageCount);
end;
//property getterExtCtrls_TNotebook_PageIndex
function get_ExtCtrls_TNotebook_PageIndex(p:TNotebook):Integer;cdecl;
begin
Result:=Integer(p.PageIndex);
end;
//property setterExtCtrls_TNotebook_PageIndex
procedure set_ExtCtrls_TNotebook_PageIndex(p:TNotebook;v:Integer);cdecl; 
begin
p.PageIndex:=(v);
end;
//property getterExtCtrls_TNotebook_Pages
function get_ExtCtrls_TNotebook_Pages(p:TNotebook):tstrings;cdecl;
begin
Result:=tstrings(p.Pages);
end;
//property setterExtCtrls_TNotebook_Pages
procedure set_ExtCtrls_TNotebook_Pages(p:TNotebook;v:tstrings);cdecl; 
begin
p.Pages:=(v);
end;
//property getterExtCtrls_TNotebook_DragMode
function get_ExtCtrls_TNotebook_DragMode(p:TNotebook):Integer;cdecl;
begin
Result:=Integer(p.DragMode);
end;
//property setterExtCtrls_TNotebook_DragMode
procedure set_ExtCtrls_TNotebook_DragMode(p:TNotebook;v:tdragmode);cdecl; 
begin
p.DragMode:=(v);
end;
//property setterExtCtrls_TNotebook_OnDragDrop
function set_ExtCtrls_TNotebook_OnDragDrop(p:TNotebook;newMethod:Controls_TDragDropEvent;OldEvent:ControlsTDragDropEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragDropEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragDropEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragDrop:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TNotebook_OnDragOver
function set_ExtCtrls_TNotebook_OnDragOver(p:TNotebook;newMethod:Controls_TDragOverEvent;OldEvent:ControlsTDragOverEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragOverEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragOverEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragOver:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TNotebook_OnEndDrag
function set_ExtCtrls_TNotebook_OnEndDrag(p:TNotebook;newMethod:Controls_TEndDragEvent;OldEvent:ControlsTEndDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTEndDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTEndDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEndDrag:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TNotebook_OnMouseDown
function set_ExtCtrls_TNotebook_OnMouseDown(p:TNotebook;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseDown:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TNotebook_OnMouseEnter
function set_ExtCtrls_TNotebook_OnMouseEnter(p:TNotebook;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseEnter:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TNotebook_OnMouseLeave
function set_ExtCtrls_TNotebook_OnMouseLeave(p:TNotebook;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseLeave:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TNotebook_OnMouseMove
function set_ExtCtrls_TNotebook_OnMouseMove(p:TNotebook;newMethod:Controls_TMouseMoveEvent;OldEvent:ControlsTMouseMoveEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseMoveEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseMoveEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseMove:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TNotebook_OnMouseUp
function set_ExtCtrls_TNotebook_OnMouseUp(p:TNotebook;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseUp:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TNotebook_OnStartDrag
function set_ExtCtrls_TNotebook_OnStartDrag(p:TNotebook;newMethod:Controls_TStartDragEvent;OldEvent:ControlsTStartDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTStartDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTStartDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnStartDrag:=@callClass.call;
Result:=callClass;
end;
//constructorExtCtrls_TPaintBox_Create
function ExtCtrls_TPaintBox_Create(AOwner:tcomponent):TPaintBox;cdecl;
begin
Result:=TPaintBox.Create((AOwner));
end;
//property getterExtCtrls_TPaintBox_DragMode
function get_ExtCtrls_TPaintBox_DragMode(p:TPaintBox):Integer;cdecl;
begin
Result:=Integer(p.DragMode);
end;
//property setterExtCtrls_TPaintBox_DragMode
procedure set_ExtCtrls_TPaintBox_DragMode(p:TPaintBox;v:tdragmode);cdecl; 
begin
p.DragMode:=(v);
end;
//property getterExtCtrls_TPaintBox_ParentColor
function get_ExtCtrls_TPaintBox_ParentColor(p:TPaintBox):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentColor);
end;
//property setterExtCtrls_TPaintBox_ParentColor
procedure set_ExtCtrls_TPaintBox_ParentColor(p:TPaintBox;v:Integer);cdecl; 
begin
p.ParentColor:=integertToBoolean(v);
end;
//property getterExtCtrls_TPaintBox_ParentFont
function get_ExtCtrls_TPaintBox_ParentFont(p:TPaintBox):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentFont);
end;
//property setterExtCtrls_TPaintBox_ParentFont
procedure set_ExtCtrls_TPaintBox_ParentFont(p:TPaintBox;v:Integer);cdecl; 
begin
p.ParentFont:=integertToBoolean(v);
end;
//property getterExtCtrls_TPaintBox_ParentShowHint
function get_ExtCtrls_TPaintBox_ParentShowHint(p:TPaintBox):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentShowHint);
end;
//property setterExtCtrls_TPaintBox_ParentShowHint
procedure set_ExtCtrls_TPaintBox_ParentShowHint(p:TPaintBox;v:Integer);cdecl; 
begin
p.ParentShowHint:=integertToBoolean(v);
end;
//property setterExtCtrls_TPaintBox_OnDblClick
function set_ExtCtrls_TPaintBox_OnDblClick(p:TPaintBox;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDblClick:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TPaintBox_OnDragDrop
function set_ExtCtrls_TPaintBox_OnDragDrop(p:TPaintBox;newMethod:Controls_TDragDropEvent;OldEvent:ControlsTDragDropEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragDropEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragDropEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragDrop:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TPaintBox_OnDragOver
function set_ExtCtrls_TPaintBox_OnDragOver(p:TPaintBox;newMethod:Controls_TDragOverEvent;OldEvent:ControlsTDragOverEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragOverEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragOverEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragOver:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TPaintBox_OnEndDrag
function set_ExtCtrls_TPaintBox_OnEndDrag(p:TPaintBox;newMethod:Controls_TEndDragEvent;OldEvent:ControlsTEndDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTEndDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTEndDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEndDrag:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TPaintBox_OnMouseDown
function set_ExtCtrls_TPaintBox_OnMouseDown(p:TPaintBox;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseDown:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TPaintBox_OnMouseEnter
function set_ExtCtrls_TPaintBox_OnMouseEnter(p:TPaintBox;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseEnter:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TPaintBox_OnMouseLeave
function set_ExtCtrls_TPaintBox_OnMouseLeave(p:TPaintBox;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseLeave:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TPaintBox_OnMouseMove
function set_ExtCtrls_TPaintBox_OnMouseMove(p:TPaintBox;newMethod:Controls_TMouseMoveEvent;OldEvent:ControlsTMouseMoveEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseMoveEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseMoveEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseMove:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TPaintBox_OnMouseUp
function set_ExtCtrls_TPaintBox_OnMouseUp(p:TPaintBox;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseUp:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TPaintBox_OnPaint
function set_ExtCtrls_TPaintBox_OnPaint(p:TPaintBox;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnPaint:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TPaintBox_OnStartDrag
function set_ExtCtrls_TPaintBox_OnStartDrag(p:TPaintBox;newMethod:Controls_TStartDragEvent;OldEvent:ControlsTStartDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTStartDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTStartDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnStartDrag:=@callClass.call;
Result:=callClass;
end;
//constructorPairSplitter_TCustomPairSplitter_Create
function PairSplitter_TCustomPairSplitter_Create(TheOwner:tcomponent):TCustomPairSplitter;cdecl;
begin
Result:=TCustomPairSplitter.Create((TheOwner));
end;
//constructorPairSplitter_TPairSplitterSide_Create
function PairSplitter_TPairSplitterSide_Create(TheOwner:tcomponent):TPairSplitterSide;cdecl;
begin
Result:=TPairSplitterSide.Create((TheOwner));
end;
//property getterPairSplitter_TPairSplitterSide_Splitter
function get_PairSplitter_TPairSplitterSide_Splitter(p:TPairSplitterSide):tcustompairsplitter;cdecl;
begin
Result:=tcustompairsplitter(p.Splitter);
end;
//property setterPairSplitter_TPairSplitterSide_OnMouseDown
function set_PairSplitter_TPairSplitterSide_OnMouseDown(p:TPairSplitterSide;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseDown:=@callClass.call;
Result:=callClass;
end;
//property setterPairSplitter_TPairSplitterSide_OnMouseEnter
function set_PairSplitter_TPairSplitterSide_OnMouseEnter(p:TPairSplitterSide;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseEnter:=@callClass.call;
Result:=callClass;
end;
//property setterPairSplitter_TPairSplitterSide_OnMouseLeave
function set_PairSplitter_TPairSplitterSide_OnMouseLeave(p:TPairSplitterSide;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseLeave:=@callClass.call;
Result:=callClass;
end;
//property setterPairSplitter_TPairSplitterSide_OnMouseMove
function set_PairSplitter_TPairSplitterSide_OnMouseMove(p:TPairSplitterSide;newMethod:Controls_TMouseMoveEvent;OldEvent:ControlsTMouseMoveEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseMoveEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseMoveEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseMove:=@callClass.call;
Result:=callClass;
end;
//property setterPairSplitter_TPairSplitterSide_OnMouseUp
function set_PairSplitter_TPairSplitterSide_OnMouseUp(p:TPairSplitterSide;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseUp:=@callClass.call;
Result:=callClass;
end;
//property getterPairSplitter_TPairSplitterSide_ParentShowHint
function get_PairSplitter_TPairSplitterSide_ParentShowHint(p:TPairSplitterSide):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentShowHint);
end;
//property setterPairSplitter_TPairSplitterSide_ParentShowHint
procedure set_PairSplitter_TPairSplitterSide_ParentShowHint(p:TPairSplitterSide;v:Integer);cdecl; 
begin
p.ParentShowHint:=integertToBoolean(v);
end;
//property getterPairSplitter_TCustomPairSplitter_Sides
function get_PairSplitter_TCustomPairSplitter_Sides(p:TCustomPairSplitter;Index:Integer):tpairsplitterside;cdecl;
begin
Result:=tpairsplitterside(p.Sides[Index]);
end;
//property getterPairSplitter_TCustomPairSplitter_SplitterType
function get_PairSplitter_TCustomPairSplitter_SplitterType(p:TCustomPairSplitter):Integer;cdecl;
begin
Result:=Integer(p.SplitterType);
end;
//property setterPairSplitter_TCustomPairSplitter_SplitterType
procedure set_PairSplitter_TCustomPairSplitter_SplitterType(p:TCustomPairSplitter;v:tpairsplittertype);cdecl; 
begin
p.SplitterType:=(v);
end;
//property getterPairSplitter_TCustomPairSplitter_Position
function get_PairSplitter_TCustomPairSplitter_Position(p:TCustomPairSplitter):Integer;cdecl;
begin
Result:=Integer(p.Position);
end;
//property setterPairSplitter_TCustomPairSplitter_Position
procedure set_PairSplitter_TCustomPairSplitter_Position(p:TCustomPairSplitter;v:Integer);cdecl; 
begin
p.Position:=(v);
end;
//property setterPairSplitter_TPairSplitter_OnMouseDown
function set_PairSplitter_TPairSplitter_OnMouseDown(p:TPairSplitter;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseDown:=@callClass.call;
Result:=callClass;
end;
//property setterPairSplitter_TPairSplitter_OnMouseEnter
function set_PairSplitter_TPairSplitter_OnMouseEnter(p:TPairSplitter;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseEnter:=@callClass.call;
Result:=callClass;
end;
//property setterPairSplitter_TPairSplitter_OnMouseLeave
function set_PairSplitter_TPairSplitter_OnMouseLeave(p:TPairSplitter;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseLeave:=@callClass.call;
Result:=callClass;
end;
//property setterPairSplitter_TPairSplitter_OnMouseMove
function set_PairSplitter_TPairSplitter_OnMouseMove(p:TPairSplitter;newMethod:Controls_TMouseMoveEvent;OldEvent:ControlsTMouseMoveEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseMoveEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseMoveEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseMove:=@callClass.call;
Result:=callClass;
end;
//property setterPairSplitter_TPairSplitter_OnMouseUp
function set_PairSplitter_TPairSplitter_OnMouseUp(p:TPairSplitter;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseUp:=@callClass.call;
Result:=callClass;
end;
//property getterPairSplitter_TPairSplitter_ParentShowHint
function get_PairSplitter_TPairSplitter_ParentShowHint(p:TPairSplitter):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentShowHint);
end;
//property setterPairSplitter_TPairSplitter_ParentShowHint
procedure set_PairSplitter_TPairSplitter_ParentShowHint(p:TPairSplitter;v:Integer);cdecl; 
begin
p.ParentShowHint:=integertToBoolean(v);
end;
//constructorPairSplitter_TPairSplitter_Create
function PairSplitter_TPairSplitter_Create(TheOwner:tcomponent):TPairSplitter;cdecl;
begin
Result:=TPairSplitter.Create((TheOwner));
end;
//constructorForms_TScrollBox_Create
function Forms_TScrollBox_Create(AOwner:tcomponent):TScrollBox;cdecl;
begin
Result:=TScrollBox.Create((AOwner));
end;
//property getterForms_TScrollBox_AutoScroll
function get_Forms_TScrollBox_AutoScroll(p:TScrollBox):Integer;cdecl;
begin
Result:=BooleanTointegert(p.AutoScroll);
end;
//property setterForms_TScrollBox_AutoScroll
procedure set_Forms_TScrollBox_AutoScroll(p:TScrollBox;v:Integer);cdecl; 
begin
p.AutoScroll:=integertToBoolean(v);
end;
//property getterForms_TScrollBox_DragKind
function get_Forms_TScrollBox_DragKind(p:TScrollBox):Integer;cdecl;
begin
Result:=Integer(p.DragKind);
end;
//property setterForms_TScrollBox_DragKind
procedure set_Forms_TScrollBox_DragKind(p:TScrollBox;v:tdragkind);cdecl; 
begin
p.DragKind:=(v);
end;
//property getterForms_TScrollBox_DragMode
function get_Forms_TScrollBox_DragMode(p:TScrollBox):Integer;cdecl;
begin
Result:=Integer(p.DragMode);
end;
//property setterForms_TScrollBox_DragMode
procedure set_Forms_TScrollBox_DragMode(p:TScrollBox;v:tdragmode);cdecl; 
begin
p.DragMode:=(v);
end;
//property getterForms_TScrollBox_ParentColor
function get_Forms_TScrollBox_ParentColor(p:TScrollBox):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentColor);
end;
//property setterForms_TScrollBox_ParentColor
procedure set_Forms_TScrollBox_ParentColor(p:TScrollBox;v:Integer);cdecl; 
begin
p.ParentColor:=integertToBoolean(v);
end;
//property getterForms_TScrollBox_ParentFont
function get_Forms_TScrollBox_ParentFont(p:TScrollBox):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentFont);
end;
//property setterForms_TScrollBox_ParentFont
procedure set_Forms_TScrollBox_ParentFont(p:TScrollBox;v:Integer);cdecl; 
begin
p.ParentFont:=integertToBoolean(v);
end;
//property getterForms_TScrollBox_ParentShowHint
function get_Forms_TScrollBox_ParentShowHint(p:TScrollBox):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentShowHint);
end;
//property setterForms_TScrollBox_ParentShowHint
procedure set_Forms_TScrollBox_ParentShowHint(p:TScrollBox;v:Integer);cdecl; 
begin
p.ParentShowHint:=integertToBoolean(v);
end;
//property setterForms_TScrollBox_OnDblClick
function set_Forms_TScrollBox_OnDblClick(p:TScrollBox;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDblClick:=@callClass.call;
Result:=callClass;
end;
//property setterForms_TScrollBox_OnDragDrop
function set_Forms_TScrollBox_OnDragDrop(p:TScrollBox;newMethod:Controls_TDragDropEvent;OldEvent:ControlsTDragDropEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragDropEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragDropEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragDrop:=@callClass.call;
Result:=callClass;
end;
//property setterForms_TScrollBox_OnDragOver
function set_Forms_TScrollBox_OnDragOver(p:TScrollBox;newMethod:Controls_TDragOverEvent;OldEvent:ControlsTDragOverEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragOverEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragOverEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragOver:=@callClass.call;
Result:=callClass;
end;
//property setterForms_TScrollBox_OnEndDock
function set_Forms_TScrollBox_OnEndDock(p:TScrollBox;newMethod:Controls_TEndDragEvent;OldEvent:ControlsTEndDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTEndDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTEndDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEndDock:=@callClass.call;
Result:=callClass;
end;
//property setterForms_TScrollBox_OnEndDrag
function set_Forms_TScrollBox_OnEndDrag(p:TScrollBox;newMethod:Controls_TEndDragEvent;OldEvent:ControlsTEndDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTEndDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTEndDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEndDrag:=@callClass.call;
Result:=callClass;
end;
//property setterForms_TScrollBox_OnMouseDown
function set_Forms_TScrollBox_OnMouseDown(p:TScrollBox;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseDown:=@callClass.call;
Result:=callClass;
end;
//property setterForms_TScrollBox_OnMouseEnter
function set_Forms_TScrollBox_OnMouseEnter(p:TScrollBox;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseEnter:=@callClass.call;
Result:=callClass;
end;
//property setterForms_TScrollBox_OnMouseLeave
function set_Forms_TScrollBox_OnMouseLeave(p:TScrollBox;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseLeave:=@callClass.call;
Result:=callClass;
end;
//property setterForms_TScrollBox_OnMouseMove
function set_Forms_TScrollBox_OnMouseMove(p:TScrollBox;newMethod:Controls_TMouseMoveEvent;OldEvent:ControlsTMouseMoveEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseMoveEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseMoveEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseMove:=@callClass.call;
Result:=callClass;
end;
//property setterForms_TScrollBox_OnMouseUp
function set_Forms_TScrollBox_OnMouseUp(p:TScrollBox;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseUp:=@callClass.call;
Result:=callClass;
end;
//property setterForms_TScrollBox_OnStartDock
function set_Forms_TScrollBox_OnStartDock(p:TScrollBox;newMethod:Controls_TStartDockEvent;OldEvent:ControlsTStartDockEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTStartDockEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTStartDockEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnStartDock:=@callClass.call;
Result:=callClass;
end;
//property setterForms_TScrollBox_OnStartDrag
function set_Forms_TScrollBox_OnStartDrag(p:TScrollBox;newMethod:Controls_TStartDragEvent;OldEvent:ControlsTStartDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTStartDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTStartDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnStartDrag:=@callClass.call;
Result:=callClass;
end;
//constructorExtCtrls_TShape_Create
function ExtCtrls_TShape_Create(TheOwner:tcomponent):TShape;cdecl;
begin
Result:=TShape.Create((TheOwner));
end;
//property getterExtCtrls_TShape_Brush
function get_ExtCtrls_TShape_Brush(p:TShape):tbrush;cdecl;
begin
Result:=tbrush(p.Brush);
end;
//property setterExtCtrls_TShape_Brush
procedure set_ExtCtrls_TShape_Brush(p:TShape;v:tbrush);cdecl; 
begin
p.Brush:=(v);
end;
//property getterExtCtrls_TShape_DragKind
function get_ExtCtrls_TShape_DragKind(p:TShape):Integer;cdecl;
begin
Result:=Integer(p.DragKind);
end;
//property setterExtCtrls_TShape_DragKind
procedure set_ExtCtrls_TShape_DragKind(p:TShape;v:tdragkind);cdecl; 
begin
p.DragKind:=(v);
end;
//property getterExtCtrls_TShape_DragMode
function get_ExtCtrls_TShape_DragMode(p:TShape):Integer;cdecl;
begin
Result:=Integer(p.DragMode);
end;
//property setterExtCtrls_TShape_DragMode
procedure set_ExtCtrls_TShape_DragMode(p:TShape;v:tdragmode);cdecl; 
begin
p.DragMode:=(v);
end;
//property getterExtCtrls_TShape_ParentShowHint
function get_ExtCtrls_TShape_ParentShowHint(p:TShape):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentShowHint);
end;
//property setterExtCtrls_TShape_ParentShowHint
procedure set_ExtCtrls_TShape_ParentShowHint(p:TShape;v:Integer);cdecl; 
begin
p.ParentShowHint:=integertToBoolean(v);
end;
//property getterExtCtrls_TShape_Pen
function get_ExtCtrls_TShape_Pen(p:TShape):tpen;cdecl;
begin
Result:=tpen(p.Pen);
end;
//property setterExtCtrls_TShape_Pen
procedure set_ExtCtrls_TShape_Pen(p:TShape;v:tpen);cdecl; 
begin
p.Pen:=(v);
end;
//property setterExtCtrls_TShape_OnDragDrop
function set_ExtCtrls_TShape_OnDragDrop(p:TShape;newMethod:Controls_TDragDropEvent;OldEvent:ControlsTDragDropEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragDropEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragDropEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragDrop:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TShape_OnDragOver
function set_ExtCtrls_TShape_OnDragOver(p:TShape;newMethod:Controls_TDragOverEvent;OldEvent:ControlsTDragOverEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragOverEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragOverEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragOver:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TShape_OnEndDock
function set_ExtCtrls_TShape_OnEndDock(p:TShape;newMethod:Controls_TEndDragEvent;OldEvent:ControlsTEndDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTEndDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTEndDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEndDock:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TShape_OnEndDrag
function set_ExtCtrls_TShape_OnEndDrag(p:TShape;newMethod:Controls_TEndDragEvent;OldEvent:ControlsTEndDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTEndDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTEndDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEndDrag:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TShape_OnMouseDown
function set_ExtCtrls_TShape_OnMouseDown(p:TShape;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseDown:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TShape_OnMouseEnter
function set_ExtCtrls_TShape_OnMouseEnter(p:TShape;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseEnter:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TShape_OnMouseLeave
function set_ExtCtrls_TShape_OnMouseLeave(p:TShape;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseLeave:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TShape_OnMouseMove
function set_ExtCtrls_TShape_OnMouseMove(p:TShape;newMethod:Controls_TMouseMoveEvent;OldEvent:ControlsTMouseMoveEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseMoveEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseMoveEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseMove:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TShape_OnMouseUp
function set_ExtCtrls_TShape_OnMouseUp(p:TShape;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseUp:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TShape_OnPaint
function set_ExtCtrls_TShape_OnPaint(p:TShape;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnPaint:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TShape_OnStartDock
function set_ExtCtrls_TShape_OnStartDock(p:TShape;newMethod:Controls_TStartDockEvent;OldEvent:ControlsTStartDockEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTStartDockEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTStartDockEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnStartDock:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TShape_OnStartDrag
function set_ExtCtrls_TShape_OnStartDrag(p:TShape;newMethod:Controls_TStartDragEvent;OldEvent:ControlsTStartDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTStartDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTStartDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnStartDrag:=@callClass.call;
Result:=callClass;
end;
//property getterExtCtrls_TShape_Shape
function get_ExtCtrls_TShape_Shape(p:TShape):Integer;cdecl;
begin
Result:=Integer(p.Shape);
end;
//property setterExtCtrls_TShape_Shape
procedure set_ExtCtrls_TShape_Shape(p:TShape;v:tshapetype);cdecl; 
begin
p.Shape:=(v);
end;
//constructorButtons_TCustomSpeedButton_Create
function Buttons_TCustomSpeedButton_Create(AOwner:tcomponent):TCustomSpeedButton;cdecl;
begin
Result:=TCustomSpeedButton.Create((AOwner));
end;
//property getterButtons_TCustomSpeedButton_AllowAllUp
function get_Buttons_TCustomSpeedButton_AllowAllUp(p:TCustomSpeedButton):Integer;cdecl;
begin
Result:=BooleanTointegert(p.AllowAllUp);
end;
//property setterButtons_TCustomSpeedButton_AllowAllUp
procedure set_Buttons_TCustomSpeedButton_AllowAllUp(p:TCustomSpeedButton;v:Integer);cdecl; 
begin
p.AllowAllUp:=integertToBoolean(v);
end;
//property getterButtons_TCustomSpeedButton_Down
function get_Buttons_TCustomSpeedButton_Down(p:TCustomSpeedButton):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Down);
end;
//property setterButtons_TCustomSpeedButton_Down
procedure set_Buttons_TCustomSpeedButton_Down(p:TCustomSpeedButton;v:Integer);cdecl; 
begin
p.Down:=integertToBoolean(v);
end;
//property getterButtons_TCustomSpeedButton_Flat
function get_Buttons_TCustomSpeedButton_Flat(p:TCustomSpeedButton):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Flat);
end;
//property setterButtons_TCustomSpeedButton_Flat
procedure set_Buttons_TCustomSpeedButton_Flat(p:TCustomSpeedButton;v:Integer);cdecl; 
begin
p.Flat:=integertToBoolean(v);
end;
//property getterButtons_TCustomSpeedButton_Glyph
function get_Buttons_TCustomSpeedButton_Glyph(p:TCustomSpeedButton):tbitmap;cdecl;
begin
Result:=tbitmap(p.Glyph);
end;
//property setterButtons_TCustomSpeedButton_Glyph
procedure set_Buttons_TCustomSpeedButton_Glyph(p:TCustomSpeedButton;v:tbitmap);cdecl; 
begin
p.Glyph:=(v);
end;
//property getterButtons_TCustomSpeedButton_GroupIndex
function get_Buttons_TCustomSpeedButton_GroupIndex(p:TCustomSpeedButton):Integer;cdecl;
begin
Result:=Integer(p.GroupIndex);
end;
//property setterButtons_TCustomSpeedButton_GroupIndex
procedure set_Buttons_TCustomSpeedButton_GroupIndex(p:TCustomSpeedButton;v:Integer);cdecl; 
begin
p.GroupIndex:=(v);
end;
//property getterButtons_TCustomSpeedButton_Layout
function get_Buttons_TCustomSpeedButton_Layout(p:TCustomSpeedButton):Integer;cdecl;
begin
Result:=Integer(p.Layout);
end;
//property setterButtons_TCustomSpeedButton_Layout
procedure set_Buttons_TCustomSpeedButton_Layout(p:TCustomSpeedButton;v:tbuttonlayout);cdecl; 
begin
p.Layout:=(v);
end;
//property getterButtons_TCustomSpeedButton_Margin
function get_Buttons_TCustomSpeedButton_Margin(p:TCustomSpeedButton):Integer;cdecl;
begin
Result:=Integer(p.Margin);
end;
//property setterButtons_TCustomSpeedButton_Margin
procedure set_Buttons_TCustomSpeedButton_Margin(p:TCustomSpeedButton;v:Integer);cdecl; 
begin
p.Margin:=(v);
end;
//property getterButtons_TCustomSpeedButton_NumGlyphs
function get_Buttons_TCustomSpeedButton_NumGlyphs(p:TCustomSpeedButton):Integer;cdecl;
begin
Result:=Integer(p.NumGlyphs);
end;
//property setterButtons_TCustomSpeedButton_NumGlyphs
procedure set_Buttons_TCustomSpeedButton_NumGlyphs(p:TCustomSpeedButton;v:Integer);cdecl; 
begin
p.NumGlyphs:=(v);
end;
//property getterButtons_TCustomSpeedButton_ShowAccelChar
function get_Buttons_TCustomSpeedButton_ShowAccelChar(p:TCustomSpeedButton):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ShowAccelChar);
end;
//property setterButtons_TCustomSpeedButton_ShowAccelChar
procedure set_Buttons_TCustomSpeedButton_ShowAccelChar(p:TCustomSpeedButton;v:Integer);cdecl; 
begin
p.ShowAccelChar:=integertToBoolean(v);
end;
//property getterButtons_TCustomSpeedButton_ShowCaption
function get_Buttons_TCustomSpeedButton_ShowCaption(p:TCustomSpeedButton):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ShowCaption);
end;
//property setterButtons_TCustomSpeedButton_ShowCaption
procedure set_Buttons_TCustomSpeedButton_ShowCaption(p:TCustomSpeedButton;v:Integer);cdecl; 
begin
p.ShowCaption:=integertToBoolean(v);
end;
//property getterButtons_TCustomSpeedButton_Spacing
function get_Buttons_TCustomSpeedButton_Spacing(p:TCustomSpeedButton):Integer;cdecl;
begin
Result:=Integer(p.Spacing);
end;
//property setterButtons_TCustomSpeedButton_Spacing
procedure set_Buttons_TCustomSpeedButton_Spacing(p:TCustomSpeedButton;v:Integer);cdecl; 
begin
p.Spacing:=(v);
end;
//property getterButtons_TCustomSpeedButton_Transparent
function get_Buttons_TCustomSpeedButton_Transparent(p:TCustomSpeedButton):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Transparent);
end;
//property setterButtons_TCustomSpeedButton_Transparent
procedure set_Buttons_TCustomSpeedButton_Transparent(p:TCustomSpeedButton;v:Integer);cdecl; 
begin
p.Transparent:=integertToBoolean(v);
end;
//property setterButtons_TSpeedButton_OnDblClick
function set_Buttons_TSpeedButton_OnDblClick(p:TSpeedButton;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDblClick:=@callClass.call;
Result:=callClass;
end;
//property setterButtons_TSpeedButton_OnMouseDown
function set_Buttons_TSpeedButton_OnMouseDown(p:TSpeedButton;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseDown:=@callClass.call;
Result:=callClass;
end;
//property setterButtons_TSpeedButton_OnMouseEnter
function set_Buttons_TSpeedButton_OnMouseEnter(p:TSpeedButton;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseEnter:=@callClass.call;
Result:=callClass;
end;
//property setterButtons_TSpeedButton_OnMouseLeave
function set_Buttons_TSpeedButton_OnMouseLeave(p:TSpeedButton;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseLeave:=@callClass.call;
Result:=callClass;
end;
//property setterButtons_TSpeedButton_OnMouseMove
function set_Buttons_TSpeedButton_OnMouseMove(p:TSpeedButton;newMethod:Controls_TMouseMoveEvent;OldEvent:ControlsTMouseMoveEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseMoveEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseMoveEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseMove:=@callClass.call;
Result:=callClass;
end;
//property setterButtons_TSpeedButton_OnMouseUp
function set_Buttons_TSpeedButton_OnMouseUp(p:TSpeedButton;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseUp:=@callClass.call;
Result:=callClass;
end;
//property setterButtons_TSpeedButton_OnPaint
function set_Buttons_TSpeedButton_OnPaint(p:TSpeedButton;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnPaint:=@callClass.call;
Result:=callClass;
end;
//property getterButtons_TSpeedButton_ParentFont
function get_Buttons_TSpeedButton_ParentFont(p:TSpeedButton):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentFont);
end;
//property setterButtons_TSpeedButton_ParentFont
procedure set_Buttons_TSpeedButton_ParentFont(p:TSpeedButton;v:Integer);cdecl; 
begin
p.ParentFont:=integertToBoolean(v);
end;
//property getterButtons_TSpeedButton_ParentShowHint
function get_Buttons_TSpeedButton_ParentShowHint(p:TSpeedButton):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentShowHint);
end;
//property setterButtons_TSpeedButton_ParentShowHint
procedure set_Buttons_TSpeedButton_ParentShowHint(p:TSpeedButton;v:Integer);cdecl; 
begin
p.ParentShowHint:=integertToBoolean(v);
end;
//constructorButtons_TSpeedButton_Create
function Buttons_TSpeedButton_Create(AOwner:tcomponent):TSpeedButton;cdecl;
begin
Result:=TSpeedButton.Create((AOwner));
end;
//constructorExtCtrls_TCustomSplitter_Create
function ExtCtrls_TCustomSplitter_Create(TheOwner:tcomponent):TCustomSplitter;cdecl;
begin
Result:=TCustomSplitter.Create((TheOwner));
end;
//property getterExtCtrls_TCustomSplitter_ResizeControl
function get_ExtCtrls_TCustomSplitter_ResizeControl(p:TCustomSplitter):tcontrol;cdecl;
begin
Result:=tcontrol(p.ResizeControl);
end;
//property setterExtCtrls_TCustomSplitter_ResizeControl
procedure set_ExtCtrls_TCustomSplitter_ResizeControl(p:TCustomSplitter;v:tcontrol);cdecl; 
begin
p.ResizeControl:=(v);
end;
//property getterExtCtrls_TCustomSplitter_AutoSnap
function get_ExtCtrls_TCustomSplitter_AutoSnap(p:TCustomSplitter):Integer;cdecl;
begin
Result:=BooleanTointegert(p.AutoSnap);
end;
//property setterExtCtrls_TCustomSplitter_AutoSnap
procedure set_ExtCtrls_TCustomSplitter_AutoSnap(p:TCustomSplitter;v:Integer);cdecl; 
begin
p.AutoSnap:=integertToBoolean(v);
end;
//property getterExtCtrls_TCustomSplitter_Beveled
function get_ExtCtrls_TCustomSplitter_Beveled(p:TCustomSplitter):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Beveled);
end;
//property setterExtCtrls_TCustomSplitter_Beveled
procedure set_ExtCtrls_TCustomSplitter_Beveled(p:TCustomSplitter;v:Integer);cdecl; 
begin
p.Beveled:=integertToBoolean(v);
end;
//property getterExtCtrls_TCustomSplitter_MinSize
function get_ExtCtrls_TCustomSplitter_MinSize(p:TCustomSplitter):Integer;cdecl;
begin
Result:=Integer(p.MinSize);
end;
//property setterExtCtrls_TCustomSplitter_MinSize
procedure set_ExtCtrls_TCustomSplitter_MinSize(p:TCustomSplitter;v:Integer);cdecl; 
begin
p.MinSize:=(v);
end;
//property setterExtCtrls_TCustomSplitter_OnCanOffset
function set_ExtCtrls_TCustomSplitter_OnCanOffset(p:TCustomSplitter;newMethod:ExtCtrls_TCanOffsetEvent;OldEvent:ExtCtrlsTCanOffsetEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ExtCtrlsTCanOffsetEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ExtCtrlsTCanOffsetEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnCanOffset:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TCustomSplitter_OnCanResize
function set_ExtCtrls_TCustomSplitter_OnCanResize(p:TCustomSplitter;newMethod:ExtCtrls_TCanResizeEvent;OldEvent:ExtCtrlsTCanResizeEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ExtCtrlsTCanResizeEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ExtCtrlsTCanResizeEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnCanResize:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TCustomSplitter_OnMoved
function set_ExtCtrls_TCustomSplitter_OnMoved(p:TCustomSplitter;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMoved:=@callClass.call;
Result:=callClass;
end;
//property getterExtCtrls_TCustomSplitter_ResizeAnchor
function get_ExtCtrls_TCustomSplitter_ResizeAnchor(p:TCustomSplitter):Integer;cdecl;
begin
Result:=Integer(p.ResizeAnchor);
end;
//property setterExtCtrls_TCustomSplitter_ResizeAnchor
procedure set_ExtCtrls_TCustomSplitter_ResizeAnchor(p:TCustomSplitter;v:tanchorkind);cdecl; 
begin
p.ResizeAnchor:=(v);
end;
//property getterExtCtrls_TCustomSplitter_ResizeStyle
function get_ExtCtrls_TCustomSplitter_ResizeStyle(p:TCustomSplitter):Integer;cdecl;
begin
Result:=Integer(p.ResizeStyle);
end;
//property setterExtCtrls_TCustomSplitter_ResizeStyle
procedure set_ExtCtrls_TCustomSplitter_ResizeStyle(p:TCustomSplitter;v:tresizestyle);cdecl; 
begin
p.ResizeStyle:=(v);
end;
//property getterExtCtrls_TSplitter_ParentColor
function get_ExtCtrls_TSplitter_ParentColor(p:TSplitter):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentColor);
end;
//property setterExtCtrls_TSplitter_ParentColor
procedure set_ExtCtrls_TSplitter_ParentColor(p:TSplitter;v:Integer);cdecl; 
begin
p.ParentColor:=integertToBoolean(v);
end;
//property getterExtCtrls_TSplitter_ParentShowHint
function get_ExtCtrls_TSplitter_ParentShowHint(p:TSplitter):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentShowHint);
end;
//property setterExtCtrls_TSplitter_ParentShowHint
procedure set_ExtCtrls_TSplitter_ParentShowHint(p:TSplitter;v:Integer);cdecl; 
begin
p.ParentShowHint:=integertToBoolean(v);
end;
//constructorExtCtrls_TSplitter_Create
function ExtCtrls_TSplitter_Create(TheOwner:tcomponent):TSplitter;cdecl;
begin
Result:=TSplitter.Create((TheOwner));
end;
//constructorStdCtrls_TCustomStaticText_Create
function StdCtrls_TCustomStaticText_Create(AOwner:tcomponent):TCustomStaticText;cdecl;
begin
Result:=TCustomStaticText.Create((AOwner));
end;
//property getterStdCtrls_TCustomStaticText_Alignment
function get_StdCtrls_TCustomStaticText_Alignment(p:TCustomStaticText):Integer;cdecl;
begin
Result:=Integer(p.Alignment);
end;
//property setterStdCtrls_TCustomStaticText_Alignment
procedure set_StdCtrls_TCustomStaticText_Alignment(p:TCustomStaticText;v:talignment);cdecl; 
begin
p.Alignment:=(v);
end;
//property getterStdCtrls_TCustomStaticText_BorderStyle
function get_StdCtrls_TCustomStaticText_BorderStyle(p:TCustomStaticText):Integer;cdecl;
begin
Result:=Integer(p.BorderStyle);
end;
//property setterStdCtrls_TCustomStaticText_BorderStyle
procedure set_StdCtrls_TCustomStaticText_BorderStyle(p:TCustomStaticText;v:tstaticborderstyle);cdecl; 
begin
p.BorderStyle:=(v);
end;
//property getterStdCtrls_TCustomStaticText_FocusControl
function get_StdCtrls_TCustomStaticText_FocusControl(p:TCustomStaticText):twincontrol;cdecl;
begin
Result:=twincontrol(p.FocusControl);
end;
//property setterStdCtrls_TCustomStaticText_FocusControl
procedure set_StdCtrls_TCustomStaticText_FocusControl(p:TCustomStaticText;v:twincontrol);cdecl; 
begin
p.FocusControl:=(v);
end;
//property getterStdCtrls_TCustomStaticText_ShowAccelChar
function get_StdCtrls_TCustomStaticText_ShowAccelChar(p:TCustomStaticText):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ShowAccelChar);
end;
//property setterStdCtrls_TCustomStaticText_ShowAccelChar
procedure set_StdCtrls_TCustomStaticText_ShowAccelChar(p:TCustomStaticText;v:Integer);cdecl; 
begin
p.ShowAccelChar:=integertToBoolean(v);
end;
//property getterStdCtrls_TCustomStaticText_Transparent
function get_StdCtrls_TCustomStaticText_Transparent(p:TCustomStaticText):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Transparent);
end;
//property setterStdCtrls_TCustomStaticText_Transparent
procedure set_StdCtrls_TCustomStaticText_Transparent(p:TCustomStaticText;v:Integer);cdecl; 
begin
p.Transparent:=integertToBoolean(v);
end;
//property getterStdCtrls_TStaticText_DragKind
function get_StdCtrls_TStaticText_DragKind(p:TStaticText):Integer;cdecl;
begin
Result:=Integer(p.DragKind);
end;
//property setterStdCtrls_TStaticText_DragKind
procedure set_StdCtrls_TStaticText_DragKind(p:TStaticText;v:tdragkind);cdecl; 
begin
p.DragKind:=(v);
end;
//property getterStdCtrls_TStaticText_DragMode
function get_StdCtrls_TStaticText_DragMode(p:TStaticText):Integer;cdecl;
begin
Result:=Integer(p.DragMode);
end;
//property setterStdCtrls_TStaticText_DragMode
procedure set_StdCtrls_TStaticText_DragMode(p:TStaticText;v:tdragmode);cdecl; 
begin
p.DragMode:=(v);
end;
//property setterStdCtrls_TStaticText_OnDblClick
function set_StdCtrls_TStaticText_OnDblClick(p:TStaticText;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDblClick:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TStaticText_OnDragDrop
function set_StdCtrls_TStaticText_OnDragDrop(p:TStaticText;newMethod:Controls_TDragDropEvent;OldEvent:ControlsTDragDropEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragDropEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragDropEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragDrop:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TStaticText_OnDragOver
function set_StdCtrls_TStaticText_OnDragOver(p:TStaticText;newMethod:Controls_TDragOverEvent;OldEvent:ControlsTDragOverEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTDragOverEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTDragOverEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDragOver:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TStaticText_OnEndDrag
function set_StdCtrls_TStaticText_OnEndDrag(p:TStaticText;newMethod:Controls_TEndDragEvent;OldEvent:ControlsTEndDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTEndDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTEndDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEndDrag:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TStaticText_OnMouseDown
function set_StdCtrls_TStaticText_OnMouseDown(p:TStaticText;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseDown:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TStaticText_OnMouseEnter
function set_StdCtrls_TStaticText_OnMouseEnter(p:TStaticText;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseEnter:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TStaticText_OnMouseLeave
function set_StdCtrls_TStaticText_OnMouseLeave(p:TStaticText;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseLeave:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TStaticText_OnMouseMove
function set_StdCtrls_TStaticText_OnMouseMove(p:TStaticText;newMethod:Controls_TMouseMoveEvent;OldEvent:ControlsTMouseMoveEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseMoveEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseMoveEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseMove:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TStaticText_OnMouseUp
function set_StdCtrls_TStaticText_OnMouseUp(p:TStaticText;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseUp:=@callClass.call;
Result:=callClass;
end;
//property setterStdCtrls_TStaticText_OnStartDrag
function set_StdCtrls_TStaticText_OnStartDrag(p:TStaticText;newMethod:Controls_TStartDragEvent;OldEvent:ControlsTStartDragEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTStartDragEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTStartDragEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnStartDrag:=@callClass.call;
Result:=callClass;
end;
//property getterStdCtrls_TStaticText_ParentFont
function get_StdCtrls_TStaticText_ParentFont(p:TStaticText):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentFont);
end;
//property setterStdCtrls_TStaticText_ParentFont
procedure set_StdCtrls_TStaticText_ParentFont(p:TStaticText;v:Integer);cdecl; 
begin
p.ParentFont:=integertToBoolean(v);
end;
//property getterStdCtrls_TStaticText_ParentColor
function get_StdCtrls_TStaticText_ParentColor(p:TStaticText):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentColor);
end;
//property setterStdCtrls_TStaticText_ParentColor
procedure set_StdCtrls_TStaticText_ParentColor(p:TStaticText;v:Integer);cdecl; 
begin
p.ParentColor:=integertToBoolean(v);
end;
//property getterStdCtrls_TStaticText_ParentShowHint
function get_StdCtrls_TStaticText_ParentShowHint(p:TStaticText):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentShowHint);
end;
//property setterStdCtrls_TStaticText_ParentShowHint
procedure set_StdCtrls_TStaticText_ParentShowHint(p:TStaticText;v:Integer);cdecl; 
begin
p.ParentShowHint:=integertToBoolean(v);
end;
//constructorStdCtrls_TStaticText_Create
function StdCtrls_TStaticText_Create(AOwner:tcomponent):TStaticText;cdecl;
begin
Result:=TStaticText.Create((AOwner));
end;
//constructorGrids_TCustomStringGrid_Create
function Grids_TCustomStringGrid_Create(AOwner:tcomponent):TCustomStringGrid;cdecl;
begin
Result:=TCustomStringGrid.Create((AOwner));
end;
//property getterGrids_TCustomStringGrid_Cells
function get_Grids_TCustomStringGrid_Cells(p:TCustomStringGrid;ACol:Integer;ARow:Integer):PChar;cdecl;
begin
Result:=PChar(p.Cells[ACol,ARow]);
end;
//property setterGrids_TCustomStringGrid_Cells
procedure set_Grids_TCustomStringGrid_Cells(p:TCustomStringGrid;ACol:Integer;ARow:Integer;v:PChar);cdecl; 
begin
p.Cells[ACol,ARow]:=(v);
end;
//property getterGrids_TCustomStringGrid_Cols
function get_Grids_TCustomStringGrid_Cols(p:TCustomStringGrid;index:Integer):tstrings;cdecl;
begin
Result:=tstrings(p.Cols[index]);
end;
//property setterGrids_TCustomStringGrid_Cols
procedure set_Grids_TCustomStringGrid_Cols(p:TCustomStringGrid;index:Integer;v:tstrings);cdecl; 
begin
p.Cols[index]:=(v);
end;
//property getterGrids_TCustomStringGrid_ExtendedSelect
function get_Grids_TCustomStringGrid_ExtendedSelect(p:TCustomStringGrid):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ExtendedSelect);
end;
//property setterGrids_TCustomStringGrid_ExtendedSelect
procedure set_Grids_TCustomStringGrid_ExtendedSelect(p:TCustomStringGrid;v:Integer);cdecl; 
begin
p.ExtendedSelect:=integertToBoolean(v);
end;
//property getterGrids_TCustomStringGrid_Objects
function get_Grids_TCustomStringGrid_Objects(p:TCustomStringGrid;ACol:Integer;ARow:Integer):tobject;cdecl;
begin
Result:=tobject(p.Objects[ACol,ARow]);
end;
//property setterGrids_TCustomStringGrid_Objects
procedure set_Grids_TCustomStringGrid_Objects(p:TCustomStringGrid;ACol:Integer;ARow:Integer;v:tobject);cdecl; 
begin
p.Objects[ACol,ARow]:=(v);
end;
//property getterGrids_TCustomStringGrid_Rows
function get_Grids_TCustomStringGrid_Rows(p:TCustomStringGrid;index:Integer):tstrings;cdecl;
begin
Result:=tstrings(p.Rows[index]);
end;
//property setterGrids_TCustomStringGrid_Rows
procedure set_Grids_TCustomStringGrid_Rows(p:TCustomStringGrid;index:Integer;v:tstrings);cdecl; 
begin
p.Rows[index]:=(v);
end;
//property getterGrids_TStringGrid_Modified
function get_Grids_TStringGrid_Modified(p:TStringGrid):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Modified);
end;
//property setterGrids_TStringGrid_Modified
procedure set_Grids_TStringGrid_Modified(p:TStringGrid;v:Integer);cdecl; 
begin
p.Modified:=integertToBoolean(v);
end;
//property getterGrids_TStringGrid_InplaceEditor
function get_Grids_TStringGrid_InplaceEditor(p:TStringGrid):twincontrol;cdecl;
begin
Result:=twincontrol(p.InplaceEditor);
end;
//property getterGrids_TStringGrid_AutoEdit
function get_Grids_TStringGrid_AutoEdit(p:TStringGrid):Integer;cdecl;
begin
Result:=BooleanTointegert(p.AutoEdit);
end;
//property setterGrids_TStringGrid_AutoEdit
procedure set_Grids_TStringGrid_AutoEdit(p:TStringGrid;v:Integer);cdecl; 
begin
p.AutoEdit:=integertToBoolean(v);
end;
//property getterGrids_TStringGrid_CellHintPriority
function get_Grids_TStringGrid_CellHintPriority(p:TStringGrid):Integer;cdecl;
begin
Result:=Integer(p.CellHintPriority);
end;
//property setterGrids_TStringGrid_CellHintPriority
procedure set_Grids_TStringGrid_CellHintPriority(p:TStringGrid;v:tcellhintpriority);cdecl; 
begin
p.CellHintPriority:=(v);
end;
//property getterGrids_TStringGrid_ColumnClickSorts
function get_Grids_TStringGrid_ColumnClickSorts(p:TStringGrid):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ColumnClickSorts);
end;
//property setterGrids_TStringGrid_ColumnClickSorts
procedure set_Grids_TStringGrid_ColumnClickSorts(p:TStringGrid;v:Integer);cdecl; 
begin
p.ColumnClickSorts:=integertToBoolean(v);
end;
//property getterGrids_TStringGrid_DragKind
function get_Grids_TStringGrid_DragKind(p:TStringGrid):Integer;cdecl;
begin
Result:=Integer(p.DragKind);
end;
//property setterGrids_TStringGrid_DragKind
procedure set_Grids_TStringGrid_DragKind(p:TStringGrid;v:tdragkind);cdecl; 
begin
p.DragKind:=(v);
end;
//property getterGrids_TStringGrid_DragMode
function get_Grids_TStringGrid_DragMode(p:TStringGrid):Integer;cdecl;
begin
Result:=Integer(p.DragMode);
end;
//property setterGrids_TStringGrid_DragMode
procedure set_Grids_TStringGrid_DragMode(p:TStringGrid;v:tdragmode);cdecl; 
begin
p.DragMode:=(v);
end;
//property getterGrids_TStringGrid_HeaderHotZones
function get_Grids_TStringGrid_HeaderHotZones(p:TStringGrid):Integer;cdecl;
begin
Result:=Integer(p.HeaderHotZones);
end;
//property setterGrids_TStringGrid_HeaderHotZones
procedure set_Grids_TStringGrid_HeaderHotZones(p:TStringGrid;v:tgridzoneset);cdecl; 
begin
p.HeaderHotZones:=(v);
end;
//property getterGrids_TStringGrid_HeaderPushZones
function get_Grids_TStringGrid_HeaderPushZones(p:TStringGrid):Integer;cdecl;
begin
Result:=Integer(p.HeaderPushZones);
end;
//property setterGrids_TStringGrid_HeaderPushZones
procedure set_Grids_TStringGrid_HeaderPushZones(p:TStringGrid;v:tgridzoneset);cdecl; 
begin
p.HeaderPushZones:=(v);
end;
//property getterGrids_TStringGrid_MouseWheelOption
function get_Grids_TStringGrid_MouseWheelOption(p:TStringGrid):Integer;cdecl;
begin
Result:=Integer(p.MouseWheelOption);
end;
//property setterGrids_TStringGrid_MouseWheelOption
procedure set_Grids_TStringGrid_MouseWheelOption(p:TStringGrid;v:tmousewheeloption);cdecl; 
begin
p.MouseWheelOption:=(v);
end;
//property getterGrids_TStringGrid_ParentColor
function get_Grids_TStringGrid_ParentColor(p:TStringGrid):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentColor);
end;
//property setterGrids_TStringGrid_ParentColor
procedure set_Grids_TStringGrid_ParentColor(p:TStringGrid;v:Integer);cdecl; 
begin
p.ParentColor:=integertToBoolean(v);
end;
//property getterGrids_TStringGrid_ParentFont
function get_Grids_TStringGrid_ParentFont(p:TStringGrid):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentFont);
end;
//property setterGrids_TStringGrid_ParentFont
procedure set_Grids_TStringGrid_ParentFont(p:TStringGrid;v:Integer);cdecl; 
begin
p.ParentFont:=integertToBoolean(v);
end;
//property getterGrids_TStringGrid_RangeSelectMode
function get_Grids_TStringGrid_RangeSelectMode(p:TStringGrid):Integer;cdecl;
begin
Result:=Integer(p.RangeSelectMode);
end;
//property setterGrids_TStringGrid_RangeSelectMode
procedure set_Grids_TStringGrid_RangeSelectMode(p:TStringGrid;v:trangeselectmode);cdecl; 
begin
p.RangeSelectMode:=(v);
end;
//property getterGrids_TStringGrid_TitleFont
function get_Grids_TStringGrid_TitleFont(p:TStringGrid):tfont;cdecl;
begin
Result:=tfont(p.TitleFont);
end;
//property setterGrids_TStringGrid_TitleFont
procedure set_Grids_TStringGrid_TitleFont(p:TStringGrid;v:tfont);cdecl; 
begin
p.TitleFont:=(v);
end;
//property getterGrids_TStringGrid_TitleImageList
function get_Grids_TStringGrid_TitleImageList(p:TStringGrid):timagelist;cdecl;
begin
Result:=timagelist(p.TitleImageList);
end;
//property setterGrids_TStringGrid_TitleImageList
procedure set_Grids_TStringGrid_TitleImageList(p:TStringGrid;v:timagelist);cdecl; 
begin
p.TitleImageList:=(v);
end;
//property getterGrids_TStringGrid_TitleStyle
function get_Grids_TStringGrid_TitleStyle(p:TStringGrid):Integer;cdecl;
begin
Result:=Integer(p.TitleStyle);
end;
//property setterGrids_TStringGrid_TitleStyle
procedure set_Grids_TStringGrid_TitleStyle(p:TStringGrid;v:ttitlestyle);cdecl; 
begin
p.TitleStyle:=(v);
end;
//property setterGrids_TStringGrid_OnCellProcess
function set_Grids_TStringGrid_OnCellProcess(p:TStringGrid;newMethod:Grids_TCellProcessEvent;OldEvent:GridsTCellProcessEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:GridsTCellProcessEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=GridsTCellProcessEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnCellProcess:=@callClass.call;
Result:=callClass;
end;
//property setterGrids_TStringGrid_OnCheckboxToggled
function set_Grids_TStringGrid_OnCheckboxToggled(p:TStringGrid;newMethod:Grids_TToggledCheckboxEvent;OldEvent:GridsTToggledCheckboxEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:GridsTToggledCheckboxEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=GridsTToggledCheckboxEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnCheckboxToggled:=@callClass.call;
Result:=callClass;
end;
//property setterGrids_TStringGrid_OnEditingDone
function set_Grids_TStringGrid_OnEditingDone(p:TStringGrid;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEditingDone:=@callClass.call;
Result:=callClass;
end;
//property setterGrids_TStringGrid_OnGetCellHint
function set_Grids_TStringGrid_OnGetCellHint(p:TStringGrid;newMethod:Grids_TGetCellHintEvent;OldEvent:GridsTGetCellHintEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:GridsTGetCellHintEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=GridsTGetCellHintEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnGetCellHint:=@callClass.call;
Result:=callClass;
end;
//property setterGrids_TStringGrid_OnGetCheckboxState
function set_Grids_TStringGrid_OnGetCheckboxState(p:TStringGrid;newMethod:Grids_TGetCheckboxStateEvent;OldEvent:GridsTGetCheckboxStateEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:GridsTGetCheckboxStateEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=GridsTGetCheckboxStateEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnGetCheckboxState:=@callClass.call;
Result:=callClass;
end;
//property setterGrids_TStringGrid_OnSetCheckboxState
function set_Grids_TStringGrid_OnSetCheckboxState(p:TStringGrid;newMethod:Grids_TSetCheckboxStateEvent;OldEvent:GridsTSetCheckboxStateEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:GridsTSetCheckboxStateEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=GridsTSetCheckboxStateEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnSetCheckboxState:=@callClass.call;
Result:=callClass;
end;
//property setterGrids_TStringGrid_OnTopLeftChanged
function set_Grids_TStringGrid_OnTopLeftChanged(p:TStringGrid;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnTopLeftChanged:=@callClass.call;
Result:=callClass;
end;
//property setterGrids_TStringGrid_OnUserCheckboxBitmap
function set_Grids_TStringGrid_OnUserCheckboxBitmap(p:TStringGrid;newMethod:Grids_TUserCheckBoxBitmapEvent;OldEvent:GridsTUserCheckBoxBitmapEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:GridsTUserCheckBoxBitmapEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=GridsTUserCheckBoxBitmapEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnUserCheckboxBitmap:=@callClass.call;
Result:=callClass;
end;
//property setterGrids_TStringGrid_OnValidateEntry
function set_Grids_TStringGrid_OnValidateEntry(p:TStringGrid;newMethod:Grids_TValidateEntryEvent;OldEvent:GridsTValidateEntryEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:GridsTValidateEntryEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=GridsTValidateEntryEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnValidateEntry:=@callClass.call;
Result:=callClass;
end;
//constructorGrids_TStringGrid_Create
function Grids_TStringGrid_Create(AOwner:tcomponent):TStringGrid;cdecl;
begin
Result:=TStringGrid.Create((AOwner));
end;
//constructorExtCtrls_TCustomTrayIcon_Create
function ExtCtrls_TCustomTrayIcon_Create(TheOwner:tcomponent):TCustomTrayIcon;cdecl;
begin
Result:=TCustomTrayIcon.Create((TheOwner));
end;
//property getterExtCtrls_TCustomTrayIcon_Animate
function get_ExtCtrls_TCustomTrayIcon_Animate(p:TCustomTrayIcon):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Animate);
end;
//property setterExtCtrls_TCustomTrayIcon_Animate
procedure set_ExtCtrls_TCustomTrayIcon_Animate(p:TCustomTrayIcon;v:Integer);cdecl; 
begin
p.Animate:=integertToBoolean(v);
end;
//property getterExtCtrls_TCustomTrayIcon_BalloonFlags
function get_ExtCtrls_TCustomTrayIcon_BalloonFlags(p:TCustomTrayIcon):Integer;cdecl;
begin
Result:=Integer(p.BalloonFlags);
end;
//property setterExtCtrls_TCustomTrayIcon_BalloonFlags
procedure set_ExtCtrls_TCustomTrayIcon_BalloonFlags(p:TCustomTrayIcon;v:tballoonflags);cdecl; 
begin
p.BalloonFlags:=(v);
end;
//property getterExtCtrls_TCustomTrayIcon_BalloonHint
function get_ExtCtrls_TCustomTrayIcon_BalloonHint(p:TCustomTrayIcon):PChar;cdecl;
begin
Result:=PChar(p.BalloonHint);
end;
//property setterExtCtrls_TCustomTrayIcon_BalloonHint
procedure set_ExtCtrls_TCustomTrayIcon_BalloonHint(p:TCustomTrayIcon;v:PChar);cdecl; 
begin
p.BalloonHint:=(v);
end;
//property getterExtCtrls_TCustomTrayIcon_BalloonTimeout
function get_ExtCtrls_TCustomTrayIcon_BalloonTimeout(p:TCustomTrayIcon):Integer;cdecl;
begin
Result:=Integer(p.BalloonTimeout);
end;
//property setterExtCtrls_TCustomTrayIcon_BalloonTimeout
procedure set_ExtCtrls_TCustomTrayIcon_BalloonTimeout(p:TCustomTrayIcon;v:Integer);cdecl; 
begin
p.BalloonTimeout:=(v);
end;
//property getterExtCtrls_TCustomTrayIcon_BalloonTitle
function get_ExtCtrls_TCustomTrayIcon_BalloonTitle(p:TCustomTrayIcon):PChar;cdecl;
begin
Result:=PChar(p.BalloonTitle);
end;
//property setterExtCtrls_TCustomTrayIcon_BalloonTitle
procedure set_ExtCtrls_TCustomTrayIcon_BalloonTitle(p:TCustomTrayIcon;v:PChar);cdecl; 
begin
p.BalloonTitle:=(v);
end;
//property getterExtCtrls_TCustomTrayIcon_Canvas
function get_ExtCtrls_TCustomTrayIcon_Canvas(p:TCustomTrayIcon):tcanvas;cdecl;
begin
Result:=tcanvas(p.Canvas);
end;
//property getterExtCtrls_TCustomTrayIcon_PopUpMenu
function get_ExtCtrls_TCustomTrayIcon_PopUpMenu(p:TCustomTrayIcon):tpopupmenu;cdecl;
begin
Result:=tpopupmenu(p.PopUpMenu);
end;
//property setterExtCtrls_TCustomTrayIcon_PopUpMenu
procedure set_ExtCtrls_TCustomTrayIcon_PopUpMenu(p:TCustomTrayIcon;v:tpopupmenu);cdecl; 
begin
p.PopUpMenu:=(v);
end;
//property getterExtCtrls_TCustomTrayIcon_Icon
function get_ExtCtrls_TCustomTrayIcon_Icon(p:TCustomTrayIcon):ticon;cdecl;
begin
Result:=ticon(p.Icon);
end;
//property setterExtCtrls_TCustomTrayIcon_Icon
procedure set_ExtCtrls_TCustomTrayIcon_Icon(p:TCustomTrayIcon;v:ticon);cdecl; 
begin
p.Icon:=(v);
end;
//property getterExtCtrls_TCustomTrayIcon_Icons
function get_ExtCtrls_TCustomTrayIcon_Icons(p:TCustomTrayIcon):tcustomimagelist;cdecl;
begin
Result:=tcustomimagelist(p.Icons);
end;
//property setterExtCtrls_TCustomTrayIcon_Icons
procedure set_ExtCtrls_TCustomTrayIcon_Icons(p:TCustomTrayIcon;v:tcustomimagelist);cdecl; 
begin
p.Icons:=(v);
end;
//property getterExtCtrls_TCustomTrayIcon_Hint
function get_ExtCtrls_TCustomTrayIcon_Hint(p:TCustomTrayIcon):PChar;cdecl;
begin
Result:=PChar(p.Hint);
end;
//property setterExtCtrls_TCustomTrayIcon_Hint
procedure set_ExtCtrls_TCustomTrayIcon_Hint(p:TCustomTrayIcon;v:PChar);cdecl; 
begin
p.Hint:=(v);
end;
//property getterExtCtrls_TCustomTrayIcon_ShowIcon
function get_ExtCtrls_TCustomTrayIcon_ShowIcon(p:TCustomTrayIcon):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ShowIcon);
end;
//property setterExtCtrls_TCustomTrayIcon_ShowIcon
procedure set_ExtCtrls_TCustomTrayIcon_ShowIcon(p:TCustomTrayIcon;v:Integer);cdecl; 
begin
p.ShowIcon:=integertToBoolean(v);
end;
//property getterExtCtrls_TCustomTrayIcon_Visible
function get_ExtCtrls_TCustomTrayIcon_Visible(p:TCustomTrayIcon):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Visible);
end;
//property setterExtCtrls_TCustomTrayIcon_Visible
procedure set_ExtCtrls_TCustomTrayIcon_Visible(p:TCustomTrayIcon;v:Integer);cdecl; 
begin
p.Visible:=integertToBoolean(v);
end;
//property setterExtCtrls_TCustomTrayIcon_OnClick
function set_ExtCtrls_TCustomTrayIcon_OnClick(p:TCustomTrayIcon;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnClick:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TCustomTrayIcon_OnDblClick
function set_ExtCtrls_TCustomTrayIcon_OnDblClick(p:TCustomTrayIcon;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnDblClick:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TCustomTrayIcon_OnMouseDown
function set_ExtCtrls_TCustomTrayIcon_OnMouseDown(p:TCustomTrayIcon;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseDown:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TCustomTrayIcon_OnMouseUp
function set_ExtCtrls_TCustomTrayIcon_OnMouseUp(p:TCustomTrayIcon;newMethod:Controls_TMouseEvent;OldEvent:ControlsTMouseEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseUp:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TCustomTrayIcon_OnMouseMove
function set_ExtCtrls_TCustomTrayIcon_OnMouseMove(p:TCustomTrayIcon;newMethod:Controls_TMouseMoveEvent;OldEvent:ControlsTMouseMoveEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ControlsTMouseMoveEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ControlsTMouseMoveEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnMouseMove:=@callClass.call;
Result:=callClass;
end;
//property setterExtCtrls_TCustomTrayIcon_OnPaint
function set_ExtCtrls_TCustomTrayIcon_OnPaint(p:TCustomTrayIcon;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnPaint:=@callClass.call;
Result:=callClass;
end;
//constructorExtCtrls_TTrayIcon_Create
function ExtCtrls_TTrayIcon_Create(TheOwner:tcomponent):TTrayIcon;cdecl;
begin
Result:=TTrayIcon.Create((TheOwner));
end;
//constructorValEdit_TValueListEditor_Create
function ValEdit_TValueListEditor_Create(AOwner:tcomponent):TValueListEditor;cdecl;
begin
Result:=TValueListEditor.Create((AOwner));
end;
//property getterValEdit_TValueListEditor_Modified
function get_ValEdit_TValueListEditor_Modified(p:TValueListEditor):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Modified);
end;
//property setterValEdit_TValueListEditor_Modified
procedure set_ValEdit_TValueListEditor_Modified(p:TValueListEditor;v:Integer);cdecl; 
begin
p.Modified:=integertToBoolean(v);
end;
//property getterValEdit_TValueListEditor_Keys
function get_ValEdit_TValueListEditor_Keys(p:TValueListEditor;Index:Integer):PChar;cdecl;
begin
Result:=PChar(p.Keys[Index]);
end;
//property setterValEdit_TValueListEditor_Keys
procedure set_ValEdit_TValueListEditor_Keys(p:TValueListEditor;Index:Integer;v:PChar);cdecl; 
begin
p.Keys[Index]:=(v);
end;
//property getterValEdit_TItemProp_EditMask
function get_ValEdit_TItemProp_EditMask(p:TItemProp):PChar;cdecl;
begin
Result:=PChar(p.EditMask);
end;
//property setterValEdit_TItemProp_EditMask
procedure set_ValEdit_TItemProp_EditMask(p:TItemProp;v:PChar);cdecl; 
begin
p.EditMask:=(v);
end;
//property getterValEdit_TItemProp_EditStyle
function get_ValEdit_TItemProp_EditStyle(p:TItemProp):Integer;cdecl;
begin
Result:=Integer(p.EditStyle);
end;
//property setterValEdit_TItemProp_EditStyle
procedure set_ValEdit_TItemProp_EditStyle(p:TItemProp;v:teditstyle);cdecl; 
begin
p.EditStyle:=(v);
end;
//property getterValEdit_TItemProp_KeyDesc
function get_ValEdit_TItemProp_KeyDesc(p:TItemProp):PChar;cdecl;
begin
Result:=PChar(p.KeyDesc);
end;
//property setterValEdit_TItemProp_KeyDesc
procedure set_ValEdit_TItemProp_KeyDesc(p:TItemProp;v:PChar);cdecl; 
begin
p.KeyDesc:=(v);
end;
//property getterValEdit_TItemProp_PickList
function get_ValEdit_TItemProp_PickList(p:TItemProp):tstrings;cdecl;
begin
Result:=tstrings(p.PickList);
end;
//property setterValEdit_TItemProp_PickList
procedure set_ValEdit_TItemProp_PickList(p:TItemProp;v:tstrings);cdecl; 
begin
p.PickList:=(v);
end;
//property getterValEdit_TItemProp_MaxLength
function get_ValEdit_TItemProp_MaxLength(p:TItemProp):Integer;cdecl;
begin
Result:=Integer(p.MaxLength);
end;
//property setterValEdit_TItemProp_MaxLength
procedure set_ValEdit_TItemProp_MaxLength(p:TItemProp;v:Integer);cdecl; 
begin
p.MaxLength:=(v);
end;
//property getterValEdit_TItemProp_ReadOnly
function get_ValEdit_TItemProp_ReadOnly(p:TItemProp):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ReadOnly);
end;
//property setterValEdit_TItemProp_ReadOnly
procedure set_ValEdit_TItemProp_ReadOnly(p:TItemProp;v:Integer);cdecl; 
begin
p.ReadOnly:=integertToBoolean(v);
end;
//property getterValEdit_TValueListEditor_AutoEdit
function get_ValEdit_TValueListEditor_AutoEdit(p:TValueListEditor):Integer;cdecl;
begin
Result:=BooleanTointegert(p.AutoEdit);
end;
//property setterValEdit_TValueListEditor_AutoEdit
procedure set_ValEdit_TValueListEditor_AutoEdit(p:TValueListEditor;v:Integer);cdecl; 
begin
p.AutoEdit:=integertToBoolean(v);
end;
//property getterValEdit_TValueListEditor_DragKind
function get_ValEdit_TValueListEditor_DragKind(p:TValueListEditor):Integer;cdecl;
begin
Result:=Integer(p.DragKind);
end;
//property setterValEdit_TValueListEditor_DragKind
procedure set_ValEdit_TValueListEditor_DragKind(p:TValueListEditor;v:tdragkind);cdecl; 
begin
p.DragKind:=(v);
end;
//property getterValEdit_TValueListEditor_DragMode
function get_ValEdit_TValueListEditor_DragMode(p:TValueListEditor):Integer;cdecl;
begin
Result:=Integer(p.DragMode);
end;
//property setterValEdit_TValueListEditor_DragMode
procedure set_ValEdit_TValueListEditor_DragMode(p:TValueListEditor;v:tdragmode);cdecl; 
begin
p.DragMode:=(v);
end;
//property getterValEdit_TValueListEditor_HeaderHotZones
function get_ValEdit_TValueListEditor_HeaderHotZones(p:TValueListEditor):Integer;cdecl;
begin
Result:=Integer(p.HeaderHotZones);
end;
//property setterValEdit_TValueListEditor_HeaderHotZones
procedure set_ValEdit_TValueListEditor_HeaderHotZones(p:TValueListEditor;v:tgridzoneset);cdecl; 
begin
p.HeaderHotZones:=(v);
end;
//property getterValEdit_TValueListEditor_HeaderPushZones
function get_ValEdit_TValueListEditor_HeaderPushZones(p:TValueListEditor):Integer;cdecl;
begin
Result:=Integer(p.HeaderPushZones);
end;
//property setterValEdit_TValueListEditor_HeaderPushZones
procedure set_ValEdit_TValueListEditor_HeaderPushZones(p:TValueListEditor;v:tgridzoneset);cdecl; 
begin
p.HeaderPushZones:=(v);
end;
//property getterValEdit_TValueListEditor_MouseWheelOption
function get_ValEdit_TValueListEditor_MouseWheelOption(p:TValueListEditor):Integer;cdecl;
begin
Result:=Integer(p.MouseWheelOption);
end;
//property setterValEdit_TValueListEditor_MouseWheelOption
procedure set_ValEdit_TValueListEditor_MouseWheelOption(p:TValueListEditor;v:tmousewheeloption);cdecl; 
begin
p.MouseWheelOption:=(v);
end;
//property getterValEdit_TValueListEditor_ParentColor
function get_ValEdit_TValueListEditor_ParentColor(p:TValueListEditor):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentColor);
end;
//property setterValEdit_TValueListEditor_ParentColor
procedure set_ValEdit_TValueListEditor_ParentColor(p:TValueListEditor;v:Integer);cdecl; 
begin
p.ParentColor:=integertToBoolean(v);
end;
//property getterValEdit_TValueListEditor_ParentFont
function get_ValEdit_TValueListEditor_ParentFont(p:TValueListEditor):Integer;cdecl;
begin
Result:=BooleanTointegert(p.ParentFont);
end;
//property setterValEdit_TValueListEditor_ParentFont
procedure set_ValEdit_TValueListEditor_ParentFont(p:TValueListEditor;v:Integer);cdecl; 
begin
p.ParentFont:=integertToBoolean(v);
end;
//property getterValEdit_TValueListEditor_RowCount
function get_ValEdit_TValueListEditor_RowCount(p:TValueListEditor):Integer;cdecl;
begin
Result:=Integer(p.RowCount);
end;
//property setterValEdit_TValueListEditor_RowCount
procedure set_ValEdit_TValueListEditor_RowCount(p:TValueListEditor;v:Integer);cdecl; 
begin
p.RowCount:=(v);
end;
//property getterValEdit_TValueListEditor_TitleFont
function get_ValEdit_TValueListEditor_TitleFont(p:TValueListEditor):tfont;cdecl;
begin
Result:=tfont(p.TitleFont);
end;
//property setterValEdit_TValueListEditor_TitleFont
procedure set_ValEdit_TValueListEditor_TitleFont(p:TValueListEditor;v:tfont);cdecl; 
begin
p.TitleFont:=(v);
end;
//property getterValEdit_TValueListEditor_TitleImageList
function get_ValEdit_TValueListEditor_TitleImageList(p:TValueListEditor):timagelist;cdecl;
begin
Result:=timagelist(p.TitleImageList);
end;
//property setterValEdit_TValueListEditor_TitleImageList
procedure set_ValEdit_TValueListEditor_TitleImageList(p:TValueListEditor;v:timagelist);cdecl; 
begin
p.TitleImageList:=(v);
end;
//property getterValEdit_TValueListEditor_TitleStyle
function get_ValEdit_TValueListEditor_TitleStyle(p:TValueListEditor):Integer;cdecl;
begin
Result:=Integer(p.TitleStyle);
end;
//property setterValEdit_TValueListEditor_TitleStyle
procedure set_ValEdit_TValueListEditor_TitleStyle(p:TValueListEditor;v:ttitlestyle);cdecl; 
begin
p.TitleStyle:=(v);
end;
//property setterValEdit_TValueListEditor_OnCheckboxToggled
function set_ValEdit_TValueListEditor_OnCheckboxToggled(p:TValueListEditor;newMethod:Grids_TToggledCheckboxEvent;OldEvent:GridsTToggledCheckboxEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:GridsTToggledCheckboxEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=GridsTToggledCheckboxEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnCheckboxToggled:=@callClass.call;
Result:=callClass;
end;
//property setterValEdit_TValueListEditor_OnEditingDone
function set_ValEdit_TValueListEditor_OnEditingDone(p:TValueListEditor;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnEditingDone:=@callClass.call;
Result:=callClass;
end;
//property setterValEdit_TValueListEditor_OnTopLeftChanged
function set_ValEdit_TValueListEditor_OnTopLeftChanged(p:TValueListEditor;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnTopLeftChanged:=@callClass.call;
Result:=callClass;
end;
//property setterValEdit_TValueListEditor_OnUserCheckboxBitmap
function set_ValEdit_TValueListEditor_OnUserCheckboxBitmap(p:TValueListEditor;newMethod:Grids_TUserCheckBoxBitmapEvent;OldEvent:GridsTUserCheckBoxBitmapEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:GridsTUserCheckBoxBitmapEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=GridsTUserCheckBoxBitmapEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnUserCheckboxBitmap:=@callClass.call;
Result:=callClass;
end;
//property setterValEdit_TValueListEditor_OnValidateEntry
function set_ValEdit_TValueListEditor_OnValidateEntry(p:TValueListEditor;newMethod:Grids_TValidateEntryEvent;OldEvent:GridsTValidateEntryEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:GridsTValidateEntryEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=GridsTValidateEntryEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnValidateEntry:=@callClass.call;
Result:=callClass;
end;
//property getterValEdit_TValueListEditor_DisplayOptions
function get_ValEdit_TValueListEditor_DisplayOptions(p:TValueListEditor):Integer;cdecl;
begin
Result:=Integer(p.DisplayOptions);
end;
//property setterValEdit_TValueListEditor_DisplayOptions
procedure set_ValEdit_TValueListEditor_DisplayOptions(p:TValueListEditor;v:tdisplayoptions);cdecl; 
begin
p.DisplayOptions:=(v);
end;
//property getterValEdit_TValueListEditor_DropDownRows
function get_ValEdit_TValueListEditor_DropDownRows(p:TValueListEditor):Integer;cdecl;
begin
Result:=Integer(p.DropDownRows);
end;
//property setterValEdit_TValueListEditor_DropDownRows
procedure set_ValEdit_TValueListEditor_DropDownRows(p:TValueListEditor;v:Integer);cdecl; 
begin
p.DropDownRows:=(v);
end;
//property getterValEdit_TValueListEditor_KeyOptions
function get_ValEdit_TValueListEditor_KeyOptions(p:TValueListEditor):Integer;cdecl;
begin
Result:=Integer(p.KeyOptions);
end;
//property setterValEdit_TValueListEditor_KeyOptions
procedure set_ValEdit_TValueListEditor_KeyOptions(p:TValueListEditor;v:tkeyoptions);cdecl; 
begin
p.KeyOptions:=(v);
end;
//property getterValEdit_TValueListEditor_Options
function get_ValEdit_TValueListEditor_Options(p:TValueListEditor):Integer;cdecl;
begin
Result:=Integer(p.Options);
end;
//property setterValEdit_TValueListEditor_Options
procedure set_ValEdit_TValueListEditor_Options(p:TValueListEditor;v:tgridoptions);cdecl; 
begin
p.Options:=(v);
end;
//property getterClasses_TStringList_Sorted
function get_Classes_TStringList_Sorted(p:TStringList):Integer;cdecl;
begin
Result:=BooleanTointegert(p.Sorted);
end;
//property setterClasses_TStringList_Sorted
procedure set_Classes_TStringList_Sorted(p:TStringList;v:Integer);cdecl; 
begin
p.Sorted:=integertToBoolean(v);
end;
//property getterClasses_TStringList_CaseSensitive
function get_Classes_TStringList_CaseSensitive(p:TStringList):Integer;cdecl;
begin
Result:=BooleanTointegert(p.CaseSensitive);
end;
//property setterClasses_TStringList_CaseSensitive
procedure set_Classes_TStringList_CaseSensitive(p:TStringList;v:Integer);cdecl; 
begin
p.CaseSensitive:=integertToBoolean(v);
end;
//property setterClasses_TStringList_OnChange
function set_Classes_TStringList_OnChange(p:TStringList;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnChange:=@callClass.call;
Result:=callClass;
end;
//property setterClasses_TStringList_OnChanging
function set_Classes_TStringList_OnChanging(p:TStringList;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnChanging:=@callClass.call;
Result:=callClass;
end;
//property getterClasses_TStringList_OwnsObjects
function get_Classes_TStringList_OwnsObjects(p:TStringList):Integer;cdecl;
begin
Result:=BooleanTointegert(p.OwnsObjects);
end;
//property setterClasses_TStringList_OwnsObjects
procedure set_Classes_TStringList_OwnsObjects(p:TStringList;v:Integer);cdecl; 
begin
p.OwnsObjects:=integertToBoolean(v);
end;
//property getterClasses_TStringList_SortStyle
function get_Classes_TStringList_SortStyle(p:TStringList):Integer;cdecl;
begin
Result:=Integer(p.SortStyle);
end;
//property setterClasses_TStringList_SortStyle
procedure set_Classes_TStringList_SortStyle(p:TStringList;v:tstringssortstyle);cdecl; 
begin
p.SortStyle:=(v);
end;
//property getterValEdit_TValueListEditor_Strings
function get_ValEdit_TValueListEditor_Strings(p:TValueListEditor):tvalueliststrings;cdecl;
begin
Result:=tvalueliststrings(p.Strings);
end;
//property setterValEdit_TValueListEditor_Strings
procedure set_ValEdit_TValueListEditor_Strings(p:TValueListEditor;v:tvalueliststrings);cdecl; 
begin
p.Strings:=(v);
end;
//property getterValEdit_TValueListEditor_TitleCaptions
function get_ValEdit_TValueListEditor_TitleCaptions(p:TValueListEditor):tstrings;cdecl;
begin
Result:=tstrings(p.TitleCaptions);
end;
//property setterValEdit_TValueListEditor_TitleCaptions
procedure set_ValEdit_TValueListEditor_TitleCaptions(p:TValueListEditor;v:tstrings);cdecl; 
begin
p.TitleCaptions:=(v);
end;
//property setterValEdit_TValueListEditor_OnGetPickList
function set_ValEdit_TValueListEditor_OnGetPickList(p:TValueListEditor;newMethod:ValEdit_TGetPickListEvent;OldEvent:ValEditTGetPickListEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ValEditTGetPickListEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ValEditTGetPickListEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnGetPickList:=@callClass.call;
Result:=callClass;
end;
//property setterValEdit_TValueListEditor_OnStringsChange
function set_ValEdit_TValueListEditor_OnStringsChange(p:TValueListEditor;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnStringsChange:=@callClass.call;
Result:=callClass;
end;
//property setterValEdit_TValueListEditor_OnStringsChanging
function set_ValEdit_TValueListEditor_OnStringsChanging(p:TValueListEditor;newMethod:Classes_TNotifyEvent;OldEvent:ClassesTNotifyEvent_wrapper;FreeOldEvent:integer):pointer;cdecl; 
var callClass:ClassesTNotifyEvent_wrapper;
begin
if FreeOldEvent=1 then OldEvent.free;
callClass:=ClassesTNotifyEvent_wrapper.Create;
callClass.c:=newMethod;
p.OnStringsChanging:=@callClass.call;
Result:=callClass;
end;
procedure ClassesTNotifyEvent_wrapper.call(Sender:TObject);
begin
C(tobject(Sender));
end;
procedure ControlsTDragDropEvent_wrapper.call(Sender:TObject;Source:TObject;X:Integer;Y:Integer);
begin
C(tobject(Sender),tobject(Source),Integer(X),Integer(Y));
end;
procedure ControlsTDragOverEvent_wrapper.call(Sender:TObject;Source:TObject;X:Integer;Y:Integer;State:TDragState;var Accept:Boolean);
begin
C(tobject(Sender),tobject(Source),Integer(X),Integer(Y),Integer(State),BooleanTointegert(Accept));
end;
procedure ControlsTEndDragEvent_wrapper.call(Sender:TObject;Target:TObject;X:Integer;Y:Integer);
begin
C(tobject(Sender),tobject(Target),Integer(X),Integer(Y));
end;
procedure ControlsTMouseEvent_wrapper.call(Sender:TObject;Button:TMouseButton;Shift:TShiftState;X:Integer;Y:Integer);
begin
C(tobject(Sender),Integer(Button),Integer(Shift),Integer(X),Integer(Y));
end;
procedure ControlsTMouseMoveEvent_wrapper.call(Sender:TObject;Shift:TShiftState;X:Integer;Y:Integer);
begin
C(tobject(Sender),Integer(Shift),Integer(X),Integer(Y));
end;
procedure ControlsTStartDockEvent_wrapper.call(Sender:TObject;var DragObject:TDragDockObject);
begin
C(tobject(Sender),tdragdockobject(DragObject));
end;
procedure ControlsTStartDragEvent_wrapper.call(Sender:TObject;var DragObject:TDragObject);
begin
C(tobject(Sender),tdragobject(DragObject));
end;
procedure MenusTMenuMeasureItemEvent_wrapper.call(Sender:TObject;ACanvas:TCanvas;var AWidth:Integer;var AHeight:Integer);
begin
C(tobject(Sender),tcanvas(ACanvas),Integer(AWidth),Integer(AHeight));
end;
procedure MenusTMenuChangeEvent_wrapper.call(Sender:TObject;Source:TMenuItem;Rebuild:Boolean);
begin
C(tobject(Sender),tmenuitem(Source),BooleanTointegert(Rebuild));
end;
procedure ControlsTGetDockCaptionEvent_wrapper.call(Sender:TObject;AControl:TControl;var ACaption:string);
begin
C(tobject(Sender),tcontrol(AControl),PChar(ACaption));
end;
procedure ControlsTDockDropEvent_wrapper.call(Sender:TObject;Source:TDragDockObject;X:Integer;Y:Integer);
begin
C(tobject(Sender),tdragdockobject(Source),Integer(X),Integer(Y));
end;
procedure ControlsTDockOverEvent_wrapper.call(Sender:TObject;Source:TDragDockObject;X:Integer;Y:Integer;State:TDragState;var Accept:Boolean);
begin
C(tobject(Sender),tdragdockobject(Source),Integer(X),Integer(Y),Integer(State),BooleanTointegert(Accept));
end;
procedure FormsTCloseEvent_wrapper.call(Sender:TObject;var CloseAction:TCloseAction);
begin
C(tobject(Sender),Integer(CloseAction));
end;
procedure FormsTCloseQueryEvent_wrapper.call(Sender:TObject;var CanClose:Boolean);
begin
C(tobject(Sender),BooleanTointegert(CanClose));
end;
procedure FormsTModalDialogFinished_wrapper.call(Sender:TObject;AResult:Integer);
begin
C(tobject(Sender),Integer(AResult));
end;
procedure StdCtrlsTMeasureItemEvent_wrapper.call(Control:TWinControl;Index:Integer;var AHeight:Integer);
begin
C(twincontrol(Control),Integer(Index),Integer(AHeight));
end;
procedure StdCtrlsTSelectionChangeEvent_wrapper.call(Sender:TObject;User:Boolean);
begin
C(tobject(Sender),BooleanTointegert(User));
end;
procedure StdCtrlsTScrollEvent_wrapper.call(Sender:TObject;ScrollCode:TScrollCode;var ScrollPos:Integer);
begin
C(tobject(Sender),Integer(ScrollCode),Integer(ScrollPos));
end;
procedure FormsTIdleEvent_wrapper.call(Sender:TObject;var Done:Boolean);
begin
C(tobject(Sender),BooleanTointegert(Done));
end;
procedure FormsTQueryEndSessionEvent_wrapper.call(var Cancel:Boolean);
begin
C(BooleanTointegert(Cancel));
end;
procedure CheckLstTCheckListClicked_wrapper.call(Sender:TObject;Index:Integer);
begin
C(tobject(Sender),Integer(Index));
end;
procedure ExtCtrlsTBandDragEvent_wrapper.call(Sender:TObject;Control:TControl;var Drag:Boolean);
begin
C(tobject(Sender),tcontrol(Control),BooleanTointegert(Drag));
end;
procedure ExtCtrlsTCanResizeEvent_wrapper.call(Sender:TObject;var NewSize:Integer;var Accept:Boolean);
begin
C(tobject(Sender),Integer(NewSize),BooleanTointegert(Accept));
end;
procedure GridsTOnSelectEvent_wrapper.call(Sender:TObject;aCol:Integer;aRow:Integer);
begin
C(tobject(Sender),Integer(aCol),Integer(aRow));
end;
procedure GridsTToggledCheckboxEvent_wrapper.call(sender:TObject;aCol:Integer;aRow:Integer;aState:TCheckboxState);
begin
C(tobject(sender),Integer(aCol),Integer(aRow),Integer(aState));
end;
procedure GridsTOnCompareCells_wrapper.call(Sender:TObject;ACol:Integer;ARow:Integer;BCol:Integer;BRow:Integer;var Result:Integer);
begin
C(tobject(Sender),Integer(ACol),Integer(ARow),Integer(BCol),Integer(BRow),Integer(Result));
end;
procedure GridsTOnPrepareCanvasEvent_wrapper.call(sender:TObject;aCol:Integer;aRow:Integer;aState:TGridDrawState);
begin
C(tobject(sender),Integer(aCol),Integer(aRow),Integer(aState));
end;
procedure GridsTSelectEditorEvent_wrapper.call(Sender:TObject;aCol:Integer;aRow:Integer;var Editor:TWinControl);
begin
C(tobject(Sender),Integer(aCol),Integer(aRow),twincontrol(Editor));
end;
procedure GridsTUserCheckBoxBitmapEvent_wrapper.call(Sender:TObject;const aCol:Integer;const aRow:Integer;const CheckedState:TCheckboxState;var ABitmap:TBitmap);
begin
C(tobject(Sender),Integer(aCol),Integer(aRow),Integer(CheckedState),tbitmap(ABitmap));
end;
procedure GridsTValidateEntryEvent_wrapper.call(sender:TObject;aCol:Integer;aRow:Integer;const OldValue:string;var NewValue:string);
begin
C(tobject(sender),Integer(aCol),Integer(aRow),PChar(OldValue),PChar(NewValue));
end;
procedure GridsTGetCellHintEvent_wrapper.call(Sender:TObject;ACol:Integer;ARow:Integer;var HintText:string);
begin
C(tobject(Sender),Integer(ACol),Integer(ARow),PChar(HintText));
end;
procedure GridsTGetCheckboxStateEvent_wrapper.call(Sender:TObject;ACol:Integer;ARow:Integer;var Value:TCheckboxState);
begin
C(tobject(Sender),Integer(ACol),Integer(ARow),Integer(Value));
end;
procedure GridsTSetCheckboxStateEvent_wrapper.call(Sender:TObject;ACol:Integer;ARow:Integer;const Value:TCheckboxState);
begin
C(tobject(Sender),Integer(ACol),Integer(ARow),Integer(Value));
end;
procedure GridsTGridOperationEvent_wrapper.call(Sender:TObject;IsColumn:Boolean;sIndex:Integer;tIndex:Integer);
begin
C(tobject(Sender),BooleanTointegert(IsColumn),Integer(sIndex),Integer(tIndex));
end;
procedure GridsTGetEditEvent_wrapper.call(Sender:TObject;ACol:Integer;ARow:Integer;var Value:string);
begin
C(tobject(Sender),Integer(ACol),Integer(ARow),PChar(Value));
end;
procedure GridsTHdrEvent_wrapper.call(Sender:TObject;IsColumn:Boolean;Index:Integer);
begin
C(tobject(Sender),BooleanTointegert(IsColumn),Integer(Index));
end;
procedure GridsTHeaderSizingEvent_wrapper.call(sender:TObject;const IsColumn:Boolean;const aIndex:Integer;const aSize:Integer);
begin
C(tobject(sender),BooleanTointegert(IsColumn),Integer(aIndex),Integer(aSize));
end;
procedure GridsTOnSelectCellEvent_wrapper.call(Sender:TObject;aCol:Integer;aRow:Integer;var CanSelect:Boolean);
begin
C(tobject(Sender),Integer(aCol),Integer(aRow),BooleanTointegert(CanSelect));
end;
procedure GridsTSetEditEvent_wrapper.call(Sender:TObject;ACol:Integer;ARow:Integer;const Value:string);
begin
C(tobject(Sender),Integer(ACol),Integer(ARow),PChar(Value));
end;
procedure ExtCtrlsTCanOffsetEvent_wrapper.call(Sender:TObject;var NewOffset:Integer;var Accept:Boolean);
begin
C(tobject(Sender),Integer(NewOffset),BooleanTointegert(Accept));
end;
procedure GridsTCellProcessEvent_wrapper.call(Sender:TObject;aCol:Integer;aRow:Integer;processType:TCellProcessType;var aValue:string);
begin
C(tobject(Sender),Integer(aCol),Integer(aRow),Integer(processType),PChar(aValue));
end;
procedure ValEditTGetPickListEvent_wrapper.call(Sender:TObject;const KeyName:string;Values:TStrings);
begin
C(tobject(Sender),PChar(KeyName),tstrings(Values));
end;
exports
Forms_Application_Initialize,
Forms_Application_Run,
Forms_Application_CreateForm,
Forms_Application_CreateFormLFM
,get_Classes_TComponent_Components
,get_Classes_TComponent_ComponentCount
,get_Classes_TComponent_ComponentIndex
,set_Classes_TComponent_ComponentIndex
,get_Classes_TComponent_ComponentState
,get_Classes_TComponent_ComponentStyle
,get_Classes_TComponent_Owner
,LCLClasses_TLCLComponent_Create
,get_LCLClasses_TLCLComponent_LCLRefCount
,Classes_TBasicActionLink_Create
,Classes_TBasicAction_Create
,get_Classes_TBasicAction_ActionComponent
,set_Classes_TBasicAction_ActionComponent
,set_Classes_TBasicAction_OnExecute
,set_Classes_TBasicAction_OnUpdate
,get_Classes_TBasicActionLink_Action
,set_Classes_TBasicActionLink_Action
,set_Classes_TBasicActionLink_OnChange
,ActnList_TActionLink_Create
,Controls_TControlActionLink_Create
,get_Controls_TDragObject_AlwaysShowDragImages
,set_Controls_TDragObject_AlwaysShowDragImages
,get_Controls_TDragObject_AutoCreated
,get_Controls_TDragObject_AutoFree
,get_Controls_TDragObject_Control
,set_Controls_TDragObject_Control
,get_Controls_TDragObject_DragTarget
,set_Controls_TDragObject_DragTarget
,get_Controls_TDragObject_Dropped
,get_Controls_TDragDockObject_DropAlign
,set_Controls_TDragDockObject_DropAlign
,get_Controls_TDragDockObject_DropOnControl
,set_Controls_TDragDockObject_DropOnControl
,get_Controls_TDragDockObject_Floating
,set_Controls_TDragDockObject_Floating
,get_Controls_TDragDockObject_IncreaseDockArea
,get_Controls_TControl_AnchoredControls
,Controls_TControl_Create
,get_Controls_TControl_AccessibleDescription
,set_Controls_TControl_AccessibleDescription
,get_Controls_TControl_AccessibleValue
,set_Controls_TControl_AccessibleValue
,get_Controls_TControl_AccessibleRole
,set_Controls_TControl_AccessibleRole
,get_Controls_TControl_Action
,set_Controls_TControl_Action
,get_Controls_TControl_Align
,set_Controls_TControl_Align
,get_Controls_TControl_Anchors
,set_Controls_TControl_Anchors
,get_Controls_TAnchorSide_Owner
,get_Controls_TAnchorSide_Kind
,get_Controls_TAnchorSide_Control
,set_Controls_TAnchorSide_Control
,get_Controls_TAnchorSide_Side
,set_Controls_TAnchorSide_Side
,get_Controls_TControl_AutoSize
,set_Controls_TControl_AutoSize
,get_Controls_TControlBorderSpacing_Control
,get_Controls_TControlBorderSpacing_AroundLeft
,get_Controls_TControlBorderSpacing_AroundTop
,get_Controls_TControlBorderSpacing_AroundRight
,get_Controls_TControlBorderSpacing_AroundBottom
,get_Controls_TControlBorderSpacing_ControlLeft
,get_Controls_TControlBorderSpacing_ControlTop
,get_Controls_TControlBorderSpacing_ControlWidth
,get_Controls_TControlBorderSpacing_ControlHeight
,get_Controls_TControlBorderSpacing_ControlRight
,get_Controls_TControlBorderSpacing_ControlBottom
,set_Controls_TControlBorderSpacing_OnChange
,get_Controls_TControlBorderSpacing_InnerBorder
,set_Controls_TControlBorderSpacing_InnerBorder
,get_Controls_TControlBorderSpacing_CellAlignHorizontal
,set_Controls_TControlBorderSpacing_CellAlignHorizontal
,get_Controls_TControlBorderSpacing_CellAlignVertical
,set_Controls_TControlBorderSpacing_CellAlignVertical
,get_Controls_TControl_BorderSpacing
,set_Controls_TControl_BorderSpacing
,get_Controls_TControl_Caption
,set_Controls_TControl_Caption
,get_Controls_TControl_CaptureMouseButtons
,set_Controls_TControl_CaptureMouseButtons
,get_Controls_TControl_ClientHeight
,set_Controls_TControl_ClientHeight
,get_Controls_TControl_ClientWidth
,set_Controls_TControl_ClientWidth
,get_Controls_TSizeConstraints_MaxInterfaceHeight
,get_Controls_TSizeConstraints_MaxInterfaceWidth
,get_Controls_TSizeConstraints_MinInterfaceHeight
,get_Controls_TSizeConstraints_MinInterfaceWidth
,get_Controls_TSizeConstraints_Control
,get_Controls_TSizeConstraints_Options
,set_Controls_TSizeConstraints_Options
,set_Controls_TSizeConstraints_OnChange
,get_Controls_TControl_Constraints
,set_Controls_TControl_Constraints
,get_Controls_TControl_ControlState
,set_Controls_TControl_ControlState
,get_Controls_TControl_ControlStyle
,set_Controls_TControl_ControlStyle
,get_Controls_TControl_Enabled
,set_Controls_TControl_Enabled
,Graphics_TFont_Create
,get_Graphics_TFont_IsMonoSpace
,get_Graphics_TFont_CanUTF8
,get_Graphics_TFont_PixelsPerInch
,set_Graphics_TFont_PixelsPerInch
,get_Graphics_TFont_Height
,set_Graphics_TFont_Height
,get_Graphics_TFont_Name
,set_Graphics_TFont_Name
,get_Graphics_TFont_Orientation
,set_Graphics_TFont_Orientation
,get_Graphics_TFont_Pitch
,set_Graphics_TFont_Pitch
,get_Graphics_TFont_Quality
,set_Graphics_TFont_Quality
,get_Graphics_TFont_Size
,set_Graphics_TFont_Size
,get_Graphics_TFont_Style
,set_Graphics_TFont_Style
,get_Controls_TControl_Font
,set_Controls_TControl_Font
,get_Controls_TControl_IsControl
,set_Controls_TControl_IsControl
,get_Controls_TControl_MouseEntered
,set_Controls_TControl_OnChangeBounds
,set_Controls_TControl_OnClick
,set_Controls_TControl_OnResize
,get_Controls_TControl_Parent
,set_Controls_TControl_Parent
,Menus_TMenuActionLink_Create
,Menus_TMenuItem_Create
,get_Menus_TMenuItem_Count
,get_Menus_TMenuItem_Items
,get_Menus_TMenuItem_MenuIndex
,set_Menus_TMenuItem_MenuIndex
,get_Menus_TMenuItem_Menu
,get_Menus_TMenuItem_Parent
,get_Menus_TMenuItem_Action
,set_Menus_TMenuItem_Action
,get_Menus_TMenuItem_AutoCheck
,set_Menus_TMenuItem_AutoCheck
,get_Menus_TMenuItem_Checked
,set_Menus_TMenuItem_Checked
,get_Menus_TMenuItem_Default
,set_Menus_TMenuItem_Default
,get_Menus_TMenuItem_Enabled
,set_Menus_TMenuItem_Enabled
,Graphics_TGraphic_Create
,get_Graphics_TGraphic_Empty
,get_Graphics_TGraphic_Height
,set_Graphics_TGraphic_Height
,get_Graphics_TGraphic_Modified
,set_Graphics_TGraphic_Modified
,get_Graphics_TGraphic_MimeType
,set_Graphics_TGraphic_OnChange
,get_Graphics_TGraphic_PaletteModified
,set_Graphics_TGraphic_PaletteModified
,get_Graphics_TGraphic_Transparent
,set_Graphics_TGraphic_Transparent
,get_Graphics_TGraphic_Width
,set_Graphics_TGraphic_Width
,Graphics_TRasterImage_Create
,Graphics_TCanvas_Create
,get_Graphics_TCanvas_AntialiasingMode
,set_Graphics_TCanvas_AntialiasingMode
,get_Graphics_TCanvas_AutoRedraw
,set_Graphics_TCanvas_AutoRedraw
,Graphics_TBrush_Create
,get_Graphics_TBrush_Bitmap
,set_Graphics_TBrush_Bitmap
,get_Graphics_TCanvas_Brush
,set_Graphics_TCanvas_Brush
,get_Graphics_TCanvas_Font
,set_Graphics_TCanvas_Font
,get_Graphics_TCanvas_Height
,Graphics_TPen_Create
,get_Graphics_TPen_Cosmetic
,set_Graphics_TPen_Cosmetic
,get_Graphics_TPen_EndCap
,set_Graphics_TPen_EndCap
,get_Graphics_TPen_JoinStyle
,set_Graphics_TPen_JoinStyle
,get_Graphics_TCanvas_Pen
,set_Graphics_TCanvas_Pen
,set_Graphics_TGraphicsObject_OnChanging
,set_Graphics_TGraphicsObject_OnChange
,Graphics_TRegion_Create
,get_Graphics_TCanvas_Region
,set_Graphics_TCanvas_Region
,get_Graphics_TCanvas_Width
,set_Graphics_TCanvas_OnChange
,set_Graphics_TCanvas_OnChanging
,get_Graphics_TRasterImage_Canvas
,get_Graphics_TRasterImage_Masked
,set_Graphics_TRasterImage_Masked
,get_Graphics_TRasterImage_PixelFormat
,set_Graphics_TRasterImage_PixelFormat
,get_Graphics_TRasterImage_RawImage
,get_Graphics_TRasterImage_TransparentMode
,set_Graphics_TRasterImage_TransparentMode
,Graphics_TCustomBitmap_Create
,get_Graphics_TCustomBitmap_HandleType
,set_Graphics_TCustomBitmap_HandleType
,get_Graphics_TCustomBitmap_Monochrome
,set_Graphics_TCustomBitmap_Monochrome
,Graphics_TFPImageBitmap_Create
,Graphics_TBitmap_Create
,get_Menus_TMenuItem_Bitmap
,set_Menus_TMenuItem_Bitmap
,get_Menus_TMenuItem_GlyphShowMode
,set_Menus_TMenuItem_GlyphShowMode
,get_Menus_TMenuItem_RadioItem
,set_Menus_TMenuItem_RadioItem
,get_Menus_TMenuItem_RightJustify
,set_Menus_TMenuItem_RightJustify
,get_Menus_TMenuItem_ShowAlwaysCheckable
,set_Menus_TMenuItem_ShowAlwaysCheckable
,get_LCLClasses_TLCLReferenceComponent_HandleAllocated
,get_LCLClasses_TLCLReferenceComponent_ReferenceAllocated
,LCLClasses_TLCLReferenceComponent_Create
,ImgList_TCustomImageList_Create
,ImgList_TCustomImageList_CreateSize
,get_ImgList_TCustomImageList_HasOverlays
,get_ImgList_TCustomImageList_AllocBy
,set_ImgList_TCustomImageList_AllocBy
,get_ImgList_TCustomImageList_Count
,get_ImgList_TCustomImageList_DrawingStyle
,set_ImgList_TCustomImageList_DrawingStyle
,get_ImgList_TCustomImageList_Height
,set_ImgList_TCustomImageList_Height
,get_ImgList_TCustomImageList_Width
,set_ImgList_TCustomImageList_Width
,set_ImgList_TCustomImageList_OnChange
,get_ImgList_TCustomImageList_Masked
,set_ImgList_TCustomImageList_Masked
,get_ImgList_TCustomImageList_ShareImages
,set_ImgList_TCustomImageList_ShareImages
,get_ImgList_TCustomImageList_ImageType
,set_ImgList_TCustomImageList_ImageType
,get_Menus_TMenuItem_SubMenuImages
,set_Menus_TMenuItem_SubMenuImages
,get_Menus_TMenuItem_Visible
,set_Menus_TMenuItem_Visible
,set_Menus_TMenuItem_OnClick
,set_Menus_TMenuItem_OnMeasureItem
,Menus_TMenu_Create
,get_Menus_TMenu_Parent
,set_Menus_TMenu_Parent
,get_Menus_TMenu_ShortcutHandled
,set_Menus_TMenu_ShortcutHandled
,get_Menus_TMenu_BidiMode
,set_Menus_TMenu_BidiMode
,get_Menus_TMenu_ParentBidiMode
,set_Menus_TMenu_ParentBidiMode
,get_Menus_TMenu_Items
,get_Menus_TMenu_Images
,set_Menus_TMenu_Images
,get_Menus_TMenu_OwnerDraw
,set_Menus_TMenu_OwnerDraw
,set_Menus_TMenu_OnMeasureItem
,Menus_TPopupMenu_Create
,get_Menus_TPopupMenu_PopupComponent
,set_Menus_TPopupMenu_PopupComponent
,get_Menus_TPopupMenu_Alignment
,set_Menus_TPopupMenu_Alignment
,get_Menus_TPopupMenu_AutoPopup
,set_Menus_TPopupMenu_AutoPopup
,get_Menus_TPopupMenu_TrackButton
,set_Menus_TPopupMenu_TrackButton
,set_Menus_TPopupMenu_OnPopup
,set_Menus_TPopupMenu_OnClose
,get_Controls_TControl_PopupMenu
,set_Controls_TControl_PopupMenu
,get_Controls_TControl_ShowHint
,set_Controls_TControl_ShowHint
,get_Controls_TControl_Visible
,set_Controls_TControl_Visible
,get_Controls_TControl_DockOrientation
,set_Controls_TControl_DockOrientation
,get_Controls_TControl_Floating
,get_Controls_TControl_HostDockSite
,set_Controls_TControl_HostDockSite
,get_Controls_TControl_LRDockWidth
,set_Controls_TControl_LRDockWidth
,get_Controls_TControl_TBDockHeight
,set_Controls_TControl_TBDockHeight
,get_Controls_TControl_UndockHeight
,set_Controls_TControl_UndockHeight
,get_Controls_TControl_UndockWidth
,set_Controls_TControl_UndockWidth
,get_Controls_TControl_BiDiMode
,set_Controls_TControl_BiDiMode
,get_Controls_TControl_ParentBiDiMode
,set_Controls_TControl_ParentBiDiMode
,get_Controls_TControl_AnchorSideLeft
,set_Controls_TControl_AnchorSideLeft
,get_Controls_TControl_AnchorSideTop
,set_Controls_TControl_AnchorSideTop
,get_Controls_TControl_AnchorSideRight
,set_Controls_TControl_AnchorSideRight
,get_Controls_TControl_AnchorSideBottom
,set_Controls_TControl_AnchorSideBottom
,get_Controls_TControl_Left
,set_Controls_TControl_Left
,get_Controls_TControl_Height
,set_Controls_TControl_Height
,get_Controls_TControl_Top
,set_Controls_TControl_Top
,get_Controls_TControl_Width
,set_Controls_TControl_Width
,get_Controls_TControl_HelpType
,set_Controls_TControl_HelpType
,get_Controls_TControl_HelpKeyword
,set_Controls_TControl_HelpKeyword
,get_Controls_TWinControl_BoundsLockCount
,get_Controls_TWinControl_Brush
,get_Controls_TWinControl_CachedClientHeight
,get_Controls_TWinControl_CachedClientWidth
,get_Controls_TControlChildSizing_Control
,set_Controls_TControlChildSizing_OnChange
,get_Controls_TControlChildSizing_LeftRightSpacing
,set_Controls_TControlChildSizing_LeftRightSpacing
,get_Controls_TControlChildSizing_TopBottomSpacing
,set_Controls_TControlChildSizing_TopBottomSpacing
,get_Controls_TControlChildSizing_HorizontalSpacing
,set_Controls_TControlChildSizing_HorizontalSpacing
,get_Controls_TControlChildSizing_VerticalSpacing
,set_Controls_TControlChildSizing_VerticalSpacing
,get_Controls_TControlChildSizing_EnlargeHorizontal
,set_Controls_TControlChildSizing_EnlargeHorizontal
,get_Controls_TControlChildSizing_EnlargeVertical
,set_Controls_TControlChildSizing_EnlargeVertical
,get_Controls_TControlChildSizing_ShrinkHorizontal
,set_Controls_TControlChildSizing_ShrinkHorizontal
,get_Controls_TControlChildSizing_ShrinkVertical
,set_Controls_TControlChildSizing_ShrinkVertical
,get_Controls_TControlChildSizing_Layout
,set_Controls_TControlChildSizing_Layout
,get_Controls_TControlChildSizing_ControlsPerLine
,set_Controls_TControlChildSizing_ControlsPerLine
,get_Controls_TWinControl_ChildSizing
,set_Controls_TWinControl_ChildSizing
,get_Controls_TWinControl_ControlCount
,get_Controls_TWinControl_Controls
,get_Controls_TWinControl_DockClientCount
,get_Controls_TWinControl_DockClients
,get_Controls_TWinControl_DockManager
,set_Controls_TWinControl_DockManager
,get_Controls_TWinControl_DockSite
,set_Controls_TWinControl_DockSite
,get_Controls_TWinControl_DoubleBuffered
,set_Controls_TWinControl_DoubleBuffered
,get_Controls_TWinControl_IsResizing
,get_Controls_TWinControl_TabStop
,set_Controls_TWinControl_TabStop
,set_Controls_TWinControl_OnDockDrop
,set_Controls_TWinControl_OnDockOver
,set_Controls_TWinControl_OnEnter
,set_Controls_TWinControl_OnExit
,get_Controls_TWinControl_Showing
,get_Controls_TWinControl_UseDockManager
,set_Controls_TWinControl_UseDockManager
,get_Controls_TWinControl_DesignerDeleting
,set_Controls_TWinControl_DesignerDeleting
,get_Controls_TWinControl_VisibleDockClientCount
,Controls_TWinControl_Create
,Controls_TCustomControl_Create
,get_Controls_TCustomControl_Canvas
,set_Controls_TCustomControl_Canvas
,set_Controls_TCustomControl_OnPaint
,Forms_TScrollingWinControl_Create
,Forms_TControlScrollBar_Create
,get_Forms_TControlScrollBar_Kind
,get_Forms_TControlScrollBar_Size
,get_Forms_TControlScrollBar_Smooth
,set_Forms_TControlScrollBar_Smooth
,get_Forms_TControlScrollBar_Position
,set_Forms_TControlScrollBar_Position
,get_Forms_TControlScrollBar_Range
,set_Forms_TControlScrollBar_Range
,get_Forms_TControlScrollBar_Tracking
,set_Forms_TControlScrollBar_Tracking
,get_Forms_TControlScrollBar_Visible
,set_Forms_TControlScrollBar_Visible
,get_Forms_TScrollingWinControl_HorzScrollBar
,set_Forms_TScrollingWinControl_HorzScrollBar
,get_Forms_TScrollingWinControl_VertScrollBar
,set_Forms_TScrollingWinControl_VertScrollBar
,Forms_TCustomDesignControl_Create
,get_Forms_TCustomDesignControl_DesignTimeDPI
,set_Forms_TCustomDesignControl_DesignTimeDPI
,get_Forms_TCustomDesignControl_DesignTimePPI
,set_Forms_TCustomDesignControl_DesignTimePPI
,get_Forms_TCustomDesignControl_PixelsPerInch
,set_Forms_TCustomDesignControl_PixelsPerInch
,get_Forms_TCustomDesignControl_Scaled
,set_Forms_TCustomDesignControl_Scaled
,Forms_TCustomForm_Create
,Forms_TCustomForm_CreateNew
,get_Forms_TCustomForm_Active
,get_Forms_TCustomForm_ActiveControl
,set_Forms_TCustomForm_ActiveControl
,get_Forms_TCustomForm_ActiveDefaultControl
,set_Forms_TCustomForm_ActiveDefaultControl
,get_Forms_TCustomForm_AllowDropFiles
,set_Forms_TCustomForm_AllowDropFiles
,get_Forms_TCustomForm_AlphaBlend
,set_Forms_TCustomForm_AlphaBlend
,get_Forms_TCustomForm_AutoScroll
,set_Forms_TCustomForm_AutoScroll
,get_Forms_TCustomForm_BorderIcons
,set_Forms_TCustomForm_BorderIcons
,get_Forms_TCustomForm_BorderStyle
,set_Forms_TCustomForm_BorderStyle
,get_Forms_TCustomForm_CancelControl
,set_Forms_TCustomForm_CancelControl
,get_Forms_TCustomForm_DefaultControl
,set_Forms_TCustomForm_DefaultControl
,get_Forms_TCustomForm_DefaultMonitor
,set_Forms_TCustomForm_DefaultMonitor
,get_Forms_TIDesigner_LookupRoot
,get_Forms_TIDesigner_DefaultFormBoundsValid
,set_Forms_TIDesigner_DefaultFormBoundsValid
,get_Forms_TCustomForm_Designer
,set_Forms_TCustomForm_Designer
,get_Forms_TCustomForm_EffectiveShowInTaskBar
,get_Forms_TCustomForm_FormState
,get_Forms_TCustomForm_FormStyle
,set_Forms_TCustomForm_FormStyle
,get_Forms_TCustomForm_HelpFile
,set_Forms_TCustomForm_HelpFile
,Graphics_TCustomIcon_Create
,get_Graphics_TCustomIcon_Current
,set_Graphics_TCustomIcon_Current
,get_Graphics_TCustomIcon_Count
,Graphics_TIcon_Create
,get_Forms_TCustomForm_Icon
,set_Forms_TCustomForm_Icon
,get_Forms_TCustomForm_KeyPreview
,set_Forms_TCustomForm_KeyPreview
,get_Forms_TCustomForm_MDIChildren
,Menus_TMainMenu_Create
,get_Menus_TMainMenu_Height
,set_Menus_TMainMenu_OnChange
,get_Forms_TCustomForm_Menu
,set_Forms_TCustomForm_Menu
,get_Forms_TMonitor_MonitorNum
,get_Forms_TMonitor_Left
,get_Forms_TMonitor_Height
,get_Forms_TMonitor_Top
,get_Forms_TMonitor_Width
,get_Forms_TMonitor_Primary
,get_Forms_TMonitor_PixelsPerInch
,get_Forms_TCustomForm_Monitor
,get_Forms_TCustomForm_PopupMode
,set_Forms_TCustomForm_PopupMode
,get_Forms_TCustomForm_PopupParent
,set_Forms_TCustomForm_PopupParent
,set_Forms_TCustomForm_OnActivate
,set_Forms_TCustomForm_OnClose
,set_Forms_TCustomForm_OnCloseQuery
,set_Forms_TCustomForm_OnCreate
,set_Forms_TCustomForm_OnDeactivate
,set_Forms_TCustomForm_OnDestroy
,set_Forms_TCustomForm_OnHide
,set_Forms_TCustomForm_OnShow
,set_Forms_TCustomForm_OnShowModalFinished
,set_Forms_TCustomForm_OnWindowStateChange
,get_Forms_TCustomForm_ParentFont
,set_Forms_TCustomForm_ParentFont
,get_Forms_TCustomForm_Position
,set_Forms_TCustomForm_Position
,get_Forms_TCustomForm_RestoredLeft
,get_Forms_TCustomForm_RestoredTop
,get_Forms_TCustomForm_RestoredWidth
,get_Forms_TCustomForm_RestoredHeight
,get_Forms_TCustomForm_ShowInTaskBar
,set_Forms_TCustomForm_ShowInTaskBar
,get_Forms_TCustomForm_WindowState
,set_Forms_TCustomForm_WindowState
,Forms_TForm_Create
,get_Forms_TForm_DragKind
,set_Forms_TForm_DragKind
,get_Forms_TForm_DragMode
,set_Forms_TForm_DragMode
,set_Forms_TForm_OnDblClick
,set_Forms_TForm_OnDragDrop
,set_Forms_TForm_OnDragOver
,set_Forms_TForm_OnEndDock
,set_Forms_TForm_OnMouseDown
,set_Forms_TForm_OnMouseEnter
,set_Forms_TForm_OnMouseLeave
,set_Forms_TForm_OnMouseMove
,set_Forms_TForm_OnMouseUp
,set_Forms_TForm_OnStartDock
,get_Forms_TForm_SessionProperties
,set_Forms_TForm_SessionProperties
,get_Forms_TForm_LCLVersion
,set_Forms_TForm_LCLVersion
,ExtCtrls_TCustomPanel_Create
,get_ExtCtrls_TCustomPanel_Alignment
,set_ExtCtrls_TCustomPanel_Alignment
,get_ExtCtrls_TCustomPanel_FullRepaint
,set_ExtCtrls_TCustomPanel_FullRepaint
,get_ExtCtrls_TCustomPanel_ParentColor
,set_ExtCtrls_TCustomPanel_ParentColor
,get_ExtCtrls_TPanel_DragKind
,set_ExtCtrls_TPanel_DragKind
,get_ExtCtrls_TPanel_DragMode
,set_ExtCtrls_TPanel_DragMode
,get_ExtCtrls_TPanel_ParentFont
,set_ExtCtrls_TPanel_ParentFont
,get_ExtCtrls_TPanel_ParentShowHint
,set_ExtCtrls_TPanel_ParentShowHint
,set_ExtCtrls_TPanel_OnDblClick
,set_ExtCtrls_TPanel_OnDragDrop
,set_ExtCtrls_TPanel_OnDragOver
,set_ExtCtrls_TPanel_OnEndDock
,set_ExtCtrls_TPanel_OnEndDrag
,set_ExtCtrls_TPanel_OnGetDockCaption
,set_ExtCtrls_TPanel_OnMouseDown
,set_ExtCtrls_TPanel_OnMouseEnter
,set_ExtCtrls_TPanel_OnMouseLeave
,set_ExtCtrls_TPanel_OnMouseMove
,set_ExtCtrls_TPanel_OnMouseUp
,set_ExtCtrls_TPanel_OnStartDock
,set_ExtCtrls_TPanel_OnStartDrag
,ExtCtrls_TPanel_Create
,StdCtrls_TButtonControl_Create
,StdCtrls_TCustomButton_Create
,get_StdCtrls_TCustomButton_Active
,get_StdCtrls_TCustomButton_Default
,set_StdCtrls_TCustomButton_Default
,get_StdCtrls_TCustomButton_Cancel
,set_StdCtrls_TCustomButton_Cancel
,get_StdCtrls_TButton_DragKind
,set_StdCtrls_TButton_DragKind
,get_StdCtrls_TButton_DragMode
,set_StdCtrls_TButton_DragMode
,set_StdCtrls_TButton_OnDragDrop
,set_StdCtrls_TButton_OnDragOver
,set_StdCtrls_TButton_OnEndDrag
,set_StdCtrls_TButton_OnMouseDown
,set_StdCtrls_TButton_OnMouseEnter
,set_StdCtrls_TButton_OnMouseLeave
,set_StdCtrls_TButton_OnMouseMove
,set_StdCtrls_TButton_OnMouseUp
,set_StdCtrls_TButton_OnStartDrag
,get_StdCtrls_TButton_ParentFont
,set_StdCtrls_TButton_ParentFont
,get_StdCtrls_TButton_ParentShowHint
,set_StdCtrls_TButton_ParentShowHint
,StdCtrls_TButton_Create
,StdCtrls_TCustomCheckBox_Create
,get_StdCtrls_TCustomCheckBox_AllowGrayed
,set_StdCtrls_TCustomCheckBox_AllowGrayed
,get_StdCtrls_TCustomCheckBox_State
,set_StdCtrls_TCustomCheckBox_State
,set_StdCtrls_TCustomCheckBox_OnChange
,StdCtrls_TRadioButton_Create
,get_StdCtrls_TRadioButton_Checked
,set_StdCtrls_TRadioButton_Checked
,get_StdCtrls_TRadioButton_DragKind
,set_StdCtrls_TRadioButton_DragKind
,get_StdCtrls_TRadioButton_DragMode
,set_StdCtrls_TRadioButton_DragMode
,set_StdCtrls_TRadioButton_OnDragDrop
,set_StdCtrls_TRadioButton_OnDragOver
,set_StdCtrls_TRadioButton_OnEndDrag
,set_StdCtrls_TRadioButton_OnMouseDown
,set_StdCtrls_TRadioButton_OnMouseEnter
,set_StdCtrls_TRadioButton_OnMouseLeave
,set_StdCtrls_TRadioButton_OnMouseMove
,set_StdCtrls_TRadioButton_OnMouseUp
,set_StdCtrls_TRadioButton_OnStartDrag
,get_StdCtrls_TRadioButton_ParentColor
,set_StdCtrls_TRadioButton_ParentColor
,get_StdCtrls_TRadioButton_ParentFont
,set_StdCtrls_TRadioButton_ParentFont
,get_StdCtrls_TRadioButton_ParentShowHint
,set_StdCtrls_TRadioButton_ParentShowHint
,StdCtrls_TCheckBox_Create
,get_StdCtrls_TCheckBox_Checked
,set_StdCtrls_TCheckBox_Checked
,get_StdCtrls_TCheckBox_DragKind
,set_StdCtrls_TCheckBox_DragKind
,get_StdCtrls_TCheckBox_DragMode
,set_StdCtrls_TCheckBox_DragMode
,set_StdCtrls_TCheckBox_OnDragDrop
,set_StdCtrls_TCheckBox_OnDragOver
,set_StdCtrls_TCheckBox_OnEditingDone
,set_StdCtrls_TCheckBox_OnEndDrag
,set_StdCtrls_TCheckBox_OnMouseDown
,set_StdCtrls_TCheckBox_OnMouseEnter
,set_StdCtrls_TCheckBox_OnMouseLeave
,set_StdCtrls_TCheckBox_OnMouseMove
,set_StdCtrls_TCheckBox_OnMouseUp
,set_StdCtrls_TCheckBox_OnStartDrag
,get_StdCtrls_TCheckBox_ParentColor
,set_StdCtrls_TCheckBox_ParentColor
,get_StdCtrls_TCheckBox_ParentFont
,set_StdCtrls_TCheckBox_ParentFont
,get_StdCtrls_TCheckBox_ParentShowHint
,set_StdCtrls_TCheckBox_ParentShowHint
,StdCtrls_TToggleBox_Create
,get_StdCtrls_TToggleBox_Checked
,set_StdCtrls_TToggleBox_Checked
,get_StdCtrls_TToggleBox_DragKind
,set_StdCtrls_TToggleBox_DragKind
,get_StdCtrls_TToggleBox_DragMode
,set_StdCtrls_TToggleBox_DragMode
,set_StdCtrls_TToggleBox_OnDragDrop
,set_StdCtrls_TToggleBox_OnDragOver
,set_StdCtrls_TToggleBox_OnEndDrag
,set_StdCtrls_TToggleBox_OnMouseDown
,set_StdCtrls_TToggleBox_OnMouseEnter
,set_StdCtrls_TToggleBox_OnMouseLeave
,set_StdCtrls_TToggleBox_OnMouseMove
,set_StdCtrls_TToggleBox_OnMouseUp
,set_StdCtrls_TToggleBox_OnStartDrag
,get_StdCtrls_TToggleBox_ParentFont
,set_StdCtrls_TToggleBox_ParentFont
,get_StdCtrls_TToggleBox_ParentShowHint
,set_StdCtrls_TToggleBox_ParentShowHint
,StdCtrls_TCustomComboBox_Create
,get_StdCtrls_TCustomComboBox_CharCase
,set_StdCtrls_TCustomComboBox_CharCase
,get_StdCtrls_TCustomComboBox_DroppedDown
,set_StdCtrls_TCustomComboBox_DroppedDown
,get_StdCtrls_TCustomComboBox_DroppingDown
,set_StdCtrls_TCustomComboBox_DroppingDown
,get_StdCtrls_TCustomComboBox_AutoComplete
,set_StdCtrls_TCustomComboBox_AutoComplete
,get_StdCtrls_TCustomComboBox_AutoCompleteText
,set_StdCtrls_TCustomComboBox_AutoCompleteText
,get_StdCtrls_TCustomComboBox_AutoDropDown
,set_StdCtrls_TCustomComboBox_AutoDropDown
,get_StdCtrls_TCustomComboBox_AutoSelect
,set_StdCtrls_TCustomComboBox_AutoSelect
,get_StdCtrls_TCustomComboBox_AutoSelected
,set_StdCtrls_TCustomComboBox_AutoSelected
,get_StdCtrls_TCustomComboBox_ArrowKeysTraverseList
,set_StdCtrls_TCustomComboBox_ArrowKeysTraverseList
,get_StdCtrls_TCustomComboBox_Canvas
,get_StdCtrls_TCustomComboBox_DropDownCount
,set_StdCtrls_TCustomComboBox_DropDownCount
,get_Classes_TStrings_DelimitedText
,set_Classes_TStrings_DelimitedText
,get_Classes_TStrings_LineBreak
,set_Classes_TStrings_LineBreak
,get_Classes_TStrings_StrictDelimiter
,set_Classes_TStrings_StrictDelimiter
,get_Classes_TStrings_ValueFromIndex
,set_Classes_TStrings_ValueFromIndex
,get_Classes_TStrings_Capacity
,set_Classes_TStrings_Capacity
,get_Classes_TStrings_CommaText
,set_Classes_TStrings_CommaText
,get_Classes_TStrings_Count
,get_Classes_TStrings_Names
,get_Classes_TStrings_Objects
,set_Classes_TStrings_Objects
,get_Classes_TStrings_Strings
,set_Classes_TStrings_Strings
,get_Classes_TStrings_Text
,set_Classes_TStrings_Text
,get_Classes_TStrings_StringsAdapter
,set_Classes_TStrings_StringsAdapter
,get_Classes_TStrings_SkipLastLineBreak
,set_Classes_TStrings_SkipLastLineBreak
,get_StdCtrls_TCustomComboBox_Items
,set_StdCtrls_TCustomComboBox_Items
,get_StdCtrls_TCustomComboBox_ItemIndex
,set_StdCtrls_TCustomComboBox_ItemIndex
,get_StdCtrls_TCustomComboBox_ReadOnly
,set_StdCtrls_TCustomComboBox_ReadOnly
,get_StdCtrls_TCustomComboBox_SelLength
,set_StdCtrls_TCustomComboBox_SelLength
,get_StdCtrls_TCustomComboBox_SelStart
,set_StdCtrls_TCustomComboBox_SelStart
,get_StdCtrls_TCustomComboBox_SelText
,set_StdCtrls_TCustomComboBox_SelText
,get_StdCtrls_TCustomComboBox_Style
,set_StdCtrls_TCustomComboBox_Style
,get_StdCtrls_TCustomComboBox_Text
,set_StdCtrls_TCustomComboBox_Text
,get_StdCtrls_TComboBox_DragKind
,set_StdCtrls_TComboBox_DragKind
,get_StdCtrls_TComboBox_DragMode
,set_StdCtrls_TComboBox_DragMode
,get_StdCtrls_TComboBox_ItemHeight
,set_StdCtrls_TComboBox_ItemHeight
,get_StdCtrls_TComboBox_ItemWidth
,set_StdCtrls_TComboBox_ItemWidth
,get_StdCtrls_TComboBox_MaxLength
,set_StdCtrls_TComboBox_MaxLength
,set_StdCtrls_TComboBox_OnChange
,set_StdCtrls_TComboBox_OnCloseUp
,set_StdCtrls_TComboBox_OnDblClick
,set_StdCtrls_TComboBox_OnDragDrop
,set_StdCtrls_TComboBox_OnDragOver
,set_StdCtrls_TComboBox_OnEndDrag
,set_StdCtrls_TComboBox_OnDropDown
,set_StdCtrls_TComboBox_OnEditingDone
,set_StdCtrls_TComboBox_OnGetItems
,set_StdCtrls_TComboBox_OnMeasureItem
,set_StdCtrls_TComboBox_OnMouseDown
,set_StdCtrls_TComboBox_OnMouseEnter
,set_StdCtrls_TComboBox_OnMouseLeave
,set_StdCtrls_TComboBox_OnMouseMove
,set_StdCtrls_TComboBox_OnMouseUp
,set_StdCtrls_TComboBox_OnSelect
,set_StdCtrls_TComboBox_OnStartDrag
,get_StdCtrls_TComboBox_ParentColor
,set_StdCtrls_TComboBox_ParentColor
,get_StdCtrls_TComboBox_ParentFont
,set_StdCtrls_TComboBox_ParentFont
,get_StdCtrls_TComboBox_ParentShowHint
,set_StdCtrls_TComboBox_ParentShowHint
,get_StdCtrls_TComboBox_Sorted
,set_StdCtrls_TComboBox_Sorted
,StdCtrls_TComboBox_Create
,StdCtrls_TCustomEdit_Create
,get_StdCtrls_TCustomEdit_Alignment
,set_StdCtrls_TCustomEdit_Alignment
,get_StdCtrls_TCustomEdit_CanUndo
,get_StdCtrls_TCustomEdit_CharCase
,set_StdCtrls_TCustomEdit_CharCase
,get_StdCtrls_TCustomEdit_EchoMode
,set_StdCtrls_TCustomEdit_EchoMode
,get_StdCtrls_TCustomEdit_HideSelection
,set_StdCtrls_TCustomEdit_HideSelection
,get_StdCtrls_TCustomEdit_MaxLength
,set_StdCtrls_TCustomEdit_MaxLength
,get_StdCtrls_TCustomEdit_Modified
,set_StdCtrls_TCustomEdit_Modified
,get_StdCtrls_TCustomEdit_NumbersOnly
,set_StdCtrls_TCustomEdit_NumbersOnly
,set_StdCtrls_TCustomEdit_OnChange
,get_StdCtrls_TCustomEdit_ReadOnly
,set_StdCtrls_TCustomEdit_ReadOnly
,get_StdCtrls_TCustomEdit_SelLength
,set_StdCtrls_TCustomEdit_SelLength
,get_StdCtrls_TCustomEdit_SelStart
,set_StdCtrls_TCustomEdit_SelStart
,get_StdCtrls_TCustomEdit_SelText
,set_StdCtrls_TCustomEdit_SelText
,get_StdCtrls_TCustomEdit_Text
,set_StdCtrls_TCustomEdit_Text
,get_StdCtrls_TCustomEdit_TextHintFontStyle
,set_StdCtrls_TCustomEdit_TextHintFontStyle
,get_StdCtrls_TEdit_AutoSelected
,set_StdCtrls_TEdit_AutoSelected
,get_StdCtrls_TEdit_AutoSelect
,set_StdCtrls_TEdit_AutoSelect
,get_StdCtrls_TEdit_DragKind
,set_StdCtrls_TEdit_DragKind
,get_StdCtrls_TEdit_DragMode
,set_StdCtrls_TEdit_DragMode
,set_StdCtrls_TEdit_OnDblClick
,set_StdCtrls_TEdit_OnDragDrop
,set_StdCtrls_TEdit_OnDragOver
,set_StdCtrls_TEdit_OnEditingDone
,set_StdCtrls_TEdit_OnEndDrag
,set_StdCtrls_TEdit_OnMouseDown
,set_StdCtrls_TEdit_OnMouseEnter
,set_StdCtrls_TEdit_OnMouseLeave
,set_StdCtrls_TEdit_OnMouseMove
,set_StdCtrls_TEdit_OnMouseUp
,set_StdCtrls_TEdit_OnStartDrag
,get_StdCtrls_TEdit_ParentColor
,set_StdCtrls_TEdit_ParentColor
,get_StdCtrls_TEdit_ParentFont
,set_StdCtrls_TEdit_ParentFont
,get_StdCtrls_TEdit_ParentShowHint
,set_StdCtrls_TEdit_ParentShowHint
,StdCtrls_TEdit_Create
,StdCtrls_TCustomMemo_Create
,get_StdCtrls_TCustomMemo_Lines
,set_StdCtrls_TCustomMemo_Lines
,StdCtrls_TMemoScrollbar_Create
,get_StdCtrls_TCustomMemo_HorzScrollBar
,set_StdCtrls_TCustomMemo_HorzScrollBar
,get_StdCtrls_TCustomMemo_VertScrollBar
,set_StdCtrls_TCustomMemo_VertScrollBar
,get_StdCtrls_TCustomMemo_ScrollBars
,set_StdCtrls_TCustomMemo_ScrollBars
,get_StdCtrls_TCustomMemo_WantReturns
,set_StdCtrls_TCustomMemo_WantReturns
,get_StdCtrls_TCustomMemo_WantTabs
,set_StdCtrls_TCustomMemo_WantTabs
,get_StdCtrls_TCustomMemo_WordWrap
,set_StdCtrls_TCustomMemo_WordWrap
,get_StdCtrls_TMemo_DragKind
,set_StdCtrls_TMemo_DragKind
,get_StdCtrls_TMemo_DragMode
,set_StdCtrls_TMemo_DragMode
,set_StdCtrls_TMemo_OnDblClick
,set_StdCtrls_TMemo_OnDragDrop
,set_StdCtrls_TMemo_OnDragOver
,set_StdCtrls_TMemo_OnEditingDone
,set_StdCtrls_TMemo_OnEndDrag
,set_StdCtrls_TMemo_OnMouseDown
,set_StdCtrls_TMemo_OnMouseEnter
,set_StdCtrls_TMemo_OnMouseLeave
,set_StdCtrls_TMemo_OnMouseMove
,set_StdCtrls_TMemo_OnMouseUp
,set_StdCtrls_TMemo_OnStartDrag
,get_StdCtrls_TMemo_ParentColor
,set_StdCtrls_TMemo_ParentColor
,get_StdCtrls_TMemo_ParentFont
,set_StdCtrls_TMemo_ParentFont
,get_StdCtrls_TMemo_ParentShowHint
,set_StdCtrls_TMemo_ParentShowHint
,StdCtrls_TMemo_Create
,StdCtrls_TCustomGroupBox_Create
,get_StdCtrls_TGroupBox_DragKind
,set_StdCtrls_TGroupBox_DragKind
,get_StdCtrls_TGroupBox_DragMode
,set_StdCtrls_TGroupBox_DragMode
,get_StdCtrls_TGroupBox_ParentColor
,set_StdCtrls_TGroupBox_ParentColor
,get_StdCtrls_TGroupBox_ParentFont
,set_StdCtrls_TGroupBox_ParentFont
,get_StdCtrls_TGroupBox_ParentShowHint
,set_StdCtrls_TGroupBox_ParentShowHint
,set_StdCtrls_TGroupBox_OnDblClick
,set_StdCtrls_TGroupBox_OnDragDrop
,set_StdCtrls_TGroupBox_OnDragOver
,set_StdCtrls_TGroupBox_OnEndDock
,set_StdCtrls_TGroupBox_OnEndDrag
,set_StdCtrls_TGroupBox_OnMouseDown
,set_StdCtrls_TGroupBox_OnMouseEnter
,set_StdCtrls_TGroupBox_OnMouseLeave
,set_StdCtrls_TGroupBox_OnMouseMove
,set_StdCtrls_TGroupBox_OnMouseUp
,set_StdCtrls_TGroupBox_OnStartDock
,set_StdCtrls_TGroupBox_OnStartDrag
,StdCtrls_TGroupBox_Create
,Controls_TGraphicControl_Create
,get_Controls_TGraphicControl_Canvas
,StdCtrls_TCustomLabel_Create
,get_StdCtrls_TLabel_Alignment
,set_StdCtrls_TLabel_Alignment
,get_StdCtrls_TLabel_DragKind
,set_StdCtrls_TLabel_DragKind
,get_StdCtrls_TLabel_DragMode
,set_StdCtrls_TLabel_DragMode
,get_StdCtrls_TLabel_FocusControl
,set_StdCtrls_TLabel_FocusControl
,get_StdCtrls_TLabel_Layout
,set_StdCtrls_TLabel_Layout
,get_StdCtrls_TLabel_ParentColor
,set_StdCtrls_TLabel_ParentColor
,get_StdCtrls_TLabel_ParentFont
,set_StdCtrls_TLabel_ParentFont
,get_StdCtrls_TLabel_ParentShowHint
,set_StdCtrls_TLabel_ParentShowHint
,get_StdCtrls_TLabel_ShowAccelChar
,set_StdCtrls_TLabel_ShowAccelChar
,get_StdCtrls_TLabel_Transparent
,set_StdCtrls_TLabel_Transparent
,get_StdCtrls_TLabel_WordWrap
,set_StdCtrls_TLabel_WordWrap
,set_StdCtrls_TLabel_OnDblClick
,set_StdCtrls_TLabel_OnDragDrop
,set_StdCtrls_TLabel_OnDragOver
,set_StdCtrls_TLabel_OnEndDrag
,set_StdCtrls_TLabel_OnMouseDown
,set_StdCtrls_TLabel_OnMouseEnter
,set_StdCtrls_TLabel_OnMouseLeave
,set_StdCtrls_TLabel_OnMouseMove
,set_StdCtrls_TLabel_OnMouseUp
,set_StdCtrls_TLabel_OnStartDrag
,get_StdCtrls_TLabel_OptimalFill
,set_StdCtrls_TLabel_OptimalFill
,StdCtrls_TLabel_Create
,StdCtrls_TCustomListBox_Create
,get_StdCtrls_TCustomListBox_Canvas
,get_StdCtrls_TCustomListBox_ClickOnSelChange
,set_StdCtrls_TCustomListBox_ClickOnSelChange
,get_StdCtrls_TCustomListBox_Columns
,set_StdCtrls_TCustomListBox_Columns
,get_StdCtrls_TCustomListBox_Count
,get_StdCtrls_TCustomListBox_ExtendedSelect
,set_StdCtrls_TCustomListBox_ExtendedSelect
,get_StdCtrls_TCustomListBox_IntegralHeight
,set_StdCtrls_TCustomListBox_IntegralHeight
,get_StdCtrls_TCustomListBox_ItemHeight
,set_StdCtrls_TCustomListBox_ItemHeight
,get_StdCtrls_TCustomListBox_ItemIndex
,set_StdCtrls_TCustomListBox_ItemIndex
,get_StdCtrls_TCustomListBox_Items
,set_StdCtrls_TCustomListBox_Items
,get_StdCtrls_TCustomListBox_MultiSelect
,set_StdCtrls_TCustomListBox_MultiSelect
,set_StdCtrls_TCustomListBox_OnDblClick
,set_StdCtrls_TCustomListBox_OnMeasureItem
,set_StdCtrls_TCustomListBox_OnMouseDown
,set_StdCtrls_TCustomListBox_OnMouseEnter
,set_StdCtrls_TCustomListBox_OnMouseLeave
,set_StdCtrls_TCustomListBox_OnMouseMove
,set_StdCtrls_TCustomListBox_OnMouseUp
,set_StdCtrls_TCustomListBox_OnSelectionChange
,get_StdCtrls_TCustomListBox_Options
,set_StdCtrls_TCustomListBox_Options
,get_StdCtrls_TCustomListBox_ParentColor
,set_StdCtrls_TCustomListBox_ParentColor
,get_StdCtrls_TCustomListBox_ParentFont
,set_StdCtrls_TCustomListBox_ParentFont
,get_StdCtrls_TCustomListBox_ParentShowHint
,set_StdCtrls_TCustomListBox_ParentShowHint
,get_StdCtrls_TCustomListBox_ScrollWidth
,set_StdCtrls_TCustomListBox_ScrollWidth
,get_StdCtrls_TCustomListBox_SelCount
,get_StdCtrls_TCustomListBox_Selected
,set_StdCtrls_TCustomListBox_Selected
,get_StdCtrls_TCustomListBox_Sorted
,set_StdCtrls_TCustomListBox_Sorted
,get_StdCtrls_TCustomListBox_Style
,set_StdCtrls_TCustomListBox_Style
,get_StdCtrls_TCustomListBox_TopIndex
,set_StdCtrls_TCustomListBox_TopIndex
,get_StdCtrls_TListBox_DragKind
,set_StdCtrls_TListBox_DragKind
,get_StdCtrls_TListBox_DragMode
,set_StdCtrls_TListBox_DragMode
,set_StdCtrls_TListBox_OnDragDrop
,set_StdCtrls_TListBox_OnDragOver
,set_StdCtrls_TListBox_OnEndDrag
,set_StdCtrls_TListBox_OnStartDrag
,StdCtrls_TListBox_Create
,StdCtrls_TCustomScrollBar_Create
,get_StdCtrls_TCustomScrollBar_Kind
,set_StdCtrls_TCustomScrollBar_Kind
,get_StdCtrls_TCustomScrollBar_Max
,set_StdCtrls_TCustomScrollBar_Max
,get_StdCtrls_TCustomScrollBar_Min
,set_StdCtrls_TCustomScrollBar_Min
,get_StdCtrls_TCustomScrollBar_PageSize
,set_StdCtrls_TCustomScrollBar_PageSize
,get_StdCtrls_TCustomScrollBar_Position
,set_StdCtrls_TCustomScrollBar_Position
,set_StdCtrls_TCustomScrollBar_OnChange
,set_StdCtrls_TCustomScrollBar_OnScroll
,get_StdCtrls_TScrollBar_DragKind
,set_StdCtrls_TScrollBar_DragKind
,get_StdCtrls_TScrollBar_DragMode
,set_StdCtrls_TScrollBar_DragMode
,get_StdCtrls_TScrollBar_ParentShowHint
,set_StdCtrls_TScrollBar_ParentShowHint
,set_StdCtrls_TScrollBar_OnDragDrop
,set_StdCtrls_TScrollBar_OnDragOver
,set_StdCtrls_TScrollBar_OnEndDrag
,set_StdCtrls_TScrollBar_OnStartDrag
,StdCtrls_TScrollBar_Create
,Forms_TApplicationProperties_Create
,get_Forms_TApplicationProperties_CaptureExceptions
,set_Forms_TApplicationProperties_CaptureExceptions
,get_Forms_TApplicationProperties_ExceptionDialog
,set_Forms_TApplicationProperties_ExceptionDialog
,get_Forms_TApplicationProperties_HelpFile
,set_Forms_TApplicationProperties_HelpFile
,get_Forms_TApplicationProperties_Hint
,set_Forms_TApplicationProperties_Hint
,get_Forms_TApplicationProperties_HintHidePause
,set_Forms_TApplicationProperties_HintHidePause
,get_Forms_TApplicationProperties_HintPause
,set_Forms_TApplicationProperties_HintPause
,get_Forms_TApplicationProperties_HintShortCuts
,set_Forms_TApplicationProperties_HintShortCuts
,get_Forms_TApplicationProperties_HintShortPause
,set_Forms_TApplicationProperties_HintShortPause
,get_Forms_TApplicationProperties_ShowButtonGlyphs
,set_Forms_TApplicationProperties_ShowButtonGlyphs
,get_Forms_TApplicationProperties_ShowMenuGlyphs
,set_Forms_TApplicationProperties_ShowMenuGlyphs
,get_Forms_TApplicationProperties_ShowHint
,set_Forms_TApplicationProperties_ShowHint
,get_Forms_TApplicationProperties_ShowMainForm
,set_Forms_TApplicationProperties_ShowMainForm
,get_Forms_TApplicationProperties_Title
,set_Forms_TApplicationProperties_Title
,set_Forms_TApplicationProperties_OnActivate
,set_Forms_TApplicationProperties_OnDeactivate
,set_Forms_TApplicationProperties_OnIdle
,set_Forms_TApplicationProperties_OnIdleEnd
,set_Forms_TApplicationProperties_OnEndSession
,set_Forms_TApplicationProperties_OnQueryEndSession
,set_Forms_TApplicationProperties_OnMinimize
,set_Forms_TApplicationProperties_OnModalBegin
,set_Forms_TApplicationProperties_OnModalEnd
,set_Forms_TApplicationProperties_OnRestore
,set_Forms_TApplicationProperties_OnHint
,ExtCtrls_TBevel_Create
,get_ExtCtrls_TBevel_ParentShowHint
,set_ExtCtrls_TBevel_ParentShowHint
,get_ExtCtrls_TBevel_Shape
,set_ExtCtrls_TBevel_Shape
,get_ExtCtrls_TBevel_Style
,set_ExtCtrls_TBevel_Style
,set_ExtCtrls_TBevel_OnMouseDown
,set_ExtCtrls_TBevel_OnMouseEnter
,set_ExtCtrls_TBevel_OnMouseLeave
,set_ExtCtrls_TBevel_OnMouseMove
,set_ExtCtrls_TBevel_OnMouseUp
,set_ExtCtrls_TBevel_OnPaint
,Buttons_TCustomBitBtn_Create
,get_Buttons_TCustomBitBtn_DefaultCaption
,set_Buttons_TCustomBitBtn_DefaultCaption
,get_Buttons_TCustomBitBtn_Glyph
,set_Buttons_TCustomBitBtn_Glyph
,get_Buttons_TCustomBitBtn_NumGlyphs
,set_Buttons_TCustomBitBtn_NumGlyphs
,get_Buttons_TCustomBitBtn_Kind
,set_Buttons_TCustomBitBtn_Kind
,get_Buttons_TCustomBitBtn_Layout
,set_Buttons_TCustomBitBtn_Layout
,get_Buttons_TCustomBitBtn_Margin
,set_Buttons_TCustomBitBtn_Margin
,get_Buttons_TCustomBitBtn_Spacing
,set_Buttons_TCustomBitBtn_Spacing
,get_Buttons_TCustomBitBtn_GlyphShowMode
,set_Buttons_TCustomBitBtn_GlyphShowMode
,set_Buttons_TBitBtn_OnDragDrop
,set_Buttons_TBitBtn_OnDragOver
,set_Buttons_TBitBtn_OnEndDrag
,set_Buttons_TBitBtn_OnMouseDown
,set_Buttons_TBitBtn_OnMouseEnter
,set_Buttons_TBitBtn_OnMouseLeave
,set_Buttons_TBitBtn_OnMouseMove
,set_Buttons_TBitBtn_OnMouseUp
,set_Buttons_TBitBtn_OnStartDrag
,get_Buttons_TBitBtn_ParentFont
,set_Buttons_TBitBtn_ParentFont
,get_Buttons_TBitBtn_ParentShowHint
,set_Buttons_TBitBtn_ParentShowHint
,Buttons_TBitBtn_Create
,CheckLst_TCustomCheckListBox_Create
,get_CheckLst_TCustomCheckListBox_AllowGrayed
,set_CheckLst_TCustomCheckListBox_AllowGrayed
,get_CheckLst_TCustomCheckListBox_Checked
,set_CheckLst_TCustomCheckListBox_Checked
,get_CheckLst_TCustomCheckListBox_Header
,set_CheckLst_TCustomCheckListBox_Header
,get_CheckLst_TCustomCheckListBox_ItemEnabled
,set_CheckLst_TCustomCheckListBox_ItemEnabled
,get_CheckLst_TCustomCheckListBox_State
,set_CheckLst_TCustomCheckListBox_State
,set_CheckLst_TCustomCheckListBox_OnClickCheck
,set_CheckLst_TCustomCheckListBox_OnItemClick
,get_CheckLst_TCheckListBox_DragMode
,set_CheckLst_TCheckListBox_DragMode
,set_CheckLst_TCheckListBox_OnDragDrop
,set_CheckLst_TCheckListBox_OnDragOver
,set_CheckLst_TCheckListBox_OnEndDrag
,set_CheckLst_TCheckListBox_OnStartDrag
,CheckLst_TCheckListBox_Create
,ColorBox_TCustomColorBox_Create
,get_ColorBox_TCustomColorBox_ColorRectWidth
,set_ColorBox_TCustomColorBox_ColorRectWidth
,get_ColorBox_TCustomColorBox_ColorRectOffset
,set_ColorBox_TCustomColorBox_ColorRectOffset
,get_ColorBox_TCustomColorBox_Style
,set_ColorBox_TCustomColorBox_Style
,get_ColorBox_TCustomColorBox_ColorNames
,get_ColorBox_TColorBox_DragMode
,set_ColorBox_TColorBox_DragMode
,get_ColorBox_TColorBox_ItemHeight
,set_ColorBox_TColorBox_ItemHeight
,get_ColorBox_TColorBox_ItemWidth
,set_ColorBox_TColorBox_ItemWidth
,set_ColorBox_TColorBox_OnChange
,set_ColorBox_TColorBox_OnCloseUp
,set_ColorBox_TColorBox_OnDblClick
,set_ColorBox_TColorBox_OnDragDrop
,set_ColorBox_TColorBox_OnDragOver
,set_ColorBox_TColorBox_OnEndDrag
,set_ColorBox_TColorBox_OnDropDown
,set_ColorBox_TColorBox_OnEditingDone
,set_ColorBox_TColorBox_OnMouseDown
,set_ColorBox_TColorBox_OnMouseEnter
,set_ColorBox_TColorBox_OnMouseLeave
,set_ColorBox_TColorBox_OnMouseMove
,set_ColorBox_TColorBox_OnMouseUp
,set_ColorBox_TColorBox_OnStartDrag
,set_ColorBox_TColorBox_OnSelect
,get_ColorBox_TColorBox_ParentColor
,set_ColorBox_TColorBox_ParentColor
,get_ColorBox_TColorBox_ParentFont
,set_ColorBox_TColorBox_ParentFont
,get_ColorBox_TColorBox_ParentShowHint
,set_ColorBox_TColorBox_ParentShowHint
,ColorBox_TColorBox_Create
,ColorBox_TCustomColorListBox_Create
,get_ColorBox_TCustomColorListBox_ColorRectWidth
,set_ColorBox_TCustomColorListBox_ColorRectWidth
,get_ColorBox_TCustomColorListBox_ColorRectOffset
,set_ColorBox_TCustomColorListBox_ColorRectOffset
,get_ColorBox_TCustomColorListBox_Style
,set_ColorBox_TCustomColorListBox_Style
,get_ColorBox_TCustomColorListBox_ColorNames
,get_ColorBox_TColorListBox_DragKind
,set_ColorBox_TColorListBox_DragKind
,get_ColorBox_TColorListBox_DragMode
,set_ColorBox_TColorListBox_DragMode
,set_ColorBox_TColorListBox_OnDragDrop
,set_ColorBox_TColorListBox_OnDragOver
,set_ColorBox_TColorListBox_OnEndDrag
,set_ColorBox_TColorListBox_OnStartDrag
,ColorBox_TColorListBox_Create
,ExtCtrls_TCustomControlBar_Create
,get_ExtCtrls_TCustomControlBar_AutoDock
,set_ExtCtrls_TCustomControlBar_AutoDock
,get_ExtCtrls_TCustomControlBar_AutoDrag
,set_ExtCtrls_TCustomControlBar_AutoDrag
,get_ExtCtrls_TCustomControlBar_DrawingStyle
,set_ExtCtrls_TCustomControlBar_DrawingStyle
,get_ExtCtrls_TCustomControlBar_GradientDirection
,set_ExtCtrls_TCustomControlBar_GradientDirection
,Graphics_TPicture_Create
,get_Graphics_TPicture_Bitmap
,set_Graphics_TPicture_Bitmap
,get_Graphics_TPicture_Icon
,set_Graphics_TPicture_Icon
,Graphics_TJPEGImage_Create
,get_Graphics_TJPEGImage_GrayScale
,get_Graphics_TJPEGImage_ProgressiveEncoding
,get_Graphics_TPicture_Jpeg
,set_Graphics_TPicture_Jpeg
,Graphics_TPixmap_Create
,get_Graphics_TPicture_Pixmap
,set_Graphics_TPicture_Pixmap
,Graphics_TPortableNetworkGraphic_Create
,get_Graphics_TPicture_PNG
,set_Graphics_TPicture_PNG
,Graphics_TPortableAnyMapGraphic_Create
,get_Graphics_TPicture_PNM
,set_Graphics_TPicture_PNM
,get_Graphics_TPicture_Graphic
,set_Graphics_TPicture_Graphic
,get_Graphics_TPicture_Height
,get_Graphics_TPicture_Width
,set_Graphics_TPicture_OnChange
,get_ExtCtrls_TCustomControlBar_Picture
,set_ExtCtrls_TCustomControlBar_Picture
,get_ExtCtrls_TCustomControlBar_RowSnap
,set_ExtCtrls_TCustomControlBar_RowSnap
,set_ExtCtrls_TCustomControlBar_OnBandDrag
,set_ExtCtrls_TCustomControlBar_OnCanResize
,set_ExtCtrls_TCustomControlBar_OnPaint
,get_ExtCtrls_TControlBar_DragKind
,set_ExtCtrls_TControlBar_DragKind
,get_ExtCtrls_TControlBar_DragMode
,set_ExtCtrls_TControlBar_DragMode
,get_ExtCtrls_TControlBar_ParentFont
,set_ExtCtrls_TControlBar_ParentFont
,get_ExtCtrls_TControlBar_ParentShowHint
,set_ExtCtrls_TControlBar_ParentShowHint
,set_ExtCtrls_TControlBar_OnDblClick
,set_ExtCtrls_TControlBar_OnDragDrop
,set_ExtCtrls_TControlBar_OnDragOver
,set_ExtCtrls_TControlBar_OnEndDock
,set_ExtCtrls_TControlBar_OnEndDrag
,set_ExtCtrls_TControlBar_OnMouseDown
,set_ExtCtrls_TControlBar_OnMouseEnter
,set_ExtCtrls_TControlBar_OnMouseLeave
,set_ExtCtrls_TControlBar_OnMouseMove
,set_ExtCtrls_TControlBar_OnMouseUp
,set_ExtCtrls_TControlBar_OnStartDock
,set_ExtCtrls_TControlBar_OnStartDrag
,ExtCtrls_TControlBar_Create
,get_Classes_TCollection_Count
,get_Classes_TCollectionItem_Collection
,set_Classes_TCollectionItem_Collection
,get_Classes_TCollectionItem_ID
,get_Classes_TCollectionItem_Index
,set_Classes_TCollectionItem_Index
,get_Classes_TCollectionItem_DisplayName
,set_Classes_TCollectionItem_DisplayName
,get_Classes_TCollection_Items
,set_Classes_TCollection_Items
,get_Grids_TGridColumns_Grid
,Grids_TGridColumn_Create
,get_Grids_TGridColumn_Grid
,get_Grids_TGridColumn_DefaultWidth
,get_Grids_TGridColumn_StoredWidth
,get_Grids_TGridColumn_WidthChanged
,get_Grids_TGridColumn_Alignment
,set_Grids_TGridColumn_Alignment
,get_Grids_TGridColumn_ButtonStyle
,set_Grids_TGridColumn_ButtonStyle
,get_Grids_TGridColumn_Expanded
,set_Grids_TGridColumn_Expanded
,get_Grids_TGridColumn_Font
,set_Grids_TGridColumn_Font
,get_Grids_TGridColumn_Layout
,set_Grids_TGridColumn_Layout
,get_Grids_TGridColumn_MinSize
,set_Grids_TGridColumn_MinSize
,get_Grids_TGridColumn_MaxSize
,set_Grids_TGridColumn_MaxSize
,get_Grids_TGridColumn_PickList
,set_Grids_TGridColumn_PickList
,get_Grids_TGridColumn_ReadOnly
,set_Grids_TGridColumn_ReadOnly
,get_Grids_TGridColumn_SizePriority
,set_Grids_TGridColumn_SizePriority
,get_Grids_TGridColumnTitle_Column
,get_Grids_TGridColumnTitle_Alignment
,set_Grids_TGridColumnTitle_Alignment
,get_Grids_TGridColumnTitle_Caption
,set_Grids_TGridColumnTitle_Caption
,get_Grids_TGridColumnTitle_Font
,set_Grids_TGridColumnTitle_Font
,get_Grids_TGridColumnTitle_ImageIndex
,set_Grids_TGridColumnTitle_ImageIndex
,get_Grids_TGridColumnTitle_ImageLayout
,set_Grids_TGridColumnTitle_ImageLayout
,get_Grids_TGridColumnTitle_Layout
,set_Grids_TGridColumnTitle_Layout
,get_Grids_TGridColumnTitle_MultiLine
,set_Grids_TGridColumnTitle_MultiLine
,get_Grids_TGridColumnTitle_PrefixOption
,set_Grids_TGridColumnTitle_PrefixOption
,get_Grids_TGridColumn_Title
,set_Grids_TGridColumn_Title
,get_Grids_TGridColumn_Width
,set_Grids_TGridColumn_Width
,get_Grids_TGridColumn_Visible
,set_Grids_TGridColumn_Visible
,get_Grids_TGridColumn_ValueChecked
,set_Grids_TGridColumn_ValueChecked
,get_Grids_TGridColumn_ValueUnchecked
,set_Grids_TGridColumn_ValueUnchecked
,get_Grids_TGridColumns_Items
,set_Grids_TGridColumns_Items
,get_Grids_TGridColumns_VisibleCount
,get_Grids_TGridColumns_Enabled
,get_Controls_TDragImageList_Dragging
,Controls_TDragImageList_Create
,Controls_TImageList_Create
,Grids_TCustomGrid_Create
,get_Grids_TCustomGrid_SelectedRangeCount
,get_Grids_TCustomGrid_SortOrder
,set_Grids_TCustomGrid_SortOrder
,get_Grids_TCustomGrid_SortColumn
,Grids_TCustomDrawGrid_Create
,get_Grids_TCustomDrawGrid_AllowOutboundEvents
,set_Grids_TCustomDrawGrid_AllowOutboundEvents
,get_Grids_TCustomDrawGrid_Col
,set_Grids_TCustomDrawGrid_Col
,get_Grids_TCustomDrawGrid_ColWidths
,set_Grids_TCustomDrawGrid_ColWidths
,get_Grids_TCustomDrawGrid_Editor
,set_Grids_TCustomDrawGrid_Editor
,get_Grids_TCustomDrawGrid_EditorMode
,set_Grids_TCustomDrawGrid_EditorMode
,get_Grids_TCustomDrawGrid_ExtendedColSizing
,set_Grids_TCustomDrawGrid_ExtendedColSizing
,get_Grids_TCustomDrawGrid_AltColorStartNormal
,set_Grids_TCustomDrawGrid_AltColorStartNormal
,get_Grids_TCustomDrawGrid_FastEditing
,set_Grids_TCustomDrawGrid_FastEditing
,get_Grids_TCustomDrawGrid_FocusRectVisible
,set_Grids_TCustomDrawGrid_FocusRectVisible
,get_Grids_TCustomDrawGrid_GridHeight
,get_Grids_TCustomDrawGrid_GridWidth
,get_Grids_TCustomDrawGrid_IsCellSelected
,get_Grids_TCustomDrawGrid_LeftCol
,set_Grids_TCustomDrawGrid_LeftCol
,get_Grids_TCustomDrawGrid_Row
,set_Grids_TCustomDrawGrid_Row
,get_Grids_TCustomDrawGrid_RowHeights
,set_Grids_TCustomDrawGrid_RowHeights
,get_Grids_TCustomDrawGrid_SaveOptions
,set_Grids_TCustomDrawGrid_SaveOptions
,get_Grids_TCustomDrawGrid_SelectedColumn
,get_Grids_TCustomDrawGrid_StrictSort
,set_Grids_TCustomDrawGrid_StrictSort
,get_Grids_TCustomDrawGrid_TopRow
,set_Grids_TCustomDrawGrid_TopRow
,get_Grids_TCustomDrawGrid_UseXORFeatures
,set_Grids_TCustomDrawGrid_UseXORFeatures
,get_Grids_TCustomDrawGrid_AutoAdvance
,set_Grids_TCustomDrawGrid_AutoAdvance
,get_Grids_TCustomDrawGrid_AutoFillColumns
,set_Grids_TCustomDrawGrid_AutoFillColumns
,get_Grids_TCustomDrawGrid_ColCount
,set_Grids_TCustomDrawGrid_ColCount
,get_Grids_TCustomDrawGrid_Columns
,set_Grids_TCustomDrawGrid_Columns
,get_Grids_TCustomDrawGrid_DefaultColWidth
,set_Grids_TCustomDrawGrid_DefaultColWidth
,get_Grids_TCustomDrawGrid_DefaultDrawing
,set_Grids_TCustomDrawGrid_DefaultDrawing
,get_Grids_TCustomDrawGrid_DefaultRowHeight
,set_Grids_TCustomDrawGrid_DefaultRowHeight
,get_Grids_TCustomDrawGrid_FixedCols
,set_Grids_TCustomDrawGrid_FixedCols
,get_Grids_TCustomDrawGrid_FixedRows
,set_Grids_TCustomDrawGrid_FixedRows
,get_Grids_TCustomDrawGrid_Flat
,set_Grids_TCustomDrawGrid_Flat
,get_Grids_TCustomDrawGrid_GridLineWidth
,set_Grids_TCustomDrawGrid_GridLineWidth
,get_Grids_TCustomDrawGrid_Options
,set_Grids_TCustomDrawGrid_Options
,get_Grids_TCustomDrawGrid_Options2
,set_Grids_TCustomDrawGrid_Options2
,get_Grids_TCustomDrawGrid_ParentShowHint
,set_Grids_TCustomDrawGrid_ParentShowHint
,get_Grids_TCustomDrawGrid_RowCount
,set_Grids_TCustomDrawGrid_RowCount
,get_Grids_TCustomDrawGrid_ScrollBars
,set_Grids_TCustomDrawGrid_ScrollBars
,get_Grids_TCustomDrawGrid_TabAdvance
,set_Grids_TCustomDrawGrid_TabAdvance
,get_Grids_TCustomDrawGrid_VisibleColCount
,get_Grids_TCustomDrawGrid_VisibleRowCount
,set_Grids_TCustomDrawGrid_OnAfterSelection
,set_Grids_TCustomDrawGrid_OnBeforeSelection
,set_Grids_TCustomDrawGrid_OnColRowDeleted
,set_Grids_TCustomDrawGrid_OnColRowExchanged
,set_Grids_TCustomDrawGrid_OnColRowInserted
,set_Grids_TCustomDrawGrid_OnColRowMoved
,set_Grids_TCustomDrawGrid_OnCompareCells
,set_Grids_TCustomDrawGrid_OnDblClick
,set_Grids_TCustomDrawGrid_OnDragDrop
,set_Grids_TCustomDrawGrid_OnDragOver
,set_Grids_TCustomDrawGrid_OnEditButtonClick
,set_Grids_TCustomDrawGrid_OnButtonClick
,set_Grids_TCustomDrawGrid_OnEndDock
,set_Grids_TCustomDrawGrid_OnEndDrag
,set_Grids_TCustomDrawGrid_OnGetEditMask
,set_Grids_TCustomDrawGrid_OnGetEditText
,set_Grids_TCustomDrawGrid_OnHeaderClick
,set_Grids_TCustomDrawGrid_OnHeaderSized
,set_Grids_TCustomDrawGrid_OnHeaderSizing
,set_Grids_TCustomDrawGrid_OnMouseDown
,set_Grids_TCustomDrawGrid_OnMouseEnter
,set_Grids_TCustomDrawGrid_OnMouseLeave
,set_Grids_TCustomDrawGrid_OnMouseMove
,set_Grids_TCustomDrawGrid_OnMouseUp
,set_Grids_TCustomDrawGrid_OnPickListSelect
,set_Grids_TCustomDrawGrid_OnPrepareCanvas
,set_Grids_TCustomDrawGrid_OnSelectEditor
,set_Grids_TCustomDrawGrid_OnSelection
,set_Grids_TCustomDrawGrid_OnSelectCell
,set_Grids_TCustomDrawGrid_OnSetEditText
,set_Grids_TCustomDrawGrid_OnStartDock
,set_Grids_TCustomDrawGrid_OnStartDrag
,get_Grids_TDrawGrid_InplaceEditor
,get_Grids_TDrawGrid_AutoEdit
,set_Grids_TDrawGrid_AutoEdit
,get_Grids_TDrawGrid_ColumnClickSorts
,set_Grids_TDrawGrid_ColumnClickSorts
,get_Grids_TDrawGrid_DragKind
,set_Grids_TDrawGrid_DragKind
,get_Grids_TDrawGrid_DragMode
,set_Grids_TDrawGrid_DragMode
,get_Grids_TDrawGrid_ExtendedSelect
,set_Grids_TDrawGrid_ExtendedSelect
,get_Grids_TDrawGrid_HeaderHotZones
,set_Grids_TDrawGrid_HeaderHotZones
,get_Grids_TDrawGrid_HeaderPushZones
,set_Grids_TDrawGrid_HeaderPushZones
,get_Grids_TDrawGrid_MouseWheelOption
,set_Grids_TDrawGrid_MouseWheelOption
,get_Grids_TDrawGrid_ParentColor
,set_Grids_TDrawGrid_ParentColor
,get_Grids_TDrawGrid_ParentFont
,set_Grids_TDrawGrid_ParentFont
,get_Grids_TDrawGrid_RangeSelectMode
,set_Grids_TDrawGrid_RangeSelectMode
,get_Grids_TDrawGrid_TitleFont
,set_Grids_TDrawGrid_TitleFont
,get_Grids_TDrawGrid_TitleImageList
,set_Grids_TDrawGrid_TitleImageList
,get_Grids_TDrawGrid_TitleStyle
,set_Grids_TDrawGrid_TitleStyle
,set_Grids_TDrawGrid_OnCheckboxToggled
,set_Grids_TDrawGrid_OnEditingDone
,set_Grids_TDrawGrid_OnGetCellHint
,set_Grids_TDrawGrid_OnGetCheckboxState
,set_Grids_TDrawGrid_OnSetCheckboxState
,set_Grids_TDrawGrid_OnUserCheckboxBitmap
,Grids_TDrawGrid_Create
,ExtCtrls_TCustomFlowPanel_Create
,get_ExtCtrls_TCustomFlowPanel_AutoWrap
,set_ExtCtrls_TCustomFlowPanel_AutoWrap
,ExtCtrls_TFlowPanelControlList_Create
,get_ExtCtrls_TFlowPanelControl_Control
,set_ExtCtrls_TFlowPanelControl_Control
,get_ExtCtrls_TFlowPanelControl_WrapAfter
,set_ExtCtrls_TFlowPanelControl_WrapAfter
,get_ExtCtrls_TFlowPanelControlList_Items
,set_ExtCtrls_TFlowPanelControlList_Items
,get_ExtCtrls_TCustomFlowPanel_ControlList
,set_ExtCtrls_TCustomFlowPanel_ControlList
,get_ExtCtrls_TCustomFlowPanel_FlowStyle
,set_ExtCtrls_TCustomFlowPanel_FlowStyle
,get_ExtCtrls_TCustomFlowPanel_FlowLayout
,set_ExtCtrls_TCustomFlowPanel_FlowLayout
,get_ExtCtrls_TFlowPanel_DragKind
,set_ExtCtrls_TFlowPanel_DragKind
,get_ExtCtrls_TFlowPanel_DragMode
,set_ExtCtrls_TFlowPanel_DragMode
,get_ExtCtrls_TFlowPanel_ParentFont
,set_ExtCtrls_TFlowPanel_ParentFont
,get_ExtCtrls_TFlowPanel_ParentShowHint
,set_ExtCtrls_TFlowPanel_ParentShowHint
,set_ExtCtrls_TFlowPanel_OnDblClick
,set_ExtCtrls_TFlowPanel_OnDragDrop
,set_ExtCtrls_TFlowPanel_OnDragOver
,set_ExtCtrls_TFlowPanel_OnEndDock
,set_ExtCtrls_TFlowPanel_OnEndDrag
,set_ExtCtrls_TFlowPanel_OnMouseDown
,set_ExtCtrls_TFlowPanel_OnMouseEnter
,set_ExtCtrls_TFlowPanel_OnMouseLeave
,set_ExtCtrls_TFlowPanel_OnMouseMove
,set_ExtCtrls_TFlowPanel_OnMouseUp
,set_ExtCtrls_TFlowPanel_OnStartDock
,set_ExtCtrls_TFlowPanel_OnStartDrag
,ExtCtrls_TFlowPanel_Create
,ExtCtrls_TCustomImage_Create
,get_ExtCtrls_TCustomImage_Canvas
,get_ExtCtrls_TCustomImage_AntialiasingMode
,set_ExtCtrls_TCustomImage_AntialiasingMode
,get_ExtCtrls_TCustomImage_Center
,set_ExtCtrls_TCustomImage_Center
,get_ExtCtrls_TCustomImage_KeepOriginXWhenClipped
,set_ExtCtrls_TCustomImage_KeepOriginXWhenClipped
,get_ExtCtrls_TCustomImage_KeepOriginYWhenClipped
,set_ExtCtrls_TCustomImage_KeepOriginYWhenClipped
,get_ExtCtrls_TCustomImage_Picture
,set_ExtCtrls_TCustomImage_Picture
,set_ExtCtrls_TCustomImage_OnMouseDown
,set_ExtCtrls_TCustomImage_OnMouseEnter
,set_ExtCtrls_TCustomImage_OnMouseLeave
,set_ExtCtrls_TCustomImage_OnMouseMove
,set_ExtCtrls_TCustomImage_OnMouseUp
,get_ExtCtrls_TCustomImage_Stretch
,set_ExtCtrls_TCustomImage_Stretch
,get_ExtCtrls_TCustomImage_StretchOutEnabled
,set_ExtCtrls_TCustomImage_StretchOutEnabled
,get_ExtCtrls_TCustomImage_StretchInEnabled
,set_ExtCtrls_TCustomImage_StretchInEnabled
,get_ExtCtrls_TCustomImage_Transparent
,set_ExtCtrls_TCustomImage_Transparent
,get_ExtCtrls_TCustomImage_Proportional
,set_ExtCtrls_TCustomImage_Proportional
,set_ExtCtrls_TCustomImage_OnPictureChanged
,get_ExtCtrls_TImage_DragMode
,set_ExtCtrls_TImage_DragMode
,set_ExtCtrls_TImage_OnDblClick
,set_ExtCtrls_TImage_OnDragDrop
,set_ExtCtrls_TImage_OnDragOver
,set_ExtCtrls_TImage_OnEndDrag
,set_ExtCtrls_TImage_OnPaint
,set_ExtCtrls_TImage_OnStartDrag
,get_ExtCtrls_TImage_ParentShowHint
,set_ExtCtrls_TImage_ParentShowHint
,ExtCtrls_TImage_Create
,ExtCtrls_TCustomLabeledEdit_Create
,ExtCtrls_TBoundLabel_Create
,get_ExtCtrls_TBoundLabel_FocusControl
,set_ExtCtrls_TBoundLabel_FocusControl
,get_ExtCtrls_TBoundLabel_DragMode
,set_ExtCtrls_TBoundLabel_DragMode
,get_ExtCtrls_TBoundLabel_ParentColor
,set_ExtCtrls_TBoundLabel_ParentColor
,get_ExtCtrls_TBoundLabel_ParentFont
,set_ExtCtrls_TBoundLabel_ParentFont
,get_ExtCtrls_TBoundLabel_ParentShowHint
,set_ExtCtrls_TBoundLabel_ParentShowHint
,get_ExtCtrls_TBoundLabel_ShowAccelChar
,set_ExtCtrls_TBoundLabel_ShowAccelChar
,get_ExtCtrls_TBoundLabel_Layout
,set_ExtCtrls_TBoundLabel_Layout
,get_ExtCtrls_TBoundLabel_WordWrap
,set_ExtCtrls_TBoundLabel_WordWrap
,set_ExtCtrls_TBoundLabel_OnDblClick
,set_ExtCtrls_TBoundLabel_OnDragDrop
,set_ExtCtrls_TBoundLabel_OnDragOver
,set_ExtCtrls_TBoundLabel_OnEndDrag
,set_ExtCtrls_TBoundLabel_OnMouseDown
,set_ExtCtrls_TBoundLabel_OnMouseEnter
,set_ExtCtrls_TBoundLabel_OnMouseLeave
,set_ExtCtrls_TBoundLabel_OnMouseMove
,set_ExtCtrls_TBoundLabel_OnMouseUp
,set_ExtCtrls_TBoundLabel_OnStartDrag
,get_ExtCtrls_TCustomLabeledEdit_EditLabel
,get_ExtCtrls_TCustomLabeledEdit_LabelPosition
,set_ExtCtrls_TCustomLabeledEdit_LabelPosition
,get_ExtCtrls_TCustomLabeledEdit_LabelSpacing
,set_ExtCtrls_TCustomLabeledEdit_LabelSpacing
,get_ExtCtrls_TLabeledEdit_AutoSelect
,set_ExtCtrls_TLabeledEdit_AutoSelect
,get_ExtCtrls_TLabeledEdit_DragMode
,set_ExtCtrls_TLabeledEdit_DragMode
,get_ExtCtrls_TLabeledEdit_ParentColor
,set_ExtCtrls_TLabeledEdit_ParentColor
,get_ExtCtrls_TLabeledEdit_ParentFont
,set_ExtCtrls_TLabeledEdit_ParentFont
,get_ExtCtrls_TLabeledEdit_ParentShowHint
,set_ExtCtrls_TLabeledEdit_ParentShowHint
,set_ExtCtrls_TLabeledEdit_OnDblClick
,set_ExtCtrls_TLabeledEdit_OnDragDrop
,set_ExtCtrls_TLabeledEdit_OnDragOver
,set_ExtCtrls_TLabeledEdit_OnEditingDone
,set_ExtCtrls_TLabeledEdit_OnEndDrag
,set_ExtCtrls_TLabeledEdit_OnMouseDown
,set_ExtCtrls_TLabeledEdit_OnMouseEnter
,set_ExtCtrls_TLabeledEdit_OnMouseLeave
,set_ExtCtrls_TLabeledEdit_OnMouseMove
,set_ExtCtrls_TLabeledEdit_OnMouseUp
,set_ExtCtrls_TLabeledEdit_OnStartDrag
,ExtCtrls_TLabeledEdit_Create
,MaskEdit_TCustomMaskEdit_Create
,get_MaskEdit_TCustomMaskEdit_Modified
,set_MaskEdit_TCustomMaskEdit_Modified
,get_MaskEdit_TMaskEdit_IsMasked
,get_MaskEdit_TMaskEdit_EditText
,set_MaskEdit_TMaskEdit_EditText
,get_MaskEdit_TMaskEdit_AutoSelect
,set_MaskEdit_TMaskEdit_AutoSelect
,get_MaskEdit_TMaskEdit_CharCase
,set_MaskEdit_TMaskEdit_CharCase
,get_MaskEdit_TMaskEdit_DragKind
,set_MaskEdit_TMaskEdit_DragKind
,get_MaskEdit_TMaskEdit_DragMode
,set_MaskEdit_TMaskEdit_DragMode
,get_MaskEdit_TMaskEdit_MaxLength
,set_MaskEdit_TMaskEdit_MaxLength
,get_MaskEdit_TMaskEdit_ParentColor
,set_MaskEdit_TMaskEdit_ParentColor
,get_MaskEdit_TMaskEdit_ParentFont
,set_MaskEdit_TMaskEdit_ParentFont
,get_MaskEdit_TMaskEdit_ParentShowHint
,set_MaskEdit_TMaskEdit_ParentShowHint
,set_MaskEdit_TMaskEdit_OnDblClick
,set_MaskEdit_TMaskEdit_OnDragDrop
,set_MaskEdit_TMaskEdit_OnDragOver
,set_MaskEdit_TMaskEdit_OnEditingDone
,set_MaskEdit_TMaskEdit_OnEndDock
,set_MaskEdit_TMaskEdit_OnEndDrag
,set_MaskEdit_TMaskEdit_OnMouseDown
,set_MaskEdit_TMaskEdit_OnMouseEnter
,set_MaskEdit_TMaskEdit_OnMouseLeave
,set_MaskEdit_TMaskEdit_OnMouseMove
,set_MaskEdit_TMaskEdit_OnMouseUp
,set_MaskEdit_TMaskEdit_OnStartDock
,set_MaskEdit_TMaskEdit_OnStartDrag
,get_MaskEdit_TMaskEdit_EditMask
,set_MaskEdit_TMaskEdit_EditMask
,MaskEdit_TMaskEdit_Create
,ExtCtrls_TNotebook_Create
,get_ExtCtrls_TNotebook_ActivePage
,ExtCtrls_TPage_Create
,get_ExtCtrls_TPage_PageIndex
,set_ExtCtrls_TPage_OnMouseDown
,set_ExtCtrls_TPage_OnMouseEnter
,set_ExtCtrls_TPage_OnMouseLeave
,set_ExtCtrls_TPage_OnMouseMove
,set_ExtCtrls_TPage_OnMouseUp
,get_ExtCtrls_TPage_ParentShowHint
,set_ExtCtrls_TPage_ParentShowHint
,get_ExtCtrls_TNotebook_ActivePageComponent
,get_ExtCtrls_TNotebook_Page
,get_ExtCtrls_TNotebook_PageCount
,get_ExtCtrls_TNotebook_PageIndex
,set_ExtCtrls_TNotebook_PageIndex
,get_ExtCtrls_TNotebook_Pages
,set_ExtCtrls_TNotebook_Pages
,get_ExtCtrls_TNotebook_DragMode
,set_ExtCtrls_TNotebook_DragMode
,set_ExtCtrls_TNotebook_OnDragDrop
,set_ExtCtrls_TNotebook_OnDragOver
,set_ExtCtrls_TNotebook_OnEndDrag
,set_ExtCtrls_TNotebook_OnMouseDown
,set_ExtCtrls_TNotebook_OnMouseEnter
,set_ExtCtrls_TNotebook_OnMouseLeave
,set_ExtCtrls_TNotebook_OnMouseMove
,set_ExtCtrls_TNotebook_OnMouseUp
,set_ExtCtrls_TNotebook_OnStartDrag
,ExtCtrls_TPaintBox_Create
,get_ExtCtrls_TPaintBox_DragMode
,set_ExtCtrls_TPaintBox_DragMode
,get_ExtCtrls_TPaintBox_ParentColor
,set_ExtCtrls_TPaintBox_ParentColor
,get_ExtCtrls_TPaintBox_ParentFont
,set_ExtCtrls_TPaintBox_ParentFont
,get_ExtCtrls_TPaintBox_ParentShowHint
,set_ExtCtrls_TPaintBox_ParentShowHint
,set_ExtCtrls_TPaintBox_OnDblClick
,set_ExtCtrls_TPaintBox_OnDragDrop
,set_ExtCtrls_TPaintBox_OnDragOver
,set_ExtCtrls_TPaintBox_OnEndDrag
,set_ExtCtrls_TPaintBox_OnMouseDown
,set_ExtCtrls_TPaintBox_OnMouseEnter
,set_ExtCtrls_TPaintBox_OnMouseLeave
,set_ExtCtrls_TPaintBox_OnMouseMove
,set_ExtCtrls_TPaintBox_OnMouseUp
,set_ExtCtrls_TPaintBox_OnPaint
,set_ExtCtrls_TPaintBox_OnStartDrag
,PairSplitter_TCustomPairSplitter_Create
,PairSplitter_TPairSplitterSide_Create
,get_PairSplitter_TPairSplitterSide_Splitter
,set_PairSplitter_TPairSplitterSide_OnMouseDown
,set_PairSplitter_TPairSplitterSide_OnMouseEnter
,set_PairSplitter_TPairSplitterSide_OnMouseLeave
,set_PairSplitter_TPairSplitterSide_OnMouseMove
,set_PairSplitter_TPairSplitterSide_OnMouseUp
,get_PairSplitter_TPairSplitterSide_ParentShowHint
,set_PairSplitter_TPairSplitterSide_ParentShowHint
,get_PairSplitter_TCustomPairSplitter_Sides
,get_PairSplitter_TCustomPairSplitter_SplitterType
,set_PairSplitter_TCustomPairSplitter_SplitterType
,get_PairSplitter_TCustomPairSplitter_Position
,set_PairSplitter_TCustomPairSplitter_Position
,set_PairSplitter_TPairSplitter_OnMouseDown
,set_PairSplitter_TPairSplitter_OnMouseEnter
,set_PairSplitter_TPairSplitter_OnMouseLeave
,set_PairSplitter_TPairSplitter_OnMouseMove
,set_PairSplitter_TPairSplitter_OnMouseUp
,get_PairSplitter_TPairSplitter_ParentShowHint
,set_PairSplitter_TPairSplitter_ParentShowHint
,PairSplitter_TPairSplitter_Create
,Forms_TScrollBox_Create
,get_Forms_TScrollBox_AutoScroll
,set_Forms_TScrollBox_AutoScroll
,get_Forms_TScrollBox_DragKind
,set_Forms_TScrollBox_DragKind
,get_Forms_TScrollBox_DragMode
,set_Forms_TScrollBox_DragMode
,get_Forms_TScrollBox_ParentColor
,set_Forms_TScrollBox_ParentColor
,get_Forms_TScrollBox_ParentFont
,set_Forms_TScrollBox_ParentFont
,get_Forms_TScrollBox_ParentShowHint
,set_Forms_TScrollBox_ParentShowHint
,set_Forms_TScrollBox_OnDblClick
,set_Forms_TScrollBox_OnDragDrop
,set_Forms_TScrollBox_OnDragOver
,set_Forms_TScrollBox_OnEndDock
,set_Forms_TScrollBox_OnEndDrag
,set_Forms_TScrollBox_OnMouseDown
,set_Forms_TScrollBox_OnMouseEnter
,set_Forms_TScrollBox_OnMouseLeave
,set_Forms_TScrollBox_OnMouseMove
,set_Forms_TScrollBox_OnMouseUp
,set_Forms_TScrollBox_OnStartDock
,set_Forms_TScrollBox_OnStartDrag
,ExtCtrls_TShape_Create
,get_ExtCtrls_TShape_Brush
,set_ExtCtrls_TShape_Brush
,get_ExtCtrls_TShape_DragKind
,set_ExtCtrls_TShape_DragKind
,get_ExtCtrls_TShape_DragMode
,set_ExtCtrls_TShape_DragMode
,get_ExtCtrls_TShape_ParentShowHint
,set_ExtCtrls_TShape_ParentShowHint
,get_ExtCtrls_TShape_Pen
,set_ExtCtrls_TShape_Pen
,set_ExtCtrls_TShape_OnDragDrop
,set_ExtCtrls_TShape_OnDragOver
,set_ExtCtrls_TShape_OnEndDock
,set_ExtCtrls_TShape_OnEndDrag
,set_ExtCtrls_TShape_OnMouseDown
,set_ExtCtrls_TShape_OnMouseEnter
,set_ExtCtrls_TShape_OnMouseLeave
,set_ExtCtrls_TShape_OnMouseMove
,set_ExtCtrls_TShape_OnMouseUp
,set_ExtCtrls_TShape_OnPaint
,set_ExtCtrls_TShape_OnStartDock
,set_ExtCtrls_TShape_OnStartDrag
,get_ExtCtrls_TShape_Shape
,set_ExtCtrls_TShape_Shape
,Buttons_TCustomSpeedButton_Create
,get_Buttons_TCustomSpeedButton_AllowAllUp
,set_Buttons_TCustomSpeedButton_AllowAllUp
,get_Buttons_TCustomSpeedButton_Down
,set_Buttons_TCustomSpeedButton_Down
,get_Buttons_TCustomSpeedButton_Flat
,set_Buttons_TCustomSpeedButton_Flat
,get_Buttons_TCustomSpeedButton_Glyph
,set_Buttons_TCustomSpeedButton_Glyph
,get_Buttons_TCustomSpeedButton_GroupIndex
,set_Buttons_TCustomSpeedButton_GroupIndex
,get_Buttons_TCustomSpeedButton_Layout
,set_Buttons_TCustomSpeedButton_Layout
,get_Buttons_TCustomSpeedButton_Margin
,set_Buttons_TCustomSpeedButton_Margin
,get_Buttons_TCustomSpeedButton_NumGlyphs
,set_Buttons_TCustomSpeedButton_NumGlyphs
,get_Buttons_TCustomSpeedButton_ShowAccelChar
,set_Buttons_TCustomSpeedButton_ShowAccelChar
,get_Buttons_TCustomSpeedButton_ShowCaption
,set_Buttons_TCustomSpeedButton_ShowCaption
,get_Buttons_TCustomSpeedButton_Spacing
,set_Buttons_TCustomSpeedButton_Spacing
,get_Buttons_TCustomSpeedButton_Transparent
,set_Buttons_TCustomSpeedButton_Transparent
,set_Buttons_TSpeedButton_OnDblClick
,set_Buttons_TSpeedButton_OnMouseDown
,set_Buttons_TSpeedButton_OnMouseEnter
,set_Buttons_TSpeedButton_OnMouseLeave
,set_Buttons_TSpeedButton_OnMouseMove
,set_Buttons_TSpeedButton_OnMouseUp
,set_Buttons_TSpeedButton_OnPaint
,get_Buttons_TSpeedButton_ParentFont
,set_Buttons_TSpeedButton_ParentFont
,get_Buttons_TSpeedButton_ParentShowHint
,set_Buttons_TSpeedButton_ParentShowHint
,Buttons_TSpeedButton_Create
,ExtCtrls_TCustomSplitter_Create
,get_ExtCtrls_TCustomSplitter_ResizeControl
,set_ExtCtrls_TCustomSplitter_ResizeControl
,get_ExtCtrls_TCustomSplitter_AutoSnap
,set_ExtCtrls_TCustomSplitter_AutoSnap
,get_ExtCtrls_TCustomSplitter_Beveled
,set_ExtCtrls_TCustomSplitter_Beveled
,get_ExtCtrls_TCustomSplitter_MinSize
,set_ExtCtrls_TCustomSplitter_MinSize
,set_ExtCtrls_TCustomSplitter_OnCanOffset
,set_ExtCtrls_TCustomSplitter_OnCanResize
,set_ExtCtrls_TCustomSplitter_OnMoved
,get_ExtCtrls_TCustomSplitter_ResizeAnchor
,set_ExtCtrls_TCustomSplitter_ResizeAnchor
,get_ExtCtrls_TCustomSplitter_ResizeStyle
,set_ExtCtrls_TCustomSplitter_ResizeStyle
,get_ExtCtrls_TSplitter_ParentColor
,set_ExtCtrls_TSplitter_ParentColor
,get_ExtCtrls_TSplitter_ParentShowHint
,set_ExtCtrls_TSplitter_ParentShowHint
,ExtCtrls_TSplitter_Create
,StdCtrls_TCustomStaticText_Create
,get_StdCtrls_TCustomStaticText_Alignment
,set_StdCtrls_TCustomStaticText_Alignment
,get_StdCtrls_TCustomStaticText_BorderStyle
,set_StdCtrls_TCustomStaticText_BorderStyle
,get_StdCtrls_TCustomStaticText_FocusControl
,set_StdCtrls_TCustomStaticText_FocusControl
,get_StdCtrls_TCustomStaticText_ShowAccelChar
,set_StdCtrls_TCustomStaticText_ShowAccelChar
,get_StdCtrls_TCustomStaticText_Transparent
,set_StdCtrls_TCustomStaticText_Transparent
,get_StdCtrls_TStaticText_DragKind
,set_StdCtrls_TStaticText_DragKind
,get_StdCtrls_TStaticText_DragMode
,set_StdCtrls_TStaticText_DragMode
,set_StdCtrls_TStaticText_OnDblClick
,set_StdCtrls_TStaticText_OnDragDrop
,set_StdCtrls_TStaticText_OnDragOver
,set_StdCtrls_TStaticText_OnEndDrag
,set_StdCtrls_TStaticText_OnMouseDown
,set_StdCtrls_TStaticText_OnMouseEnter
,set_StdCtrls_TStaticText_OnMouseLeave
,set_StdCtrls_TStaticText_OnMouseMove
,set_StdCtrls_TStaticText_OnMouseUp
,set_StdCtrls_TStaticText_OnStartDrag
,get_StdCtrls_TStaticText_ParentFont
,set_StdCtrls_TStaticText_ParentFont
,get_StdCtrls_TStaticText_ParentColor
,set_StdCtrls_TStaticText_ParentColor
,get_StdCtrls_TStaticText_ParentShowHint
,set_StdCtrls_TStaticText_ParentShowHint
,StdCtrls_TStaticText_Create
,Grids_TCustomStringGrid_Create
,get_Grids_TCustomStringGrid_Cells
,set_Grids_TCustomStringGrid_Cells
,get_Grids_TCustomStringGrid_Cols
,set_Grids_TCustomStringGrid_Cols
,get_Grids_TCustomStringGrid_ExtendedSelect
,set_Grids_TCustomStringGrid_ExtendedSelect
,get_Grids_TCustomStringGrid_Objects
,set_Grids_TCustomStringGrid_Objects
,get_Grids_TCustomStringGrid_Rows
,set_Grids_TCustomStringGrid_Rows
,get_Grids_TStringGrid_Modified
,set_Grids_TStringGrid_Modified
,get_Grids_TStringGrid_InplaceEditor
,get_Grids_TStringGrid_AutoEdit
,set_Grids_TStringGrid_AutoEdit
,get_Grids_TStringGrid_CellHintPriority
,set_Grids_TStringGrid_CellHintPriority
,get_Grids_TStringGrid_ColumnClickSorts
,set_Grids_TStringGrid_ColumnClickSorts
,get_Grids_TStringGrid_DragKind
,set_Grids_TStringGrid_DragKind
,get_Grids_TStringGrid_DragMode
,set_Grids_TStringGrid_DragMode
,get_Grids_TStringGrid_HeaderHotZones
,set_Grids_TStringGrid_HeaderHotZones
,get_Grids_TStringGrid_HeaderPushZones
,set_Grids_TStringGrid_HeaderPushZones
,get_Grids_TStringGrid_MouseWheelOption
,set_Grids_TStringGrid_MouseWheelOption
,get_Grids_TStringGrid_ParentColor
,set_Grids_TStringGrid_ParentColor
,get_Grids_TStringGrid_ParentFont
,set_Grids_TStringGrid_ParentFont
,get_Grids_TStringGrid_RangeSelectMode
,set_Grids_TStringGrid_RangeSelectMode
,get_Grids_TStringGrid_TitleFont
,set_Grids_TStringGrid_TitleFont
,get_Grids_TStringGrid_TitleImageList
,set_Grids_TStringGrid_TitleImageList
,get_Grids_TStringGrid_TitleStyle
,set_Grids_TStringGrid_TitleStyle
,set_Grids_TStringGrid_OnCellProcess
,set_Grids_TStringGrid_OnCheckboxToggled
,set_Grids_TStringGrid_OnEditingDone
,set_Grids_TStringGrid_OnGetCellHint
,set_Grids_TStringGrid_OnGetCheckboxState
,set_Grids_TStringGrid_OnSetCheckboxState
,set_Grids_TStringGrid_OnTopLeftChanged
,set_Grids_TStringGrid_OnUserCheckboxBitmap
,set_Grids_TStringGrid_OnValidateEntry
,Grids_TStringGrid_Create
,ExtCtrls_TCustomTrayIcon_Create
,get_ExtCtrls_TCustomTrayIcon_Animate
,set_ExtCtrls_TCustomTrayIcon_Animate
,get_ExtCtrls_TCustomTrayIcon_BalloonFlags
,set_ExtCtrls_TCustomTrayIcon_BalloonFlags
,get_ExtCtrls_TCustomTrayIcon_BalloonHint
,set_ExtCtrls_TCustomTrayIcon_BalloonHint
,get_ExtCtrls_TCustomTrayIcon_BalloonTimeout
,set_ExtCtrls_TCustomTrayIcon_BalloonTimeout
,get_ExtCtrls_TCustomTrayIcon_BalloonTitle
,set_ExtCtrls_TCustomTrayIcon_BalloonTitle
,get_ExtCtrls_TCustomTrayIcon_Canvas
,get_ExtCtrls_TCustomTrayIcon_PopUpMenu
,set_ExtCtrls_TCustomTrayIcon_PopUpMenu
,get_ExtCtrls_TCustomTrayIcon_Icon
,set_ExtCtrls_TCustomTrayIcon_Icon
,get_ExtCtrls_TCustomTrayIcon_Icons
,set_ExtCtrls_TCustomTrayIcon_Icons
,get_ExtCtrls_TCustomTrayIcon_Hint
,set_ExtCtrls_TCustomTrayIcon_Hint
,get_ExtCtrls_TCustomTrayIcon_ShowIcon
,set_ExtCtrls_TCustomTrayIcon_ShowIcon
,get_ExtCtrls_TCustomTrayIcon_Visible
,set_ExtCtrls_TCustomTrayIcon_Visible
,set_ExtCtrls_TCustomTrayIcon_OnClick
,set_ExtCtrls_TCustomTrayIcon_OnDblClick
,set_ExtCtrls_TCustomTrayIcon_OnMouseDown
,set_ExtCtrls_TCustomTrayIcon_OnMouseUp
,set_ExtCtrls_TCustomTrayIcon_OnMouseMove
,set_ExtCtrls_TCustomTrayIcon_OnPaint
,ExtCtrls_TTrayIcon_Create
,ValEdit_TValueListEditor_Create
,get_ValEdit_TValueListEditor_Modified
,set_ValEdit_TValueListEditor_Modified
,get_ValEdit_TValueListEditor_Keys
,set_ValEdit_TValueListEditor_Keys
,get_ValEdit_TItemProp_EditMask
,set_ValEdit_TItemProp_EditMask
,get_ValEdit_TItemProp_EditStyle
,set_ValEdit_TItemProp_EditStyle
,get_ValEdit_TItemProp_KeyDesc
,set_ValEdit_TItemProp_KeyDesc
,get_ValEdit_TItemProp_PickList
,set_ValEdit_TItemProp_PickList
,get_ValEdit_TItemProp_MaxLength
,set_ValEdit_TItemProp_MaxLength
,get_ValEdit_TItemProp_ReadOnly
,set_ValEdit_TItemProp_ReadOnly
,get_ValEdit_TValueListEditor_AutoEdit
,set_ValEdit_TValueListEditor_AutoEdit
,get_ValEdit_TValueListEditor_DragKind
,set_ValEdit_TValueListEditor_DragKind
,get_ValEdit_TValueListEditor_DragMode
,set_ValEdit_TValueListEditor_DragMode
,get_ValEdit_TValueListEditor_HeaderHotZones
,set_ValEdit_TValueListEditor_HeaderHotZones
,get_ValEdit_TValueListEditor_HeaderPushZones
,set_ValEdit_TValueListEditor_HeaderPushZones
,get_ValEdit_TValueListEditor_MouseWheelOption
,set_ValEdit_TValueListEditor_MouseWheelOption
,get_ValEdit_TValueListEditor_ParentColor
,set_ValEdit_TValueListEditor_ParentColor
,get_ValEdit_TValueListEditor_ParentFont
,set_ValEdit_TValueListEditor_ParentFont
,get_ValEdit_TValueListEditor_RowCount
,set_ValEdit_TValueListEditor_RowCount
,get_ValEdit_TValueListEditor_TitleFont
,set_ValEdit_TValueListEditor_TitleFont
,get_ValEdit_TValueListEditor_TitleImageList
,set_ValEdit_TValueListEditor_TitleImageList
,get_ValEdit_TValueListEditor_TitleStyle
,set_ValEdit_TValueListEditor_TitleStyle
,set_ValEdit_TValueListEditor_OnCheckboxToggled
,set_ValEdit_TValueListEditor_OnEditingDone
,set_ValEdit_TValueListEditor_OnTopLeftChanged
,set_ValEdit_TValueListEditor_OnUserCheckboxBitmap
,set_ValEdit_TValueListEditor_OnValidateEntry
,get_ValEdit_TValueListEditor_DisplayOptions
,set_ValEdit_TValueListEditor_DisplayOptions
,get_ValEdit_TValueListEditor_DropDownRows
,set_ValEdit_TValueListEditor_DropDownRows
,get_ValEdit_TValueListEditor_KeyOptions
,set_ValEdit_TValueListEditor_KeyOptions
,get_ValEdit_TValueListEditor_Options
,set_ValEdit_TValueListEditor_Options
,get_Classes_TStringList_Sorted
,set_Classes_TStringList_Sorted
,get_Classes_TStringList_CaseSensitive
,set_Classes_TStringList_CaseSensitive
,set_Classes_TStringList_OnChange
,set_Classes_TStringList_OnChanging
,get_Classes_TStringList_OwnsObjects
,set_Classes_TStringList_OwnsObjects
,get_Classes_TStringList_SortStyle
,set_Classes_TStringList_SortStyle
,get_ValEdit_TValueListEditor_Strings
,set_ValEdit_TValueListEditor_Strings
,get_ValEdit_TValueListEditor_TitleCaptions
,set_ValEdit_TValueListEditor_TitleCaptions
,set_ValEdit_TValueListEditor_OnGetPickList
,set_ValEdit_TValueListEditor_OnStringsChange
,set_ValEdit_TValueListEditor_OnStringsChanging; 
begin
end.
