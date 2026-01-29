# -*- coding: utf-8 -*-

from cof.properties import *
import config.cofConfig
from cof.utils import reduce_mod, increase_dice, max_dm
from ClusterShell.NodeSet import RangeSet

ranged_weapons = ['arbalete-de-poing', 'arbalete-legere', 'arbalete-lourde', 'arc-court', 'arc-long',
                  'fronde', 'mousquet', 'petoire', 'recurse-crossbow']

short_weapons = ['dague', 'dague-de-jet', 'epee-courte', 'left-hand', 'rapiere', 'stiletto', 'throwing-knife',
                 'throwing-shuriken']

long_weapons = ['baton', 'baton-ferre', 'epee-batarde', 'epee-longue', 'hache-a-1-main', 'gourdin', 'hachette',
                'javelot', 'katana', 'masse-d-armes', 'marteau-de-guerre', 'scourge', 'vivelame']

heavy_weapons = ['2-hands-scourge', 'cavalry-spear', 'epee-a-2-mains', 'hache-a-2-mains', 'pike', 'spear']

lothar_exclude_weapons = ranged_weapons + long_weapons + heavy_weapons


weapon_size = {
    "short_weapons": {
        "bonus-defense-magique": 1,
        "zone-lumiere": 3,
    },
    "1-hand": {
        "bonus-defense-magique": 2,
        "zone-lumiere": 6,
    },
    "2-hands": {
        "bonus-defense-magique": 3,
        "zone-lumiere": 12,
    }
}


def get_size(weapon):
    if weapon.base_item in short_weapons:
        return "short_weapons"
    elif weapon.hands == 1:
        return "1-hand"
    else:
        return "2-hands"


weapons = {
    'cost': lambda item: Cost(
        value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
        unit=config.cofConfig.config['global']['cost']['unit']).iso(),
    'flavors': {
        'magical': {
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'magical_levels': [1, 2, 3, 4],
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='magical', count=magical_level)],
            'name': lambda item, magical_level: "{} +{}".format(item.name, magical_level),
            'short_description': lambda item, magical_level: "{} Cette arme est magique avec un bonus de +{}.".format(
                item.short_description, magical_level),
            'full_description': lambda item, magical_level: "{} Cette arme est magique et offre un bonus de +{} en "
                                                            "attaque et aux dégats.".format(item.full_description,
                                                                                            magical_level),
            'cost': lambda item, magical_level: cof.properties.Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'attack': lambda item, magical_level: None if item.attack is None else Attack(
                atype=item.attack.atype,
                name=item.attack.name,
                mod=item.attack.mod + magical_level,
                damages=Damage(
                    base=[bdm for bdm in item.attack.damages.base],
                    other=[odm for odm in item.attack.damages.other] +
                          [Mod(mtype="+", count=magical_level, target="magical")]
                ),
                range=None if item.attack.range is None else Range(value=item.attack.range.value,
                                                                   unit=item.attack.range.unit),
                area=None if item.attack.area is None else Area(value=item.attack.area.value,
                                                                unit=item.attack.area.unit),
                critical=item.attack.critical.union(RangeSet())
            )
        },
        'quality': {
            'category': lambda item, magical_level: 'Optionel',
            'material': lambda item, magical_level: item.material,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='quality', count=1)],
            'magical_levels': 0,
            'name': lambda item, magical_level: "{}, de qualité".format(item.name),
            'short_description': lambda item, magical_level: "{} Cette arme est de qualité et offre un bonus "
                                                             "de +1.".format(item.short_description),
            'full_description': lambda item, magical_level: "{} Cette arme est de qualité et offre un bonus de +1 "
                                                            "en attaque ou aux dégats.".format(
                item.full_description),
            'cost': lambda item, magical_level: cof.properties.Cost(
                value=config.cofConfig.config['global']['cost']['quality'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso() + item.cost.iso() * 2,
            'special_property': lambda item, magical_level: [sp for sp in item.special_property] +
                                                            ['Attaque : +1 ou DM : +1']

        },
        'sharp': {
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='sharp', count=1)],
            'magical_levels': 1,
            'name': lambda item, magical_level: "{}, affûtée".format(item.name),
            'short_description': lambda item, magical_level: "{} Cette arme est affûtée et augmente les "
                                                             "critiques de 1.".format(
                item.short_description),
            'full_description': lambda item, magical_level: "{} Cette arme est magique et augmente les chances de "
                                                            "réussite critique de 1 point et ajoute +1d6 aux "
                                                            "dégats critiques.".format(item.full_description),

            'cost': lambda item, magical_level: cof.properties.Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'attack': lambda item, magical_level: None if item.attack is None else Attack(
                atype=item.attack.atype,
                name=item.attack.name,
                mod=item.attack.mod,
                damages=Damage(
                    base=[bdm for bdm in item.attack.damages.base],
                    other=[odm for odm in item.attack.damages.other]
                ),
                range=None if item.attack.range is None else Range(value=item.attack.range.value,
                                                                   unit=item.attack.range.unit),
                area=None if item.attack.area is None else Area(value=item.attack.area.value,
                                                                unit=item.attack.area.unit),
                critical=RangeSet("{}-{}".format(item.attack.critical[0]-1, item.attack.critical[-1]))
            ),
            # Done at generation time
            # 'special_property': lambda item, magical_level: [sp for sp in item.special_property]
            # if item.attack is None else
            # [sp for sp in item.special_property] + ['Critique : [{}]'.format(item.attack.critical)]
        },
        'dead-scourge': {
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='dead-scourge', count=1)],
            'magical_levels': 1,
            'name': lambda item, magical_level: "{}, fléau des morts".format(item.name),
            'short_description': lambda item, magical_level: "{} Cette arme augmente les dégâts faits aux "
                                                             "morts-vivants.".format(item.short_description),
            'full_description': lambda item, magical_level: "{} Cette arme augmente les dégâts de +1d6 face aux "
                                                            "morts-vivants.".format(
                item.full_description),
            'cost': lambda item, magical_level: cof.properties.Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'attack': lambda item, magical_level: None if item.attack is None else Attack(
                atype=item.attack.atype,
                name=item.attack.name,
                mod=item.attack.mod,
                damages=Damage(
                    base=[bdm for bdm in item.attack.damages.base],
                    other=[odm for odm in item.attack.damages.other] +
                          [Mod(target="dead", mtype="+", count=1, die=6,
                               limitation="Seulement contre les morts-vivants")]
                ),
                range=None if item.attack.range is None else Range(value=item.attack.range.value,
                                                                   unit=item.attack.range.unit),
                area=None if item.attack.area is None else Area(value=item.attack.area.value,
                                                                unit=item.attack.area.unit),
                critical=item.attack.critical.union(RangeSet())
            )
        },
        'dragon-scourge': {
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='dragon-scourge', count=1)],
            'magical_levels': 1,
            'name': lambda item, magical_level: "{}, fléau des dragons".format(item.name),
            'short_description': lambda item, magical_level: "{} Cette arme augmente les dégâts faits aux "
                                                             "dragons.".format(item.short_description),
            'full_description': lambda item, magical_level: "{} Cette arme augmente les dégâts de +1d6 face aux "
                                                            "dragons.".format(
                item.full_description),
            'cost': lambda item, magical_level: cof.properties.Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'attack': lambda item, magical_level: None if item.attack is None else Attack(
                atype=item.attack.atype,
                name=item.attack.name,
                mod=item.attack.mod,
                damages=Damage(
                    base=[bdm for bdm in item.attack.damages.base],
                    other=[odm for odm in item.attack.damages.other] +
                          [Mod(target="dragon", mtype="+", count=1, die=6, limitation="Seulement contre les dragons")]
                ),
                range=None if item.attack.range is None else Range(value=item.attack.range.value,
                                                                   unit=item.attack.range.unit),
                area=None if item.attack.area is None else Area(value=item.attack.area.value,
                                                                unit=item.attack.area.unit),
                critical=item.attack.critical.union(RangeSet())
            )
        },
        'giant-scourge': {
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'magical_levels': 1,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='giant-scourge', count=1)],
            'name': lambda item, magical_level: "{}, fléau des géants".format(item.name),
            'short_description': lambda item, magical_level: "{} Cette arme augmente les dégâts faits aux "
                                                             "géants.".format(item.short_description),
            'full_description': lambda item, magical_level: "{} Cette arme augmente les dégâts de +1d6 face aux "
                                                            "géants.".format(
                item.full_description),
            'cost': lambda item, magical_level: cof.properties.Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'attack': lambda item, magical_level: None if item.attack is None else Attack(
                atype=item.attack.atype,
                name=item.attack.name,
                mod=item.attack.mod,
                damages=Damage(
                    base=[bdm for bdm in item.attack.damages.base],
                    other=[odm for odm in item.attack.damages.other] +
                          [Mod(target="giant", mtype="+", count=1, die=6, limitation="Seulement contre les géants")]
                ),
                range=None if item.attack.range is None else Range(value=item.attack.range.value,
                                                                   unit=item.attack.range.unit),
                area=None if item.attack.area is None else Area(value=item.attack.area.value,
                                                                unit=item.attack.area.unit),
                critical=item.attack.critical.union(RangeSet())
            )
        },
        'goblin-scourge': {
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'magical_levels': 1,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='goblin-scourge', count=1)],
            'name': lambda item, magical_level: "{}, fléau des goblinoïdes".format(item.name),
            'short_description': lambda item, magical_level: "{} Cette arme augmente les dégâts faits aux "
                                                             "goblinoïdes.".format(item.short_description),
            'full_description': lambda item, magical_level: "{} Cette arme augmente les dégâts de +1d6 face aux "
                                                            "goblinoïdes.".format(
                item.full_description),
            'cost': lambda item, magical_level: cof.properties.Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'attack': lambda item, magical_level: None if item.attack is None else Attack(
                name=item.attack.name,
                atype=item.attack.atype,
                mod=item.attack.mod,
                damages=Damage(
                    base=[bdm for bdm in item.attack.damages.base],
                    other=[odm for odm in item.attack.damages.other] +
                          [Mod(target="goblin", mtype="+", count=1, die=6, limitation="Seulement contre les gobelins")]
                ),
                range=None if item.attack.range is None else Range(value=item.attack.range.value,
                                                                   unit=item.attack.range.unit),
                area=None if item.attack.area is None else Area(value=item.attack.area.value,
                                                                unit=item.attack.area.unit),
                critical=item.attack.critical.union(RangeSet())
            )
        },
        'daemon-scourge': {
            'category': lambda item, magical_level: 'Magique',
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'magical_levels': 1,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='daemon-scourge', count=1)],
            'name': lambda item, magical_level: "{}, fléau des démons".format(item.name),
            'short_description': lambda item, magical_level: "{} Cette arme augmente les dégâts faits aux "
                                                             "démons.".format(item.short_description),
            'full_description': lambda item, magical_level: "{} Cette arme augmente les dégâts de +1d6 face aux "
                                                            "démons.".format(
                item.full_description),
            'cost': lambda item, magical_level: cof.properties.Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'attack': lambda item, magical_level: None if item.attack is None else Attack(
                atype=item.attack.atype,
                name=item.attack.name,
                mod=item.attack.mod,
                damages=Damage(
                    base=[bdm for bdm in item.attack.damages.base],
                    other=[odm for odm in item.attack.damages.other] +
                          [Mod(target="daemon", mtype="+", count=1, die=6, limitation="Seulement contre les démons")]
                ),
                range=None if item.attack.range is None else Range(value=item.attack.range.value,
                                                                   unit=item.attack.range.unit),
                area=None if item.attack.area is None else Area(value=item.attack.area.value,
                                                                unit=item.attack.area.unit),
                critical=item.attack.critical.union(RangeSet())
            )
        },
        'fire': {
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'magical_levels': 2,
            'name': lambda item, magical_level: "{}, de feu".format(item.name),
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='fire', count=1)],
            'short_description': lambda item, magical_level: "{} Cette arme fait des dégâts supplémentaires de "
                                                             "feu.".format(item.short_description),
            'full_description': lambda item, magical_level: "{} Cette arme fait des dégâts supplémentaires de "
                                                            "+1d6 DM de feu.".format(item.full_description),
            'cost': lambda item, magical_level: cof.properties.Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'attack': lambda item, magical_level: None if item.attack is None else Attack(
                atype=item.attack.atype,
                name=item.attack.name,
                mod=item.attack.mod,
                damages=Damage(
                    base=[bdm for bdm in item.attack.damages.base],
                    other=[odm for odm in item.attack.damages.other] + [Mod(target="fire", mtype="+", count=1, die=6)]
                ),
                range=None if item.attack.range is None else Range(value=item.attack.range.value,
                                                                   unit=item.attack.range.unit),
                area=None if item.attack.area is None else Area(value=item.attack.area.value,
                                                                unit=item.attack.area.unit),
                critical=item.attack.critical.union(RangeSet())
            )
        },
        'serious-fire': {
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'magical_levels': 6,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='fire', count=2)],
            'name': lambda item, magical_level: "{}, de feu intense".format(item.name),
            'short_description': lambda item, magical_level: "{} Cette arme fait d'énormes dégâts supplémentaires "
                                                             "de feu.".format(item.short_description),
            'full_description': lambda item, magical_level: "{} Cette arme fait d'énormes dégâts supplémentaires "
                                                            "de +2d6 DM de feu.".format(item.full_description),
            'cost': lambda item, magical_level: cof.properties.Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'attack': lambda item, magical_level: None if item.attack is None else Attack(
                atype=item.attack.atype,
                mod=item.attack.mod,
                name=item.attack.name,
                damages=Damage(
                    base=[bdm for bdm in item.attack.damages.base],
                    other=[odm for odm in item.attack.damages.other] + [Mod(target="fire", mtype="+", count=2, die=6)]
                ),
                range=None if item.attack.range is None else Range(value=item.attack.range.value,
                                                                   unit=item.attack.range.unit),
                area=None if item.attack.area is None else Area(value=item.attack.area.value,
                                                                unit=item.attack.area.unit),
                critical=item.attack.critical.union(RangeSet())
            )
        },
        'lightning': {
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'magical_levels': 2,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='lightning', count=1)],
            'name': lambda item, magical_level: "{}, de foudre".format(item.name),
            'short_description': lambda item, magical_level: "{} Cette arme fait des dégâts supplémentaires de "
                                                             "foudre.".format(item.short_description),
            'full_description': lambda item, magical_level: "{} Cette arme fait des dégâts supplémentaires de "
                                                            "+1d6 DM de foudre.".format(item.full_description),
            'cost': lambda item, magical_level: cof.properties.Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'attack': lambda item, magical_level: None if item.attack is None else Attack(
                atype=item.attack.atype,
                name=item.attack.name,
                mod=item.attack.mod,
                damages=Damage(
                    base=[bdm for bdm in item.attack.damages.base],
                    other=[odm for odm in item.attack.damages.other] +
                          [Mod(target="lightning", mtype="+", count=1, die=6)]
                ),
                range=None if item.attack.range is None else Range(value=item.attack.range.value,
                                                                   unit=item.attack.range.unit),
                area=None if item.attack.area is None else Area(value=item.attack.area.value,
                                                                unit=item.attack.area.unit),
                critical=item.attack.critical.union(RangeSet())
            )
        },
        'serious-lightning': {
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'magical_levels': 6,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='lightning', count=2)],
            'name': lambda item, magical_level: "{}, de foudre intense".format(item.name),
            'short_description': lambda item, magical_level: "{} Cette arme fait d'énormes dégâts supplémentaires "
                                                             "de foudre.".format(item.short_description),
            'full_description': lambda item, magical_level: "{} Cette arme fait d'énormes dégâts supplémentaires "
                                                            "de +2d6 DM de foudre.".format(item.full_description),
            'cost': lambda item, magical_level: cof.properties.Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'attack': lambda item, magical_level: None if item.attack is None else Attack(
                atype=item.attack.atype,
                name=item.attack.name,
                mod=item.attack.mod,
                damages=Damage(
                    base=[bdm for bdm in item.attack.damages.base],
                    other=[odm for odm in item.attack.damages.other] +
                          [Mod(target="lightning", mtype="+", count=2, die=6)]
                ),
                range=None if item.attack.range is None else Range(value=item.attack.range.value,
                                                                   unit=item.attack.range.unit),
                area=None if item.attack.area is None else Area(value=item.attack.area.value,
                                                                unit=item.attack.area.unit),
                critical=item.attack.critical.union(RangeSet())
            )
        },
        'coldness': {
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'magical_levels': 2,
            'name': lambda item, magical_level: "{}, de froid".format(item.name),
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='coldness', count=1)],
            'short_description': lambda item, magical_level: "{} Cette arme fait des dégâts supplémentaires de "
                                                             "froid.".format(item.short_description),
            'full_description': lambda item, magical_level: "{} Cette arme fait des dégâts supplémentaires de "
                                                            "+1d6 DM de froid.".format(item.full_description),
            'cost': lambda item, magical_level: cof.properties.Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'attack': lambda item, magical_level: None if item.attack is None else Attack(
                atype=item.attack.atype,
                name=item.attack.name,
                mod=item.attack.mod,
                damages=Damage(
                    base=[bdm for bdm in item.attack.damages.base],
                    other=[odm for odm in item.attack.damages.other] +
                          [Mod(target="coldness", mtype="+", count=1, die=6)]
                ),
                range=None if item.attack.range is None else Range(value=item.attack.range.value,
                                                                   unit=item.attack.range.unit),
                area=None if item.attack.area is None else Area(value=item.attack.area.value,
                                                                unit=item.attack.area.unit),
                critical=item.attack.critical.union(RangeSet())
            )
        },
        'serious-coldness': {
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'magical_levels': 6,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='coldness', count=2)],
            'name': lambda item, magical_level: "{}, de froid intense".format(item.name),
            'short_description': lambda item, magical_level: "{} Cette arme fait d'énormes dégâts supplémentaires "
                                                             "de froid.".format(item.short_description),
            'full_description': lambda item, magical_level: "{} Cette arme fait d'énormes dégâts supplémentaires "
                                                            "de +2d6 DM de froid.".format(item.full_description),
            'cost': lambda item, magical_level: cof.properties.Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'attack': lambda item, magical_level: None if item.attack is None else Attack(
                atype=item.attack.atype,
                name=item.attack.name,
                mod=item.attack.mod,
                damages=Damage(
                    base=[bdm for bdm in item.attack.damages.base],
                    other=[odm for odm in item.attack.damages.other] +
                          [Mod(target="coldness", mtype="+", count=2, die=6)]
                ),
                range=None if item.attack.range is None else Range(value=item.attack.range.value,
                                                                   unit=item.attack.range.unit),
                area=None if item.attack.area is None else Area(value=item.attack.area.value,
                                                                unit=item.attack.area.unit),
                critical=item.attack.critical.union(RangeSet())
            )
        },
        'acid': {
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'magical_levels': 2,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='acid', count=1)],
            'name': lambda item, magical_level: "{}, d'acide".format(item.name),
            'short_description': lambda item, magical_level: "{} Cette arme fait des dégâts supplémentaires "
                                                             "d'acide.".format(item.short_description),
            'full_description': lambda item, magical_level: "{} Cette arme fait des dégâts supplémentaires de "
                                                            "+1d6 DM d'acide.".format(item.full_description),
            'cost': lambda item, magical_level: cof.properties.Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'attack': lambda item, magical_level: None if item.attack is None else Attack(
                atype=item.attack.atype,
                name=item.attack.name,
                mod=item.attack.mod,
                damages=Damage(
                    base=[bdm for bdm in item.attack.damages.base],
                    other=[odm for odm in item.attack.damages.other] + [Mod(target="acid", mtype="+", count=1, die=6)]
                ),
                range=None if item.attack.range is None else Range(value=item.attack.range.value,
                                                                   unit=item.attack.range.unit),
                area=None if item.attack.area is None else Area(value=item.attack.area.value,
                                                                unit=item.attack.area.unit),
                critical=item.attack.critical.union(RangeSet())
            )
        },
        'serious-acid': {
            'category': lambda item, magical_level: 'Magique',
            'material': lambda item, magical_level: item.material,
            'magical_levels': 6,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='acid', count=2)],
            'name': lambda item, magical_level: "{}, d'acide intense".format(item.name),
            'short_description': lambda item, magical_level: "{} Cette arme fait d'énormes dégâts supplémentaires "
                                                             "d'acide.".format(item.short_description),
            'full_description': lambda item, magical_level: "{} Cette arme fait d'énormes dégâts supplémentaires "
                                                            "de +2d6 DM d'acide.".format(item.full_description),
            'cost': lambda item, magical_level: cof.properties.Cost(
                value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
                unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'attack': lambda item, magical_level: None if item.attack is None else Attack(
                atype=item.attack.atype,
                name=item.attack.name,
                mod=item.attack.mod,
                damages=Damage(
                    base=[bdm for bdm in item.attack.damages.base],
                    other=[odm for odm in item.attack.damages.other] + [Mod(target="acid", mtype="+", count=2, die=6)]
                ),
                range=None if item.attack.range is None else Range(value=item.attack.range.value,
                                                                   unit=item.attack.range.unit),
                area=None if item.attack.area is None else Area(value=item.attack.area.value,
                                                                unit=item.attack.area.unit),
                critical=item.attack.critical.union(RangeSet())
            )
        },
        'silver': {
            'category': lambda item, magical_level: 'Bazar du bizarre',
            'material': lambda item, magical_level: 'silver',
            'magical_levels': 0,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='silver', count=1)],
            'name': lambda item, magical_level: "{}, en argent alchimique".format(item.name),
            'short_description': lambda item, magical_level: "{} Cette arme double les dégâts contre les "
                                                             "lycanthropes.".format(
                item.short_description),
            'full_description': lambda item, magical_level: "{} Cette arme est en argent et double les dégâts contre "
                                                            "les lycanthropes et autres créatures sensibles à "
                                                            "l'argent. L'arme ignore "
                                                            "également la RD d'une telle créature.".format(
                item.full_description),
            'cost': lambda item, magical_level: cof.properties.Cost(
                value=(config.cofConfig.config['global']['cost']['silver'] *
                       max_dm(item.attack.damages) + item.cost.iso().value),
                unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'special_property': lambda item, magical_level: [sp for sp in item.special_property] +
                                                            ["DM: x2 (sensible à l'argent)",
                                                             "RD: ignoré (sensible à l'agent)"]
        },
        'cold-iron': {
            'category': lambda item, magical_level: 'Bazar du bizarre',
            'material': lambda item, magical_level: 'cold-iron',
            'magical_levels': 0,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='cold-iron', count=1)],
            'name': lambda item, magical_level: "{}, en fer froid".format(item.name),
            'short_description': lambda item, magical_level: "{} Cette arme en fer froid double les dégâts contre "
                                                             "les fées et les démons.".format(
                item.short_description),
            'full_description': lambda item, magical_level: "{} Cette arme est en fer froid et double les dégâts "
                                                            "contre les fées et les démons.".format(
                item.full_description),
            'cost': lambda item, magical_level: cof.properties.Cost(
                value=(config.cofConfig.config['global']['cost']['cold-iron'] *
                       max_dm(item.attack.damages) + item.cost.iso().value),
                unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'special_property': lambda item, magical_level: [sp for sp in item.special_property] +
                                                            ["DM: x2 (fées et démons)"]
        },
        'durium': {
            'category': lambda item, magical_level: 'Bazar du bizarre',
            'material': lambda item, magical_level: 'durium',
            'magical_levels': 0,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='durium', count=1)],
            'name': lambda item, magical_level: "{}, en durium".format(item.name),
            'short_description': lambda item, magical_level: "{} Cette arme augmente le dé de dégâts avec une "
                                                             "légère pénalité.".format(item.short_description),
            'full_description': lambda item, magical_level: "{} Cette arme est faite en durium, un métal bleu sombre "
                                                            "très dur et particulièrement lourd. Elle impose un malus "
                                                            "de -1 en attaque, mais augmente le dé de DM d'une "
                                                            "catégorie (d4->d6->d8->d10->d12) et elles sont presque "
                                                            "indestructibles. Le durium réduit d'un facteur 2 la "
                                                            "portée de cet arme.".format(item.full_description)
            if item.attack.range is not None else "{} Cette arme est faite en durium, un métal bleu sombre "
                                                            "très dur et particulièrement lourd. Elle impose un malus "
                                                            "de -1 en attaque, mais augmente le dé de DM d'une "
                                                            "catégorie (d4->d6->d8->d10->d12) et elles sont presque "
                                                            "indestructibles.".format(item.full_description),
            'cost': lambda item, magical_level: cof.properties.Cost(
                value=(config.cofConfig.config['global']['cost']['durium'] *
                       max_dm(item.attack.damages) + item.cost.iso().value),
                unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'attack': lambda item, magical_level: None if item.attack is None else Attack(
                atype=item.attack.atype,
                name=item.attack.name,
                mod=item.attack.mod - 1,
                damages=Damage(
                    base=increase_dice([bdm for bdm in item.attack.damages.base]),
                    other=[odm for odm in item.attack.damages.other]
                ),
                range=None if item.attack.range is None else Range(value=item.attack.range.value / 2,
                                                                   unit=item.attack.range.unit),
                area=None if item.attack.area is None else Area(value=item.attack.area.value,
                                                                unit=item.attack.area.unit),
                critical=item.attack.critical.union(RangeSet())
            ),
        },
        'mythral': {
            'category': lambda item, magical_level: 'Bazar du bizarre',
            'material': lambda item, magical_level: 'mythral',
            'magical_levels': 0,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='mythral', count=1)],
            'name': lambda item, magical_level: "{}, en mythral".format(item.name),
            'short_description': lambda item, magical_level: "{} Cette arme augmente le bonus de +1 en "
                                                             "attaque.".format(item.short_description),
            'full_description': lambda item, magical_level: "{} Cette arme est faite en mythral, un métal très léger "
                                                            "de couleur argent. Les armes bénéficient d'un bonus de +1 "
                                                            "en attaque car elles sont beaucoup plus "
                                                            "maniables.".format(item.full_description),
            'attack': lambda item, magical_level: None if item.attack is None else Attack(
                atype=item.attack.atype,
                name=item.attack.name,
                mod=item.attack.mod + 1,
                damages=Damage(
                    base=[bdm for bdm in item.attack.damages.base],
                    other=[odm for odm in item.attack.damages.other]
                ),
                range=None if item.attack.range is None else Range(value=item.attack.range.value,
                                                                   unit=item.attack.range.unit),
                area=None if item.attack.area is None else Area(value=item.attack.area.value,
                                                                unit=item.attack.area.unit),
                critical=item.attack.critical.union(RangeSet())
            ),
            'cost': lambda item, magical_level: cof.properties.Cost(
                value=(config.cofConfig.config['global']['cost']['mythral'] *
                       max_dm(item.attack.damages) + item.cost.iso().value),
                unit=config.cofConfig.config['global']['cost']['unit']).iso()
        },
        'lothar': {
            'category': lambda item, magical_level: 'Bazar du bizarre',
            'material': lambda item, magical_level: 'lothar',
            'magical_levels': 0,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='lothar', count=1)],
            'exclude': lothar_exclude_weapons,
            'name': lambda item, magical_level: "{}, en lothar".format(item.name),
            'short_description': lambda item, magical_level: "{} Cette arme augmente les  critiques "
                                                             "de 1.".format(item.short_description),
            'full_description': lambda item, magical_level: "{} Cette arme est faite en lothar, un métal doré "
                                                            "qui a la particularité d'être très souple. Cela lui "
                                                            "permet de vrier dans le blessures et de se tordre pour "
                                                            "continuer sa trajectoire lorsqu'il rencontre un os."
                                                            "Les armes faite en lothar voient leur zone de critique "
                                                            "augmentée d'un point.".format(item.full_description),
            'attack': lambda item, magical_level: None if item.attack is None else Attack(
                atype=item.attack.atype,
                name=item.attack.name,
                mod=item.attack.mod,
                damages=Damage(
                    base=[bdm for bdm in item.attack.damages.base],
                    other=[odm for odm in item.attack.damages.other]
                ),
                range=None if item.attack.range is None else Range(value=item.attack.range.value,
                                                                   unit=item.attack.range.unit),
                area=None if item.attack.area is None else Area(value=item.attack.area.value,
                                                                unit=item.attack.area.unit),
                critical=RangeSet("{}-{}".format(item.attack.critical[0]-1, item.attack.critical[-1]))
            ),
            'cost': lambda item, magical_level: cof.properties.Cost(
                value=(config.cofConfig.config['global']['cost']['lothar'] *
                       max_dm(item.attack.damages) + item.cost.iso().value),
                unit=config.cofConfig.config['global']['cost']['unit']).iso()
        },
        'adamantium': {
            'category': lambda item, magical_level: 'Bazar du bizarre',
            'material': lambda item, magical_level: 'adamantium',
            'magical_levels': 0,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='adamantium', count=1)],
            'name': lambda item, magical_level: "{}, en adamantium".format(item.name),
            'short_description': lambda item, magical_level: "{} Cette arme ignore une partie de la RD de la "
                                                             "cible.".format(
                item.short_description),
            'full_description': lambda item, magical_level: "{} Cette arme est faite en adamantium, un métal d'une "
                                                            "dureté exceptionnelle. Le point de fusion de ce métal est "
                                                            "particulièrement élevé et le rend très difficile à "
                                                            "forger. Cette arme ignore 10 point de la RD des "
                                                            "structures et 5 points de la RD des "
                                                            "créatures.".format(
                item.full_description),
            'cost': lambda item, magical_level: cof.properties.Cost(
                value=(config.cofConfig.config['global']['cost']['adamantium'] *
                       max_dm(item.attack.damages) + item.cost.iso().value),
                unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'special_property': lambda item, magical_level: [sp for sp in item.special_property] +
                                                            ["RD (structures): Ignore 10 pts",
                                                             "RD (créatures): Ignore 5 pts"]
        },
        'sombracier': {
            'category': lambda item, magical_level: 'Bazar du bizarre',
            'material': lambda item, magical_level: 'sombracier',
            'magical_levels': 0,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='sombracier', count=1)],
            'name': lambda item, magical_level: "{}, en sombracier".format(item.name),
            'short_description': lambda item, magical_level: "{} Cette arme ignore les protections magiques de la "
                                                             "cible.".format(
                item.short_description),
            'full_description': lambda item, magical_level: "{} Cette arme est faite en sombracier, un métal lourd "
                                                            "presque noir imperméable à la magie. Ce métal très rare "
                                                            "passe à travers tous les sorts de protection et ignore "
                                                            "les bonus de magie des armures ou ceux accordés par "
                                                            "les sorts. Cette arme est insensible à la magie et ne "
                                                            "peut être téléportée, rendu invisible, etc... Elle "
                                                            "confère cependant un bonus à ses tests et à sa DEF "
                                                            "contre la magie de +{}.".format(
                item.full_description, weapon_size[get_size(item)]['bonus-defense-magique']),
            'cost': lambda item, magical_level: cof.properties.Cost(
                value=(config.cofConfig.config['global']['cost']['sombracier'] *
                       max_dm(item.attack.damages) + item.cost.iso().value),
                unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'special_property': lambda item, magical_level: [sp for sp in item.special_property] +
                                                            ["DEF (résistance à la magie) : +{}".format(
                                                                weapon_size[get_size(item)]['bonus-defense-magique']),
                                                             "Tests (resistance à la magie) : +{}".format(
                                                                weapon_size[get_size(item)]['bonus-defense-magique'])]
        },
        'laenk': {
            'category': lambda item, magical_level: 'Bazar du bizarre',
            'material': lambda item, magical_level: 'laenk',
            'magical_levels': 0,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='laenk', count=1)],
            'name': lambda item, magical_level: "{}, en laënk".format(item.name),
            'short_description': lambda item, magical_level: "{} Cette arme émet de la lumière lorsqu'il fait "
                                                             "noir.".format(
                item.short_description),
            'full_description': lambda item, magical_level: "{} Cette arme est faite en laënk, un métal argenté "
                                                            "précieux qui émet de la lumière lorsqu'il fait noir. La "
                                                            "zone éclairée est de {} m.".format(
                item.full_description, weapon_size[get_size(item)]['zone-lumiere']),
            'cost': lambda item, magical_level: cof.properties.Cost(
                value=(config.cofConfig.config['global']['cost']['laenk'][get_size(item)] *
                       max_dm(item.attack.damages) + item.cost.iso().value),
                unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'special_property': lambda item, magical_level: [sp for sp in item.special_property] +
                                                            ["Lumière: {} m".format(
                                                                weapon_size[get_size(item)]['zone-lumiere'])]
        },
        'xylene': {
            'category': lambda item, magical_level: 'Bazar du bizarre',
            'material': lambda item, magical_level: 'xylene',
            'magical_levels': 0,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='xylene', count=1)],
            'name': lambda item, magical_level: "{}, en xylène".format(item.name),
            'short_description': lambda item, magical_level: "{} Cette arme fait +1d4 DM d'électricité contre les "
                                                             "armures de métal.".format(item.short_description),
            'full_description': lambda item, magical_level: "{} Cette arme est faite en xylène, un métal naturellement "
                                                            "magique qui a la propriété de produire des décharges "
                                                            "électriques lorsqu'on le frappe sur un autre métal. "
                                                            "Contre tout adversaire qui porte une armure de métal, "
                                                            "une telle arme occasionne +1d4 de DM "
                                                            "d'électricité.".format(item.full_description),
            'attack': lambda item, magical_level: None if item.attack is None else Attack(
                atype=item.attack.atype,
                name=item.attack.name,
                mod=item.attack.mod,
                damages=Damage(
                    base=[bdm for bdm in item.attack.damages.base],
                    other=[odm for odm in item.attack.damages.other] +
                          [Mod(target="lightning", mtype="+", die=4,
                               count=1, limitation="Seulement contre armure de métal")]
                ),
                range=None if item.attack.range is None else Range(value=item.attack.range.value,
                                                                   unit=item.attack.range.unit),
                area=None if item.attack.area is None else Area(value=item.attack.area.value,
                                                                unit=item.attack.area.unit),
                critical=item.attack.critical
            ),
            'cost': lambda item, magical_level: cof.properties.Cost(
                value=(config.cofConfig.config['global']['cost']['xylene'] *
                       max_dm(item.attack.damages) + item.cost.iso().value),
                unit=config.cofConfig.config['global']['cost']['unit']).iso(),
        },
        'phospharium': {
            'category': lambda item, magical_level: 'Bazar du bizarre',
            'material': lambda item, magical_level: 'phospharium',
            'magical_levels': 0,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='phospharium', count=1)],
            'name': lambda item, magical_level: "{}, en phospharium".format(item.name),
            'short_description': lambda item, magical_level: "{} Cette arme fait +1d4 DM de feu et peut servir "
                                                             "d'éclairage.".format(
                item.short_description),
            'full_description': lambda item, magical_level: "{} Cette arme est faite en phospharium, un métal "
                                                            "naturellement magique qui a la propriété de devenir "
                                                            "brûlant au contact de l'air, produisant même quelques "
                                                            "flamèches. Elle est fournie avec un épais étui si ajusté "
                                                            "que lorsque l'arme est au fourreau elle est tiède. "
                                                            "L'arme occasionne +1d4 de DM de feu. Elle peut également "
                                                            "servir d'éclairage et éclaire dans ce cas une zone "
                                                            "de {} m.".format(
                item.full_description, weapon_size[get_size(item)]['zone-lumiere']),
            'attack': lambda item, magical_level: None if item.attack is None else Attack(
                atype=item.attack.atype,
                name=item.attack.name,
                mod=item.attack.mod,
                damages=Damage(
                    base=[bdm for bdm in item.attack.damages.base],
                    other=[odm for odm in item.attack.damages.other] +
                          [Mod(target="fire", mtype="+", die=4,
                               count=1)]
                ),
                range=None if item.attack.range is None else Range(value=item.attack.range.value,
                                                                   unit=item.attack.range.unit),
                area=None if item.attack.area is None else Area(value=item.attack.area.value,
                                                                unit=item.attack.area.unit),
                critical=item.attack.critical
            ),
            'cost': lambda item, magical_level: cof.properties.Cost(
                value=(config.cofConfig.config['global']['cost']['phospharium'] *
                       max_dm(item.attack.damages) + item.cost.iso().value),
                unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'special_property': lambda item, magical_level: [sp for sp in item.special_property] +
                                                            ["Lumière : {} m".format(
                                                                weapon_size[get_size(item)]['zone-lumiere'])]
        },
        'hybberium': {
            'category': lambda item, magical_level: 'Bazar du bizarre',
            'material': lambda item, magical_level: 'hybberium',
            'magical_levels': 0,
            'flavor': lambda item, magical_level: item.flavor + [Flavor(ftype='hybberium', count=1)],
            'name': lambda item, magical_level: "{}, en hybberium".format(item.name),
            'short_description': lambda item, magical_level: "{} Cette arme fait +1d4 DM de froid.".format(
                item.short_description),
            'full_description': lambda item, magical_level: "{} Cette arme est faite en hybberium, un métal "
                                                            "naturellement magique qui a la propriété de devenir "
                                                            "glacial au contact de l'air, produisant du givre. "
                                                            "Elle est fournie avec un épais étui et, à l'air libre, "
                                                            "elle occasionne +1d4 de DM de froid.".format(
                item.full_description, weapon_size[get_size(item)]['zone-lumiere']),
            'attack': lambda item, magical_level: None if item.attack is None else Attack(
                atype=item.attack.atype,
                name=item.attack.name,
                mod=item.attack.mod,
                damages=Damage(
                    base=[bdm for bdm in item.attack.damages.base],
                    other=[odm for odm in item.attack.damages.other] +
                          [Mod(target="coldness", mtype="+", die=4,
                               count=1)]
                ),
                range=None if item.attack.range is None else Range(value=item.attack.range.value,
                                                                   unit=item.attack.range.unit),
                area=None if item.attack.area is None else Area(value=item.attack.area.value,
                                                                unit=item.attack.area.unit),
                critical=item.attack.critical
            ),
            'cost': lambda item, magical_level: cof.properties.Cost(
                value=(config.cofConfig.config['global']['cost']['hybberium'] *
                       max_dm(item.attack.damages) + item.cost.iso().value),
                unit=config.cofConfig.config['global']['cost']['unit']).iso(),
        },
    },
    'addons': {
        'baton': {
            'category': 'Standard',
            'base_item': 'baton',
            'full_description': "Un simple bâton en bois. Une arme rudimentaire mais relativement efficace vu "
                                "son prix. Très maniable, il s'utilise à 2 mains. Il inflige 1d4 dégâts qui "
                                "peuvent être temporaires si son porteur le décide.",
            'short_description': "Un simple bâton en bois.",
            'weight': cof.properties.Weight(value=1.0, unit='Kg'),
            'hands': 2,
            'attack': Attack(
                atype='melee',
                damages=Damage(
                    base=[Mod(die=4, count=1, target=['blunt'])],
                    other=[]
                ),
                critical=RangeSet([20])
            ),
            'material': 'wood',
            'special_property': ['Les dégats peuvent être temporaires']
        },
        'baton-ferre': {
            'category': 'Standard',
            'base_item': 'baton-ferre',
            'full_description': "Un bâton en bois renforcé en plusieurs endroits par de petites lanières de fer. "
                                "Une arme efficace vu son prix. Très maniable, il s'utilise à 2 mains. Il "
                                "inflige 1d6 dégâts.",
            'short_description': "Un bâton en bois renforcé en plusieurs endroits par de petites lanières de fer.",
            'weight': cof.properties.Weight(value=1.0, unit='Kg'),
            'hands': 2,
            'attack': Attack(
                atype='melee',
                damages=Damage(
                    base=[Mod(die=6, count=1, target=['blunt'])],
                    other=[]
                ),
                critical=RangeSet([20])
            ),
            'special_property': []

        },
        'dague': {
            'category': 'Standard',
            'base_item': 'dague',
            'full_description': "Une arme blanche à simple ou double tranchant dont la pointe en forme de losange, "
                                "et de préférence symétrique, améliore le pouvoir de perforation. Cette arme à une "
                                "main inflige 1d4 dégâts.",
            'short_description': "Une arme blanche à simple ou double tranchant.",
            'weight': cof.properties.Weight(value=0.5, unit='Kg'),
            'hands': 1,
            'attack': Attack(
                atype='melee',
                damages=Damage(
                    base=[Mod(die=4, count=1, target=['punctured', 'sharp'])],
                    other=[]
                ),
                critical=RangeSet([20])
            ),
            'special_property': []
        },
        'epee-a-2-mains': {
            'category': 'Standard',
            'base_item': 'epee-a-2-mains',
            'full_description': "L'épée à deux mains est une arme blanche à double tranchant utilisée pour faucher"
                                "dans les lignes ennemies. Cette arme à 2 mains inflige 2d6 de dégâts.",
            'short_description': "L'épée à deux mains est une arme blanche à double tranchant utilisée pour faucher"
                                "dans les lignes ennemies.",
            'weight': cof.properties.Weight(value=3.0, unit='Kg'),
            'hands': 2,
            'attack': Attack(
                atype='melee',
                damages=Damage(
                    base=[Mod(die=6, count=2, target=['punctured', 'sharp'])],
                    other=[]
                ),
                critical=RangeSet([20])
            ),
            'special_property': []
        },
        'epee-batarde': {
            'category': 'Standard',
            'base_item': 'epee-batarde',
            'full_description': "L'épée batarde est un compromis entre l'épée longue et l'épée à 2 mains. Utilisée "
                                "à une main, cette arme inflige 1d8 dégâts. A 2 mains, elle inflige 1d12 dégâts.",
            'short_description': "L'épée batarde est un compromis entre l'épée longue et l'épée à 2 mains.",
            'weight': cof.properties.Weight(value=2.0, unit='Kg'),
            'hands': 3,
            'attack': Attack(
                atype='melee',
                damages=Damage(
                    base=[Mod(die=8, count=1, target=['punctured', 'sharp'])],
                    other=[]
                ),
                critical=RangeSet([20])
            ),
            'special_property': ["Inflige 1d12 DM si tenue à 2 mains"]
        },
        'epee-courte': {
            'category': 'Standard',
            'base_item': 'epee-courte',
            'full_description': "Plus petite que l'épée longue, mais aussi plus maniable, cette arme s'utilise à "
                                "une main et inflige 1d6 dégâts",
            'short_description': "Une épée plus courte qu'une épée classique.",
            'weight': cof.properties.Weight(value=1.0, unit='Kg'),
            'hands': 1,
            'attack': Attack(
                atype='melee',
                damages=Damage(
                    base=[Mod(die=6, count=1, target=['punctured', 'sharp'])],
                    other=[]
                ),
                critical=RangeSet([20])
            ),
            'special_property': []
        },
        'epee-longue': {
            'category': 'Standard',
            'base_item': 'epee-longue',
            'full_description': "Plus longue qu'une épée classique, elle reste une valeur sûre pour n'importe quel "
                                "aventurier souhaitant accomplir de hauts faîts. Elle s'utilise à une main et "
                                "inflige 1d8 dégâts.",
            'short_description': "Une épée plus longue qu'une épée classique.",
            'weight': cof.properties.Weight(value=1.5, unit='Kg'),
            'hands': 1,
            'attack': Attack(
                atype='melee',
                damages=Damage(
                    base=[Mod(die=8, count=1, target=['punctured', 'sharp'])],
                    other=[]
                ),
                critical=RangeSet([20])
            ),
            'special_property': []
        },
        'gourdin': {
            'category': 'Standard',
            'base_item': 'gourdin',
            'full_description': "Une arme rustique, le plus souvent en bois qui s'utilise à une main. Le gourdin "
                                "inflige 1d4 dégâts qui peuvent être temporaires si son porteur le décide.",
            'short_description': "Une arme rustique, le plus souvent en bois qui s'utilise à une main",
            'weight': cof.properties.Weight(value=1.0, unit='Kg'),
            'hands': 1,
            'attack': Attack(
                atype='melee',
                damages=Damage(
                    base=[Mod(die=4, count=1, target=['blunt'])],
                    other=[]
                ),
                critical=RangeSet([20])
            ),
            'special_property': ["Les dégats peuvent être temporaires"]
        },
        'hache-a-1-main': {
            'category': 'Standard',
            'base_item': 'hache-a-1-main',
            'full_description': "Une hache d'arme classique qui permet de tailler en pièce n'importe quel ennemie. "
                                "Elle s'utilise à une main et inflige 1d8 dégâts.",
            'short_description': "Une hache d'arme classique qui permet de tailler en pièce n'importe quel "
                                 "ennemie.",
            'weight': cof.properties.Weight(value=2.0, unit='Kg'),
            'hands': 1,
            'attack': Attack(
                atype='melee',
                damages=Damage(
                    base=[Mod(die=8, count=1, target=['sharp'])],
                    other=[]
                ),
                critical=RangeSet([20])
            ),
            'special_property': []
        },
        'hache-a-2-mains': {
            'category': 'Standard',
            'base_item': 'hache-a-2-mains',
            'full_description': "Une hache d'arme inposante qui peut désolidariser n'importe quelle tête d'un "
                                "corps en un seul coup. Elle s'utilise à 2 mains et inflige 2d6 dégâts. ",
            'short_description': "Une hache d'arme inposante qui peut désolidariser n'importe quelle tête d'un "
                                 "corps en un seul coup",
            'weight': cof.properties.Weight(value=3.5, unit='Kg'),
            'hands': 2,
            'attack': Attack(
                atype='melee',
                damages=Damage(
                    base=[Mod(die=6, count=2, target=['sharp'])],
                    other=[]
                ),
                critical=RangeSet([20])
            ),
            'special_property': []
        },
        'katana': {
            'category': 'Standard',
            'base_item': 'katana',
            'full_description': "Le katana est une arme blanche courbe à un seul tranchant. Le katana est une "
                                "arme de taille (dont on utilise le tranchant) et d'estoc (dont on utilise la "
                                "pointe). Il s'utilise à 2 mains et inflige 1d10 dégâts (critiques sur 19-20).",
            'short_description': "Le katana est une arme blanche courbe à un seul tranchant.",
            'weight': cof.properties.Weight(value=1.5, unit='Kg'),
            'hands': 2,
            'attack': Attack(
                atype='melee',
                damages=Damage(
                    base=[Mod(die=10, count=1, target=['punctured', 'sharp'])],
                    other=[]
                ),
                critical=RangeSet([19, 20])
            ),
            'special_property': []
        },
        'marteau-de-guerre': {
            'category': 'Standard',
            'base_item': 'marteau-de-guerre',
            'full_description': "Le marteau de guerre est une arme offensive utilisée principalement contre les "
                                "armures. Le marteau de guerre peut fausser les articulations des armures, "
                                "empêchant ainsi certains mouvements. Il s'utilise à une main et inflige 1d6 "
                                "dégâts.",
            'short_description': "Le marteau de guerre est une arme offensive utilisée principalement contre les "
                                "armures.",
            'weight': cof.properties.Weight(value=1.0, unit='Kg'),
            'hands': 1,
            'attack': Attack(
                atype='melee',
                damages=Damage(
                    base=[Mod(die=6, count=1, target=['blunt'])],
                    other=[]
                ),
                critical=RangeSet([20])
            ),
            'special_property': []
        },
        'masse-d-armes': {
            'category': 'Standard',
            'base_item': 'masse-d-armes',
            'full_description': "La masse d'armes est une arme contondante constituée d'une masse lourde "
                                "accrochée au bout d'un bâton plus ou moins long. Ce fut l'une des premières armes "
                                "utilisées par l’humanité. Elle s'utilise à une main et inflige 1d6 dégâts.",
            'short_description': "La masse d'armes est une arme contondante constituée d'une masse lourde "
                                "accrochée au bout d'un bâton plus ou moins long.",
            'weight': cof.properties.Weight(value=2.0, unit='Kg'),
            'hands': 1,
            'attack': Attack(
                atype='melee',
                damages=Damage(
                    base=[Mod(die=6, count=1, target=['blunt'])],
                    other=[]
                ),
                critical=RangeSet([20])
            ),
            'special_property': []
        },
        'rapiere': {
            'category': 'Standard',
            'base_item': 'rapiere',
            'full_description': "La rapière est une épée longue et fine, à la garde élaborée, à la lame flexible, "
                                "destinée essentiellement aux coups d'estoc. La rapière, même si elle n'est pas "
                                "faite pour trancher un homme en deux, est affûtée, et peut causer de sérieuses "
                                "entailles si un coup à la volée atteint l'adversaire. Elle s'utilise à une "
                                "main et inflige 1d6 dégâts (critiques sur 19-20).",
            'short_description': "La rapière est une épée longue et fine, à la garde élaborée, à la lame "
                                 "flexible, destinée essentiellement aux coups d'estoc.",
            'weight': cof.properties.Weight(value=1.0, unit='Kg'),
            'hands': 1,
            'attack': Attack(
                atype='melee',
                damages=Damage(
                    base=[Mod(die=6, count=1, target=['punctured', 'sharp'])],
                    other=[]
                ),
                critical=RangeSet([19, 20])
            ),
            'special_property': []
        },
        'vivelame': {
            'category': 'Standard',
            'base_item': 'vivelame',
            'full_description': "La vivelame est un katana plus prestigieux que la normale avec de riches "
                                "ornements. Il s'utilise à 2 mains et inflige 1d10 dégâts (critiques sur 19-20).",
            'short_description': "La vivelame est un katana plus prestigieux que la normale avec de riches "
                                 "ornements.",
            'weight': cof.properties.Weight(value=1.5, unit='Kg'),
            'hands': 2,
            'attack': Attack(
                atype='melee',
                damages=Damage(
                    base=[Mod(die=10, count=1, target=['punctured', 'sharp'])],
                    other=[]
                ),
                critical=RangeSet([19, 20])
            ),
            'special_property': []
        },
        'arbalete-de-poing': {
            'category': 'Standard',
            'base_item': 'arbalete-de-poing',
            'full_description': "L'arbalète de poing est une petite arbalète qui se tient à une main. Elle peut "
                                "envoyer des projectiles jusqu'à 10m et se recharge en une action simple. Elle "
                                "inflige 1d6 dégâts.",
            'short_description': "L'arbalète de poing est une petite arbalète qui se tient à une main.",
            'weight': cof.properties.Weight(value=1.5, unit='Kg'),
            'hands': 1,
            'attack': Attack(
                atype='ranged',
                damages=Damage(
                    base=[Mod(die=6, count=1, target=['punctured'])],
                    other=[],
                ),
                range=Range(value=10, unit='m'),
                critical=RangeSet([20])
            ),
            'special_property': ["Une action d'attaque pour recharger"]
        },
        'arbalete-legere': {
            'category': 'Standard',
            'base_item': 'arbalete-legere',
            'full_description': "L'arbalète est une arme de trait, constituée d'un arc monté sur un fût et "
                                "lançant des projectiles appelés carreaux. Sa version légère se tient à 2 "
                                "mains, permet d'envoyer des projectiles jusqu'à 30m et se recharge en une "
                                "action simple. Elle inflige 2d4 dégâts.",
            'short_description': "L'arbalète lègère est une arme de trait à 2 mains lançant des projectiles "
                                 "appelés carreaux",
            'weight': cof.properties.Weight(value=2.5, unit='Kg'),
            'hands': 2,
            'attack': Attack(
                atype='ranged',
                damages=Damage(
                    base=[Mod(die=4, count=2, target=['punctured'])],
                    other=[],
                ),
                range=Range(value=30, unit='m'),
                critical=RangeSet([20])
            ),
            'special_property': ["Une action d'attaque pour recharger"]
        },
        'arbalete-lourde': {
            'category': 'Standard',
            'base_item': 'arbalete-lourde',
            'full_description': "L'arbalète est une arme de trait, constituée d'un arc monté sur un fût et "
                                "lançant des projectiles appelés carreaux. Sa version lourde se tient à 2 "
                                "mains, permet d'envoyer des projectiles jusqu'à 60m et se recharge en une "
                                "action limitée. Elle inflige 3d4 dégâts.",
            'short_description': "L'arbalète lourde est une arme de trait à 2 mains lançant des projectiles "
                                 "appelés carreaux",
            'weight': cof.properties.Weight(value=9.0, unit='Kg'),
            'hands': 2,
            'attack': Attack(
                atype='ranged',
                damages=Damage(
                    base=[Mod(die=4, count=3, target=['punctured'])],
                    other=[],
                ),
                range=Range(value=60, unit='m'),
                critical=RangeSet([20])
            ),
            'special_property': ["Une action d'attaque pour recharger"]
        },
        'arc-court': {
            'category': 'Standard',
            'base_item': 'arc-court',
            'full_description': "L'arc est une arme de trait à 2 mains destinée à lancer des flèches. Dans sa "
                                "version courte, il permet d'envoyer un projectile jusqu'à 30m et inflige "
                                "1d6 dégâts.",
            'short_description': "L'arc est une arme de trait à 2 mains destinée à lancer des flèches.",
            'weight': cof.properties.Weight(value=1.0, unit='Kg'),
            'hands': 2,
            'attack': Attack(
                atype='ranged',
                damages=Damage(
                    base=[Mod(die=6, count=1, target=['punctured'])],
                    other=[],
                ),
                range=Range(value=30, unit='m'),
                critical=RangeSet([20])
            ),
            'special_property': []
        },
        'arc-long': {
            'category': 'Standard',
            'base_item': 'arc-long',
            'full_description': "L'arc est une arme de trait à 2 mains destinée à lancer des flèches. Dans sa "
                                "version longue, il permet d'envoyer un projectile jusqu'à 50m et inflige "
                                "1d8 dégâts. Une force minimale (FOR > 13) est nécessaire pour manier un tel arc.",
            'short_description': "L'arc est une arme de trait à 2 mains destinée à lancer des flèches.",
            'weight': cof.properties.Weight(value=1.0, unit='Kg'),
            'hands': 2,
            'attack': Attack(
                atype='ranged',
                damages=Damage(
                    base=[Mod(die=8, count=1, target=['punctured'])],
                    other=[],
                ),
                range=Range(value=50, unit='m'),
                critical=RangeSet([20])
            ),
            'special_property': ["Utilisable par: FOR >= 13"]
        },
        'fronde': {
            'category': 'Standard',
            'base_item': 'fronde',
            'full_description': "La fronde est une arme individuelle de trait, constituée d’une poche "
                                "prolongée à chaque extrémité par des lanières, utilisée pour lancer "
                                "des projectiles (cailloux, balles de plomb, etc.) avec force jusqu'à 20m. Elle "
                                "s'utilise à une main et inflige 1d4 dégâts",
            'short_description': "La fronde est une arme qui permet de lancer de petits projectiles comme des "
                                 "cailloux",
            'weight': cof.properties.Weight(value=0.0, unit='Kg'),
            'hands': 2,
            'attack': Attack(
                atype='ranged',
                damages=Damage(
                    base=[Mod(die=4, count=1, target=['punctured'])],
                    other=[],
                ),
                range=Range(value=20, unit='m'),
                critical=RangeSet([20])
            ),
        },
        'hachette': {
            'category': 'Standard',
            'base_item': 'hachette',
            'full_description': "La hachette est une petite hache qui est très maniable. Elle peut être lancée "
                                "jusqu'à 5m. Elle se tient à une main et inflige 1d6 dégâts",
            'short_description': "La hachette est une petite hache qui est très maniable.",
            'weight': cof.properties.Weight(value=1.0, unit='Kg'),
            'hands': 1,
            'attack': Attack(
                atype='ranged',
                damages=Damage(
                    base=[Mod(die=6, count=1, target=['punctured'])],
                    other=[],
                ),
                range=Range(value=5, unit='m'),
                critical=RangeSet([20])
            ),
        },
        'javelot': {
            'category': 'Standard',
            'base_item': 'javelot',
            'full_description': "Un javelot est une arme de jet légère, semblable à une lance. Elle peut être "
                                "lancée jusqu'à 20m. Elle se tient à une main et inflige 1d6 dégâts",
            'short_description': "Un javelot est une arme de jet légère, semblable à une lance.",
            'weight': cof.properties.Weight(value=1.0, unit='Kg'),
            'hands': 1,
            'attack': Attack(
                atype='ranged',
                damages=Damage(
                    base=[Mod(die=6, count=1, target=['punctured'])],
                    other=[],
                ),
                range=Range(value=20, unit='m'),
                critical=RangeSet([20])
            ),
        },
        'mousquet': {
            'category': 'Standard',
            'base_item': 'mousquet',
            'full_description': "Un mousquet est une arme à feu portative dotée d'un long canon lisse, d'une crosse "
                                "d'épaule et d'un mécanisme de mise à feu à mèche. Le mousquet a été inventé pour pallier "
                                "le manque de puissance des arquebuses et pemet de tirer une cible jusqu'à 50m. "
                                "Il s'utilise à 2 mains et inflige 2d6 dégâts. Une action limitée est nécessaire "
                                "pour le recharger.",
            'short_description': "Un mousquet est une arme à feu portative au long canon.",
            'weight': cof.properties.Weight(value=2.0, unit='Kg'),
            'hands': 2,
            'attack': Attack(
                atype='ranged',
                damages=Damage(
                    base=[Mod(die=6, count=2, target=['punctured'])],
                    other=[],
                ),
                range=Range(value=50, unit='m'),
                critical=RangeSet([20])
            ),
        },
        'petoire': {
            'category': 'Standard',
            'base_item': 'petoire',
            'full_description': "Une pétoire est une sorte de pistolet. Il s'utilise à une main et permet de "
                                "tirer jusqu'à 20m. Une action limitée est nécessaire pour le recharger. Il "
                                "inflige 1d10 dégâts",
            'short_description': "Une pétoire est une sorte de pistolet.",
            'weight': cof.properties.Weight(value=0.5, unit='Kg'),
            'hands': 1,
            'attack': Attack(
                atype='ranged',
                damages=Damage(
                    base=[Mod(die=10, count=1, target=['punctured'])],
                    other=[],
                ),
                range=Range(value=20, unit='m'),
                critical=RangeSet([20])
            ),
        }
    },
    'others': {
        'dague-de-jet': {
            'category': 'Standard',
            'name': "Dague de jet",
            'base_item': 'dague-de-jet',
            'full_description': "Une arme blanche à simple ou double tranchant dont la pointe en forme de losange, "
                                "et de préférence symétrique, améliore le pouvoir de perforation. Cette arme à une "
                                "main inflige 1d4 dégâts et peut être lancée jusqu'à 5m",
            'short_description': "Une arme blanche à simple ou double tranchant spécialement conçue pour être lancée.",
            'cost': lambda item: cof.properties.Cost(value=3.0,
                                                     unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'weight': cof.properties.Weight(value=0.5, unit='Kg'),
            'hands': 1,
            'quantity': 1,
            'attack': Attack(
                atype='ranged',
                damages=Damage(
                    base=[Mod(die=4, count=1, target=['punctured'])],
                    other=[],
                ),
                range=Range(value=5, unit='m'),
                critical=RangeSet([20])
            ),
        },
        'recurve-crossbow': {
            'category': 'Optionel',
            'magical_level': 0,
            'base_item': 'recurse-crossbow',
            'name': "Arbalète à répétition",
            'short_description': "Une arbalète équipée de 5 carreaux sur sa partie supérieure.",
            'full_description': "Une arme assez lourde équipée d'un magasin de 5 carreaux sur sa partie supérieure. "
                                "Elle ne nécessite pas d'action de rechargement contrairement aux autres arbalètes, "
                                "mais requiert une FOR minimum de 14 pour être utilisée. Après 5 tirs, il faut la "
                                "recharger, ce qui nécessite une action limitée par carreau. Cette arme est une arme "
                                "à 2 mains et inflige 2d4 DM.",
            'cost': lambda item: cof.properties.Cost(value=20.0,
                                                     unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'weight': cof.properties.Weight(value=10.0, unit='Kg'),
            'hands': 2,
            'attack': Attack(
                atype='ranged',
                damages=Damage(
                    base=[Mod(die=4, count=2, target=['punctured'])],
                    other=[]
                ),
                range=Range(value=50, unit='m'),
                critical=RangeSet([20])
            ),
            'special_property': ["Utilisable par : FOR >= 14", "Après 5 tirs : Recharger (L) / carreau"]
        },
        'throwing-knife': {
            'category': 'Optionel',
            'base_item': 'throwing-knife',
            'magical_level': 0,
            'name': "Couteau de lancer",
            'short_description': "Couteaux à lancer en nombre ou de façon précise.",
            'full_description': "Ces armes de jets font peu de DM mais peuvent s'avérer dangereuses par leur nombre "
                                "ou leur précision. Seuls les bardes, les voleurs et les moines sont formés à leur "
                                "maniement. Au prix d'une action limitée, un personnage peut au choix lancer "
                                "plusieurs couteaux et infliger 2d4 DM, ou en lancer un seul avec précision et "
                                "ajouter son Mod. de DEX aux DM. Ces armes ne sont pas utilisables en combat au "
                                "contact. Les couteaux peuvent être lancés jusqu'à 10m de distance et font 1d4 DM.",
            'cost': lambda item: cof.properties.Cost(value=3.0,
                                                     unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'weight': cof.properties.Weight(value=0.1, unit='Kg'),
            'hands': 1,
            'attack': Attack(
                atype='ranged',
                damages=Damage(
                    base=[Mod(die=4, count=1, target=['punctured', 'sharp'])],
                    other=[Mod(mtype='+', target='DEX')]
                ),
                range=Range(value=10, unit='m'),
                critical=RangeSet([20])
            ),
            'quantity': 10,
            'special_property': ["Lancer multiple (L): 2d4 DM"],
        },
        'throwing-shuriken': {
            'category': 'Optionel',
            'base_item': 'throwing-shuriken',
            'magical_level': 0,
            'name': "Shurikens de lancer",
            'short_description': "Shuriken à lancer en nombre ou de façon précise.",
            'full_description': "Ces armes de jets font peu de DM mais peuvent s'avérer dangereuses par leur nombre "
                                "ou leur précision. Seuls les bardes, les voleurs et les moines sont formés à leur "
                                "maniement. Au prix d'une action limitée, un personnage peut au choix lancer "
                                "plusieurs shurikens et infliger 2d4 DM, ou en lancer un seul avec précision et "
                                "ajouter son Mod. de DEX aux DM. Ces armes ne sont pas utilisables en combat au "
                                "contact. Les shurikens peuvent être lancés jusqu'à 10m de distance et font 1d4 DM.",
            'cost': lambda item: cof.properties.Cost(value=3.0,
                                                     unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'weight': cof.properties.Weight(value=0.1, unit='Kg'),
            'hands': 1,
            'attack': Attack(
                atype='ranged',
                damages=Damage(
                    base=[Mod(die=4, count=1, target=['punctured', 'sharp'])],
                    other=[Mod(mtype='+', target='DEX')]
                ),
                range=Range(value=10, unit='m'),
                critical=RangeSet([20])
            ),
            'quantity': 10,
            'special_property': ["Lancer multiple (L): 2d4 DM"],
        },
        'spear': {
            'category': 'Optionel',
            'base_item': 'spear',
            'magical_level': 0,
            'name': "Épieu",
            'short_description': "Une lance courte et massive, formidable pour la chasse.",
            'full_description': "Une lance courte (1,50 m environ) et massive, formidable pour la chasse. Elle "
                                "offre un bonus de +2 en DEF contre les créatures seulement dotées d'armes "
                                "naturelles et inflige 2d6 DM contre celles qui ne portent pas d'armure "
                                "manufacturée. Cet arme tenue à 2 mains inflige 1d6 DM contre les autres créatures.",
            'cost': lambda item: cof.properties.Cost(value=3,
                                                     unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'weight': cof.properties.Weight(value=2.0, unit='Kg'),
            'hands': 1,
            'attack': Attack(
                atype='melee',
                damages=Damage(
                    base=[Mod(die=6, count=1, target=['punctured', 'sharp'])],
                    other=[]
                ),
                critical=RangeSet([20])
            ),
            'special_property': ['DEF: +2 contre les armes naturelles']
        },
        'scourge': {
            'category': 'Optionel',
            'base_item': 'scourge',
            'magical_level': 0,
            'name': "Fléau",
            'short_description': "Un petit manche prolongé par une chaîne et une boule "
                                 "d'acier hérissée de piques.",
            'full_description': "Un petit manche prolongé par une chaîne au bout de laquelle est suspendue une boule "
                                "d'acier,souvent hérissée de piques. Le fléau offre un bonus de +2 en attaque si "
                                "l'adversaire utilise un bouclier. Cette arme inlige en temps normal 1d6 "
                                "DM.",
            'cost': lambda item: cof.properties.Cost(value=7.0,
                                                     unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'weight': cof.properties.Weight(value=1.0, unit='Kg'),
            'hands': 1,
            'attack': Attack(
                atype='melee',
                damages=Damage(
                    base=[Mod(die=6, count=1, target=['punctured', 'sharp'])],
                    other=[]
                ),
                critical=RangeSet([20])
            ),
            'special_property': ['Attaque : +2 contre les boucliers']
        },
        '2-hands-scourge': {
            'category': 'Optionel',
            'base_item': '2-hands-scourge',
            'magical_level': 0,
            'name': "Fléau à 2 mains",
            'short_description': "Un long manche prolongé par une chaîne et une boule "
                                 "d'acier hérissée de piques.",
            'full_description': "Un long manche prolongé par une chaîne au bout de laquelle est suspendue une boule "
                                 "d'acier,souvent hérissée de piques. Le fléau offre un bonus de +2 en attaque si "
                                "l'adversaire utilise un bouclier. Cette arme à 2 mains inlige en temps normal 1d10 "
                                "DM.",
            'cost': lambda item: cof.properties.Cost(value=11.0,
                                                     unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'weight': cof.properties.Weight(value=2.0, unit='Kg'),
            'hands': 2,
            'attack': Attack(
                atype='melee',
                damages=Damage(
                    base=[Mod(die=10, count=1, target=['punctured', 'sharp'])],
                    other=[]
                ),
                critical=RangeSet([20])
            ),
            'special_property': ['Attaque: +2 contre les boucliers']
        },
        'cavalry-spear': {
            'category': 'Optionel',
            'base_item': 'cavalry-spear',
            'magical_level': 0,
            'name': "Lance de cavalerie",
            'short_description': "La lance de cavalerie ne peut être utilisée qu'à cheval.",
            'full_description': "Concue pour être utilisée uniquement à cheval, la lance de cavalerie mesure environ "
                                "3 m de long. Il faut prendre de l'élan pour l'utiliser à son plein potentiel. "
                                "L'attaque doit avoir lieu après un déplacement pour obtenir les 2d6 DM indiqués. "
                                "Sinon, en combat au contact clasique, le cavalier se voit infligé une pénalité de "
                                "-3 en  attaque et au DM.",
            'cost': lambda item: cof.properties.Cost(value=12.0,
                                                     unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'weight': cof.properties.Weight(value=2.0, unit='Kg'),
            'hands': 1,
            'attack': Attack(
                atype='melee',
                mod=-3,
                damages=Damage(
                    base=[Mod(die=6, count=2, target=['punctured', 'sharp'])],
                    other=[Mod(mtype="-", count=3)]
                ),
                critical=RangeSet([20])
            ),
            'special_property': ["Utilisable seulement à cheval", "Attaque mouvement : pas de malus"]
        },
        'left-hand': {
            'category': 'Optionel',
            'base_item': 'left-hand',
            'magical_level': 0,
            'name': "Main gauche",
            'short_description': "La main gauche comporte une garde en panier très couvrante.",
            'full_description': "La main gauche ou dague de parade comporte une garde en panier très couvrante. Elle "
                                "offre un bonus de +1 en DEF, mais seulement en combat au contact contre les "
                                "adversaires maniant des armes dont la taille et le poids n'execèdent pas une épée "
                                "longue (ce qui exclu les masses et les marteaux).",
            'cost': lambda item: cof.properties.Cost(value=5.0,
                                                     unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'weight': cof.properties.Weight(value=0.5, unit='Kg'),
            'hands': 1,
            'attack': Attack(
                atype='melee',
                damages=Damage(
                    base=[Mod(die=4, count=1, target=['punctured', 'sharp'])],
                    other=[]
                ),
                critical=RangeSet([20])
            ),
            'special_property': ["DEF: +1 contre armes légères (<1,5 Kg)"]
        },
        'pike': {
            'category': 'Optionel',
            'base_item': 'pike',
            'magical_level': 0,
            'name': "Pique",
            'short_description': "Une lance faite pour recevoir les charges de cavalerie "
                                 "ou attaquer depuis le second rang.",
            'full_description': "Une très longue lance de fantassin, destinée à recevoir les charges de cavalerie "
                                "ou à attaquer depuis le second rang. La pique double ses 1d8 DM contre une créature "
                                "de grande taille qui vient de réaliser une charge ou une action de mouvement pour "
                                "arriver au contact. Elle permet aussi d'attaquer en se tenant derrière un allié de "
                                "taille normale, avec une pénalité de -5. Elle inflige également une pénalité de -5 "
                                "en attaque dans toutes les autres conditions. Cette arme est une arme a 2 mains.",
            'cost': lambda item: cof.properties.Cost(value=5.0,
                                                     unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'weight': cof.properties.Weight(value=2.0, unit='Kg'),
            'hands': 2,
            'attack': Attack(
                mod=-5,
                atype='melee',
                damages=Damage(
                    base=[Mod(die=8, count=1, target=['punctured'])],
                    other=[]
                ),
                critical=RangeSet([20])
            ),
            'special_property': ["DM: x2 hautes tailles (mouvement)",
                                 "Attaque depuis le second rang"]
        },
        'stiletto': {
            'category': 'Optionel',
            'base_item': 'stiletto',
            'magical_level': 0,
            'name': "Stylet",
            'short_description': "Une arme destinée à transpercer les organes vitaux.",
            'full_description': "Une arme d'assassin, une pointe acérée sans tranchants destinée à transpercer les "
                                "organes vitaux. Cette arme inflige 1d3 DM, mais ne bénéficie pas du bonus de FOR. "
                                "En cas d'attaque sournoise ou par surprise, le stylet inflige [1d6 + Mod. DEX] DM.",
            'cost': lambda item: cof.properties.Cost(value=1.0,
                                                     unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'weight': cof.properties.Weight(value=0.3, unit='Kg'),
            'hands': 1,
            'attack': Attack(
                atype='melee',
                damages=Damage(
                    base=[Mod(die=3, count=1, target=['punctured'])],
                    other=[]
                ),
                critical=RangeSet([20])
            ),
            'special_property': ['DM (sournoise): 1d6 +[DEX]', "DM: Pas de bonus de FOR"]
        },
    }
}
