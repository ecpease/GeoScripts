import geopandas as gpd

ws = gpd.read_file('ws_poly_2575.shp')
print(str('Number of extra rows in ws.shp is '), ws.intersects(ws).count() -1) # Extra rows, not TOTAL rows

if len(ws) > 1:
    ws = ws.loc[ws['Shape_Area'] == max(ws['Shape_Area'])]
    print(ws)
    ws.to_file('ws_delrows.shp')
elif len(ws) == 1:
    print("You're good to go, Em!")
    print("Thanks, Em :)")
