import os,subprocess
from subprocess import Popen,STDOUT
from collections import defaultdict
def exec_cmd():
    cmd=input("Enter task:")
    cmd=cmd.lower()
    com=cmd.replace('-',' ').replace('_',' ').split()
    print(com)
    dec=["open","execute", "close","terminate"]
    tk=[c for c in com if c in dec]
    print(tk)
    mcom=defaultdict(list)             # Data structure to store correct executing command
    a=1
    j=a+1
    if 'exit' in tk:
        exit()    
    else:
        if tk is not None:
            try:
                for a in range(len(com)):
                    for j in range(len(com)):
                        f=subprocess.Popen([com[a]], stdout=os.open(os.devnull, os.O_RDWR), stderr=STDOUT)
                        stmt=input("\nWas command successful?(yes/ no)\n\t\t\t")
                        if 'yes' in stmt:
                            mcom[com[a]].append(j)
                            print(mcom)
                            print("\nanything else?")
                            exec_cmd()
                        else:
                            print(" Okay.. hope  to see you again! Bye.")

            except OSError:
                print("\nSorry!, can you repeat again")

exec_cmd()                    


