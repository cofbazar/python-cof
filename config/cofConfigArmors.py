# -*- coding: utf-8 -*-

import config.cofConfig
from cof.properties import *
from cof.utils import reduce_malus, get_def_level
from math import ceil

armors = {
    'cost': lambda item: Cost(
        value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
        unit=config.cofConfig.config['global']['cost']['unit']).iso(),
    'ids': ['tissu-matelasse', 'cuir', 'cuir-renforce', 'chemise-de-mailles', 'cotte-de-mailles', 'demi-plaque',
            'plaque-complete'],
    'flavors': {
        'quality': {
            'magical_levels': 0,
            'category': lambda item, magical_level: 'Optionel',
            'material': lambda item, magical_level: item.material,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='quality', count=1)],
            'name': lambda item, magical_level: "{}, de qualité".format(item.name),
            'short_description': lambda item, magical_level: "{} Cette armure est de qualité et réduit le malus de "
                                                             "DEX de 1.".format(item.short_description),
            'full_description': lambda item, magical_level: "{} Cette armure est de qualité et réduit le malus de "
                                                            "DEX de 1.".format(item.full_description),
            'cost': lambda item, magical_level: Cost(
                value=config.cofConfig.config['global']['cost']['quality'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso() + item.cost.iso() * 2,
            'skill': lambda item, magical_level: reduce_malus([m for m in item.skill], "Test", "DEX", 1),
        },
        'quality-twemby': {
            'magical_levels': 0,
            'category': lambda item, magical_level: 'quest',
            'material': lambda item, magical_level: item.material,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='quality', count=1),
                                                                 Flavor(ftype='twemby', count=1)],
            'name': lambda item, magical_level: "{}, des maîtres-artisans de Twemby".format(item.name),
            'short_description':
                lambda item, magical_level: "{} Cette armure est de superbe qualité, réduit le malus de "
                                            "DEX tout en améliorant sa défense.".format(item.short_description),
            'full_description': lambda item, magical_level: "{} Cette armure faite sur mesure par les "
                                                            "maîtres-artisans de Twemby est de superbe qualité. "
                                                            "Elle réduit le malus de DEX de 1 tout en améliorant "
                                                            "la défense de 1.".format(item.full_description),
            'cost': lambda item, magical_level: Cost(
                value=config.cofConfig.config['global']['cost']['quality'] +
                      config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso() + item.cost.iso() * 2,
            'defense': lambda item, magical_level: [
                Mod(label=m.label, target=m.target, mtype=m.mtype, die=m.die,
                    count=m.count + 1, limitation=m.limitation)
                if m.label == "DEF" else m for m in item.defense],
            'skill': lambda item, magical_level: reduce_malus([m for m in item.skill], "Test", "DEX", 1),
            'scenario': lambda item, magical_level: [
                Scenario(
                    campaign="Anathazerïn", title="Le Sanctuaire", chapter="Le Sanctuaire de Trenner", numbering="3"
                )
            ],
        },
        'magical': {
            'magical_levels': [1, 2, 3, 4],
        
            'name': lambda item, magical_level: "{} +{}".format(item.name, magical_level),
            'short_description': lambda item, magical_level: "{} Cette armure magique offre un bonus de DEF "
                                                             "de +{}.".format(item.short_description,
                                                                              magical_level),
            'full_description':
                lambda item, magical_level: "{} Cette armure est magique et offre un bonus de DEF de +{} et réduit "
                                            "de {} les pénalités qu'elle inflige.".format(
                    item.full_description, magical_level, magical_level),
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
            'skill': lambda item, magical_level: reduce_malus([m for m in item.skill], "Test", "DEX", magical_level),
        },
        'free-action': {
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'magical_levels': 1,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='free-action', count=1)],
            'name': lambda item, magical_level: "{}, d'action libre".format(item.name),
            'short_description':
                lambda item, magical_level: "{} Dans cette armure on ne peut pas être entravé pas magie.".format(
                    item.short_description),
            'full_description':
                lambda item, magical_level: "{} Dans cette armure le personnage ne peut pas être ralenti, immobilisé "
                                            "ou paralysé par la magie. Il obtient un bonus de +5 à tous les tests " 
                                            "pour résister à ce type d'effet préjudiciable s'il s'agit d'une "
                                            "contrainte physique.".format(item.full_description),
            'cost': lambda item, magical_level: Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso(),
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
                                                 limitation="Contraintes physiques uniquement")]
        },
        'defense': {
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'magical_levels': 1,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='defense', count=1)],
            'name': lambda item, magical_level: "{}, de défense".format(item.name),
            'short_description':
                lambda item, magical_level: "{} Cette armure réduit de 2 tous les DM subits.".format(
                    item.short_description),
            'full_description':
                lambda item, magical_level: "{} Cette armure réduit de 2 tous les DM subits.".format(
                    item.full_description),
            'defense': lambda item, magical_level: [m for m in item.defense] +
                                                   [Mod(label="RD", target="rd", count=2)],
            'cost': lambda item, magical_level: Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso()
        },
        'reinforced-defense': {
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'magical_levels': 2,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='defense', count=2)],
            'name': lambda item, magical_level: "{}, de défense supérieure".format(item.name),
            'short_description':
                lambda item, magical_level: "{} Cette armure réduit de 4 tous les DM subits.".format(
                    item.short_description),
            'full_description':
                lambda item, magical_level: "{} Cette armure réduit de 4 tous les DM subits.".format(
                    item.full_description),
            'defense': lambda item, magical_level: [m for m in item.defense] +
                                                   [Mod(label="RD", target="rd", count=4)],
            'cost': lambda item, magical_level: Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso()
        },
        'swimming': {
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'magical_levels': 1,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='swimming', count=1)],
            'name': lambda item, magical_level: "{}, de natation".format(item.name),
            'short_description':
                lambda item, magical_level: "{} Cette armure apporte un bonus de +5 au tests de natation.".format(
                    item.short_description),
            'full_description':
                lambda item, magical_level: "{} Cette armure apporte un bonus de +5 au tests de natation, de plus, "
                                            "elle flotte.".format(item.full_description),
            'skill': lambda item, magical_level: [m for m in item.skill] +
                                                 [Mod(label="Test", target="swimming", mtype="+", count=5)],
            'cost': lambda item, magical_level: Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso()
        },
        'shadow': {
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'magical_levels': 1,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='shadow', count=1)],
            'name': lambda item, magical_level: "{}, de l'ombre".format(item.name),
            'short_description':
                lambda item, magical_level: "{} Cette armure donne un bonus de +5 aux tests de discrétion.".format(
                    item.short_description),
            'full_description':
                lambda item, magical_level: "{} Cette armure donne un bonus de +5 aux tests de discrétion "
                                            "(DEX).".format(item.full_description),
            'skill': lambda item, magical_level: [m for m in item.skill] +
                                                 [Mod(label="Test", target="shadow", mtype="+", count=5)],
            'cost': lambda item, magical_level: Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso()
        },
        'protective': {
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'magical_levels': 1,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='protective', count=1)],
            'name': lambda item, magical_level: "{}, de protection".format(item.name),
            'short_description':
                lambda item, magical_level: "{} Cette armure divise par 2 les DM des coups critiques et des attaques "
                                            "sournoises.".format(item.short_description),
            'full_description':
                lambda item, magical_level: "{} Cette armure divise par 2 les DM des coups critiques et des attaques "
                                            "sournoises.".format(item.full_description),
            'cost': lambda item, magical_level: Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'special_property': lambda item, magical_level:
                item.special_property + ["DM / 2 : attaque sournoise et critique"]
        },
        'magical-resistance': {
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'magical_levels': 1,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='magical-resistance', count=1)],
            'name': lambda item, magical_level: "{}, de résistance à la magie".format(item.name),
            'short_description':
                lambda item, magical_level: "{} Cette armure apporte un bonus de +5 pour resister à la magie.".format(
                    item.short_description),
            'full_description':
                lambda item, magical_level: "{} Cette armure apporte un bonus de +5 en DEF ou aux tests pour résister "
                                            "à la magie.".format(item.full_description),
            'skill': lambda item, magical_level: [m for m in item.skill] +
                                                 [Mod(label="Test", target="magical-resistance", mtype="+", count=5)],
            'cost': lambda item, magical_level: Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'defense': lambda item, magical_level: [m for m in item.defense] +
                [Mod(label="DEF", target="magical", mtype="+", count=5, limitation="Seulement contre la magie")]
        },
        'fire-resistance': {
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'magical_levels': 1,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='fire', count=1)],
            'name': lambda item, magical_level: "{}, de résistance au feu".format(item.name),
            'short_description':
                lambda item, magical_level: "{} Cette armure réduis les dégats de feu de 10.".format(
                    item.short_description),
            'full_description':
                lambda item, magical_level: "{} Avec cette armure, son porteur retranche 10 points à tous les DM de "
                                            "feu subits".format(item.full_description),
            'defense': lambda item, magical_level: [m for m in item.defense] +
                                                   [Mod(label="RD", target="fire", count=10)],
            'cost': lambda item, magical_level: Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso()
        },
        'cold-resistance': {
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'magical_levels': 1,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='coldness', count=1)],
            'name': lambda item, magical_level: "{}, de résistance au froid".format(item.name),
            'short_description':
                lambda item, magical_level: "{} Cette armure réduis les dégats de froid de 10.".format(
                    item.short_description),
            'full_description':
                lambda item, magical_level: "{} Avec cette armure, son porteur retranche 10 points à tous les DM de "
                                            "froid subits".format(item.full_description),
            'defense': lambda item, magical_level: [m for m in item.defense] +
                                                   [Mod(label="RD", target="coldness", count=10)],
            'cost': lambda item, magical_level: Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso()
        },
        'acid-resistance': {
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'magical_levels': 1,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='acid', count=1)],
            'name': lambda item, magical_level: "{}, de résistance à l'acide".format(item.name),
            'short_description':
                lambda item, magical_level: "{} Cette armure réduis les dégats d'acide de 10.".format(
                    item.short_description),
            'full_description':
                lambda item, magical_level: "{} Avec cette armure, son porteur retranche 10 points à tous les DM "
                                            "d'acide subits".format(item.full_description),
            'defense': lambda item, magical_level: [m for m in item.defense] +
                                                   [Mod(label="RD", target="acid", count=10)],
            'cost': lambda item, magical_level: Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso()
        },
        'lightning-resistance': {
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'magical_levels': 1,
            'name': lambda item, magical_level: "{}, de résistance à la foudre".format(item.name),
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='lightning', count=1)],
            'short_description':
                lambda item, magical_level: "{} Cette armure réduis les dégats de foudre de 10.".format(
                    item.short_description),
            'full_description':
                lambda item, magical_level: "{} Avec cette armure, son porteur retranche 10 points à tous les DM de "
                                            "foudre subits".format(item.full_description),
            'defense': lambda item, magical_level: [m for m in item.defense] +
                                                   [Mod(label="RD", target="lightning", count=10)],
            'cost': lambda item, magical_level: Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso()
        },
        'durium': {
            'category': lambda item, magical_level: 'Bazar du bizarre',
            'material': lambda item, magical_level: 'durium',
            'magical_levels': 0,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='durium', count=1)],
            'name': lambda item, magical_level: "{}, en durium".format(item.name),
            'short_description':
                lambda item, magical_level: "{} Cette armure apporte un bonus en DEF, mais impose une "
                                            "forte pénalité d'armure.".format(item.short_description),
            'full_description':
                lambda item, magical_level: "{} Cette armure est faite en durium, un métal bleu sombre "
                                            "très dur et particulièrement lourd. Elle augmente la DEF de +1 mais "
                                            "impose une pénalité d'armure de +2, ce qui n'est pas très "
                                            "avantageux.".format(item.full_description),
            'defense': lambda item, magical_level: [
                Mod(label=m.label, target=m.target, mtype=m.mtype, die=m.die,
                    count=m.count + 1, limitation=m.limitation)
                if m.label == "DEF" else m for m in item.defense],
            'skill': lambda item, magical_level: reduce_malus([m for m in item.skill], "Test", "DEX", -2),
            'cost': lambda item, magical_level: Cost(
                value=get_def_level(item.defense) * 2 * config.cofConfig.config['global']['cost']['durium'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso()
        },
        'dalberath': {
            'category': lambda item, magical_level: 'Bazar du bizarre',
            'material': lambda item, magical_level: 'dalberath',
            'magical_levels': 0,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='dalberath', count=1)],
            'name': lambda item, magical_level: "{}, en dalberath".format(item.name),
            'short_description':
                lambda item, magical_level: "{} Cette armure en dalberath fait un parfait gilet de "
                                            "sauvetage.".format(item.short_description),
            'full_description':
                lambda item, magical_level: "{} Cette armure est faite en dalberath, un métal de couleur blanche "
                                            "dont la particularité est de flotter. Cette armure "
                                            "constitue un parfait gilet de "
                                            "sauvetage.".format(item.full_description),
            "special_property": lambda item, magical_level: item.special_property + ["Permet de surnager"],
            'cost': lambda item, magical_level: Cost(
                value=get_def_level(item.defense) * 2 * config.cofConfig.config['global']['cost']['dalberath'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso()
        },
        'mythral': {
            'category': lambda item, magical_level: 'Bazar du bizarre',
            'material': lambda item, magical_level: 'dalberath',
            'magical_levels': 0,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='mythral', count=1)],
            'name': lambda item, magical_level: "{}, en mythral".format(item.name),
            'short_description':
                lambda item, magical_level: "{} Cette armure en mythral réduit la pénalité "
                                            "d'armure.".format(item.short_description),
            'full_description':
                lambda item, magical_level: "{} Cette armure est faite en mythral, un métal très léger de couleur "
                                            "argent. Cette armure voit sa pénalité d'armure réduite "
                                            "de 2 points.".format(item.full_description),
            'skill': lambda item, magical_level: reduce_malus([m for m in item.skill], "Test", "DEX", 2),
            'cost': lambda item, magical_level: Cost(
                value=get_def_level(item.defense) * 2 * config.cofConfig.config['global']['cost']['mythral'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso()
        },
        'adamantium': {
            'category': lambda item, magical_level: 'Bazar du bizarre',
            'material': lambda item, magical_level: 'adamantium',
            'magical_levels': 0,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='adamantium', count=1)],
            'name': lambda item, magical_level: "{}, en adamantium".format(item.name),
            'short_description':
                lambda item, magical_level: "{} Cette armure réduit les dégâts subits.".format(item.short_description),
            'full_description':
                lambda item, magical_level: "{} Cette armure est faite en adamantium, un métal d'une duretée "
                                            "exceptionnellet. Son point de fusion particulièrement élevé le rend très "
                                            "difficile à forger. Cette armure confère à son porteur une réduction "
                                            "des DM égale à sa défense divisée oar 2 (arrondi au "
                                            "supérieur).".format(item.full_description),
            'defense':
                lambda item, magical_level: item.defense +
                                            [Mod(label="RD", target="rd", count=ceil(get_def_level(item.defense)/2))],
            'cost': lambda item, magical_level: Cost(
                value=get_def_level(item.defense) * 2 * config.cofConfig.config['global']['cost']['adamantium'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso()
        },
        'sombracier': {
            'category': lambda item, magical_level: 'Bazar du bizarre',
            'material': lambda item, magical_level: 'sombracier',
            'magical_levels': 0,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='sombracier', count=1)],
            'name': lambda item, magical_level: "{}, en sombracier".format(item.name),
            'short_description':
                lambda item, magical_level: "{} Cette armure octroie une résistance à la "
                                            "magie.".format(item.short_description),
            'full_description':
                lambda item, magical_level: f"{item.full_description} Cette armure est faite en sombracier, un métal "
                                            "lourd presque noir imperméable à la magie. Ce métal très rare et "
                                            "recherché n'est absolument pas afecté par la magie. Il passe à travers "
                                            "tous les sorts de protection et ignore les bonus de magie des armures "
                                            "ou ceux accordés par des sorts. L'inconvénient majeur reste que cette "
                                            "armure n'est absolument pas affectée par les sorts dont le propriétaire "
                                            "bénéficie: s'il est invisible, l'armure semble flotter dans les airs, "
                                            "s'il est téléporté, alors l'armure reste sur place. Une armure en "
                                            "sombracier est lourde et augmente la pénalité d'encombrement de 1 point. "
                                            "Cependant, elle octroie une résistance à la magie élevée. Cette armure "
                                            "à un score de résistance à la magie (RM) de "
                                            f"{get_def_level(item.defense)*2}. Désormais à chaque fois "
                                            "que le personnage est la cible d'un sort (ou affecté par un sort de "
                                            "zone), il doit lancer un d20. Si le résultat est inférieur ou égal au "
                                            "score de RM, il n'est pas affecté.",
            'skill': lambda item, magical_level: reduce_malus([m for m in item.skill], "Test", "DEX", -1),
            "special_property":
                lambda item, magical_level: item.special_property + [
                    f"RM (résistance à la magie) : {get_def_level(item.defense)*2}",
                    f"Non affecté par un sort si d20 < RM"
                ],
            'cost': lambda item, magical_level: Cost(
                value=get_def_level(item.defense) * 2 * config.cofConfig.config['global']['cost']['adamantium'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso()
        },
    },
    'addons': {
        'tissu-matelasse': {
            'name': 'Armure matelassée',
            'base_item': 'tissu-matelasse',
            'full_description': "Une armure matelassée se compose de couches de tissus matelassés et battus. Elle "
                                "procure un bonus de DEF +1.",
            'short_description': "Armure composée de tissus matelassés et battus.",
            'weight': Weight(value=4.0, unit='Kg'),
            'defense': [Mod(label="DEF", mtype="+", count=1)],
            'skill': [Mod(label="Test", target="DEX", count=1, mtype="-")]
        },
        'cuir': {
            'name': 'Armure de cuir',
            'base_item': 'cuir',
            'full_description': "La cuirasse et les protecteurs d'épaules de cette armure sont faits de cuir qui "
                                "a été durci en étant bouilli dans de l'huile. Le reste de l'armure est fait de "
                                "matériaux plus tendres et plus souples. Elle procure un bonus de DEF +2.",
            'short_description': "Armure composée de cuir souple dont certaines parties ont été durcies.",
            'weight': Weight(value=5.0, unit='Kg'),
            'defense': [Mod(label="DEF", mtype="+", count=2)],
            'skill': [Mod(label="Test", target="DEX", count=2, mtype="-")]
        },
        'cuir-renforce': {
            'name': 'Armure cuir renforcé',
            'base_item': 'cuir-renforce',
            'full_description': "Fabriquée à partir de cuir résistant mais souple, l'armure de cuir clouté est "
                                "renforcée avec des rivets ou des pointes. Elle procure un bonus de DEF +3.",
            'short_description': "Armure composée de cuir renforcée avec des rivets ou des pointes.",
            'weight': Weight(value=7.0, unit='Kg'),
            'defense': [Mod(label="DEF", mtype="+", count=3)],
            'skill': [Mod(label="Test", target="DEX", count=3, mtype="-")]
        },
        'chemise-de-mailles': {
            'base_item': 'chemise-de-mailles',
            'name': 'Chemise de mailles',
            'full_description': "Fait d'anneaux métalliques entrecroisés, la chemise de mailles est utilisée "
                                "entre des couches de vêtements ou de cuir. Cette armure offre une protection "
                                "modeste pour le haut du corps et permet au son provoqué par les anneaux frottant "
                                "l'un contre l'autre d'être atténué par les couches de vêtements extérieures. Elle "
                                "procure un bonus de DEF +4.",
            'short_description': "Armure composée de d'anneaux métalliques qui protège surtout le "
                                 "haut du corps.",
            'weight': Weight(value=20.0, unit='Kg'),
            'defense': [Mod(label="DEF", mtype="+", count=4)],
            'skill': [Mod(label="Test", target="DEX", count=4, mtype="-")]
        },
        'cotte-de-mailles': {
            'name': 'Cotte de mailles',
            'base_item': 'cotte-de-mailles',
            'full_description': "Fait d'anneaux métalliques entrecroisés, la cotte de mailles comprend une couche "
                                "de tissu matelassé porté sous la cotte pour éviter les frottements et amortir "
                                "l'impact de coups. Elle protège l'ensemble du corps et procure un bonus "
                                "de DEF +5.",
            'short_description': "Armure composée de d'anneaux métalliques qui protège l'ensemble "
                                 "du corps.",
            'weight': Weight(value=20.0, unit='Kg'),
            'defense': [Mod(label="DEF", mtype="+", count=5)],
            'skill': [Mod(label="Test", target="DEX", count=5, mtype="-")]
        },
        'demi-plaque': {
            'name': 'Demi-plaque',
            'base_item': 'demi-plaque',
            'full_description': "Armure composée de grandes plaques de métal qui protège le corps du combattant"
                                "à l'exception des jambes. Les plaques sont moulées de façons à ce qu’elles "
                                "dévient les coups les plus faibles et leur épaisseur garantit un maximum de "
                                "protection. Un combattant protégé par ce genre de protection est fortement "
                                "encombré dans ses mouvements. Elle procure un bonus de DEF +6.",
            'short_description': "Armure, faite de plaques de métal, qui protège le haut du corps du combattant.",
            'weight': Weight(value=20.0, unit='Kg'),
            'defense': [Mod(label="DEF", mtype="+", count=6)],
            'skill': [Mod(label="Test", target="DEX", count=6, mtype="-")]
        },
        'plaque-complete': {
            'name': 'Plaque complète',
            'base_item': 'plaque-complete',
            'full_description': "Armure composée de grandes plaques de métal qui protège le corps du combattant. "
                                "Les plaques sont moulées de façons à ce qu’elles dévient les coups les plus "
                                "faibles et leur épaisseur garantit un maximum de protection. Un combattant "
                                "protégé par ce genre de protection intégrale est fortement encombré "
                                "dans ses mouvements. Elle procure un bonus de DEF +8. Cette armure est utilisable "
                                "uniquement au départ par les chevaliers.",
            'short_description': "Armure composée de plaques de métal qui protège le corps du combattant.",
            'usable_by': ['Chevalier'],
            'weight': Weight(value=25.0, unit='Kg'),
            'defense': [Mod(label="DEF", mtype="+", count=8)],
            'skill': [Mod(label="Test", target="DEX", count=8, mtype="-")]
        }
    }
}
