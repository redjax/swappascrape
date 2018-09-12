import os
import shutil

appdirectory = 'app/'
stagedirectory = 'stage/'
 

def copyDirectory(src, dest):
    try:
        shutil.copytree(src, dest)
    # Directories are the same
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not copied. Error: %s' % e)


copyDirectory(stagedirectory,appdirectory)

shutil.rmtree(stagedirectory)
