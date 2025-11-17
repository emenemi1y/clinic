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

root = r"C:\Users\emily\OneDrive\Documents\GitHub\clinic"

files = glob.glob(os.path.join(root, "*.txt"))

data = {}
colors = {'PtPdCo': 'lightseagreen', 'PtPdNi': 'orange', 'PtPdCoNi': 'mediumslateblue',
          'PtPdCoNiCr': 'deeppink', 'PtPdNiCoCrFe': 'yellowgreen', 'Pt': 'slategrey', 'Ni': 'black'}

for file in files:
    filename = os.path.basename(file)
    alloy_name = filename.split('_')[0]
    data[alloy_name] = create_df(file, find_start_line(file))
    
alloys = data.keys()
plt.figure()
for alloy in alloys:
    I = data[alloy][0]
    V = data[alloy][1] + shift 
    plt.plot(V,I, label='{}'.format(alloy),linestyle = ('--' if alloy == 'Pt' or alloy=='Ni' else '-'), color=colors[alloy])
plt.legend(loc = "lower right")
plt.xlabel("Potential vs. RHE")
plt.ylabel("Current density (mA/cm^2)")
# plt.title("Shifted")
plt.grid()
plt.xlim(-1, 0.2)
plt.ylim(-350, 10)
plt.title("LSV curves for provided alloys")
plt.show()
    
    
