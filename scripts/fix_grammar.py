import os
import openai
from dotenv import load_dotenv
import json

# Load the api_key from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

# Read JSON file
with open('data/translation.json') as json_file:
    data = json.load(json_file)

# Iterate through the array and make OpenAI call for English translations
for i, obj in enumerate(data):
    if obj['lang'] == 'english':
        print("OLD: " + obj['description'])
        prompt = (f"Please fix the grammatical errors in this English translation of Bhagavad Gita. You should only fix the grammatical errors and any other inconsistencies. Do not change the meaning.\n\n{obj['description']}")
        completions = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.1,
        )

        # Update the description with the corrected text
        obj['description'] = completions.choices[0].text
        print("NEW: " + obj['description'] + "\n\n")

# Write the corrected data to a new JSON file
with open('data/corrected_translation.json', 'w', encoding='utf8') as outfile:
    json.dump(data, outfile, ensure_ascii=False, indent=4)

print("Grammatical errors fixed and new JSON file created with corrected translations.")
