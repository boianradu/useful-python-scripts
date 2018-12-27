import os,sys, errno, shutil, argparse, pathlib

# Author: Boian Radu
#####
# Move files to new folder.
# Recursively iterate directory for files and move every
# file to the destination folder.
# example: python .\moveFilesInsideDirectory.py --src=test --dst=dest
#####

parser = argparse.ArgumentParser()
parser.add_argument('--src', help='Source directory. Default current directory.', type=str, default='.')
parser.add_argument('--dst', help="Destination directory. Default current directory.", type=str, default='.')

args=parser.parse_args()
print(args) 
print(args.src)
print(args.dst)
 
src = args.src
dst = args.dst
pathlib.Path(dst).mkdir(parents=True, exist_ok=True) 

# recursive function that list files inside specified directory
def listFiles(dirName):
    files = os.listdir(dirName)
    for name in files:
        name = os.path.join(dirName,name)
        if os.path.isdir(name):
            listFiles(name)
        else:
            print(name)
# call the recursive listFiles function
# listFiles(src)

# recursive function that moves files deep inside
# specified directory to specified destination
def moveFiles(dirName,destination,substring):
    files = os.listdir(dirName)
    for name in files:
        fullNamePath = os.path.join(dirName,name)
        if os.path.isdir(fullNamePath):
            moveFiles(fullNamePath,destination,substring)
        elif substring in name: #move only if Substring exists in name file
            print("Moved", fullNamePath,"to",os.path.join(destination,name))
            shutil.move(fullNamePath, os.path.join(destination,name))
        else:
            print("Not moving", fullNamePath)


# create destination directory if not exists
# call moveFiles function
moveFiles(src,dst,"COVER")


