import math
import os

from config import DEFAULT_TARGET_WIDTH, DEFAULT_OUTPUT_FORMAT, AVAILABLE_OUTPUT_FORMATS
from core import ConcentrateImgsWithCover

if __name__ == '__main__':
    import argparse

    description = """example:
    # v0.1.0
        # 拼 1^2图
        python main.py "/Users/mark/Pictures/微信精选/宫崎骏-1991-岁月的童话" -c cover.jpg 明天会更好
        # 拼 2^2 图
        python main.py "/Users/mark/Pictures/微信精选/宫崎骏-1991-岁月的童话" -c cover.jpg 你喜欢哪一种 模仿吐痰 我不会跟你握手的 明天会更好
        # 拼 3^2 图
        python main.py "/Users/mark/Pictures/微信精选/宫崎骏-1991-岁月的童话" -c cover.jpg 你喜欢哪一种 模仿吐痰 我不会跟你握手的 回忆 菊花 彩虹 我们不会垂头丧气的 与自己对话 明天会更好
    
    # v0.2.0
        # 自动选取cover，因为只有一个；自动选择待拼接文件夹，因为前缀都是必选，而且有四个
        python main.py "/Users/mark/Pictures/微信精选/宫崎骏-2004-霍尔的移动城堡"  
    """

    note = """attention:
    1. 实测下来，png和jpg的显示效果差距不大，但png文件会比jpg大上好几倍
    2. 比起文件格式以及文件尺寸等因素，影响微信朋友圈最终渲染效果的决定性因素是用手机上传亦或电脑，确保质量一定要用手机上传！(可以用airdrop)
    """

    parser = argparse.ArgumentParser(description=description, epilog=note,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument("source_dir", type=str)
    parser.add_argument("queue", type=str, nargs="*", help=r"如果不指定，则会自动选取文件夹内pattern为'必选-\d+-.*'的文件夹")
    parser.add_argument("-c", "--cover_name", type=str, help="如果不指定，则会遍历找到唯一的带cover前缀的图")
    parser.add_argument("-f", "--output_format", default=DEFAULT_OUTPUT_FORMAT, choices=AVAILABLE_OUTPUT_FORMATS)
    parser.add_argument("-w", "--target_width", default=DEFAULT_TARGET_WIDTH)

    args = parser.parse_args()

    # 解析文件夹地址
    source_dir = args.source_dir
    assert os.path.exists(source_dir), f"source dir: [{source_dir}] not exists!"

    # 解析封面
    if args.cover_name:
        cover_path = os.path.join(source_dir, args.cover_name)
        assert os.path.exists(cover_path), f"cover path: [{cover_path}] not exists!"
    else:
        potential_covers = [i for i in os.listdir(source_dir) if i.startswith("cover")]
        assert len(potential_covers) != 0, f"no cover found in source dir: [{source_dir}]"
        assert len(potential_covers) == 1, f"more than one cover to be found: [{potential_covers}]"
        cover_path = os.path.join(source_dir, potential_covers[0])

    # 解析素材
    assert len(args.queue) in [0, 1, 4, 9], str(args.queue)
    if args.queue:
        queue = args.queue
    else:
        queue = sorted([i for i in os.listdir(source_dir) if i.startswith("必选")])

    # 拼接
    runner = ConcentrateImgsWithCover(source_dir, grid_cnt=int(math.sqrt(len(queue))), cover_path=cover_path,
                                      output_format=args.output_format)
    for index, item in enumerate(queue):
        runner.concat_imgs_from_dir(item, index)
