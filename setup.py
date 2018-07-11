# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 22:09:22 2018

@author: Chintan Maniyar
"""

import sys
from cx_Freeze import Executable, setup

build_exe_options = {"packages":['tweepy','datetime','dateutil', 'webbrowser', 'csv', 'pandas', 'requests', 'idna.idnadata', 'idna', 'numpy'], "excludes":['tkinter']}

if sys.platform == "win32":
    base = "Console"
    pass

setup( name = "LocationFetcher",
      version = "2.1",
      description = "Tweet Geolocator",
      options = {"build_exe": build_exe_options},
      executables = {Executable("main.py", base=None)})