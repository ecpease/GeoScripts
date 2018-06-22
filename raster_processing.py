import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import os


# Mosaic Conditioned Rasters and assign projection

dirpath = os.path.join('path', 'to', 'file_input.ext')
out_fp = os.path.join('path', 'to', 'file_output.ext')
search_criteria = r"*.bil" # delete any xmls in the folder or it wont work, sorry
q = os.path.join(dirpath, search_criteria)
print(q)
dem_fps = glob.glob(q)
print(dem_fps)
src_files_to_mosaic = []
for fp in dem_fps:
    src = rasterio.open(fp)
    src_files_to_mosaic.append(src)
print(src_files_to_mosaic) # If get error: Memory Error, delecte any xmls or .ovr files
mosaic, out_trans = merge(src_files_to_mosaic)
out_meta = src.meta.copy()

proj = '﻿Proj4: +proj=longlat +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +no_defs'  # NAD 83
out_meta.update({"driver": "GTiff", "height": mosaic.shape[1], "width": mosaic.shape[2], "transform": out_trans, "crs":
                 proj})
print("Writing file...")
with rasterio.open(out_fp, "w", **out_meta) as dest:
    kwargs = src.meta
    kwargs.update(
        bigtiff='YES',
        dtype=rasterio.uint32
    )
    dest.write(mosaic)


# Re-Project Conditioned Raster to NAD 83 Albers Equal Area

print("Reprojecting raster to NAD83 Albers Equal Area...")
os.chdir("D:\\path\\to\\folder")
os.system('gdalwarp input.tif output_reprojected.tif -t_srs "+proj=aea +lat_1=29.5 +lat_2=45.5 +lat_0=23 +lon_0=-96 '
          '+x_0=0 +y_0=0 +ellps=GRS9- +towgs84=0,0,0,0,0,0,0 +units=m _no_defs"') # one way to do it
os.system('gdalwarp -t_srs "+proj=longlat +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +no_defs" -overwrite acc_test.tif flacc.tif') # another way to do it
os.system('gdal_translate -of "GTiff" acc.ascii acc_test.tif') # translate from one type of file to another
