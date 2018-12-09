unit Unit3;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, FileUtil, LvlGraphCtrl, Forms, Controls, Graphics, Dialogs,
  StdCtrls;

type

  { TForm2 }

  TForm2 = class(TForm)
    LvlGraphControl1: TLvlGraphControl;
    Memo1: TMemo;
    Button1: TButton;
    Memo2: TMemo;
    OrderButton: TButton;
    procedure Button1Click(Sender: TObject);
    procedure LvlGraphControl1SelectionChanged(Sender: TObject);
    procedure OrderButtonClick(Sender: TObject);
  private

  public

  end;

var
  Form2: TForm2;

implementation

{$R *.lfm}

{ TForm2 }

procedure TForm2.Button1Click(Sender: TObject);
var
  L, Clname, parenclass: string;
  k: integer;
  p1, p2: SizeInt;
begin
  Memo1.Lines.LoadFromFile(
    'G:\dev\temp\lclbinding2\parser\generated\python\stdctrls.py');
  Memo2.Clear;
  for k := 0 to Memo1.Lines.Count - 1 do
  begin
    L := Memo1.Lines[k];
    if l.StartsWith('class') then
    begin
      p1 := Pos('(', l);
      p2 := Pos(')', l);
      Clname := Trim(Copy(l, 6, p1 - 6));
      parenclass := trim(Copy(l, p1 + 1, p2 - p1 - 1));
      Memo2.Append(Clname + ',' + parenclass);
      LvlGraphControl1.Graph.GetEdge(Clname, parenclass, True);
    end;
  end;
end;

procedure TForm2.LvlGraphControl1SelectionChanged(Sender: TObject);
var
  k: integer;
begin
  //Form2.Caption:= LvlGraphControl1.Graph.LevelCount.ToString();
  Form2.Caption := LvlGraphControl1.Graph.Levels[2].Count.ToString();
  for k := 0 to LvlGraphControl1.Graph.Levels[2].Count - 1 do
  begin
    // LvlGraphControl1.Graph.Levels[2].Nodes[k].Caption;
  end;
end;

procedure TForm2.OrderButtonClick(Sender: TObject);
var
  k, m, n: integer;
  CN, PlN: TStringList;
  Cpn, tcn, L: string;
  p1, p2: SizeInt;
begin
  PlN := TStringList.Create;
  CN := TStringList.Create;
  Memo2.Clear;
  //get class name
  for k := 0 to Memo1.Lines.Count - 1 do
  begin
    L := Memo1.Lines[k];
    if l.StartsWith('class') then
    begin
      p1 := Pos('(', l);
      p2 := Pos(')', l);
      CN.Add(Trim(Copy(l, 6, p1 - 6)));
      PlN.Add(trim(Copy(l, p1 + 1, p2 - p1 - 1)));
    end;
  end;
  for n := 0 to 50 do
  begin
    for k := 0 to cn.Count - 2 do
    begin
      Cpn := PlN[k];
      for m := k + 1 to cn.Count - 1 do
      begin
        if Cpn = CN[m] then
        begin
          CN.Exchange(m, k);
          PlN.Exchange(m, k);
        end;
      end;
    end;
  end;

  for k := 0 to cn.Count - 1 do
  begin
    Memo2.Append(cn[k] + '(' + PlN[k] + ')');
  end;
end;

end.
