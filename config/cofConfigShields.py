# -*- coding: utf-8 -*-
from cof.properties import *

shields = {
    'cost': lambda item: Cost(
        value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
        unit=config.cofConfig.config['global']['cost']['unit']).iso(),
    'ids': ['petit-bouclier', 'grand-bouclier'],
#    'others': {
#        'ring-of-protection': {
#        },
#        'cloak-of-protection': {
#        }
#    },
    'addons': {
        'petit-bouclier': {
           'base_item': 'petit-bouclier',
           'category': 'Standard',
           'hands': 1,
           'full_description': "Un petit bouclier en métal qui occupe une main. Très maniable, il n'offre "
                               "cependant que très peu de protection contre les projectiles. Il procure un "
                               "bonus de DEF +1.",
           'short_description': "Un petit bouclier très maniable en métal qui occupe une main.",
           'weight': Weight(value=2.0, unit='Kg'),
           'defense': [Mod(label="DEF", mtype="+", count=1)],
        },
        'grand-bouclier': {
            'base_item': 'grand-bouclier',
            'category': 'Standard',
            'hands': 1,
            'full_description': "Un grand bouclier en métal qui occupe une main. Ce bouclier offre une bonne "
                                "protection contre les projectiles. Il procure un bonus de DEF +2.",
            'short_description': "Un grand bouclier en métal qui occupe une main.",
            'weight': Weight(value=3.0, unit='Kg'),
            'defense': [Mod(label="DEF", mtype="+", count=2)],
        }
    }
}
