import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
COUNTRIES_FILE = os.path.join(BASE_DIR, "countries.json")

def load_countries():
    """ Mamlakatlar ma'lumotlarini JSON fayldan yuklash """
    with open(COUNTRIES_FILE, "r", encoding="utf-8") as file:
        return json.load(file)
