import random
import subprocess
import re


chList = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]

newMac = ""
for i in range(12):
    newMac += random.choice(chList)
   
ifconfigResult = subprocess.check_output("ifconfig eth0", shell=True).decode()

oldMac = re.search("ether(.*?)t",ifconfigResult).group(1).strip()

subprocess.check_output("ifconfig eth0 down",shell=True)
subprocess.check_output("ifconfig eth0 hw ether "+newMac,shell=True)
subprocess.check_output("ifconfig eth0 up",shell=True)

print("Old Mac: ",oldMac)
print("New Mac: ",newMac)





