安装：

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

训练：

python -m torch.distributed.launch --nproc_per_node 1 --nnodes M --node_rank N --master_addr='10.12.133.58' --master_port=29501 tools/train.py configs/lsknet/lsk_t_fpn_1x_dota_le90.py --seed 0 --launcher pytorch

M:表示节点个数
N:表示当前节点的标号
master_addr： 主节点的IP地址
master_port：主节点的端口

例如，单节点运行，M=1, N=0

