# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 10:39:17 2018

@author: Chintan Maniyar
"""

import requests, csv
import pandas as pd

GEOCODE_URL = 'https://maps.googleapis.com/maps/api/geocode'
df = pd.read_csv('prod.csv')
api_key = "AIzaSyBSRBZ5TxNXO_7HnMoEK0DrhfDWJdiG-gk"
coordinates = {'lat':[], 'lng':[]}

def generateGeocodes():
    for address in df['place']:
        if address != "00":
            print(address)
            api_response = requests.get(GEOCODE_URL + '/json?address={0}&key={1}'.format(address, api_key))
            api_response_dict = api_response.json()
        
        if api_response_dict['status'] == 'OK':
            print(api_response_dict['results'][0]['geometry']['location']['lat'])
            print(api_response_dict['results'][0]['geometry']['location']['lng'])
            coordinates['lat'].append(api_response_dict['results'][0]['geometry']['location']['lat'])
            coordinates['lng'].append(api_response_dict['results'][0]['geometry']['location']['lng'])

    try:
        with open('coordinates.csv', 'w', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(coordinates.keys())
            writer.writerows(zip(*coordinates.values()))
    except IOError as e:
        print(e)