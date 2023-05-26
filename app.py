# import folium
# from streamlit_folium import st_folium
# import pandas as pd
# import streamlit as st

# df = pd.read_csv('community.csv')
# df_1 = df[df['type'] == 'ชุมชนแออัด']
# df_2 = df[df['type'] == 'ชุมชนชานเมือง']
# df_3 = df[df['type'] == 'ชุมชนหมู่บ้านจัดสรร']
# df_4 = df[df['type'] == 'เคหะชุมชน']
# df_5 = df[df['type'] == 'ชุมชนเมือง']
# df_6 = df[df['type'] == 'ชุมชนอาคารสูง']

# map_th = folium.Map(location=[13.756331, 100.501762], tiles="Stamen Toner", zoom_start=12)

# for lat, lng, name in zip(#df_test['Latitude'],df_test['Longitude']):
#         df_1['lat'].astype(float), 
#         df_1['lng'].astype(float),
#         df_1['name'] +", " + df_1['type']): 
       
#     folium.CircleMarker(
#         [lat, lng],
#         radius=5,
       
#         color='#fa0202',
#         fill=True,
#         popup= folium.Popup(name, max_width="100"),
#         fill_color='#fa0202',
#         fill_opacity=0.7,
#         parse_html=False).add_to(map_th)

# for lat, lng, name in zip(#df_test['Latitude'],df_test['Longitude']):
#         df_2['lat'].astype(float), 
#         df_2['lng'].astype(float),
#         df_2['name'] +", " + df_2['type']): 
       
   
#     folium.CircleMarker(
#         [lat, lng],
#         radius=5,
       
#         color='#fa7202',
#         fill=True,
#         popup= folium.Popup(name, max_width="100"),
#         fill_color='#fa7202',
#         fill_opacity=0.7,
#         parse_html=False).add_to(map_th)
    
# for lat, lng, name in zip(#df_test['Latitude'],df_test['Longitude']):
#         df_3['lat'].astype(float), 
#         df_3['lng'].astype(float),
#         df_3['name'] +", " + df_3['type']): 
   
#     folium.CircleMarker(
#         [lat, lng],
#         radius=5,
       
#         color='#fad902',
#         fill=True,
#         popup= folium.Popup(name, max_width="100"),
#         fill_color='#fad902',
#         fill_opacity=0.7,
#         parse_html=False).add_to(map_th)
# for lat, lng, name in zip(#df_test['Latitude'],df_test['Longitude']):
#         df_4['lat'].astype(float), 
#         df_4['lng'].astype(float),
#         df_4['name'] +", " + df_4['type']): 
       
   
#     folium.CircleMarker(
#         [lat, lng],
#         radius=5,
       
#         color='#02fa49',
#         fill=True,
#         popup= folium.Popup(name, max_width="100"),
#         fill_color='#02fa49',
#         fill_opacity=0.7,
#         parse_html=False).add_to(map_th)
    
# for lat, lng, name in zip(#df_test['Latitude'],df_test['Longitude']):
#         df_5['lat'].astype(float), 
#         df_5['lng'].astype(float),
#         df_5['name'] +", " + df_5['type']): 
       

#     folium.CircleMarker(
#         [lat, lng],
#         radius=5,
       
#         color='#027afa',
#         fill=True,
#         popup= folium.Popup(name, max_width="100"),
#         fill_color='#027afa',
#         fill_opacity=0.7,
#         parse_html=False).add_to(map_th)
    
# for lat, lng, name in zip(#df_test['Latitude'],df_test['Longitude']):
#         df_6['lat'].astype(float), 
#         df_6['lng'].astype(float),
#         df_6['name'] +", " + df_6['type']): 
   
#     folium.CircleMarker(
#         [lat, lng],
#         radius=5,
       
#         color='#9b02fa',
#         fill=True,
#         popup= folium.Popup(name, max_width="100"),
#         fill_color='#9b02fa',
#         fill_opacity=0.7,
#         parse_html=False).add_to(map_th)
    


# # # call to render Folium map in Streamlit
# st_data = st_folium(map_th, width=725)


import folium
from streamlit_folium import st_folium
import pandas as pd
import streamlit as st

df = pd.read_csv('community.csv')
# _1 = st.checkbox('ชุมชนแออัด')
# _2 = st.checkbox('ชุมชนชานเมือง')
# _3 = st.checkbox('ชุมชนหมู่บ้านจัดสรร')
# _4 = st.checkbox('เคหะชุมชน')
# _5 = st.checkbox('ชุมชนเมือง')
# _6 = st.checkbox('ชุมชนอาคารสูง')

map_th1 = folium.Map(location=[13.756331, 100.501762], tiles="Stamen Toner", zoom_start=11)
for lat, lng, name in zip(df['lat'].astype(float), df['lng'].astype(float), df['name'] + "\n(" + df['type'] + ")"):
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
map1 = st_folium(map_th1, width=725, returned_objects=[])

map_th2 = folium.Map(location=[13.756331, 100.501762], tiles="Stamen Toner", zoom_start=11)
for lat, lng, name in zip(df['lat'].astype(float), df['lng'].astype(float), df['name'] + "\n(" + df['type'] + ")"):
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
map2 = st_folium(map_th2, width=725, returned_objects=[])

map_th3 = folium.Map(location=[13.756331, 100.501762], tiles="Stamen Toner", zoom_start=11)
for lat, lng, name in zip(df['lat'].astype(float), df['lng'].astype(float), df['name'] + "\n(" + df['type'] + ")"):
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
map3 = st_folium(map_th3, width=725, returned_objects=[])

map_th4 = folium.Map(location=[13.756331, 100.501762], tiles="Stamen Toner", zoom_start=11)
for lat, lng, name in zip(df['lat'].astype(float), df['lng'].astype(float), df['name'] + "\n(" + df['type'] + ")"):
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
map4 = st_folium(map_th4, width=725, returned_objects=[])

map_th5 = folium.Map(location=[13.756331, 100.501762], tiles="Stamen Toner", zoom_start=11)
for lat, lng, name in zip(df['lat'].astype(float), df['lng'].astype(float), df['name'] + "\n(" + df['type'] + ")"):
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
map5 = st_folium(map_th5, width=725, returned_objects=[])




option = st.selectbox(
    'Select community type',
    ('ชุมชนแออัด', 'ชุมชนชานเมือง', 'ชุมชนหมู่บ้านจัดสรร','เคหะชุมชน','ชุมชนเมือง'))


if option == 'ชุมชนแออัด':
    # df = df[df['type'] == 'ชุมชนแออัด']
    map1
if option == 'ชุมชนเมือง':
    # df = df[df['type'] == 'ชุมชนชานเมือง']
    map2
if option == 'ชุมชนหมู่บ้านจัดสรร':
    # df = df[df['type'] == 'ชุมชนหมู่บ้านจัดสรร']
    map3
if option == 'เคหะชุมชน':
    # df = df[df['type'] == 'เคหะชุมชน']
    map4
if option == 'ชุมชนเมือง':
    # df = df[df['type'] == 'ชุมชนเมือง']
    map5




# df_1 = df[df['type'] == 'ชุมชนแออัด']
# df_2 = df[df['type'] == 'ชุมชนชานเมือง']
# df_3 = df[df['type'] == 'ชุมชนหมู่บ้านจัดสรร']
# df_4 = df[df['type'] == 'เคหะชุมชน']
# df_5 = df[df['type'] == 'ชุมชนเมือง']
# df_6 = df[df['type'] == 'ชุมชนอาคารสูง']

# map_th = folium.Map(location=[13.756331, 100.501762], tiles="Stamen Toner", zoom_start=12)

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
# st_folium(map_th, width=725, returned_objects=[])
