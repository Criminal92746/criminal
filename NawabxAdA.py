import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from PY6 import NAWAB
 
        NAWAB()
 
 
 
elif bit == "32bit":
 
        from PY3 import NAWAB
 
 
        NAWAB()
