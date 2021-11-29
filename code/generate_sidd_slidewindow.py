import os
from glob import glob
import cv2
import argparse
from joblib import Parallel, delayed
from tqdm import tqdm
from natsort import natsorted

parser = argparse.ArgumentParser(description='Generate patches from Full Resolution images')
parser.add_argument('--src_hq_dir', default='E:/data-hao/SIDD_Medium_Srgb/hq', type=str,
                    help='Directory for full hq resolution images')
parser.add_argument('--src_lq_dir', default='E:/data-hao/SIDD_Medium_Srgb/lq', type=str,
                    help='Directory for full lq resolution images')
parser.add_argument('--tar_hq_dir', default='E:/data-hao/dataset-Noise/SIDD/train_v3/hq', type=str,
                    help='Directory for hq image patches')
parser.add_argument('--tar_lq_dir', default='E:/data-hao/dataset-Noise/SIDD/train_v3/lq', type=str,
                    help='Directory for lq image patches')
parser.add_argument('--ps', default=256, type=int, help='Image Patch Size')
parser.add_argument('--num_cores', default=6, type=int, help='Number of CPU Cores')

args = parser.parse_args()

src_hq = args.src_hq_dir
src_lq = args.src_lq_dir
tar_hq = args.tar_hq_dir
tar_lq = args.tar_lq_dir

if not os.path.exists(tar_hq):
    os.makedirs(tar_hq)

if not os.path.exists(tar_lq):
    os.makedirs(tar_lq)

# get sorted folders
noisy_files = natsorted(glob(os.path.join(src_lq, '*.PNG')))
clean_files = natsorted(glob(os.path.join(src_hq, '*.PNG')))

# print(len(noisy_files))
# print(len(clean_files))
pch_size = args.ps
stride = pch_size - pch_size//2


def save_files(ii):
    im_noisy_int8 = cv2.imread(noisy_files[ii])
    H, W, _ = im_noisy_int8.shape
    im_gt_int8 = cv2.imread(clean_files[ii])
    ind_H = list(range(0, H - pch_size + 1, stride))
    if ind_H[-1] < H - pch_size:
        ind_H.append(H - pch_size)
    ind_W = list(range(0, W - pch_size + 1, stride))
    print(len(ind_H), len(ind_W))
    if ind_W[-1] < W - pch_size:
        ind_W.append(W - pch_size)
    count = 1
    for start_H in ind_H:
        for start_W in ind_W:
            pch_noisy = im_noisy_int8[start_H:start_H + pch_size, start_W:start_W + pch_size, ]
            pch_gt = im_gt_int8[start_H:start_H + pch_size, start_W:start_W + pch_size, ]
            cv2.imwrite(os.path.join(tar_lq, '{}_{}.png'.format(ii + 1, count + 1)), pch_noisy)
            cv2.imwrite(os.path.join(tar_hq, '{}_{}.png'.format(ii + 1, count + 1)), pch_gt)
            count += 1

Parallel(n_jobs=10)(delayed(save_files)(i) for i in tqdm(range(len(noisy_files))))
print('Finish!\n')
