import requests
import pandas as pd

address_df = pd.read_csv('YOUR_FILE_PATH.csv', encoding = "ISO-8859-1")


google_api_key = "YOUR_GOOGLE_MAPS_KEY"
url = 'https://maps.googleapis.com/maps/api/geocode/json'

def geocode2(row):
    try:
        address = row
        params = {'key' : google_api_key, 'sensor': 'false', 'address': address}
        r = requests.get(url, params=params)
        results = r.json()['results']
        location = results[0]['geometry']['location']
        return(location['lat'], location['lng'])
    except:
        return 'Could not geocode'

#make sure you have a column called "Address" that contains the full address
address_df['Lat_Long'] = address_df['Address'].apply(lambda x : geocode2(x))

address_df['Lat'] = address_df['Lat_Long'].apply(lambda x: str(x).split(',')[0].replace('(','') )
address_df['Lon'] = address_df['Lat_Long'].apply(lambda x: str(x).split(',')[1].replace(')','') )

address_df.to_csv('Geocoded.csv', index=False)
