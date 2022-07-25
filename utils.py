import requests


def calculate_multiplier(attack_type, pokemon_types):
    response = requests.get("https://pokeapi.co/api/v2/type/"+attack_type)
    if response.ok:
        response_data = response.json()
        multiplier = 1
        for i in pokemon_types:
            damage_relations = response_data['damage_relations']
            if any(d['name'] == i for d in damage_relations['no_damage_to']):
                multiplier *= 0
                break
            elif any(d['name'] == i for d in damage_relations['double_damage_to']):
                multiplier *= 2
            elif any(d['name'] == i for d in damage_relations['half_damage_to']):
                multiplier *= 0.5
        return(str(multiplier)+'x')
    else:
        return('Error')
