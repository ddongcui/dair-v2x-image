# -*- coding: utf-8 -*-
import json
from tqdm import tqdm 
import os 
import pdb
w = 1920
h = 1080
jsons = os.listdir('./labels')
type_dict = {
    "Pedestrian": 0,
    "Motorcyclist": 1,
    "Car": 2,
    "Cyclist": 3,
    "Van": 4,
    "Truck": 5,
    "Bus": 6,
    "Barrowlist": 7
}
for j in tqdm(jsons):
    j_file = os.path.join('./labels',j)
    with open(j_file, 'r') as f:
        data = json.load(f)

    txt_file = os.path.join('./txt',j.split('.')[0]+'.txt')

    # ¿¿txt¿¿¿¿¿¿¿
    with open(txt_file, 'w') as f:
        for item in data:
            # ¿¿type
            type_ = item['type']
            if type_ != 'Trafficcone':
                # ¿¿2d_box
                type_ = type_dict[type_]
                box = item['2d_box']
                # ¿¿¿¿
                x = (box['xmin'] + box['xmax']) / (2 * w)
                y = (box['ymin'] + box['ymax']) / (2 * h)
                width = (box['xmax'] - box['xmin']) / w
                height = (box['ymax'] - box['ymin']) / h
                # ¿¿¿txt¿¿
                f.write(f'{type_} {x:.6f} {y:.6f} {width:.6f} {height:.6f}\n')

