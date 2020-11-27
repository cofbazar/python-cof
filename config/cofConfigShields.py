# -*- coding: utf-8 -*-
from cof.properties import *
import config.cofConfig
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
     'flavors': {
        'magical': {
            'magical_levels': [1, 2, 3, 4],
        
            'name': lambda item, magical_level: "{} +{}".format(item.name, magical_level),
            'short_description': lambda item, magical_level: "{} Ce bouclier offre un bonus de DEF "
                                                             "de +{}.".format(item.short_description,
                                                                              magical_level),
            'full_description':
                lambda item, magical_level: "{} Ce bouclier est magique et offre un bonus de DEF de +{}.".format(
                    item.full_description, magical_level),
            'cost': lambda item, magical_level: Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso(),
                    'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='magical', count=magical_level)],
            'defense': lambda item, magical_level: [
                Mod(label=m.label, target=m.target, mtype=m.mtype, die=m.die,
                    count=m.count + magical_level, limitation=m.limitation)
                if m.label == "DEF" else m for m in item.defense],
        },
     },
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
