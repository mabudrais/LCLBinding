unit dataunit;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, fgl;

type
  TbooleanList = specialize TFPGList<boolean>;
  TStringMap = specialize TFPGMapObject<string, TObject>;
  function isDefinedSimpleIdentfire(T:String):Boolean;
implementation
  var
    DefinedSimpleIdentfire: TStringList=nil;

  function isDefinedSimpleIdentfire(T: String): Boolean;
  begin
    if not Assigned(DefinedSimpleIdentfire)then
    begin
      DefinedSimpleIdentfire := TStringList.Create;
  DefinedSimpleIdentfire.AddStrings(['integer', 'string', 'boolean',
    'double', 'tcaption']);
    end;
    Result:=DefinedSimpleIdentfire.IndexOf(T)>-1;
  end;

end.
