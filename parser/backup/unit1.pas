unit Unit1;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, FileUtil, Forms, Controls, Graphics, Dialogs, StdCtrls,
  Grids, contnrs, pasfileunit, Parserunit, Parser2Unit, dateutils, LResources,Unit3;

type

  { TForm1 }

  TForm1 = class(TForm)
    FileMemo: TMemo;
    ClassMemo: TMemo;
    Label1: TLabel;
    ParseButton: TButton;
    StringGrid1: TStringGrid;
    ErrorMemo: TMemo;
    Button1: TButton;
    Button2: TButton;
    ClassNameMemo: TMemo;
    ClassNamesButton: TButton;
    procedure ParseButtonClick(Sender: TObject);
    procedure FormCreate(Sender: TObject);
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
    procedure ClassNamesButtonClick(Sender: TObject);
  private
    LCLParser: TLCLParser;
    P2: TLCLParser2;
  public
    function loadfles(const LCLPath: string): TObjectList;

  end;

var
  Form1: TForm1;

implementation

{$R *.lfm}
uses PythonUnit;

{ TForm1 }

procedure TForm1.ParseButtonClick(Sender: TObject);
var
  LCLPath: string;
  TargetFiles: TObjectList;
  TargetFileName, TargetFileName2: TStringList;
  k: integer;
begin
 // TForm.Create();
  LCLPath := 'G:\dev\temp\lclbinding2\parser\targetfile\';
  TargetFileName := FindAllFiles(LCLPath, '', False);
  TargetFileName2 := TStringList.Create;
  for k := 0 to TargetFileName.Count - 1 do
  begin
    if not TargetFileName[k].Contains('.inc') then
      TargetFileName2.add(ExtractFileName(TargetFileName[k]));
  end;
  FileMemo.Lines.Clear;
  FileMemo.Lines.AddStrings(TargetFileName2);
  TargetFiles := loadfles(LCLPath);
end;

function TForm1.loadfles(const LCLPath: string): TObjectList;
var
  K: integer;
  TargetFiles: TObjectList;
  t1: TDateTime;
begin
  P2 := TLCLParser2.Create(FileMemo.Lines, ClassMemo.Lines, LCLPath);
  ShowMessage('parser2 end');
  //Form1.OnClick:=;
 {
  TargetFiles := TObjectList.Create;
  for K := 0 to FileMemo.Lines.Count - 1 do
  begin
    TargetFiles.Add(TPasFile.Create(LCLPath + FileMemo.Lines[k]));
  end;
  LCLParser := TLCLParser.Create(TargetFiles, ClassMemo.Lines);
  t1 := Now;
  LCLParser.Parse(p2.ParsedFiles);
  Label1.Caption := 'parse time ' + MinutesBetween(t1, Now).ToString() + ' m';
  ErrorMemo.Lines.AddStrings(LCLParser.ErrorMsg);
  //SetCursorPos(50,50);         }
end;

procedure TForm1.FormCreate(Sender: TObject);
begin

end;

procedure TForm1.Button1Click(Sender: TObject);
var
  py: TPythonLang;
begin
  py := TPythonLang.Create('generated\python');
  py.GenerateBinding(p2.ParsedObject);
  py.SaveFiles;
end;

procedure TForm1.Button2Click(Sender: TObject);
begin
  Unit3.Form2.Show;
end;

procedure TForm1.ClassNamesButtonClick(Sender: TObject);
var
  e: String;
  k: Integer;
begin
  ClassNameMemo.Clear;
  for k:=0 to ClassMemo.Lines.Count-1 do
  begin
    ClassNameMemo.Lines.Add(e+' if CompareText(AClassName, '''+Trim(ClassMemo.Lines[k])+''') = 0 then');
    ClassNameMemo.Lines.Add('ComponentClass := '+Trim(ClassMemo.Lines[k]));
    e:='else';
  end;
end;

end.
