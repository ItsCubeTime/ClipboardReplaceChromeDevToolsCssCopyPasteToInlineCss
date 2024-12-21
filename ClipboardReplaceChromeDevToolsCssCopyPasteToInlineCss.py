import subprocess
import sys
import pathlib
try:
    import clipboard
except:
    def install(package):
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    install('clipboard')
    import clipboard

r = ''
inputStr:str = clipboard.paste()

lines=inputStr.split('\n')
for line in lines:
    pair=line.split(' ',1)
    r+=f'''{pair[0]}:{pair[1]};'''
clipboard.copy(r.replace('\n','').replace('\r',''))
