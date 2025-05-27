'''
T1112 - Modify Registry
'''

import winreg

hive1 = winreg.HKEY_CURRENT_USER
subkey = r'Software\\Microsoft\\Windows\\CurrentVersion\\Policies'

#open key 
key = winreg.OpenKeyEx(hive1, subkey)
print(f"{subkey} Opened Succesfully")

#delete key
winreg.DeleteKey()