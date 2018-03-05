import requests
import pandas as pd

address_df = pd.read_csv('YOUR_FILE_PATH.csv', encoding = "ISO-8859-1")

google_api_key = "YOUR_GOOGLE_MAPS_KEY"

def geocode2(row):
    try:
        address = row
        url = 'https://maps.googleapis.com/maps/api/geocode/json'
        params = {'key' : google_api_key, 'sensor': 'false', 'address': address}
        r = requests.get(url, params=params)
        results = r.json()['results']
        location = results[0]['geometry']['location']
        return(location['lat'], location['lng'])
    except:
        return 'Could not geocode'

#we're going to break up the csv into dataframes of 100 rows each and geocode 100 at a time, saving progress as we go 
df_list = []
for g, df in address_df.groupby(np.arange(len(address_df)) // 100):
    df_list.append(df)

#iterate through our list of dataframes, saving our progress as we go
for i, df in enumerate(df_list):
    print("starting df " + str(i))
    file_name = "Geocoded_" + str(i) + ".csv"
    #make sure you have a column called "Address" that contains the full address
    df['Lat_Long'] = df['Address'].apply(lambda x : geocode2(x))
    df.to_csv(file_name, index=False)


#this will append all the dataframes and save them in one file
pd.concat(df_list).to_csv('Geocoded_Full.csv', index=False)