program project1;

{$mode objfpc}{$H+}

uses
  {$IFDEF UNIX}{$IFDEF UseCThreads}
  cthreads,
  {$ENDIF}{$ENDIF}
  Interfaces, // this includes the LCL widgetset
  Forms, Unit1
  { you can add units after this };

{$R *.res}
 var
   p,pf,CP,APtype:Pointer;
   Asize, k: Integer;
begin
  RequireDerivedFormResource:=True;
  Application.Scaled:=True;
  Application.Initialize;
  Application.CreateForm(TForm1, Form1);
  Application.ForceUpdateMainForm(Form1);
  p:=Application;
  APtype:=@Application.ApplicationType;
  pf:=Form1;
  Asize:=SizeOf(Application);
  k:=0;
  while k<1000 do
  begin
    CP:=Pointer((P+k)^);
    if cp=pf then
    WriteLn(k);
    Inc(k,4);
  end;
  Application.Run;
end.

