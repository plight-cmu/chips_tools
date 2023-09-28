import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()
        
    ### Begin Add Code Here ###
    #Loop through the json_data
    
    for data in json_data:
        new_game = test_data.Game(json_data[data]["title"], json_data[data]["Year"], json_data[data]["platform"])
        test_data.GameLibrary.add_game(new_game)
        #Create a new Game object from the json_data by reading
        #  title
        #  year
        #  platform (which requires reading name and launch_year)
        #Add that Game object to the game_library
    ### End Add Code Here ###

        return game_library

#Part 2
input_json_file = "data/test_data.json"

with open(input_json_file, "r") as reader:
    library_json_data = json.load(reader)

new_library = make_game_library_from_json(library_json_data)
    
print(new_library)



### Begin Add Code Here ###
#Open the file specified by input_json_file
#Use the json module to load the data from the file
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
#Print out the resulting GameLibrary data using print()
### End Add Code Here ###


