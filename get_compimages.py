# import dct_t
import dwt_t
import os
from prettytable import PrettyTable as pt
import cv2

directory_path = os.getcwd()+"/work/original/"
target_path = os.getcwd()+"/work/compressed/"
files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

for file in files:
    if file.startswith("."):
        continue
    filename = directory_path+file
    base_name, ext = file.split(".")
    I =  dwt_t.get_dwt(filename)[-1]
    # I =  dct_t.get_dct(filename)[-1]
    # cv2.imwrite(target_path+base_name+"_DCT_compressed"+".png",I)
    cv2.imwrite(target_path+base_name+"_DWT_compressed"+".png",I)