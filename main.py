################################################################
#                       __               ___         ___       #
#                      /\ \             /\_ \      /'___`\     #
#  ___     ___ ___     \_\ \    _____   \//\ \    /\_\ /\ \    #
# /'___\ /' __` __`\   /'_` \  /\ '__`\   \ \ \   \/_/// /__   #
#/\ \__/ /\ \/\ \/\ \ /\ \L\ \ \ \ \L\ \   \_\ \_    // /_\ \  #
#\ \____\\ \_\ \_\ \_\\ \___,_\ \ \ ,__/   /\____\  /\______/  #
# \/____/ \/_/\/_/\/_/ \/__,_ /  \ \ \/    \/____/  \/_____/   #
#                                 \ \_\                        #
################################################################
#the temp researching code parts



#                        (while downloading)


#                        else:
#                            print(f"downloading   {ma['data']['downloadUrl']}...")
#                            dfile(ma['data']['downloadUrl'], header, ma['data']["fileName"])
#import a lot of trash
#because why not?     
import json
from shutil import move, Error
from time import sleep, perf_counter
from tkinter.messagebox import YES
import requests
import re
import zipfile
from webbrowser import open_new_tab as sajh
from os import path, makedirs, rmdir, replace, listdir, rename, rmdir
from sys import argv
from threading import Thread
#banner:
banner = """
                         __               ___         ___     
                        /\ \             /\_ \      /'___`\   
  ___     ___ ___       \_\ \    _____   \//\ \    /\_\ /\ \  
 /'___\  /' __` __`\    /'_` \  /\ '__`\   \ \ \   \/_/// /__ 
/\ \__/  /\ \/\ \/\ \  /\ \L\ \ \ \ \L\ \   \_\ \_    // /_\ \    
\ \____\ \ \_\ \_\ \_\ \ \___,_\ \ \ ,__/   /\____\  /\______/
 \/____/  \/_/\/_/\/_/  \/__,_ /  \ \       \/____/  \/_____/ 
                                   \_\                      
"""
print(banner, "\n                    Version: I forgor💀          ")
try:
    fuak = str(argv[2]).replace(".zip", "")
except IndexError:
    print("\n")
def gffcd(cd):
    if not cd:
        return None
    fn = re.findall('filename=(.+)', cd)
    if len(fn) == 0:
        return None
    return fn[0]
def dfile(url, header, name):
    if url == None:
        print("[ERR]Url = None")
    else:
        r = requests.get(url, headers=header,allow_redirects=True)
        global fuak
        fuak = str(argv[2]).replace(".zip", "")
        try:
            open(f'.\{fuak}\mods\{name}', 'wb').write(r.content)
        except FileNotFoundError:
            makedirs(fuak)
            makedirs(f'{fuak}\mods')
#read token parts
#code
if path.exists('token.json'):
    aasja = open('token.json', encoding='utf-8', mode='r+')
    aasjf = aasja.read()
    hauj = json.loads(aasjf)
    try:
        try:
            global API_KEY
            API_KEY = hauj['API_KEY']
        except IndexError:
            aasja.write('{\n    "API_KEY":""\n}')
            print("[ERR]invaild token.json,\n token.json reseted. you can find 'API key' in:\nhttps://console.curseforge.com/?#/api-keys")

    except KeyError:
        aasja.write('{\n    "API_KEY":""\n}')
        print("[ERR]invaild token.json,\n token.json reseted. you can find 'API key' in:\nhttps://console.curseforge.com/?#/api-keys")
else:
    aldgjh = open('token.json', encoding='utf-8', mode='w')
    print("[INF]token.json doesn't exist,\ncreating new one,\nyou can find 'API_KEY' in:\nhttps://console.curseforge.com/?#/api-keys")
    aldgjh.write('{\n    "API_KEY":""\n}')
try:
    if argv[1].startswith("-"):
        if argv[1] == "-help":
            print("list of command:\n -about about the apps\n -f <file> decompile the modpack as instance(without version.jar)\n -help  print the list")
        if argv[1] == "-about":
            sajh("https://youtu.be/dQw4w9WgXcQ")
        if argv[1] == "-f":
            #⩔⩔⩔ the main parts
            print(f'[INF]trying to open {argv[2]}')
            if path.exists(argv[2]):
                global sa
                sa = zipfile.ZipFile(argv[2], mode='r')
                #sa = zip files
                global ls
                l = sa.read('manifest.json')
                f = l.decode('utf-8').replace("'", '"')
                h = json.dumps(f)
                ls = json.loads(f)
                dlist = []
                nlist = []
                #ls = readed manifest.json
                #⩔⩔⩔ the download part
                t1_start = perf_counter()
                for i, a in enumerate(ls['files']):
                    try:
                        projID = ls['files'][i]['projectID']
                        fileID = ls['files'][i]['fileID']
                        header = {'Accept': 'application/json', 'x-api-key':f'{API_KEY}'}
                        mu = requests.get(f'https://api.curseforge.com/v1/mods/{projID}/files/{fileID}', headers=header)
                        ma = mu.json()
                        print("[INF]Collecting download url: " + ma['data']['fileName'])
                        if ma['data']['downloadUrl'] == None:
                            print(f"[ERR] projectID: {projID}, fileID: {fileID} is missing. skipping")
                        else:
                            dlist.append(ma['data']['downloadUrl'])
                            nlist.append(ma['data']['fileName'])
                    except requests.exceptions.MissingSchema:
                        print(f'[Error]files {fileID} is missing download url')
                        continue
                t1_end = perf_counter()
                print(f"[INF]Finished collect download url, time elapsed: {t1_end - t1_start} seconds")
                sleep(1)
                print("[INF]start the download part")
                #ths = the download threads
                t2_start = perf_counter()
                ths = []
                for i, aasdsa in enumerate(dlist):
                    j = int(i)
                    ths.append(Thread(target=dfile, args=(dlist[j], header, nlist[j])))
                for kabs in ths:
                    kabs.start()
                for kbbs in ths:
                    kbbs.join()
                try:
                    print(f"[INF]try to open {ls['overrides']}")
                    for file in sa.namelist():
                        if file.startswith(f"{ls['overrides']}/"):
                            sa.extract(file, f'{ls["overrides"]}/')
                    alls = listdir(f"{ls['overrides']}/{ls['overrides']}")
                    print(alls)
                    for one in alls:
                        try:
                            print(f"{one} => {fuak}")
                            move(f"{ls['overrides']}/{ls['overrides']}/" + one, f"{fuak}/")
                        except Error:
                            pass

                    sleep(1)
                    rmdir(f"{ls['overrides']}/{ls['overrides']}")
                    sleep(1)
                    rmdir(ls['overrides'])
                except KeyError:
                    print("[WRN]Overrides didn't exist")
                    pass
                except FileNotFoundError:
                    print("[ERR]override didn't exist, but it exist in manifest, check your modpack are somthing is missing?")
                print("modpack need modloader to launch,\n the app can't automatic download modloader.\nplease manually download modloader")
                la = ls['minecraft']['modLoaders']
                print(f"modloader:{la}\nversion: {ls['minecraft']['version']}")
                t2_end = perf_counter()
                print(f"\n[INF]Downloading part finished. time elapsed: {t2_end - t2_start} seconds")
                
#^^^ list of commands
    else:
        print('type -help for list of commands')
except IndexError:
    print('type -help for list of commands')
