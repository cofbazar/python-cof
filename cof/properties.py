# -*- coding: utf-8 -*-

import cof.generics
import typing
import copy
from typing import Optional


class Cost(cof.generics.GenericUnitObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def __unit_list__(self):
        return {'pp': 100, 'po': 10, 'pa': 1, 'pc': 0.1}


class Weight(cof.generics.GenericUnitObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def __unit_list__(self):
        return {'T': 1000, 'Kg': 1, 'g': 0.001}


class Range(cof.generics.GenericUnitObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def __unit_list__(self):
        return {'km': 1000, 'm': 1, 'cm': 0.01}


class Area(cof.generics.GenericUnitObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def __unit_list__(self):
        return {'km': 1000, 'm': 1, 'cm': 0.01}


class Scenario(object):
    def __init__(self, **kwargs):
        self._title: Optional[str] = None
        self._chapter: Optional[str] = None
        self._numbering: Optional[str] = None
        self._campaign: Optional[str] = None
        self._assign(**kwargs)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def chapter(self):
        return self._chapter

    @chapter.setter
    def chapter(self, value):
        self._chapter = value

    @property
    def numbering(self):
        return self._numbering

    @numbering.setter
    def numbering(self, value):
        self._numbering = value

    @property
    def campaign(self):
        return self._campaign

    @campaign.setter
    def campaign(self, value):
        self._campaign = value

    def _assign(self: object, **kwargs):
        """ Assign kwargs arguments to the corresponding object attribute if exists.

        Kwargs arguments are assigned by attribute name.

        :param dict kwargs: Kwargs passed to the __init__ function
        :raise AttributeError: if Object attribute does not exists
        """
        for attribute, value in kwargs.items():
            if not attribute.startswith('_'):
                # Force private attribute use
                attribute = '_{}'.format(attribute)
            if hasattr(self, attribute):
                # self.__log__.debug("Found attribute '{}' with value '{}'".format(attribute, value))
                if attribute.startswith('_'):
                    # Force setter use
                    attribute = attribute.replace('_', '', 1)
                setattr(self, attribute, value)
            else:
                raise AttributeError('No attribute "{}" found in object ""'.format(attribute, self))


class Duration(cof.generics.GenericUnitObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def __unit_list__(self):
        return {'j': 86400, 'h': 3600, 'min': 60, 's': 1, 'tr': 5}


class Flavor(object):
    def __init__(self, **kwargs):
        self._ftype: str = ""
        self._count: int = 0
        self._assign(**kwargs)

    @property
    def ftype(self):
        return self._ftype

    @ftype.setter
    def ftype(self, value):
        self._ftype = value

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value

    def _assign(self: object, **kwargs):
        """ Assign kwargs arguments to the corresponding object attribute if exists.

        Kwargs arguments are assigned by attribute name.

        :param dict kwargs: Kwargs passed to the __init__ function
        :raise AttributeError: if Object attribute does not exists
        """
        for attribute, value in kwargs.items():
            if not attribute.startswith('_'):
                # Force private attribute use
                attribute = '_{}'.format(attribute)
            if hasattr(self, attribute):
                # self.__log__.debug("Found attribute '{}' with value '{}'".format(attribute, value))
                if attribute.startswith('_'):
                    # Force setter use
                    attribute = attribute.replace('_', '', 1)
                setattr(self, attribute, value)
            else:
                raise AttributeError('No attribute "{}" found in object ""'.format(attribute, self))

class Property(object):
    """
        Propriété : PROPERTY Mod
        Résistance à la magie DEF +5
        Résistance à la magie +5
        Natation +5

        Not implemented
    """
    pass


class Mod(object):
    """
        Modificateur : LABEL +/-COUNT
        Exemple : DEF +1 ou CHA +3 ou +1 ou feu +4 ou DEX -1 ou feu +1d4
    """
    def __init__(self, **kwargs):
        self._mtype: typing.Optional[str] = None
        self._count: typing.Optional[int] = None
        self._die: typing.Optional[int] = None
        self._target: typing.Optional[typing.Union[str, list]] = None
        self._label: typing.Optional[str] = None
        self._limitation: typing.Optional[str] = None
        self._assign(**kwargs)

    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, value):
        self._target = value

    @property
    def limitation(self):
        return self._limitation

    @limitation.setter
    def limitation(self, value):
        self._limitation = value

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, value):
        self._label = value

    @property
    def mtype(self):
        return self._mtype

    @mtype.setter
    def mtype(self, value):
        self._mtype = value

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value

    @property
    def die(self):
        return self._die

    @die.setter
    def die(self, value):
        self._die = value

    def updie(self):
        ndie = copy.copy(self)
        if self._die is not None:
            if self._die in [4, 6, 8, 10]:
                ndie._die += 2
            elif self._die == 3:
                ndie._die = 4
        return ndie

    def _assign(self: object, **kwargs):
        """ Assign kwargs arguments to the corresponding object attribute if exists.

        Kwargs arguments are assigned by attribute name.

        :param dict kwargs: Kwargs passed to the __init__ function
        :raise AttributeError: if Object attribute does not exists
        """
        for attribute, value in kwargs.items():
            if not attribute.startswith('_'):
                # Force private attribute use
                attribute = '_{}'.format(attribute)
            if hasattr(self, attribute):
                # self.__log__.debug("Found attribute '{}' with value '{}'".format(attribute, value))
                if attribute.startswith('_'):
                    # Force setter use
                    attribute = attribute.replace('_', '', 1)
                setattr(self, attribute, value)
            else:
                raise AttributeError('No attribute "{}" found in object ""'.format(attribute, self))


class Damage(object):
    """
        [Die | Mod]
        Exemple :

        tranchant : 3d6
        contondant : 3d6, feu +1
        feu : 3d6

    """
    def __init__(self, **kwargs):
        self._base: list = []
        self._other: list = []
        self._assign(**kwargs)

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, value):
        self._base = value

    @property
    def other(self):
        return self._other

    @other.setter
    def other(self, value):
        self._other = value

    def _assign(self: object, **kwargs):
        """ Assign kwargs arguments to the corresponding object attribute if exists.

        Kwargs arguments are assigned by attribute name.

        :param dict kwargs: Kwargs passed to the __init__ function
        :raise AttributeError: if Object attribute does not exists
        """
        for attribute, value in kwargs.items():
            if not attribute.startswith('_'):
                # Force private attribute use
                attribute = '_{}'.format(attribute)
            if hasattr(self, attribute):
                # self.__log__.debug("Found attribute '{}' with value '{}'".format(attribute, value))
                if attribute.startswith('_'):
                    # Force setter use
                    attribute = attribute.replace('_', '', 1)
                setattr(self, attribute, value)
            else:
                raise AttributeError('No attribute "{}" found in object ""'.format(attribute, self))


class Attack(object):
    def __init__(self, **kwargs):
        self._name: typing.Optional[str] = None
        self._mod: typing.Optional[int] = 0
        self._atype: str = ''
        self._damages: object = None
        self._critical: object = None
        self._range: object = None
        self._area: object = None
        self._assign(**kwargs)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def mod(self):
        return self._mod

    @mod.setter
    def mod(self, value):
        self._mod = value

    @property
    def atype(self):
        return self._atype

    @atype.setter
    def atype(self, value):
        self._atype = value

    @property
    def damages(self):
        return self._damages

    @damages.setter
    def damages(self, value):
        self._damages = value

    @property
    def critical(self):
        return self._critical

    @critical.setter
    def critical(self, value):
        self._critical = value

    @property
    def range(self):
        return self._range

    @range.setter
    def range(self, value):
        self._range = value

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = value

    def _assign(self: object, **kwargs):
        """ Assign kwargs arguments to the corresponding object attribute if exists.

        Kwargs arguments are assigned by attribute name.

        :param dict kwargs: Kwargs passed to the __init__ function
        :raise AttributeError: if Object attribute does not exists
        """
        for attribute, value in kwargs.items():
            if not attribute.startswith('_'):
                # Force private attribute use
                attribute = '_{}'.format(attribute)
            if hasattr(self, attribute):
                # self.__log__.debug("Found attribute '{}' with value '{}'".format(attribute, value))
                if attribute.startswith('_'):
                    # Force setter use
                    attribute = attribute.replace('_', '', 1)
                setattr(self, attribute, value)
            else:
                raise AttributeError('No attribute "{}" found in object ""'.format(attribute, self))


class Defense(object):
    """
    RM : d

    """
    def __init__(self, **kwargs):
        self._name: typing.Optional[str] = None
        self._label: typing.Optional[str] = None
        self._mod: typing.Optional[int] = None
        self._dtype: typing.Optional[str] = None
        self._assign(**kwargs)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, value):
        self._label = value

    @property
    def mod(self):
        return self._mod

    @mod.setter
    def mod(self, value):
        self._mod = value

    @property
    def dtype(self):
        return self._dtype

    @dtype.setter
    def dtype(self, value):
        self._dtype = value

    def _assign(self: object, **kwargs):
        """ Assign kwargs arguments to the corresponding object attribute if exists.

        Kwargs arguments are assigned by attribute name.

        :param dict kwargs: Kwargs passed to the __init__ function
        :raise AttributeError: if Object attribute does not exists
        """
        for attribute, value in kwargs.items():
            if not attribute.startswith('_'):
                # Force private attribute use
                attribute = '_{}'.format(attribute)
            if hasattr(self, attribute):
                # self.__log__.debug("Found attribute '{}' with value '{}'".format(attribute, value))
                if attribute.startswith('_'):
                    # Force setter use
                    attribute = attribute.replace('_', '', 1)
                setattr(self, attribute, value)
            else:
                raise AttributeError('No attribute "{}" found in object ""'.format(attribute, self))
