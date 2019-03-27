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


#define source and vars for renaming and duplicating
src = 'F:\\python\\work_scripts\\' + "%s".join(fname)
x = 0
i = 0


#perform rename 
while i < len(refs):
    shutil.copy(src, 'F:\\python\\work_scripts\\' + "%s".join(refs[x]) + ".jpg")
    x += 1
    i += 1
