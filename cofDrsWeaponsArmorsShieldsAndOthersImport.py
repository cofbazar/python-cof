# -*- coding: utf-8 -*-

import re
import bs4
import urllib.request as urlr
import cof.capacities
import cof.utils
import cof.items
import cof.properties
import json
import config.cofConfig as ccofC
import unicodedata
import os
import copy
import cilogger.cilogger
from ClusterShell.NodeSet import RangeSet
log = cilogger.cilogger.ccilogger(__name__)


@cilogger.cilogger.ftrace
def gen_weapons(base_item, flavor_id, flavor, magical_level):
    fitem = copy.copy(base_item)
    fitem.oid = "{}-{}+{}".format(base_item.oid, flavor_id, magical_level)
    fitem.magical_level = magical_level
    for a, v in flavor.items():
        if hasattr(fitem, a):
            setattr(fitem, a, v(fitem, magical_level))
    log.debug('Generated item : {} ({}) from {}'.format(fitem.oid, fitem.name, base_item.oid))
    return fitem


@cilogger.cilogger.ftrace
def main():
    url = 'http://co-drs.org/regles/equipement/'
    html = urlr.urlopen(url).read()
    soup = bs4.BeautifulSoup(html, 'html.parser')

    w_list = ['table-des-armes-de-contact', 'table-des-armes-a-distance']
    a_list = ['table-des-armures-et-des-boucliers']
    material_list = ['table-du-materiel']
    mount_char_list = ['table-des-montures-et-des-chariots']
    inn_list = ['table-des-consommations-auberge']
    real_estate_list = ['table-des-biens-immobiliers']

    ilist = {
        'weapons': {
            'list': cof.items.Items(),
            'item': lambda loid, lname: cof.items.Weapon(oid=loid, name=lname)
        },
        'armors': {
            'list': cof.items.Items(),
            'item': lambda loid, lname: cof.items.Armor(oid=loid, name=lname)
        },
        'robes': {
            'list': cof.items.Items(),
            'item': lambda loid, lname: cof.items.Robe(oid=loid, name=lname)
        },
        'bracers': {
            'list': cof.items.Items(),
            'item': lambda loid, lname: cof.items.Bracer(oid=loid, name=lname)
        },
        'rings': {
            'list': cof.items.Items(),
            'item': lambda loid, lname: cof.items.Ring(oid=loid, name=lname)
        },
        'cloaks': {
            'list': cof.items.Items(),
            'item': lambda loid, lname: cof.items.Cloak(oid=loid, name=lname)
        },
        'shields': {
            'list': cof.items.Items(),
            'item': lambda loid, lname: cof.items.Shield(oid=loid, name=lname)
        },
        'mounts': {
            'list': cof.items.Items(),
            'item': lambda loid, lname: cof.items.Mount(oid=loid, name=lname)
        },
        'chars': {
            'list': cof.items.Items(),
            'item': lambda loid, lname: cof.items.Char(oid=loid, name=lname)
        },
        'materials': {
            'list': cof.items.Items(),
            'item': lambda loid, lname: cof.items.Material(oid=loid, name=lname)
        },
        'inns': {
            'list': cof.items.Items(),
            'item': lambda loid, lname: cof.items.Inn(oid=loid, name=lname)
        },
        'realestates': {
            'list': cof.items.Items(),
            'item': lambda loid, lname: cof.items.RealEstate(oid=loid, name=lname)
        },
        'helmets': {
            'list': cof.items.Items(),
            'item': lambda loid, lname: cof.items.Helmet(oid=loid, name=lname)
        },
    }

    for t in soup.find_all('table'):
        if t.find('caption') and t.caption.find('a') and t.caption.find('a').attrs['id'] \
                in w_list + a_list + material_list + mount_char_list + inn_list + real_estate_list:
            log.debug('Found caption "{}"'.format(t.caption))
            keys = None
            for tr in t.find_all('tr'):
                ckey = 'undefined-attribute'
                oid = ''
                itmp = None
                if tr.find_all('th'):
                    keys = [cof.utils.string_to_id(k.text) for k in tr.find_all('th')]
                if tr.find('td'):
                    log.debug('TR : {}'.format(tr))
                    w = dict(zip(keys, [unicodedata.normalize("NFKD", v.text) for v in tr.find_all('td')]))
                    log.debug('{}'.format(w))
                    if t.caption.find('a').attrs['id'] in w_list:
                        tdid = 'armes'
                        ckey = 'weapons'
                        oid = cof.utils.string_to_id(w[tdid])
                        log.debug('Generated oid : "{}"'.format(oid))
                        name = w[tdid]
                        itmp = cof.items.Weapon(oid=oid, name=name)
                    elif t.caption.find('a').attrs['id'] in a_list:
                        tdid = 'armures'
                        oid = cof.utils.string_to_id(w[tdid])
                        name = w[tdid]
                        if oid in ccofC.config['armors']['ids']:
                            ckey = 'armors'
                            itmp = cof.items.Armor(oid=oid, name=name)
                        elif oid in ccofC.config['shields']['ids']:
                            ckey = 'shields'
                            itmp = cof.items.Shield(oid=oid, name=name)
                        else:
                            log.error('Unknown item type : not a shield, not an armor...')
                    elif t.caption.find('a').attrs['id'] in material_list:
                        tdid = 'objets'
                        ckey = 'materials'
                        oid = cof.utils.string_to_id(w[tdid])
                        log.debug('Generated oid : "{}"'.format(oid))
                        name = w[tdid]
                        itmp = cof.items.Material(oid=oid, name=name)
                    elif t.caption.find('a').attrs['id'] in mount_char_list:
                        tdid = 'montures-chariots'
                        oid = cof.utils.string_to_id(w[tdid])
                        log.debug('Generated oid : "{}"'.format(oid))
                        name = w[tdid]
                        if oid in ccofC.config['mounts']['ids']:
                            ckey = 'mounts'
                            itmp = cof.items.Mount(oid=oid, name=name)
                        elif oid in ccofC.config['chars']['ids']:
                            ckey = 'chars'
                            itmp = cof.items.Char(oid=oid, name=name)
                        else:
                            log.error('Unknown item type : not a char, not a mount...')
                    elif t.caption.find('a').attrs['id'] in inn_list:
                        tdid = 'achats'
                        ckey = 'inns'
                        oid = cof.utils.string_to_id(w[tdid])
                        log.debug('Generated oid : "{}"'.format(oid))
                        name = w[tdid]
                        itmp = cof.items.Inn(oid=oid, name=name)
                    elif t.caption.find('a').attrs['id'] in real_estate_list:
                        tdid = 'biens'
                        ckey = 'realestates'
                        oid = cof.utils.string_to_id(w[tdid])
                        log.debug('Generated oid : "{}"'.format(oid))
                        name = w[tdid]
                        itmp = cof.items.RealEstate(oid=oid, name=name)

                    itmplist = []
                    if ckey in ccofC.config and 'split' in ccofC.config[ckey]:
                        if oid in ccofC.config[ckey]['split']:
                            for noid in ccofC.config[ckey]['split'][oid]:
                                nitem = copy.copy(itmp)
                                nitem.oid = noid
                                nitem.update(ccofC.config[ckey]['split'][oid])
                                itmplist.append(nitem)
                        else:
                            itmplist.append(itmp)
                    else:
                        itmplist.append(itmp)

                    for i in itmplist:
                        if w['prix'] == '-':
                            i.cost = cof.properties.Cost(value=0, unit='pa').iso()
                        elif '-' in w['prix']:
                            log.warning('Cost range not implemeted ("{}")...'.format(w['prix']))
                            # i.cost = cof.properties.Cost(value=0, unit='pa')
                        else:
                            cost_regex = re.compile(r'^(.+)\s+(pp|po|pa|pc)$')
                            m = cost_regex.match(w['prix'])
                            if m:
                                value = int(m.group(1).replace(' ', ''))
                                unit = m.group(2)
                                i.cost = cof.properties.Cost(value=value, unit=unit).iso()
                            else:
                                log.error('Unable to parse cost "{}" with regex "{}" ...'.format(w['prix'], cost_regex))

                        if ckey in ccofC.config and 'addons' in ccofC.config[ckey]:
                            i.update(ccofC.config[ckey]['addons'])

                        ilist[ckey]['list'].add(i)

                        if ckey in ccofC.config and 'flavors' in ccofC.config[ckey]:
                            for flavor_id, flavor in ccofC.config[ckey]['flavors'].items():
                                if 'exclude' not in flavor or (hasattr(i, 'base_item') and
                                                               i.base_item not in flavor['exclude']):
                                    if isinstance(flavor['magical_levels'], list):
                                        for magical_level in flavor['magical_levels']:
                                            fi = gen_weapons(i, flavor_id, flavor, magical_level)
                                            ilist[ckey]['list'].add(fi)
                                            for f_id, f in ccofC.config[ckey]['flavors'].items():
                                                if 'exclude' not in f or ( hasattr(i, 'base_item') and
                                                                           i.base_item not in f['exclude']):
                                                    if not isinstance(f['magical_levels'], list):
                                                        if f_id not in ccofC.config['global']['unique-flavors']:
                                                            ifi = gen_weapons(fi, f_id, f,
                                                                              fi.magical_level + f['magical_levels'])
                                                            ilist[ckey]['list'].add(ifi)
                                    else:
                                        fi = gen_weapons(i, flavor_id, flavor, flavor['magical_levels'])
                                        ilist[ckey]['list'].add(fi)

    for itype in ilist:

        if 'others' in ccofC.config[itype]:
            for oid, data in ccofC.config[itype]['others'].items():
                item = ilist[itype]['item'](oid, data['name'])
                item.update({oid: {k: v for k, v in data.items() if not callable(v)}})
                item.cost = data['cost'](item)

                # Etrange ? on ne sait pas bien a quoi ça sert ...
                if 'exclude' not in data or (hasattr(item, 'base_item') and item.base_item not in data['exclude']):
                    ilist[itype]['list'].add(item)

                if itype in ccofC.config and 'flavors' in ccofC.config[itype]:
                    for flavor_id, flavor in ccofC.config[itype]['flavors'].items():
                        if 'exclude' not in flavor or (hasattr(item, 'base_item') and
                                                       item.base_item not in flavor['exclude']):
                            if isinstance(flavor['magical_levels'], list):
                                for magical_level in flavor['magical_levels']:
                                    fi = gen_weapons(item, flavor_id, flavor, magical_level)
                                    ilist[itype]['list'].add(fi)
                                    for f_id, f in ccofC.config[itype]['flavors'].items():
                                        if 'exclude' in f:
                                            log.debug('Exclude list : {}'.format(f['exclude']))
                                        if 'exclude' not in f or (hasattr(fi, 'base_item') and
                                                                  fi.base_item not in f['exclude']):
                                            if not isinstance(f['magical_levels'], list):
                                                if f_id not in ccofC.config['global']['unique-flavors']:
                                                    ifi = gen_weapons(fi, f_id, f,
                                                                      fi.magical_level + f['magical_levels'])
                                                    ilist[itype]['list'].add(ifi)
                                        else:
                                            log.warning('Exclude oid {} from flavor "{}": {}'.format(fi.oid,
                                                                                                     f_id,
                                                                                                     f['exclude']))
                            else:
                                fi = gen_weapons(item, flavor_id, flavor, flavor['magical_levels'])
                                ilist[itype]['list'].add(fi)

    for l in ilist:
        item_file = os.path.join(ccofC.config['global']['path']['root'],
                                 ccofC.config['global']['path']['data'],
                                 '{}.json'.format(l))
        ilist[l]['list'].save(item_file)


if __name__ == '__main__':
    cilogger.cilogger.rootlogger.setLevel('DEBUG')
    main()
