import sys
import os
import subprocess

print ""
print "******* Easily Format a SD Card in OSX to FAT32 *******"
print "1.) alle Volumes anzeigen: "
print ""
print ""
print ""

os.system("diskutil list")

print ""
print ""
print "2.) Now input the volumeName of disk. The name, which appers in Finder.app when you simply insert the sd card. Should be in last row, under NAME"
volumeName  = raw_input(">")
volumeName = volumeName.upper()


if(volumeName == ""):
	print "Error: no name is given"
	os._exit(1)	
print "> convert valume Name to upper Case :" +volumeName
result = ""
try:
	com = "diskutil info " + volumeName+" |grep Node"
	result = subprocess.check_output(com, stderr=subprocess.STDOUT, shell=True)
except subprocess.CalledProcessError as e:
    print "Valume Name was not found. Please check again!"
    raise RuntimeError("command '{}' return with error (code {})".format(e.cmd, e.returncode))

path = result[result.index("/dev/disk"):-3] 

print "> mounted at path: " + path
isOk = raw_input("Correct path? (y/n) >")
if (isOk == "y"):
	com= "sudo diskutil eraseDisk FAT32 " +volumeName+" MBRFormat "+ path
	os.system(com)	
else:
	print "> Thanks for using the script"
	os._exit(0)	
