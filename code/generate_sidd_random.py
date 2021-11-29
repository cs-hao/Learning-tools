#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import shutil

from glob import glob
from tqdm import tqdm
import numpy as np
import os
from natsort import natsorted
import cv2
from joblib import Parallel, delayed
import multiprocessing
import argparse

parser = argparse.ArgumentParser(description='Generate patches from Full Resolution images')
parser.add_argument('--src_hq_dir', default='E:/data-hao/SIDD_Medium_Srgb/hq', type=str, help='Directory for full hq resolution images')
parser.add_argument('--src_lq_dir', default='E:/data-hao/SIDD_Medium_Srgb/lq', type=str, help='Directory for full lq resolution images')
parser.add_argument('--tar_hq_dir', default='E:/data-hao/dataset-Noise/SIDD/train/hq',type=str, help='Directory for hq image patches')
parser.add_argument('--tar_lq_dir', default='E:/data-hao/dataset-Noise/SIDD/train/lq',type=str, help='Directory for lq image patches')
parser.add_argument('--ps', default=256, type=int, help='Image Patch Size')
parser.add_argument('--num_patches', default=300, type=int, help='Number of patches per image')
parser.add_argument('--num_cores', default=6, type=int, help='Number of CPU Cores')

args = parser.parse_args()

src_hq = args.src_hq_dir
src_lq = args.src_lq_dir
tar_hq = args.tar_hq_dir
tar_lq = args.tar_lq_dir

PS = args.ps
NUM_PATCHES = args.num_patches
NUM_CORES = args.num_cores

noisy_patchDir = tar_lq
clean_patchDir = tar_hq

if not os.path.exists(noisy_patchDir):
    os.makedirs(noisy_patchDir)

if not os.path.exists(clean_patchDir):
    os.makedirs(clean_patchDir)

#get sorted folders
noisy_files = natsorted(glob(os.path.join(src_lq, '*.PNG')))
clean_files = natsorted(glob(os.path.join(src_hq, '*.PNG')))


def save_files(i):
    noisy_file, clean_file = noisy_files[i], clean_files[i]
    noisy_img = cv2.imread(noisy_file)
    clean_img = cv2.imread(clean_file)

    H = noisy_img.shape[0]
    W = noisy_img.shape[1]
    for j in range(NUM_PATCHES):
        rr = np.random.randint(0, H - PS)
        cc = np.random.randint(0, W - PS)
        noisy_patch = noisy_img[rr:rr + PS, cc:cc + PS, :]
        clean_patch = clean_img[rr:rr + PS, cc:cc + PS, :]

        cv2.imwrite(os.path.join(noisy_patchDir, '{}_{}.png'.format(i+1,j+1)), noisy_patch)
        cv2.imwrite(os.path.join(clean_patchDir, '{}_{}.png'.format(i+1,j+1)), clean_patch)

Parallel(n_jobs=NUM_CORES)(delayed(save_files)(i) for i in tqdm(range(len(noisy_files))))
# list_hq = sorted(os.listdir('E:/data-hao/SIDD_Medium_Srgb/LQ_Patch'))
# print(list_hq)


# 将 SIDD 数据集中的LQ和HQ图片分类，因为下载下来的时候是在各个文件夹中的
# 将文件分类后，HQ和LQ分类成两类文件夹
def gci(inpath, lqpath, hqpath):
    files = os.listdir(inpath)
    for fi in files:
        fi_d = os.path.join(inpath, fi)
        if os.path.isdir(fi_d):
            gci(fi_d, lqpath, hqpath)
        else:
            # filepath = os.path.join(inpath, fi_d)
            filename = os.path.basename(fi_d)
            if 'NOISY' in filename:
                # print(filename)
                shutil.move(fi_d, os.path.join(lqpath, filename))
                # print(os.path.join(lqpath, filename))
            else:
                shutil.move(fi_d, os.path.join(hqpath, filename))
                # print(os.path.join(hqpath, filename))

# 递归遍历/root目录下所有文件
# gci('E:/data-hao/SIDD_Medium_Srgb/Data', 'E:/data-hao/SIDD_Medium_Srgb/LQ', 'E:/data-hao/SIDD_Medium_Srgb/HQ')