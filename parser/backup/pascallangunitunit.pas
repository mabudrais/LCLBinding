unit PascalLangunitUnit;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils,LangugeModuleUnit,pascalFileUnit,TLangueFileUnit;
   type

     { TPascalLang }

     TPascalLang=class(TLangugeModule)
       constructor Create(D:String);
       function addFile(Filename: string): TLangueFile; override;
       function GetMainFile:TLangueFile;
     end;

implementation

{ TPascalLang }

constructor TPascalLang.Create(D:String);
var
  MainFile: TpascalBindingFile;
begin
    Inherited;
    Self.SavingDiroctry:=D;
    MainFile:=TpascalBindingFile.Create('main');
    MainFile.filename:='lclexports.dpr';
    Self.LangueFile.Add(MainFile);
    PascalExport:=Nil;
end;

function TPascalLang.addFile(Filename: string): TLangueFile;
begin
Result:=LangueFile[0] as TLangueFile;
end;

function TPascalLang.GetMainFile: TLangueFile;
begin
 Result:=LangueFile[0] as TLangueFile;
end;

end.

