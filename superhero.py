import requests

url = 'https://superheroapi.com/api/2619421814940190/search/'
def find_superint_hero(hero_list):
    for hero in hero_list:
        res = requests.get(url + hero['name'])
        hero['intelligence'] = int(res.json()['results'][0]['powerstats']['intelligence'])
    super_int = max(hero_list, key = lambda k: k['intelligence'])
    message = f'{super_int["name"]} самый сильный супергерой! Его мощность составляет - {super_int["intelligence"]}'
    return message

print(find_superint_hero([{'name' : 'Hulk'}, {'name' : 'Captain America'}, {'name' : 'Thanos'}]))