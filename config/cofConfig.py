# -*- coding: utf-8 -*-

import config.cofConfigCapacities
import config.cofConfigPotions
import config.cofConfigSpells
import config.cofConfigMagicWands
import config.cofConfigWeapons
import config.cofConfigArmors
import config.cofConfigRobes
import config.cofConfigBracers
import config.cofConfigRings
import config.cofConfigCloaks
import config.cofConfigShields
import config.cofConfigMounts
import config.cofConfigChars
import config.cofConfigMaterials
import config.cofConfigInns
import config.cofConfigRealEstates
import config.cofConfigHelmets
import config.cofConfigBoots
import config.cofConfigGloves
import config.cofConfigBelts
import cof.properties

config = {
    'global': {
        'path': {
            'root': './',
            'data': 'data',
            'image': 'assets'
        },
        'cost': {
            'bullets': 10,
            'spells': 50,
            'potions': 50,
            'quality': 50,
            'magical': 2000,
            'silver': 100,
            'cold-iron': 100,
            'durium': 100,
            'dalberath': 200,
            'mythral': 500,
            'lothar': 500,
            'adamantium': 1000,
            'sombracier': 5000,
            'laenk': {
                'short_weapons': 100,
                '1-hand': 200,
                '2-hands': 300,
            },
            'xylene': 300,
            'phospharium': 500,
            'hybberium': 500,
            'naesk': 100,
            'krontaar': 300,
            'unit': 'pa'
        },
        'unique-flavors': ['quality', 'quality-twemby', 'silver', 'cold-iron', 'durium', 'dalberath', 'mythral',
                           'lothar', 'adamantium', 'sombracier', 'laenk', 'xylene', 'phospharium', 'hybberium'],

    },
    'gui': {
        'area': {
            'village': {
                'name': 'Village',
                'people': 500,
                'max-cost': cof.properties.Cost(value=20, unit='pa').iso()
            },
            'borough': {
                'name': 'Bourg',
                'people': 2000,
                'max-cost': cof.properties.Cost(value=200, unit='pa').iso()
            },
            'town': {
                'name': 'Ville',
                'people': 8000,
                'max-cost': cof.properties.Cost(value=1000, unit='pa').iso()
            },
            'city': {
                'name': 'Cité',
                'people': 30000,
                'max-cost': cof.properties.Cost(value=3000, unit='pa').iso()
            },
            'megalopolis': {
                'name': 'Mégapole',
                'people': 100000,
                'max-cost': cof.properties.Cost(value=5000, unit='pa').iso()
            },
        }
    },
    'Agglomérations': {
        'Village': {
            'Habitants': 500,
            'Prix maximum': cof.properties.Cost(value=20, unit='pa')
        },
        'Bourg': {
            'Habitants': 2000,
            'Prix maximum': cof.properties.Cost(value=200, unit='pa')
        },
        'Ville': {
            'Habitants': 8000,
            'Prix maximum': cof.properties.Cost(value=1000, unit='pa')
        },
        'Cité': {
            'Habitants': 30000,
            'Prix maximum': cof.properties.Cost(value=3000, unit='pa')
        },
        'Mégapole': {
            'Habitants': 100000,
            'Prix maximum': cof.properties.Cost(value=5000, unit='pa')
        }
    },
    'ui': {
        'itype': {'name': 'Type', 'style': {'white-space': 'nowrap', 'border': '1px solid #ddd',
                                            'padding': '1px 1px 1px 1px'}},
        'ticon': {'name': 'Type', 'style': {'border': '1px solid #ddd', 'padding': '1 1 1 1'}},
        'name': {'name': 'Nom', 'style': {'white-space': 'nowrap', 'border': '1px solid #ddd',
                                          'padding': '1px 1px 1px 1px'}},
        'count': {'name': 'Nombre', 'style': {'white-space': 'nowrap', 'border': '1px solid #ddd', 'width': '55px',
                                              'padding': '1px 1px 1px 1px'}},
        'short_description': {'name': 'Description courte', 'style': {'border': '1px solid #ddd',
                                                                      'padding': '1px 1px 1px 1px'}},
        'full_description': {'name': 'Description complète', 'style': {'border': '1px solid #ddd',
                                                                       'padding': '1px 1px 1px 1px'}},
        'cost': {'name': 'Prix', 'style': {'white-space': 'nowrap', 'text-align': 'right', 'border': '1px solid #ddd',
                                           'padding': '1px 1px 5px 1px', 'width': '60px'}},
        'total_per_item': {'name': 'Total', 'style': {'white-space': 'nowrap', 'text-align': 'right',
                                                      'border': '1px solid #ddd',  'padding': '1px 1px 5px 1px',
                                                      'width': '60px'}},
        'weight': {'name': 'Poids', 'style': {'white-space': 'nowrap', 'border': '1px solid #ddd'}}
    },
    'Capacity': "capacities",
    'capacities': config.cofConfigCapacities.capacities,
    'Potion': "potions",
    'potions': config.cofConfigPotions.potions,
    "Spell": "spells",
    'spells': config.cofConfigSpells.spells,
    "MagicalWand": "magicwands",
    'magicwands': config.cofConfigMagicWands.magicwands,
    "Weapon": "weapons",
    'weapons': config.cofConfigWeapons.weapons,
    "Shield": 'shields',
    'shields': config.cofConfigShields.shields,
    "Armor": 'armors',
    'armors': config.cofConfigArmors.armors,
    "Robe": "robes",
    'robes': config.cofConfigRobes.robes,
    "Bracer": "bracelets",
    'bracers': config.cofConfigBracers.bracers,
    "Ring": "rings",
    'rings': config.cofConfigRings.rings,
    "Cloak": "cloaks",
    'cloaks': config.cofConfigCloaks.cloaks,
    "Mount": "mounts",
    'mounts': config.cofConfigMounts.mounts,
    "Char": "chars",
    'chars': config.cofConfigChars.chars,
    "Material": "materials",
    'materials': config.cofConfigMaterials.materials,
    "Inn": "inns",
    'inns': config.cofConfigInns.inns,
    "RealEstate": "realestates",
    'realestates': config.cofConfigRealEstates.realestates,
    "Helmet": "helmets",
    'helmets': config.cofConfigHelmets.helmets,
    "Boots": "boots",
    'boots': config.cofConfigBoots.boots,
    "Gloves": "gloves",
    'gloves': config.cofConfigGloves.gloves,
    "Belt": "belts",
    'belts': config.cofConfigBelts.belts,
}
