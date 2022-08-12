import pandas as pd
import folium
import json

df = pd.read_csv("samsung/final_project/covid-vaccination-doses-per-capita.csv")
df["Date"] = pd.to_datetime(df['Day'])
df.set_index('Date', inplace=True)
df.drop(['Day'], axis=1, inplace=True)

covid_c = df.groupby(['Entity'])

total_df = covid_c.sum()

center = [43.36934117528415, 76.85875490159314]
#35.762887375145795, 84.08313219586536

m = folium.Map(location=center, zoom_start=7,
               max_bounds= True,
               min_zoom=1, min_lat=-84,
               max_lat=84,min_lon=-175, max_lon=187,
               )

geo_path = 'samsung/final_project/countries.geojson'

json_data = json.load(open(geo_path))

folium.Choropleth(geo_data = json_data,
                  data = total_df,
                  columns=(total_df.index,'total_vaccinations_per_hundred'),
                  key_on='properties.ADMIN',
                  fill_color='Blues',
                  fill_opacity=0.7,
                  line_opacity=2,
                  ).add_to(m)

folium.LayerControl().add_to(m)

m.save('samsung/final_project/vaccine.html')
m