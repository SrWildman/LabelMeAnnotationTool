import binascii
import io
import os
import sys
import math

import PIL.Image
import pydicom
import numpy as np

from shutil import copyfile

err = []
walk_dir = os.path.abspath(sys.argv[1])
out_dirs = []
for i in range(2,len(sys.argv)):
    out_dirs.append(os.path.abspath(sys.argv[i]))
print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))
print('out_dirs (absolute) = ' + str(out_dirs))

for root, subdirs, files in os.walk(walk_dir):
    print('--\nroot = ' + root)

    for subdir in subdirs:
        print('\t- subdirectory ' + subdir)

    for filename in files:
        file_path = os.path.join(root, filename)
        print('\t- file %s (full path: %s)' % (filename, file_path))
        if filename.endswith('.dcm'):
            try:
                orig = pydicom.dcmread(file_path)
                pix_arr = orig.pixel_array
                img = PIL.Image.fromarray(pix_arr.astype('uint8'))
                if(img.mode == 'I;16'):
                    img.mode = 'I'
                    # print(img,orig)
                    img = img.point(lambda i:i*(1./4)).convert('L')
                for out in out_dirs:
                    fold = os.path.join(out,subdir)
                    if not os.path.isdir(fold):
                        os.mkdir(fold)
                    pat = os.path.join(fold,filename)
                    img.save(pat[:-4] + '.jpg')
                    print('\t- saved file ' + filename[:-4] + '.jpg' +
                        ' (full path: ' + pat[:-4] + '.jpg' + ')')
            except NotImplementedError as e:
                print('\t- ERROR: ' + str(e))
                err.append(str(e))
                pass
        elif filename.endswith('.jpg') or filename.endswith('jpeg'):
            for out in out_dirs:
                fold = os.path.join(out,subdir)
                if not os.path.isdir(fold):
                    os.mkdir(fold)
                pat = os.path.join(fold,filename)
                copyfile(file_path,pat[:-4] + '.jpg')
                print('\t- saved file ' + filename[:-4] + '.jpg' +
                    ' (full path: ' + pat[:-4] + '.jpg' + ')')

if len(err) > 0: print(err)
