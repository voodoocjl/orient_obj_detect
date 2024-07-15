conda create --name openmmlab python=3.8 -y
conda activate openmmlab
conda install pytorch==1.8.0 torchvision==0.9.0 cudatoolkit=10.2 -c pytorch
pip install -U openmim
mim install mmcv-full
mim install mmdet\<3.0.0

cd ~
git clone https://github.com/open-mmlab/mmrotate.git
cd mmrotate
pip install -v -e .

cd ~
git clone https://github.com/voodoocjl/orient_obj_detect.git
cd orient_obj_detect
./run.sh

