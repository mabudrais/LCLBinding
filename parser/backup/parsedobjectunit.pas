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
    parameterName, parameterType, parameterAcsess: string;
    parameterTypeO: TParsedObject;
    isSimpleType, isDefaultType: boolean;
    constructor Create(CparameterName, CparameterAcsess: string);
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
    index1, index2, IndexType, AccesModifir, Basicproptype: string;
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

{ TparsedConstructor }

constructor TparsedConstructor.Create;
begin
  inherited;
  LinkedConstructor := nil;
end;

procedure TparsedConstructor.CopyDataFrom(Con: TparsedConstructor; memb,
  CFileName: string);
begin
  Self.TParsedObjectName := Con.TParsedObjectName;
  Self.FileName:=CFileName;
  Self.pro := TParsedProcedureType.Create;
  self.pro.TParsedObjectName := con.pro.TParsedObjectName;
  self.pro.paramaterList := con.pro.paramaterList;
  self.pro.memberof:=memb;
  Self.pro.FileName:=CFileName;
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

{ TparsedFunction }

constructor TparsedFunction.Create;
begin
  inherited;
end;

end.
