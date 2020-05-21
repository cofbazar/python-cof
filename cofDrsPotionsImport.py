# -*- coding: utf-8 -*-

import re
import bs4
import urllib.request as urlr
import cof.capacities
import cof.items
from cof.properties import *
import config.cofConfig
import cof.utils
import os
import cilogger.cilogger
log = cilogger.cilogger.ccilogger(__name__)


# @cilogger.cilogger.ftrace
def main():
    url = 'http://co-drs.org/regles/objets-magiques/'
    html = urlr.urlopen(url).read()
    soup = bs4.BeautifulSoup(html, 'html.parser')
    capacities_file = os.path.join(config.cofConfig.config['global']['path']['root'],
                                   config.cofConfig.config['global']['path']['data'],
                                   'capacities.json')

    # potion_base_price = 50 # 50 pa
    potion_list = ['table-des-potions-de-soin', 'table-des-potions-communes', 'table-des-potions-rares']

    capacities_list = cof.capacities.Capacities()
    capacities_list.load(capacities_file)

    ilist = cof.items.Items()
    for t in soup.find_all('table'):
        if t.find('caption') and t.caption.find('a') and t.caption.find('a').attrs['id'] in potion_list:
            potion = t.find_all('a', href=re.compile(r'/capacites/'))
            for h in potion:
                log.debug('Found link "{}"'.format(h['href']))
                cap = capacities_list.get_by_id(h['href'])
                if cap is not None:
                    # Potion mineures
                    for magical_level, use in config.cofConfig.config['potions']['magical_level'].items():
                        it = cof.items.Potion(oid=cof.utils.string_to_id('potion-{}-{}'.format(cap.name.lower(),
                                                                                               magical_level)),
                                              name='Potion {}, {}'.format(use['label'], cap.name),
                                              full_description=cap.full_description,
                                              short_description=cap.short_description,
                                              way_rank=cap.way_rank,
                                              magical_level=magical_level,
                                              range=cap.range,
                                              area=cap.area,
                                              duration=cap.duration,
                                              category="Magique",
                                              skill=cap.skill,
                                              quantity=1,
                                              flavor=[Flavor(ftype=magical_level, count=1)],
                                              defense=cap.defense,
                                              attack=cap.attack,
                                              special_property=cap.special_property,
                                              base_item=cof.utils.string_to_id(f"potion-{cap.name.lower()}"),
                                              weight=config.cofConfig.config['potions']['weight'],
                                              use=use['use'])
                        it.cost = config.cofConfig.config['potions']['cost'](it)
                        it.update(config.cofConfig.config['potions']['addons'])
                        ilist.add(it)

    potions_file = os.path.join(config.cofConfig.config['global']['path']['root'],
                                config.cofConfig.config['global']['path']['data'],
                                'potions.json')
    ilist.save(potions_file)


if __name__ == '__main__':
    cilogger.cilogger.rootlogger.setLevel('DEBUG')
    main()
