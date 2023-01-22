## This script removes newlines and spaces at the start of the text. It also removes chapter and verse numbers from the start of each line if they exist.
import json
import re

# load the json file into a variable
with open("data/corrected_translation.json", "r") as json_file:
    data = json.load(json_file)

# iterate through the array of objects
for obj in data:
    # check if the lang is english
    if obj["lang"] == "english":
        # remove newlines and spaces at the start of the text
        obj["description"] = obj["description"].lstrip("\n ")
        # remove chapter and verse numbers
        obj["description"] = re.sub(r"(\d+\.\d+|।।\d+\.\d+।।)", "", obj["description"])
        obj["description"] = obj["description"].lstrip(". ").lstrip("")

# save the modified data to a new json file
with open("data/corrected_translation_cleaned.json", "w", encoding="utf8") as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)
