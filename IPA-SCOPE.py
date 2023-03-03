import optparse
import os
from sys import path
from time import sleep
from func import logo, Helper,unzip_ip,Fore,Style,slow1,slow
import plistlib
import json
import sys
Y = Fore.LIGHTYELLOW_EX + Style.BRIGHT
G = Fore.LIGHTGREEN_EX + Style.BRIGHT 
R = Fore.LIGHTRED_EX + Style.BRIGHT
W = Fore.LIGHTWHITE_EX + Style.BRIGHT 
B = Fore.LIGHTBLUE_EX + Style.BRIGHT 

scan_plist = sys.argv

parser = optparse.OptionParser()
parser.add_option("-i", "--ipa",dest="ipa", help="drop ipa file to analysis app ")
parser.add_option("-o", "--output",dest="output", help="where you want save the app folder file")
(options, arguments) = parser.parse_args()
try:
    def main():
        unzip_file = [options.output,options.ipa]
        ### If user don't use any of flag it will show help guid
        if not all(unzip_file):   
            Helper()
            print("")
        ### if else program will zip & unzip the .ipa file and grab all binray strings & info.plist as well
        else:
            logo()
            unzip_ip(options.ipa,options.output)
            sleep(3)
            os.system("clear")
            logo()
            print(f"[{Y}+{W}]You will found you app in : {Y}{options.output}/Payload")
            logo()
            def Grab_Info():
                    app_part = os.popen(f"cd {options.output}"+"/Payload/;ls").read()
                    name = app_part
                    filename = name.rsplit('.', 1)[0]
                    AF_filename = list(filename.split(" "))
                    info = options.output+"/Payload/"+AF_filename[0]+".app"+"/Info.plist"
                    fileName=os.path.expanduser(info)
                    #Make result folder for Target IPA
                    os.system(f"mkdir output/{AF_filename[0]}")
                    print(f"{W}[{Y}+{W}]{B}Info plist :{W}\n")
                    with open(fileName, 'rb') as f:
                        pl = plistlib.load(f)
                    with open(f'output/{AF_filename[0]}/{AF_filename[0]}_plist_file.json', 'w') as outfile:
                        json.dump(pl,outfile)
                        '''
                        [p.1] that mean some ios app don't have this key in info.plist because 
                        info.plist it xml format file whcie have key,string also some time dic inside dic.
                        '''
                        # p.1
                        try:
                            API_KEY = pl['Fabric']['APIKey']
                            print(f"{W}API KEY : {G + API_KEY}\n")
                        except KeyError: "Fabric"
                        pass

                        # p.1

                        try:
                            mic = pl['NSMicrophoneUsageDescription']
                            print(f"{W}MIC Permission : {G + mic}\n")
                        except KeyError: 'NSMicrophoneUsageDescription'
                        pass
                        #Good in some cases
                        name_of_bin = pl['CFBundleExecutable']
                        print(f"{W}Name of Bin : {G + name_of_bin}\n")
                        mix_version = pl['MinimumOSVersion']
                        print(f"{W}Minimum_Version : {G + mix_version}\n")

                        # p.1

                        try:
                            BundleUrl = pl['CFBundleURLTypes']
                            for Url in BundleUrl:
                                url_scheme = Url['CFBundleURLName'] 
                                print(f"{W}Url scheme : {G + url_scheme}\n")
                            ssl_Allow = pl['NSAppTransportSecurity']['NSAllowsArbitraryLoads']
                            if ssl_Allow == True:
                                print(f"{W}SSL transfom Allow : {G}True\n")
                            else:
                                print(f"{W}SSL transfom Allow : {R}False\n")
                        except KeyError: 'CFBundleURLName'
                        pass
                        print(f"{W}[{R}!!{W}]{B}Info.plist values will save as {W}[{Y}{AF_filename[0]}_plist_file.json{W}]{B} check out !{W}\n")
            Grab_Info()
            def url_strings(wereSaveIt):
                app_part = os.popen(f"cd {wereSaveIt}"+"/Payload/;ls").read()
                name = app_part
                filename = name.rsplit('.', 1)[0]
                AF_filename = list(filename.split(" "))
                info = wereSaveIt+"/Payload/"+AF_filename[0]+".app"+"/%s"%AF_filename[0]
                fileName=os.path.expanduser(info)
                binary_path= str(info)
                full_path = wereSaveIt+"/Payload/"+AF_filename[0]+".app"+"/"
                slow(f"[{Y}+{W}] All Links\n")
                links = os.system(f'strings  {binary_path} |  grep -Eo "(http|https)://[a-zA-Z0-9./?=_%:-]*" | sort -u')
                slow(f"\n[{Y}+{W}] Some interesting file\n")
                json_files = os.popen(f'cd {full_path} && find . -type f -name "*.json"').read()
                print(json_files)
                sleep(2)
                certificate = os.popen(f'cd {full_path} && find . -type f -name "*.cer"').read()
                print(certificate)
                sleep(2)
                certificate_der = os.popen(f'cd {full_path} && find . -type f -name "*.der"').read()
                print(certificate_der)
                sleep(2)
                print(f"{W}You can check them in this folder[{R}{full_path}{W}]{W}")
                slow(f"\n[{Y}+{W}] All Info.plist files\n")
                plist_files = os.popen(f'cd {full_path} && find . -type f -name "*.plist"').read()
                print(plist_files)
                print(f"{W}You can check them in this folder[{R}{full_path}{W}]{W}")
                slow(f"\n[{Y}+{W}]Some files about api\n")
                api = os.popen(f'cd {full_path} && grep -Ril "api"').read()
                print(api)
                with open(f'output/{AF_filename[0]}/{AF_filename[0]}_intresting_files.txt', 'a') as x:
                    x.write('[+]json files\n'+json_files+'\n'+'[+]certificate[CER]\n'+certificate+'\n'+'[+]certificate[DER]\n'+certificate_der+'\n'+'[+]API\n'+api+'\n'+'[+]Plist files\n'+plist_files)
                slow(f"\n[{Y}+{W}]Extract Data Section & addr \n")
                slow(f"[{Y}+{W}]{R}Check txt file in /output")
                slow(f"\n[{Y}+{W}]Extract Strings  \n")
                slow(f"[{Y}+{W}]{R}Check txt file in /output")
                print(f"{W}You can check them in this folder[{R}{full_path}{W}]{W}")
                sleep(1)
                Links = os.popen(f'strings  {binary_path} |  grep -Eo "(http|https)://[a-zA-Z0-9./?=_%:-]*" | sort -u').read()
                data_section = os.popen(f'rabin2 -qz {binary_path}').read()
                sleep(2)
                All_strings = os.popen(f'rabin2 -zzz {binary_path}').read()
                sleep(2)
                Linked_libraries = os.popen(f'rabin2 -l {binary_path}').read()
                sleep(2)
                with open(f'output/{AF_filename[0]}/{AF_filename[0]}_Links.txt', 'a') as x:
                        x.write(Links)
                with open(f'output/{AF_filename[0]}/{AF_filename[0]}_Linked_libraries.txt', 'a') as x:
                        x.write('[+]Data sction\n' + data_section + '\n' + '\n[+]Linked_libraries\n' + Linked_libraries + '\n')
                with open(f'output/{AF_filename[0]}/{AF_filename[0]}_Strings.txt', 'a') as x:
                        x.write('[+]All_strings\n' + All_strings + '\n')
                print(f"\n[{Y}+{W}]{R}All Links & Strings it will save in {Y}/output{R} file !!")
            url_strings(options.output)
            Rename_ipa(options.ipa)
    main()
except KeyboardInterrupt:
    os.system("clear")
    logo()
    Exit = input(f"\n[{R}!{W}] Press q if you want exit if not Press c : ")
    if Exit == "q":
        os.system("clear")
        exit()
    if Exit == "c":
        main()
