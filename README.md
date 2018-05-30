# Bare Bones Python (Pandas) Geocoder (Google Maps API)

All that is required to get this working is a csv file with a column named `address` and a [Google Maps API key](https://developers.google.com/maps/documentation/geocoding/get-api-key)

For larger csv files, use the Larger Geocoder - which breaks up your data into data frames of 100 rows a piece. These data frames are geocoded one at a time and saved as csv's while the code is executing. Then finally all data frames are appended and saved in a single csv.
