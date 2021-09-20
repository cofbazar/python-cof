# -*- coding: utf-8 -*-

import cof.properties

chars = {
    'ids': ['carriole', 'chariot'],
    'addons': {
        'carriole': {
            'full_description': "Un véhicule à deux roues, tiré par des chevaux ou des boeufs et couvert ou non "
                                "d'une bâche. La carriole sert généralement au transport des personnes.",
            'short_description': "Un véhicule à deux roues, tiré par des chevaux ou des boeufs servant au transport "
                                 "des personnes.",
            'weight': cof.properties.Weight(value=100.0, unit='Kg')
        },
        'chariot': {
            'full_description': "Un véhicule à 4 roues permettant de transporter des personnes ou du matériel. "
                                "Le chariot est tiré le plus souvent par des boeufs et peut être couvert par une "
                                "bâche pour protéger la cargaison.",
            'short_description': "Un véhicule à 4 roues permettant de transporter du matériel.",
            'weight': cof.properties.Weight(value=200.0, unit='Kg')
        }
    }
}
