import numpy as np
import pandas as pd
import datetime
import folium
import json
import matplotlib.pyplot as plt
from datetime import date, datetime, time, timezone

df = pd.read_csv("samsung/final_project/covid.csv")
#df.info()
# df["Year"] = pd.to_datetime(df['Day'])
# df.set_index('Year', inplace=True)
# df.drop(['Day'], axis=1, inplace=True)

#df.head()
#print(len(df['location'].unique()))

covid_c = df.groupby(['Country'])

# for key,group in covid_c:
#     print('+key:', key)
#     print('+number:', len(group))
#     print(group.head())
#     print('\n')
    
total_df = covid_c.sum()
#print(total_df.head())

# map = folium.Map(location = [37.2594750011864, 127.05145091394964],
#                  zoom_start=13,
#                  tiles="stamenwatercolor"
#                  )

# map.save('samsung/final_project/index.html')
# #map
# marker_map = folium.Map(location=[43.27017110116431, 76.89366300769296], zoom_start=12, tiles="Stamen Terrain")

# folium.Marker(
#     location=[43.27017110116431, 76.89366300769296],
#     popup="Mt. Hood Meadows",
#     icon=folium.Icon(icon="cloud"),
# ).add_to(marker_map)

# folium.Marker(
#     location=[43.27017110116431, 76.89366300769296],
#     popup="Timberline Lodge",
#     icon=folium.Icon(color="green"),
#     ).add_to(marker_map)

# folium.CircleMarker(
#     location=[43.27017110116431, 76.89366300769296],
#     radius=100,
#     popup="circle",
#     color="#3186cc",
# ).add_to(marker_map)

#map

# url = (
#     "https://github.com/python-visualization/folium/tree/main/examples/data"
# )

# state_geo = "samsung/final_project/us-states.json"
# state_unemployment = 'samsung/final_project/US_Unemployment_Oct2012.csv'
# state_data = pd.read_csv(state_unemployment)

# m = folium.Map(loction=[48, -102], zoom_start=3)

# folium.Choropleth(
#     geo_data=state_geo,
#     name="chotopleth",
#     data = state_data,
#     colums = ["State", "Unemployment"],
#     key_on="feature.id",
#     fill_color="YlGn",
#     fill_opacity=0.7,
#     line_opacity=0.2,
#     legend_name="Unemployment Rate (%)",
# ).add_to(m)

# folium.LayerControl().add_to(m)

#m

center = [35.762887375145795, 84.08313219586536]

m = folium.Map(location=center, zoom_start=2,
               max_bounds= True,
               min_zoom=1, min_lat=-84,
               max_lat=84,min_lon=-175, max_lon=187,
               )

geo_path = 'samsung/final_project/countries.geojson'

json_data = json.load(open(geo_path))

folium.Choropleth(geo_data = json_data,
                  data = total_df,
                  columns=(total_df.index,'Daily new confirmed deaths due to COVID-19 per million people'),
                  key_on='properties.ADMIN',
                  fill_color='Blues',
                  fill_opacity=0.7,
                  line_opacity=0.5,
                  ).add_to(m)

folium.LayerControl().add_to(m)

m.save('samsung/final_project/index.html')
m