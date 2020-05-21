# -*- coding: utf-8 -*-

import cof.utils
import cof.generics
import json
import re
import cilogger.cilogger
log = cilogger.cilogger.ccilogger(__name__)


@cilogger.cilogger.ctrace
class Way(cof.generics.GenericObject):

    def __init__(self, **kwargs):
        #: List of capacity object id belonging to this way
        self._capacities: list = []
        super().__init__(**kwargs)

    @property
    def capacities(self):
        return self._capacities

    @capacities.setter
    def capacities(self, capacities):
        self._capacities = capacities

    def add_capacity(self, capacity):
        self._capacities.append(capacity)

    @property
    def itype(self):
        return 'Voie'


@cilogger.cilogger.ctrace
class Ways(cof.generics.GenericObjects):

    def __init__(self):
        super().__init__()
