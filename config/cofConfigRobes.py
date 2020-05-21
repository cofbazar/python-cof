# -*- coding: utf-8 -*-

from cof.properties import *
import config.cofConfig

robes = {
    'cost': lambda item: Cost(
        value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
        unit=config.cofConfig.config['global']['cost']['unit']).iso(),
    'others': {
        'robe-of-wizard': {
            'skill': [],
            'defense': [Mod(label="DEF", target="", mtype="+", count=0)],
            'special_property': [],
            'base_item': 'robe-of-wizard',
            'magical_level': 0,
            'name': "Robe de mage",
            'short_description': "Robe de mage.",
            'full_description': "Le bonus de la robe de mage ne se cumule pas avec le bonus d'armure. Elle est en "
                                "général utilisé par les magiciens.",
            'cost': lambda item: cof.properties.Cost(value=2, unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'weight': cof.properties.Weight(value=1.0, unit='Kg')
        }
    },
    'flavors': {
        'magical': {
            'material': lambda item, magical_level: item.material,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='magical', count=magical_level)],
            'defense': lambda item, magical_level: [
                Mod(label=m.label, target=m.target, mtype=m.mtype, die=m.die,
                    count=m.count + magical_level, limitation=m.limitation)
                if m.label == "DEF" else m for m in item.defense],
            'magical_levels': [1, 2, 3, 4],
            'name': lambda item, magical_level: "{} +{}".format(item.name, magical_level),
            'short_description': lambda item, magical_level: "{} Cette robe est magique et offre un bonus en DEF "
                                                             "de +{}.".format(item.short_description,
                                                                              magical_level),
            'full_description': lambda item, magical_level: "{} Cette robe est magique et offre un bonus en DEF "
                                                            "de +{}.".format(
                item.full_description, magical_level),
            'cost': lambda item, magical_level: cof.properties.Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso()
        },
        'free-move': {
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='free-action', count=1)],
            'special_property':
                lambda item, magical_level: [p for p in item.special_property] +
                                            ["Immunité : ralenti, paralysé, immobilisé par la magie"],
            'skill':
                lambda item, magical_level: [m for m in item.skill] +
                                            [Mod(label="Test", target="slowdown-resistance", mtype="+", count="5",
                                                 limitation="Contraintes physiques uniquement"),
                                             Mod(label="Test", target="immobilized-resistance", mtype="+", count="5",
                                                 limitation="Contraintes physiques uniquement"),
                                             Mod(label="Test", target="paralysed-resistance", mtype="+", count="5",
                                                 limitation="Contraintes physiques uniquement")],
            'magical_levels': 1,
            'name': lambda item, magical_level: "{}, d'action libre".format(item.name),
            'short_description': lambda item, magical_level: "{} Dans cette robe, le personnage ne peut être ralenti, "
                                                             "immobilisé ou paralysé par magie.".format(
                item.short_description),
            'full_description': lambda item, magical_level: "{} Dans cette robe, le personnage ne peut être ralenti, "
                                                            "immobilisé ou paralysé par magie. Il obtient également "
                                                            "un bonus de +5 à tous les tests pour résister à ce type "
                                                            "d'effet préjudiciable s'il s'agit d'une contrainte "
                                                            "physique.".format(item.full_description),

            'cost': lambda item, magical_level: cof.properties.Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso()
        },
        'defense': {
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='defense', count=1)],
            'defense': lambda item, magical_level: [m for m in item.defense] +
                                                   [Mod(label="RD", target="rd", count=2)],
            'magical_levels': 1,
            'name': lambda item, magical_level: "{}, de défense".format(item.name),
            'short_description': lambda item, magical_level: "{} Cette robe réduit de 2 tous les DM subits.".format(
                item.short_description),
            'full_description': lambda item, magical_level: "{} Cette robe réduit de 2 tous les DM subits.".format(
                item.full_description),

            'cost': lambda item, magical_level: cof.properties.Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso()
        },
        'higher-defense': {
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='defense', count=2)],
            'defense': lambda item, magical_level: [m for m in item.defense] +
                                                   [Mod(label="RD", target="rd", count=4)],
            'magical_levels': 2,
            'name': lambda item, magical_level: "{}, de défense supérieure".format(item.name),
            'short_description': lambda item, magical_level: "{} Cette robe réduit de 4 tous les DM subits.".format(
                item.short_description),
            'full_description': lambda item, magical_level: "{} Cette robe réduit de 4 tous les DM subits.".format(
                item.full_description),

            'cost': lambda item, magical_level: cof.properties.Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso()
        },
        'swimming': {
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='swimming', count=1)],
            'skill': lambda item, magical_level: [m for m in item.skill] +
                                                 [Mod(label="Test", target="swimming", mtype="+", count=5)],
            'magical_levels': 1,
            'name': lambda item, magical_level: "{}, de natation".format(item.name),
            'short_description': lambda item, magical_level: "{} Cette robe apporte un bonus de +5 aux test de "
                                                             "natation.".format(item.short_description),
            'full_description': lambda item, magical_level: "{} Cette robe apporte un bonus de +5 aux test de "
                                                            "natation.".format(item.full_description),

            'cost': lambda item, magical_level: cof.properties.Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso()
        },
        'shadow': {
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='shadow', count=1)],
            'skill': lambda item, magical_level: [m for m in item.skill] +
                                                 [Mod(label="Test", target="shadow", mtype="+", count=5)],
            'magical_levels': 1,
            'name': lambda item, magical_level: "{}, de l'ombre".format(item.name),
            'short_description': lambda item, magical_level: "{} Cette robe apporte un bonus +5 aux test de "
                                                             "discrétion.".format(item.short_description),
            'full_description': lambda item, magical_level: "{} Cette robe apporte un bonus +5 aux test de discrétion "
                                                            "(DEX).".format(item.full_description),

            'cost': lambda item, magical_level: cof.properties.Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso()
        },
        'protective': {
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='protective', count=1)],
            'special_property': lambda item, magical_level:
                item.special_property + ["DM / 2 : attaque sournoise et critique"],
            'magical_levels': 1,
            'name': lambda item, magical_level: "{}, de protection".format(item.name),
            'short_description': lambda item, magical_level: "{} Cette robe réduit les dégats critiques".format(
                item.short_description),
            'full_description': lambda item, magical_level: "{} Cette robe divise par 2 les DM des coups critiques et "
                                                            "des attaques sournoises.".format(
                item.full_description),

            'cost': lambda item, magical_level: cof.properties.Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso()
        },
        'magical-resistance': {
            #'exclude': ['robe-of-wizard-magical+{}'.format(level) for level in [1, 2, 3, 4]],
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='magical-resistance', count=1)],
            'defense': lambda item, magical_level: [m for m in item.defense] +
                [Mod(label="DEF", target="magical", mtype="+", count=5, limitation="Seulement contre la magie")], 
            'magical_levels': 5,
            'name': lambda item, magical_level: "{}, de resistance à la magie".format(item.name),
            'short_description': lambda item, magical_level: "{} Cette robe apporte un bonus de +5 en DEF pour "
                                                             "résister à la magie.".format(
                item.short_description),
            'full_description': lambda item, magical_level: "{} Cette robe apporte un bonnus de +5 en DEF ou aux tests "
                                                            "pour résister à la magie.".format(
                item.full_description),

            'cost': lambda item, magical_level: cof.properties.Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso()
        },
        'fire-resistance': {
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='fire', count=1)],
            'defense': lambda item, magical_level: [m for m in item.defense] +
                                                   [Mod(label="RD", target="fire", count=10)],
            'magical_levels': 1,
            'name': lambda item, magical_level: "{}, de resistance au feu".format(item.name),
            'short_description': lambda item, magical_level: "{} Cette robe permet de réduire de 10 DM les dếgats "
                                                             "occasionnés par le feu.".format(
                item.short_description),
            'full_description': lambda item, magical_level: "{} Cette robe permet de réduire de 10 DM les dếgats "
                                                            "occasionnés par le feu.".format(
                item.full_description),

            'cost': lambda item, magical_level: cof.properties.Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso()
        },
        'coldness-resistance': {
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='coldness', count=1)],
            'defense': lambda item, magical_level: [m for m in item.defense] +
                                                   [Mod(label="RD", target="coldness", count=10)],
            'magical_levels': 1,
            'name': lambda item, magical_level: "{}, de resistance au froid".format(item.name),
            'short_description': lambda item, magical_level: "{} Cette robe permet de réduire de 10 DM les dếgats "
                                                             "occasionnés par le froid.".format(
                item.short_description),
            'full_description': lambda item, magical_level: "{} Cette robe permet de réduire de 10 DM les dếgats "
                                                            "occasionnés par le froid.".format(
                item.full_description),

            'cost': lambda item, magical_level: cof.properties.Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso()
        },
        'acid-resistance': {
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='acid', count=1)],
            'defense': lambda item, magical_level: [m for m in item.defense] +
                                                   [Mod(label="RD", target="acid", count=10)],
            'magical_levels': 1,
            'name': lambda item, magical_level: "{}, de resistance à l'acide".format(item.name),
            'short_description': lambda item, magical_level: "{} Cette robe permet de réduire de 10 DM les dếgats "
                                                             "occasionnés par l'acide.".format(
                item.short_description),
            'full_description': lambda item, magical_level: "{} Cette robe permet de réduire de 10 DM les dếgats "
                                                            "occasionnés par l'acide.".format(
                item.full_description),

            'cost': lambda item, magical_level: cof.properties.Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso()
        },
        'lightning-resistance': {
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='lightning', count=1)],
            'defense': lambda item, magical_level: [m for m in item.defense] +
                                                   [Mod(label="RD", target="lightning", count=10)],
            'magical_levels': 1,
            'name': lambda item, magical_level: "{}, de resistance à la foudre".format(item.name),
            'short_description': lambda item, magical_level: "{} Cette robe permet de réduire de 10 DM les dếgats "
                                                             "occasionnés par la foudre.".format(
                item.short_description),
            'full_description': lambda item, magical_level: "{} Cette robe permet de réduire de 10 DM les dếgats "
                                                            "occasionnés par la foudre.".format(
                item.full_description),

            'cost': lambda item, magical_level: cof.properties.Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso()
        }
    }
}
