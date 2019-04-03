import subprocess
import sys

with open('requirements.txt','r') as f:
    for requirement in f.readlines():
        subprocess.call([sys.executable, "-m", "pip", "install",requirement])