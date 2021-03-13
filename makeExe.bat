d:
cd D:\dev\python3\rhodes-no-workers-desktop\

del *.spec
rd /s /q build 
rd /s /q dist

pyinstaller -w -i "src/icon.ico" "__init__.py" --hidden-import PyQT5.sip

xcopy src dist\__init__\src\ /s
xcopy page dist\__init__\page\ /s

copy LICENSE dist\__init__\

pause