# Pytorch安装（editor：pakchung10/2021.06） #
----------

## GPU版pytorch安装 ##
## 检查是否有合适的GPU，若有则安装Cuda与CuDNN（需检查电脑是否有合适的GPU） ##

### 1.在桌面上右键点击NVIDIA控制面板。 ###

![](https://i0.hdslb.com/bfs/album/4de1f1e54e412f7970377ac12a0542b5fc59fa0f.png)

### 2.进入NVIDIA控制面板后，点击帮助，选择系统信息 ###

![](https://i0.hdslb.com/bfs/album/af0fc0cfa70e2eac52237816aec7aed41dc2c5a1.png)

### 3.查看电脑的显卡信息（本机显卡型号为NVIDIA GeForce GTX 1050 Ti,驱动型号为466.47），同时需要注意显卡驱动的更新 ###

![](https://i0.hdslb.com/bfs/album/348e473a4e78f37490cf3b1acd555a4ed9d0375f.png)

### 4.下载Cuda（官网：[https://developer.nvidia.com/cuda-10.1-download-archive-update2](https://developer.nvidia.com/cuda-10.1-download-archive-update2)） ###
关于Cuda的版本选择，可以进入官方指南查询（[https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html](https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html)），根据计算机的GPU型号以及驱动版本进行选择。

![](https://i0.hdslb.com/bfs/album/8c82070f80d46125183091c752d54d92ea4453d4.png)

根据本机的466.47驱动版本，则选择CUDA 11.3.1，进入官网选择“Legacy Releases”查看CUDA的历史版本进行选择

![](https://i0.hdslb.com/bfs/album/398e5138785780ff4c7c7824c4472415a5023fb4.png)

选择CUDA Toolkit 11.3.1版本

![](https://i0.hdslb.com/bfs/album/e7b9c61ef24abc8a98d3e4a20715564118bafeb2.png)

根据计算机的实际参数选择本地安装（local）

![](https://i0.hdslb.com/bfs/album/83aaf938da0ace6b50fa03b446146d0248eb4af3.png)

点击Download

![](https://i0.hdslb.com/bfs/album/bb898b99bd87f4d1ced165c54b7bc4ee6791af4c.png)

### 5.开始Cuda正式安装步骤 ###
----------

打开驱动文件.exe

![](https://i0.hdslb.com/bfs/album/a187cf5978f02b24ed98d0f32ee999f174202298.png)

选择默认安装路径

![](https://i0.hdslb.com/bfs/album/142c5a9aa150d877dbc0d6c0ddee6ed1cdbf23b2.png)

![](https://i0.hdslb.com/bfs/album/90b813fe86b9bb74d9105b06fb2c7f3308a9cf06.png)

程序自检

![](https://i0.hdslb.com/bfs/album/303f38c4f7ac227380a20539b8ca678ce10d140d.png)

点击“同意并继续”

![](https://i0.hdslb.com/bfs/album/e27ef6349dbc1e985a3af1aa4e13103c103ef3ba.png)

点击“下一步”

![](https://i0.hdslb.com/bfs/album/9e4f0d59d685d351e68b3ad66a77d4469ff89b77.png)

点击“下一步”

![](https://i0.hdslb.com/bfs/album/11589407c69a2d0b77549cfcd8a793fe8ef34d79.png)

点击“下一步”（安装路径按默认，安装程序将自动配置）

![](https://i0.hdslb.com/bfs/album/555ceca98bdfee5741d7009768dd9ced093acbcc.png)

勾选“同意”，点击“next”

![](https://i0.hdslb.com/bfs/album/4b8ce01b7fb4d8065998fa5e82d60b805d51672d.png)

自动安装

![](https://i0.hdslb.com/bfs/album/a6f8cfaea5ae836659f6e3c1d352b5fff0c1d708.png)

选择下一步

![](https://i0.hdslb.com/bfs/album/d8b33819b59f7ae3022a1d3dd9f23484d3537fa6.png)

直接点击关闭

![](https://i0.hdslb.com/bfs/album/1fb68f283f1c6018dee926eab46ad892813cfdaf.png)

至此CUDA安装完成

### 6.验证Cuda安装是否成功（Cuda的系统变量会自动配置完成） ###

右键点击“我的电脑”后点击“属性”

![](https://i0.hdslb.com/bfs/album/769846eef2bb334ffa8a6912db7e70d68d54c8e2.png)

点击“高级系统设置”

![](https://i0.hdslb.com/bfs/album/084b2c086f284b10e12c1007b94a05bbe9fb5d22.png)

查看系统变量（Cuda系统变量已自动配置）

![](https://i0.hdslb.com/bfs/album/71501a6e41fb1c61a5f2e4e75f4c5f2d68128d56.png)

win+R键输入 `cmd` 打开cmd命令行界面输入 `nvcc -V` ，显示Cuda版本信息则表示安装成功
![](https://i0.hdslb.com/bfs/album/9244e2ec92fa082025552eba2cd6275cc4d8ac92.png)

### 7.下载CuDNN（官网：[https://developer.nvidia.com/rdp/cudnn-download](https://developer.nvidia.com/rdp/cudnn-download)） ###

初次登陆该网站需要注册账号

![](https://i0.hdslb.com/bfs/album/2c4e97b9596b1cb404c9b2eb90fd11059017148a.png)

根据计算机的参数选择合适的CuDNN版本

![](https://i0.hdslb.com/bfs/album/57fde7fc464a0b36527d844972e59194ac83f878.png)

### 8.安装CuDNN ###

解压下载得CuDNN文件

![](https://i0.hdslb.com/bfs/album/ff60a22f11dd0b536709ffaff156ce477565c41f.png)

分别将解压活得的文件夹下cuda/include、cuda/lib、cuda/bin三个目录中的内容拷贝到C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.1对应的include、lib、bin目录下即可。

![](https://i0.hdslb.com/bfs/album/beaf39a1e4ec20c4ef8d5524b3dc4ca716ff1892.png)

配置环境变量（添加环境变量 `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.3\lib\x64`）

右键点击“此电脑”，点击“属性”，点击“高级系统设置”，点击“环境变量”，点击“系统变量”，点击“path”，点击“编辑”，点击“新建”加入该路径即可。

![](https://i0.hdslb.com/bfs/album/7055355da61285509e4ff730df4abacd851e4017.png)

### 9.安装Pytorch（官网：[https://pytorch.org/](https://pytorch.org/)） ###

进入Pytorch官网

![](https://i0.hdslb.com/bfs/album/b1f465e31476671f668212da7f219b9de72ac4a0.png)

按照计算机参数选择合适的版本进行自动下载安装

（获取命令：`conda install pytorch torchvision torchaudio cudatoolkit=11.1 -c pytorch -c conda-forge`）

![](https://i0.hdslb.com/bfs/album/28a84d2fd223bcbc5114b6776372ce2c967ed696.png)

使用Conda安装（Anaconda管理环境以及第三方包比较方便）

打开Anaconda powershell prompt界面（Anaconda使用教程参考[https://blog.csdn.net/u014628771/article/details/8006662](https://blog.csdn.net/u014628771/article/details/8006662)4）

![](https://i0.hdslb.com/bfs/album/050c95b8c51582dcc6c745e61b4c023c55099e4f.png)

创建新环境进行安装Pytorch（也可在原有的环境底下进行安装，ps：若原环境曾安装过pytorch可能导致安装失败）

    conda create --name pytorch_for_teach python=3.7

![](https://i0.hdslb.com/bfs/album/830e22b8710aa776c9fa334625453b69bc99a5ce.png)

输入“y”后稍等片刻，出现以下画面则说明环境创建成功

![](https://i0.hdslb.com/bfs/album/d6ed8c47c00b6f122714c66ab3b413acdbac823d.png)

![](https://i0.hdslb.com/bfs/album/b99cd512ca34bd4f43fd34cd011a7dee60d31163.png)

启动该新创建的Python环境（旧有安装包删除 `conda clean --all`）

    conda activate pytorch_for_teach

![](https://i0.hdslb.com/bfs/album/e0e729923ce5964d499d39459d96ec7c2e0a181f.png)

为加快pytorch下载速度，将下载源设置为清华源

创建.condarc文件修改默认下载源

    conda config --set show_channel_urls yes

![](https://i0.hdslb.com/bfs/album/ff352a54d411f3378210ef5f36e69a23b19a39c8.png)

![](https://i0.hdslb.com/bfs/album/32786c24a8af35b84055b33805d93d1c975bccb7.png)

记事本方式打开.condarc文件，拷贝以下内容覆盖后保存

    channels:
      - defaults
    show_channel_urls: true
    default_channels:
      - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
      - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
      - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
    custom_channels:
      conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
      msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
      bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
      menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
      pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
      simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud

![](https://i0.hdslb.com/bfs/album/8dd4d6fa052b42e77d9d069be69324bea582db7c.png)

运行 `conda clean -i` 清除索引缓存，保证用的是镜像站提供的索引

![](https://i0.hdslb.com/bfs/album/4ada95812ea10efad3d4b0c2b55df43143f58640.png)

运行 `conda create -n pytorch_for_teach numpy` / `conda install numpy` 测试


将上面获得的Conda安装Pytorch命令拷贝到Conda界面进行输入运行

    conda install pytorch torchvision torchaudio cudatoolkit=11.1 -c pytorch -c conda-forge

![](https://i0.hdslb.com/bfs/album/63fcb431b013216f7198f259ecf29c550748e1d5.png)

输入“y”

![](https://i0.hdslb.com/bfs/album/5e829c5102ade85513ca619455a4955becd2ae0b.png)

安装完成

![](https://i0.hdslb.com/bfs/album/2a1ebffc502b862dcfa152a3f1732ee1914aaf5e.png)

### 10.测试pytorch安装完成与否 ###

在conda界面直接测试pytorch

    python
    
    import torch
    
    print(torch.cuda.is_available())

![](https://i0.hdslb.com/bfs/album/5cfc5bf5ce7c28ae475f706ce62d410643f3ccc7.png)

至此，GPU版pytorch安装完成

## 附CPU版pytorch安装 ##

进入Pytorch官网（[https://pytorch.org/get-started/locally/](https://pytorch.org/get-started/locally/)）

![](https://i0.hdslb.com/bfs/album/b3377b068c2abe7da417fb07e02062df4aebfe3d.png)

获取CPU版下载命令

    conda install pytorch torchvision torchaudio cpuonly -c pytorch

![](https://i0.hdslb.com/bfs/album/78d91afbd6e50dfb118c8f0b9491e3d1621a8930.png)

输入“y”

![](https://i0.hdslb.com/bfs/album/b4bdfd76be9432f35213eb9ac307cb117291d6bf.png)

测试是否安装成功

    python
    
    import torch
    
    print(torch.__version__)

![](https://i0.hdslb.com/bfs/album/8a35c9db21d4059f06bd8653494937a2a17203ad.png)



