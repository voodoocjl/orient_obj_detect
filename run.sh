#!/bin/bash

# 复制 test.py 文件
cp change/test.py ~/anaconda3/envs/openmmlab/lib/python3.8/site-packages/mmdet/apis/test.py

# 复制 distributed.py 文件
cp change/distributed.py ~/anaconda3/envs/openmmlab/lib/python3.8/site-packages/torch/nn/parallel/distributed.py

# 复制 distributed_mmcv.py 文件并重命名为 distributed.py
cp change/distributed_mmcv.py ~/anaconda3/envs/openmmlab/lib/python3.8/site-packages/mmcv/parallel/distributed.py distributed.py

# 复制 dist_utils.py 文件
cp change/dist_utils.py ~/anaconda3/envs/openmmlab/lib/python3.8/site-packages/mmcv/runner/dist_utils.py

# 复制 util_distribution.py
cp change/util_distribution.py ~/mmrotate/mmrotate/utils/util_distribution.py

cp mmrotate/ ./mmrotate/

cp models/ ./mmrotate/

pip install timm

