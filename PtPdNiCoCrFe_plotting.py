# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 16:11:08 2025

@author: emily
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Nov  8 15:29:00 2025

@author: emily
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import math

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
shift = R*T/F * math.log(10) * pH

root = r"C:\Users\emily\OneDrive\Documents\GitHub\clinic\PtPdNiCoCrFe"

# PLATINUM

PtPdNiCoCrFe_file1 = os.path.join(root, "PtPdNiCoCrFe_Test1_C01.txt")
PtPdNiCoCrFe_file2 = os.path.join(root, "PtPdNiCoCrFe_Test4_C01.txt")

PtPdNiCoCrFe1 = create_df(PtPdNiCoCrFe_file1, find_start_line(PtPdNiCoCrFe_file1))
PtPdNiCoCrFe2 = create_df(PtPdNiCoCrFe_file2, find_start_line(PtPdNiCoCrFe_file2))

I = PtPdNiCoCrFe1[0]
V = PtPdNiCoCrFe1[1] + shift
plt.figure()
plt.plot(V,I,label="PtPdNiCoCrFe, before sanding", color = "firebrick")

I = PtPdNiCoCrFe2[0]
V = PtPdNiCoCrFe2[1] + shift
plt.plot(V,I,label="PtPdNiCoCrFe, after sanding", color = "red")


plt.legend()
plt.xlabel("Voltage vs. RHE")
plt.ylabel("Current density (mA/cm\u00b2)")
plt.title("LSV Curve, PtPdNiCoCrFe before and after sanding")
plt.xlim(-1.1, 0.3)
plt.ylim(-400, 10)
plt.grid()
plt.show()
