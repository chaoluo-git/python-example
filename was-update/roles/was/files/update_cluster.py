import sys


def updateEar(appName, cellName, rootName, earFile, clusterName):
    # declare global variable
    global AdminApp
    # update the existing application
    AdminApp.update(appName, "app",
                    "[-operation update -cell " + cellName + " -contextroot " + rootName + " -contents " + earFile + " -cluster " + clusterName + "]")
    AdminConfig.save()

# end update()

# read the file by lines
fileName = sys.argv[0] + ".txt"
print fileName
f = open(fileName, "r")
lines = f.readlines()
f.close()
names = lines[0].split(",")
appName = names[0]
cellName = names[1]
rootName = names[2]
earFile = names[3]
clusterName = names[4]
print appName, cellName, rootName, earFile, clusterName
updateEar(appName, cellName, rootName, earFile, clusterName)