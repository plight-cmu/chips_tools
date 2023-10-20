from cc_classes import CCLevel
from cc_classes import CCLevelPack
from cc_classes import CCMapTitleField
from cc_classes import CCEncodedPasswordField
from cc_classes import CCMapHintField
from cc_classes import CCMonsterMovementField
import cc_dat_utils

import json

#Part 3
#Load your custom JSON file
#Convert JSON data to CCLevelPack


def make_CClvPack_from_json( json_data ):
   
    game_level_pack = CCLevelPack()

    for lv in cclv_json_data["levels"]:
        game_level = CCLevel()
        game_field3 = CCMapTitleField(" ")
        game_field6 = CCEncodedPasswordField("0000")
        game_field7 = CCMapHintField(" ")
        game_field8 = CCMonsterMovementField(" ")
        
        game_level.level_number = lv["level_number"]
        game_level.time = lv["time"]
        game_level.num_chips = lv["number_of_chips"]
        game_level.upper_layer = lv["upper_layer"]
        game_level.lower_layer = lv["lower_layer"]
        
        game_field3.title = lv["title"]
        game_field6.password = lv["password"]
        game_field7.hint = lv["hint"]
        game_field8.monsters = lv["moving_objects"]
        
        game_level.optional_fields.append(game_field3)
        game_level.optional_fields.append(game_field6)
        game_level.optional_fields.append(game_field7)

        game_level_pack.add_level(game_level)

    return game_level_pack
    

input_json_file = "data/minkyuns_cc1.json"

with open(input_json_file, "r") as reader:
    cclv_json_data = json.load(reader)

new_level_pack = make_CClvPack_from_json(cclv_json_data)
    
print(new_level_pack)

#Save converted data to DAT file
cc_dat_utils.write_cc_level_pack_to_dat(new_level_pack, "data/minkyuns_cc1.dat")
