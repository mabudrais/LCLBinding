program lclparser;

{$mode objfpc}{$H+}

uses
  {$IFDEF UNIX}{$IFDEF UseCThreads}
  cthreads,
  {$ENDIF}{$ENDIF}
  Interfaces, // this includes the LCL widgetset
  Forms, lazcontrols, Unit1, Parserunit, pasfileunit, LangugeModuleUnit,
  TLangueFileUnit, parsedobjectunit, PascalLangunitUnit, pascalFileUnit,
  Parser2Unit, PythonUnit, pythonFileUnit, dataunit,  Unit3
  { you can add units after this };

{$R *.res}

begin
  RequireDerivedFormResource:=True;
  Application.Initialize;
  Application.CreateForm(TForm1, Form1);
  Application.CreateForm(TForm2, Form2);
  Application.Run;
end.

