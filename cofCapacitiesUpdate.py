# -*- coding: utf-8 -*-

import re
import bs4
import urllib.request as urlr
import cof.capacities
import cof.ways
import cof.utils
import json
import config.cofConfig
import os
import cilogger.cilogger
log = cilogger.cilogger.ccilogger(__name__)


@cilogger.cilogger.ftrace
def sanitize(t):
    sanitize_regex = re.compile(r'[\s\n]+', re.MULTILINE)
    return sanitize_regex.sub(' ', '{}'.format(t))


@cilogger.cilogger.ftrace
def main():

    capacities_file = os.path.join(config.cofConfig.config['global']['path']['root'],
                                   config.cofConfig.config['global']['path']['data'],
                                   'capacities-orig.json')
    capacities = cof.capacities.Capacities()
    capacities.load(capacities_file)
    for c in config.cofConfig.config['capacities']['capacities']:
        capacities.add(cof.capacities.Capacity(**c))
    for c in capacities:
        c.update(config.cofConfig.config['capacities']['addons'])

    capacities_file = os.path.join(config.cofConfig.config['global']['path']['root'],
                                   config.cofConfig.config['global']['path']['data'],
                                   'capacities.json')
    capacities.save(capacities_file)


if __name__ == '__main__':
    cilogger.cilogger.rootlogger.setLevel('DEBUG')
    main()
