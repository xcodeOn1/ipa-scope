import os 
from pip._vendor.colorama import Fore, Style
from time import sleep
import optparse
import json
import time as mm
import sys as n
from time import sleep
from pathlib import Path
def slow(M):  ## By Twitter : @Matrix0700
    for c in M + '\n':
        n.stdout.write(c)
        n.stdout.flush()
        mm.sleep(1. / 20)


def slow2(M):  ## By Twitter : @Matrix0700
    for c in M + '\n':
        n.stdout.write(c)
        n.stdout.flush()
        mm.sleep(1. / 25)


def slow1(M):  ## By Twitter : @Matrix0700
    for c in M + '\n':
        n.stdout.write(c)
        n.stdout.flush()
        mm.sleep(1. / 2000)
# Color 
Y = Fore.LIGHTYELLOW_EX + Style.BRIGHT
G = Fore.LIGHTGREEN_EX + Style.BRIGHT 
R = Fore.LIGHTRED_EX + Style.BRIGHT
W = Fore.LIGHTWHITE_EX + Style.BRIGHT 
B = Fore.LIGHTBLUE_EX + Style.BRIGHT 

# def unzip_ip(ipaFile,wereSaveIt):
#     try:
#          # zip the file and unzip it also take the app name
#         slow(f"[{Y}+{W}] wait now extra zip file")
#         sleep(3)
#         path_of_ipa = ipaFile
#         zip_ext = '.zip'
#         name_without_ext = os.path.splitext(path_of_ipa)[0]
#         file_after_zip = os.rename(path_of_ipa, name_without_ext + zip_ext)
#         zip_file_path = name_without_ext+".zip"
#         with ZipFile(zip_file_path, 'r') as Unzip:
#             Unzip.extractall(wereSaveIt)
    except FileNotFoundError:
        slow(f"\n[{R}!!{W}]{Y} Make sure app end with (.ipa)")
        exit()
def Rename_ipa(ipaFile):
    p = Path(ipaFile)
    zip_path = ipaFile
    without_extra_slash = os.path.normpath(zip_path)
    zip_app_name = os.path.basename(without_extra_slash)
    full_path= str(p.parent) + f"/{zip_app_name}"
    zip_ext = '.ipa'
    last_path = os.path.splitext(full_path)[0]
    os.system(f"mv {last_path}.zip {last_path}.ipa")
def Helper():
    logo = f'''
{G}
 ██▓ ██▓███   ▄▄▄        ██████  ▄████▄   ▒█████   ██▓███  ▓█████ 
▓██▒▓██░  ██▒▒████▄    ▒██    ▒ ▒██▀ ▀█  ▒██▒  ██▒▓██░  ██▒▓█   ▀ 
▒██▒▓██░ ██▓▒▒██  ▀█▄  ░ ▓██▄   ▒▓█    ▄ ▒██░  ██▒▓██░ ██▓▒▒███   
░██░▒██▄█▓▒ ▒░██▄▄▄▄██   ▒   ██▒▒▓▓▄ ▄██▒▒██   ██░▒██▄█▓▒ ▒▒▓█  ▄ 
░██░▒██▒ ░  ░ ▓█   ▓██▒▒██████▒▒▒ ▓███▀ ░░ ████▓▒░▒██▒ ░  ░░▒████▒
░▓  ▒▓▒░ ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒░▒░▒░ ▒▓▒░ ░  ░░░ ▒░ ░
 ▒ ░░▒ ░       ▒   ▒▒ ░░ ░▒  ░ ░  ░  ▒     ░ ▒ ▒░ ░▒ ░      ░ ░  ░
 ▒ ░░░         ░   ▒   ░  ░  ░  ░        ░ ░ ░ ▒  ░░          ░   
 ░                 ░  ░      ░  ░ ░          ░ ░              ░  ░
                                ░                                 
        {W}  Coded By : {Y}Xcode0x | {B}Twitter: {W}@Xcodeone1 

                 {B}Telegram : {W}https://t.me/x0Saudi

                 Here You can Fonud How script work !!
'''
    meun = f'''
{Y}~!#Unzip_ipa :

{W}you should use -i [IPA_file] flag and -o [output where you want save the file

Like follow command {R}python3 IPA_SCOPE.py -i testApp.ipa -o /home/youUser/Desktop
    '''
    print(logo + meun )
def logo():
    logo = f'''
{G}
 ██▓ ██▓███   ▄▄▄        ██████  ▄████▄   ▒█████   ██▓███  ▓█████ 
▓██▒▓██░  ██▒▒████▄    ▒██    ▒ ▒██▀ ▀█  ▒██▒  ██▒▓██░  ██▒▓█   ▀ 
▒██▒▓██░ ██▓▒▒██  ▀█▄  ░ ▓██▄   ▒▓█    ▄ ▒██░  ██▒▓██░ ██▓▒▒███   
░██░▒██▄█▓▒ ▒░██▄▄▄▄██   ▒   ██▒▒▓▓▄ ▄██▒▒██   ██░▒██▄█▓▒ ▒▒▓█  ▄ 
░██░▒██▒ ░  ░ ▓█   ▓██▒▒██████▒▒▒ ▓███▀ ░░ ████▓▒░▒██▒ ░  ░░▒████▒
░▓  ▒▓▒░ ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒░▒░▒░ ▒▓▒░ ░  ░░░ ▒░ ░
 ▒ ░░▒ ░       ▒   ▒▒ ░░ ░▒  ░ ░  ░  ▒     ░ ▒ ▒░ ░▒ ░      ░ ░  ░
 ▒ ░░░         ░   ▒   ░  ░  ░  ░        ░ ░ ░ ▒  ░░          ░   
 ░                 ░  ░      ░  ░ ░          ░ ░              ░  ░
                                ░                                 
        {W}  Coded By : {Y}Xcode0x | {B}Twitter: {W}@Xcodeone1 
        
                 {B}Telegram : {W}https://t.me/x0Saudi

'''
    os.system("clear")
    print(logo)
