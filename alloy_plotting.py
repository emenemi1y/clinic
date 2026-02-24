# -*- coding: utf-8 -*-
"""
Created on Sun Nov  9 16:23:08 2025

@author: emily
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import math
import glob

def is_data_line(line):
    parts = line.strip().split('\t')
    parts = [p for p in parts if p]
    if not parts:
        return False
    try:
        [float(p) for p in parts]
        return True
    except ValueError:
        return False
    
def find_start_line(filename):
    start_line = None
    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        for i, line in enumerate(f):
            if is_data_line(line):
                start_line = i
                break
    return start_line

def create_df(filename, startline):
    df = pd.read_csv(
        filename,
        sep="\t",
        header=None,
        skiprows=startline,
        engine="python",
        encoding="utf-8",
        encoding_errors="ignore"
    )
    return df

# Gas constant
R = 8.3145 # J * mol^-1 * K^-1
T = 25 + 273.15 # Room temperature (K)
F = 96485.3321 # s * A * mol^-1
pH = 14
Ru = 4.52 # uncompensated solution resistance 
shift = R*T/F * math.log(10) * pH

root = r"C:\Users\PC\Documents\GitHub\clinic\data\Ni"

filebase = {'magnet': 'Ni_magnet_2_23_02_LSV_C01.txt',
            'no magnet': 'Ni_2_23_02_LSV_C01.txt'}
'''
filebase = {'Pt_{22.5}Pd_{22.5}Ni_{22.5}Co_{22.5}Cr_{10}': 'Pt22.5Pd22.5Ni22.5Co22_02_LSV_C01.txt',
            'Pt_{40}Pt_{20}Ni_{20}Co_{20}': 'Pt40Pt20Ni20Co20_polished_2-6_02_LSV_C01.txt',
            'Pt_{20}Pd_{20}Ni_{20}Co_{40}': 'Co40_polished_2-10_02_LSV_C01.txt',
            'Pt_{20}Pd_{40}Ni_{40}Co_{40}': 'Pd40_polished_2-10_02_LSV_C01.txt',
            'Pt_{30}Pd_{30}Ni_{10}Co_{10}Cr_{10}': 'Ni10Co10_polished_2-10_02_LSV_C01.txt',
            'Pt_{20}Pd_{40}Ni_{40}Co_{40}': 'Pd40_polished_2-10_02_LSV_C01.txt',
            'X18.5': 'X18_02_LSV_C01.txt'}

            'Pt': 'Pt_2-10_02_LSV_C01.txt',
            'PtPdCo': 'PtPdCo_2-10_02_LSV_C01.txt',
            'PtPdCoNiCrFe':'PtPdCoNiCrFe_2-10_02_LSV_C01.txt',
            'PtPdNiCoCr': 'PtPdNiCoCr_polished_IR_02_LSV_C01.txt'}
    '''

data = {}
# colors = {'PtPdCo': 'lightseagreen', 'PtPdNi': 'orange', 'PtPdCoNi': 'mediumslateblue',
#           'PtPdCoNiCr': 'deeppink', 'PtPdNiCoCrFe': 'yellowgreen', 'Pt': 'slategrey', 'Ni': 'black'}

plt.figure()
for test in filebase.keys():
    file = os.path.join(root, filebase[test])
    data[test] = create_df(file, find_start_line(file))
    I = data[test][3]
    if (test == 'double'): I = I / 2
    V = data[test][2] + shift
    plt.plot(V,I, label=f'${test}$')
    
plt.legend()
plt.xlabel('Potential vs. RHE')
#plt.ylabel('Absolute current (mA)')
plt.ylabel('Current density ($mA/cm^2$)')

plt.grid()
# plt.xlim(-0.65, 0.2)
# plt.ylim(-500, 10)
#plt.title("LSV curves, $Pt$")
# plt.title("LSV curves, $Pt_{22.5}Pd_{22.5}Ni_{22.5}Co_{22.5}Cr_{10}$")
plt.title('Ni with/without magnet')
plt.show()
    
    
