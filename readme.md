# 微信朋友圈封面墙脚本

## background

朋友圈有时候会出现一些一张大图被切分成多张小图，然后每张小图点开后其实又是一张长图的效果。

尽管它们多见于营销相关的朋友，但确实是一个很有意思的小技巧，也很赏心悦目。

那它是怎么做到的呢？

其实就是首先把一张大图（我们称之为cover）拆成1、4或者9个正方形小格子，然后每个小格子在其上下方都加入等高的其他图片内容即可。

由于微信会自动居中显示，所以这样正好就能实现这样的效果，例如：

![朋友圈图片拼接效果展示](https://mark-vue-oss.oss-cn-hangzhou.aliyuncs.com/images/20220714/95c4ee4b77614c08becd750bb533e0aa.png?x-oss-process=image/auto-orient,1/interlace,1/quality,q_100/format,jpg)

而其实，每张小图是长这样的：

![小图详情](https://mark-vue-oss.oss-cn-hangzhou.aliyuncs.com/images/20220714/f4d396c0cb4840dea19e1d4060fd3147.png?x-oss-process=image/auto-orient,1/interlace,1/quality,q_100/format,jpg)

这仅需要不多的几行代码就可以搞定，也是本仓库的实现目标。

## practice

其实一开始我是喜欢拼九宫图的，后来发现在个人主页只会显示前四张，导致奇丑，所以目前就全部采用拼四张的做法，以统一效果了~

具体实践的话，脚本其实是最简单的部分，最耗时的部分在于选取素材，以下以我常用的场景看宫崎骏的电影为例：

1. 看电影时不断地截图，看完一部大概有一两百张截图

2. 在mac图库里创建一个本电影对应的专辑，把这些截图都拉进去（使用专辑，方便直接按delete键移除相片，否则需要command+delete，而且会删到垃圾桶里去，在专辑里移除还是会保留library里的原件的）

3. 打开Finder，创建一个本电影对应的文件夹，把专辑里的图片分别拷贝入不同的主题文件夹（每张图片可能有多种不同的可分类目标，所以是一对多关系）

4. 从这些主题中，筛选出四个最想拼图的，分别命名为`必选-序号-主题名`

5. 选定一个cover

6. 然后就可以跑我们的脚本了，拼图结果自动输出在`out`文件夹内

7. 最后使用`airdrop`传到手机，然后上传朋友圈（长图不能在桌面端朋友圈直接上传，否则压缩到怀疑人生）

## script demo

```shell
SOURCE_DIR='./samples/宫崎骏-2001-千与千寻'
python src/main.py $SOURCE_DIR
ls $SOURCE_DIR/out
# out: cover_growth-0-渺小.jpg   cover_growth-1-温暖.jpg   cover_growth-2-草原.jpg   cover_growth-3-花园.jpg
```