#!/usr/bin/python

import matplotlib.pyplot as plt
from skimage import exposure, io, util
from skimage.restoration import denoise_nl_means
from skimage.transform import rotate
import numpy as np
import argparse
import os

import sys

parser = argparse.ArgumentParser(description='Overlap cells and neutron autoradiography tracks.')
parser.add_argument('DIR', help='Directory where the pictures are saved.')
parser.add_argument('Number', help='Pictures must be saved in tif format and named "Number"_Cell.tif and "Number"_Neutron.tif.')
args = parser.parse_args()

plt.figure(figsize=(20,10))
cell_img = io.imread(os.path.join(args.DIR,args.Number+"_Cell.tif"))

cell = exposure.equalize_adapthist(cell_img, clip_limit=0.03)
cell = denoise_nl_means(cell, 7, 9, 0.08, multichannel=True)

plt.figure(figsize=(20,10))
track_img = io.imread(os.path.join(args.DIR,args.Number+"_Neutron.tif"))
track_img = util.invert(track_img)

track = exposure.equalize_adapthist(track_img, clip_limit=0.03)
track = denoise_nl_means(track, 7, 9, 0.08, multichannel=True)
track = rotate(track,354,resize=True)

plt.figure(figsize=(20,10))
color_img = np.zeros((1177,1477,4),dtype="float32")
color_img[0:1177,0:1477,0] = track

#color_img[40:1078,0:1376,0]=cell
color_img[40:1078,0:1376,1]=cell
color_img[40:1078,0:1376,2]=cell
color_img[40:1078,0:1376,3]=np.full((1038,1376), 1)

plt.imsave(args.Number+"overlap.png",color_img[40:1078,0:1376])
