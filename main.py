# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 13:43:42 2018

@author: Chintan Maniyar
"""
'''
LocationFetcher Version: 2, Revision: 1
'''
import streaming, geocode, maps

if __name__ == "__main__":
    
    #fetch tweets and validate them, info prints the tweet information on the console
    streaming.fetchTweets(info=True)
    
    #generate geocodes for map markers
    geocode.generateGeocodes()
    
    #pull up the map
    maps.showMap()
    
    input()