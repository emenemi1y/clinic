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

root = r"C:\Users\emily\OneDrive\Documents\GitHub\clinic\Ni"

# PLATINUM

Ni1_file = os.path.join(root, "Ni_Test1_C01.txt")
Ni2_file = os.path.join(root, "Ni_Test2_C01.txt")

Ni1 = create_df(Ni1_file, find_start_line(Ni1_file))
Ni2 = create_df(Ni2_file, find_start_line(Ni2_file))

I = Ni1[0]
V = Ni1[1] + shift
plt.figure()
plt.plot(V,I,label="Ni, before sanding", color = "firebrick")

I = Ni2[0]
V = Ni2[1] + shift
plt.plot(V,I,label="Ni, after sanding", color = "red")


plt.legend()
plt.xlabel("Voltage vs. RHE")
plt.ylabel("Current density (mA/cm\u00b2)")
plt.title("LSV Curve, Ni before and after sanding")
plt.xlim(-1.1, 0.3)
plt.ylim(-400, 10)
plt.grid()
plt.show()
