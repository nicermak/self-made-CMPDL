#import a lot of trash
import json
from shutil import move, Error
import requests
import re
import zipfile
from webbrowser import open_new_tab as sajh
from os import path, makedirs, rmdir, replace, listdir, rename, rmdir
from sys import argv

#var
fuak = str(argv[2]).replace(".zip", "")
#fun
def gffcd(cd):
    if not cd:
        return None
    fn = re.findall('filename=(.+)', cd)
    if len(fn) == 0:
        return None
    return fn[0]
def dfile(url, header, name):
    r = requests.get(url, headers=header,allow_redirects=True)
    global fuak
    fuak = str(argv[2]).replace(".zip", "")
    try:
        open(f'.\{fuak}\mods\{name}', 'wb').write(r.content)
    except FileNotFoundError:
        makedirs(fuak)
        makedirs(f'{fuak}\mods')
def idExists(object):
    if len(object) == 1:
        return False
    else:
        return True
#code
if path.exists('token.json'):
    aasja = open('token.json', encoding='utf-8', mode='r+')
    aasjf = aasja.read()
    hauj = json.loads(aasjf)
    try:
        if len(hauj['API_KEY']) < 0:
            aasja.write('{\n    "API_KEY":""\n}')
            print("invaild token.json,\n token.json reseted. you can find 'API key' in:\nhttps://console.curseforge.com/?#/api-keys")
        else:
            global API_KEY
            API_KEY = hauj['API_KEY']
    except KeyError:
        aasja.write('{\n    "API_KEY":""\n}')
        print("invaild token.json,\n token.json reseted. you can find 'API key' in:\nhttps://console.curseforge.com/?#/api-keys")
else:
    aldgjh = open('token.json', encoding='utf-8', mode='w')
    print("token.json doesn't exist,\ncreating new one,\nyou can find 'API_KEY' in:\nhttps://console.curseforge.com/?#/api-keys")
    aldgjh.write('{\n    "API_KEY":""\n}')
if idExists(argv):
    if argv[1].startswith("-"):
        if argv[1] == "-help":
            print("list of command:\n -about about the apps\n -f <file> decompile the modpack as folder(without version.jar)\n -help  print the list")
        if argv[1] == "-about":
            sajh("https://youtu.be/dQw4w9WgXcQ")
        if argv[1] == "-f":
            print(f'trying to open {argv[2]}')
            if path.exists(argv[2]):
                global sa
                sa = zipfile.ZipFile(argv[2], mode='r')
                global ls
                l = sa.read('manifest.json')
                f = l.decode('utf-8').replace("'", '"')
                h = json.dumps(f)
                ls = json.loads(f)
                ja = 0
                for olo in range(len(ls['files'])):
                    try:
                        ha = ls['files'][ja]['projectID']
                        oa = ls['files'][ja]['fileID']
                        header = {'Accept': 'application/json', 'x-api-key':f'{API_KEY}'}
                        mu = requests.get(f'https://api.curseforge.com/v1/mods/{ha}/files/{oa}', headers=header)
                        ma = mu.json()
                        if path.exists(f"{fuak}/mods/{ma['data']['fileName']}"):
                            print(f"[Error]file {ma['data']['fileName']} already existed skipping to next file")
                            ja = ja+1
                            continue
                        else:
                            print(f"downloading   {ma['data']['downloadUrl']}...")
                            dfile(ma['data']['downloadUrl'], header, ma['data']["fileName"])
                            ja = ja + 1

                    except requests.exceptions.MissingSchema:
                        print(f'[Error]files {oa} is missing download url')
                        ja = ja + 1
                        continue
                for file in sa.namelist():
                    if file.startswith(f"{ls['overrides']}/"):
                        sa.extract(file, f'{ls["overrides"]}/')
                alls = listdir(ls['overrides'])
                print(alls)
                for one in alls:
                    try:
                        print(f"{one} => {fuak}")
                        move(f"{ls['overrides']}/" + one, f"{fuak}/")
                    except Error:
                        pass
                print("modpack need modloader to launch,\n the app can't automatic download modloader.\nplease manually download modloader")
                la = ls['minecraft']['modLoaders']
                print(f"modloader:{la}\nversion: {ls['minecraft']['version']}")
                rmdir(ls['overrides'])

                
        
                
            else:
                print("zip isn't exist")
    else:
        print('type -help for list of commands')
else:
    print('type -help for list of commands')
