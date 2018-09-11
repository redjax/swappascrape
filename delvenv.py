import shutil
import os

def delete_venv():
    dirs = ['Include/', 'Lib', 'Scripts', 'tcl']
    files = ['pip-selfcheck.json']


    # Remove venv directories
    for dir in dirs:
        shutil.rmtree(dir)


    # Remove venv files
    for f in files:
        os.remove(f)
