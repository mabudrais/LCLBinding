unit pythonFileUnit;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, TLangueFileUnit, parsedobjectunit, contnrs, dataunit, Math;

type

  { TpythonFile }

  TpythonFile = class(TLangueFile)
    Pas: TLangueFile;
    ReturnTypeDec: TpythonFile;
    constructor Create(Fname: string);
    procedure AddUses(Name: string); override;
    procedure AddClass(CL: TParsedClass); override;
    procedure AddFunction(fun: TparsedFunction); override;
    procedure AddConstructor(co: TparsedConstructor); override;
    procedure AddProcedure(fun: TparsedFunction); override;
    procedure AddProperty(prop: TParsedProperty); override;
    procedure AddUses(U: TparsedUses); override;
    procedure save(saveFolder: string); override;
    procedure AddProcedureType(prot: TParsedProcedureType); override;
    procedure AddSet(S: TParsedSet); override;
  private
    function space(num: integer): string;
    function PythonToPasConvert(V, T: string): string;
    procedure AddEventProperty(prop, Link: TParsedProperty);
    function PasTOPythonConvert(V, T: string; o: TParsedObject = nil): string;
    function PasToCtypeConvert(V, T: string; o: TParsedObject = nil): string;
    procedure ClassReordering;
    function ReturnTypeCorection(rtype, PFN: string; s: boolean;
      Rtypeo: TObject): string;
  end;

implementation

uses pascalFileUnit;

{ TpythonFile }

constructor TpythonFile.Create(Fname: string);
begin
  inherited;
  FileExt := '.py';
  C.Add('from MainPasObject import *');
  C.Add('import LCLBindingUtil');
  C.Add(('#import end'));
end;

procedure TpythonFile.AddClass(CL: TParsedClass);
var
  index: integer;
begin
  if C.IndexOf('#class ' + cl.TParsedObjectName + ' start') > -1 then
  begin

    Exit;
  end;
  //add parent class import
  index := C.IndexOf('#import end');
  Self.insertafter(index, '#class ' + cl.TParsedObjectName + ' start');
  Self.insertafter(index + 1, 'class ' + cl.TParsedObjectName + '(' +
    cl.ParentClass + '):');
  Self.InsertAfter(index + 2, '#' + space(1) + 'pointer=c_void_p()');
  Self.insertafter(index + 3, space(1) + 'def __init__(self):#' + cl.TParsedObjectName);
  Self.insertafter(index + 4, space(2) + cl.ParentClass + '.__init__(self)');
  Self.insertafter(index + 5, '#class ' + cl.TParsedObjectName + ' end');
  //add_to_impfile(clname);
  // Result := True;
end;

function TpythonFile.space(num: integer): string;
var
  str: string;
  i: integer;
begin
  for i := 0 to num - 1 do
    str := str + '    ';
  Result := str;
end;

function TpythonFile.PythonToPasConvert(V, T: string): string;
begin //v var name T var pascal type
  T := LowerCase(T);
  if (T = 'string') or (t = 'integer') then
    Exit(V)
  else if T = 'boolean' then
    Exit('booleantoint(' + V + ')')
  else
    Exit(v + '.pointer');
end;

function TpythonFile.PasTOPythonConvert(V, T: string; o: TParsedObject = nil): string;
var
  T2: string;
begin //v var name T var pascal type
  T2 := LowerCase(T);
  if Assigned(o) and ((o is TParsedSet) or (o is TParsedEnum)) then
    Exit(V);
  if (T2 = 'string') or (T2 = 'integer') then
    Exit(V)
  else if T2 = 'boolean' then
    Exit('LCLBindingUtil.IntToBoolean(' + V + ')')
  else
    Exit('LCLBindingUtil.GetPytonObject(' + v + ',' + T + ')');
end;

function TpythonFile.PasToCtypeConvert(V, T: string; o: TParsedObject = nil): string;
var
  T2: string;
begin //v var name T var pascal type
  if Assigned(o) and ((o is TParsedSet) or (o is TParsedEnum)) then
    Exit('c_int');
  T2 := LowerCase(T);
  if (T2 = 'string') or (T2 = 'tcaption') then
    Exit('c_char_p')
  else if (T2 = 'integer') or (T2 = 'boolean') then
    Exit('c_int')
  else
    Exit('c_void_p');
end;

procedure TpythonFile.AddConstructor(co: TparsedConstructor);
var
  CEI, k: integer;
  PFN, para, callcomma, paracall, paraComma: string;
  P: TpascalBindingFile;
  proc: TParsedProcedureType;
  Cp: TparsedParameter;
begin
  proc := co.pro;
  CEI := C.IndexOf('#class ' + proc.memberof + ' end');
  if CEI < 0 then
  begin
    WriteLn('failed to find python class' + proc.memberof);
    Exit;
  end;
  P := pas as TpascalBindingFile;
  if not CheckPara(proc.paramaterList) then
    exit;
  p.AddExportFunction(co);
  PFN := proc.FileName + '_' + proc.memberof + '_' + proc.TParsedObjectName;
  para := '';
  for k := 0 to proc.paramaterList.Count - 1 do
  begin
    Cp := proc.paramaterList[k] as TparsedParameter;
    Para := para + paraComma + cp.parameterName;
    paracall := paracall + callcomma + '(' + PythonToPasConvert(
      cp.parameterName, cp.parameterType) + ')';
    callcomma := ',';
    paraComma := ',';
  end;
  C.Insert(CEI, '#constructor' + PFN);
  c.Insert(CEI + 1, space(1) + '@staticmethod');
  C.Insert(CEI + 2, space(1) + 'def ' + proc.TParsedObjectName + '(' + para + '):');
  C.Insert(CEI + 3, space(2) + 'return LCLBindingUtil.GetPytonObject(LCLBinding.' +
    PFN + '(' + paracall + '),' + proc.memberof + ')');
end;

procedure TpythonFile.AddFunction(fun: TparsedFunction);
begin
  inherited AddFunction(fun);
end;

procedure TpythonFile.AddProcedure(fun: TparsedFunction);
var
  CEI, k: integer;
  PFN, para, callcomma, paracall, paraComma, r: string;
  P: TpascalBindingFile;
  proc: TParsedProcedureType;
  Cp, rt: TparsedParameter;
begin
  proc := fun.pro;
  if proc.TParsedObjectName='Show'then
  WriteLn('nn');
  CEI := C.IndexOf('#class ' + proc.memberof + ' end');
  if CEI < 0 then
  begin
    WriteLn('failed to find python class' + proc.memberof);
    Exit;
  end;
  P := pas as TpascalBindingFile;
  if not CheckPara(proc.paramaterList) then
    exit;
  if proc.hasResult then
  begin
    if not CheckPara(proc.resultType) then
      Exit;
    r := 'r=(';
  end;
  p.AddExportFunction(fun);
  PFN := proc.FileName + '_' + proc.memberof + '_' + proc.TParsedObjectName;
  para := 'self,';
  for k := 0 to proc.paramaterList.Count - 1 do
  begin
    Cp := proc.paramaterList[k] as TparsedParameter;
    Para := para + paraComma + cp.parameterName;
    paracall := paracall + callcomma + '(' + PythonToPasConvert(
      cp.parameterName, cp.parameterType) + ')';
    callcomma := ',';
    paraComma := ',';
  end;
  C.Insert(CEI, '#Procedure ' + PFN);
  c.Insert(CEI + 1, space(1) + '@staticmethod');
  C.Insert(CEI + 2, space(1) + 'def ' + proc.TParsedObjectName + '(' + para + '):');
  C.Insert(CEI + 3, space(2) + r + 'LCLBinding.' + PFN + '(' +
    paracall + ')' );
  if proc.hasResult then
  begin
    rt := proc.resultType;
    C.Insert(CEI + 4, ReturnTypeCorection(rt.parameterType, PFN,
      rt.isSimpleType, rt.parameterTypeO));
  end;
end;

procedure TpythonFile.AddEventProperty(prop, Link: TParsedProperty);
var
  CEI, k: integer;
  PFN, Para, callcomma, paracall, CtypePara: string;
  PT: TParsedProcedureType;
  Cp: TparsedParameter;
begin
  CEI := C.IndexOf('#class ' + prop.memberof + ' end');
  PFN := prop.FileName + '_' + prop.memberof + '_' + Link.TParsedObjectName;
  if not (Link.IsWritable and Link.IsReadable) then
    exit;
  if link.Isindexed then
    Exit;
  PT := Link.proptype as TParsedProcedureType;
  if not CheckPara(PT.paramaterList) then
    exit;
  Para := '';
  CtypePara := 'c_void_p';
  for k := 0 to PT.paramaterList.Count - 1 do
  begin
    Cp := PT.paramaterList[k] as TparsedParameter;
    CtypePara := CtypePara + ',' + PasToCtypeConvert('', cp.parameterType,
      cp.parameterTypeO);
    Para := Para + ',' + cp.parameterName;
    paracall := paracall + callcomma + PasTOPythonConvert(cp.parameterName,
      cp.parameterType, cp.parameterTypeO);
    callcomma := ',';
  end;
  C.Insert(CEI, space(1) + 'def _Warper_' + Link.TParsedObjectName +
    '(self' + Para + '):');
  C.Insert(CEI + 1, space(2) + 'self.' + Link.TParsedObjectName +
    'call(' + paracall + ')');
  C.Insert(CEI + 2, space(1) + 'def set' + Link.TParsedObjectName + '(self,v):');
  C.Insert(CEI + 3, space(2) + 'FunctionForm= CFUNCTYPE(' + CtypePara + ')');
  C.Insert(CEI + 4, space(2) + 'FreeOldEvent=0');
  C.Insert(CEI + 5, space(2) + 'oldobj=0');
  C.Insert(CEI + 6, space(2) + 'if hasattr(self, ''' + Link.TParsedObjectName +
    'call''):');
  C.Insert(CEI + 7, space(3) + 'FreeOldEvent=1');
  C.Insert(CEI + 8, space(3) + 'oldobj=self.' + Link.TParsedObjectName + 'PasObject');
  C.Insert(CEI + 9, space(2) + 'self.' + Link.TParsedObjectName + 'call=v ');
  C.Insert(CEI + 10, space(2) + 'self.Pas' + Link.TParsedObjectName +
    '=FunctionForm(self._Warper_' + Link.TParsedObjectName + ')');
  // PythonProperty := PythonProperty + PythonPropertyComma + 'set' +
  // Link.TParsedObjectName;
  C.Insert(CEI + 11, space(2) + 'self.' + Link.TParsedObjectName +
    'PasObject=LCLBinding.set_' + PFN + '(self.pointer,self.Pas' +
    Link.TParsedObjectName + ',oldobj,FreeOldEvent)');
  C.Insert(CEI + 12, space(1) + 'def get' + Link.TParsedObjectName + '(self):');
  C.Insert(CEI + 13, space(2) + 'return ' + Link.TParsedObjectName + 'call');
  C.Insert(CEI + 14, space(1) + Link.TParsedObjectName + '=property(get' +
    Link.TParsedObjectName + ',set' + Link.TParsedObjectName + ')');
end;


procedure TpythonFile.AddProperty(prop: TParsedProperty);
var
  P: TpascalBindingFile;
  CEI, k: integer;
  PFN, PythonProperty, PythonPropertyComma, Indexpara, PrivateStr: string;
  link: TParsedProperty;
begin
  P := pas as TpascalBindingFile;
  link := prop.GetLinkedProperty();
  // if link.TParsedObjectName = 'Cells' then
  // WriteLn('');
  //if prop.TParsedObjectName = 'OnMouseMove' then
  // WriteLn('lll');
  if (Link.proptype = nil) and (not Link.isSimple) and (not Link.isDefaultType) then
    Exit;
  if not CheckPara(link.paramaterList) then
    exit;
  PrivateStr := '_';
  Indexpara := '';
  if link.Isindexed then   //only integer index are supported
  begin
    PrivateStr := '';
    for k := 0 to link.paramaterList.Count - 1 do
      Indexpara := Indexpara + ',' + TparsedParameter(link.paramaterList[k]).parameterName;
    //Exit;
  end;
  if not Link.IsReadable then
    raise  Exception.Create('unreadable property');
  P.AddExportProperty(prop, link);
  if (Assigned(Link.proptype) and (Link.proptype is TParsedProcedureType)) then
  begin
    AddEventProperty(prop, link);
    Exit;
  end;
  CEI := C.IndexOf('#class ' + prop.memberof + ' end');
  PFN := prop.FileName + '_' + prop.memberof + '_' + Link.TParsedObjectName;
  if CEI < 0 then
    raise Exception.Create('Class not found');
  PythonProperty := '';
  PythonPropertyComma := '';
  if Link.IsReadable then
  begin
    PythonProperty := 'get' + Link.TParsedObjectName;
    PythonPropertyComma := ',';
    C.Insert(CEI, space(1) + 'def get' + Link.TParsedObjectName +
      '(self' + Indexpara + '):');
    C.Insert(CEI + 1, space(2) + 'r=LCLBinding.get_' + PFN +
      '(self.pointer' + Indexpara + ')');
    c.Insert(CEI + 2, ReturnTypeCorection(link.TParsedObjectType,
      PFN, link.isSimple, link.proptype));
  end;
  CEI := C.IndexOf('#class ' + prop.memberof + ' end');
  if Link.IsWritable then
  begin
    C.Insert(CEI, space(1) + 'def set' + Link.TParsedObjectName +
      '(self' + Indexpara + ',v):');
    PythonProperty := PythonProperty + PythonPropertyComma + 'set' +
      Link.TParsedObjectName;
    if Link.isSimple then
      C.Insert(CEI + 1, space(2) + 'LCLBinding.set_' + PFN +
        '(self.pointer' + Indexpara + ',v)')
    else
      C.Insert(CEI + 1, space(2) + 'LCLBinding.set_' + PFN +
        '(self.pointer' + Indexpara + ',v.pointer)');
  end;
  CEI := C.IndexOf('#class ' + prop.memberof + ' end');
  if not link.Isindexed then
    C.Insert(CEI, space(1) + Link.TParsedObjectName + '=property(' +
      PythonProperty + ')');
end;

procedure TpythonFile.AddUses(Name: string);
var
  temp: String;
  index: Integer;
begin
  index := C.IndexOf('#import end');
  c.Insert(0,'from '+Name+' import *');
end;

procedure TpythonFile.AddUses(U: TparsedUses);
begin
  inherited AddUses(U);
end;

procedure TpythonFile.ClassReordering;
var
  k, m, n, Cindex: integer;
  CN, PlN, OrderedClass, imprtstrlist: TStringList;
  Cpn, tcn, L, Cstr: string;
  p1, p2: SizeInt;
  ClassContent: TObjectList;
begin
  PlN := TStringList.Create;
  CN := TStringList.Create;
  OrderedClass := TStringList.Create;
  //get class name
  for k := 0 to C.Count - 1 do
  begin
    L := C[k];
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
  ClassContent := TObjectList.Create;
  for k := cn.Count - 1 downto 0 do
  begin
    OrderedClass.Add(cn[k]);
    ClassContent.Add(TStringList.Create);
  end;
  for k := 0 to OrderedClass.Count - 1 do
  begin
    Cindex := C.IndexOf('#class ' + OrderedClass[k] + ' start');
    Cstr := c[Cindex];
    while not Cstr.StartsWith('#class ' + OrderedClass[k] + ' end') do
    begin
      (ClassContent[k] as TStringList).Add(Cstr);
      c.Delete(Cindex);
      Cstr := c[Cindex];
    end;
    (ClassContent[k] as TStringList).Add(Cstr);
    c.Delete(Cindex);
  end;
  for k := ClassContent.Count - 1 downto 0 do
    c.AddStrings((ClassContent[k] as TStringList));
end;

procedure TpythonFile.save(saveFolder: string);
var
  temp: String;
begin
  temp:=c[0];
  ClassReordering;
  temp:=c[0];
  inherited save(saveFolder);
end;

procedure TpythonFile.AddProcedureType(prot: TParsedProcedureType);
var
  P: TpascalBindingFile;
begin
  P := pas as TpascalBindingFile;
  P.AddEportProcedureType(prot);
end;

procedure TpythonFile.AddSet(S: TParsedSet);
var
  index, k: integer;
  dic, comma, E: string;
begin
  index := C.IndexOf('#import end');
  Self.InsertAfter(index, 'def Create' + s.TParsedObjectName + 'FromInt(i):');
  for k := 0 to s.Enum.Names.Count - 1 do
  begin
    E := s.Enum.Names[k].Replace(',', '');
    dic := dic + comma + round(power(2, k)).ToString() + ':"' + E + '"';
    comma := ',';
  end;
  Self.InsertAfter(index + 1, space(1) + 'dic={' + dic + '}');
  self.InsertAfter(index + 2, space(1) + 'return CreateSetFormint(i,dic)');
end;

function TpythonFile.ReturnTypeCorection(rtype, PFN: string; s: boolean;
  Rtypeo: TObject): string;
begin
  if (CompareText(Rtype, 'String') = 0) or (CompareText(Rtype, 'TCaption') = 0) then
    ReturnTypeDec.c.Add('LCLBinding.get_' + PFN + '.restype=c_char_p');
  if s then
    Result := (space(2) + 'return LCLBindingUtil.ConvertPascal' + rtype + '(r)')
  else if (Rtypeo <> nil) and ((Rtypeo is TParsedEnum) or (Rtypeo is TParsedSet)) then
    Result := (space(2) + 'return r')
  else
    Result := (space(2) + 'return LCLBindingUtil.GetPytonObject(r,' + Rtype + ')');
end;

end.
