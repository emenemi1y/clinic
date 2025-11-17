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

root = r"C:\Users\emily\OneDrive\Documents\GitHub\clinic\magnet"

# PLATINUM

PtN_file = os.path.join(root, "Magnet1_North_Test1_C01.txt")
PtS_file = os.path.join(root, "Magnet1_South_Test1_C01.txt")

PtN = create_df(PtN_file, find_start_line(PtN_file))
PtS = create_df(PtS_file, find_start_line(PtS_file))

I = PtN[0]
V = PtN[1] + shift
plt.figure()
plt.plot(V,I,label="Pt, North", color = "firebrick")

I = PtS[0]
V = PtS[1] + shift
plt.plot(V,I,label="Pt, South", color = "red")

# NICKEL
'''
NiN_file = os.path.join(root, "Magnet2_North_Test1_C01.txt")
NiS_file = os.path.join(root, "Magnet2_South_Test1_C01.txt")

NiN = create_df(NiN_file, find_start_line(NiN_file))
NiS = create_df(NiS_file, find_start_line(NiS_file))

I = NiN[0]
V = NiN[1] + shift
plt.plot(V,I,label="Ni, North", color="darkblue")

I = NiS[0]
V = NiS[1] + shift
plt.plot(V,I,label="Ni, South", color="dodgerblue")
'''
# UNMAGNETIZED
Pt_file = os.path.join(root, "Pt_Test1_C01.txt")
Ni_file = os.path.join(root, "Ni_Test1_C01.txt")
Pt = create_df(Pt_file, find_start_line(Pt_file))
Ni = create_df(Ni_file, find_start_line(Ni_file))

I = Pt[0]
V = Pt[1] + shift
plt.plot(V, I, label="Pt, no magnet", color = "red", linestyle='--')
'''
I = Ni[0]
V = Ni[1] + shift
plt.plot(V, I, label="Ni, no magnet", color='blue', linestyle='--')
'''


plt.legend()
plt.xlabel("Voltage vs. RHE")
plt.ylabel("Current density (mA/cm\u00b2)")
plt.title("LSV Curve, Magnetic Prototypes")
plt.xlim(-1.1, 0.3)
plt.ylim(-400, 10)
plt.grid()
plt.show()
