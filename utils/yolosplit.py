import glob
import os 
import os.path as op
import random
import shutil
os.chdir('D:/AI Builders/Project/data/My Dataset 3.0/new_yolo')
path = glob.glob('train\labels\*')

while len(glob.glob("valid/labels/*.txt")) < 230:
    p = random.choice(os.listdir("train/labels/")) 
    
    filename, file_ext = os.path.splitext(p)
    if glob.glob(f"train/images/{filename}.*") != []:
        imgpath = glob.glob(f"train/images/{filename}.*")[0]
        shutil.move(imgpath, f"valid/images/{op.basename(imgpath)}")
        shutil.move(f"train/labels/{p}", f"valid/labels/{p}")
        print(f"Moved {filename}")
        