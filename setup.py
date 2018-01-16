import sys
from cx_Freeze import setup, Executable
import os

os.environ['TCL_LIBRARY'] = r'C:\Program Files\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Program Files\Python36\tcl\tk8.6'

build_options = {"includes": ["tkinter"], "include_files": ["build/tcl86t.dll", "build/tk86t.dll", "build/paper_icon.ico"]}

setup(
    name = "Paper Text Editor",
    version = "0.1",
    options = {"build_exe": build_options},
    description = "A WIP text editor for a school assignment",
    executables = [Executable("paper.pyw", base = "Win32GUI")])