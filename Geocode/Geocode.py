import pandas as pd
import geopandas as gpd
import requests
from shapely.geometry import Point

# Function to geocode an address using Photon
def geocode_address_photon(house, city, state, zip_code):
    # Combine the address components into a single string
    address = f"{house}, {city}, {state} {zip_code}"
    url = f"http://photon.komoot.io/api/?q={address}"  # Updated to use the current domain
    response = requests.get(url)
    data = response.json()
    if data['features']:
        lon, lat = data['features'][0]['geometry']['coordinates']
        return Point(lon, lat)
    else:
        return None

# Load addresses from CSV
addresses_df = pd.read_csv('Addresses.csv')

# Geocode addresses
# Adjust the column names 'House', 'City', 'State', 'Zip' to match your CSV file's exact column names
geometry = [geocode_address_photon(row['House'], row['City'], row['State'], row['Zip']) 
            for index, row in addresses_df.iterrows()]
geocoded_gdf = gpd.GeoDataFrame(addresses_df, geometry=geometry)

# Set the CRS for the GeoDataFrame to WGS 84 (EPSG:4326)
geocoded_gdf.set_crs(epsg=4326, inplace=True)

# Optional: Save the geocoded addresses to a new file
geocoded_gdf.to_file("Geocoded_Addresses.shp", driver='ESRI Shapefile')