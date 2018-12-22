unit parsedobjectunit;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, contnrs, dataunit;

type

  TParsedObject = class
    TParsedObjectType, FileName, TParsedObjectName, memberof: string;
    Linenumber: integer;
  end;

  PTParsedObject = ^TParsedObject;
  { TparsedParameter }

  TparsedParameter = class
  private
    parsedObjectList: TObject;
    index: integer;
    function getparameterTypeO: TParsedObject;
  public
    parameterName, parameterType, parameterAcsess: string;
    isSimpleType, isDefaultType: boolean;
    property parameterTypeO: TParsedObject read getparameterTypeO;
    constructor Create(CparameterName, CparameterAcsess: string);
    procedure SetparameterTypeO(o: TObject; cindex: integer);
    //parameterAcsess cons var value
  end;

  { TparsedUses }

  TparsedUses = class(TParsedObject)
    useslist: TStringList;
    constructor Create;
  end;

  { TParsedProperty }

  TParsedProperty = class(TParsedObject)
  protected
    _proptype: PTParsedObject;
    function Getproptype: TParsedObject;
  public
    LinkedProperty: TParsedProperty;
    Isindexed, IsReadable, IsWritable, isSimple, isDefaultType: boolean;
    AccesModifir, Basicproptype: string;
    paramaterList: TObjectList;
    constructor Create;
    property proptype: TParsedObject read Getproptype;
    function GetLinkedProperty(): TParsedProperty;
    procedure Setproptype(PT: PTParsedObject);
  end;

  { TParsedClass }

  TParsedClass = class(TParsedObject)
    ParentClass: string;
    ParentclassO: TParsedClass;
    Members: TStringMap;
    constructor Create;
  end;

  { TParsedEnum }

  TParsedEnum = class(TParsedObject)
    Names: TStringList;
    constructor Create;
  end;

  TParsedSet = class(TParsedObject)
    Enum: TParsedEnum;
  end;

  { TParsedProcedureType }

  TParsedProcedureType = class(TParsedObject)
    paramaterList: TObjectList;
    hasResult: boolean;
    resultType: TparsedParameter;
    constructor Create;
    destructor Destroy; override;
  end;

  { TparsedFunction }
  TparsedFunction = class(TParsedProcedureType)
    pro: TParsedProcedureType;
    constructor Create;
  end;

  { TparsedConstructor }

  TparsedConstructor = class(TparsedFunction)
    LinkedConstructor: TparsedConstructor;
    constructor Create;
    procedure CopyDataFrom(Con: TparsedConstructor; memb, CFileName: string);
  end;

implementation

uses Parser2Unit;

{ TparsedConstructor }

constructor TparsedConstructor.Create;
begin
  inherited;
  LinkedConstructor := nil;
end;

procedure TparsedConstructor.CopyDataFrom(Con: TparsedConstructor;
  memb, CFileName: string);
begin
  Self.TParsedObjectName := Con.TParsedObjectName;
  Self.FileName := CFileName;
  Self.pro := TParsedProcedureType.Create;
  self.pro.TParsedObjectName := con.pro.TParsedObjectName;
  self.pro.paramaterList := con.pro.paramaterList;
  self.pro.memberof := memb;
  Self.pro.FileName := CFileName;
end;

{ TParsedProperty }

function TParsedProperty.GetLinkedProperty(): TParsedProperty;
var
  p: TParsedProperty;
begin
  if LinkedProperty = nil then
    Result := Self
  else
  begin
    p := Self;
    while p.LinkedProperty <> nil do
      p := p.LinkedProperty;
    Result := p;
  end;
end;

function TParsedProperty.Getproptype: TParsedObject;
begin
  Result := _proptype^;
end;

procedure TParsedProperty.Setproptype(PT: PTParsedObject);
begin
  _proptype := PT;
end;

constructor TParsedProperty.Create;
begin
  inherited;
  Self.paramaterList := TObjectList.Create;
end;

{ TParsedClass }

constructor TParsedClass.Create;
begin
  inherited;
  Members := TStringMap.Create;
  ParentclassO := nil;
  Members.Sorted := True;
end;

{ TParsedEnum }

constructor TParsedEnum.Create;
begin
  Names := TStringList.Create;
end;

{ TParsedProcedureType }

destructor TParsedProcedureType.Destroy;
var
  k: integer;
begin
  inherited Destroy;
  paramaterList.Free;
end;

constructor TParsedProcedureType.Create;
begin
  paramaterList := TObjectList.Create();
  hasResult := False;
end;

{ TparsedUses }

constructor TparsedUses.Create;
begin
  useslist := TStringList.Create;
end;

{ TparsedParameter }

constructor TparsedParameter.Create(CparameterName, CparameterAcsess: string);
begin
  parameterName := CparameterName;
  if CparameterAcsess <> 'val' then
    parameterAcsess := CparameterAcsess;
end;

function TparsedParameter.getparameterTypeO: TParsedObject;
var
  PFIS: TStringMap;
  cPFI: TPFI;
begin
  if (index < 0)or(Self.parsedObjectList=Nil) then
    Exit(nil);
  try
    PFIS := parsedObjectList as TStringMap;
    cPFI := (PFIS.Data[Index] as TPFI);
  except
    on e: Exception do
      writeln('ll');
  end;
  Result := cPFI.Ob;
end;

procedure TparsedParameter.SetparameterTypeO(o: TObject; cindex: integer);
begin
  Self.parsedObjectList := o;
  index := cindex;
end;

{ TparsedFunction }

constructor TparsedFunction.Create;
begin
  inherited;
end;

end.
