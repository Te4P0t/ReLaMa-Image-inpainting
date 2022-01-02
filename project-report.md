# 项目报告

​	本项目希望通过阅读image inpainting相关的文献，了解该领域的发展历史和近期的研究成果。并通过尝试相关方法，比较这些方法之间的优缺点，通过特定图像查看相应的效果，同时加深对image inpainting任务和各种方法的理解。最终尝试在LaMa网络的基础上进行一些尝试和修改，尽可能取得更好的效果。

## 绪论

​	图像修复（Image inpainting），即修复老旧的和编制的图像的技术。虽然已经存在了很多年，但随着进来图像处理技术的快速进步，得到了更多的关注。随着图像处理工具的改善，自动图像修复变成了计算机视觉领域的一个重要的且富有挑战性的任务。

​	我们可以将现有的图像修复的方法分为以下四类，传统的，和基于CNN的，基于GAN的和基于Transformer的。

​	在传统的方法中，主要又可分为两类，一类是基于补丁的方法（Patch-based），主要通过在图像未损坏的部分搜索良好的替换补丁，然后复制到需要修复的区域。如Markov Random Field (MRF)。另一类是基于扩散的方法（Diffusion-based），主要通过从图像缺失部分的边界出发，逐渐平滑地像缺失区域内部进行填充。

​	在近10年中，由于CNN在各种计算机视觉任务中的优秀表现和潜力，CNN也逐渐被在图像修复领域。许多基于卷积神经网络的网络或encoder-decoder的结构被提出。

​	基于GAN的网络使用一种由粗到细的网络和上下文注意力模块，在inpainting任务中取得了很好的效果。现有的基于GAN的图像修复网络较少。

​	在近1-2年中，Transformer被移植到了视觉领域，并取得了出人意料的结果。这也为各类计算机视觉任务提供了一种新的可行的且效果优秀的方法。基于Transformer的模型弥补了CNN感受野不足的缺点，在图像修复领域也取得了出人意料的效果。

## 各方法的实现细节

### 传统的（Traditional-Based)

#### Navier-Stokes, Fluid Dynamics, and Image and Video Inpainting

https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=990497&tag=1

​	该算法是基于流体动力学，并利用的偏微分方程。基本原理是启发式的。它首先沿着正常区域的边缘向待修补区域移动（因为边界是连续的）。它通过匹配待修复区域中的梯度向量来延伸等照度线（isophotes，由灰度值相等的点练成的线。就像等高线连接高度相同的点一样）。为了实现这个目的，使用了流体动力学中的一些方法。完成这一步之后，通过填充颜色来使这个区域内的灰度值变化最小。

看不大懂说实话。。。

#### An Image Inpainting Technique Based on the Fast Marching Method

https://quelknas.myqnapcloud.com:8081/uploads/PAPERS/JGT04/paper.pdf

数学模型：

![image-20220102121618607](https://te4p0t.github.io/assets/images/typora-user-images/202201021241838.png)

伪代码：

![image-20220102121804332](https://te4p0t.github.io/assets/images/typora-user-images/202201021241082.png)

​	基于快速行进算法（Fast Marching Method）。假设图中一个区域需要修补，算法从边界开始，逐渐进入区域内部。

​	首先填充边界的像素。对需要修复的像素点，取周围小邻域中所有像素点的归一化加权值替代。修复后移动到下一个最近的像素点。

​	FMM确保靠近已知像素的区域首先被修复。

### 基于CNN的（CNN-Based)

#### Context Encoders: Feature Learning by Inpainting

![image-20211229171912001](https://raw.githubusercontent.com/Te4P0t/te4p0t.github.io/main/assets/images/typora-user-images/image-20211229171912001.png)

- 网络结构仿照autoencoders，但是autoencoders只能获得上下文特征，但是无法得到较好的语义上的特征。本文将Image Inpainting的任务类比为word2vec（通过预测给定上下文的单词，从自然语言句子中学习单词表示）。
- 损失函数使用L2 Loss和Adversarial Loss集合，L2 Loss根据上下文信息获得缺失部分的整体结构，Adversarial Loss从分布中选择一个特定的结果（效果上使结果更加真实）。

- Encoder和Decoder都是卷积网络，Encoder和Decoder之间通过channel-wise的全连接层来链接，Encoder用来提取特征，而Decoder则生成图像缺失区域。

##### 网络结构

![image-20211229175300957](https://te4p0t.github.io/assets/images/typora-user-images/202201021241540.png)

Encoder仿照AlexNet结构，由5个卷积层和一个池化层组成。权重随机初始化。

Encoder和Decoder之间由一个Channel-wise fully-connected layer连接。和普通的全连接层不同，该层没有连接不同特征图的参数，只在特征图内传播信息，因此减少了参数量。

Decoder层采用转置卷积（上采样+卷积），直到图片恢复原大小。

##### Loss结构

![image-20211229181526906](https://raw.githubusercontent.com/Te4P0t/te4p0t.github.io/main/assets/images/typora-user-images/image-20211229181526906.png)

![image-20211229181557152](https://raw.githubusercontent.com/Te4P0t/te4p0t.github.io/main/assets/images/typora-user-images/image-20211229181557152.png)

总结：通过Encoder-Decoder网络、结合L2 Loss和对抗Loss，实现比传统意义上范围更大的Image Inpainting。

### 基于Transformer的（Transformer-Based)

#### High-Fidelity Pluralistic Image Completion with Transformers

url:[High-Fidelity Pluralistic Image Completion With Transformers (thecvf.com)](https://openaccess.thecvf.com/content/ICCV2021/papers/Wan_High-Fidelity_Pluralistic_Image_Completion_With_Transformers_ICCV_2021_paper.pdf)

##### 主要困难：

由于CNN的固有属性（如 spatial-invariant kernals），虽然他能够生成细致的纹理信息，但是很难获得全局结构的信息。但是transformer在这方面要有更好的效果（modelint long-term relationship  and generating diverse results）。

##### 改进点：

将CNN和Transformer的优点结合，先利用Transformer生成缺失部分的结构信息，再在此基础上用CNN来补充纹理信息。

##### 成果：

1. 与确定性补全方法相比，图像保真度大大提高。
2. 拥有更好的多样性，能够实现多元化。
3. 在大型mask和通用数据集上有很好的泛化能力。

##### 网络结构：

![image-20211229185329232](https://raw.githubusercontent.com/Te4P0t/te4p0t.github.io/main/assets/images/typora-user-images/image-20211229185329232.png)



### LaMa（Fast Fourier Convlutoins)

#### Resolution-robust Large Mask Inpainting with Fourier Convolutions

##### 针对问题：大尺度的image inpainting。

##### 主要困难：

现有的卷积结构缺乏足够大的感受野。

##### 改进点：

1. 使用了基于快速傅里叶卷积（*fast Fourier convolutions*）的网络结构。在网络的前几层就使感受野覆盖整张图片。
2. 使用了一种高感受野的感知loss。
3. 使用了大尺度的训练mask。

##### 细节

网络结构

![image-20211230191020855](https://te4p0t.github.io/assets/images/typora-user-images/typora-user-imagesimage-20211230191020855.png)

FFC将通道分为两个平行的分支

1. local branch使用传统的卷积
2. global branch使用快速傅里叶变换来获得全局的上下文信息。

FFC遵循以下步骤

![image-20211230191534487](https://te4p0t.github.io/assets/images/typora-user-images/typora-user-imagesimage-20211230191534487.png)

![image-20211230191546477](https://raw.githubusercontent.com/Te4P0t/te4p0t.github.io/main/assets/images/typora-user-images/image-20211230191546477.png)



## 结果

我们尝试了以下几种方法

1. 传统的

   1. **基于快速行进方法（Fast Marching Method, FMM）的图像修复技术**（以下采用简称TELEA）
   2. **Navier-Stokes，流体动力学以及图像和视频修补**（以下简称NS）
2. 基于CNN的

   1. **context-encoder：Feature Learning by Inpainting**（以下简称C_E）
   2. **Pluralistic**（以下简称Plura）
3. 基于Transformer的

   1. **Image Completion Transformer**（以下简称ICT）
4. LaMa
   1. **Resolution-robust Large Mask Inpainting with Fourier Convolutions**（以下简称LaMa）

#### case1:小范围图像修复

|        | 原图                                                         | mask                                                         | with mask                                                    |
| ------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| test_1 | ![img](https://raw.githubusercontent.com/Te4P0t/te4p0t.github.io/main/assets/images/typora-user-images/img.png) | ![mask](https://raw.githubusercontent.com/Te4P0t/te4p0t.github.io/main/assets/images/typora-user-images/mask.png) | ![label_viz](https://raw.githubusercontent.com/Te4P0t/te4p0t.github.io/main/assets/images/typora-user-images/label_viz.png) |
| test_2 | ![img](https://te4p0t.github.io/assets/images/typora-user-images/202201021243011.png) | ![mask_3_2](https://raw.githubusercontent.com/Te4P0t/te4p0t.github.io/main/assets/images/typora-user-images/mask_3_2.png) | ![label_viz](https://te4p0t.github.io/assets/images/typora-user-images/202201021243302.png) |


| TELEA                                                        | NS                                                           | Plura                                                        | LaMa                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| <img src="https://raw.githubusercontent.com/Te4P0t/te4p0t.github.io/main/assets/images/typora-user-images/out_img_1_2.png" alt="out_img_1_2" style="zoom: 33%;" /> | <img src="https://te4p0t.github.io/assets/images/typora-user-images/202201021244556.png" alt="out_img_1_2" style="zoom:33%;" /> | ![image-20220101211858279](https://raw.githubusercontent.com/Te4P0t/te4p0t.github.io/main/assets/images/typora-user-images/image-20220101211858279.png) | <img src="https://raw.githubusercontent.com/Te4P0t/te4p0t.github.io/main/assets/images/typora-user-images/img_1_2_mask.png" alt="img_1_2_mask" style="zoom: 33%;" /> |
| <img src="https://raw.githubusercontent.com/Te4P0t/te4p0t.github.io/main/assets/images/typora-user-images/out_img_3_2.png" alt="out_img_3_2" style="zoom: 33%;" /> | <img src="https://raw.githubusercontent.com/Te4P0t/te4p0t.github.io/main/assets/images/typora-user-images/out_img_3_2.png" style="zoom: 33%;" /> | ![image-20220101212251863](https://raw.githubusercontent.com/Te4P0t/te4p0t.github.io/main/assets/images/typora-user-images/image-20220101212251863.png) | <img src="https://raw.githubusercontent.com/Te4P0t/te4p0t.github.io/main/assets/images/typora-user-images/img_3_2_mask.png" alt="img_3_2_mask" style="zoom: 33%;" /> |

#### case2:区域图像修复

|        | 原图                                                         | mask                                                         | with mask                                                    |
| ------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| test_1 | ![img](https://te4p0t.github.io/assets/images/typora-user-images/202201021239579.png) | ![mask](https://te4p0t.github.io/assets/images/typora-user-images/202201021239321.png) | ![label_viz](https://te4p0t.github.io/assets/images/typora-user-images/202201021239819.png) |
| test_2 | ![img](https://te4p0t.github.io/assets/images/typora-user-images/202201021238301.png) | ![mask_3_1](https://te4p0t.github.io/assets/images/typora-user-images/mask_3_1.png) | ![label_viz](https://te4p0t.github.io/assets/images/typora-user-images/202201021239362.png) |

| TELEA                                                        | NS                                                           | Plura                                                        | LaMa                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| <img src="https://te4p0t.github.io/assets/images/typora-user-images/out_img_1_1.png" alt="out_img_1_1" style="zoom:33%;" /> | <img src="https://te4p0t.github.io/assets/images/typora-user-images/202201021245035.png" alt="out_img_1_1" style="zoom:33%;" /> | ![image-20220101212946984](https://raw.githubusercontent.com/Te4P0t/te4p0t.github.io/main/assets/images/typora-user-images/image-20220101212946984.png) | <img src="https://raw.githubusercontent.com/Te4P0t/te4p0t.github.io/main/assets/images/typora-user-images/img_1_1_mask.png" alt="img_1_1_mask" style="zoom:33%;" /> |
| <img src="https://te4p0t.github.io/assets/images/typora-user-images/out_img_3_1.png" alt="out_img_3_1" style="zoom:33%;" /> | <img src="https://te4p0t.github.io/assets/images/typora-user-images/202201021246024.png" alt="out_img_3_1" style="zoom:33%;" /> | ![image-20220101212613147](https://raw.githubusercontent.com/Te4P0t/te4p0t.github.io/main/assets/images/typora-user-images/image-20220101212613147.png) | <img src="https://raw.githubusercontent.com/Te4P0t/te4p0t.github.io/main/assets/images/typora-user-images/img_3_1_mask.png" alt="img_3_1_mask" style="zoom:33%;" /> |

#### case3:大范围图像修复

|        | 原图                                                         | mask                                                         | with mask                                                    |
| ------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| test_1 | ![img](https://te4p0t.github.io/assets/images/typora-user-images/202201021236551.png) | ![label](https://te4p0t.github.io/assets/images/typora-user-images/label.png) | ![label_viz](https://te4p0t.github.io/assets/images/typora-user-images/202201021237486.png) |

| TELEA                                                        | NS                                                           | LaMa                                                         | Plura                                                        | ICT_1                                                        | ICT_2                                                        |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| <img src="https://te4p0t.github.io/assets/images/typora-user-images/out_img_nature.png" alt="out_img_nature" style="zoom:25%;" /> | <img src="https://te4p0t.github.io/assets/images/typora-user-images/202201021246590.png" alt="out_img_nature" style="zoom:25%;" /> | <img src="https://te4p0t.github.io/assets/images/typora-user-images/img_mask.png" alt="img_mask" style="zoom: 25%;" /> | ![image-20220101220224251](https://te4p0t.github.io/assets/images/typora-user-images/image-20220101220224251.png) | ![img_nature_3](https://te4p0t.github.io/assets/images/typora-user-images/img_nature_3.png) | ![img_nature_4](https://te4p0t.github.io/assets/images/typora-user-images/img_nature_4.png) |






## 分析

#### 传统方法的缺点

​	传统的image inpainting针对的是照片中小范围的缺失或损坏。各种传统的方法在这样的情况下都能取得不错的结果。但近年来，image inpainting的任务逐渐扩大到大范围的图像填补。在大范围的图像填补任务中，传统的方法无法取得良好的结果。

#### CNN的问题

​	CNN的出现使得大范围的图像填补任务有了可能。但是由于CNN自身的缺陷（在一次卷积操作中，一个像素点的取值仅仅受他附近像素点的影响），所以CNN很难获取到一张图片的全局信息，更重视局部信息。（这可以通过简单的实验来证明，如果将MNIST数据集中每张图片的像素点随机打乱，重新训练，全连接网络的准确率几乎不受影响，而CNN准确率会大幅下降。）

​	而CNN的这个缺陷几乎无法改善的。因为想要让每个像素点都获得图片全局的信息，就需要使用全连接网络，而全连接的神经网络在深度增加时，参数会爆炸式的增长，所需要的计算成本太高，为了减少参数量才提出了CNN。换而言之，CNN的出发点决定了其必然会有这样的问题。

## 我们的方法

### 对image inpainting的Re-thinking

​	而在大范围的image inpainting任务中，对图片的全局感知是至关重要的。归根到底，就是CNN网络感受野的问题。

​	尽管cnn通过卷积层的叠加，理论上也可以得到很大的感受野。但实际感受野要小于理论感受野，详情可见**Understanding the Effective Receptive Field in Deep Convolutional Neural Networks**这篇文章。

![image-20211230103422326](https://te4p0t.github.io/assets/images/typora-user-images/image-20211230103422326.png)

文章中指出并不是感受野内所有像素对输出向量的贡献相同，实际感受野是一个高斯分布，有效感受野仅占理论感受野的一部分。

对于大尺度的image inpainting来说，感受野越大，说明模型所能得到的上下文信息越丰富。而CNN-based的网络在这方面做的不够好。

在上述对比实验的过程中，针对大尺度image inpainting任务表现较好的两个项目，LaMa和ICT，实际上都是在尽量解决CNN感受野不足的问题。前者采用了**快速傅里叶卷积**，以能够**在前几层就使模型得到足够有效的感受野**。而后者在上下文信息的处理上直接用效果更好的**Transformer替代了卷积**。

### 尝试

​	我们思考注意力模块（attention module）在网络模型中的作用是什么呢？

​	事实上，在CNN网络中添加的各种注意力机制，本质上是用来**弥补CNN局部性过强，全局性不足**的问题，从而获得全局的上下文信息。这与image inpainting任务的一个关键点不谋而合。（Vision Transformer的出现与注意力也有一定关联，比如Non Local Block模块就与ViT中的self-attention很相似）

​	那么我们能不能在LaMa网络结构的基础上，尝试**添加一些注意力模块**，来使得LaMa模型能够得到**更大的感受野**，从而增强上下文信息获取的能力，提高在大尺度image inpainting任务上的能力呢？

​	**因为LaMa中的网络结构的是类ResNet的结构，考虑在每个FFCResNetblock中加入CBAM结构。且因为LaMa中的网络有两个平行分支（local branch和global branch），所以在要在原版CBAM的基础上做一些改动，对local和global分别做通道和空间注意力。**

修改后的FFC_CBAM

```python
class FFCChannelAttention(nn.Module):
    def __init__(self, channels, ratio_g, ratio=4):
        super(FFCChannelAttention, self).__init__()
        in_cg = int(channels * ratio_g)
        in_cl = channels - in_cg

        self.avg_pool = nn.AdaptiveAvgPool2d(1)
        self.max_pool = nn.AdaptiveMaxPool2d(1)

        self.conv1 = nn.Conv2d(channels, channels // ratio, 1, bias=False)
        self.relu1 = nn.ReLU()
        self.conv_a2l = None if in_cl==0 else nn.Conv2d(channels // ratio, in_cl, kernel_size=1, bias=True)
        self.conv_a2g = None if in_cg==0 else nn.Conv2d(channels // ratio, in_cg, kernel_size=1, bias=True)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = x if type(x) is tuple else (x, 0)
        id_l, id_g = x

        x = id_l if type(id_g) is int else torch.cat([id_l, id_g], dim=1)
        avgx = self.avg_pool(x)
        avgx = self.relu1(self.conv1(avgx))
        avgx_l = 0 if self.conv_a2l is None else self.sigmoid(self.conv_a2l(avgx))
        avgx_g = 0 if self.conv_a2g is None else self.sigmoid(self.conv_a2g(avgx))

        maxx = self.max_pool(x)
        maxx = self.relu1(self.conv1(maxx))
        maxx_l = 0 if self.conv_a2l is None else self.sigmoid(self.conv_a2l(maxx))
        maxx_g = 0 if self.conv_a2g is None else self.sigmoid(self.conv_a2g(maxx))
        x_l = id_l * self.sigmoid(avgx_l + maxx_l)
        x_g = id_g * self.sigmoid(avgx_g + maxx_g)
        return x_l, x_g

class FFCSpatialAttention(nn.Module):
    def __init__(self, kernel_size=7):
        super(FFCSpatialAttention, self).__init__()
        assert kernel_size in (3, 7)
        padding = 3 if kernel_size == 7 else 1

        self.conv = nn.Conv2d(2, 1, kernel_size, padding=padding, bias=False)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = x if type(x) is tuple else (x, 0)
        id_l, id_g = x
        if id_l is None:
            x_l = 0
        else:
            avg_l = torch.mean(id_l, dim=1, keepdim=True)
            max_l, _ = torch.max(id_l, dim=1, keepdim=True)
            x_l = torch.cat([avg_l, max_l], dim=1)
            x_l = self.sigmoid(self.conv(x_l))

        if id_g is None:
            x_g = 0
        else:
            avg_g = torch.mean(id_g, dim=1, keepdim=True)
            max_g, _ = torch.max(id_g, dim=1, keepdim=True)
            x_g = torch.cat([avg_g, max_g], dim=1)
            x_g = self.sigmoid(self.conv(x_g))

        x_l = id_l*x_l
        x_g = id_g*x_g
        return x_l, x_g
```

![image-20211230212318770](https://te4p0t.github.io/assets/images/typora-user-images/image-20211230212318770.png)

在FFCResNetblock中加入我们修改后的CBAM。

​	因为时间和计算资源的缺乏，我们无法使用Places365这个较大的数据集做训练（105G），因此只能被迫选取了相对较小的人脸数据集**CelebA-HQ**，尽管如此，训练一个epoch仍需要**8个小时**左右（我们使用的显卡是GTX_1060）。

​	我们训练设置了6个epoch，同时batch-size减小为6。

以下是我们训练的模型得到的效果：

![image-20211231142018358](https://te4p0t.github.io/assets/images/typora-user-images/image-20211231142018358.png)

![image-20211231142102228](https://te4p0t.github.io/assets/images/typora-user-images/image-20211231142102228.png)

![image-20211231142221279](https://te4p0t.github.io/assets/images/typora-user-images/image-20211231142221279.png)

以上是我们训练的模型在第6个epoch结束后，在test数据集（未训练）上做的结果，左图是原图（ground truth），图中连通域是mask区域，右图是最终修复的结果。

可以看出模型在人脸修复上能够达到不错的效果，尽管放大后细节部位仍能看出和未遮挡区域不协调的部分（尤其是在一只眼睛遮挡，另一只未遮挡的情况下，模型无法恢复出较对称的图形，因此看上去不协调）。

但是毕竟我们训练的epoch较少（参照LaMa训练了40个epoch，batch-size为10，而我们仅仅训练了6个epoch，batch-size为6），如果有足够的时间和计算资源，应该能达到更好的效果。

## 总结和讨论

​	在本次项目中，我们基本完成了选题报告中所设定的任务和目标。从横向纵向两个维度对比了image inpainting这个任务上的不同方法的效果，了解了该领域方法的演进以及该领域当前的发展现状。

​	我们认识到了上下文信息对于大尺度image inpainting任务的重要性，在理解了LaMa和ICT网络结构和具体原理后，尝试通过在LaMa现有的结构中增加我们修改后的CBAM模块，以提高感受野，使模型能够更好的获得上下文信息。

​	可惜的是，由于时间和计算资源的限制，我们只能在CelebA-HQ这种小型数据集上跑少量的epoch进行训练和测试，效果也没有达到预期。如果今后还有机会，可以在此基础上添加其他注意力模块或继续尝试和改进新的模型结构。

## 个人贡献声明

综述与文献阅读：谢雨成、夏鸿、刘源

复现和改进LaMa：夏鸿、谢雨成

尝试复现其他方法：刘源、谢雨成

在现有数据集上测试并比较：夏鸿、刘源

总贡献占比：谢雨成：$$\displaystyle \frac{1}{3}$$​   夏鸿：$$\displaystyle \frac{1}{3}$$  刘源：$$\displaystyle \frac{1}{3}$$

## 引用参考

papers:

[Image inpainting: A review](https://arxiv.org/ftp/arxiv/papers/1909/1909.06399.pdf)

[CBAM: Convolutional Block Attention Module](https://link.zhihu.com/?target=http%3A//openaccess.thecvf.com/content_ECCV_2018/papers/Sanghyun_Woo_Convolutional_Block_Attention_ECCV_2018_paper.pdf)

[[2109.07161\] Resolution-robust Large Mask Inpainting with Fourier Convolutions (arxiv.org)](https://arxiv.org/abs/2109.07161)

[High-Fidelity Pluralistic Image Completion with Transformers (arxiv.org)](https://arxiv.org/pdf/2103.14031.pdf)

[[1903.04227\] Pluralistic Image Completion (arxiv.org)](https://arxiv.org/abs/1903.04227)

[[1604.07379\] Context Encoders: Feature Learning by Inpainting (arxiv.org)](https://arxiv.org/abs/1604.07379)

[[IEEE Xplore Full-Text PDF] Navier-Stokes, Fluid Dynamics, and Image and Video Inpainting](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=990497&tag=1)

[An Image Inpainting Technique Based on the Fast Marching Method](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.98.5505&rep=rep1&type=pdf)

codes:

[BoyuanJiang/context_encoder_pytorch: PyTorch Implement of Context Encoders: Feature Learning by Inpainting (github.com)](https://github.com/BoyuanJiang/context_encoder_pytorch)

[lyndonzheng/Pluralistic-Inpainting: CVPR 2019: "Pluralistic Image Completion" (github.com)](https://github.com/lyndonzheng/Pluralistic-Inpainting)

[raywzy/ICT: High-Fidelity Pluralistic Image Completion with Transformers (ICCV 2021) (github.com)](https://github.com/raywzy/ICT)

[saic-mdal/lama: 🦙 LaMa Image Inpainting, Resolution-robust Large Mask Inpainting with Fourier Convolutions, WACV 2022 (github.com)](https://github.com/saic-mdal/lama)

other:

[geekyutao/Image-Inpainting: A paper summary of image inpainting (github.com)](https://github.com/geekyutao/Image-Inpainting)

[Image Inpainting | Papers With Code](https://paperswithcode.com/task/image-inpainting)

[【Paper】Image Inpainting 必读papers- 梁君牧 - 博客园](https://www.cnblogs.com/lwp-nicol/p/15016914.html#generative-image-inpainting-with-contextual-attention-1)

[目标检测和感受野的总结和想法 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/108493730?utm_source=qq&utm_medium=social&utm_oi=941444345661009920)

[卷积神经网络的感受野 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/44106492)

