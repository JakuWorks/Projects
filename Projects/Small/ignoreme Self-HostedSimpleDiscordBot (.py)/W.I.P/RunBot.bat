@echo off

rem The below comment makes it easier to measure how long should the 'arrows' be.
rem "          Running .\Assets\RunBotPhase2.ps1
set "ArrowBody=---------------------------------"
set "RunBotPhase2_Path=.\Assets\RunBotPhase2.ps1"

echo %ArrowBody%^>
echo Setup Started!
echo Running %RunBotPhase2_Path%
echo ^<%ArrowBody%

@echo on

Powershell -noexit -nologo -ExecutionPolicy Bypass -Command %RunBotPhase2_Path%
