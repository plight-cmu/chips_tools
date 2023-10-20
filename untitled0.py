# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 21:05:51 2023

@author: minkyuns
"""

import test_data
import json



#Part 2
input_json_file = "data/test_data.json"

with open(input_json_file, "r") as reader:
    library_json_data = json.load(reader)
    
    for data in library_json_data:
        print(data)
        
    print(library_json_data)
    
print("\n")

print(library_json_data['game1']['title'], library_json_data['game1']['year'])


new_library = test_data.GameLibrary()

