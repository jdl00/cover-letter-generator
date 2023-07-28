import os

from json import dumps
from uuid import uuid4


SUFFIX_LENGTH = 48
VALID_PREFIX = 'sk'
DICT_KEY = "openai_api_key"
CONST_KEY_PATH = os.path.abspath(os.path.join("resources", "key"))


api_key = input("Please Enter you Open AI key.\n")

# Basic validation check of the key
split_api_key = api_key.split('-')
if split_api_key[0] != VALID_PREFIX:
    print("Error: Invalid API key prefix.")
elif len(split_api_key[1]) != SUFFIX_LENGTH:
    print("Error: Invalid suffix length.")

key_json_obj = dumps({DICT_KEY: api_key}, indent=4)

file_name_path = os.path.join(CONST_KEY_PATH,
                              f"{str(uuid4())}.json")

with open(file_name_path, "w") as f:
    f.write(key_json_obj)
