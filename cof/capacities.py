# -*- coding: utf-8 -*-

import cof.generics
import typing
import cilogger.cilogger
log = cilogger.cilogger.ccilogger(__name__)


@cilogger.cilogger.ctrace
class Capacity(cof.generics.GenericObject):
    """ COF Capacity

    .. TODO::
        * wid should not be None
        * way_rank should be greater than 0
    """
    def __init__(self, **kwargs):
        #: Capacity full description
        self._full_description: typing.Optional[str] = None
        #: Capacity short description
        self._short_description: typing.Optional[str] = None
        #: Way ID
        self._wid: typing.Optional[str] = None
        #: Way rank
        self._way_rank: int = -1
         #: Capacity special property
        self._special_property: list = []
        # Is it a limited capacity ?
        self._limited = False
        self._area: Optional[Area] = None
        self._duration: Optional[Duration] = None
        self._range: Optional[Range] = None
        self._skill: typing.Optional[list[object]] = None
        self._defense: typing.Optional[list[object]] = None
        self._attack: object = None
        self._creature: typing.Optional[list] = None
        super().__init__(**kwargs)

    @property
    def creature(self):
        return self._creature

    @creature.setter
    def creature(self, creature):
        self._creature = creature

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
    def special_property(self):
        return self._special_property

    @special_property.setter
    def special_property(self, value):
        self._special_property = value
 
    @property
    def full_description(self):
        return self._full_description

    @full_description.setter
    def full_description(self, full_description):
        self._full_description = full_description

    @property
    def short_description(self):
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        self._short_description = short_description

    @property
    def wid(self):
        return self._wid

    @wid.setter
    def wid(self, wid):
        self._wid = wid

    @property
    def way_rank(self):
        return self._way_rank

    @way_rank.setter
    def way_rank(self, way_rank):
        self._way_rank = int(way_rank)

    @property
    def limited(self):
        return self._limited

    @limited.setter
    def limited(self, limited):
        self._limited = limited

    @property
    def itype(self):
        return 'Capacité'


@cilogger.cilogger.ctrace
class Capacities(cof.generics.GenericObjects):

    def __init__(self):
        super().__init__()
