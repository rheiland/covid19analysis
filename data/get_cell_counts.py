import glob
from pyMCDS_cells import pyMCDS_cells
import numpy as np

xml_files = glob.glob('output*.xml')
xml_files.sort()
print(xml_files)
num_xml = len(xml_files)
print(num_xml)
tcount = 0
count_macs = np.zeros(44)
#mcds1 = pyMCDS('output00000001.xml', 'timeseries_set')
for xml_f in xml_files:
    # mcds = pyMCDS_cells('output00000001.xml','.')
    mcds = pyMCDS_cells(xml_f,'.')

    # Matlab (Adrianne)
    # ind1(tcount) = length(find( MCDS.discrete_cells.metadata.type == 3)); %CD8
    # ind2(tcount) = length(find( MCDS.discrete_cells.metadata.type == 4)); %macs
    # ind3(tcount) = length(find( MCDS.discrete_cells.metadata.type == 5)); %neutrophils
    # dead_cells(tcount) = length(MCDS.discrete_cells.dead_cells);
    # live_target_cells(tcount) = length(find( MCDS.discrete_cells.metadata.type == 1))-dead_cells(tcount);
    # infected_cells(tcount) = length(find(MCDS.discrete_cells.custom.virion>1));

    print('time=',mcds.get_time())
    cell_id = mcds.data['discrete_cells']['ID']
    num_cells = cell_id.shape[0]
    print('# cells = ',num_cells)
    cell_type = mcds.data['discrete_cells']['cell_type']
    macs = np.where(cell_type == 4.0)
    count_macs[tcount] = len(macs[0])
    print('# macs = ',len(macs[0]))
    # for idx in range(num_cells):
        # if (cell_ids[idx] == 4.0):  # macs
    tcount += 1
    # break