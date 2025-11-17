# -*- coding: utf-8 -*-
"""
Created on Sun Oct 26 13:01:45 2025

@author: emily
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


root = r'C:\Users\emily\OneDrive\Documents\GitHub\clinic'
data = pd.read_csv(os.path.join(root, 'Ni_analog_test_data.csv'))

Vin = data['V in (V)']
Iout = data['Converted I (mA)']

plt.figure()
plt.scatter(Vin, Iout, s=10)
plt.xlabel('Voltage vs. Reference (V)')
plt.ylabel('Reaction Current (mA/cm\u00b2)')
plt.title('Ni electrode, analog potentiostat')
plt.grid(True)
plt.show()
