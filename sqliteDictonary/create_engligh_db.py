from sqlite_database import SqliteDatabase
import requests

API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en_US/"

def get_definition(word):
    response = requests.get(API_URL + word)
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]['meanings'][0]['definitions'][0]['definition']
    return definition

def get_synonyms(word):
    response = requests.get(API_URL + word)
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]['meanings'][0]['definitions'][0]['synonyms']
    return None

def get_antonyms(word):
    response = requests.get(API_URL + word)
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]['meanings'][0]['definitions'][0]['antonyms']
    return None

