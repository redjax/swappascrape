import os
import shutil
from subprocess import call

directory = 'app'
# Run pip requirements install in shell
call('pip install -r requirements.txt')
call('python postgitpull.py')
call('deactivate')