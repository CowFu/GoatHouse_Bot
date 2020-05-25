import random
import json


def name_generator(type):
    names = json.load(open('ref/names.json'))
    result = ''
    if type.lower() == 'help':
        species = str(list(names.keys()))
        return 'valid namegens are {}'.format(species.strip("[]"))
    if type in names:
        for key in names[type].keys():
            rand = random.randint(0, len(names[type][key])-1)
            result += names[type][key][rand] + ' '
    else:
        return f'{type} is not a valid namegen'

    return result
