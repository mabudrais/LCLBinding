program project1;
   uses Classes, SysUtils,Interfaces,Forms,LResources2,StdCtrls,Menus;
type

  { Loadlfm }

  Loadlfm = class
    function LoadFromText(FileName: string): PChar;
  private
    procedure OnFindClass(Reader: TReader; const AClassName: string;
      var ComponentClass: TComponentClass);
  end;
  TMAp=class(TApplication)
    private
    FCreatingForm:TForm;
    end;

function Loadlfm.LoadFromText(FileName: string): PChar;
var
  strlist: TStringList;
  NewComponent: TComponent;
  AStream: TMemoryStream;
  ststream: TStringStream;
  txtf: TextFile;
  cntentstr, temp, ObjectSData: string;
  P,MF,AMF:Pointer;
begin
  ObjectSData := '  ';
  strlist := TStringList.Create;
  strlist.LoadFromFile(filename);
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
  TForm(NewComponent).Show;

  Application.ForceUpdateMainForm(TForm(NewComponent));
  TForm(NewComponent).HandleNeeded;
  Result := PChar(ObjectSData);
  strlist.Free;
end;

procedure Loadlfm.OnFindClass(Reader: TReader; const AClassName: string;
  var ComponentClass: TComponentClass);
begin
    if CompareText(AClassName, 'TGroupBox') = 0 then
    ComponentClass := TGroupBox
  else if CompareText(AClassName, 'TCheckBox') = 0 then
    ComponentClass := TCheckBox
  else if CompareText(AClassName, 'TRadioButton') = 0 then
    ComponentClass := TRadioButton
  else if CompareText(AClassName, 'TForm') = 0 then
    ComponentClass := TForm
  else if CompareText(AClassName, 'TButton') = 0 then
    ComponentClass := TButton
  else if CompareText(AClassName, 'TEdit') = 0 then
    ComponentClass := TEdit
  else if CompareText(AClassName, 'TLabel') = 0 then
    ComponentClass := TLabel
  else if CompareText(AClassName, 'TMemo') = 0 then
    ComponentClass := TMemo
  else if CompareText(AClassName, 'TMainMenu') = 0 then
    ComponentClass := TMainMenu
  else if CompareText(AClassName, 'TMenuItem') = 0 then
    ComponentClass := TMenuItem
  else if CompareText(AClassName, 'TPopupMenu') = 0 then
    ComponentClass := TPopupMenu;
end;

var
   LFM: Loadlfm;
   F: TForm;
   p: Pointer;
 begin
  Application.Initialize;
  p:=Application;
    LFM :=Loadlfm.Create;
    LFM.LoadFromText(
      'G:\dev\temp\lclbinding2\parser\generated\python\test\lfmtest\unit1.lfm');
   // Application.UpdateMainForm(F);
    Lfm.Free;
    Application.Run;
end.

