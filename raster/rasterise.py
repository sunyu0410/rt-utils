import nibabel as nib
import numpy as np
import sys
sys.path.append('rt-utils')
from rt_utils import RTStructBuilder

rtstruct = RTStructBuilder.create_new('ct-dcm')
mask = nib.load('seg-test.nii.gz').get_fdata().astype(np.uint8)

#mask = np.swapaxes(mask, 0, 1) # mask.shape[:2] must match with dcm.pixel_array.shape
mask1 = mask==1

rtstruct.add_roi(mask1, name='mask1')

rtstruct.save('./mask1')


rtstruct2 = RTStructBuilder.create_from('ct-dcm', rt_struct_path='mask1.dcm')
mask1_reload = rtstruct2.get_roi_mask_by_name('mask1')

print(np.all(mask1==mask1_reload))
