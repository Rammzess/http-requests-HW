import requests

TOKEN = "2619421814940190"
heroes_data = {}

class SuperHero():
    def get_intelligence(name):
        url = f"https://superheroapi.com/api/{TOKEN}/search/{name}"
        hero_id = requests.get(url, timeout=5)
        intelligence = hero_id.json()['results'][0]['powerstats']['intelligence']
        return intelligence

    def the_smartest_hero(heroes_data):
        max_int = max(heroes_data.values())
        final_dict = {key:value for key, value in heroes_data.items() if value == max_int}
        final_list = list(final_dict.items())    
        return f'The smartest hero is {final_list[0][0]}: {final_list[0][1]} points'

    heroes_data['Hulk'] = int(get_intelligence('Hulk'))
    heroes_data['Captain America'] = int(get_intelligence('Captain America'))
    heroes_data['Thanos'] = int(get_intelligence('Thanos'))

    print(the_smartest_hero(heroes_data))



