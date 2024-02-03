import cv2
import argparse
import numpy as np
from PIL import Image


def get_args():
    parser = argparse.ArgumentParser(description='命令行中传入一个数字')

    parser.add_argument(
        '-s', '--size', type=str, help='分辨率, 比如281x375, wxh格式', default="281x375")
    parser.add_argument('--width', type=int, help='Target 图片的宽')
    parser.add_argument('--height', type=int, help='Target 图片的高')
    parser.add_argument('--img-path', type=str, nargs='+', required=True,
                        help='传入的图片路径')
    args = parser.parse_args()
    return args


def analyze_args(args):
    w, h = [int(x) for x in args.size.split("x")]
    if hasattr(args, "width") and args.width:
        w = args.width
    if hasattr(args, "height") and args.height:
        h = args.height

    return {
        "img_path": args.img_path if args.img_path else [],
        "shape": (w, h),
    }


def cv2_read_resize_write(img_path, args):
    # 只传入图片路径
    im = cv2.imread(img_path)
    im_resized = cv2.resize(im, args["shape"])
    cv2.imwrite(img_path, im_resized)

def pil_read_resize_write(img_path, args):

    im = Image.open(img_path)
    im_resized = im.resize(args["shape"], resample=Image.BILINEAR)
    # im_resized.show()
    im_resized.save(img_path)


if __name__ == "__main__":
    args = get_args()
    args = analyze_args(args)
    
    for img_path in args["img_path"]:

        # cv2_read_resize_write(img_path, args)
        pil_read_resize_write(img_path, args)