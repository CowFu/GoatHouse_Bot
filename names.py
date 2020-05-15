import random
import json


def name_generator(type):
    names = json.load(open('ref/names.json'))
    if type.lower() == 'help':
        species = str(list(names.keys()))
        return 'valid namegens are {}'.format(species.strip("[]"))
    if type in names:
        first_names = names[type.lower()]['first']
        last_names = names[type.lower()]['last']
    else:
        return f'{type} is not a valid namegen'

    return str(first_names[random.randint(0, len(first_names)-1)]) + \
        ' ' + str(last_names[random.randint(0, len(last_names)-1)])
