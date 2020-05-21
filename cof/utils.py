# -*- coding: utf-8 -*-

""" Module for debugging and displaying data in tables

This module contains useful functions for debugging and displaying data in tables
"""

import sys
import re
import os
import unicodedata
import json
import copy
import cilogger.cilogger
log = cilogger.cilogger.ccilogger(__name__)


def sanitize(t):
    sanitize_regex = re.compile(r'[\s\n]+', re.MULTILINE)
    return sanitize_regex.sub(' ', '{}'.format(t))


def string_to_id(s):
    safe_s = unicodedata.normalize('NFD', s)\
        .encode('ascii', 'ignore')\
        .decode("utf-8")
    id_regex = re.compile(r'[\W_]+', re.MULTILINE)
    return id_regex.sub('-', '{}'.format(safe_s)).lower()


def reduce_mod(mod_list):
    ml = []
    target_list = {}

    mls = [{"mtype": m.mtype, "target": m.target, "die": m.die, "count": m.count} for m in mod_list]
    log.debug(f"Merge mod : {mls}")
    for m in mod_list:
        if m.target in target_list:
            if target_list[m.target].die == m.die:
                if target_list[m.target].mtype == '-':
                    a_mtype = -1
                else:
                    a_mtype = 1
                if m.mtype == '-':
                    b_mtype = -1
                else:
                    b_mtype = 1
                a_count = target_list[m.target].count
                b_count = m.count
                new_count = a_count * a_mtype + b_count * b_mtype
                log.debug(f"Resultat : {new_count} = {a_count} * {a_mtype} + {b_count} * {b_mtype}")
                if new_count < 0:
                    target_list[m.target].mtype = '-'
                    target_list[m.target].count = -1 * new_count
                elif new_count > 0:
                    target_list[m.target].mtype = '+'
                    target_list[m.target].count = new_count
                else:
                    ml.remove(target_list[m.target])
                    target_list.pop(m.target, None)

            else:
                raise RuntimeError("Not handle : different dice for same damage type")
        else:
            nm = copy.copy(m)
            target_list.update({m.target: nm})
            ml.append(nm)
    mls = [{"mtype": m.mtype, "target": m.target, "die": m.die, "count": m.count} for m in ml]
    log.debug(f"Merge mod result: {mls}")
    return ml


def max_dm(damages):
    dm_max = 0.0
    for dm in damages.base + damages.other:
        if dm.die is None:
            d = 1.0
        else:
            d = dm.die
        if dm.mtype == '-':
            m = -1.0
        else:
            m = 1.0

        if dm.count is not None:
            dm_max += dm.count * d * m
    return dm_max


def increase_dice(mod_list):
    ml = []
    for m in mod_list:
        nm = copy.copy(m)
        if m.die is not None:
            if m.die in [4, 6, 8, 10]:
                nm.die = m.die + 2
            elif m.die == 3:
                nm.die = 4
        ml.append(nm)
    return ml


def reduce_malus(mod_list, label, target, reduction):
    ml = []
    for m in mod_list:
        if m.label == label and m.target == target:
            if m.mtype == "-" and (m.count - reduction) > 0:
                nm = copy.copy(m)
                nm.count -= reduction
                ml.append(nm)
        else:
            nm = copy.copy(m)
            ml.append(nm)

    return ml


def get_def_level(mod_list):
    def_level = 0
    for m in mod_list:
        if m.label == "DEF":
            if m.mtype == "+" and m.count > 0:
                def_level += m.count

    return def_level
