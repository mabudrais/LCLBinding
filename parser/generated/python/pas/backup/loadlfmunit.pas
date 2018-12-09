unit Loadlfmunit;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, LResources2, StdCtrls, Menus,ExtCtrls,Buttons, CheckLst,GraphType,ImgList,Dialogs,
   MaskEdit,  Grids, PairSplitter, ColorBox,
  ValEdit;

type

  { Loadlfm }

  Loadlfm = class
    function LoadFromText(FileName, FormName: string): PChar;
  private
    procedure OnFindClass(Reader: TReader; const AClassName: string;
      var ComponentClass: TComponentClass);
  end;

implementation

{ Loadlfm }
procedure Loadlfm.OnFindClass(Reader: TReader; const AClassName: string;
  var ComponentClass: TComponentClass);
begin
   if CompareText(AClassName, 'TForm') = 0 then
ComponentClass := TForm
else if CompareText(AClassName, 'TMainMenu') = 0 then
ComponentClass := TMainMenu
else if CompareText(AClassName, 'TPanel') = 0 then
ComponentClass := TPanel
else if CompareText(AClassName, 'TPopupMenu') = 0 then
ComponentClass := TPopupMenu
else if CompareText(AClassName, 'TButton') = 0 then
ComponentClass := TButton
else if CompareText(AClassName, 'TRadioButton') = 0 then
ComponentClass := TRadioButton
else if CompareText(AClassName, 'TCheckBox') = 0 then
ComponentClass := TCheckBox
else if CompareText(AClassName, 'TToggleBox') = 0 then
ComponentClass := TToggleBox
else if CompareText(AClassName, 'TComboBox') = 0 then
ComponentClass := TComboBox
else if CompareText(AClassName, 'TEdit') = 0 then
ComponentClass := TEdit
else if CompareText(AClassName, 'TMemo') = 0 then
ComponentClass := TMemo
else if CompareText(AClassName, 'TGroupBox') = 0 then
ComponentClass := TGroupBox
else if CompareText(AClassName, 'TLabel') = 0 then
ComponentClass := TLabel
else if CompareText(AClassName, 'TListBox') = 0 then
ComponentClass := TListBox
else if CompareText(AClassName, 'TScrollBar') = 0 then
ComponentClass := TScrollBar
else if CompareText(AClassName, 'TApplicationProperties') = 0 then
ComponentClass := TApplicationProperties
else if CompareText(AClassName, 'TBevel') = 0 then
ComponentClass := TBevel
else if CompareText(AClassName, 'TBitBtn') = 0 then
ComponentClass := TBitBtn
else if CompareText(AClassName, 'TCheckListBox') = 0 then
ComponentClass := TCheckListBox
else if CompareText(AClassName, 'TColorBox') = 0 then
ComponentClass := TColorBox
else if CompareText(AClassName, 'TColorListBox') = 0 then
ComponentClass := TColorListBox
else if CompareText(AClassName, 'TControlBar') = 0 then
ComponentClass := TControlBar
else if CompareText(AClassName, 'TDrawGrid') = 0 then
ComponentClass := TDrawGrid
else if CompareText(AClassName, 'TFlowPanel') = 0 then
ComponentClass := TFlowPanel
else if CompareText(AClassName, 'TImage') = 0 then
ComponentClass := TImage
else if CompareText(AClassName, 'TLabeledEdit') = 0 then
ComponentClass := TLabeledEdit
else if CompareText(AClassName, 'TMaskEdit') = 0 then
ComponentClass := TMaskEdit
else if CompareText(AClassName, 'TNotebook') = 0 then
ComponentClass := TNotebook
else if CompareText(AClassName, 'TPaintBox') = 0 then
ComponentClass := TPaintBox
else if CompareText(AClassName, 'TPairSplitter') = 0 then
ComponentClass := TPairSplitter
else if CompareText(AClassName, 'TPairSplitterSide') = 0 then
ComponentClass := TPairSplitterSide
else if CompareText(AClassName, 'TPairSplitterSide') = 0 then
ComponentClass := TPairSplitterSide
else if CompareText(AClassName, 'TScrollBox') = 0 then
ComponentClass := TScrollBox
else if CompareText(AClassName, 'TShape') = 0 then
ComponentClass := TShape
else if CompareText(AClassName, 'TSpeedButton') = 0 then
ComponentClass := TSpeedButton
else if CompareText(AClassName, 'TSplitter') = 0 then
ComponentClass := TSplitter
else if CompareText(AClassName, 'TStaticText') = 0 then
ComponentClass := TStaticText
else if CompareText(AClassName, 'TStringGrid') = 0 then
ComponentClass := TStringGrid
else if CompareText(AClassName, 'TTrayIcon') = 0 then
ComponentClass := TTrayIcon
else if CompareText(AClassName, 'TValueListEditor') = 0 then
ComponentClass := TValueListEditor;
end;

function Loadlfm.LoadFromText(FileName,FormName: string): PChar;
var
  strlist: TStringList;
  NewComponent: TComponent;
  AStream: TMemoryStream;
  ststream: TStringStream;
  txtf: TextFile;
  cntentstr, temp: string;
begin
  ObjectSData := '';
  strlist := TStringList.Create;
  strlist.LoadFromFile(filename);
  strlist[0]:=StringReplace(strlist[0], FormName, 'TForm', [rfReplaceAll]);
 // strlist.SaveToFile('Temp.lfm');
  try
    //cntentstr := 'object Form22: TForm'#13#10'  Left = 229'#13#10'  Height = 393'#13#10'  Top = 130'#13#10'  Width = 668'#13#10'  Caption = ''Form1'''#13#10'  ClientHeight = 393'#13#10'  ClientWidth = 668'#13#10'  LCLVersion = ''1.2.6.0'''#13#10'  object Button1: TButton'#13#10'    Left = 494'#13#10'    Height = 25'#13#10'    Top = 97'#13#10'    Width = 75'#13#10'    Caption = ''Button1'''#13#10'    TabOrder = 1'#13#10'  end'#13#10'end'#13#10;
    cntentstr := strlist.Text;
    //AStream := TMemoryStream.Create;
    ststream := TStringStream.Create(cntentstr);
    // ReadStreamFromString(AStream);

    NewComponent := nil;

    // ReadComponentFromBinaryStream(AStream,NewComponent,
    //                          @OnFindClass,DestinationGroupBox);
    ReadComponentFromTextStream(ststream, NewComponent, @OnFindClass);
    // ShowMessage('oo2');
  finally
    ststream.Free;
  end;
  Application.ForceUpdateMainForm(TForm(NewComponent));
  TForm(NewComponent).Show;
  Result := PChar(ObjectSData);
  strlist.Free;

end;

end.
