import requests

# number_id = 379
# url = f"https://akabab.github.io/superhero-api/api/powerstats/{number_id}.json"
list_superhero = ['Hulk']

resp = requests.get(url).json()
print(resp)