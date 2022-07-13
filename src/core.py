import os

from PIL import Image

from config import DEFAULT_TARGET_WIDTH, DEFAULT_OUTPUT_DIR_NAME, DEFAULT_OUTPUT_FORMAT
from algo import concat_imgs_with_centered


class ConcentrateImgsWithCover:

    def __init__(
            self,
            source_path,
            grid_cnt: int,
            cover_path: str,
            output_format=DEFAULT_OUTPUT_FORMAT,
            target_width: int = DEFAULT_TARGET_WIDTH
    ):
        self._source_path = source_path
        self._grid_cnt = grid_cnt
        self._cover_path = cover_path
        self._output_format = output_format
        self._target_width = target_width
        print("source dir path: ", self._source_path)
        self._output_dir_path = os.path.join(self._source_path, DEFAULT_OUTPUT_DIR_NAME)
        print("output dir path: ", self._output_dir_path)
        if not os.path.exists(self._output_dir_path):
            os.mkdir(self._output_dir_path)

    def _get_block_of_image(self, img: Image.Image, index: int):
        left = (img.width - img.height) >> 1
        img = img.crop((left, 0, img.width - left, img.height))
        unit = img.width // self._grid_cnt
        row = index // self._grid_cnt
        col = index % self._grid_cnt
        return img.crop((unit * col, unit * row, unit * (col + 1), unit * (row + 1))).resize(
            (self._target_width, self._target_width))

    def concat_imgs_from_dir(self, imgs_dir_name: str, index: int):
        print("imgs_dir_name: ", imgs_dir_name)
        imgs_dir_path = os.path.join(self._source_path, imgs_dir_name)
        imgs = []
        for img_name in sorted([i for i in os.listdir(imgs_dir_path) if i.startswith("screenshot")],
                               key=lambda x: int(x[10:-4])):
            img_path = os.path.join(imgs_dir_path, img_name)
            imgs.append(Image.open(img_path))
        cover_img = Image.open(self._cover_path)
        blocked_img = self._get_block_of_image(cover_img, index)
        merged_imgs = concat_imgs_with_centered(imgs, blocked_img)

        output_path = os.path.join(self._output_dir_path,
                                   f"{self._cover_path.split('.')[0]}-{self._grid_cnt}-{index}-{imgs_dir_name}.{self._output_format}")
        merged_imgs.save(output_path)
        print("outputted file path: ", output_path)
        # merged_imgs.show()
