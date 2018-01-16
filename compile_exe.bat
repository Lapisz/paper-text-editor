@ECHO OFF
"C:\Program Files\Python36\python.exe" setup.py build
echo Finished compiling.
timeout 3 > nul