import urllib3
import sys
import json


class Pokemon:
    """
    This class is used to generate pokemon object and store its basic information as well as its raw data from api
    """

    def __init__(self, raw_data):
        self.name = ''
        self.poke_type = []
        self.raw_data = raw_data
        self.name = self.raw_data['forms'][0]['name']

    def set_type(self, poke_type):
        self.poke_type = poke_type


class PokemonType:
    """
    Pokemon type object is created by this class as well as its advantage type and weakness
    """

    def __init__(self, name):
        self.name = name
        type_url = 'http://pokeapi.co/api/v2/type/'
        http = urllib3.PoolManager()
        r = http.request('GET', type_url + self.name)
        raw_data = json.loads(r.data)
        self.half_damage_from = [poke_type['name'] for poke_type in raw_data['damage_relations']['half_damage_from']]
        self.no_damage_from = [poke_type['name'] for poke_type in raw_data['damage_relations']['no_damage_from']]
        self.no_damage_to = [poke_type['name'] for poke_type in raw_data['damage_relations']['no_damage_to']]
        self.half_damage_to = [poke_type['name'] for poke_type in raw_data['damage_relations']['half_damage_to']]
        self.double_damage_from = [poke_type['name'] for poke_type in raw_data['damage_relations']['double_damage_from']]
        self.double_damage_to = [poke_type['name'] for poke_type in raw_data['damage_relations']['double_damage_to']]


class PokeSearch:
    """
    This class includes getting data from rest API, sort type for each pokemon and evaluator based on pokemons
    type and base stat
    """

    def __init__(self):
        self.pokeapi_url = 'http://pokeapi.co/api/v2/pokemon/'

    def get_data(self, argu):
        http = urllib3.PoolManager()
        r = http.request('GET', self.pokeapi_url + argu)
        return json.loads(r.data)

    def get_type(self, data):
        types = []
        for poke_type in data['types']:
            types.append(PokemonType(poke_type['type']['name']))
        return types

    def compare_pokemon_type(self, pokemon1, pokemon2):
        balance_index = 1
        temp_balance_index = 1

        for poke_type1 in pokemon1.poke_type:
            for poke_type2 in pokemon2.poke_type:
                temp_balance_index = 1
                if poke_type2.name in poke_type1.no_damage_from:
                    return pokemon1.name
                if poke_type2.name in poke_type1.no_damage_to:
                    return pokemon2.name
                if poke_type2.name in poke_type1.half_damage_from:
                    temp_balance_index *= 2
                if poke_type2.name in poke_type1.double_damage_to:
                    temp_balance_index *= 2
                if poke_type2.name in poke_type1.half_damage_to:
                    temp_balance_index *= 0.5
                if poke_type2.name in poke_type1.double_damage_from:
                    temp_balance_index *= 0.5

                balance_index *= temp_balance_index

        if balance_index > 1:
            return pokemon1.name
        elif balance_index < 1:
            return pokemon2.name
        else:
            return 0

    def compare_pokemon_score(self, pokemon1, pokemon2):
        pokemon1_score = sum([int(stat['base_stat']) for stat in pokemon1.raw_data['stats']])
        pokemon2_score = sum([int(stat['base_stat']) for stat in pokemon2.raw_data['stats']])
        if pokemon1_score > pokemon2_score:
            return pokemon1.name
        elif pokemon1_score < pokemon2_score:
            return pokemon2.name
        else:
            return 0


def main():
    poke_search = PokeSearch()
    input1 = sys.argv[1]
    input2 = sys.argv[2]

    pokemon1 = Pokemon(poke_search.get_data(input1))
    pokemon2 = Pokemon(poke_search.get_data(input2))

    pokemon1.set_type(poke_search.get_type(pokemon1.raw_data))
    pokemon2.set_type(poke_search.get_type(pokemon2.raw_data))
    res = poke_search.compare_pokemon_type(pokemon1, pokemon2)
    if res != 0:
        print(res)
        return
    else:
        res = poke_search.compare_pokemon_score(pokemon1,pokemon2)
        if res != 0:
            print(res)
            return
        else:
            print(pokemon1.name)
            return


if __name__ == "__main__":
    main()
