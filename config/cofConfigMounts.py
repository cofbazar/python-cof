# -*- coding: utf-8 -*-

import cof.properties

mounts = {
    'ids': ['cheval-de-guerre-leger', 'cheval-de-selle', 'mule-ou-ane', 'poney'],
    'split': {
        'mule-ou-ane': {
            'mule': {
                'name': 'Mule',
                "short_description": "Une mule.",
                "full_description": "Une mule."
            },
            'ane': {
                'name': 'Âne',
                "short_description": "Un âne.",
                "full_description": "Un âne."
            }
        }
    },
    'addons': {
        'cheval-de-guerre-leger': {
            'full_description': "Un cheval spécialement dressé pour les combats.",
            'short_description': "Un cheval spécialement dressé pour les combats.",
            'weight': cof.properties.Weight(value=600.0, unit='Kg')
        },
        'cheval-de-selle': {
            'full_description': "Un cheval dressé pour être monté.",
            'short_description': "Un cheval dressé pour être monté.",
            'weight': cof.properties.Weight(value=500.0, unit='Kg')
        },
        'poney': {
            'full_description': "Un cheval de petite taille avec une crinière épaisse, une queue et un pelage "
                                "fournis.",
            'short_description': "Un cheval de petite taille.",
            'weight': cof.properties.Weight(value=400.0, unit='Kg')
        }
    }
}
