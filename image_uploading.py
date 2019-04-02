import csv
import os
import shutil
import glob

#read in refs from csv
with open('refs.csv', 'r') as f:
    reader = csv.reader(f)
    refs = list(reader)


#set working dir and look for image
os.chdir('F:\\python\\work_scripts')
fname = glob.glob('*.jpg') or glob.glob('*.jpeg')


#define var for counting and source directory
x = 0
src = 'F:\\python\\work_scripts\\' + fname[x]


#loop over list of refs creating versions of image with refs as filenames 
for i in refs:
    shutil.copy(src, 'F:\\python\\work_scripts\\' + "%s".join(refs[x]) + ".jpg")
    x += 1
