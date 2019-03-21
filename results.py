#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

rcParams['font.family'] = 'serif'
rcParams['font.serif'] = ['Computer Modern Roman']

f = plt.figure(figsize=(3.5, 2.25))
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

alpha=1
M = [98, 83, 78, 65, 37, 18]
S = [1, 3, 2, 3, 2, 2]

x = np.arange(6)
labels = ['Ref', 'LPCNet\n(unquant)', 'Opus\n9 kb/s', 'LPCNet\n1.6 kb/s', 'MELP', 'Speex']
line1 = plt.errorbar(x, M, S, capsize=2, alpha=alpha, color='#0000d0', linestyle=' ', marker='.', label='Reference')
plt.xticks(x, labels)

plt.axes().set_yticks([30, 50, 70, 90], minor=True)

plt.tick_params(axis='both', which='major', labelsize=9)
plt.ylim(10, 100)
plt.yticks([20, 40, 60, 80, 100])
#plt.xlabel('Dense Equivalent Units', fontsize=9)
plt.ylabel('Quality (MUSHRA)', fontsize=9)
plt.grid(True, which='both')

f.savefig("mushra1.pdf", bbox_inches='tight')
