import binascii
import io
import os
import sys
import math

import PIL.Image
import pydicom
import numpy as np

err = []
walk_dir = os.path.abspath(sys.argv[1])
print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))

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
                img.save(file_path[:-4] + '.jpg')
                print('\t- saved file ' + filename[:-4] + '.jpg' +
                      ' (full path: ' + file_path[:-4] + '.jpg' + ')')
            except NotImplementedError as e:
                print('\t- ERROR: ' + str(e))
                err.append(str(e))
                pass

if len(err) > 0: print(err)
