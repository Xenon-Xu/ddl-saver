@echo off
if "%1"=="h" goto min
start mshta vbscript:createobject("wscript.shell").run("""%~nx0"" h",0)(window.close)&&exit
:min
@python main.py