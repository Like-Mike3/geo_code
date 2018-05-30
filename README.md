# Bare Bones Geocoder

[Install Pandas](https://pandas.pydata.org/pandas-docs/version/0.22.0/install.html), grab a [Google Maps API key](https://developers.google.com/maps/documentation/geocoding/get-api-key), and make sure your csv file has a column named named `address` and you're good to go.   

For larger csv files, use the Larger Geocoder - which breaks up your data into data frames of 100 rows a piece. These data frames are geocoded one at a time and saved as csv's while the code is executing. Then finally all data frames are appended and saved in a single csv.
