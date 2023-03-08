import sys
sys.path.append('.')

from rt_utils import RTStructBuilder
import numpy as np

mask = np.load('raster/mask.npy') == 1

rtstruct = RTStructBuilder.create_new(
    dicom_series_path='dcm'
)

rtstruct.add_roi(mask=mask)

rtstruct.save('rt_util_result')