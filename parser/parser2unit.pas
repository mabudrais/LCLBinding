unit Parser2Unit;

{$mode objfpc}{$H+} {$R+}

interface

uses
  Classes, SysUtils, FileUtil, fgl, contnrs, PParser, PasTree,
  parsedobjectunit, dataunit;

type

  TSimpleEngine = class(TPasTreeContainer)
  public
    function CreateElement(AClass: TPTreeElement; const AName: string;
      AParent: TPasElement; AVisibility: TPasMemberVisibility;
      const ASourceFilename: string; ASourceLinenumber: integer): TPasElement;
      override;
    function FindElement(const AName: string): TPasElement; override;
  end;

  { TPFI }

  TPFI = class
    Name, FileName: string;
    E: TPasElement;
    Ob: TParsedObject;
    Processed: boolean;
    constructor Create(CName, CFileName: string; CE: TPasElement; CM: TPasModule);
  private
    M: TPasModule;
  end;



  { TLCLParser2 }

  TLCLParser2 = class
    ParsedFiles, ParsedObject: TObjectList;
    PFIS: TStringMap;
    NilParsedObject: TParsedObject;
    constructor Create(fileList: TStrings; CTargetClass: TStrings; path: string);
  private
    CurrentFile: TPasModule;
    DefinedIdentfire: TStringList;
    procedure ParseFile(const FileName, path: string);
    procedure CW(Text: string);
    function ParseIdentTifire(c: string; var Index: integer;
      ristrict: boolean = False): TParsedObject;
    function findPasElement(ElementName: string; CFile: TPasModule): TPasElement;
    function ParseElement(E: TPasElement): TParsedObject;
    function GetClassData(C: TPasClassType): TParsedClass;
    function ProcessProperty(p: TPasProperty; CO: TParsedClass): TParsedProperty;
    function AddIndex(Iname: string): integer;
    function GetProcedureType(P: TPasProcedureType;
      ATPO: boolean = True): TParsedObject;
    function GetParamterType(T: string; out SimpleType, DT: boolean;
      out index: integer): TParsedObject;
    function ProcessConstructor(con: TPasConstructor;
      CN: string): TparsedConstructor;
    function GetSetData(S: TPasSetType): TParsedObject;
    function GetEnumType(EN: TPasEnumType): TParsedObject;
    function ProcessDefinedProperty(p: TPasProperty; CN: string): TParsedProperty;
    function ProcessUNDefinedProperty(const CO: TParsedClass;
      const p: TPasProperty): TParsedProperty;
    function CheckInUses(var oldCurrentfile: TPasModule;
      var Index: integer): boolean;
    function HasConstructor(O: TParsedClass; var ConIndex: integer): boolean;
    function ProcessProcedure(pr: TPasProcedure; CN: string): TparsedFunction;
  end;

implementation

{ TPFI }

constructor TPFI.Create(CName, CFileName: string; CE: TPasElement; CM: TPasModule);
begin
  Name := CName;
  FileName := CFileName;
  E := CE;
  Ob := nil;
  M := CM;
  Processed := False;
end;



function TSimpleEngine.CreateElement(AClass: TPTreeElement; const AName: string;
  AParent: TPasElement; AVisibility: TPasMemberVisibility;
  const ASourceFilename: string; ASourceLinenumber: integer): TPasElement;
begin
  // Writeln(AName, ' : ', AClass.ClassName, ' at ', ASourceFilename,
  //   ':', ASourceLinenumber);
  Result := AClass.Create(AName, AParent);
  Result.Visibility := AVisibility;
  Result.SourceFilename := ASourceFilename;
  Result.SourceLinenumber := ASourceLinenumber;
end;

function TSimpleEngine.FindElement(const AName: string): TPasElement;
begin
  { dummy implementation, see TFPDocEngine.FindElement for a real example }
  Result := nil;
end;

{ TLCLParser2 }

constructor TLCLParser2.Create(fileList: TStrings; CTargetClass: TStrings;
  path: string);
var
  FileName, LCLComponenetName: string;
  i: integer;
begin
  NilParsedObject := nil;
  ParsedFiles := TObjectList.Create();
  ParsedObject := TObjectList.Create();
  PFIS := TStringMap.Create();
  PFIS.Sorted := True;

  DefinedIdentfire := TStringList.Create;
  DefinedIdentfire.AddStrings(['tobject', 'tpersistent']);
  for FileName in fileList do
  begin
    ParseFile(FileName, path);
  end;
  // WriteLn(PFIS.Count);
  for LCLComponenetName in CTargetClass do
    ParseIdentTifire(LCLComponenetName, i);
end;

function TLCLParser2.findPasElement(ElementName: string; CFile: TPasModule): TPasElement;
var
  Decls: TFPList;
  CDeclName: string;
  k: integer;
begin
  Result := nil;
  Decls := CFile.InterfaceSection.Declarations;
  for k := 0 to Decls.Count - 1 do
  begin
    CDeclName := (TObject(Decls[k]) as TPasElement).Name;
    if CompareText(CDeclName,ElementName)=0 then
      Exit((TObject(Decls[k]) as TPasElement));
  end;
end;

function TLCLParser2.GetParamterType(T: string; out SimpleType, DT: boolean;
  out index: integer): TParsedObject;
begin
  Result := nil;
  SimpleType := False;
  DT := False;
  T := LowerCase(T);
  if not isDefinedSimpleIdentfire(T) then
  begin
    begin
      if DefinedIdentfire.IndexOf(T) < 0 then
      begin
        Result := ParseIdentTifire(T, index, True);
        if Result = nil then
          Exit;
      end
      else
        DT := True;
    end;
  end
  else
    SimpleType := True;
end;

function TLCLParser2.ProcessConstructor(con: TPasConstructor;
  CN: string): TparsedConstructor;
var
  P: TParsedObject;
  PP: TparsedConstructor;
begin
  //  if CN = 'TCustomImageList' then
  //  CW('kkk');
  Result := nil;
  P := GetProcedureType(con.ProcType, False);
  if Assigned(P) then
  begin
    p.memberof := CN;
    p.TParsedObjectName := con.Name;
    PP := TparsedConstructor.Create;
    pp.FileName := p.FileName;
    pp.pro := p as TParsedProcedureType;
    ParsedObject.Add(pp);
    Result := pp;
  end;
end;

function TLCLParser2.ProcessProcedure(pr: TPasProcedure; CN: string): TparsedFunction;
var
  P: TParsedObject;
  PP: TparsedFunction;
  prot: TParsedProcedureType;
  k: integer;
begin
  //  if CN = 'TCustomImageList' then
  //  CW('kkk');
  Result := nil;
  if pr.Name = 'Show' then
    cw('mmm');
  Result := nil;
  P := GetProcedureType(pr.ProcType, False);
  if Assigned(P) then
  begin
    prot := p as TParsedProcedureType;
    for k := 0 to prot.paramaterList.Count - 1 do
    begin
      if (prot.paramaterList[k] as TparsedParameter).parameterAcsess = 'var' then
        Exit;
    end;
    p.memberof := CN;
    p.TParsedObjectName := pr.Name;
    PP := TparsedFunction.Create;
    pp.FileName := p.FileName;
    pp.pro := p as TParsedProcedureType;
    ParsedObject.Add(pp);
    Result := pp;
  end
  else
    WriteLn('failed to parse  Procedure' + cn + '.' + pr.Name);
end;

function TLCLParser2.ProcessProperty(p: TPasProperty; CO: TParsedClass): TParsedProperty;
var
  E: TPasExpr;
  CN, CArgTypeName: string;
  O: TParsedProperty;
  SimpleType: boolean;
  rt, VT: TPasType;
  PC: TParsedClass;
  CArg: TPasArgument;
begin
  CN := co.TParsedObjectName;
  O := nil;
  // p.Args for indexd property
  if p.Name = 'Strings' then
    CW('');
  if p.Args.Count > 0 then
  begin

  end;
  CW(p.Args.Count.ToString());
  rt := p.ResolvedType;
  VT := p.VarType;
  if Assigned(p.VarType) then
    O := ProcessDefinedProperty(p, CN)
  else
    O := ProcessUNDefinedProperty(CO, p);
  if Assigned(O) then
    ParsedObject.Add(O);
  Result := O;
end;

function TLCLParser2.GetClassData(C: TPasClassType): TParsedClass;
var
  k, index, LinkConIndex: integer;
  CMember: TPasElement;
  CMemberType: string;
  O: TParsedClass;
  PM: TParsedObject;//PM parsed Member
  Con: TparsedConstructor;
begin
  O := TParsedClass.Create;
  Result := O;
  ParsedObject.Add(o);
  o.TParsedObjectName := c.Name;
  if o.TParsedObjectName = 'TButton' then
    CW('');
  o.FileName := CurrentFile.Name;
  if Assigned(c.AncestorType) then
  begin
    o.ParentClass := c.AncestorType.FullName;
    o.ParentclassO := ParseIdentTifire(LowerCase(o.ParentClass), index) as TParsedClass;
    if o.ParentclassO=Nil then
    o.ParentClass:='TObject';
  end
  else
    o.ParentClass := 'TObject';
  for k := 0 to C.Members.Count - 1 do
  begin
    PM := nil;
    CMember := TObject(C.Members[k]) as TPasElement;
    if not ((CMember.Visibility = visPublic) or (CMember.Visibility = visPublished)) then
    begin
      if not (CMember is TPasProperty) then
        Continue;
    end;
    CMemberType := CMember.ClassName;
    //if (CMember.SourceLinenumber>600)and(o.TParsedObjectName='TCustomForm') then
    // CW('pp');
    if CMember is TPasFunction then
    else if CMember is TPasConstructor then
      PM := ProcessConstructor(CMember as TPasConstructor, o.TParsedObjectName)
    else if CMember.ClassType = TPasDestructor then
    else if CMember is TPasProcedure then
      PM := ProcessProcedure(CMember as TPasProcedure, o.TParsedObjectName)
    else if CMember is TPasProperty then
      PM := ProcessProperty(CMember as TPasProperty, o);
    if Assigned(PM) then
      o.Members.Add(CMember.Name, PM);
  end;
  //copy inhirited constructor
  if not HasConstructor(O, LinkConIndex) then
  begin
    //copy parent Constructor then
    if Assigned(o.ParentclassO) and (HasConstructor(o.ParentclassO, LinkConIndex)) then
    begin
      Con := TparsedConstructor.Create;
      con.CopyDataFrom(o.ParentclassO.Members.Data[LinkConIndex] as
        TparsedConstructor, o.TParsedObjectName, o.FileName);
      o.Members.Add(con.TParsedObjectName, con);
      ParsedObject.Add(con);
    end;
  end;
end;

function TLCLParser2.GetProcedureType(P: TPasProcedureType;
  ATPO: boolean = True): TParsedObject;
var
  //ATPO add to parsed object
  k, index: integer;
  CArg: TPasArgument;
  ArgTypeName, ArgName, Access, tt: string;
  DT, SimpleType, WrongType, SearchFail: boolean;
  O: TParsedProcedureType;
  ParsedArg: TparsedParameter;
  SearchedParaType: TParsedObject;
  funt: TPasFunctionType;
begin
  Result := nil;
  O := TParsedProcedureType.Create;
  if p is TPasFunctionType then
  begin
    o.hasResult := True;
    funt := p as TPasFunctionType;
    o.resultType := TparsedParameter.Create('Result', '');
    o.resultType.parameterType := funt.ResultEl.ResultType.Name;
    GetParamterType(funt.ResultEl.ResultType.Name, SimpleType, DT, index);
    o.resultType.SetparameterTypeO(PFIS, index);
    if (not DT) and (not SimpleType) and (index < 0) then
    begin
      FreeAndNil(o);
      Exit(nil);
    end;
  end;
  WrongType := False;
  O := TParsedProcedureType.Create;
  o.TParsedObjectName := p.Name;
  o.FileName := CurrentFile.Name;
  o.TParsedObjectName := P.Name;
  for k := 0 to P.Args.Count - 1 do
  begin
    SimpleType := False;
    DT := False;
    SearchFail := False;
    CArg := TPasArgument(P.Args[k]);
    ArgName := CArg.Name;
    if not Assigned(CArg.ArgType) then
      Exit(nil);
    ArgTypeName := CArg.ArgType.Name;
    if isDefinedSimpleIdentfire(LowerCase(ArgTypeName)) then
      SimpleType := True
    else if DefinedIdentfire.IndexOf(LowerCase(ArgTypeName)) > -1 then
      DT := True
    else
    begin
      SearchedParaType := ParseIdentTifire(LowerCase(ArgTypeName), index, True);
      if index < 0 then

        SearchFail := True;
    end;
    if (not DT) and (not SimpleType) and (SearchFail) then
    begin
      WrongType := True;
      Break;
    end;
    if (CArg.Access = argConst) then
      Access := 'const'
    else if (CArg.Access = argDefault) then
      Access := 'def'
    else if (CArg.Access = argVar) or (CArg.Access = argOut) then
      Access := 'var'
    else
      WrongType := True;
    ParsedArg := TparsedParameter.Create(ArgName, Access);
    ParsedArg.parameterType := ArgTypeName;
    ParsedArg.isSimpleType := SimpleType;
    ParsedArg.isDefaultType := Dt;
    if (not SimpleType) and (not Dt) then
      ParsedArg.SetparameterTypeO(PFIS, index);
    o.paramaterList.Add(ParsedArg);
  end;
  if WrongType then
    FreeAndNil(o)
  else
  begin
    if ATPO then
      ParsedObject.Add(o);
  end;
  Result := o;
end;

function TLCLParser2.GetSetData(S: TPasSetType): TParsedObject;
var
  PTName: string;
  EN: TPasEnumType;
  PT: TPasType;
  PPT, PEN: TParsedObject;
  PS: TParsedSet;
  index: integer;
begin
  Result := nil;
  if not Assigned(s.EnumType) then
    Exit(nil);
  if (s.EnumType is TPasEnumType) then
  begin
    EN := s.EnumType as TPasEnumType;
    PEN := GetEnumType(EN);
  end
  else
  begin
    PT := s.EnumType as TPasType;
    PTName := Pt.Name;
    PEN := ParseIdentTifire(LowerCase(PTName), index, True);
    if PPT = nil then
      Exit(nil);
  end;
  PS := TParsedSet.Create;
  ps.Enum := PEN as TParsedEnum;
  ps.TParsedObjectName := s.Name;
  PS.FileName := CurrentFile.Name;
  ParsedObject.Add(PS);
  CW(PS.Enum.Names[0]);
  Result := PS;
end;

function TLCLParser2.GetEnumType(EN: TPasEnumType): TParsedObject;
var
  PE: TParsedEnum;
begin
  PE := TParsedEnum.Create;
  EN.GetEnumNames(Pe.Names);
  if PE.Names.Count > 32 then
  begin
    PE.Free;
    Exit(nil);
  end;
  ParsedObject.Add(PE);
  Result := PE;
end;

function TLCLParser2.ParseElement(E: TPasElement): TParsedObject;
begin
  Result := nil;
  if E is TPasClassType then
    Result := GetClassData(E as TPasClassType)
  else if E is TPasProcedureType then
    Result := GetProcedureType(E as TPasProcedureType)
  else if E is TPasSetType then
    Result := GetSetData(E as TPasSetType)
  else if E is TPasEnumType then
    Result := GetEnumType(E as TPasEnumType);
end;

function TLCLParser2.ParseIdentTifire(c: string; var Index: integer;
  ristrict: boolean = False): TParsedObject;
var
  TokenIndex, m, UI: integer;
  CFile, oldCurrentfile: TPasModule;
  Search, found: boolean;
  E: TPasElement;
  Cuses, clname, CFilename, CurrentFileName: string;
  cPFI: TPFI;
begin
  Result := nil;
  if CompareText(c, 'tmousemoveevent')=0 then
  begin
    WriteLn('lll');
    // Exit;
  end;
  oldCurrentfile := CurrentFile;
  index := PFIS.IndexOf(LowerCase(c) + '_0');
  found := False;
  if (Index > -1) and (ristrict) then
  begin
    found := CheckInUses(oldCurrentfile, Index);
    if not found then
      raise Exception.Create('not found ');
  end;
  if (Index > -1) and ((not ristrict) or found) then
  begin
    cPFI := (PFIS.Data[Index] as TPFI);
    if not (cPFI.Processed) then
    begin
      cPFI.Processed := True;
      CurrentFile := cPFI.M;
      cPFI.Ob := ParseElement(cPFI.E);
    end;
    Result := cPFI.Ob;
  end;
 { if Assigned(CurrentFile) then
    CurrentFileName := CurrentFile.Name;
  for k := 0 to ParsedFiles.Count - 1 do
  begin
    CFile := ParsedFiles[k] as TPasModule;
    Search := False;
    CFilename := CFile.Name;
    if (ristrict) and ((CurrentFileName <> CFilename)) then
    begin
      for m := 0 to Length(CurrentFile.InterfaceSection.UsesClause) - 1 do
      begin
        Cuses := LowerCase(CurrentFile.InterfaceSection.UsesClause[m].Module.FullName);
        if Cuses = CFile.Name then
          Search := True;
      end;
    end
    else
      Search := True;
    if not Search then
      Continue;
    E := findPasElement(LowerCase(c), CFile);
    if (E <> nil) then
    begin
      clname := E.ClassName;
      CurrentFile := CFile;
      Result := ParseElement(E);
    end;
  end;                   }
  CurrentFile := oldCurrentfile;
end;

function TLCLParser2.AddIndex(Iname: string): integer;
var
  k: integer;
  ckey: string;
begin
   Iname:=LowerCase(IName);
  k := PFIS.IndexOf((IName));
  if k < 0 then
    Exit(0);
  ckey := PFIS.Keys[k];
  while ckey.Contains(Iname + '_') do
  begin
    Inc(k);
    ckey := PFIS.Keys[k];
  end;
  Result := k;
end;

procedure TLCLParser2.ParseFile(const FileName, path: string);
var
  k, I: integer;
  Decls: TFPList;
  E: TSimpleEngine;
  M: TPasModule;
  IName: string;
  CPFI: TPFI;
  PU: TparsedUses;
begin
  E := TSimpleEngine.Create;
  M := nil;
  try
    M := ParseSource(E, path + FileName, 'linux', 'i386');
    ParsedFiles.Add(m);
      { Cool, we successfully parsed the module.
        Now output some info about it. }
    if M.InterfaceSection <> nil then
    begin
      CW(m.InterfaceSection.UsesClause[0].Module.FullName);
      Decls := M.InterfaceSection.Declarations;
      for I := 0 to Decls.Count - 1 do
      begin
        IName := (TObject(Decls[I]) as TPasElement).Name;
        CW('Interface item ' + I.ToString() + ' : ' + IName);
        CPFI := TPFI.Create(IName, FileName, TObject(Decls[I]) as TPasElement, M);
        PFIS.Add(LowerCase(IName) + '_' + AddIndex(IName).ToString(), CPFI);
      end;
    end
    else
      CW('No interface section --- this is not a unit, this is a ' + M.ClassName);
    PU := TparsedUses.Create;
    Pu.FileName := ExtractFileNameWithoutExt(ExtractFileName(FileName));
    for k := 0 to Length(m.InterfaceSection.UsesClause) - 1 do
    begin
      CW(m.InterfaceSection.UsesClause[k].Module.FullName);
      PU.useslist.Add(m.InterfaceSection.UsesClause[k].Module.FullName);
    end;
    ParsedObject.Add(PU);
  finally
    // FreeAndNil(M);
    FreeAndNil(E)
  end;
end;

procedure TLCLParser2.CW(Text: string);
begin
  // WriteLn(Text);
end;

function TLCLParser2.ProcessDefinedProperty(p: TPasProperty;
  CN: string): TParsedProperty;
var
  DT, SimpleType: boolean;
  O: TParsedProperty;
  Ctype: TParsedObject;
  CTypeName, CArgTypeName: string;
  index, k: integer;
  CArg: TPasArgument;
  CPara: TparsedParameter;
begin
  SimpleType := False;
  CTypeName := p.VarType.Name;
  index := -1;
  Ctype := GetParamterType(CTypeName, SimpleType, DT, index);
  if Ctype is TParsedProcedureType then
  begin
    if (Ctype as TParsedProcedureType).hasResult then
    cw('iss function');
  end;
  {if (Ctype = nil) and (not SimpleType) and (not DT) then
    Exit(nil);    }
  O := TParsedProperty.Create;
  o.LinkedProperty := nil;
  O.TParsedObjectName := p.Name;
  O.TParsedObjectType := CTypeName;
  O.Setproptype(@NilParsedObject);
  if index > -1 then
    o.Setproptype(@((PFIS.Data[Index] as TPFI).Ob));
  o.memberof := CN;
  o.IsReadable := p.ReadAccessor <> nil;
  o.IsWritable := p.WriteAccessor <> nil;
  o.isSimple := SimpleType;
  o.isDefaultType := Dt;
  if ((P.Visibility = visPublic) or (P.Visibility = visPublished)) then
    o.AccesModifir := 'public'
  else
    o.AccesModifir := 'private';
  o.FileName := CurrentFile.Name;
  if p.Args.Count > 0 then
  begin
    o.Isindexed := True;
    for k := 0 to p.Args.Count - 1 do
    begin
      CArg := TPasArgument(p.Args[k]);
      if CompareText(CArg.ArgType.Name, 'Integer') <> 0 then
      begin
        WriteLn(o.memberof + ' ' + o.TParsedObjectName + ' index ' +
          CArg.Name + ' ' + CArg.ArgType.Name);
        Exit(nil);
      end;
      CPara := TparsedParameter.Create(CArg.Name, 'const');
      CPara.isSimpleType := True;
      CPara.parameterType := 'Integer';
      o.paramaterList.Add(CPara);
    end;
  end
  else
    o.Isindexed := False;
  Result := O;
end;

function TLCLParser2.ProcessUNDefinedProperty(const CO: TParsedClass;
  const p: TPasProperty): TParsedProperty;
var
  Temp: TObject;
  PPI: integer;
  CCS: TParsedClass;
  O, LinkedProp: TParsedProperty;
  TempCname: string;
begin
  O := nil;
  CCS := Co.ParentclassO;//class chain Head
  while True do
  begin
    if Assigned(CCS) then
    begin
      PPI := CCs.Members.IndexOf(p.Name);//parent class index
      if PPI > -1 then
      begin
        Temp := (CCs.Members[p.Name]);
        TempCname := Temp.ClassName;
        LinkedProp := Temp as TParsedProperty;
        if LinkedProp.AccesModifir = 'public' then
          break;
        O := TParsedProperty.Create;
        o.LinkedProperty := LinkedProp;
        O.TParsedObjectName := p.Name;
        O.memberof := Co.TParsedObjectName;
        O.FileName := Co.FileName;
        if ((P.Visibility = visPublic) or (P.Visibility = visPublished)) then
          o.AccesModifir := 'public'
        else
          o.AccesModifir := 'private';
        Break;
      end;
    end
    else
      Break;
    CCS := CCs.ParentclassO;
  end;
  Result := O;
end;

function TLCLParser2.CheckInUses(var oldCurrentfile: TPasModule;
  var Index: integer): boolean;
var
  cPFI2: TPFI;
  Target: string;
  CU: string;
  found: boolean;
  k: integer;
begin
  cPFI2 := (PFIS.Data[Index] as TPFI);
  Target := ((ExtractFileNameWithoutExt(cPFI2.FileName)));
  if CompareText(oldCurrentfile.Name, Target) = 0 then
    found := True
  else
  begin
    for k := 0 to oldCurrentfile.InterfaceSection.UsesList.Count - 1 do
    begin
      CU := oldCurrentfile.InterfaceSection.UsesClause[k].Module.FullName;
      if CompareText(Target, CU) = 0 then
        found := True;
    end;
  end;
  Result := found;
end;

function TLCLParser2.HasConstructor(O: TParsedClass; var ConIndex: integer): boolean;
var
  ConstructorFound: boolean;
  k: integer;
begin
  Result := False;
  ConIndex := -1;
  for k := 0 to o.Members.Count - 1 do
  begin
    if o.Members.Data[k] is TparsedConstructor then
    begin
      ConIndex := k;
      Exit(True);
    end;
  end;
end;

end.
