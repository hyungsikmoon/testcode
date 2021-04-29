import os
from PIL import Image

dir_path = '/home/hs.moon/work/PAE/PAE/data/test/gender/test/'
output_path = '/home/hs.moon/work/PAE/PAE/data/test/gender/test_resize/'

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                dir, file = os.path.split(full_filename)
                print(full_filename)
                print(dir)
                print(file)
                image = Image.open(full_filename)
                resize_image=image.resize((160,160))
                resize_image.save(dir+'/Resized_'+file)
    except PermissionError:
        pass

search(dir_path)
