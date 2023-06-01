import os
import json
from .speech_senth import say


brain_json = os.path.join(os.path.dirname(__file__), 'data', 'brain.json')

with open(brain_json) as f:
    brain = json.load(f)


def toAr(pmt):
    pmt_ar = pmt.split()
    return pmt_ar


def cmd_filter(pmt_ar):
    cmd = []
    ar1 = brain["word_pool"]
    ar2 = pmt_ar
    for str1 in ar1:
        for str2 in ar2:
            if str1 == str2:
                cmd.append(str1)
    return cmd



def handle(pmt):
    pmt_ar = toAr(pmt)
    cmd = cmd_filter(pmt_ar)
    res = cmd
    if len(str(res)) <3:
        res = res + "no cmd"
    return res


