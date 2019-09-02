# Marissa Salcido 86569875 salcidom

import mapquest_api

class directions:
    def generate_output(self, json_dict: dict) -> str:
        '''searches for the narrative of directions from the json dictionary
            and prints each narrative'''
        print('\nDIRECTIONS')
        for item in json_dict['route']['legs']:
            for item1 in item['maneuvers']:
                print(item1['narrative'])

class distance:
    def generate_output(self, json_dict: dict) -> int:
        '''searches for the total distance from the json dictionary and prints
            the result in miles'''
        print('\nTOTAL DISTANCE')
        distance = round(json_dict['route']['distance'])
        print(distance, 'miles')

class time:
    def generate_output(self, json_dict: dict) -> int:
        '''searches for the total time from the json dictionary and prints
            the result in minutes'''
        print('\nTOTAL TIME')
        time = round((json_dict['route']['time']) / 60)
        print(time, 'minutes')

class latitude_longitude:
    def generate_output(self, json_dict: dict) -> str:
        '''searches for the lat/long pairs in the json dictionary and prints the pair
            with a cardinal direction depending on the value of each lat/long'''
        print('\nLATLONGS')
        for latLng in json_dict['route']['locations']:
            latitude = latLng['latLng']['lat']
            longitude = latLng['latLng']['lng']
            if latitude >= 0:
                print('{0:.2f}'.format(latitude) + 'N', end = ' ')
            else:
                print('{0:.2f}'.format(abs(latitude)) + 'S', end = ' ')
            if longitude >= 0:
                print('{0:.2f}'.format(longitude) + 'E')
            else:
                print('{0:.2f}'.format(abs(longitude)) + 'W')

class elevation:
    def generate_output(self, json_dict: dict) -> int:
        '''searches for the lat/long of each location in the json response,
            and searches for the heights from the mapquest API for elevations'''
        print('\nELEVATION')
        lat_long_list = []
        for latLng in json_dict['route']['locations']:
            latitude = latLng['latLng']['lat']
            longitude = latLng['latLng']['lng']
            lat_lng_pair = str(latitude) + ',' + str(longitude)
            json_elevation_dict = mapquest_api.search_elevation(lat_lng_pair)
            for height in json_elevation_dict['elevationProfile']:
                print(round(height['height']))

def run_commands(json_dict: dict, command_new_objects: list) -> None:
    '''calls the same method for each object in the list: command_new_objects, generating a different output
        depending on which class the object is'''
    for obj in command_new_objects:
        obj.generate_output(json_dict)

def handle_commands(commands: list) -> list:
    '''based on which command the user inputs, appends an object of a defined class to an empty list
        and returns the list'''
    command_new_objects = []
    for command in commands:
        if command == 'STEPS':
            command_new_objects.append(directions())
        elif command == 'TOTALDISTANCE':
            command_new_objects.append(distance())
        elif command == 'TOTALTIME':
            command_new_objects.append(time())
        elif command == 'LATLONG':
            command_new_objects.append(latitude_longitude())
        elif command == 'ELEVATION':
            command_new_objects.append(elevation())
        
    return command_new_objects
        
    
