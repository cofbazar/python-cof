# -*- coding: utf-8 -*-

from cof.properties import *
import config.cofConfig

boots = {
    'weight': Weight(value=0.3, unit='Kg'),
    'cost': lambda item: Cost(
        value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
        unit=config.cofConfig.config['global']['cost']['unit']).iso(),
}
