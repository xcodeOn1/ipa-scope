import os
from func import logo

logo()
menu = '''
[1] Mac OS
[2] Linux (if you use kali don't need anything)
[00]exit
'''
print(menu)
Q = input(str("which OS did you use >> "))
while True:
    if Q == '1' :
        os.system("brew install radare2")
        print("[+]Now you can run the tool")
    if Q == '2':
        os.system("git clone https://github.com/radareorg/radare2;radare2/sys/install.sh")
        print("[+]Now you can run the tool") 
    else:
        break
