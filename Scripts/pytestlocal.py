'''
Created on Apr 2, 2019

@author: DELL
'''

import requests
import pytest
import json

@pytest.fixture
def scrape(url):
    html=requests.get(url).text
    return html