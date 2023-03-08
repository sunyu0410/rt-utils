# Create a dummpy segmentation.

import pydicom
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('.')
from rt_utils import RTStructBuilder

# Create a dummpy segmentation.
dcm = pydicom.read_file('raster/dcm2/MRBRAIN.DCM')

mask = np.zeros_like(dcm.pixel_array)
mask[100:200, 100:200] = 1
mask[125:150, 125:150] = 0
mask[300:350, 300:350] = 1
mask = np.expand_dims(mask, -1)

rtstruct = RTStructBuilder.create_new(
    dicom_series_path='raster/dcm2'
)

rtstruct.add_roi(mask=mask==1)
rtstruct.save('raster/rt_util_hole_result')

# Load existing RT Struct. Requires the series path and existing RT Struct path
rtstruct = RTStructBuilder.create_from(
  dicom_series_path="raster/dcm2", 
  rt_struct_path="raster/rt_util_hole_result.dcm"
)

# View all of the ROI names from within the image
print(rtstruct.get_roi_names())

# Loading the 3D Mask from within the RT Struct
mask_3d = rtstruct.get_roi_mask_by_name("ROI-1")

# Display one slice of the region
first_mask_slice = mask_3d[:, :, 0]
plt.imshow(first_mask_slice)
plt.show()