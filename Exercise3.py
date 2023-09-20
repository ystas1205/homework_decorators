import inspect
import requests
from Exercise1 import function


@function
def get_request():
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url=url)
    list_heroes = []
    for i in response.json():
        dict_h = {i['name']: i['powerstats']['intelligence']}
        for name, intelligence in dict_h.items():
            if name == 'Hulk' or name == 'Captain America' or name == 'Thanos':
                dict_heroes = {name: intelligence}
                for n_i in dict_heroes.items():
                    list_heroes.append(n_i)
    list_heroes.sort(key=lambda x: (x[1]), reverse=True)
    return (f'Самым умным героем является {list_heroes[0][0]}',
            inspect.getargvalues(inspect.currentframe().f_back))


if __name__ == "__main__":
    get_request()
