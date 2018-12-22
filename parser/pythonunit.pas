unit PythonUnit;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, LangugeModuleUnit,pythonFileUnit,TLangueFileUnit;

type

  { TPythonLang }

  TPythonLang = class(TLangugeModule)
   ReturnTypeDec:TpythonFile;
    constructor Create(D: string);
   function addFile(Filename: string): TLangueFile; override;
  end;

implementation

uses PascalLangunitUnit;

{ TPythonLang }

constructor TPythonLang.Create(D: string);
begin
  inherited;
  SavingDiroctry:=D;
  PascalExport := TPascalLang.Create(D +PathDelim+ 'pas');
  ReturnTypeDec:=TpythonFile.Create('ReturnTypeDec');
  ReturnTypeDec.AddCodeline('from ctypes import *');
  ReturnTypeDec.AddCodeline('#importx end');
  Self.LangueFile.Add(ReturnTypeDec);
end;

function TPythonLang.addFile(Filename: string): TLangueFile;
var
  R: TpythonFile;
begin
  R:=TpythonFile.Create(Filename);
  R.Pas:=(PascalExport as TPascalLang).GetMainFile();
  r.ReturnTypeDec:=ReturnTypeDec;
  Self.LangueFile.Add(R);
  Result:=R;
end;

end.
