import pandas as pd
import folium
import json

df = pd.read_csv("samsung/final_project/covid.csv")

covid_c = df.groupby(['Country'])

total_df = covid_c.sum()

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

m.save('samsung/final_project/death.html')
m