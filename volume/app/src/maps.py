import dash

import dash_core_components as dcc
import dash_html_components as html

# import main

import plotly.express as px
import pandas as pd
import geocoder
import folium

# geocoder
thokkaido = geocoder.osm('北海道', timeout=5.0)
ttokyo = geocoder.osm('東京都千代田区', timeout=5.0)
tchiba = geocoder.osm('千葉県夷隅郡大多喜町森宮', timeout=5.0)
tkyoto = geocoder.osm('京都市', timeout=5.0)
tnagoya = geocoder.osm('名古屋市', timeout=5.0)
tosaka = geocoder.osm('大阪市', timeout=5.0)

fm = folium.Map(tchiba.latlng, zoom_start=5)
# folium.Marker(ret.latlng).add_to(fm)
folium.vector_layers.PolyLine(
    locations=[thokkaido.latlng, tchiba.latlng],
    color='blue',
    weight=1.2
).add_to(fm)
folium.vector_layers.PolyLine(
    locations=[tchiba.latlng, ttokyo.latlng],
    color='blue',
    weight=2.6
).add_to(fm)
folium.vector_layers.PolyLine(
    locations=[tchiba.latlng, tnagoya.latlng],
    color='blue',
    weight=1
).add_to(fm)
folium.vector_layers.PolyLine(
    locations=[tchiba.latlng, tkyoto.latlng],
    color='blue',
    weight=2.5
).add_to(fm)
folium.vector_layers.PolyLine(
    locations=[tchiba.latlng, tosaka.latlng],
    color='blue',
    weight=2.8
).add_to(fm)
fm.save('folium_jp.html')

layout = html.Div(
    children=[
        html.H1("Hello Dash"),

        html.Div(children='''
            Dash: A web appliation framework for Python.
        '''),

        html.Iframe(
            id="example-map",
            srcDoc=open('folium_jp.html', 'r').read(), width='100%', height="600"
        ),
    ]
)
