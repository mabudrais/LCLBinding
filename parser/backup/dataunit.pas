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

  end;

end.
