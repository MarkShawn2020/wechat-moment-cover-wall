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

## usage

### demo

```shell
SOURCE_DIR='./samples/宫崎骏-2001-千与千寻'
python src/main.py $SOURCE_DIR
ls $SOURCE_DIR/out
# out: cover_growth-0-渺小.jpg   cover_growth-1-温暖.jpg   cover_growth-2-草原.jpg   cover_growth-3-花园.jpg
```