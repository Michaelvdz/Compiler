from main import *
import os

currentPath = os.getcwd() + "/implementationTests"

files = os.listdir(currentPath)

for i in files:
    previousPath = currentPath
    currentPath += f"/{i}"
    try:
        main(currentPath)
    except SystemExit as e:
        pass
    currentPath = previousPath
