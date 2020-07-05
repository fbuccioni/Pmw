import string
import os
import shutil
import glob
import tarfile
import subprocess


#Version to be released
VERSION1='1.3.3'
VERSION2='2.0.1'

#DIR is the directory name extension and is automatically generated
DIR1=VERSION1.replace('.', '_')
DIR2=VERSION2.replace('.', '_')

# Date to put in documentation for the release date of this release
VERSION_DATE="23 March 2015"


# Location of Pmw source files (on local PC):
SRC_DIR='Pmw_0_0_0'

# Temporary directory
TEMP='C:\Temp\\'

#Test variables
#print(VERSION)
#print(DIR)
#print(VERSION_DATE)
#print(BASEDIR)
#print(OUTFILEDIR)
#print(SRC_DIR)

print("Using Pmw/%(SRC_DIR)s to create Pmw.%(VERSION)s" % {'SRC_DIR':SRC_DIR,\
                                                           'VERSION':VERSION2})

STARTDIR = os.getcwd()
print(STARTDIR)

path = TEMP + 'Pmw' + '-' + VERSION2
if (os.path.isdir(path)):
    print('Old folder deleted')
    shutil.rmtree(path)

path = TEMP + 'Pmw'
if (os.path.isdir(path)):
    print('Old folder deleted')
    shutil.rmtree(path)

results = []
os.chdir(TEMP)
for file in glob.glob('Pmw*.tar.gz'):
    os.remove(file)

os.chdir(STARTDIR)
shutil.copytree('Pmw', path + '\\Pmw')
shutil.copy('setup.py', path)
shutil.copy('PKG-INFO', path)

os.chdir(TEMP + 'Pmw\\Pmw')
os.rename('Pmw_1_0_0', 'Pmw_' + DIR1)
os.rename('Pmw_2_0_0', 'Pmw_' + DIR2)
os.chdir('..')


for tup in os.walk('.'):
    for dir in tup[1]:
        filepath = tup[0] + '\\' + dir
        if (dir == 'CVS'):
            shutil.rmtree(filepath)
        if (dir == '__pycache__'):
            shutil.rmtree(filepath)
    for file in tup[2]:
        filepath = tup[0] + '\\' + file
        if (file.endswith('.pyc')):
            os.remove(filepath)
        if (file.endswith('.py.bak')):
            os.remove(filepath)

from glob import glob
for f in glob('*~'):
    os.remove(f)
'''
os.remove('ReleaseProcedure')
os.remove('TODO')
os.remove('maketar.sh')
os.remove('maketar.py')
os.remove('set_env.sh')



#create documentation source
os.chdir('Pmw_' + DIR)
tf = tarfile.open('Pmw_' + DIR + '.docsrc.tar.gz', 'w:gz')
tf.add('docsrc')
tf.close()
shutil.move('Pmw_' + DIR + '.docsrc.tar.gz', '../..')

#create manuals
os.chdir('docsrc')
#p = subprocess.Popen("python createmanuals.py", shell=False)
subprocess.call("python createmanuals.py")
os.chdir('..')
shutil.rmtree('docsrc')
os.chdir('..')

for tup in os.walk('.'):
    for file in tup[1]:
        filepath = tup[0] + '\\' + file
        if (file == '__pycache__') and os.path.isdir(filepath):
            shutil.rmtree(filepath)
        if (file.endswith('.pyc')):
            shutil.rmtree(filepath)
        if (file.endswith('.py.bak')):
            shutil.rmtree(filepath)


#generate package file
#navigate to TEMP
os.chdir('..')

if os.path.exists('src'):
    shutil.rmtree('src')
os.mkdir('src')

shutil.move('Pmw/setup.py', 'src/')
shutil.rmtree('Pmw/Alpha_99_9_example')
shutil.copytree('Pmw', 'src/Pmw')



if os.path.exists('Pmw2'):
    shutil.rmtree('Pmw2')
os.rename('src', 'Pmw2')
'''
os.chdir('..')
os.rename('Pmw', 'Pmw-' + VERSION2)
tf = tarfile.open('Pmw-' + VERSION2 + '.tar.gz', 'w:gz')
tf.add('Pmw-' + VERSION2)
tf.close()
