# LaMa-Image-Inpainting
Final Project for CV

## 环境配置（for Linux）

tips:该环境是运行项目内所有方法的充分非必要条件。

1.安装conda

2.

```shell
conda env create -f environment.yml
conda activate relama
conda install pytorch torchvision torchaudio cudatoolkit=10.2 -c pytorch -y
pip install -r requirement.txt
```

## 测试

### TELEA

修改test_TELEA.py下img、mask和save路径

```shell
python test_TELEA.py
```

### Navier_Stokes

修改test_NS.py下img、mask和save路径

```shell
python test_NS.py
```

### Context_encoder

下载对应模型

```shell
cp netG_streetview.pth context_encoder_pytorch/model/
cd context_encoder_pytorch
python test_one.py --netG model/netG_streeview.pth --test_image [testimg_path]
```

### ICT

下载对应模型

```shell
unzip ckpts_ICT.zip
python run.py --input_image [test_image_folder] \
              --input_mask [test_mask_folder] \
              --sample_num 1  --save_place [save_path] \
              --ImageNet
```

可选：```--ImageNet``` ```--FFHQ``` ```--Places2_Nature```

tips:文件路径请使用绝对路径

### LaMa

下载对应模型

```shell
cd lama_origin
export TORCH_HOME=$(pwd) && export PYTHONPATH=.
unzip lama-models.zip
```

```shell
python bin/predict.py model.path=$(pwd)/big-lama indir=$(pwd)/LaMa_test_images outdir=$(pwd)/output
```

### LaMa_ours

下载对应模型

```shell
cd lama_ours
export TORCH_HOME=$(pwd) && export PYTHONPATH=.
```

```shell
python bin/predict.py model.path=$(pwd)/big-lama indir=$(pwd)/LaMa_test_images outdir=$(pwd)/output
```

