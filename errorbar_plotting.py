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
    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        for i, line in enumerate(f):
            if is_data_line(line):
                return i
    return None

def create_df(filename):
    startline = find_start_line(filename)
    return pd.read_csv(
        filename,
        sep="\t",
        header=None,
        skiprows=startline,
        engine="python",
        encoding="utf-8",
        encoding_errors="ignore"
    )

# Gas constant
# Gas constant
R = 8.3145 # J * mol^-1 * K^-1
T = 25 + 273.15 # Room temperature (K)
F = 96485.3321 # s * A * mol^-1
pH = 14
shift = R*T/F * math.log(10) * pH

root = r"/content/drive/MyDrive/Platalytix/Lab Material/Data"  # change, had to mount google drive for this

# Alloy lists
alloys = {
    "Co40": [
        "Co40_2_18_02_LSV_C01.txt",
        "Co40_2_19_02_LSV_C01.txt",
        "Co40_polished_2-10_02_LSV_C01.txt",
    ],
    "Ni": [
        "Ni_2_11_02_LSV_C01.txt",
        "Ni_2_18_02_LSV_C01.txt",
        "Ni_2_19_02_LSV_C01.txt",
        "Ni_2_23_02_LSV_C01.txt",
    ],
    "Ni10Co10": [
        "Ni10Co10_2-17_02_LSV_C01.txt",
        "Ni10Co10_2_19_02_LSV_C01.txt",
        "Ni10Co10_polished_2-10_02_LSV_C01.txt",
        "PtPdNi10Co10Cr10_polished_2_16_02_02_LSV_C01.txt",
    ],
    "Ni25Co25": [
        "Ni25Co25_2_19_02_LSV_C01.txt",
        "Pt20Pd10Ni25Co25Cr20_polished_2-6_02_LSV_C01.txt",
        "PtPdNi25Co25Cr_polished_2_16_02_02_LSV_C01.txt",
    ],
    "Ni40": [
        "Ni40_2-17_02_LSV_C01.txt",
        "Ni40_2_19_02_LSV_C01.txt",
        "Ni_40_polished_2_16_26_02_LSV_C01.txt",
        "Pt20Pd20Ni40Co20_polished_2-6_02_LSV_C01.txt",
    ],
    "Pd40": [
        "Pd40_2-17_02_LSV_C01.txt",
        "Pd40_polished_2-10_02_LSV_C01.txt",
        "PtPd_40_CoNi_2_12_02_LSV_C01.txt",
    ],
    "Pt": [
        "Pt_2-10_02_LSV_C01.txt",
        "Pt_2_12_02_LSV_C01.txt",
        "Pt_2_19_02_LSV_C01.txt",
    ],
    "Pt40": [
        "Pt40PdNiCo_polished_2_16_02_02_LSV_C01.txt",
        "Pt40Pt20Ni20Co20_polished_2-6_02_LSV_C01.txt",
        "Pt40_2-17_02_LSV_C01.txt",
        "Pt40_2_19_02_LSV_C01.txt",
    ],
    "PtPdCo": [
        "PtPdCo_2-10_02_LSV_C01.txt",
        "PtPdCo_2_12_02_LSV_C01.txt",
    ],
    "PtPdCoNi": [
        "PtPdCoNi_2-19_02_LSV_C01.txt",
        "PtPdCoNi_2_11_02_LSV_C01.txt",
        "PtPdCoNi_2_12_02_LSV_C01.txt",
    ],
    "PtPdCoNiCrFe": [
        "PtPdCoNiCrFe_2-10_02_LSV_C01.txt",
        "PtPdCoNiCrFe_2_18_02_LSV_C01.txt",
    ],
    "PtPdNi": [
        "PtPdNi_2_11_02_LSV_C01.txt",
        "PtPdNi_2_18_02_LSV_C01.txt",
    ],
    "PtPdNiCoCr": [ # last file has two copies in folder?
        "PtPdCoNiCr_2_11_polished_02_LSV_C01.txt",
        "PtPdCoNiCr_2_11_unpolished_02_LSV_C01.txt",
        "PtPdNiCoCr_polished_IR_02_LSV_C01.txt",
    ],
    "X18.75": [
        "X18_02_LSV_C01.txt",
        "X18_75_2-17_02_LSV_C01.txt",
        "X18_75_polished_2-12_02_LSV_C01.txt",
        "X18_75_unpolished_2-12_02_LSV_C01.txt",
    ],
    "X22.5": [
        "Pt22.5Pd22.5Ni22.5Co22_02_LSV_C01.txt",
        "PtPdNiCoCrX22_02_LSV_C01.txt",
        "X22_5_2-17_02_LSV_C01.txt"
    ],
}

alloy_colors = {
    "Co40": "firebrick",             # Pt20Pd20Ni20Co40
    "Ni": "darkorange",              # Ni
    "Ni10Co10": "orangered",         # Pt30Pd30Ni10Co10Cr20
    "Ni25Co25": "tomato",            # Pt20Pd10Ni25Co25Cr20
    "Ni40": "sienna",                # Pt20Pd20Ni40Co20

    "Pd40": "royalblue",             # Pt20Pd40Ni20Co20
    "Pt": "navy",                    # Pt
    "Pt40": "dodgerblue",            # Pt40Pd20Ni20Co20

    "PtPdNi": "mediumorchid",        # PtPdNi
    "PtPdCo": "blueviolet",          # PtPdCo
    "PtPdCoNi": "darkviolet",        # PtPdCoNi

    "PtPdNiCoCr": "rebeccapurple",   # PtPdNiCoCr
    "PtPdCoNiCrFe": "seagreen",      # PtPdCoNiCrFe
    "X18.75": "olive",               # Pt18.75Pd18.75Ni18.75Co18.75Cr25
    "X22.5": "darkolivegreen",       # Pt22.5Pd22.5Ni22.5Co22.5Cr10
}

def process_alloy(alloy_name, file_list):
    currents = []
    voltages = []

    for fname in file_list:
        path = os.path.join(root, alloy_name, fname)

        df = create_df(path)

        I = df[3].values
        V = df[2].values + shift

        I = I[2:]
        V = V[2:]

        voltages.append(V)
        currents.append(I)

    # need interpolate since data are diff lengths
    V_common = np.linspace(
        max(min(v) for v in voltages),
        min(max(v) for v in voltages),
        500
    )

    I_interp = []
    for V, I in zip(voltages, currents):
        idx = np.argsort(V)
        I_interp.append(np.interp(V_common, V[idx], I[idx]))

    I_interp = np.array(I_interp)

    I_mean = np.mean(I_interp, axis=0)
    I_std = np.std(I_interp, axis=0)
    I_sem = np.std(I_interp, axis=0) / np.sqrt(len(I_interp))

    return V_common, I_mean, I_std

# Plot
for alloy_name, files in alloys.items():
    Vc, Im, Is = process_alloy(alloy_name, files)
    color = alloy_colors.get(alloy_name, None)

    plt.plot(Vc, Im, linewidth=2.5, label=alloy_name, color=color)
    plt.fill_between(Vc, Im-Is, Im+Is, alpha=0.25, color=color)

plt.xlabel("Voltage vs. RHE")
plt.ylabel("Current density (mA/cm²)")
plt.title("LSV Curve Comparison")
plt.xlim(-1.1, 0.3)
plt.ylim(-400, 10)
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()

"""
# plot for alloys with Cr
alloys_subset_cr = [
    "X22.5",
    "Ni25Co25",
    "X18.75",
    "Ni10Co10",
    "PtPdNiCoCr",
    "PtPdCoNiCrFe",
]

subset_cr_colors = {
    "X22.5": "red",
    "Ni25Co25": "green",
    "X18.75": "purple",
    "Ni10Co10": "blue",
    "PtPdNiCoCr": "navy",
    "PtPdCoNiCrFe": "orange",
}

for alloy_name, files in alloys.items():
    if alloy_name not in alloys_subset_cr:
        continue

    Vc, Im, Is = process_alloy(alloy_name, files)
    color = subset_cr_colors.get(alloy_name, None)

    plt.plot(Vc, Im, linewidth=2.5, label=alloy_name, color=color)
    plt.fill_between(Vc, Im-Is, Im+Is, alpha=0.25, color=color)

plt.xlabel("Voltage vs. RHE")
plt.ylabel("Current density (mA/cm²)")
plt.title("LSV Curve Comparison (alloys with Cr)")
plt.xlim(-1.1, 0.3)
plt.ylim(-400, 10)
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()
"""
