import requests

API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en_US/"

def get_definition(word):
    response = requests.get(API_URL + word)
    if response.status_code == 200:
        data = response.json()
        if data:
            definition =  data[0]['meanings'][0]['definitions'][0]['definition']
    return None

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

if __name__ == "__main__":
    definition = get_definition("hello")
    print(definition)
    synonyms = get_synonyms("hello")
    print(synonyms)
    antonyms = get_antonyms("hello")
    print(antonyms)