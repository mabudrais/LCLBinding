@echo off
SET THEFILE=lclexports.dll
echo Linking %THEFILE%
C:\lazarus\fpc\3.0.4\bin\i386-win32\ld.exe -b pei-i386 -m i386pe  --gc-sections  -s --dll  --entry _DLLMainCRTStartup   --base-file base.$$$ -o lclexports.dll link.res
if errorlevel 1 goto linkend
C:\lazarus\fpc\3.0.4\bin\i386-win32\dlltool.exe -S C:\lazarus\fpc\3.0.4\bin\i386-win32\as.exe -D lclexports.dll -e exp.$$$ --base-file base.$$$ 
if errorlevel 1 goto linkend
C:\lazarus\fpc\3.0.4\bin\i386-win32\ld.exe -b pei-i386 -m i386pe  -s --dll  --entry _DLLMainCRTStartup   -o lclexports.dll link.res exp.$$$
if errorlevel 1 goto linkend
C:\lazarus\fpc\3.0.4\bin\i386-win32\postw32.exe --subsystem console --input lclexports.dll --stack 16777216
if errorlevel 1 goto linkend
goto end
:asmend
echo An error occurred while assembling %THEFILE%
goto end
:linkend
echo An error occurred while linking %THEFILE%
:end
