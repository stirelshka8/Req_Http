import requests

def search_id_hero():
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    return_data_hero = requests.get(url)
    dict_return_data_hero = {}
    dict_return_data_hero = return_data_hero.json()
    list_hero = ['Hulk', 'Captain America', 'Thanos']
    list_id = {}

    for name_hero in list_hero:
        for data_return_data in dict_return_data_hero:
            for data_return_key, data_return_val in data_return_data.items():
                if data_return_val == name_hero:
                    list_id[name_hero] = data_return_data['id']

    return list_id

def smart_hero():
    list_id = search_id_hero()
    dict_hero = {}
    for list_id_key, list_id_val in list_id.items():
        url_id_hero = f'https://akabab.github.io/superhero-api/api/powerstats/{list_id_val}.json'
        data_return = requests.get(url_id_hero).json()
        dict_hero[list_id_key] = data_return['intelligence']\
    
    return max(dict_hero)