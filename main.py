import requests

class SuperHero_ID:
    def __init__ (self):
        self.list_superhero = ["Hulk", "Captain America", "Thanos"]

    def search(self, url = "https://akabab.github.io/superhero-api/api/all.json"):
        self.url = url
        self.data_hero  = requests.get(self.url).json()
        return self.data_hero
            
    




# TODO: Код ниже! Выдает стату. Осталось написать код поиска по ID и дело в шляпе
# number_id = 379
# url = f"https://akabab.github.io/superhero-api/api/powerstats/{number_id}.json"

supher = SuperHero_ID()

print(supher.search())