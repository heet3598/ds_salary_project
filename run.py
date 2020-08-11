# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 15:05:29 2020

@author: heet3
"""


import glassdoor_scraper as gs
import pandas as pd

path = 'C:/Users/heet3/webdrivers/chromedriver'

df = gs.get_jobs('data science', 15,False,path, 15)
