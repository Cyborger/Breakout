from cx_Freeze import setup, Executable

exe=Executable(
     script="main.py",
     base="Win32Gui",
     )
includefiles=["Resources"]
includes=[]
excludes=[]
packages=["pygame", "ZedLib"]
setup(
     version = "1.0",
     description = "Breakout clone",
     author = "Joe Zlonicky",
     name = "Breakout",
     options = {'build_exe': {'excludes':excludes,'packages':packages,'include_files':includefiles}},
     executables = [exe]
     )
