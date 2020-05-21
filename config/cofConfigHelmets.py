# -*- coding: utf-8 -*-

from cof.properties import *
import config.cofConfig

helmets = {
    'cost': lambda item: Cost(
        value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
        unit=config.cofConfig.config['global']['cost']['unit']).iso(),
    'others': {
        'leather-helmet': {
            'base_item': 'leather-helmet',
            'category': 'Standard',
            'skill': [
                Mod(label="Test", target="view", count=2, mtype="-"), 
                Mod(label="Test", target="hearing", count=2, mtype="-"),
                Mod(label="Test", target="embuscade", count=2, mtype="-")
                ],
            'defense': [Mod(label="RD", target="rd", count=2, limitation="Seulement contre les critiques")],
            'magical_level': 0,
            'name': "Calotte en cuir",
            'short_description': "Une calotte en cuir qui protègera un peu la tête de l'aventurier et ne "
                                 "diminuera que légèrement sa perception.",
            'full_description': "La calotte en cuir est l'élément indispensable pour compléter une armure de cuir. "
                                "Elle offre une RD de 2 lorsque l'on subit un coup critique. Le port de de ce casque "
                                "inflige une pénalité de -2 a tous les tests de SAG destinés à simuler la perception, "
                                "détecter un bruit ou une créature cachée, échaper à une embuscade, etc.",
            'cost': lambda item: cof.properties.Cost(value=1.0,
                                                     unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'weight': cof.properties.Weight(value=0.5, unit='Kg')
        },
        'camail-helmet': {
            'base_item': 'camail-helmet',
            'category': 'Standard',
            'skill': [
                Mod(label="Test", target="view", count=4, mtype="-"), 
                Mod(label="Test", target="hearing", count=4, mtype="-"),
                Mod(label="Test", target="embuscade", count=4, mtype="-")
                ],
            'defense': [Mod(label="RD", target="rd", count=4, limitation="Seulement contre les critiques")],
            'magical_level': 0,
            'name': "Camail",
            'short_description': "Un camail qui protègera la tête de l'aventurier mais "
                                 "diminuera sa perception.",
            'full_description': "Le camail est l'élément indispensable pour compléter une chemise de maille. "
                                "Il offre une RD de 4 lorsque l'on subit un coup critique. Le port de de ce casque "
                                "inflige une pénalité de -4 a tous les tests de SAG destinés à simuler la perception, "
                                "détecter un bruit ou une créature cachée, échaper à une embuscade, etc.",
            'cost': lambda item: cof.properties.Cost(value=3.0,
                                                     unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'weight': cof.properties.Weight(value=1.0, unit='Kg')
        },
        'maille-helmet': {
            'base_item': 'maille-helmet',
            'category': 'Standard',
            'skill': [
                Mod(label="Test", target="view", count=6, mtype="-"), 
                Mod(label="Test", target="hearing", count=6, mtype="-"),
                Mod(label="Test", target="embuscade", count=6, mtype="-")
                ],
            'defense': [Mod(label="RD", target="rd", count=6, limitation="Seulement contre les critiques")],
            'magical_level': 0,
            'name': "Casque",
            'short_description': "Un casque qui protègera beaucoup la tête de l'aventurier mais "
                                 "diminuera fortement sa perception..",
            'full_description': "Le casque est l'élément indispensable pour compléter une cotte de maille. "
                                "Il offre une RD de 6 lorsque l'on subit un coup critique. Le port de de ce casque "
                                "inflige une pénalité de -6 a tous les tests de SAG destinés à simuler la perception, "
                                "détecter un bruit ou une créature cachée, échaper à une embuscade, etc.",
            'cost': lambda item: cof.properties.Cost(value=5.0,
                                                     unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'weight': cof.properties.Weight(value=1.5, unit='Kg')
        },
        'heavy-helmet': {
            'base_item': 'heavy-helmet',
            'category': 'Standard',
            'skill': [
                Mod(label="Test", target="view", count=8, mtype="-"), 
                Mod(label="Test", target="hearing", count=8, mtype="-"),
                Mod(label="Test", target="embuscade", count=8, mtype="-")
                ],
            'defense': [Mod(label="RD", target="rd", count=8, limitation="Seulement contre les critiques")],
            'magical_level': 0,
            'name': "Heaume",
            'short_description': "Un heaume qui protègera énormément la tête de l'aventurier mais " 
                                 "réduira sa perception quasiment à néant.",
            'full_description': "Le heaume est l'élément indispensable pour compléter une armure de demi-plaques. "
                                "Il offre une RD de 8 lorsque l'on subit un coup critique. Le port de de ce casque "
                                "inflige une pénalité de -8 a tous les tests de SAG destinés à simuler la perception, "
                                "détecter un bruit ou une créature cachée, échaper à une embuscade, etc.",
            'cost': lambda item: cof.properties.Cost(value=8.0,
                                                     unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'weight': cof.properties.Weight(value=2.0, unit='Kg')
        },
    }
}
