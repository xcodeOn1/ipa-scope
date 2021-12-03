import os 
from pip._vendor.colorama import Fore, Style
from time import sleep
import optparse
import json
import time as mm
import sys as n
from time import sleep
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

def unzip_ip(ipaFile,wereSaveIt):
    # zip the file and unzip it also take the app name
    slow(f"[{Y}+{W}] wait now extra zip file")
    sleep(3)
    name = ipaFile
    filename = name.rsplit('.', 1)[0]
    AF_filename = list(filename.split(" "))
    os.system(f"mv {name} {AF_filename[0]}.zip")
    os.system(f"mv {AF_filename[0]}.zip {wereSaveIt}")
    unzip = f"unzip {AF_filename[0]}"
    os.system(f"cd {wereSaveIt};{unzip}")
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
        {W}  Coded By : {Y}Xcode | {B}Twitter: {W}@Xcodeone1 

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
        {W}  Coded By : {Y}Xcode | {B}Twitter: {W}@Xcodeone1 
        
                 {B}Telegram : {W}https://t.me/x0Saudi

'''
    os.system("clear")
    print(logo)
