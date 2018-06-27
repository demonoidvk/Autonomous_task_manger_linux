import os
import db

def calib():
   # f=os.popen(" su -c 'echo 20 > /sys/class/backlight/intel_backlight/brightness'")
    os.system("xinput disable 'ELAN Touchscreen'")
    os.system("redshift -O 4200")
#now =f.read()

# or use os.system(query)