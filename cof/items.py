# -*- coding: utf-8 -*-

import cof.generics
import typing


class Item(cof.generics.GenericObject):

    """ Class for describing COF items


    .. todo:: check type from config
    """
    def __init__(self, **kwargs):
        #: Item full description
        self._full_description: typing.Optional[str] = None

        #: Item short description
        self._short_description: typing.Optional[str] = None

        #: Item's weight : must be a dict containing value and unit ( ex: {'value': 10, 'unit', 'Kg'}
        self._weight: object = None

        #: Item's cost : must be a dict containing value and unit ( ex: {'value': 10, 'unit', 'pa'}
        self._cost: object = None

        #: Items category
        self._category: Optional[str] = None

        #: Items special property
        self._special_property: list = []

        #: Items can be use by listed class name. Default to empty list means everybody can use it
        self._usable_by: list = []

        #: base item on which the final item is derived
        self._base_item: str = ''

        #: base item on which the final item is derived
        self._flavor: List[object] = []

        #: Item's use slot. Default to -1 means infinite use, 0 mean need a big slot with no limit value
        self._use: int = -1

        #: Item's quantity. Default to -1 means infinite use, 0 mean need a big slot with no limit value
        self._quantity: int = -1

        self._scenario: Optional[list] = None
        self._hands: int = 0
        #: Item's rank in the way. Default to -1 means not applicable for this item
        self._way_rank: int = -1

        #: Item's magical level. Default to None means not applicable for this item. Must be one of config defined
        #: magical levels
        self._magical_level: typing.Optional = None
        self._defense: typing.Optional[list[object]] = None
        self._attack: object = None
        self._area: Optional[Area] = None
        self._duration: Optional[Duration] = None
        self._range: Optional[Range] = None
        self._skill: typing.Optional[list[object]] = None
        self._creature: typing.Optional[list] = None
        self._ability: typing.Optional[list[object]] = None
        self._material: Optional[string] = None
        super().__init__(**kwargs)

    @property
    def full_description(self):
        return self._full_description

    @full_description.setter
    def full_description(self, full_desc):
        self._full_description = full_desc

    @property
    def short_description(self):
        return self._short_description

    @short_description.setter
    def short_description(self, short_desc):
        self._short_description = short_desc

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        self._weight = weight

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, cost):
        self._cost = cost

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        self._category = category

    @property
    def special_property(self):
        return self._special_property

    @special_property.setter
    def special_property(self, value):
        self._special_property = value

    @property
    def usable_by(self):
        return self._usable_by

    @usable_by.setter
    def usable_by(self, usable_by):
        self._usable_by = usable_by

    @property
    def base_item(self):
        return self._base_item

    @base_item.setter
    def base_item(self, value):
        self._base_item = value

    @property
    def flavor(self):
        return self._flavor

    @flavor.setter
    def flavor(self, value):
        self._flavor = value

    @property
    def use(self):
        return self._use

    @use.setter
    def use(self, use):
        self._use = use

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity

    @property
    def scenario(self):
        return self._scenario

    @scenario.setter
    def scenario(self, scenario):
        self._scenario = scenario

    @property
    def hands(self):
        return self._hands

    @hands.setter
    def hands(self, value):
        self._hands = value

    @property
    def defense(self):
        return self._defense

    @defense.setter
    def defense(self, value):
        self._defense = value

    @property
    def attack(self):
        return self._attack

    @attack.setter
    def attack(self, value):
        self._attack = value
    @property
    def skill(self):
        return self._skill

    @skill.setter
    def skill(self, value):
        self._skill = value

    @property
    def ability(self):
        return self.ability

    @ability.setter
    def ability(self, value):
        self.ability = value

    @property
    def range(self):
        return self._range

    @range.setter
    def range(self, value):
        self._range = value

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = value

    @property
    def way_rank(self):
        return self._way_rank

    @way_rank.setter
    def way_rank(self, way_rank: int):
        self._way_rank = way_rank

    @property
    def magical_level(self):
        return self._magical_level

    @magical_level.setter
    def magical_level(self, magical_level):
        self._magical_level = magical_level

    @property
    def creature(self):
        return self._creature

    @creature.setter
    def creature(self, creature):
        self._creature = creature

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, value):
        self._material = value


class Potion(Item):
    @property
    def itype(self):
        return 'Potion'

    @property
    def ticon(self):
        return 'round-bottom-flask.png'


class Spell(Item):
    @property
    def itype(self):
        return 'Parchemin'

    @property
    def ticon(self):
        return 'scroll-unfurled.png'


class MagicalWand(Item):
    @property
    def itype(self):
        return 'Baguette magique'

    @property
    def ticon(self):
        return 'crystal-wand.png'


class Weapon(Item):
    @property
    def itype(self):
        return 'Arme'

    @property
    def ticon(self):
        return 'crossed-swords.png'


class Armor(Item):
    @property
    def itype(self):
        return 'Armure'

    @property
    def ticon(self):
        return 'leather-armor.png'


class Shield(Item):
    @property
    def itype(self):
        return 'Bouclier'

    @property
    def ticon(self):
        return 'c-shield.png'


class Char(Item):
    @property
    def itype(self):
        return 'Chariot'

    @property
    def ticon(self):
        return 'chariot.png'


class Mount(Item):
    @property
    def itype(self):
        return 'Monture'

    @property
    def ticon(self):
        return 'donkey.png'


class Material(Item):
    @property
    def itype(self):
        return 'Matériel'

    @property
    def ticon(self):
        return 'swiss-army-knife.png'


class Inn(Item):
    @property
    def itype(self):
        return "Consommation d'auberge"

    @property
    def ticon(self):
        return 'beer-stein.png'


class RealEstate(Item):
    @property
    def itype(self):
        return "Bien immobilier"

    @property
    def ticon(self):
        return 'house.png'


class Bullet(Item):
    @property
    def itype(self):
        return "Munition"

    @property
    def ticon(self):
        return 'bullet.png'


class Ring(Item):
    @property
    def itype(self):
        return "Anneau"

    @property
    def ticon(self):
        return 'ring.png'


class Gloves(Item):
    @property
    def itype(self):
        return "Gants"

    @property
    def ticon(self):
        return 'gloves.png'


class Belt(Item):
    @property
    def itype(self):
        return "Ceinture"

    @property
    def ticon(self):
        return 'belts.png'


class Boots(Item):
    @property
    def itype(self):
        return "Bottes"

    @property
    def ticon(self):
        return 'boots.png'


class Amulet(Item):
    @property
    def itype(self):
        return "Amulette"

    @property
    def ticon(self):
        return 'amulet.png'


class Cloak(Item):
    @property
    def itype(self):
        return "Cape"

    @property
    def ticon(self):
        return 'cloak.png'


class Robe(Item):
    @property
    def itype(self):
        return "Robe"

    @property
    def ticon(self):
        return 'robe.png'


class Bracer(Item):
    @property
    def itype(self):
        return "Bracelet"

    @property
    def ticon(self):
        return 'bracer.png'


class Helmet(Item):
    @property
    def itype(self):
        return 'Casque'

    @property
    def ticon(self):
        return 'helmets.png'


class Items(cof.generics.GenericObjects):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
