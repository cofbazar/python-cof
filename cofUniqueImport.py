# -*- coding: utf-8 -*-

from cof.items import Items
from cof.capacities import Capacities
from config.cofConfig import config as ccofC
from config.cofConfigUniques import uniques as ccofCU
from cof.utils import string_to_id
from copy import copy
import os
import cilogger.cilogger
log = cilogger.cilogger.ccilogger(__name__)


@cilogger.cilogger.ftrace
def main():
    capacities_file = os.path.join(ccofC['global']['path']['root'],
                                   ccofC['global']['path']['data'],
                                   'capacities.json')

    capacities_list = Capacities()
    capacities_list.load(capacities_file)

    ilist = Items()
    for itype in ccofCU:
        for oid, idata in ccofCU[itype].items():
            log.debug(f"New unique object : {oid}")
            # Standard import
            import importlib
            # Load "module.submodule.MyClass"
            iclass = getattr(importlib.import_module("cof.items"), itype)
            # Instantiate the class (pass arguments to the constructor, if needed)

            if "capacity" in idata:
                cap = capacities_list.get_by_id(idata["capacity"])
                if cap is not None:
                    item = iclass(
                        oid=oid,
                        full_description=cap.full_description,
                        short_description=cap.short_description,
                        way_rank=cap.way_rank,
                        range=cap.range,
                        area=cap.area,
                        duration=cap.duration,
                        category="Magique",
                        skill=cap.skill,
                        defense=cap.defense,
                        attack=cap.attack,
                        magical_level=cap.way_rank,
                        special_property=cap.special_property,
                    )

                    item.name = f"{item.itype} - {cap.name}"
                    item.base_item = item.oid
                    if 'cost' in ccofC[ccofC[itype]]:
                        item.cost = ccofC[ccofC[itype]]['cost'](item)
                    if 'weight' in ccofC[ccofC[itype]]:
                        item.weight = ccofC[ccofC[itype]]['weight']
                    del idata["capacity"]
                else:
                    item = iclass(oid=oid)
            else:
                item = iclass(oid=oid)

            item.base_item = item.oid
            # We need first set static data as they may be useful to compute dynamical attributes
            item.update({oid: {k: v for k, v in idata.items() if not callable(v)}})

            if "magical_levels" in idata:
                for l in idata["magical_levels"]:
                    nitem = copy(item)
                    nitem.magical_level = l
                    for attribute, func in {k: v for k, v in idata.items() if callable(v)}.items():
                        log.debug(f"Update attribute '{attribute}' with computed value '{func(nitem)}'")
                        nitem.update({oid: {attribute: func(nitem)}})
                    nitem.oid = f"{nitem.oid}+{l}"
                    ilist.add(nitem)
                del idata["magical_levels"]
            elif "flavors" in idata:
                for f in idata["flavors"]:
                    nitem = copy(item)
                    if 'oid' in idata and callable(idata['oid']):
                        nitem.oid = idata['oid'](item, f)
                        log.debug(f"New item oid '{nitem.oid}' for object {nitem.__class__.__name__}")
                    for attribute, func in {k: v for k, v in idata.items() if callable(v) if not k == "oid"}.items():
                        log.debug(f"Update attribute '{attribute}' with computed value '{func(item, f)}'")
                        nitem.update({nitem.oid: {attribute: func(item, f)}})

                    ilist.add(nitem)
                del idata["flavors"]
            else:
                # We need first set static data as they may be useful to compute dynamical attributes
                item.update({oid: {k: idata[k](item) for k, v in idata.items() if callable(v)}})
                ilist.add(item)

    item_file = os.path.join(ccofC['global']['path']['root'],
                             ccofC['global']['path']['data'],
                             'uniques.json')
    ilist.save(item_file)


if __name__ == '__main__':
    cilogger.cilogger.rootlogger.setLevel('DEBUG')
    main()
