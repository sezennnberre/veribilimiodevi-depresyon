# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 02:11:30 2023

@author: HP
"""

import pandas as pd
import numpy as np
import matplotlib as plt 
from pandas.api.types import is_numeric_dtype


depresyon = pd.read_csv("data\scores.csv")

depresyon.dropna(inplace= True)

#klasör içindeki csv leri nasıl okuyacağımı bilemedim. 

#okusam bile nasıl sorgulama yapıcağımı ve neyi sorgulamam gerektiğini anlamadım.