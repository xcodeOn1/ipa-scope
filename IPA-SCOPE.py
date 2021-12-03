import optparse
import os
from sys import path
from time import sleep
from func import logo, Helper ,unzip_ip,Fore,Style,slow1,slow
import plistlib
import json
from macholibre import parse
try:
    os.system("pip3 install git+https://github.com/aaronst/macholibre.git")
    os.system("clear")
except:
    pass
Y = Fore.LIGHTYELLOW_EX + Style.BRIGHT
G = Fore.LIGHTGREEN_EX + Style.BRIGHT 
R = Fore.LIGHTRED_EX + Style.BRIGHT
W = Fore.LIGHTWHITE_EX + Style.BRIGHT 
B = Fore.LIGHTBLUE_EX + Style.BRIGHT 

parser = optparse.OptionParser()
parser.add_option("-i", "--ipa",dest="ipa", help="drop ipa file to anlasy")
parser.add_option("-o", "--output",dest="output", help="where you want save the zip file")
(options, arguments) = parser.parse_args()
try:
    def main():
        unzip_file = [options.output,options.ipa]
        ### If user don't use any of flag it will show help guid
        if not all(unzip_file):   
            Helper()
            print("")
        ### if else the program will zip & unzip the .ipa file and grab all binray strings & info.plist as well
        else:
            logo()
            unzip_ip(options.ipa,options.output)
            sleep(3)
            os.system("clear")
            logo()
            slow(f"[{Y}+{W}]You will found you app in : {Y}{options.output}/Payload")
            scan = str(input(f"{W}[{Y}+{W}]{W}Do you want scan the app '{G}y/{R}n'{W}: "))
            if scan == "n":
                print(f"{W}[{Y}!{W}]Ok than see you later !!")
                exit()
            else:
                logo()
                def Grab_Info():
                    app_part = os.popen(f"cd {options.output}"+"/Payload/;ls").read()
                    name = app_part
                    filename = name.rsplit('.', 1)[0]
                    AF_filename = list(filename.split(" "))
                    info = options.output+"/Payload/"+AF_filename[0]+".app"+"/Info.plist"
                    fileName=os.path.expanduser(info)
                    slow(f"{W}[{Y}+{W}]{B}Info plist :{W}\n")
                    print()
                    with open(fileName, 'rb') as f:
                        pl = plistlib.load(f)
                    with open(f'output/{AF_filename[0]}_plist_file.json', 'w') as outfile:
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
                        slow(f"{W}[{R}!!{W}]{B}Info.plist values will save as {W}[{Y}Info.json{W}]{B} check out !{W}\n")
                        try:
                            # Read the bin file and get the straings
                            bin_path = f"{options.output}"+"/Payload/"+AF_filename[0]+".app/"+AF_filename[0]
                            strings_in_bin = parse(bin_path)
                            out_file = open(f'output/{AF_filename[0]}_BIN.json', 'w')
                            parse(bin_path, out=out_file)
                        except FileNotFoundError:
                            slow1(f"{W}[{R}×{W}]There is Erorr !! ")
                            slow1(f"{W}[{R}×{W}]Check the binary name Here : {options.output}"+"/Payload/"+AF_filename[0]+".app/")
                            sleep(3)
                            os.system("clear")
                            logo()
                            bin_name = str(input(f"{W}[{Y}!{W}] Put the binary name Here >> "))
                            def Get_String_bin(binName):
                                # Read the bin file and get the straings
                                bin_path = f"{options.output}"+"/Payload/"+AF_filename[0]+".app/"+bin_name
                                strings_in_bin = parse(bin_path)
                                out_file = open(f'output/{AF_filename[0]}_BIN.json', 'w')
                                parse(bin_path, out=out_file)
                            Get_String_bin(bin_name)
                        slow(f"{W}[{Y}+{W}]{B}Get binray Strings plist :{W}\n")
                        slow(f"{W}[{R}!!{W}]{W}Coming soon Grab Emails,numbers and more")
                        slow(f"{W}[{R}!!{W}]{B}Binray Strings will save as {W}[{Y}{AF_filename[0]}_BIN.json{W}]{B} check out !{W}\n")
            Grab_Info()
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
