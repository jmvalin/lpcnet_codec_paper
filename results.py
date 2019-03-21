#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

rcParams['font.family'] = 'serif'
rcParams['font.serif'] = ['Computer Modern Roman']

f = plt.figure(figsize=(3.15, 2.25))
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

alpha=1
M = [96.45085995085995, 80.92628992628993, 70.71007371007371, 62.770270270270274, 40.34643734643735, 16.723587223587224]
S= [1.0379529732616408, 1.4369615731372152, 1.5308744570855792, 1.5540355221401643, 1.4036532266711577, 0.9904327587887473]

M2 = [98.18532338308458, 83.72014925373135, 77.98258706467662, 65.85323383084577, 37.07587064676617, 17.79726368159204] 
S2 = [0.7177322786293536, 1.1948726816966997, 1.27490737255248, 1.4683757808615971, 1.326762298776267, 0.9732949527323175]


x = np.arange(6)
labels = ['Ref', 'LPCNet\nunquant', 'Opus\n9 kb/s', 'LPCNet\n1.6 kb/s', 'MELP\n2.4 kb/s', 'Speex\n4 kb/s']
line1 = plt.errorbar(x-0.12, M, S, capsize=2, alpha=alpha, color='#0000d0', linestyle=' ', marker='_', markersize=3.2, label='Set 1')
line2 = plt.errorbar(x+0.12, M2, S2, capsize=2, alpha=alpha, color='#c00000', linestyle=' ', marker='.', markersize=3.2, label='Set 2')
plt.xticks(x, labels)

plt.axes().set_yticks([30, 50, 70, 90], minor=True)
plt.axes().set_xticks(np.arange(7)-0.5, minor=True)

plt.tick_params(axis='x', which='major', labelsize=6, length=0)
plt.tick_params(axis='y', which='major', labelsize=8)
plt.ylim(10, 100)
plt.yticks([20, 40, 60, 80, 100])
#plt.xlabel('Dense Equivalent Units', fontsize=9)
plt.ylabel('Quality (MUSHRA)', fontsize=8, labelpad=0)
plt.grid(True, which='both', axis='y')
plt.grid(True, which='minor', axis='x')

plt.legend(handles=[line1, line2], loc=1, fontsize=8)

f.savefig("mushra1.pdf", bbox_inches='tight')
