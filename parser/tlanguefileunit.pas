unit TLangueFileUnit;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, parsedobjectunit;

type

  { TLangueFile }

  TLangueFile = class
    filename: string;
    FileExt:String;
    constructor Create(Fname:String);
    procedure AddUses(Name: string); virtual;
    procedure AddClass(C: TParsedClass); virtual;
    procedure AddFunction(fun: TparsedFunction); virtual;
    procedure AddConstructor(c: TparsedConstructor); virtual;
    procedure AddProcedure(pro: Pointer); virtual;
    procedure AddProperty(prop: TParsedProperty); virtual;
    procedure AddUses(U: TparsedUses); virtual;
    procedure save(saveFolder: string); virtual;
    procedure AddProcedureType(prot :TParsedProcedureType);virtual;
    procedure AddSet(S:TParsedSet);virtual;
    procedure AddCodeline(L:String);
   protected
    C: TStringList; //file content
    function InsertAfter(index: integer; str: string): integer;
  end;

implementation

{ TLangueFile }
function TLangueFile.InsertAfter(index: integer; str: string): integer;
begin
  if index >= C.Count - 1 then
  begin
    C.Append(str);
    Result := C.Count;
  end
  else
  begin
    C.Insert(index + 1, str);
    Result := index + 1;
  end;
end;
procedure TLangueFile.AddClass(C: TParsedClass);
begin

end;

procedure TLangueFile.AddFunction(fun: TparsedFunction);
begin

end;

procedure TLangueFile.AddProcedure(pro: Pointer);
begin

end;

procedure TLangueFile.AddProperty(prop: TParsedProperty);
begin

end;

procedure TLangueFile.AddUses(Name: string);
begin

end;

procedure TLangueFile.AddConstructor(c: TparsedConstructor);
begin

end;

procedure TLangueFile.save(saveFolder: string);
begin
  C.SaveToFile(saveFolder+PathDelim+filename+FileExt);
end;

constructor TLangueFile.Create(Fname: String);
begin
  filename:=Fname;
  C := TStringList.Create;
end;

procedure TLangueFile.AddUses(U: TparsedUses);
begin

end;

procedure TLangueFile.AddProcedureType(prot: TParsedProcedureType);
begin

end;

procedure TLangueFile.AddCodeline(L: String);
begin
  c.Add(L);
end;

procedure TLangueFile.AddSet(S: TParsedSet);
begin

end;

end.
