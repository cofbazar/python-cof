# -*- coding: utf-8 -*-
""" Module for managing generic object and objects list

"""
import sys
import json
import re
import importlib
import abc
import typing
import pathlib
import cilogger.cilogger
import functools
import copy
from ClusterShell.NodeSet import RangeSet
log = cilogger.cilogger.ccilogger(__name__)


@cilogger.cilogger.ctrace
class JSONObjectEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            result = {(o.replace('_', '', 1) if o.startswith('_') else o): v for o, v in obj.__dict__.items()}
            result['__type__'] = obj.__class__.__name__
            if result['__type__'] == 'RangeSet':
                return '{}'.format(obj)
            else:
                self.__log__.trace('Found attribute list "{}" for object "{}"'.format(result.keys(), obj))
                return result
        except AttributeError:
            return json.JSONEncoder.default(self, obj)

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def __log__(self):
        return cilogger.cilogger.ccilogger('{}.{}'.format(self.__class__.__module__, self.__class__.__name__))


@cilogger.cilogger.ctrace
class JSONObjectDecoder(json.JSONDecoder):
    def __init__(self):
        super().__init__(object_hook=self.default)

    def default(self, obj):
        if '__type__' in obj:
            otype = obj.pop('__type__')
            self.__log__.trace('Obj: {}'.format(obj))
            lpackage = ['{}.{}'.format(__package__, m) for m in dir(sys.modules[__package__]) if not m.startswith('__')]
            self.__log__.trace('Found package list "{}" in "{}"'.format(lpackage, __package__))
            for module in lpackage:
                try:
                    self.__log__.trace('Trying object class "{}" in module "{}" ...'.format(otype, module))
                    cls = getattr(sys.modules[module], otype)
                    return cls(**obj)
                except AttributeError:
                    pass
        else:
            return obj

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def __log__(self):
        return cilogger.cilogger.ccilogger('{}.{}'.format(self.__class__.__module__, self.__class__.__name__))


@functools.total_ordering
@cilogger.cilogger.ctrace
class GenericObject(abc.ABC):
    """ Abstract class for managing generic objects

    All generic objects can be load from json and save to json

    :raise AttributeError: if oid is None when assign is done
    """

    def __init__(self: object, **kwargs):
        self._oid: typing.Optional[str] = None
        self._name: typing.Optional[str] = None
        self._count: int = 1
        self._assign(**kwargs)
        if self._oid is None:
            raise AttributeError("Object must have at least an object ID")

    def _assign(self: object, **kwargs):
        """ Assign kwargs arguments to the corresponding object attribute if exists.

        Kwargs arguments are assigned by attribute name.

        :param dict kwargs: Kwargs passed to the __init__ function

        :raise AttributeError: if Object attribute does not exists
        """
        for attribute, value in kwargs.items():
            self.__log__.trace("Parsing attribute '{}' with value '{}'".format(attribute, value))
            if not attribute.startswith('_'):
                # Force private attribute use
                attribute = '_{}'.format(attribute)
            if hasattr(self, attribute):
                self.__log__.trace("Found attribute '{}' with value '{}'".format(attribute, value))
                if attribute.startswith('_'):
                    # Force setter use
                    attribute = attribute.replace('_', '', 1)
                setattr(self, attribute, value)
            else:
                raise AttributeError('No attribute "{}" found in object ""'.format(attribute, self))

    def update(self: object, d: dict):
        """ Updates attributes'value if attribute found in dict

        :param dict d: A dict formatted as {'itemID': {'attribute1': value1, ..., 'attributeN': valueN}}
        """
        for attribute in [a.replace('_', '', 1) if a.startswith('_') else a for a in self.__dict__]:
            self.__log__.debug('Trying to update attribute "{}" for object "{}"'.format(attribute, self._oid))
            if self._oid in d and attribute in d[self._oid]:
                self.__log__.debug('Updating attribute "{}" with value "{}"'.format(attribute, d[self._oid][attribute]))
                setattr(self, attribute, d[self._oid][attribute])

    @property
    def oid(self: object) -> str:
        """Get and set unique object identifier"""
        return self._oid

    @oid.setter
    def oid(self: object, oid: str):
        self._oid = oid

    @property
    def name(self: object) -> str:
        """Get and set object name"""
        return self._name

    @name.setter
    def name(self: object, name: str):
        self._name = name

    @property
    def count(self):
        """ Get and set object count """
        return self._count

    @count.setter
    def count(self, value: int):
        self._count = value

    def _is_valid_operand(self, other):
        return hasattr(self, 'cost') and self._cost is not None and \
               hasattr(other, 'cost') and other.cost is not None

    def __eq__(self, other):
        if self._is_valid_operand(other):
            return self.cost == other.cost
        else:
            return NotImplemented

    def __lt__(self, other):
        if self._is_valid_operand(other):
            return self.cost < other.cost
        else:
            return NotImplemented

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def __log__(self):
        return cilogger.cilogger.ccilogger('{}.{}'.format(self.__class__.__module__, self.__class__.__name__))


@functools.total_ordering
@cilogger.cilogger.ctrace
class GenericUnitObject(abc.ABC):
    """ Abstract class for managing sub objects """
    def __init__(self: object, **kwargs):
        self._value: typing.Optional[int] = None
        self._unit: typing.Optional[str] = None
        self._assign(**kwargs)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        self._value = v

    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, u):
        self._unit = u

    def iso(self):
        if hasattr(self, '__unit_list__') and self._value is not None and self._unit is not None and \
                self._unit in self.__unit_list__:
            x = copy.copy(self)
            x._value = self._value * self.__unit_list__[self._unit]
            x._unit = 'pa'
            return x
        else:
            return NotImplemented

    def to(self, to_unit):
        if hasattr(self, '__unit_list__') and self._value is not None and self._unit is not None and \
                self._unit in self.__unit_list__ and to_unit in self.__unit_list__:
            x = self.iso()
            x._value = x._value / self.__unit_list__[to_unit]
            return x
        else:
            return NotImplemented

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

    def _is_valid_operand(self, other):
        return hasattr(other, 'unit') and hasattr(other, 'value') and \
               hasattr(other, '__unit_list__') and hasattr(self, '__unit_list__') and \
               self._value is not None and self._unit is not None and self._unit in self.__unit_list__ and \
               other.value is not None and other.unit is not None and other.unit in other.__unit_list__

    def __eq__(self, other):
        if self._is_valid_operand(other):
            return self.iso().value == other.iso().value
        else:
            return NotImplemented

    def __lt__(self, other):
        if self._is_valid_operand(other):
            return self.iso().value < other.iso().value
        else:
            return NotImplemented

    def __add__(self, other):
        if self._is_valid_operand(other):
            x = self.iso()
            x._value = self.iso().value + other.iso().value
            return x
        else:
            return NotImplemented

    def __mul__(self, n):
        if hasattr(self, '__unit_list__') and self._value is not None and self._unit is not None and \
                self._unit in self.__unit_list__ and (isinstance(n, float) or isinstance(n, int)) and n is not None:
            x = self.iso()
            x._value = self.iso().value * n
            return x
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __str__(self):
        return '{} {}'.format(self._value, self._unit)

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def __log__(self):
        return cilogger.cilogger.ccilogger('{}.{}'.format(self.__class__.__module__, self.__class__.__name__))


@cilogger.cilogger.ctrace
class GenericObjects(abc.ABC):
    """ Abstract class for managing objects list

    List can be load from json file and save to json file

    """

    def __init__(self: object, allow_duplicate_object_id: bool = False):
        self._objects = []
        self._objects_by_oid = {}
        self._objects_by_type = {}
        self._allow_duplicate_object_id = allow_duplicate_object_id

    def get(self: object) -> list:
        """ Get all objects from list

        :return: Objects list
        """
        return self._objects

    def len(self):
        return len(self._objects)

    def get_ids(self: object) -> list:
        """ Get all objects ids from list

        :return: Objects Ids list
        """
        return [o for o in self._objects_by_oid]

    def get_types(self):
        return [t for t in self._objects_by_type]

    def get_by_id(self: object, oid: str) -> typing.Optional[GenericObject]:
        """ Get an object from the list by its id

        :param str oid: Unique object identifier
        :return: An object matching the id or None if not found
        """
        if oid in self._objects_by_oid:
            obj = self._objects_by_oid[oid]
        else:
            obj = None
        return obj

    def get_by_type(self: object, otype: str) -> list:
        """ Get all objects from the list matching otype

        :return: Objects list for objects matching otype
        """
        if otype in self._objects_by_type:
            objs = self._objects_by_type[otype]
        else:
            objs = None
        return objs

    def add(self: object, obj: GenericObject):
        """ Add an object to the objects list

        :param cof.generics.object obj: Object to add to the list
        """
        if obj.oid in self._objects_by_oid:
            self.__log__.debug('Adding object "{}" ...'.format(obj.oid))
            if self._allow_duplicate_object_id:
                self._objects_by_oid[obj.oid].count += 1
            else:
                self.__log__.warning('Object "{}" with ID "{}" is already in object list'.format(obj, obj.oid))
        else:
            self._objects.append(obj)
            self._objects_by_oid.update({obj.oid: obj})
            if obj.itype in self._objects_by_type:
                self._objects_by_type[obj.itype].append(obj)
            else:
                self._objects_by_type.update({obj.itype: [obj]})

    def delete(self: object, obj: GenericObject):
        """ Add an object to the objects list

        :param cof.generics.object obj: Object to add to the list
        """
        if obj.oid in self._objects_by_oid:
            o = self._objects_by_oid[obj.oid]
            if self._allow_duplicate_object_id and o.count > 1:
                o.count -= 1
            else:
                if o.count > 1:
                    self.__log__.warning('Object "{}" with ID "{}" is more than once in object list'.format(obj,
                                                                                                            obj.oid))
                self._objects.remove(obj)
                self._objects_by_oid.pop(obj.oid)
                if obj.itype in self._objects_by_type:
                    self._objects_by_type[obj.itype].remove(obj)
                    if not self._objects_by_type[obj.itype]:
                        self._objects_by_type.pop(obj.itype)

        else:
            log.error('Object "{}" with ID "{}" is not in object list'.format(obj, obj.oid))

    def adds(self: object, lobj: list):
        """ Add an object list to the objects list

        :param list[cof.generics.object] lobj: Object list to add to the list
        """
        for obj in lobj:
            self.add(obj)

    def save(self: object, objects_file: str):
        """ Save all objects from the list in a json file

        :param str objects_file: Json file full path to save objects list
        """
        with open(objects_file, 'w') as objects_fh:
            json.dump(self._objects, cls=JSONObjectEncoder, fp=objects_fh, indent=2,
                      sort_keys=True, ensure_ascii=False)

    def load(self, objects_file):
        """ Load all objects into the list from a json file

        :param str objects_file: Json file full path to load objects list from
        """
        with open(objects_file, 'r') as objects_fh:
            self.adds(json.load(objects_fh, cls=JSONObjectDecoder))

    def __iter__(self):
        return self._objects.__iter__()

    def __next__(self):
        return self._objects.__next__()

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def __log__(self):
        return cilogger.cilogger.ccilogger('{}.{}'.format(self.__class__.__module__, self.__class__.__name__))
