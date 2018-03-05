# geo_code

A bare bones python geocoder using Google Maps API and Pandas.

For larger csv files, use the Larger Geocoder - which breaks up your data into data frames of 100 rows a piece. These data frames are geocoded one at a time and saved as csv's while the code is executing. Then finally all data frames are appended and saved in a single csv.
