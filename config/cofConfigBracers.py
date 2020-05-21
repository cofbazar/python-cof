# -*- coding: utf-8 -*-

from cof.properties import *
import config.cofConfig

bracers = {
    'cost': lambda item: Cost(
        value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
        unit=config.cofConfig.config['global']['cost']['unit']).iso(),
    'others': {
        'bracers-of-defense': {
            'exclude': ['bracers-of-defense'],
            'magical_level': 0,
            'name': "Bracelets",
            'short_description': "Bracelets de défense.",
            'full_description': "Le bonus des bracelets de défense ne se cumule pas avec le bonus d'armure. Ils sont "
                                "en général utilisé par les magiciens ou les moines.",
            'cost': lambda item: cof.properties.Cost(value=0, unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'weight': cof.properties.Weight(value=0.1, unit='Kg'),
            'skill': [],
            'defense': [Mod(label="DEF", target="", mtype="+", count=0)],
            'special_property': [],
            'base_item': 'bracers-of-defense',
        },
    },
    'flavors': {
        'magical': {
            'magical_levels': [1, 2, 3, 4],
            'name': lambda item, magical_level: "{} +{}".format(item.name, magical_level),
            'short_description': lambda item, magical_level: "{} Ces bracelets sont magiques et offre un bonus en DEF "
                                                             "de +{}.".format(item.short_description,
                                                                              magical_level),
            'full_description': lambda item, magical_level: "{} Ces bracelets sont magiques et offre un bonus en DEF "
                                                            "de +{}.".format(
                item.full_description, magical_level),
            'material': lambda item, magical_level: item.material,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='magical', count=magical_level)],
            'defense': lambda item, magical_level: [
                Mod(label=m.label, target=m.target, mtype=m.mtype, die=m.die,
                    count=m.count + magical_level, limitation=m.limitation)
                if m.label == "DEF" else m for m in item.defense], 
            'cost': lambda item, magical_level: cof.properties.Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso()
        },
        'free-action': {
            'magical_levels': 1,
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'name': lambda item, magical_level: "{}, d'action libre".format(item.name),
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='free-action', count=1)],
            'short_description': lambda item, magical_level: "{} Avec ces bracelets, le personnage ne peut être "
                                                             "ralenti, immobilisé ou paralysé par magie.".format(
                item.short_description),
            'full_description': lambda item, magical_level: "{} Avec ces bracelets, le personnage ne peut être "
                                                            "ralenti, immobilisé ou paralysé par magie. Il obtient "
                                                            "également un bonus de +5 à tous les tests pour résister "
                                                            "à ce type d'effet préjudiciable s'il s'agit d'une "
                                                            "contrainte physique.".format(item.full_description),
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
            'cost': lambda item, magical_level: cof.properties.Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso()
        },
        'defense': {
            'magical_levels': 1,
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='defense', count=1)],
            'name': lambda item, magical_level: "{}, de défense".format(item.name),
            'short_description': lambda item, magical_level: "{} Ces bracelets réduisent de 2 tous les DM "
                                                             "subits.".format(item.short_description),
            'full_description': lambda item, magical_level: "{} Ces bracelets réduisent de 2 tous les DM "
                                                            "subits.".format(item.full_description),
            'defense': lambda item, magical_level: [m for m in item.defense] +
                                                   [Mod(label="RD", target="rd", count=2)],
            'cost': lambda item, magical_level: cof.properties.Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso()
        },
        'reinforced-defense': {
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'magical_levels': 2,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='defense', count=2)],
            'name': lambda item, magical_level: "{}, de défense supérieure".format(item.name),
            'short_description': lambda item, magical_level: "{} Ces bracelets réduisent de 4 tous les DM "
                                                             "subits.".format(item.short_description),
            'full_description': lambda item, magical_level: "{} Ces bracelets réduisent de 4 tous les DM "
                                                            "subits.".format(item.full_description),
            'defense': lambda item, magical_level: [m for m in item.defense] +
                                                   [Mod(label="RD", target="rd", count=4)],
            'cost': lambda item, magical_level: cof.properties.Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso()
        },
        'swimming': {
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'magical_levels': 1,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='swimming', count=1)],
            'name': lambda item, magical_level: "{}, de natation".format(item.name),
            'short_description': lambda item, magical_level: "{} Ces bracelets apportent un bonus de +5 aux test de "
                                                             "natation.".format(item.short_description),
            'full_description': lambda item, magical_level: "{} Ces bracelets apportent un bonus de +5 aux test de "
                                                            "natation.".format(item.full_description),
            'skill': lambda item, magical_level: [m for m in item.skill] +
                                                 [Mod(label="Test", target="swimming", mtype="+", count=5)],
            'cost': lambda item, magical_level: cof.properties.Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso()
        },
        'shadow': {
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'magical_levels': 1,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='shadow', count=1)],
            'name': lambda item, magical_level: "{}, de l'ombre".format(item.name),
            'short_description': lambda item, magical_level: "{} Ces bracelets apportent un bonus +5 aux test de "
                                                             "discrétion.".format(item.short_description),
            'full_description': lambda item, magical_level: "{} Ces bracelets apportent un bonus +5 aux test de "
                                                            "discrétion (DEX).".format(item.full_description),
            'skill': lambda item, magical_level: [m for m in item.skill] +
                                                 [Mod(label="Test", target="shadow", mtype="+", count=5)],
            'cost': lambda item, magical_level: cof.properties.Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso()
        },
        'protective': {
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'magical_levels': 1,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='protective', count=1)],
            'name': lambda item, magical_level: "{}, de protection".format(item.name),
            'short_description': lambda item, magical_level: "{} Ces bracelets réduisent les dégats critiques".format(
                item.short_description),
            'full_description': lambda item, magical_level: "{} Ces bracelets divisent par 2 les DM des coups "
                                                            "critiques et des attaques sournoises.".format(
                item.full_description),
            'special_property': lambda item, magical_level:
                item.special_property + ["DM / 2 : attaque sournoise et critique"],
            'cost': lambda item, magical_level: cof.properties.Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso()
        },
        'magical-resistance': {
            #'exclude': ['bracers-of-defense-magical+{}'.format(level) for level in [1, 2, 3, 4]],
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'magical_levels': 1,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='magical-resistance', count=1)],
            'name': lambda item, magical_level: "{}, de resistance à la magie".format(item.name),
            'short_description': lambda item, magical_level: "{} Ces bracelets apportent un bonus de +5 en DEF "
                                                             "pour résister à la magie.".format(
                item.short_description),
            'full_description': lambda item, magical_level: "{} Ces bracelets apportent un bonus de +5 en DEF ou aux "
                                                            "tests pour résister à la magie.".format(
                item.full_description),
            'defense': lambda item, magical_level: [m for m in item.defense] +
                [Mod(label="DEF", target="magical", mtype="+", count=5, limitation="Seulement contre la magie")],
            'cost': lambda item, magical_level: cof.properties.Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso()
        },
        'fire-resistance': {
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'magical_levels': 1,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='fire', count=1)],
            'name': lambda item, magical_level: "{}, de resistance au feu".format(item.name),
            'short_description': lambda item, magical_level: "{} Ces bracelets permettent de réduire de 10 DM les "
                                                             "dếgats occasionnés par le feu.".format(
                item.short_description),
            'full_description': lambda item, magical_level: "{} Ces bracelets permettent de réduire de 10 DM les "
                                                            "dếgats occasionnés par le feu.".format(
                item.full_description),
            'defense': lambda item, magical_level: [m for m in item.defense] +
                                                   [Mod(label="RD", target="fire", count=10)],
            'cost': lambda item, magical_level: cof.properties.Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso()
        },
        'coldness-resistance': {
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'magical_levels': 1,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='coldness', count=1)],
            'name': lambda item, magical_level: "{}, de resistance au froid".format(item.name),
            'short_description': lambda item, magical_level: "{} Ces bracelets permettent de réduire de 10 DM les "
                                                             "dếgats occasionnés par le froid.".format(
                item.short_description),
            'full_description': lambda item, magical_level: "{} Ces bracelets permettent de réduire de 10 DM les "
                                                            "dếgats occasionnés par le froid.".format(
                item.full_description),
            'defense': lambda item, magical_level: [m for m in item.defense] +
                                                   [Mod(label="RD", target="coldness", count=10)],
            'cost': lambda item, magical_level: cof.properties.Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso()
        },
        'acid-resistance': {
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'magical_levels': 1,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='acid', count=1)],
            'name': lambda item, magical_level: "{}, de resistance à l'acide".format(item.name),
            'short_description': lambda item, magical_level: "{} Ces bracelets permettent de réduire de 10 DM les "
                                                             "dếgats occasionnés par l'acide.".format(
                item.short_description),
            'full_description': lambda item, magical_level: "{} Ces bracelets permettent de réduire de 10 DM les "
                                                            "dếgats occasionnés par l'acide.".format(
                item.full_description),
            'defense': lambda item, magical_level: [m for m in item.defense] +
                                                   [Mod(label="RD", target="acid", count=10)],
            'cost': lambda item, magical_level: cof.properties.Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso()
        },
        'lightning-resistance': {
            'magical_levels': 1,
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='lightning', count=1)],
            'name': lambda item, magical_level: "{}, de resistance à la foudre".format(item.name),
            'short_description': lambda item, magical_level: "{} Ces bracelets permettent de réduire de 10 DM les "
                                                             "dếgats occasionnés par la foudre.".format(
                item.short_description),
            'full_description': lambda item, magical_level: "{} Ces bracelets permettent de réduire de 10 DM les "
                                                            "dếgats occasionnés par la foudre.".format(
                item.full_description),
            'defense': lambda item, magical_level: [m for m in item.defense] +
                                                   [Mod(label="RD", target="lightning", count=10)],
            'cost': lambda item, magical_level: cof.properties.Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso()
        }
    }
}
