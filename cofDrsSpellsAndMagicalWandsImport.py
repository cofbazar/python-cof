# -*- coding: utf-8 -*-

import re
import bs4
import urllib.request as urlr
import cof.capacities
import cof.ways
import cof.utils
import cof.items
import json
import os
import config.cofConfig
import cilogger.cilogger
log = cilogger.cilogger.ccilogger(__name__)


# @cilogger.cilogger.ftrace
def main():
    url = 'http://co-drs.org/regles/objets-magiques/'
    html = urlr.urlopen(url).read()
    soup = bs4.BeautifulSoup(html, 'html.parser')
    capacities_file = os.path.join(config.cofConfig.config['global']['path']['root'],
                                   config.cofConfig.config['global']['path']['data'],
                                   'capacities.json')

    capacities_list = cof.capacities.Capacities()
    capacities_list.load(capacities_file)

    ways_file = os.path.join(config.cofConfig.config['global']['path']['root'],
                             config.cofConfig.config['global']['path']['data'],
                             'ways.json')

    ways_list = cof.ways.Ways()
    ways_list.load(ways_file)

    # potion_base_price = 50 # 50 pa
    spell_list = ['table-des-parchemins']

    slist = cof.items.Items()
    mwlist = cof.items.Items()

    for t in soup.find_all('table'):
        log.debug('Found table "{}"'.format(t.caption))
        if t.find('caption') and t.caption.find('a') and t.caption.find('a').attrs['id'] in spell_list:
            log.debug('Found caption "{}"'.format(t.caption))
            voie = t.find_all('a', href=re.compile(r'/voies/'))
            log.debug('Found voie "{}"'.format(voie))
            for h in voie:
                log.debug('Found link "{}"'.format(h['href']))
                w = ways_list.get_by_id((h['href']))
                for cid in w.capacities:
                    cap = capacities_list.get_by_id(cid)
                    if cap is not None:
                        for magical_level, way_rank_list in config.cofConfig.config['spells']['magical_level'].items():
                            if cap.way_rank in way_rank_list:
                                it = cof.items.Spell(
                                    oid=cof.utils.string_to_id('spell-{}'.format(cap.name.lower(), magical_level)),
                                    name='Parchemin - {}'.format(cap.name),
                                    full_description=cap.full_description,
                                    short_description=cap.short_description,
                                    way_rank=cap.way_rank,
                                    magical_level=magical_level,
                                    range=cap.range,
                                    area=cap.area,
                                    duration=cap.duration,
                                    category="Magique",
                                    creature=cap.creature,
                                    skill=cap.skill,
                                    quantity=1,
                                    defense=cap.defense,
                                    attack=cap.attack,
                                    base_item=cof.utils.string_to_id(f"spell-{cap.name.lower()}"),
                                    special_property=cap.special_property,
                                    weight=config.cofConfig.config['spells']['weight'],
                                    use=config.cofConfig.config['spells']['use'])
                                it.cost = config.cofConfig.config['spells']['cost'](it)
                                it.update(config.cofConfig.config['spells']['addons'])
                                slist.add(it)

                        for magical_level, data in config.cofConfig.config['magicwands']['magical_level'].items():
                            log.debug('Data : {}'.format(data))
                            if cap.way_rank in data['way_rank_list']:
                                it = cof.items.MagicalWand(
                                    oid=cof.utils.string_to_id('magic-wand-{}'.format(cap.name.lower(),
                                                                                         magical_level)),
                                    name='Baguette - {}'.format(cap.name),
                                    full_description=cap.full_description,
                                    short_description=cap.short_description,
                                    way_rank=cap.way_rank,
                                    magical_level=magical_level,
                                    range=cap.range,
                                    area=cap.area,
                                    hands=1,
                                    duration=cap.duration,
                                    category="Magique",
                                    skill=cap.skill,
                                    quantity=1,
                                    creature=cap.creature,
                                    defense=cap.defense,
                                    attack=cap.attack,
                                    base_item=cof.utils.string_to_id(f"magic-wand-{cap.name.lower()}"),
                                    special_property=cap.special_property,
                                    weight=config.cofConfig.config['magicwands']['weight'],
                                    use=data['use'])
                                it.cost = config.cofConfig.config['magicwands']['cost'](it)
                                it.update(config.cofConfig.config['magicwands']['addons'])
                                it.full_description += f"{it.full_description} Cette baguette contient " \
                                                       f"{data['use']} charges."
                                mwlist.add(it)

    spells_file = os.path.join(config.cofConfig.config['global']['path']['root'],
                               config.cofConfig.config['global']['path']['data'],
                               'spells.json')
    mw_file = os.path.join(config.cofConfig.config['global']['path']['root'],
                           config.cofConfig.config['global']['path']['data'],
                           'magicalwands.json')

    slist.save(spells_file)
    mwlist.save(mw_file)


if __name__ == '__main__':
    cilogger.cilogger.rootlogger.setLevel('DEBUG')
    main()
