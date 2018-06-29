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
    ws.to_file('ws_delrows2.shp')
elif len(ws) == 1:
    print("You're good to go, Em!")
    print("Thanks, Em :)")