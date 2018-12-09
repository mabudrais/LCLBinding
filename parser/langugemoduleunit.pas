unit LangugeModuleUnit;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, TLangueFileUnit, parsedobjectunit, contnrs, FileUtil;

type

  { TLangugeModule }

  TLangugeModule = class
    LangueFile: TObjectList;
    PascalExport: TLangugeModule;
    constructor Create(D: string);
    function SetDiroctry(D: string): TLangugeModule;
    function addFile(Filename: string): TLangueFile; virtual;
    procedure GenerateBinding(ParsedObject: TList);

  private
    function IsPublicMember(obj: TParsedObject): boolean;
  public
    function GetTargetFile(var obj: TParsedObject): TLangueFile;
    procedure SaveFiles;
  protected
    SavingDiroctry: string;
    procedure GenerateFiles(const ParsedObject: TList);
  end;

implementation

uses PascalLangunitUnit;

{ TLangugeModule }

function TLangugeModule.addFile(Filename: string): TLangueFile;
begin
  raise Exception.Create('this procedure must be reimplemented ' + Filename);
  Result := nil;
end;

procedure TLangugeModule.GenerateBinding(ParsedObject: TList);
begin
  if (PascalExport = nil) and (not (Self is TPascalLang)) then
    raise Exception.Create('please create PascalExport class');
  GenerateFiles(ParsedObject);
end;

function TLangugeModule.GetTargetFile(var obj: TParsedObject): TLangueFile;
var
  targetlangfile: TLangueFile;
  filename, ObjectName: string;
  lf: Pointer;
begin
  ObjectName := obj.TParsedObjectName;
  filename := ExtractFileNameWithoutExt(obj.FileName);
  targetlangfile := nil;
  for lf in LangueFile do
  begin
    if TLangueFile(lf).filename = filename then
      targetlangfile := TLangueFile(lf);
  end;
  if targetlangfile = nil then
  begin
    targetlangfile := addFile(filename);
  end;
  Result := targetlangfile;
end;

constructor TLangugeModule.Create(D: string);
begin
  LangueFile := TObjectList.Create;
  PascalExport := nil;
  SavingDiroctry := D;
end;

function TLangugeModule.SetDiroctry(D: string): TLangugeModule;
begin
  SavingDiroctry := D;
  Result := Self;
end;

procedure TLangugeModule.SaveFiles;
var
  lf: Pointer;
begin
  if not DirectoryExists(SavingDiroctry) then
    CreateDir(SavingDiroctry);
  for lf in LangueFile do
    TLangueFile(lf).save(SavingDiroctry);
  if PascalExport <> nil then
    PascalExport.SaveFiles;
end;

function TLangugeModule.IsPublicMember(obj: TParsedObject): boolean;
var
  prop: TParsedProperty;
begin
  if not (obj is TParsedProperty) then
    Exit(True);
  prop := obj as TParsedProperty;
  if (prop.AccesModifir = 'public') or (prop.AccesModifir = 'published') then
    Exit(True);
  Result := False;
end;

procedure TLangugeModule.GenerateFiles(const ParsedObject: TList);
var
  targetlangfile: TLangueFile;
  obj: TParsedObject;
  o: Pointer;
begin
  for o in ParsedObject do
  begin
    obj := TParsedObject(o);
    if not IsPublicMember(obj) then
      Continue;
    targetlangfile := GetTargetFile(obj);
    if obj is TParsedClass then
      targetlangfile.AddClass(obj as TParsedClass)
    else if obj is TparsedConstructor then
      targetlangfile.AddConstructor(obj as TparsedConstructor)
    else if obj is TParsedProperty then
      targetlangfile.AddProperty(obj as TParsedProperty)
    else if obj is TparsedUses then
      targetlangfile.AddUses(obj as TparsedUses)
    else if obj is TParsedProcedureType then
      targetlangfile.AddProcedureType(obj as TParsedProcedureType)
      else if obj is TParsedSet then
      targetlangfile.AddSet(obj as TParsedSet);
  end;
end;

end.
