unit Parserunit;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, contnrs, pasfileunit, LazFileUtils, PScanner, parsedobjectunit;

type

  { TLCLParser }

  TLCLParser = class
    constructor Create(fileList: TObjectList; CTargetClass: TStrings);
  private
    Lineindex, charindex: integer;
    CurrentFile: TPasFile;
    targetfile: TObjectList;
    TargetClass: TStringList;
    fr: TFileResolver;
    passcaner: TPascalScanner;
    function findDifintionTokenIndex(IdentTifire: string): integer;

    function IsDifintion(IdentTifire: string; tokenindex: integer): boolean;
    function isSeoratorChar(c: string): boolean;
    function ParseAccessModifire(LCLclassName, FileName: string;
      var tokenindex: integer; var AccessModifire: string): boolean;
    function ParseClass(IdentTifireName: string; tokenIndex: integer): TParsedClass;
    function ParseIdentTifire(c: string; ristrict: boolean = False): TParsedObject;
    function ParseIdentTifire(IdentTifireName: string;
      tokenindex: integer): TParsedObject;
    procedure GetWords(number: integer; Words: TStrings;
      var tokens: array of ttoken);
    function GetClassName(var LCLclassName, LCLParentclassName: string;
      tokenIndex: integer): boolean;
    function ParseProperties(LCLclassName, FileName, NewAccessModifire: string;
      var Wordnum: integer): boolean;
    function ParseVarDeclration(LCLclassName, FileName, NewAccessModifire: string;
      var Wordnum: integer): boolean;
    function ParseConstructor(LCLclassName, FileName: string;
      var tokenindex: integer; AccessModifire: string): boolean;
    function ATT(t, tt: TToken): boolean;
    procedure ParsUndifinedProperty(var Wordnum: integer);
    procedure HideUnusedFile;
    procedure ExtractPropertyRW(var Wordnum: integer; var R, W: boolean);
    procedure parseParameter(var tokenindex: integer; paralist: TList);
    function setprivouseParamertype(const cword: string; paralist: TList): boolean;
    function Parsetype(pasType: string; out obj: TParsedObject): string;
  public
    ErrorMsg: TStrings;
    ParseResult: TObjectList;
    procedure Parse;
  end;


implementation


{ TLCLParser }

constructor TLCLParser.Create(fileList: TObjectList; CTargetClass: TStrings);

begin
  targetfile := fileList;
  TargetClass := TStringList.Create;
  ErrorMsg := TStringList.Create;
  TargetClass.AddStrings(CTargetClass);
  ParseResult := TObjectList.Create;
  //removeMultilinecomment();
  //removelinecomment();
  //TokinizeFlles;
end;


function TLCLParser.isSeoratorChar(c: string): boolean;
begin
  Result := False;
  if (c = ',') or (c = ';') or (c = ')') or (c = '(') or (c = '[') or
    (c = ']') or (c = ':') or (c = '=') then
    Result := True;
end;


function TLCLParser.GetClassName(var LCLclassName, LCLParentclassName: string;
  tokenIndex: integer): boolean;
var
  isclass: boolean;
begin
  isclass := False;
  if CurrentFile.tokens[tokenIndex + 2] = tkclass then
  begin
    LCLclassName := CurrentFile.Strings[tokenIndex];
    if (CurrentFile.tokens[tokenIndex + 3] <> tkBraceOpen) and
      (CurrentFile.tokens[tokenIndex + 3] <> tkSemicolon) then
      isclass := True;
    if (CurrentFile.tokens[tokenIndex + 3] = tkBraceOpen) and
      (CurrentFile.tokens[tokenIndex + 6] <> tkSemicolon) then
    begin
      isclass := True;
      LCLParentclassName := CurrentFile.Strings[tokenIndex + 4];
    end;
    if not isclass then
      Exit(False);
  end;
  Result := isclass;
end;

function TLCLParser.IsDifintion(IdentTifire: string; tokenindex: integer): boolean;
begin
  Result := False;
  if (CurrentFile.tokens[tokenindex + 1] = tkEqual) then
  begin
    if CurrentFile.tokens[tokenindex + 2] = tkprocedure then
      Exit(True);
    if CurrentFile.tokens[tokenindex + 2] = tkBraceOpen then
      Exit(True);
    if CurrentFile.tokens[tokenindex + 2] = tkset then
      Exit(True);
    if CurrentFile.tokens[tokenindex + 2] = tkclass then
    begin
      if (CurrentFile.tokens[tokenindex + 3] <> tkBraceOpen) and
        (CurrentFile.tokens[tokenindex + 3] <> tkSemicolon) then
        Exit(True);
      if (CurrentFile.tokens[tokenindex + 3] = tkBraceOpen) and
        (CurrentFile.tokens[tokenindex + 6] <> tkSemicolon) then
        Exit(True);
    end;
  end;
end;

function TLCLParser.findDifintionTokenIndex(IdentTifire: string): integer;
var

  token: TToken;
  k: integer;
begin
  Result := -1;
  k := 0;
  token := CurrentFile.tokens[k];
  while token <> tkEOF do
  begin
    if (token = tkIdentifier) and (CurrentFile.Strings[k].ToLower = IdentTifire) then
    begin
      if IsDifintion(LowerCase(IdentTifire), k) then
        Exit(k);
    end;
    Inc(k);
    if k >= CurrentFile.Count then
      Exit;
    token := CurrentFile.tokens[k];
  end;
end;

function TLCLParser.ParseVarDeclration(LCLclassName, FileName, NewAccessModifire: string;
  var Wordnum: integer): boolean;
var
  cword: string;
begin
  Result := False;
  cword := CurrentFile[Wordnum];
  if (CurrentFile.tokens[Wordnum] = tkIdentifier) and
    (CurrentFile.tokens[Wordnum + 1] = tkColon) then
  begin
    while CurrentFile.tokens[Wordnum] <> tkSemicolon do
      Inc(Wordnum);
    Result := True;
  end;
end;

function TLCLParser.Parsetype(pasType: string; out obj: TParsedObject): string;
begin
  Result := '';
  obj := nil;
  if CurrentFile.DefinedIdentfire.IndexOf(pasType) > -1 then
    Exit(pasType);
  obj := ParseIdentTifire(pasType, True);
  if obj <> nil then
    Exit(pasType);
end;

function TLCLParser.ParseProperties(LCLclassName, FileName, NewAccessModifire: string;
  var Wordnum: integer): boolean;
var
  Cword, word3, propertyName, PropertyType: string;
  PropertyObj: TParsedProperty;
  oldWordNum: integer;
  R, W: boolean;
begin
  Result := False;
  oldWordNum := Wordnum;
  R := False;
  w := False;
  if CurrentFile.tokens[Wordnum] = tkproperty then
  begin
    Inc(Wordnum);
    propertyName := CurrentFile[Wordnum];
    Inc(Wordnum);
    word3 := CurrentFile[Wordnum];
    if (CurrentFile.tokens[Wordnum] = tkSemicolon) or (word3 = 'default') then
      ParsUndifinedProperty(Wordnum);
    if CurrentFile.tokens[Wordnum] = tkColon then
    begin
      Inc(Wordnum);
      PropertyType := CurrentFile[Wordnum];
      ExtractPropertyRW(Wordnum, R, W);
    end;
    if word3 = '[' then //this is more complicated
      Exit(False);
    PropertyObj := TParsedProperty.Create;
    //PropertyObj.Basicproptype:=Parsetype(PropertyType,PropertyObj.proptype);
    PropertyObj.Linenumber := CurrentFile.LineNumber[oldWordNum];
    PropertyObj.Isindexed := False;
    PropertyObj.FileName := FileName;
    PropertyObj.memberof := LCLclassName;
    PropertyObj.TParsedObjectName := propertyName;
    PropertyObj.TParsedObjectType := PropertyType;
    PropertyObj.IsReadable := R;
    PropertyObj.IsWritable := W;
    PropertyObj.AccesModifir := NewAccessModifire;
    if (PropertyType.Length = 0) or
      (CurrentFile.DefinedIdentfire.IndexOf(PropertyType) > -1) then
      ParseResult.Add(PropertyObj)
    else
      ErrorMsg.Add('undefined type ' + PropertyType);
    Result := True;
  end;
  if Result = False then
    Wordnum := oldWordNum;
end;

function TLCLParser.ParseAccessModifire(LCLclassName, FileName: string;
  var tokenindex: integer; var AccessModifire: string): boolean;
var
  Cword: string;
  ctoken: TToken;
begin
  Result := False;
  Cword := CurrentFile[tokenindex];
  if CurrentFile.tokens[tokenindex] <> tkIdentifier then
    Exit;
  if (Cword = 'private') or (Cword = 'public') or (Cword = 'protected') or
    (Cword = 'published') then
  begin
    Result := True;
    AccessModifire := Cword;
  end;
end;

function TLCLParser.ParseConstructor(LCLclassName, FileName: string;
  var tokenindex: integer; AccessModifire: string): boolean;
var
  cConstructor: TparsedConstructor;
begin
  Result := False;
  if CurrentFile.tokens[tokenindex] <> tkconstructor then
    Exit(False);
  Inc(tokenindex);
  cConstructor := TparsedConstructor.Create;
  cConstructor.memberof := LCLclassName;
  cConstructor.FileName := FileName;
  cConstructor.Linenumber := CurrentFile.LineNumber[tokenindex];
  cConstructor.TParsedObjectType := LCLclassName;
  cConstructor.TParsedObjectName := CurrentFile[tokenindex];
  Inc(tokenindex);
  parseParameter(tokenindex, cConstructor.paramaterList);
  if cConstructor.paramaterList.Count > 0 then
    Inc(tokenindex);
  if CurrentFile.tokens[tokenindex] <> tkSemicolon then
    raise Exception.Create('constroctor end with' + CurrentFile[tokenindex]);
  ParseResult.Add(cConstructor);
  Result := True;
end;

function TLCLParser.ParseClass(IdentTifireName: string;
  tokenIndex: integer): TParsedClass;
var
  LCLclassName, LCLParentclassName, FileName, NewAccessModifire,
  showme, AccessModifire: string;
  isclass, wrongParse: boolean;
  ParsedClass: TParsedClass;
  ctoken: TToken;
  tokenLine: longint;
  ParentClassObj: TParsedObject;
begin
  tokenLine := CurrentFile.LineNumber[tokenIndex];
  if not GetClassName(LCLclassName, LCLParentclassName, tokenIndex) then
    Exit(nil);
  ParsedClass := TParsedClass.Create;
   ParseResult.Add(ParsedClass);
  FileName := CurrentFile.PasFilename;
  Inc(tokenIndex, 3);
  if not LCLParentclassName.IsEmpty then
  begin
    while CurrentFile.tokens[tokenIndex] <> tkBraceClose do
      Inc(tokenIndex);
    Inc(tokenIndex);
  end;
  ctoken := CurrentFile.tokens[tokenIndex];
  AccessModifire := 'puplic';
  while ctoken <> tkend do
  begin
    wrongParse := False;
    if ParseAccessModifire(LCLclassName, FileName, tokenIndex, AccessModifire) then
    else if ParseProperties(LCLclassName, FileName, AccessModifire, tokenIndex) then
    else if ParseVarDeclration(LCLclassName, FileName, AccessModifire, tokenIndex) then
    else if ParseConstructor(LCLclassName, FileName, tokenIndex, AccessModifire) then
    else
      wrongParse := True;
    if wrongParse then
    begin
      ErrorMsg.Add(LCLclassName + ' ' + tokenIndex.ToString() +
        ' ' {+GetWord(Wordnum)} + ' ' + CurrentFile.LineNumber[tokenIndex].ToString());
      ctoken := CurrentFile.tokens[tokenIndex];
      while ctoken <> tkSemicolon do
      begin
        Inc(tokenIndex);
        ctoken := CurrentFile.tokens[tokenIndex];
      end;
    end;
    Inc(tokenIndex);
    ctoken := CurrentFile.tokens[tokenIndex];
    //CWord := GetWord(tokenIndex);
  end;
  if CurrentFile.tokens[tokenIndex + 1] <> tkSemicolon then
    raise Exception.Create('unusal class end');
  ParentClassObj := ParseIdentTifire(LCLParentclassName, True);
  ParsedClass.TParsedObjectName:=LCLclassName;
  ParsedClass.FileName:=FileName;
  ParsedClass.ParentClass := LCLParentclassName;
  if ParentClassObj <> nil then
    ParsedClass.ParentclassO := ParentClassObj as TParsedClass;
end;

function TLCLParser.ParseIdentTifire(IdentTifireName: string;
  tokenindex: integer): TParsedObject;
var
  k: integer;
  Filename: string;
  PasFile: TPasFile;
begin
  if ParseClass(IdentTifireName, tokenindex) = nil then
    ErrorMsg.Add('ParseIdentTifire Faile ' + IdentTifireName);
end;

function TLCLParser.ParseIdentTifire(c: string;
  ristrict: boolean = False): TParsedObject;
var
  k, TokenIndex: integer;
  cid: TParsedObject;
begin
  Result := nil;
  if ristrict then
    HideUnusedFile();
  for k := 0 to targetfile.Count - 1 do
  begin
    CurrentFile := targetfile[k] as TPasFile;
    if (CurrentFile.Hide) and (ristrict) then
      Continue;
    TokenIndex := findDifintionTokenIndex(LowerCase(c));
    if (TokenIndex > -1) then
    begin
      cid := ParseIdentTifire(c, TokenIndex);
      if cid <> nil then
        Exit(cid);
    end;
  end;
end;

procedure TLCLParser.Parse;
var
  c: string;
  k: integer;
  U: TparsedUses;
begin
  for k := 0 to targetfile.Count - 1 do
  begin
    U := TparsedUses.Create;
    u.FileName := (targetfile[k] as TPasFile).PasFilename;
    u.useslist.AddStrings((targetfile[k] as TPasFile).UsesFile);
    ParseResult.Add(U);
  end;
  for c in TargetClass do
  begin
    for k := 0 to targetfile.Count - 1 do
      (targetfile[k] as TPasFile).Hide := False;
    ParseIdentTifire(c);
  end;
end;

procedure TLCLParser.ParsUndifinedProperty(var Wordnum: integer);
begin
  while CurrentFile.tokens[Wordnum] <> tkSemicolon do
    Inc(Wordnum);
end;

procedure TLCLParser.HideUnusedFile;
var
  k: integer;
  PasFile: TPasFile;
  Filename: string;
begin
  for k := 0 to targetfile.Count - 1 do
  begin
    PasFile := targetfile[k] as TPasFile;
    PasFile.Hide := False;
    Filename := ExtractFileNameOnly(PasFile.PasFilename);
    if (CurrentFile.UsesFile.IndexOf(Filename) < 0)and(not(CurrentFile = PasFile)) then
      PasFile.Hide := True;
  end;
end;

function TLCLParser.ATT(t, tt: TToken): boolean;
begin
  if t <> tt then
    raise Exception.Create('not equul token');
end;

procedure TLCLParser.ExtractPropertyRW(var Wordnum: integer; var R, W: boolean);
var
  CWord: string;
begin
  R := False;
  W := False;
  Inc(Wordnum);
  CWord := CurrentFile[Wordnum];
  while CurrentFile.tokens[Wordnum] <> tkSemicolon do
  begin
    if CWord = 'read' then
      R := True;
    if CWord = 'write' then
      W := True;
    Inc(Wordnum);
    CWord := CurrentFile[Wordnum];
  end;
end;

procedure TLCLParser.GetWords(number: integer; Words: TStrings;
  var tokens: array of ttoken);
var
  k: integer;
begin
  for k := 0 to number - 1 do
  begin
    tokens[k] := passcaner.FetchToken;
    Words.Add(passcaner.CurTokenString);
    if tokens[k] = tkEOF then
      Exit;
  end;
end;

procedure TLCLParser.parseParameter(var tokenindex: integer; paralist: TList);
var
  ctoken: TToken;
  cword, acces, cparatype: string;
  pretokencolon, pretokenequal: boolean;
begin
  ctoken := CurrentFile.tokens[tokenindex];
  if CurrentFile.tokens[tokenindex] = tkBraceOpen then
  begin
    Inc(tokenindex);
    ctoken := CurrentFile.tokens[tokenindex];
    cword := CurrentFile[tokenindex].ToLower;
    cparatype := '';
    acces := 'val';
    pretokencolon := False;
    pretokenequal := False;
    while CurrentFile.tokens[tokenindex] <> tkBraceClose do
    begin
      if (cword = 'var') or (cword = 'const') or (cword = 'out') then
        acces := cword
      else if ctoken = tkColon then
        pretokencolon := True
      else if ctoken = tkEqual then
        pretokenequal := True
      else if ctoken = tkSemicolon then
      begin
        acces := 'val';
        cparatype := '';
      end
      else if (pretokenequal) then
      begin
        if not (CurrentFile.tokens[tokenindex + 1] in [tkSemicolon, tkBraceClose]) then
          raise Exception.Create('unexpected after equle para' +
            CurrentFile.LineNumber[tokenindex].ToString());
      end
      else if (pretokencolon) and ATT(ctoken, tkIdentifier) then
        pretokencolon := setprivouseParamertype(cword, paralist)
      else if ATT(ctoken, tkIdentifier) then
        paralist.Add(TparsedParameter.Create(cword, acces));
      Inc(tokenindex);
      ctoken := CurrentFile.tokens[tokenindex];
      cword := CurrentFile[tokenindex].ToLower;
    end;
  end;
end;

function TLCLParser.setprivouseParamertype(const cword: string;
  paralist: TList): boolean;
var
  k: integer;
begin
  Result := False;
  for k := paralist.Count - 1 downto 0 do
  begin
    if TparsedParameter(paralist[k]).parameterType = '' then
      TparsedParameter(paralist[k]).parameterType := cword
    else
      Exit;
  end;
end;

end.
