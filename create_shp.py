import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import os
# df = pd.read_excel('RioGrandeSites.xlsx')
# # print(df.head())
# shp = df['DEC_LONG_VA', 'DEC_LAT_VA']
# shp = gpd.GeoDataFrame(df, geometry='geometry')
# df.crs= "+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs" #WGS84
# df.to_file('RGsite.shp')
masterDF = pd.read_excel('Clearwater_SiteInformation.xlsx')
masterDF.dropna(subset=['Longitude', 'Latitude'],inplace=True)
masterDF['geometry'] = masterDF.apply(lambda xy: Point(xy['Longitude'],xy['Latitude']),axis=1)
masterDF = masterDF[['StationNo', 'SiteName', 'SiteType', 'WellNo', 'GeologicUnit', 'Aquifer', 'geometry']]
# masterDF['geometry'] = masterDF['geometry'].astype(str)
# masterDF['DEC_LAT_VA'] = masterDF['DEC_LAT_VA'].astype(float)

# proj4 = '+proj=longlat +ellps=GRS80 +datum=NAD83 +no_defs ' # from epsg 4269
proj4 = '+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs'
masterDF = gpd.GeoDataFrame(masterDF,geometry='geometry' ,crs=proj4)
masterDF.to_file(os.path.join('shapefile', 'ClearwaterSites.shp'))
print(masterDF['geometry'])
proj4_utm ='+proj=longlat +ellps=GRS80 +datum=NAD83 +no_defs '


# print(masterDF.head())

# now reporject to nad83 albers
# proj4_albers = '+proj=utm +zone=4 +ellps=GRS80 +datum=NAD83 +units=m +no_defs' # i'm guessing it is this one http://spatialreference.org/ref/epsg/3083/ but double check
# masterDF.to_crs(proj4_albers)
# print(masterDF.dtypes())


masterDF = masterDF.to_crs(proj4_utm)

print(masterDF['geometry'])
print(masterDF.crs)
masterDF.to_file(os.path.join('shapefile', 'ClearwaterSites2.shp'))