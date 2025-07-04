# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
import torch.utils.data
import torchvision
from .kitti import build as build_kitti
from .coco import build1 as build_kitti2coco
from .coco import build as build_coco
from .kitti_eval import get_kitti_api_from_dataset


def get_coco_api_from_dataset(dataset):
    for _ in range(10):
        # if isinstance(dataset, torchvision.datasets.CocoDetection):
        #     break
        if isinstance(dataset, torch.utils.data.Subset):
            dataset = dataset.dataset
    if isinstance(dataset, torchvision.datasets.CocoDetection):
        return dataset.coco


def build_dataset(image_set, args):
    if args.dataset_file == 'coco':
        if args.kitti2coco:
            return build_kitti2coco(image_set, args)
        else:
            return build_coco(image_set, args)
    if args.dataset_file == 'coco_panoptic':
        # to avoid making panopticapi required for coco
        from .coco_panoptic import build as build_coco_panoptic
        return build_coco_panoptic(image_set, args)
    if args.dataset_file == 'kitti':
        return build_kitti(image_set, args)
    raise ValueError(f'dataset {args.dataset_file} not supported')
