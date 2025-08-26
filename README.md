```text
  ___          _____               _        _ _    ___                          
 | _ \  _  _  |_   _|  ___   ___  | |  ___ | | |  | _ \  ___   _ __   _ _   ___ 
 |  _/ | || |   | |   / _ \ / _ \ | | (_-< |_  _| |   / / -_) | '_ \ | '_| / _ \
 |_|    \_, |   |_|   \___/ \___/ |_| /__/   |_|  |_|_\ \___| | .__/ |_|   \___/
        |__/                                                  |_|               
```

---

A collection of Python utilities potentially useful for reproducing research papers

一系列复现论文成果时可能用到的 python 小工具

---

## 🔦 RPS4SH

### 🖐 用途
Extract 9-dimensional SH lighting coefficients from .rps files 

从 .rps 文件中提取 9 维 SH 光照系数

### 📦 需额外安装的依赖

- `numpy`

### 🚀 快速开始

```bash
wget https://raw.githubusercontent.com/MRoldL001/PyTools4Repro/main/tools/RPS4SH.py
```

打开 `RPS4SH.py` ，修改 input_dir 和 output_dir 为实际路径

```bash
python RPS4SH.py
```

---

## ⬇️ downloadObjaverse.py

### 🖐 用途
Stable download of the Objaverse dataset under poor network conditions

在较差的网络环境下稳定下载 Objaverse 数据集

### 📦 需额外安装的依赖

- `objaverse`

### 🚀 快速开始

参见 downloadObjaverse.py 的[主仓库](https://github.com/MRoldL001/downloadObjaverse)

---

## 🌲 flattenner

### 🖐 用途
Moves all files from subfolders to the root directory to flatten the folder structure

把指定目录下所有子目录的文件移到根目录，实现目录扁平化

### 📦 需额外安装的依赖

无

### 🚀 快速开始

```bash
wget https://raw.githubusercontent.com/MRoldL001/PyTools4Repro/main/tools/flattenner.py
python flatten.py <文件夹路径>
```

或者，如果你想顺带移除空的子文件夹

```bash
wget https://raw.githubusercontent.com/MRoldL001/PyTools4Repro/main/tools/flattenner.py
python flatten.py <文件夹路径> -red   # red 指 remove empty dir
```

---

## 🖼️ img2png

### 🖐 用途
A simple Python script that batch converts all JPG and WEBP images in the current directory into PNG format. With just slight modifications, it can be adapted for different needs

一个简单的 python 脚本，用于将当前目录下所有 jpg 及 webp 格式图片批量转成 png 格式，只需简单改动便能适用于不同需求

### 📦 需额外安装的依赖

- `PIL`

### 🚀 快速开始

```bash
wget https://raw.githubusercontent.com/MRoldL001/PyTools4Repro/main/tools/img2png.py
python img2png.py
```
