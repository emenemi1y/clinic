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

def create_df(filename):
    df = pd.read_csv(
        filename,
        sep="\t",
        header=find_start_line(filename)-4,
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

root = r"C:\Users\PC\Documents\GitHub\clinic\data\X22.5"

filebase = {'side A, up': 'X225_N52magA_up_3_11_02_LSV_C01.txt',
            'side B, up': 'X225_N52magB_up_3_11_02_LSV_C01.txt',
            'side A, flat': 'X225_N52magA_flat_3_11_02_LSV_C01.txt',
            'side B, flat': 'X225_N52magB_flat_3_11_02_LSV_C01.txt',
            'no magnet': 'X22_5_2-17_02_LSV_C01.txt'}
data = {}
# colors = {'PtPdCo': 'lightseagreen', 'PtPdNi': 'orange', 'PtPdCoNi': 'mediumslateblue',
#           'PtPdCoNiCr': 'deeppink', 'PtPdNiCoCrFe': 'yellowgreen', 'Pt': 'slategrey', 'Ni': 'black'}

plt.figure()
for test in filebase.keys():
    file = os.path.join(root, filebase[test])
    data[test] = create_df(file)
    I = data[test]["<I>/mA"].values
    V = data[test]["Ewe/V"].values + shift
    plt.plot(V,I, label=f'{test}')
    
plt.legend()
plt.xlabel('Potential vs. RHE')
#plt.ylabel('Absolute current (mA)')
plt.ylabel('Current density ($mA/cm^2$)')

plt.grid() 
plt.xlim(-0.75, 0.2)
plt.ylim(-500, 10)
#plt.title("LSV curves, $PtPdCoNi$")
#plt.title("LSV curves, $Pt_{20}Pd_{20}Ni_{20}Co_{40}$")
#plt.title('Ni with/without magnet')
plt.title('LSV curves, X22.5, magnet tests')
plt.show()
    
    
