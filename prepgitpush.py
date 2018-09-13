import os
import shutil

import delvenv

appdirectory = 'app/'
stagedirectory = 'stage/'
filearray = ['swappascrape.py', 'op5search.csv']


def copyDirectory(src, dest):
    try:
        shutil.copytree(src, dest)
    # Directories are the same
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not copied. Error: %s' % e)


copyDirectory(appdirectory, stagedirectory)
os.remove(os.path.join(stagedirectory, 'op5search.csv'))

shutil.rmtree(appdirectory)

# Delete the virtualenv before pushing.
delvenv.delete_venv()
