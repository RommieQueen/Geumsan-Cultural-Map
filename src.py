import pandas as pd
import folium
import urllib.request, json
import requests

df = pd.read_csv('./data.csv')

loc = [36.16260, 127.4619] #금산구 위도 경도

# 맵 , 마커 생성
m = folium.Map(location=loc, zoom_start=10)   

folium.Marker(
    location=loc,
    tooltip="금산군",
    popup="금산군",
    icon=folium.Icon(icon="star"),
).add_to(m)

# 금산군 오버레이



# 금산군 문화재 위치 추가

for i in range(len(df.index)):
    folium.Marker(
        location= [ df['위도'][i], df['경도'][i] ],
        tooltip = df['문화재명'][i],
        popup= df['문화재명'][i],
        icon=folium.Icon(icon="클라우드")
    ).add_to(m)


# 저장
m.save('map.html')