import pandas as pd
import folium
import urllib.request, json
import requests

loc = [36.038, 127.488] #금산구 위도 경도

# 맵 , 마커 생성
m = folium.Map(location=loc, zoom_start=10)   

folium.Marker(
    location=loc,
    tooltip="금산군",
    popup="금산군",
    icon=folium.Icon(icon="star"),
).add_to(m)

# 한국 위치 json 오버레이 추가
m_json = './location.json'.json()

folium.GeoJson(m_json, name="Geumsan-gun").add_to(m)
folium.LayerControl().add_to(m)


# 저장
m.save('map.html')