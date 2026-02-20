import os
def lock(a):
  if a == "shutdown" or a == "Shutdown":
   print("Shutting down please wait...")
   os.system("shutdown /s /t 1")
  elif a == "restart" or a == "Restart":
   print("Restarting please wait...")
   os.system("shutdown /r /t 1")  
answer = input("Do you want to restart the computer or shutdown it- ")   
lock(answer)   

