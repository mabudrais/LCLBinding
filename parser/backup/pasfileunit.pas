unit pasfileunit;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, fgl, PScanner, FileUtil;

type
  TIntegerList = specialize TFPGList<integer>;
  TTokenList = specialize TFPGList<TToken>;
  { TPasFile }

  TPasFile = class(TStringList)
    constructor Create(FileName: string; load: boolean = True);
    destructor Destroy; override;
  public
    PasFilename, FullPath: string;
    UsesFile: TStringList;
    DefinedIdentfire: TStringList;
    LineNumber: TIntegerList;
    tokens: TTokenList;
    Hide: boolean;
  private
    procedure Tokenize;
    procedure ParsUses;
  end;

implementation

{ TPasFile }

constructor TPasFile.Create(FileName: string; load: boolean = True);
begin
  inherited Create;
  UsesFile := TStringList.Create;
  DefinedIdentfire := TStringList.Create;
  LineNumber := TIntegerList.Create;
  tokens := TTokenList.Create;
  DefinedIdentfire.AddStrings(['integer', 'string', 'boolean', 'tobject',
    'tpersistent']);
  FullPath := FileName;
  PasFilename := ExtractFileNameWithoutExt(ExtractFileName(FileName));
  Tokenize;
  ParsUses;
end;

destructor TPasFile.Destroy;
begin
  UsesFile.Free;
  DefinedIdentfire.Free;
  LineNumber.Free;
  tokens.Free;
  inherited Destroy;
end;

procedure TPasFile.Tokenize;
var
  passcaner: TPascalScanner;
  fr: TFileResolver;
  token: TToken;
  ctokenstr: string;
begin
  fr := TFileResolver.Create;
  passcaner := TPascalScanner.Create(fr);
  passcaner.AddDefine('fpc', True);
  passcaner.OpenFile(FullPath);
  token := passcaner.FetchToken;
  while (token <> tkimplementation) and (token <> tkEOF) do
  begin
    if (token <> tkLineEnding) and (token <> tkWhitespace) and (token <> tkComment) then
    begin
      tokens.Add(token);
      LineNumber.Add(passcaner.CurRow);
      if passcaner.CurRow > 207 then
        ctokenstr := passcaner.CurTokenString;
      Self.Add(passcaner.CurTokenString.ToLower);
    end;
    token := passcaner.FetchToken;
  end;
  fr.Free;
  passcaner.Free;
end;

procedure TPasFile.ParsUses;
var
  tokenstring: string;
  token: TToken;
  k: integer;
begin
  k := 0;
  while (tokens[k] <> tkuses) and (k < tokens.Count) do
    Inc(k);
  if k = tokens.Count then
    Exit;
  Inc(k);
  token := tokens[k];
  while token <> tkSemicolon do
  begin
    if token = tkIdentifier then
      self.UsesFile.Add(Self.Strings[k]);
    Inc(k);
    token := tokens[k];
  end;
end;

end.
