# Novel_In_Image_With_Background

## 功能介绍

NII是一个在文字和图片之间互相转换的便利工具。可以有效地隐藏文本内容或者在设备之间方便地传输。与彩色二维码作用类似。

Novel_In_Image_With_Background则是在NII的基础上添加了背景，因为红色通道没有发挥作用，可以考虑增加背景。

## 用法

### 文字转图片：

```python
python nii.py -e xxx.txt
```

其中`xxx.txt`是要转换的文本路径。

### 图片转文字

```python
python nii.py -d xxx.bmp
```

其中`xxx.bmp`是要转换的图片路径。

## 使用前

在开始使用之前，请确保您的设备已经安装了Python 3.6或更新版本，和`pillow`库。如果没有安装`pillow`，我们提供了一个方便的方式来安装，只需

```python
python nii.py -i
```

等待安装完成即可。

### ToDo

* 背景不可以自定义，默认使用了一张地球的航拍照，

	可以考虑增加自定义修改背景的功能，

	以后没事干的时候再做吧！
* 文字为空时，会报错

	最好添加人性化提醒！

### Done

* 修复了没有装Pillow会报错的bug

	由于直接在开头引入了PIL库，所以如果没有安装Pillow，怎么操作都是会报错的，导致了安装模块并没有什么用，故把dec和enc的import换到了if语句内