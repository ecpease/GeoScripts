import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import os

# Read in and mosaic all rasters from a folder
dirpath = os.path.join(')
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

#Assign raster projection
proj = '﻿Proj4: +proj=longlat +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +no_defs'  # NAD 83
out_meta.update({"driver": "GTiff", "height": mosaic.shape[1], "width": mosaic.shape[2], "transform": out_trans, "crs":
                 proj})
# Write to file
print("Writing file...")
with rasterio.open(out_fp, "w", **out_meta) as dest:
    kwargs = src.meta
    kwargs.update(
        bigtiff='YES',
        dtype=rasterio.uint32
    )
    dest.write(mosaic)