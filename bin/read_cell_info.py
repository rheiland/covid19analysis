import scipy
from scipy import io

cells_dict = {}
# fix file pathname for cross-platform!!
#dir = "/Users/heiland/dev/cancer_EMEWS_1.0.0/run1/"
iframe = 500
#fname = "output%08d_cells" % iframe
fname = "output%08d_cells_physicell" % iframe

#fname = "output00000001_cells"
#print("fname = ",fname)
#scipy.io.loadmat(dir + fname, cells_dict)
scipy.io.loadmat(fname, cells_dict)
#val = cells_dict['basic_agents']
val = cells_dict['cells']


#scipy.io.loadmat("output00000358_cells_physicell",cells_dict)
#val = cells_dict['cells']

# Create points
num_pts = val.shape[1]
print "num_pts =",num_pts
#newPts = vtk.vtkPoints()
#cell_color_ID = vtk.vtkFloatArray()
#cell_diam = vtk.vtkFloatArray()

#kdx=6
#if (kdx == 5): 
#  scalars.SetName('cell_type')
#elif (kdx == 6): 
#  scalars.SetName('cycle_model')
#elif (kdx == 7): 
#  scalars.SetName('current_phase')

#cell_color_ID.SetName('cell_color_ID')
#cell_diam.SetName('cell_diameter')

maxDist = 0.0
maxDist = 500.0
maxDist = 3.9
for idx in range(0, num_pts):
  # rf. PhysiCell User Guide for these array indices to a cell's position.
  x = val[1,idx]
  y = -val[2,idx]  # invert Y (points down)
  z = val[3,idx]
#  dist = math.sqrt(x*x + y*y + z*z)
#  if dist > maxDist:
#    maxDist = dist
#  newPts.InsertPoint(idx, x/maxDist,y/maxDist,z/maxDist)
#  sval = val[kdx,idx]
  sval = 0   # immune cells are black??
  if val[5,idx] == 1:  # immune cell type
    sval = 1   # lime green 
  if val[7,idx] > 100 and val[7,idx] < 104:
    sval = 2   # necrotic: brownish
  elif val[7,idx] == 100:
    sval = 3   # apoptotic: red

#  cell_color_ID.InsertNextValue(sval)
  # V=(4/3)pi*r^3 -> r^3 = v*0.75/pi
#  diam = (val[4,idx]*0.2387)**0.333 * 2.0
  radius = (val[4,idx]*0.2387)**0.333 
#  diam = diam/22.0
#  diam = diam*5
#  cell_diam.InsertNextValue(diam)

#print 'maxDist = ',maxDist

# Add the points to the vtkPolyData object.
#pdo.SetPoints(newPts)
#pdo.GetPointData().AddArray(cell_color_ID)
#pdo.GetPointData().AddArray(cell_diam)

#verts = vtk.vtkCellArray()
#for idx in range(0, num_pts):
#  verts.InsertNextCell(1)
#  verts.InsertCellPoint(idx)

#pdo.SetVerts(verts)
