import geopandas as gpd

# Read the shapefile using geopandas
shapefile_path = 'support\\ne_110m_admin_0_countries.shx'  # Replace with the path to the downloaded shapefile
gdf = gpd.read_file(shapefile_path)

# Convert multi-part geometries to single-part geometries
gdf_singlepart = gdf.explode()

# Fix any invalid geometries
gdf_valid = gdf_singlepart.buffer(0)

# Convert to GeoJSON format
output_geojson = 'coastline.geojson'  # Output file path
gdf_valid.to_file(output_geojson, driver='GeoJSON')