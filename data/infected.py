import glob
from pyMCDS_cells import pyMCDS_cells
import numpy as np
import matplotlib.pyplot as plt   # if you want to plot results

# run this script from your output directory
xml_files = glob.glob('output*.xml')
xml_files.sort()
print(xml_files)

n = len(xml_files)
t = np.zeros(n)
uninfected = np.zeros(n)
infected = np.zeros(n)
dead = np.zeros(n)
idx = 0
for f in xml_files:
    mcds = pyMCDS_cells(f,'.')
    t[idx] = mcds.get_time()

    cycle = mcds.data['discrete_cells']['cycle_model']
    cycle = cycle.astype(int)
    
    ID_uninfected = np.where((mcds.data['discrete_cells']['assembled_virion'] < 1) & (cycle < 100))
    ID_infected = np.where((mcds.data['discrete_cells']['assembled_virion'] >= 1) & (cycle < 100))
    uninfected[idx] = len(ID_uninfected[0])
    infected[idx] = len(ID_infected[0])
 
    dead_ID = np.where( cycle >= 100 )
    dead[idx] = len(dead_ID[0])
#    print(infected)
#    print(dead)

    idx += 1

plt.plot(t,uninfected, label='uninfected', linewidth=2)
plt.plot(t,infected, label='infected', linewidth=2)
plt.plot(t,dead, label='dead', linewidth=2)
plt.legend(loc='center left', prop={'size': 8})
plt.show()