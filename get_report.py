import dct_t
# import dwt_t
import os
from prettytable import PrettyTable as pt

directory_path = os.getcwd()+"/work/original/"
files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
table = pt()
table.field_names = ["Filename", "Compression ratio", "PSNR", "MSE","Decode time (s)","Code time (s)"]

for file in files:
    if file.startswith("."):
        continue
    filename = directory_path+file
    # compression_ratio, compression_time, decompression_time, MSE, PSNR =  dwt_t.get_dwt(filename)
    compression_ratio, compression_time, decompression_time, MSE, PSNR =  dct_t.get_dct(filename)
    table.add_row([file.split(".")[0],"%.3f"%compression_ratio,"%.3f"%PSNR,"%.3f"%MSE,"%.3f"%decompression_time,"%.3f"%compression_time])

print(table)
