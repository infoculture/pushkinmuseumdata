#!/usr/bin/env python
# Require typer, please use "pip install typer"
import json
import typer
import csv

import pprint
DATA_FILE = '../data/objects/objects-enhanced-red.json'


def toraw():
    fout = open('../data/objects/refined/data.jsonl', 'w', encoding='utf8')
    data = json.load(open(DATA_FILE, 'r', encoding='utf8'))
    for key, value in data.items():
        value['id'] = key
        fout.write(json.dumps(value, ensure_ascii=False) + '\n')

    fout.close()
    pass

def toshortened():
    fout = open('../data/objects/refined/data_shortened.jsonl', 'w', encoding='utf8')
    data = json.load(open(DATA_FILE, 'r', encoding='utf8'))
    for key, value in data.items():
        value['id'] = key
        if len(value['gallery']) > 0:
            image = list(value['gallery'].values())[0]
            value['image_url'] = image['url']
            if 'msannotation' in image.keys():
                value['msannotation'] = list(value['gallery'].values())[0]['msannotation']
            else:
                value['msannotation'] = ''
        del value['gallery']
        fout.write(json.dumps(value, ensure_ascii=False) + '\n')

    fout.close()
    pass



def refine():
    toraw()
    toshortened()
    pass
                    

if __name__ == "__main__":
    typer.run(refine)
