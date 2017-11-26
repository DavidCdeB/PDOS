#
import matplotlib.pyplot as plt
import sys
import numpy as np
import os

folder_222 = '/home/david/Trabajo/structures/PDOS_at_different_volumes/Calcite_I/CI_SCELPHONO_222_Volumes_PDOS/Adding_INTERPHESS_444_1'
folder_444 = '/home/david/Trabajo/structures/PDOS_at_different_volumes/Calcite_I/CI_SCELPHONO_444_Volumes_PDOS/Adding_INTERPHESS_444_1'

files_222 = ["116.573346_PDOS.PHONDOS",\
"118.139505_PDOS.PHONDOS",\
"119.713653_PDOS.PHONDOS",\
"121.297131_PDOS.PHONDOS",\
"122.894958_PDOS.PHONDOS",\
"124.510211_PDOS.PHONDOS",\
"124.512598_PDOS.PHONDOS",\
"125.884132_PDOS.PHONDOS",\
"127.054446_PDOS.PHONDOS",\
"127.265886_PDOS.PHONDOS",\
"128.656314_PDOS.PHONDOS",\
"130.054927_PDOS.PHONDOS",\
"131.463313_PDOS.PHONDOS",\
"132.880152_PDOS.PHONDOS",\
"134.309582_PDOS.PHONDOS",\
"135.750582_PDOS.PHONDOS",\
"137.200672_PDOS.PHONDOS"]

files_444 = ["116.573346.PHONDOS",\
"118.139505.PHONDOS",\
"119.713653.PHONDOS",\
"121.297131.PHONDOS",\
"122.894958.PHONDOS",\
"124.510211.PHONDOS",\
"124.512598.PHONDOS",\
"125.884132.PHONDOS",\
"127.054446.PHONDOS",\
"127.265886.PHONDOS",\
"128.656314.PHONDOS",\
"130.054927.PHONDOS",\
"131.463313.PHONDOS",\
"132.880152.PHONDOS",\
"134.309582.PHONDOS",\
"135.750582.PHONDOS",\
"137.200672.PHONDOS"]

vols_all = ["116.573346",\
"118.139505",\
"119.713653",\
"121.297131",\
"122.894958",\
"124.510211",\
"124.512598",\
"125.884132",\
"127.054446",\
"127.265886",\
"128.656314",\
"130.054927",\
"131.463313",\
"132.880152",\
"134.309582",\
"135.750582",\
"137.200672"]

vols = vols_all[0:3]
files_222_0_3 = files_222[0:3]
files_444_0_3 = files_444[0:3]

print 'len(vols) = ', len(vols)
fig = plt.figure()
plt.suptitle('Adding INTERPHESS 444', fontsize=12, fontweight="bold")

for indx_vols, indx_files in zip(range(1, len(vols)+1), range(len(vols))):
        print 'indx_vols init = ' , indx_vols
        print 'indx_files init = ' , indx_files
        ax = fig.add_subplot(len(vols), 1, indx_vols)
#       ax.set_title('V = ' + vols[indx_vols-1], fontsize=10) # This title stays in the center, and outside the graph
        ax.text(.85,.80,'V = ' + vols[indx_vols-1] + ' $\AA^{3}$', fontsize=10, #alpha=1.0,
            bbox=dict(alpha=1.0, facecolor='white', pad=1.0), #, facecolor='red', edgecolor='red'),
#           bbox=dict(facecolor='none', edgecolor='blue', pad=10.0, alpha=1.0),
#           alpha=1.0,
            horizontalalignment='center',
            transform=ax.transAxes)
        x_222, y_222 = np.loadtxt(os.path.join(folder_222, files_222_0_3[indx_files]), skiprows = 4).T
        x_444, y_444 = np.loadtxt(os.path.join(folder_444, files_444_0_3[indx_files]), skiprows = 4).T
        ax.plot(x_222, y_222, color='m', label='SCELPHONO 2x2x2') # black lines OK
        ax.plot(x_444, y_444, color='k', label='SCELPHONO 4x4x4') # magenta lines OK
        ax.grid()
#       ax.set_ylim(0.01, 1.01) 
#       ylabels = [0.0, 0.5, 1.0] 
#       ax.set_yticklabels(ylabels)#, #,rotation=0),
#                 verticalalignment='baseline')#,
#                 horizontalalignment='left')

        if indx_vols == 1 and indx_files == 0:
           print 'enter 1st if loop'
           print 'indx_vols == 1 and indx_files == 0: ', indx_files 
           ax.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
                mode="expand", borderaxespad=0, ncol=4)
           ax.set_ylabel('PDOS (states/cm$^{-1}$/cell)')
#          ax.set_title('Adding INTERPHESS', fontsize=9)
           ax.tick_params(labelbottom='off') 


        if indx_vols == len(vols) and indx_files == len(vols)-1:
           print 'enter 2nd if loop'
           print 'indx_files if indx_vols == len(vols)+1 and indx_files == len(vols): = ' , indx_files
           ax.set_xlabel('Energy (cm$^{-1}$)')

        else:
            ax.tick_params(labelbottom='off')

fig.savefig("PDOS_0-3.pdf", bbox_inches='tight', pad_inches=0.3)#, tight_layout() )#, bbox_inches=bbox)
plt.close()

vols = vols_all[3:6]
files_222_3_6 = files_222[3:6]
files_444_3_6 = files_444[3:6]

fig = plt.figure()
plt.suptitle('Adding INTERPHESS 444', fontsize=12, fontweight="bold")

print 'len(vols) second!= ', len(vols)
for indx_vols, indx_files in zip(range(1, len(vols)+1), range(len(vols))):
        print 'indx_vols init = ' , indx_vols
        print 'indx_files init = ' , indx_files
        ax = fig.add_subplot(len(vols), 1, indx_vols)
#       ax.set_title('V = ' + vols[indx_vols-1], fontsize=10) # This title stays in the center, and outside the graph
        ax.text(.85,.80,'V = ' + vols[indx_vols-1] + ' $\AA^{3}$', fontsize=10, #alpha=1.0,
            bbox=dict(alpha=1.0, facecolor='white', pad=1.0), #, facecolor='red', edgecolor='red'),
#           bbox=dict(facecolor='none', edgecolor='blue', pad=10.0, alpha=1.0),
#           alpha=1.0,
            horizontalalignment='center',
            transform=ax.transAxes)
        x_222, y_222 = np.loadtxt(os.path.join(folder_222, files_222_3_6[indx_files]), skiprows = 4).T
        x_444, y_444 = np.loadtxt(os.path.join(folder_444, files_444_3_6[indx_files]), skiprows = 4).T
        ax.plot(x_222, y_222, color='m', label='SCELPHONO 2x2x2') # black lines OK
        ax.plot(x_444, y_444, color='k', label='SCELPHONO 4x4x4') # magenta lines OK
        ax.grid()
#       ax.set_ylim(0.01, 1.01) 
#       ylabels = [0.0, 0.5, 1.0] 
#       ax.set_yticklabels(ylabels)#, #,rotation=0),
#                 verticalalignment='baseline')#,
#                 horizontalalignment='left')

        if indx_vols == 1 and indx_files == 0:
           print 'enter 1st if loop'
           print 'indx_vols == 1 and indx_files == 0: ', indx_files 
           ax.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
                mode="expand", borderaxespad=0, ncol=4)
           ax.set_ylabel('PDOS (states/cm$^{-1}$/cell)')
#          ax.set_title('Adding INTERPHESS', fontsize=9)
           ax.tick_params(labelbottom='off') 


        if indx_vols == len(vols) and indx_files == len(vols)-1:
           print 'enter 2nd if loop'
           print 'indx_files if indx_vols == len(vols)+1 and indx_files == len(vols): = ' , indx_files
           ax.set_xlabel('Energy (cm$^{-1}$)')

        else:
            ax.tick_params(labelbottom='off')

fig.savefig("PDOS_3-6.pdf", bbox_inches='tight', pad_inches=0.3)#, tight_layout() )#, bbox_inches=bbox)
plt.close()

vols = vols_all[6:9]
files_222_6_9 = files_222[6:9]
files_444_6_9 = files_444[6:9]

fig = plt.figure()
plt.suptitle('Adding INTERPHESS 444', fontsize=12, fontweight="bold")

print 'len(vols) = ', len(vols)
for indx_vols, indx_files in zip(range(1, len(vols)+1), range(len(vols))):
        print 'indx_vols init = ' , indx_vols
        print 'indx_files init = ' , indx_files
        ax = fig.add_subplot(len(vols), 1, indx_vols)
#       ax.set_title('V = ' + vols[indx_vols-1], fontsize=10) # This title stays in the center, and outside the graph
        ax.text(.85,.80,'V = ' + vols[indx_vols-1] + ' $\AA^{3}$', fontsize=10, #alpha=1.0,
            bbox=dict(alpha=1.0, facecolor='white', pad=1.0), #, facecolor='red', edgecolor='red'),
#           bbox=dict(facecolor='none', edgecolor='blue', pad=10.0, alpha=1.0),
#           alpha=1.0,
            horizontalalignment='center',
            transform=ax.transAxes)
        x_222, y_222 = np.loadtxt(os.path.join(folder_222, files_222_6_9[indx_files]), skiprows = 4).T
        x_444, y_444 = np.loadtxt(os.path.join(folder_444, files_444_6_9[indx_files]), skiprows = 4).T
        ax.plot(x_222, y_222, color='m', label='SCELPHONO 2x2x2') # black lines OK
        ax.plot(x_444, y_444, color='k', label='SCELPHONO 4x4x4') # magenta lines OK
        ax.grid()
#       ax.set_ylim(0.01, 1.01) 
#       ylabels = [0.0, 0.5, 1.0] 
#       ax.set_yticklabels(ylabels)#, #,rotation=0),
#                 verticalalignment='baseline')#,
#                 horizontalalignment='left')

        if indx_vols == 1 and indx_files == 0:
           print 'enter 1st if loop'
           print 'indx_vols == 1 and indx_files == 0: ', indx_files 
           ax.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
                mode="expand", borderaxespad=0, ncol=4)
           ax.set_ylabel('PDOS (states/cm$^{-1}$/cell)')
#          ax.set_title('Adding INTERPHESS', fontsize=9)
           ax.tick_params(labelbottom='off') 


        if indx_vols == len(vols) and indx_files == len(vols)-1:
           print 'enter 2nd if loop'
           print 'indx_files if indx_vols == len(vols)+1 and indx_files == len(vols): = ' , indx_files
           ax.set_xlabel('Energy (cm$^{-1}$)')

        else:
            ax.tick_params(labelbottom='off')

fig.savefig("PDOS_7-10.pdf", bbox_inches='tight', pad_inches=0.3)#, tight_layout() )#, bbox_inches=bbox)
plt.close()

vols = vols_all[9:12]

files_222_9_12 = files_222[9:12]
files_444_9_12 = files_444[9:12]

fig = plt.figure()
plt.suptitle('Adding INTERPHESS 444', fontsize=12, fontweight="bold")

print 'len(vols) = ', len(vols)
for indx_vols, indx_files in zip(range(1, len(vols)+1), range(len(vols))):
        print 'indx_vols init = ' , indx_vols
        print 'indx_files init = ' , indx_files
        ax = fig.add_subplot(len(vols), 1, indx_vols)
#       ax.set_title('V = ' + vols[indx_vols-1], fontsize=10) # This title stays in the center, and outside the graph
        ax.text(.85,.80,'V = ' + vols[indx_vols-1] + ' $\AA^{3}$', fontsize=10, #alpha=1.0,
            bbox=dict(alpha=1.0, facecolor='white', pad=1.0), #, facecolor='red', edgecolor='red'),
#           bbox=dict(facecolor='none', edgecolor='blue', pad=10.0, alpha=1.0),
#           alpha=1.0,
            horizontalalignment='center',
            transform=ax.transAxes)
        x_222, y_222 = np.loadtxt(os.path.join(folder_222, files_222_9_12[indx_files]), skiprows = 4).T
        x_444, y_444 = np.loadtxt(os.path.join(folder_444, files_444_9_12[indx_files]), skiprows = 4).T
        ax.plot(x_222, y_222, color='m', label='SCELPHONO 2x2x2') # black lines OK
        ax.plot(x_444, y_444, color='k', label='SCELPHONO 4x4x4') # magenta lines OK
        ax.grid()
#       ax.set_ylim(0.01, 1.01) 
#       ylabels = [0.0, 0.5, 1.0] 
#       ax.set_yticklabels(ylabels)#, #,rotation=0),
#                 verticalalignment='baseline')#,
#                 horizontalalignment='left')

        if indx_vols == 1 and indx_files == 0:
           print 'enter 1st if loop'
           print 'indx_vols == 1 and indx_files == 0: ', indx_files 
           ax.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
                mode="expand", borderaxespad=0, ncol=4)
           ax.set_ylabel('PDOS (states/cm$^{-1}$/cell)')
#          ax.set_title('Adding INTERPHESS', fontsize=9)
           ax.tick_params(labelbottom='off') 


        if indx_vols == len(vols) and indx_files == len(vols)-1:
           print 'enter 2nd if loop'
           print 'indx_files if indx_vols == len(vols)+1 and indx_files == len(vols): = ' , indx_files
           ax.set_xlabel('Energy (cm$^{-1}$)')

        else:
            ax.tick_params(labelbottom='off')

fig.savefig("PDOS_10-13.pdf", bbox_inches='tight', pad_inches=0.3)#, tight_layout() )#, bbox_inches=bbox)
plt.close()

vols = vols_all[12:15]
files_222_12_15 = files_222[12:15]
files_444_12_15 = files_444[12:15]

print 'len(vols) = ', len(vols)
fig = plt.figure()
plt.suptitle('Adding INTERPHESS 444', fontsize=12, fontweight="bold")

for indx_vols, indx_files in zip(range(1, len(vols)+1), range(len(vols))):
        print 'indx_vols init = ' , indx_vols
        print 'indx_files init = ' , indx_files
        ax = fig.add_subplot(len(vols), 1, indx_vols)
#       ax.set_title('V = ' + vols[indx_vols-1], fontsize=10) # This title stays in the center, and outside the graph
        ax.text(.85,.80,'V = ' + vols[indx_vols-1] + ' $\AA^{3}$', fontsize=10, #alpha=1.0,
            bbox=dict(alpha=1.0, facecolor='white', pad=1.0), #, facecolor='red', edgecolor='red'),
#           bbox=dict(facecolor='none', edgecolor='blue', pad=10.0, alpha=1.0),
#           alpha=1.0,
            horizontalalignment='center',
            transform=ax.transAxes)
        x_222, y_222 = np.loadtxt(os.path.join(folder_222, files_222_12_15[indx_files]), skiprows = 4).T
        x_444, y_444 = np.loadtxt(os.path.join(folder_444, files_444_12_15[indx_files]), skiprows = 4).T
        ax.plot(x_222, y_222, color='m', label='SCELPHONO 2x2x2') # black lines OK
        ax.plot(x_444, y_444, color='k', label='SCELPHONO 4x4x4') # magenta lines OK
        ax.grid()
#       ax.set_ylim(0.01, 1.01) 
#       ylabels = [0.0, 0.5, 1.0] 
#       ax.set_yticklabels(ylabels)#, #,rotation=0),
#                 verticalalignment='baseline')#,
#                 horizontalalignment='left')

        if indx_vols == 1 and indx_files == 0:
           print 'enter 1st if loop'
           print 'indx_vols == 1 and indx_files == 0: ', indx_files 
           ax.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
                mode="expand", borderaxespad=0, ncol=4)
           ax.set_ylabel('PDOS (states/cm$^{-1}$/cell)')
#          ax.set_title('Adding INTERPHESS', fontsize=9)
           ax.tick_params(labelbottom='off') 


        if indx_vols == len(vols) and indx_files == len(vols)-1:
           print 'enter 2nd if loop'
           print 'indx_files if indx_vols == len(vols)+1 and indx_files == len(vols): = ' , indx_files
           ax.set_xlabel('Energy (cm$^{-1}$)')

        else:
            ax.tick_params(labelbottom='off')

fig.savefig("PDOS_14-17.pdf", bbox_inches='tight', pad_inches=0.3)#, tight_layout() )#, bbox_inches=bbox)
plt.close()

vols = vols_all[15:17]
print 'vols = ', vols
files_222_15_17 = files_222[15:17]
print 'files_222_15_17 = ', files_222_15_17
files_444_15_17 = files_444[15:17]
print 'files_444_15_17 = ', files_444_15_17

fig = plt.figure()
plt.suptitle('Adding INTERPHESS 444', fontsize=12, fontweight="bold")

print 'len(vols) = ', len(vols)
for indx_vols, indx_files in zip(range(1, len(vols)+1), range(len(vols))):
        print 'indx_vols init = ' , indx_vols
        print 'indx_files init = ' , indx_files
        ax = fig.add_subplot(len(vols), 1, indx_vols)
#       ax.set_title('V = ' + vols[indx_vols-1], fontsize=10) # This title stays in the center, and outside the graph
        ax.text(.85,.80,'V = ' + vols[indx_vols-1] + ' $\AA^{3}$', fontsize=10, #alpha=1.0,
            bbox=dict(alpha=1.0, facecolor='white', pad=1.0), #, facecolor='red', edgecolor='red'),
#           bbox=dict(facecolor='none', edgecolor='blue', pad=10.0, alpha=1.0),
#           alpha=1.0,
            horizontalalignment='center',
            transform=ax.transAxes)
        x_222, y_222 = np.loadtxt(os.path.join(folder_222, files_222_15_17[indx_files]), skiprows = 4).T
        x_444, y_444 = np.loadtxt(os.path.join(folder_444, files_444_15_17[indx_files]), skiprows = 4).T

        print 'folder_444 = ', folder_444
        print 'files_444 17-18= ', files_444_15_17[indx_files] ## this is wrong, because it prints "files_444 =  118.139505.PHONDOS"
 
        ax.plot(x_222, y_222, color='m', label='SCELPHONO 2x2x2') # black lines OK
        ax.plot(x_444, y_444, color='k', label='SCELPHONO 4x4x4') # magenta lines OK
        ax.grid()
#       ax.set_ylim(0.01, 1.01) 
#       ylabels = [0.0, 0.5, 1.0] 
#       ax.set_yticklabels(ylabels)#, #,rotation=0),
#                 verticalalignment='baseline')#,
#                 horizontalalignment='left')

        if indx_vols == 1 and indx_files == 0:
           print 'enter 1st if loop'
           print 'indx_vols == 1 and indx_files == 0: ', indx_files 
           ax.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
                mode="expand", borderaxespad=0, ncol=4)
           ax.set_ylabel('PDOS (states/cm$^{-1}$/cell)')
#          ax.set_title('Adding INTERPHESS', fontsize=9)
           ax.tick_params(labelbottom='off') 


        if indx_vols == len(vols) and indx_files == len(vols)-1:
           print 'enter 2nd if loop'
           print 'indx_files if indx_vols == len(vols)+1 and indx_files == len(vols): = ' , indx_files
           ax.set_xlabel('Energy (cm$^{-1}$)')

        else:
            ax.tick_params(labelbottom='off')

fig.savefig("PDOS_17-18.pdf", bbox_inches='tight', pad_inches=0.3)#, tight_layout() )#, bbox_inches=bbox)
plt.close()
#plt.show()

vols_0 = vols_all[0]
vols_8 = vols_all[8]
vols = [vols_0, vols_8]

print 'vols = ', vols
files_222_0_8 = [files_222[0], files_222[8]]
print 'files_222_0_8 = ', files_222_0_8
files_444_0_8 = [files_444[0], files_444[8]]
print 'files_444_0_8 = ', files_444_0_8

fig = plt.figure()
plt.suptitle('Adding INTERPHESS 444', fontsize=12, fontweight="bold")
print 'len(vols) = ', len(vols)
for indx_vols, indx_files in zip(range(1, len(vols)+1), range(len(vols))):
        print 'indx_vols init = ' , indx_vols
        print 'indx_files init = ' , indx_files
        ax = fig.add_subplot(len(vols), 1, indx_vols)
#       ax.set_title('V = ' + vols[indx_vols-1], fontsize=10) # This title stays in the center, and outside the graph
        ax.text(.85,.80,'V = ' + vols[indx_vols-1] + ' $\AA^{3}$', fontsize=10, #alpha=1.0,
            bbox=dict(alpha=1.0, facecolor='white', pad=1.0), #, facecolor='red', edgecolor='red'),
#           bbox=dict(facecolor='none', edgecolor='blue', pad=10.0, alpha=1.0),
#           alpha=1.0,
            horizontalalignment='center',
            transform=ax.transAxes)
        x_222, y_222 = np.loadtxt(os.path.join(folder_222, files_222_0_8[indx_files]), skiprows = 4).T
        x_444, y_444 = np.loadtxt(os.path.join(folder_444, files_444_0_8[indx_files]), skiprows = 4).T
        print 'folder_444 = ', folder_444
        print 'files_444 = ', files_444_0_8[indx_files] ## this now correct (rints "files_444 =  118.139505.PHONDOS")
        ax.plot(x_222, y_222, color='m', label='SCELPHONO 2x2x2') # black lines OK
        ax.plot(x_444, y_444, color='k', label='SCELPHONO 4x4x4') # magenta lines OK
        ax.grid()
#       ax.set_ylim(0.01, 1.01) 
#       ylabels = [0.0, 0.5, 1.0] 
#       ax.set_yticklabels(ylabels)#, #,rotation=0),
#                 verticalalignment='baseline')#,
#                 horizontalalignment='left')

        if indx_vols == 1 and indx_files == 0:
           print 'enter 1st if loop'
           print 'indx_vols == 1 and indx_files == 0: ', indx_files 
           ax.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
                mode="expand", borderaxespad=0, ncol=4)
           ax.set_ylabel('PDOS (states/cm$^{-1}$/cell)')
#          ax.set_title('Adding INTERPHESS', fontsize=9)
           ax.tick_params(labelbottom='off') 


        if indx_vols == len(vols) and indx_files == len(vols)-1:
           print 'enter 2nd if loop'
           print 'indx_files if indx_vols == len(vols)+1 and indx_files == len(vols): = ' , indx_files
           ax.set_xlabel('Energy (cm$^{-1}$)')

        else:
            ax.tick_params(labelbottom='off')

fig.savefig("PDOS_0_and_8.pdf", bbox_inches='tight', pad_inches=0.3)#, tight_layout() )#, bbox_inches=bbox)


### Subplot1: V = 116 & v = 127; SCELPHONO 444:
### Subplot2: V = 116 & v = 127; SCELPHONO 222:

vols_0 = vols_all[0] # V=116
vols_8 = vols_all[8] # V=127

vols = ['4x4x4', '2x2x2']
fig = plt.figure()
plt.suptitle('Adding INTERPHESS 444', fontsize=12, fontweight="bold")

print 'len(vols) = ', len(vols)

ax = fig.add_subplot(len(vols), 1, 1)
ax.text(.85,.80,'SCELPHONO ' + vols[0], fontsize=10, #alpha=1.0,
            bbox=dict(alpha=1.0, facecolor='white', pad=1.0), #, facecolor='red', edgecolor='red'),
#           bbox=dict(facecolor='none', edgecolor='blue', pad=10.0, alpha=1.0),
#           alpha=1.0,
            horizontalalignment='center',
            transform=ax.transAxes)

x_444_V_116, y_444_V_116 = np.loadtxt(os.path.join(folder_444, files_444[0]), skiprows = 4).T
x_444_V_127, y_444_V_127 = np.loadtxt(os.path.join(folder_444, files_444[8]), skiprows = 4).T

ax.plot(x_444_V_116, y_444_V_116, color='k', label='V = ' + vols_0)
#ax.plot(x_444_V_127, y_444_V_127, color='r', linestyle='--', label='V = ' + vols_8)
ax.plot(x_444_V_127, y_444_V_127, color='r', label='V = ' + vols_8)

ax.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
                mode="expand", borderaxespad=0, ncol=4)
ax.set_ylabel('PDOS (states/cm$^{-1}$/cell)')
#ax.set_title('Adding INTERPHESS', fontsize=9)
ax.tick_params(labelbottom='off')
ax.grid()

ax2 = fig.add_subplot(len(vols), 1, 2) #, sharey=ax) # -> Add <sharey=ax> in order to have the same ylims as ax subplot
ax2.text(.85,-.40,'SCELPHONO ' + vols[1], fontsize=10, #alpha=1.0,
            bbox=dict(alpha=1.0, facecolor='white', pad=1.0), #, facecolor='red', edgecolor='red'),
#           bbox=dict(facecolor='none', edgecolor='blue', pad=10.0, alpha=1.0),
#           alpha=1.0,
            horizontalalignment='center',
            transform=ax.transAxes)

x_222_V_116, y_222_V_116 = np.loadtxt(os.path.join(folder_222, files_222[0]), skiprows = 4).T
x_222_V_127, y_222_V_127 = np.loadtxt(os.path.join(folder_222, files_222[8]), skiprows = 4).T

ax2.plot(x_222_V_116, y_222_V_116, color='k', label='V = ' + vols_0)
#ax2.plot(x_222_V_127, y_222_V_127, color='r', linestyle='--', label='V = ' + vols_8)
ax2.plot(x_222_V_127, y_222_V_127, color='r', label='V = ' + vols_8)
ax2.set_xlabel('Energy (cm$^{-1}$)')
ax2.grid()
fig.savefig("PDOS_0_and_8_both_scelphonos.pdf", bbox_inches='tight', pad_inches=0.3)#, tight_layout() )#, bbox_inches=bbox)


### Subplot1: V = 116;  SCELPHONO 444, with and without interpolation:
### Subplot2: V = 127;  SCELPHONO 444, with and without interpolation:
folder_444_no_inter = '/home/david/Trabajo/structures/PDOS_at_different_volumes/Calcite_I/CI_SCELPHONO_444_Volumes_PDOS'

vols_0 = vols_all[0] # V=116
vols_8 = vols_all[8] # V=127

vols = ['4x4x4', '2x2x2']
fig = plt.figure()
print 'len(vols) = ', len(vols)

ax = fig.add_subplot(len(vols), 1, 1)
ax.text(.85,.80,'SCELPHONO ' + vols[0], fontsize=10, #alpha=1.0,
            bbox=dict(alpha=1.0, facecolor='white', pad=1.0), #, facecolor='red', edgecolor='red'),
#           bbox=dict(facecolor='none', edgecolor='blue', pad=10.0, alpha=1.0),
#           alpha=1.0,
            horizontalalignment='center',
            transform=ax.transAxes)

x_444_V_116, y_444_V_116 = np.loadtxt(os.path.join(folder_444, files_444[0]), skiprows = 4).T
x_444_V_116_no_inter, y_444_V_116_no_inter = np.loadtxt(os.path.join(folder_444_no_inter, files_444[0]), skiprows = 4).T

ax.plot(x_444_V_116, y_444_V_116, color='k', linestyle='-', label='V = ' + vols_0 + ' INTERPHESS')
ax.plot(x_444_V_116_no_inter, y_444_V_116_no_inter, color='orange', label='V = ' + vols_0 )

#ax.plot(x_444_V_127, y_444_V_127, color='r', linestyle='--', label='V = ' + vols_8 + 'INTERPHESS')
#ax.plot(x_444_V_127_no_inter, y_444_V_127_no_inter, color='r', label='V = ' + vols_8)

ax.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
                mode="expand", borderaxespad=0, ncol=4)
ax.set_ylabel('PDOS (states/cm$^{-1}$/cell)')
#ax.set_title('Adding INTERPHESS', fontsize=9)
ax.tick_params(labelbottom='off')
ax.grid()
#plt.show()
#sys.exit()

ax2 = fig.add_subplot(len(vols), 1, 2) #, sharey=ax) # -> Add <sharey=ax> in order to have the same ylims as ax subplot
ax2.text(.85,-.40,'SCELPHONO ' + vols[0], fontsize=10, #alpha=1.0,
            bbox=dict(alpha=1.0, facecolor='white', pad=1.0), #, facecolor='red', edgecolor='red'),
#           bbox=dict(facecolor='none', edgecolor='blue', pad=10.0, alpha=1.0),
#           alpha=1.0,
            horizontalalignment='center',
            transform=ax.transAxes)

x_444_V_127, y_444_V_127 = np.loadtxt(os.path.join(folder_444, files_444[8]), skiprows = 4).T
x_444_V_127_no_inter, y_444_V_127_no_inter = np.loadtxt(os.path.join(folder_444_no_inter, files_444[8]), skiprows = 4).T

ax2.plot(x_444_V_127, y_444_V_127, color='m', linestyle='-', label='V = ' + vols_8 + ' INTERPHESS 444')
ax2.plot(x_444_V_127_no_inter, y_444_V_127_no_inter, color='orange', label='V = ' + vols_8 )

ax2.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
                mode="expand", borderaxespad=0, ncol=4)
#ax2.set_ylabel('PDOS (states/cm$^{-1}$/cell)')
#ax.set_title('Adding INTERPHESS', fontsize=9)
#ax2.tick_params(labelbottom='off')
ax2.grid()
#plt.show()
#sys.exit()


ax2.set_xlabel('Energy (cm$^{-1}$)')
fig.savefig("PDOS_0_and_8_both_scelphonos_effect_of_INTERPHESS.pdf", bbox_inches='tight', pad_inches=0.3)#, tight_layout() )#, bbox_inches=bbox)


# V = 127, Scelphono 444 and Scelphono 222 + Interphess 222
vols_0 = vols_all[8]
fig = plt.figure()
ax = fig.add_subplot(2, 1, 1)
ax.text(.85,.80,'V = ' + vols_0 + ' $\AA^{3}$', fontsize=10, #alpha=1.0,
            bbox=dict(alpha=1.0, facecolor='white', pad=1.0), #, facecolor='red', edgecolor='red'),
#           bbox=dict(facecolor='none', edgecolor='blue', pad=10.0, alpha=1.0),
#           alpha=1.0,
            horizontalalignment='center',
            transform=ax.transAxes)

x_444, y_444 = np.loadtxt(os.path.join(folder_444_no_inter, files_444[8]), skiprows = 4).T
x_222, y_222 = np.loadtxt('/home/david/Trabajo/structures/PDOS_at_different_volumes/Calcite_I/CI_SCELPHONO_222_Volumes_PDOS/Adding_INTERPHESS_222_1/127.054446_PD_PHONDOS', skiprows = 4).T
print 'folder_444 = ', folder_444
print 'files_444[8] = ', files_444[8]

ax.plot(x_222, y_222, color='m', label='SCELPHONO 2x2x2 + INTERPHESS 222') # black lines OK
ax.plot(x_444, y_444, color='k', label='SCELPHONO 4x4x4') # magenta lines OK

ax.grid()
#       ax.set_ylim(0.01, 1.01) 
#       ylabels = [0.0, 0.5, 1.0] 
#       ax.set_yticklabels(ylabels)#, #,rotation=0),
#                 verticalalignment='baseline')#,
#                 horizontalalignment='left')

ax.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
            mode="expand", borderaxespad=0, ncol=4)
ax.set_ylabel('PDOS (states/cm$^{-1}$/cell)')
#ax.set_title('Adding INTERPHESS', fontsize=9)
#ax.tick_params(labelbottom='off') 
ax.set_xlabel('Energy (cm$^{-1}$)')

fig.savefig("PDOS_8_Scelphono_444_and_Scelphono_222_plus_interphess_222.pdf", bbox_inches='tight', pad_inches=0.3)#, tight_layout() )#, bbox_inches=bbox)


plt.show()


