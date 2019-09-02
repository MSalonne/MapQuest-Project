# Marissa Salcido 86569875 salcidom
# Project 3
import json
import urllib.parse
import urllib.request

APIKey = 'APJbjywSbr9c1OMrnQGV75mzr61rd5MG'
URL = 'http://open.mapquestapi.com/directions/v2/route?'
URL_ELEVATION = 'http://open.mapquestapi.com/elevation/v1/profile?'

def create_url(locations: list) -> str:
    '''changes the user input's locations to a URL represented as a string'''
    query = [('key',APIKey), ('from',locations[0])]
    for location in locations[1:]:
        query.append(('to',location))
    query = urllib.parse.urlencode(query)
    return(URL + query)

def search_elevation(latitude_longitude: str) -> str:
    '''takes the locations' lat/long and returns the elevations'''
    query = urllib.parse.urlencode([('key', APIKey), ('unit','f'),('latLngCollection',latitude_longitude)])
    return convert_json(URL_ELEVATION + query)
    
def convert_json(url: str) -> dict:
    '''sends url to the api and converts the response to a dictionary'''
    response = None
    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)
    
    finally:
        if response != None:
            response.close()
    
