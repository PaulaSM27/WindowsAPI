'''
Download 7zip
'''

import requests
from pathlib import Path
import shutil

path = str(Path.home()/"Downloads/7zip.exe")

url = "https://www.7-zip.org/a/7z2409-x64.exe"

response = requests.get(url, stream=True)
if response.status_code == 200:
    print("Connection Successful")
else: 
    print(f"Connection Failed. Status Code: {response.status_code}")

with open (path, 'wb') as file:
    shutil.copyfileobj(response.raw, file)

print(f"Download Successful. Path: {path}")