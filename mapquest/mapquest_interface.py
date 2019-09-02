# Marisa Salcido 86569875 salcidom
# Project 3

import mapquest_api
import mapquest_output_response

def location_count() -> None:
    '''allows user to input the number of locations'''
    while True:
        try:
            user_int = int(input().strip())
            if user_int < 2:
                print('Invalid input. Enter a number greater than or equal to 2.')
            else:
                return user_int
        except:
            print('Invalid input. Enter a number greater than or equal to 2.')
            
def store_location(user_int: int) -> list:
    '''allows user to input locations n number of times and returns a location list'''
    locations = []
    for input_count in range(user_int):
        new_location = input()
        locations.append(new_location)
    return locations

def output_count() -> int:
    '''allows user to input number of lines of output to produce'''
    while True:
        try:
            user_int = int(input().strip())
            if user_int > 5:
                print('Invalid input. Enter a number less than or equal to 5.')
            return user_int
        except:
            print('Invalid input. Enter a number greater than or equal to 5.')
             
def store_command(user_int: int) -> list:
    '''allows user to input commands on n number of lines and returns command list'''
    commands = []
    for input_count in range(user_int):
        new_command = input()
        commands.append(new_command)
    return commands
    
def results() -> None:
    '''starts the user input request and generates an output based on the locations and commands'''
    locations = store_location(location_count())
    try:
        json_dict = mapquest_api.convert_json(mapquest_api.create_url(locations))
        
        if json_dict['info']['statuscode'] != 0:
            print('\nNO ROUTE FOUND')
            quit()
    except:
        print('\nMAPQUEST ERROR')
        quit()
                                              
    converted_commands = mapquest_output_response.handle_commands(store_command(output_count()))
    mapquest_output_response.run_commands(json_dict, converted_commands)
    print('\nDirections Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')
        
if __name__ == '__main__':
    results()
            
        
