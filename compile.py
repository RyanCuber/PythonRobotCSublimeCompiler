import win32com.client as comclt
import os,time
wsh= comclt.Dispatch("WScript.Shell")

os.system("start ") # insert file you want to compile, be sure that robotc is the default program to open

time.sleep(2)
wsh.SendKeys("{F5}") # send the keys you want
#imp.reload(compile)
