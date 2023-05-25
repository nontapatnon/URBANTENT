import pandas as pd
import folium
from shapely.geometry import Point, Polygon
from streamlit_folium import st_folium


df = pd.read_csv('community.csv')
df_1 = df[df['type'] == 'ชุมชนแออัด']
df_2 = df[df['type'] == 'ชุมชนชานเมือง']
df_3 = df[df['type'] == 'ชุมชนหมู่บ้านจัดสรร']
df_4 = df[df['type'] == 'เคหะชุมชน']
df_5 = df[df['type'] == 'ชุมชนเมือง']
df_6 = df[df['type'] == 'ชุมชนอาคารสูง']



map_th = folium.Map(location=[13.756331, 100.501762], tiles="Stamen Toner", zoom_start=12)

for lat, lng, name in zip(#df_test['Latitude'],df_test['Longitude']):
        df_1['lat'].astype(float), 
        df_1['lng'].astype(float),
        df_1['name'] +", " + df_1['type']): 
       
   
    folium.CircleMarker(
        [lat, lng],
        radius=5,
       
        color='#fa0202',
        fill=True,
        popup= name,
        fill_color='#fa0202',
        fill_opacity=0.7,
        parse_html=False).add_to(map_th)

for lat, lng, name in zip(#df_test['Latitude'],df_test['Longitude']):
        df_2['lat'].astype(float), 
        df_2['lng'].astype(float),
        df_2['name'] +", " + df_2['type']): 
       
   
    folium.CircleMarker(
        [lat, lng],
        radius=5,
       
        color='#fa7202',
        fill=True,
        popup= name,
        fill_color='#fa7202',
        fill_opacity=0.7,
        parse_html=False).add_to(map_th)
    
for lat, lng, name in zip(#df_test['Latitude'],df_test['Longitude']):
        df_3['lat'].astype(float), 
        df_3['lng'].astype(float),
        df_3['name'] +", " + df_3['type']): 
       
   
    folium.CircleMarker(
        [lat, lng],
        radius=5,
       
        color='#fad902',
        fill=True,
        popup= name,
        fill_color='#fad902',
        fill_opacity=0.7,
        parse_html=False).add_to(map_th)
for lat, lng, name in zip(#df_test['Latitude'],df_test['Longitude']):
        df_4['lat'].astype(float), 
        df_4['lng'].astype(float),
        df_4['name'] +", " + df_4['type']): 
       
   
    folium.CircleMarker(
        [lat, lng],
        radius=5,
       
        color='#02fa49',
        fill=True,
        popup= name,
        fill_color='#02fa49',
        fill_opacity=0.7,
        parse_html=False).add_to(map_th)
    
for lat, lng, name in zip(#df_test['Latitude'],df_test['Longitude']):
        df_5['lat'].astype(float), 
        df_5['lng'].astype(float),
        df_5['name'] +", " + df_5['type']): 
       
   
    folium.CircleMarker(
        [lat, lng],
        radius=5,
       
        color='#027afa',
        fill=True,
        popup= name,
        fill_color='#027afa',
        fill_opacity=0.7,
        parse_html=False).add_to(map_th)
    
for lat, lng, name in zip(#df_test['Latitude'],df_test['Longitude']):
        df_6['lat'].astype(float), 
        df_6['lng'].astype(float),
        df_6['name'] +", " + df_6['type']): 
       
   
    folium.CircleMarker(
        [lat, lng],
        radius=5,
       
        color='#9b02fa',
        fill=True,
        popup= name,
        fill_color='#9b02fa',
        fill_opacity=0.7,
        parse_html=False).add_to(map_th)
    
# # call to render Folium map in Streamlit
st_data = st_folium(map_th, width=725)