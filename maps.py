# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 11:00:00 2018

@author: Chintan Maniyar
"""
import pandas as pd
import requests, webbrowser

GMAPS_URL = 'https://maps.googleapis.com/maps/api/staticmap'
df = pd.read_csv('coordinates.csv')
def showMap():
    cpairs = ["%s,%s" % (x, y)for x,y in zip(*(df['lat'],df['lng']))]
    preq = requests.PreparedRequest()
    preq.prepare_url(GMAPS_URL, {'size':'1920x720', 'markers':cpairs})
    print(preq.url)
    webbrowser.open(preq.url)