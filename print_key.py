import winreg

hive = winreg.HKEY_LOCAL_MACHINE
subkey = r'SOFTWARE\\Microsoft\Windows NT\\CurrentVersion\Winlogon'
value_name = 'DefaultUsername'

key = winreg.OpenKey(hive, subkey)
key_value = winreg.QueryValueEx(key, value_name)
print(f"The value for {value_name} is {key_value[0]}")

winreg.CloseKey(key)

