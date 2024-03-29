import folium
from streamlit_folium import st_folium
import pandas as pd
import streamlit as st
from folium.plugins import HeatMap, HeatMapWithTime

df = pd.read_csv('community.csv')
heatmap_df = pd.read_csv('districtBKK_den_loc.csv')
# ['เขต', 'ชุมชน (ชุมชน)', 'ประชากร (คน)', 'ครอบครัว (ครอบครัว)''หลังคาเรือน (หลัง)', 'District', 'LAT', 'LONG']
heatmap_df0 = heatmap_df[['LAT','LONG','ประชากร (คน)']]
heatmap_df1 = heatmap_df[['LAT','LONG','District']]

heatmap_df_risk = pd.read_csv('districtBKK_risk.csv')
heatmap_df_risk0 = heatmap_df_risk[['LAT','LONG','Risk']]
heatmap_df_risk1 = heatmap_df_risk[['LAT','LONG','District']]
heatmap_df_unocc = pd.read_csv('Unoccupied.csv')
heatmap_df_unocc = heatmap_df_unocc.iloc[:-1]
heatmap_df_unocc = heatmap_df_unocc.rename(columns = {'Unnamed: 0':'name'})
heatmap_df_unocc2 = heatmap_df_unocc[['latitude', 'longitude', ' ect_lessthan15 ']]
heatmap_df_unocc2[' ect_lessthan15 '] = heatmap_df_unocc2[' ect_lessthan15 '].str.replace(',','').astype(int)
heatmap_df_unocc3 = heatmap_df_unocc[['latitude','longitude','name']]


# _1 = st.checkbox('ชุมชนแออัด')
# _2 = st.checkbox('ชุมชนชานเมือง')
# _3 = st.checkbox('ชุมชนหมู่บ้านจัดสรร')
# _4 = st.checkbox('เคหะชุมชน')
# _5 = st.checkbox('ชุมชนเมือง')
# _6 = st.checkbox('ชุมชนอาคารสูง')

# df = pd.read_csv('community.csv')
df_1 = df[df['type'] == 'ชุมชนแออัด']
df_2 = df[df['type'] == 'ชุมชนชานเมือง']
df_3 = df[df['type'] == 'ชุมชนหมู่บ้านจัดสรร']
df_4 = df[df['type'] == 'เคหะชุมชน']
df_5 = df[df['type'] == 'ชุมชนเมือง']
# df_6 = df[df['type'] == 'ชุมชนอาคารสูง']

map_th_risk = folium.Map(location=[13.80174488029037, 100.5863404554943], tiles="Stamen Toner", zoom_start=10)
HeatMap(heatmap_df_risk0, 
        min_opacity=0.4,
        blur = 18
               ).add_to(folium.FeatureGroup(name='Heat Map').add_to(map_th_risk))

for lat, lng, name in zip(heatmap_df_risk1['LAT'].astype(float), heatmap_df_risk1['LONG'].astype(float), 'เขต' + heatmap_df_risk1['District']):
    folium.CircleMarker(
        [lat, lng],
        radius=10,
        color= None,
        fill=True,
        popup=folium.Popup(name, max_width="100"),
        fill_color='#000000',
        fill_opacity= 0,
        parse_html=False
    ).add_to(map_th_risk)

map_th0 = folium.Map(location=[13.80174488029037, 100.5863404554943], tiles="Stamen Toner", zoom_start=10)
HeatMap(heatmap_df0, 
        min_opacity=0.4,
        blur = 18
               ).add_to(folium.FeatureGroup(name='Heat Map').add_to(map_th0))

for lat, lng, name in zip(heatmap_df1['LAT'].astype(float), heatmap_df1['LONG'].astype(float), 'เขต' + heatmap_df1['District']):
    folium.CircleMarker(
        [lat, lng],
        radius=10,
        color= None,
        fill=True,
        popup=folium.Popup(name, max_width="100"),
        fill_color='#000000',
        fill_opacity= 0,
        parse_html=False
    ).add_to(map_th0)
# folium.LayerControl().add_to(map_th0)

map_th = folium.Map(location=[13.80174488029037, 100.5863404554943], tiles="Stamen Toner", zoom_start=10)
for lat, lng, name in zip(df_1['lat'].astype(float), df_1['lng'].astype(float), df_1['name'] + "\n(" + df_1['type'] + ")"):
    folium.CircleMarker(
        [lat, lng],
        radius=5,
        color='#fa0202',
        fill=True,
        popup=folium.Popup(name, max_width="100"),
        fill_color='#fa0202',
        fill_opacity=0.7,
        parse_html=False
    ).add_to(map_th)
for lat, lng, name in zip(df_2['lat'].astype(float), df_2['lng'].astype(float), df_2['name'] + "\n(" + df_2['type'] + ")"):
    folium.CircleMarker(
        [lat, lng],
        radius=5,
        color='#fa7202',
        fill=True,
        popup=folium.Popup(name, max_width="100"),
        fill_color='#fa7202',
        fill_opacity=0.7,
        parse_html=False
    ).add_to(map_th)
for lat, lng, name in zip(df_3['lat'].astype(float), df_3['lng'].astype(float), df_3['name'] + "\n(" + df_3['type'] + ")"):
    folium.CircleMarker(
        [lat, lng],
        radius=5,
        color='#fad902',
        fill=True,
        popup=folium.Popup(name, max_width="100"),
        fill_color='#fad902',
        fill_opacity=0.7,
        parse_html=False
    ).add_to(map_th)
for lat, lng, name in zip(df_4['lat'].astype(float), df_4['lng'].astype(float), df_4['name'] + "\n(" + df_4['type'] + ")"):
    folium.CircleMarker(
        [lat, lng],
        radius=5,
        color='#02fa49',
        fill=True,
        popup=folium.Popup(name, max_width="100"),
        fill_color='#02fa49',
        fill_opacity=0.7,
        parse_html=False
    ).add_to(map_th)
for lat, lng, name in zip(df_5['lat'].astype(float), df_5['lng'].astype(float), df_5['name'] + "\n(" + df_5['type'] + ")"):
    folium.CircleMarker(
        [lat, lng],
        radius=5,
        color='#027afa',
        fill=True,
        popup=folium.Popup(name, max_width="100"),
        fill_color='#027afa',
        fill_opacity=0.7,
        parse_html=False
    ).add_to(map_th)

map_th1 = folium.Map(location=[13.80174488029037, 100.5863404554943], tiles="Stamen Toner", zoom_start=10)
for lat, lng, name in zip(df_1['lat'].astype(float), df_1['lng'].astype(float), df_1['name'] + "\n(" + df_1['type'] + ")"):
    folium.CircleMarker(
        [lat, lng],
        radius=5,
        color='#fa0202',
        fill=True,
        popup=folium.Popup(name, max_width="100"),
        fill_color='#fa0202',
        fill_opacity=0.7,
        parse_html=False
    ).add_to(map_th1)
# map1 = st_folium(map_th1, width=700, height= 500, returned_objects=[])

map_th2 = folium.Map(location=[13.80174488029037, 100.5863404554943], tiles="Stamen Toner", zoom_start=10)
for lat, lng, name in zip(df_2['lat'].astype(float), df_2['lng'].astype(float), df_2['name'] + "\n(" + df_2['type'] + ")"):
    folium.CircleMarker(
        [lat, lng],
        radius=5,
        color='#fa7202',
        fill=True,
        popup=folium.Popup(name, max_width="100"),
        fill_color='#fa7202',
        fill_opacity=0.7,
        parse_html=False
    ).add_to(map_th2)
# map2 = st_folium(map_th2, width=700, height= 500, returned_objects=[])

map_th3 = folium.Map(location=[13.80174488029037, 100.5863404554943], tiles="Stamen Toner", zoom_start=10)
for lat, lng, name in zip(df_3['lat'].astype(float), df_3['lng'].astype(float), df_3['name'] + "\n(" + df_3['type'] + ")"):
    folium.CircleMarker(
        [lat, lng],
        radius=5,
        color='#fad902',
        fill=True,
        popup=folium.Popup(name, max_width="100"),
        fill_color='#fad902',
        fill_opacity=0.7,
        parse_html=False
    ).add_to(map_th3)
# map3 = st_folium(map_th3, width=700, height= 500, returned_objects=[])

map_th4 = folium.Map(location=[13.80174488029037, 100.5863404554943], tiles="Stamen Toner", zoom_start=10)
for lat, lng, name in zip(df_4['lat'].astype(float), df_4['lng'].astype(float), df_4['name'] + "\n(" + df_4['type'] + ")"):
    folium.CircleMarker(
        [lat, lng],
        radius=5,
        color='#02fa49',
        fill=True,
        popup=folium.Popup(name, max_width="100"),
        fill_color='#02fa49',
        fill_opacity=0.7,
        parse_html=False
    ).add_to(map_th4)
# map4 = st_folium(map_th4, width=700, height= 500, returned_objects=[])

map_th5 = folium.Map(location=[13.80174488029037, 100.5863404554943], tiles="Stamen Toner", zoom_start=10)
for lat, lng, name in zip(df_5['lat'].astype(float), df_5['lng'].astype(float), df_5['name'] + "\n(" + df_5['type'] + ")"):
    folium.CircleMarker(
        [lat, lng],
        radius=5,
        color='#027afa',
        fill=True,
        popup=folium.Popup(name, max_width="100"),
        fill_color='#027afa',
        fill_opacity=0.7,
        parse_html=False
    ).add_to(map_th5)
# map5 = st_folium(map_th5, width=700, height= 500, returned_objects=[])

map_elec = folium.Map(location=[13.80174488029037, 100.5863404554943], tiles="Stamen Toner", zoom_start=10)
HeatMap(heatmap_df_unocc2, 
        min_opacity=0.4,
        blur = 18
               ).add_to(folium.FeatureGroup(name='Heat Map').add_to(map_elec))

for lat, lng, name in zip(heatmap_df_unocc['latitude'].astype(float), heatmap_df_unocc['longitude'].astype(float),heatmap_df_unocc['name']):
    folium.CircleMarker(
        [lat, lng],
        radius=10,
        color= None,
        fill=True,
        popup=folium.Popup(name, max_width="100"),
        fill_color='#000000',
        fill_opacity= 0,
        parse_html=False
    ).add_to(map_elec)




# -----------------------------
import geopandas as gpd
import folium

# Load the district boundaries from the GeoJSON file
districts = gpd.read_file('district.json', encoding='utf-8')

def style_function(feature):
    return {
        'fillColor': '#ffffff',  # Set the fill color of polygons
        'color': '#00f2ff',      # Set the border color of polygons
        'weight': 1,             # Set the border width in pixels
        'fillOpacity': 0       # Set the opacity of the polygon fill
    }
# Create a Folium map centered on Thailand
map_border = folium.Map(location=[13.80174488029037, 100.5863404554943], tiles="Cartodbdark_matter", zoom_start=10) #"Stamen Toner", zoom_start=8)

# Add the district boundaries to the map
folium.GeoJson(districts, style_function=style_function,
    highlight_function=lambda x: {'weight': 3, 'color': '#3f999e','fillOpacity': 0.7 },
    tooltip=folium.GeoJsonTooltip(fields=['dname'], labels=False, sticky=True)).add_to(map_border)


# ====== healthcare ======
import streamlit as st
import pandas as pd
import pydeck as pdk

data = pd.read_csv("health.csv",sep=',')
# data = data[['Restaurant','Longitude','Latitude']]
data = data[['name','lng','lat']]
data.columns = ['name', 'lng', 'lat']
# data = pd.DataFrame({
#     "lng": [longitude_values],
#     "lat": [latitude_values]
# })

# Define a layer to display on a map
layer = pdk.Layer(
    "HexagonLayer",
    data,
    get_position=["lng", "lat"],
    auto_highlight=True,
    elevation_scale=50,
    pickable=True,
    elevation_range=[0, 1000],
    extruded=True,
    coverage=0.8,
)

# Set the viewport location
view_state = pdk.ViewState(
    longitude=data['lng'].mean(), latitude=data['lat'].mean(), zoom=8, min_zoom=3, max_zoom=15, pitch=30, bearing=0,
)





# -----------------------------

# st.sidebar.title("49 Urban Tent \nSelect Community Map")
st.sidebar.title("49 URBAN TENT")

option = st.sidebar.radio(
    "Which community would you like to show",
    ('ทั้งหมด','ชุมชนแออัด', 'ชุมชนชานเมือง', 'ชุมชนหมู่บ้านจัดสรร','เคหะชุมชน','ชุมชนเมือง','Population Heatmap','Risk Heatmap','Unoccupied Heatmap', 'District Border', 'Healthcare'))

# option = st.selectbox(
#     'Select community type',
#     ('ชุมชนแออัด', 'ชุมชนชานเมือง', 'ชุมชนหมู่บ้านจัดสรร','เคหะชุมชน','ชุมชนเมือง'))

height_ = 500
width_ = 725


if option == 'ทั้งหมด':
    # df = df[df['type'] == 'ชุมชนแออัด']
    st_folium(map_th , width = width_,height=height_,  returned_objects=[])
if option == 'ชุมชนแออัด':
    # df = df[df['type'] == 'ชุมชนแออัด']
    st_folium(map_th1,width = width_,height=height_, returned_objects=[])
if option == 'ชุมชนชานเมือง':
    # df = df[df['type'] == 'ชุมชนชานเมือง']
    st_folium(map_th2,width = width_,height=height_, returned_objects=[])
if option == 'ชุมชนหมู่บ้านจัดสรร':
    # df = df[df['type'] == 'ชุมชนหมู่บ้านจัดสรร']
    st_folium(map_th3,width = width_,height=height_, returned_objects=[])
if option == 'เคหะชุมชน':
    # df = df[df['type'] == 'เคหะชุมชน']
    st_folium(map_th4,width = width_, height=height_, returned_objects=[])
if option == 'ชุมชนเมือง':
    # df = df[df['type'] == 'ชุมชนเมือง']
    st_folium(map_th5,width = width_ , height=height_, returned_objects=[])
if option == 'Population Heatmap':
    # df = df[df['type'] == 'ชุมชนเมือง']
    st_folium(map_th0, width = width_, height=height_, returned_objects=[])
if option == 'Risk Heatmap':
    # df = df[df['type'] == 'ชุมชนเมือง']
    st_folium(map_th_risk,width = width_, height=height_, returned_objects=[])
if option == 'Unoccupied Heatmap':
    # df = df[df['type'] == 'ชุมชนเมือง']
    st_folium(map_elec,width = width_, height=height_, returned_objects=[])
if option == 'District Border':
    # df = df[df['type'] == 'ชุมชนเมือง']
    st_folium(map_border, width = width_, height=height_, returned_objects=[])
if option == 'Healthcare':
    # Render using Streamlit
    st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))



# df_1 = df[df['type'] == 'ชุมชนแออัด']
# df_2 = df[df['type'] == 'ชุมชนชานเมือง']
# df_3 = df[df['type'] == 'ชุมชนหมู่บ้านจัดสรร']
# df_4 = df[df['type'] == 'เคหะชุมชน']
# df_5 = df[df['type'] == 'ชุมชนเมือง']
# df_6 = df[df['type'] == 'ชุมชนอาคารสูง']

# map_th = folium.Map(location=[13.80174488029037, 100.5863404554943], tiles="Stamen Toner", zoom_start=12)

# for lat, lng, name in zip(df_1['lat'].astype(float), df_1['lng'].astype(float), df_1['name'] + "\n(" + df_1['type'] + ")"):
#     folium.CircleMarker(
#         [lat, lng],
#         radius=5,
#         color='#fa0202',
#         fill=True,
#         popup=folium.Popup(name, max_width="100"),
#         fill_color='#fa0202',
#         fill_opacity=0.7,
#         parse_html=False
#     ).add_to(map_th)

# for lat, lng, name in zip(df_2['lat'].astype(float), df_2['lng'].astype(float), df_2['name'] + "\n(" + df_2['type'] + ")"):
#     folium.CircleMarker(
#         [lat, lng],
#         radius=5,
#         color='#fa7202',
#         fill=True,
#         popup=folium.Popup(name, max_width="100"),
#         fill_color='#fa7202',
#         fill_opacity=0.7,
#         parse_html=False
#     ).add_to(map_th)

# for lat, lng, name in zip(df_3['lat'].astype(float), df_3['lng'].astype(float), df_3['name'] + "\n(" + df_3['type'] + ")"):
#     folium.CircleMarker(
#         [lat, lng],
#         radius=5,
#         color='#fad902',
#         fill=True,
#         popup=folium.Popup(name, max_width="100"),
#         fill_color='#fad902',
#         fill_opacity=0.7,
#         parse_html=False
#     ).add_to(map_th)

# for lat, lng, name in zip(df_4['lat'].astype(float), df_4['lng'].astype(float), df_4['name'] + "\n(" + df_4['type'] + ")"):
#     folium.CircleMarker(
#         [lat, lng],
#         radius=5,
#         color='#02fa49',
#         fill=True,
#         popup=folium.Popup(name, max_width="100"),
#         fill_color='#02fa49',
#         fill_opacity=0.7,
#         parse_html=False
#     ).add_to(map_th)

# for lat, lng, name in zip(df_5['lat'].astype(float), df_5['lng'].astype(float), df_5['name'] + "\n(" + df_5['type'] + ")"):
#     folium.CircleMarker(
#         [lat, lng],
#         radius=5,
#         color='#027afa',
#         fill=True,
#         popup=folium.Popup(name, max_width="100"),
#         fill_color='#027afa',
#         fill_opacity=0.7,
#         parse_html=False
#     ).add_to(map_th)

# for lat, lng, name in zip(df_6['lat'].astype(float), df_6['lng'].astype(float), df_6['name'] + "\n(" + df_6['type'] + ")"):
#     folium.CircleMarker(
#         [lat, lng],
#         radius=5,
#         color='#9b02fa',
#         fill=True,
#         popup=folium.Popup(name, max_width="100"),
#         fill_color='#9b02fa',
#         fill_opacity=0.7,
#         parse_html=False
#     ).add_to(map_th)

# Save the map as a static image
# map_th.save('static_map.html')
# st_folium(map_th, width=700, height= 500, returned_objects=[])