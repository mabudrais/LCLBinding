unit pascalFileUnit;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, TLangueFileUnit, parsedobjectunit, fgl;

type
  TDeclrationptocMap = specialize TFPGMap<string, string>;
  { TpascalBindingFile }

  TpascalBindingFile = class(TLangueFile)
    constructor Create(Fname: string);
    procedure AddConstructor(co: TparsedConstructor); override;
    procedure AddFunction(fun: TparsedFunction); override;
    procedure AddProperty(prop: TParsedProperty); override;
    procedure AddUses(U: TparsedUses); override;
    procedure AddExportFunction(fun: TparsedFunction);
    function AddExportProperty(prop, Link: TParsedProperty): boolean;
    procedure AddEportProcedureType(prot: TParsedProcedureType);
  private
    function PropertyDecleration(prop: TParsedProperty; setter: boolean;
      var funexport: string): string;
    function PropertyBody(prop: TParsedProperty; setter: boolean): string;
    procedure AddProperty(prop: TParsedProperty; Setter: boolean);
    function BodyConvertToPas(Ty: string): string;
    function PascalResulttoCType(PascalType: string; P: TParsedObject = nil): string;
    function AddExportEventProperty(prop, Link: TParsedProperty;
      ProcedureName: string): boolean;
  protected
    F: TStringList;
    Exportlist, ClassDecl, ClassImpl, ProcTypeDecl: TStringList;
    PtoC: TDeclrationptocMap;
    function PascaltoCType(PascalType: string; P: TParsedObject = nil): string;
  public
    function FunctionDecleration(fun: TparsedFunction;
      var funexport: string): string;
    function FunctionBody(fun: TparsedFunction): string;
    procedure save(saveFolder: string); override;
    procedure AddToExport(const funexport: string);
  end;

implementation

{ TpascalBindingFile }

procedure TpascalBindingFile.AddConstructor(co: TparsedConstructor);
begin
  AddFunction(co);
end;

procedure TpascalBindingFile.AddProperty(prop: TParsedProperty);
begin
  if prop.IsWritable then
    AddProperty(prop, True);
  if prop.IsReadable then
    AddProperty(prop, False);
end;

function TpascalBindingFile.PascaltoCType(PascalType: string;
  P: TParsedObject = nil): string;
var
  index: integer;
begin
  if Assigned(p) and ((p is TParsedSet) or (p is TParsedEnum)) then
    Exit('Integer');
  PascalType := PascalType.ToLower;
  if PtoC.IndexOf(PascalType) > -1 then
    Result := PtoC.Data[PtoC.IndexOf(PascalType)]
  else
    Result := PascalType;
end;

function TpascalBindingFile.PascalResulttoCType(PascalType: string;
  P: TParsedObject = nil): string;
var
  index: integer;
begin
  if Assigned(p) and ((p is TParsedSet) or (p is TParsedEnum)) then
    Exit('Integer');
  PascalType := PascalType.ToLower;
  if PascalType = 'boolean' then
    Result := 'BooleanTointegert'
  else if PtoC.IndexOf(PascalType) > -1 then
    Result := PtoC.Data[PtoC.IndexOf(PascalType)]
  else
    Result := PascalType;
end;

procedure TpascalBindingFile.AddFunction(fun: TparsedFunction);
var
  declartion, Calling, funexport: string;
begin
  F.Add('//' + fun.Linenumber.ToString());
  F.Add(FunctionDecleration(fun, funexport));
  F.Add('begin');
  F.Add(FunctionBody(fun));
  F.Add('end;');
  AddToExport(funexport);
end;

constructor TpascalBindingFile.Create(Fname: string);
begin
  inherited Create(Fname);
  FileExt := '.dpr';
  F := TStringList.Create;
  Exportlist := TStringList.Create;
  ClassDecl := TStringList.Create;
  ClassImpl := TStringList.Create;
  ProcTypeDecl := TStringList.Create;
  PtoC := TDeclrationptocMap.Create;
  f.Add('library lclexports;');
  f.Add('uses Interfaces');
  PtoC.Add('integer', 'Integer');
  PtoC.Add('string', 'PChar');
  PtoC.Add('tcaption', 'PChar');
  PtoC.Add('boolean', 'Integer');
end;

function TpascalBindingFile.PropertyDecleration(prop: TParsedProperty;
  setter: boolean; var funexport: string): string;
var
  Cparameter: TparsedParameter;
  p: Pointer;
  Simicolon: string;
  declartion, functiotype, propType: string;
begin
  if Setter then
    functiotype := 'set'
  else
    functiotype := 'get';
  funexport := prop.FileName + '_' + prop.memberof + '_' +
    prop.TParsedObjectName + '_' + functiotype;
  declartion := funexport + '(controlpointer:Pointer';
  propType := PascaltoCType(prop.TParsedObjectType);
  if setter then
    declartion := 'procedure ' + declartion + ';p:' + propType + ');'
  else
    declartion := 'function ' + declartion + '):' + propType + ';';
  declartion := declartion + 'cdecl;';
  Result := declartion;
end;

function TpascalBindingFile.PropertyBody(prop: TParsedProperty; setter: boolean): string;
var
  Calling: string;
begin
  if not setter then
    Calling := 'Result:=' + PascaltoCType(prop.TParsedObjectType) + '(';
  Calling := Calling + prop.memberof + '(controlpointer).' + prop.TParsedObjectName;
  if setter then
    Calling := Calling + ':=' + prop.TParsedObjectType + '(p)';
  if not setter then
    Calling := Calling + ')';
  Calling := Calling + ';';
  Result := Calling;
end;

function TpascalBindingFile.FunctionDecleration(fun: TparsedFunction;
  var funexport: string): string;
var
  Cparameter: TparsedParameter;
  p: Pointer;
  declartion, simicolon: string;
begin
  funexport := fun.FileName + '_' + fun.memberof + '_' + fun.TParsedObjectName;
  declartion := funexport + declartion + '(';
  if not (fun is TparsedConstructor) then
    declartion := declartion + 'controlpointer:Pointer;';
  for p in fun.paramaterList do
  begin
    declartion := declartion + simicolon + TparsedParameter(p).parameterAcsess +
      ' ' + TparsedParameter(p).parameterName + ':' +
      PascaltoCType(TparsedParameter(p).parameterType);
    simicolon := ';';
  end;
  declartion := declartion + ')';
  if fun.TParsedObjectType <> '' then
    declartion := 'function ' + declartion + ':' + PascaltoCType(fun.TParsedObjectType)
  else
    declartion := 'procedure  ' + declartion;
  declartion := declartion + ';cdecl;';
  Result := declartion;
end;

function TpascalBindingFile.FunctionBody(fun: TparsedFunction): string;
var
  Cp: TparsedParameter;
  p: Pointer;
  colon: string;
  Calling: string;
begin
  if fun.TParsedObjectType <> '' then
  begin
    Calling := 'Result:=' + PascaltoCType(fun.TParsedObjectType) + '(';
  end;
  Calling := Calling + fun.memberof;
  if not (fun is TparsedConstructor) then
    Calling := Calling + '(controlpointer)';
  Calling := Calling + '.' + fun.TParsedObjectName + '(';
  colon := '';
  for p in fun.paramaterList do
  begin
    Cp := TparsedParameter(p);
    Calling := Calling + colon + Cp.parameterType + '(' + Cp.parameterName + ')';
    colon := ',';
  end;
  Calling := Calling + ')';
  if fun.TParsedObjectType <> '' then
    Calling := Calling + ')';
  Calling := Calling + ';';
  Result := Calling;
end;

procedure LoadFile(list: TStringList; FileName: string);
var
  F: TextFile;
  jj: string;
  oldeFileMode: byte;
  TheStream: TFileStream;
begin
  TheStream := TFileStream.Create(FileName, fmOpenRead or fmShareDenyNone);
  list.LoadFromStream(TheStream);
  TheStream.Free;
  oldeFileMode := Filemode;
  Filemode := fmOpenRead;
  AssignFile(F, FileName);
  Reset(F);
  ReadLn(F, jj);
  CloseFile(F);
  Filemode := oldeFileMode;
end;

procedure TpascalBindingFile.save(saveFolder: string);
var
  tamp1, tamp2: TStringList;
begin
  tamp1 := TStringList.Create;
  tamp2 := TStringList.Create;
  //LoadFile(tamp2,'tamp1.txt');
  tamp2.LoadFromFile(saveFolder + PathDelim + 'tamp1.txt');
  tamp1.AddStrings(tamp2);
  tamp1.Add('type');
  tamp1.AddStrings(ProcTypeDecl);
  tamp1.AddStrings(ClassDecl);
  tamp2.LoadFromFile(saveFolder + PathDelim + 'defualtFunction.txt');
  tamp1.AddStrings(tamp2);
  tamp1.AddStrings(c);
  tamp1.AddStrings(ClassImpl);
  tamp2.LoadFromFile(saveFolder + PathDelim + 'defaultExport.txt');
  tamp1.AddStrings(tamp2);
  tamp1.AddStrings(Exportlist);
  tamp1[tamp1.Count - 1] := tamp1[tamp1.Count - 1] + '; ';
  tamp1.add('begin');
  tamp1.Add('end.');
  tamp1.SaveToFile(saveFolder + PathDelim + filename + FileExt);
  tamp1.Free;
end;

procedure TpascalBindingFile.AddProperty(prop: TParsedProperty; Setter: boolean);
var
  funexport: string;
begin
  F.Add('//' + prop.FileName + ' ' + prop.memberof + ' ' + prop.TParsedObjectName +
    ' ' + prop.Linenumber.ToString());
  F.Add(PropertyDecleration(prop, Setter, funexport));
  F.Add('begin');
  F.Add(PropertyBody(prop, Setter));
  F.Add('end;');
  AddToExport(funexport);
end;

procedure TpascalBindingFile.AddToExport(const funexport: string);
var
  colon: string;
begin
  // if Exportlist.Count > 1 then
  //  colon := ',';
  Exportlist.Add(',' + funexport);
end;

procedure TpascalBindingFile.AddUses(U: TparsedUses);
var
  s, usesline, colon: string;
begin
  usesline := F[1];
  usesline := usesline + ',' + U.FileName;
  for s in u.useslist do
    usesline := usesline + ',' + s;
  F[1] := usesline;
end;

procedure TpascalBindingFile.AddExportFunction(fun: TparsedFunction);
var
  proc: TParsedProcedureType;
  Cp: TparsedParameter;
  Para, comma, paracall, ProcedureName, callcomma: string;
  k: integer;
begin
  proc := fun.pro;
  ProcedureName := proc.FileName + '_' + proc.memberof + '_' + proc.TParsedObjectName;
  C.Add('//constructor' + ProcedureName);
  for k := 0 to proc.paramaterList.Count - 1 do
  begin
    Cp := proc.paramaterList[k] as TparsedParameter;
    Para := para + comma + cp.parameterName + ':' + PascaltoCType(cp.parameterType);
    paracall := paracall + callcomma + BodyConvertToPas(cp.parameterType) +
      '(' + cp.parameterName + ')';
    comma := ';';
    callcomma := ',';
  end;
  C.Add('function ' + ProcedureName + '(' + Para + '):' + proc.memberof + ';cdecl;');
  C.Add('begin');
  C.Add('Result:=' + proc.memberof + '.' + proc.TParsedObjectName +
    '(' + paracall + ');');
  C.Add('end;');
  AddToExport(ProcedureName);
end;

function TpascalBindingFile.BodyConvertToPas(Ty: string): string;
begin
  if Ty.ToLower = 'boolean' then
    Result := 'integertToBoolean'
  else
    Result := '';
end;

function TpascalBindingFile.AddExportEventProperty(prop, Link: TParsedProperty;
  ProcedureName: string): boolean;
var
  Para, CLname: string;
  prot: TParsedProcedureType;
begin
  if not ((link.IsReadable) and (link.IsWritable)) then
    Exit(False);
  prot := Link.proptype as TParsedProcedureType;
  CLname := prot.FileName + prot.TParsedObjectName + '_wrapper';
  C.Add('//property setter' + ProcedureName);
  Para := 'p:' + prop.memberof + ';newMethod:' + prot.FileName + '_' +
    prot.TParsedObjectName + ';OldEvent:' + CLname + ';FreeOldEvent:integer';
  C.Add('function ' + 'set_' + ProcedureName + '(' + Para + '):pointer;cdecl; ');
  c.add('var callClass:' + CLname + ';');
  C.Add('begin');
  c.Add('if FreeOldEvent=1 then OldEvent.free;');
  c.add('callClass:=' + CLname + '.Create;');
  c.add('callClass.c:=newMethod;');
  C.Add('p.' + link.TParsedObjectName + ':=@callClass.call;');
  c.Add('Result:=callClass;');
  C.Add('end;');
  AddToExport('set_' + ProcedureName);
  Result := True;
end;

function TpascalBindingFile.AddExportProperty(prop, Link: TParsedProperty): boolean;
var
  ProcedureName, Para, Indexpara, IndexparaCallComma, IndexparaCall,
    PrivateStr, tempstr: string;
  k: integer;
  Cp: TparsedParameter;
begin
  Result := False;
  ProcedureName := prop.FileName + '_' + prop.memberof + '_' + prop.TParsedObjectName;
  if (Assigned(Link.proptype) and (Link.proptype is TParsedProcedureType)) then
    Exit(AddExportEventProperty(prop, link, ProcedureName));
  IndexparaCall:='';
  Indexpara:='';
  if link.Isindexed then   //only integer index are supported
  begin
    PrivateStr := '';
    if prop.TParsedObjectName='Strings' then
    WriteLn('');
    for k := 0 to link.paramaterList.Count - 1 do
    begin
      Cp := TparsedParameter(link.paramaterList[k]);
      Indexpara := Indexpara + ';' + cp.parameterName + ':' + Cp.parameterType;
      IndexparaCall := IndexparaCall + IndexparaCallComma + cp.parameterName;
      IndexparaCallComma := ',';
    end;
    IndexparaCall:='['+IndexparaCall+']';
  end;
  if link.IsReadable then
  begin
    C.Add('//property getter' + ProcedureName);
    Para := 'p:' + prop.memberof;
    tempstr:='function ' + 'get_' + ProcedureName + '(' + Para +Indexpara+ '):' +
      PascaltoCType(link.TParsedObjectType, link.proptype) + ';cdecl;';
    C.Add(tempstr);
    C.Add('begin');
    C.Add('Result:=' + PascalResulttoCType(link.TParsedObjectType, link.proptype) +
      '(p.' + link.TParsedObjectName + IndexparaCall+');');
    C.Add('end;');
    AddToExport('get_' + ProcedureName);
    Result := True;
  end;
  if link.IsWritable then
  begin
    C.Add('//property setter' + ProcedureName);
    Para := 'p:' + prop.memberof + Indexpara+';v:' + PascaltoCType(link.TParsedObjectType);
    C.Add('procedure ' + 'set_' + ProcedureName + '(' + Para + ');cdecl; ');
    C.Add('begin');
    C.Add('p.' + link.TParsedObjectName +IndexparaCall+ ':=' + BodyConvertToPas(
      link.TParsedObjectType) + '(v);');
    C.Add('end;');
    AddToExport('set_' + ProcedureName);
    Result := True;
  end;
end;

procedure TpascalBindingFile.AddEportProcedureType(prot: TParsedProcedureType);
var
  k: integer;
  Cp: TparsedParameter;
  paraCtype, paracall, comma, callcomma, para, varprefix: string;
begin
  for k := 0 to prot.paramaterList.Count - 1 do
  begin
    varprefix := '';
    Cp := prot.paramaterList[k] as TparsedParameter;
    if Cp.parameterAcsess = 'var' then
      varprefix := 'var '
      else if cp.parameterAcsess='const' then
      varprefix:='const';
    paraCtype := paraCtype + comma + cp.parameterName + ':' +
      PascaltoCType(cp.parameterType, cp.parameterTypeO);
    para := para + comma + varprefix + cp.parameterName + ':' + cp.parameterType;
    paracall := paracall + callcomma + PascalResulttoCType(
      cp.parameterType, cp.parameterTypeO) + '(' + cp.parameterName + ')';
    comma := ';';
    callcomma := ',';
  end;
  self.ProcTypeDecl.Add(prot.FileName + '_' + prot.TParsedObjectName +
    '=procedure(' + paraCtype + ');cdecl;');
  self.ClassDecl.Add(prot.FileName + prot.TParsedObjectName + '_wrapper=class');
  ClassDecl.Add('C:' + prot.FileName + '_' + prot.TParsedObjectName + ';');
  ClassDecl.add('procedure call(' + para + ');');
  ClassDecl.add('end;');
  ClassImpl.add('procedure ' + prot.FileName + prot.TParsedObjectName +
    '_wrapper.call(' + para + ');');
  ClassImpl.add('begin');
  ClassImpl.add('C(' + paracall + ');');
  ClassImpl.add('end;');
  ;
end;

end.
