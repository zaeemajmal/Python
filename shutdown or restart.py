import os
answer = input("Do you want to restart the computer or shutdown it- ")
if answer == "shutdown" or answer == "Shutdown":
  os.system("shutdown /s /t 1")
if answer == "restart" or answer == "Restart":
  os.system("shutdown /r /t 1")  