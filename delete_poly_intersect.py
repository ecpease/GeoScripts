import geopandas as gpd

ws = gpd.read_file('ws_poly_2575.shp')
print(str('Number of extra rows in ws.shp is '), ws.intersects(ws).count() -1) # Python adds one, just leave it alone

if len(ws) > 0 :
    ws = ws.loc[ws['Shape_Area'] == max(ws['Shape_Area'])]
    print(ws)
    ws.to_file('ws_delrows.shp')
else:
    print("You're good to go, Em!")
