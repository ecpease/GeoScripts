"""
Written by Emily Pease

Script to open a layer (shapefile) and determine how many features are present.  This is in the
context of watershed delineation.  It creates three columns called Site_ID, Site_Name,
and Area_sq_mi in addition to deleting any extra rows present in the geodataframe
(attribute table) that the analyst would not want included.

Often times, during watershed delineation, ESRI will create stand-alone raster cells as
part of the watershed.  This script deletes all of those.  

"""


import geopandas as gpd
import os

ws = gpd.GeoDataFrame.from_file(os.path.join('real.gdb'), layer='ws_poly2')
print(str('Number of extra rows in ws.shp is '), ws.intersects(ws).count() -1) # Extra rows, not TOTAL rows

ws['Site_ID'] = ''
ws['Site_Name'] = ''
ws['Area_sq_mi'] = ''

if len(ws) > 1:
    ws = ws.loc[ws['Shape_Area'] == max(ws['Shape_Area'])]
    print(ws)
    print(ws.touches(ws))
    ws.to_file('ws_delrows.shp')
elif len(ws) == 1:
    print("You're good to go!")
    print("Thanks :)")
