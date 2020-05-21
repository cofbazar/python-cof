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
def get_capacite(curl):
    chtml = urlr.urlopen(curl).read()
    csoup = bs4.BeautifulSoup(chtml, 'html.parser')
    strong_regex = re.compile(r'^\s*\d+\.\s+(.+?)\s+(\(L\)\s+(\*\s+)?)?:\s+$')
    name = ''
    limited = False
    full_description = ''
    d = csoup.find('div', attrs={'class': 'entry-content'})
    if d is not None and d.find_all(['strong', 'p']):
        strong = sanitize(d.find('strong').text)
        t = strong_regex.match(strong)
        if t:
            name = t.group(1)
            if t.lastindex > 1:
                limited = True

            full_description = sanitize(d.find('p').text)
        else:
            log.warning('Name not found for capacity "{}"'.format(strong))
    return {'cid': curl, 'name': name, 'full_description': full_description, 'limited': limited}

@cilogger.cilogger.ftrace
def main():

    url = 'http://co-drs.org/capacites/'
    html = urlr.urlopen(url).read()
    soup = bs4.BeautifulSoup(html, 'html.parser')
    capacities_file = os.path.join(config.cofConfig.config['global']['path']['root'],
                                   config.cofConfig.config['global']['path']['data'],
                                   'capacities.json')
    ways_file = os.path.join(config.cofConfig.config['global']['path']['root'],
                             config.cofConfig.config['global']['path']['data'],
                             'ways.json')

    # potion_list = ['table-des-potions-de-soin', 'table-des-potions-communes', 'table-des-potions-rares']
    # parchemin_list = ['table-des-parchemins']

    entry_content = soup.find('div', attrs={'class': 'entry-content'})
    # jlist = []

    clist = cof.capacities.Capacities()
    wlist = cof.ways.Ways()

    for div in entry_content.find_all('div'):
        capacity_href_regex = re.compile(r'/capacites/')
        way_href_regex = re.compile(r'/voies/')
        rank_level_regex = re.compile(r'.*rang\s+')
        capacity_url = div.find('a',  href=capacity_href_regex)['href']
        capacity_name = div.find('a',  href=capacity_href_regex).text
        if div.find('a',  href=way_href_regex) is not None:
            way_url = div.find('a',  href=way_href_regex)['href']
            way_name = div.find('a',  href=way_href_regex).text
        else:
            if capacity_url in config.cofConfig.config['capacities']:
                way_url = config.cofConfig.config['capacities'][capacity_url]['wid']
            else:
                raise RuntimeError('Unable to found way ID for capacity ID "{}"'.format(capacity_url))
            way_name = None
        way_rank = int(rank_level_regex.sub('', div.text))
        cjson = get_capacite(capacity_url)

        w = cof.ways.Way(oid=way_url, name=way_name)
        w.add_capacity(capacity_url)
        c = cof.capacities.Capacity(oid=capacity_url, name=capacity_name, wid=way_url, way_rank=way_rank,
                                    full_description=cjson['full_description'], limited=cjson['limited'])
        c.update(config.cofConfig.config['capacities']['addons'])
        wlist.add(w)
        clist.add(c)

    clist.save(capacities_file)
    wlist.save(ways_file)


if __name__ == '__main__':
    cilogger.cilogger.rootlogger.setLevel('TRACE')
    main()
