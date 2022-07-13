from typing import List

from PIL import Image


def concat_imgs(imgs: List[Image.Image]) -> Image.Image:
    assert len(imgs) > 0
    out_img = Image.new("RGB", (imgs[0].width, sum(i.height for i in imgs)))
    y_start = 0
    for img in imgs:
        assert img.width == imgs[0].width, f"the img width: {img.width}, first img width: {imgs[0].width}"
        out_img.paste(img, (0, y_start))
        y_start += img.height
    return out_img


def concat_imgs_with_centered(imgs: List[Image.Image], center_img: Image.Image) -> Image.Image:
    assert center_img.width == center_img.height, "中心图片长宽必须相等"
    assert len(imgs) % 2 == 0, "需要偶数个待合并图片"
    inserted_pos = len(imgs) >> 1
    imgs_ = []
    for img in [*imgs[:inserted_pos], center_img, *imgs[inserted_pos:]]:
        if img.width != center_img.width:
            img = img.resize((center_img.width, int(img.height * center_img.width / img.width)))
        imgs_.append(img)
    return concat_imgs(imgs_)
