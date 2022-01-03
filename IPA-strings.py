import os
from func import unzip_ip,logo,slow,Fore,Style
import optparse
Y = Fore.LIGHTYELLOW_EX + Style.BRIGHT
G = Fore.LIGHTGREEN_EX + Style.BRIGHT 
R = Fore.LIGHTRED_EX + Style.BRIGHT
W = Fore.LIGHTWHITE_EX + Style.BRIGHT 
B = Fore.LIGHTBLUE_EX + Style.BRIGHT 
parser = optparse.OptionParser()
parser.add_option("-i", "--ipa",dest="ipa", help="drop ipa file to anlasy")
parser.add_option("-o", "--output",dest="output", help="where you want save the zip file")
(options, arguments) = parser.parse_args()
logo()
unzip_ip(options.ipa,options.output)
os.system("clear")
logo()
def url_strings(wereSaveIt):
    app_part = os.popen(f"cd {wereSaveIt}"+"/Payload/;ls").read()
    name = app_part
    filename = name.rsplit('.', 1)[0]
    AF_filename = list(filename.split(" "))
    info = wereSaveIt+"/Payload/"+AF_filename[0]+".app"+"/%s"%AF_filename[0]
    fileName=os.path.expanduser(info)
    binary_path= str(info)
    full_path = wereSaveIt+"/Payload/"+AF_filename[0]+".app"+"/"
    slow(f"[{Y}+{W}] wait now extra All Links\n")
    os.system(f'strings {binary_path} |  grep -Eo "(http|https)://[a-zA-Z0-9./?=_%:-]*" | sort -u')
    slow(f"\n[{Y}+{W}] Some interesting file\n")
    os.system(f'cd {full_path} && find . -type f -name "*.json"')
    os.system(f'cd {full_path} && find . -type f -name "*.cer"')
    os.system(f'cd {full_path} && find . -type f -name "*.der"')
    print(f"{W}You can check them in this folder[{R}{full_path}{W}]{W}")
    slow(f"\n[{Y}+{W}] All Info.plist files\n")
    os.system(f'cd {full_path} && find . -type f -name "*.plist"')
    print(f"{W}You can check them in this folder[{R}{full_path}{W}]{W}")
    slow(f"\n[{Y}+{W}]Some files about api\n")
    os.system(f'cd {full_path} && grep -Ril "api"')
    print(f"{W}You can check them in this folder[{R}{full_path}{W}]{W}")
url_strings(options.output)
