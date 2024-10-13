#!/bin/bash

# 复制 test.py 文件
cp change/test.py ~/anaconda3/envs/openmmlab/lib/python3.8/site-packages/mmdet/apis/test.py

# 复制 distributed.py 文件
cp change/distributed.py ~/anaconda3/envs/openmmlab/lib/python3.8/site-packages/torch/nn/parallel/distributed.py

# 复制 distributed_mmcv.py 文件并重命名为 distributed.py
cp change/distributed_mmcv.py ~/anaconda3/envs/openmmlab/lib/python3.8/site-packages/mmcv/parallel/distributed.py

# 复制 dist_utils.py 文件
cp change/dist_utils.py ~/anaconda3/envs/openmmlab/lib/python3.8/site-packages/mmcv/runner/dist_utils.py

cp change/base_module.py ~/anaconda3/envs/openmmlab/lib/python3.8/site-packages/mmcv/runner/base_module.py

cp change/__init__.py ~/anaconda3/envs/openmmlab/lib/python3.8/site-packages/mmcv/__init__.py

cp -r mmrotate/ ~/mmrotate/

cp -r models/ ~/mmrotate/

cp -r mmcv_custom/ ~/mmrotate

pip install timm

