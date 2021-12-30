## 项目名称：Re-LaMa Image Inpainting

##### 成员列表：谢雨成、夏鸿、刘源

### 项目描述

图像修复，即修复旧的和变质的图像的艺术，虽然已经存在了很多年，但由于最近图像处理技术的发展，它变得更加受欢迎。随着图像处理工具的改进和数字图像编辑的灵活性，图像自动修复在计算机视觉中得到了重要的应用，也成为图像处理领域一个重要而富有挑战性的研究课题。

本项目对现有的Image Inpainting方法进行比较，并基于Resolution-robust Large Mask Inpainting with Fourier Convolutions方法进行改进，尝试提出一种新的网络结构解决图像修复问题。

1. 阅读Image Inpainting的综述文献，了解该任务的发展历史和近期进展。
2. 参考[🦙 LaMa](https://github.com/saic-mdal/lama)复现论文[Resolution-robust Large Mask Inpainting with Fourier Convolutions](https://arxiv.org/pdf/2109.07161v2.pdf)
3. 尝试复现Image Inpainting任务的其他方法，并比较LaMa和这些方法的区别和优缺点。
4. 尝试在LaMa基础上做一些网络结构或其他方面的改进， 尽可能取得更好的效果。

### 成员分工

综述与文献阅读：谢雨成、夏鸿、刘源

复现和改进LaMa：夏鸿、谢雨成

尝试复现其他方法：刘源、谢雨成

在现有数据集上测试并比较：夏鸿、刘源

### 所用的工具和资源

数据集：CelebA-HQ、ApolloScape、Places等

实现平台：Linux/Windows

第三方库: Pytorch、Numpy、opencv等

计算资源：飞浆AI studio、NVIDIA GeForce GTX 1060

参考资料： 

[Image inpainting: A review](https://arxiv.org/ftp/arxiv/papers/1909/1909.06399.pdf)

[【Paper】Image Inpainting 必读papers- 梁君牧 - 博客园 ](https://www.cnblogs.com/lwp-nicol/p/15016914.html#generative-image-inpainting-with-contextual-attention-1)

[Image Inpainting | Papers With Code](https://paperswithcode.com/task/image-inpainting)

[saic-mdal/lama: 🦙 LaMa Image Inpainting, Resolution-robust Large Mask Inpainting with Fourier Convolutions, WACV 2022 (github.com)](https://github.com/saic-mdal/lama)

[geekyutao/Image-Inpainting: A paper summary of image inpainting (github.com)](https://github.com/geekyutao/Image-Inpainting)
