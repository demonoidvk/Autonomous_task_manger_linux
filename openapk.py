#in this file, it would take input for opening and closing an application
import os,subprocess
import calibrate
import man

from subprocess import Popen,STDOUT
from calibrate import *
from man import helpman

def exec_cmd():
    while True:
        cmd=input("\n\t\t\t ")
        cmd=cmd.lower()
        com=cmd.replace('-',' ').replace('_',' ').split()
        dec=["open","execute", "close","terminate"]
        hp=["manual", "help"]
        if 'exit' in com:
            print(" Okay.. hope  to see you again! Bye.\n\n")
            exit()   
        elif 'no' in com:
            continue    
        elif 'calibrate' in com:
            calibrate.calib()
            print("\nanything else?")
            continue   
        elif set(hp).intersection(com):
            man.helpman()
            print("\nanything else?")
            continue
                
        else:
            try:
                f=subprocess.Popen([com[1]], stdout=os.open(os.devnull, os.O_RDWR), stderr=STDOUT)
                stmt=input("\nDid it work?(yes/ no)\n\t\t\t")
                if 'no' in stmt:
                    print(" Enter the task again.. please?")
                    continue
                else:
                    print("\nanything else for now?")      
                    continue
            except OSError:
                print("\nSorry!, can you repeat again")
                




