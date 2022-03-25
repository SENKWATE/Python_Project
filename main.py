import sys, string, os
import numpy as np 


os.system("./conversion/pas2asc.exe")

# utility functions
from functions import julian_2_standard_date


root_files = os.listdir('./input_files')


os.system("pyinstaller ./conversion/pas2asc.exe")
# for root_file in root_files:
#     root_date = julian_2_standard_date(root_file)
    # for data_logger in os.listdir('./input_files/'+root_file):
        
