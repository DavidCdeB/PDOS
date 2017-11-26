#
import re
import os
import glob
from itertools import islice
import numpy as np
import subprocess
import itertools
import sys
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


# Obtaining xtics and xtic-labels :
path='./'
template = os.path.join(path, '*.PHONBANDS')

fname = glob.glob(template)
print fname[0]
fname = fname[0]
#sys.exit()

All_Tics_on_x =[]
All_Labels_Tics_on_x = []
#for fname in glob.glob(template):
#  print fname
f = open(fname, 'r')
for line in f:

        if re.match(r"^@ XAXIS TICK     ", line):
                   
                  parameters = line
                  print 'parameters = ', parameters
                  p = parameters.split()
                  print 'p = ', p
                  Tics_on_x = p[4]
                  All_Tics_on_x.append(Tics_on_x)

        if re.match(r"^@ XAXIS TICKLABEL    ", line):
                  
                  parameters = line
                  print 'parameters = ', parameters
                  p = parameters.split()
                  print 'p = ', p
                  aux = p[3]
                  
                  aux2 = re.search('"(.*)"', aux)
                  Labels_Tics_on_x = aux2.group(1)

                  print 'Labels_Tics_on_x = ', Labels_Tics_on_x
                  All_Labels_Tics_on_x.append(Labels_Tics_on_x)

print 'All_Tics_on_x = ', All_Tics_on_x
print 'All_Labels_Tics_on_x = ', All_Labels_Tics_on_x


gen = (r for r in open(fname) if not r[0] in ('@', '#'))
data = np.genfromtxt(gen)
print type(data)

print np.shape(data)

print 'data[0][1:] = ', data[0][1:] # Extracts Ys(X1)
print 'data[0, 1:] = ', data[0, 1:] # "      

print 'data[1][1:] = ', data[1][1:] # Extracts Ys(X2)
print 'data[1, 1:] = ', data[1, 1:] # " 

print 'data[:, 1:] = ', data[:, 1:] # Extracts Ys(X1) + Ys(X2)
#######

print 'data[:][0] = ' , data[:][0]
print 'data[:, 0] = ' , data[:, 0]

fig = plt.figure()
plt.plot(data[:, 0], data[:, 1:], '-')
#plt.plot(data[:, 0], data[:, 1:], 'o-')

print 'type(All_Tics_on_x) = ', type(All_Tics_on_x)
print 'type(All_Tics_on_x[0]) = ', type(All_Tics_on_x[0])
All_Tics_on_x = [float(i) for i in All_Tics_on_x]
print 'type(All_Tics_on_x) = ', type(All_Tics_on_x)
print 'type(All_Tics_on_x[0]) = ', type(All_Tics_on_x[0])

plt.xticks(All_Tics_on_x, All_Labels_Tics_on_x)#, rotation='vertical')
plt.grid()
plt.xlabel('')
plt.ylabel('Energy (cm$^{-1}$)')
title_string = 'Phonon Band Structure B3LYP, BS-A\n'
suptitle_string = 'V = 127.054446 $\AA^{3}$. SCELPHONO 4x4x4.\nThe phonon dispersion calc. interpolates up to 320 k-points'
plt.suptitle(title_string, y=1., fontsize=14)
plt.title(suptitle_string, fontsize=10)
fig.savefig("Phonon_dispersion.pdf", bbox_inches='tight', pad_inches=0.3) #, tight_layout() , bbox_inches=bbox)

plt.show()
sys.exit()



