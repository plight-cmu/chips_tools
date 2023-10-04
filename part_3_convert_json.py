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
    new_level = CCLevel()
    new_level_pack = CCLevelPack()
    new_field3 = CCMapTitleField(" ")
    new_field6 = CCEncodedPasswordField("0000")
    new_field7 = CCMapHintField(" ")
    new_field8 = CCMonsterMovementField(" ")
    
    for lv in cclv_json_data:
        
        new_level.level_number = json_data[lv]["Level"]
        new_level.time = json_data[lv]["Time limit"]
        new_level.num_chips = json_data[lv]["Chip number"]
        new_level.upper_layer = json_data[lv]["Upper layer"]
        new_level.lower_layer = json_data[lv]["Lower layer"]
        
        new_field3.title = json_data[lv]["Map Title Field (type=3)"]
        new_field6.password = json_data[lv]["Encoded Password Field (type=6)"]
        new_field7.hint = json_data[lv]["Map Hint Field (type=7)"]
        new_field8.monsters = json_data[lv]["Moving Objects Field (type=10)"]
        
        new_level.optional_fields.append(new_field3)
        new_level.optional_fields.append(new_field6)
        new_level.optional_fields.append(new_field7)

        new_level_pack.add_level(new_level)

    return new_level_pack
    

input_json_file = "data/minkyuns_cc1.json"

with open(input_json_file, "r") as reader:
    cclv_json_data = json.load(reader)

new_level_pack = make_CClvPack_from_json(cclv_json_data)
    
print(new_level_pack)

#Save converted data to DAT file
cc_dat_utils.write_cc_level_pack_to_dat(new_level_pack, "minkyuns_cc1")
