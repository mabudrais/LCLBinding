unit Unit1;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs;

type

  { TForm1 }

  TForm1 = class(TForm)
    procedure FormCreate(Sender: TObject);
  private

  public

  end;
  TB=class
    num3:Integer;
  end;

   TA=class
     num1,Num2:Integer;
     b:TB;
   end;

var
  Form1: TForm1;

implementation

{$R *.lfm}

{ TForm1 }

procedure TForm1.FormCreate(Sender: TObject);
var
  A: TA;
  PA,PB,PNum,PNum2,PAB:Pointer;
   def1, def2:Integer;
   pint:PInteger;
   B: TB;
begin
  A:=TA.Create;
  B:=TB.Create;
  PB:=B;
  a.b:=b;
  a.Num2:=7777;
  PA:=A;
  PAB:=Pointer((PA+12)^);
  pint:=pa+12;
  def1:=pint^;
  PNum:=@A.num1;
  PNum2:=@a.Num2;
  def1:=PNum-PA;
  def2:=PNum2-PNum;

end;

end.

