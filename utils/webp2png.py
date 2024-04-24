import os
import argparse
from PIL import Image


def convert_webp_to_jpg_png(input_file, output_format):
    if not os.path.isfile(input_file):
        print(f"输入文件 {input_file} 不存在")
        return

    if not input_file.lower().endswith(".webp"):
        print(f"输入文件 {input_file} 不是webp格式")
        return

    filename = os.path.splitext(input_file)[0]
    output_file = f"{filename}.{output_format}"

    try:
        with Image.open(input_file) as im:
            im.load()
            if im.mode == "RGBA":
                background = Image.new("RGBA", im.size, (255, 255, 255))
                background.paste(im, mask=im.split()[3])
                im = background.convert("RGB")
            else:
                im = im.convert("RGB")

            if output_format.lower() == "jpg":
                output_format = "JPEG"

            im.save(output_file, output_format)
            print(f"转换完成,输出文件: {output_file}")
    except Exception as e:
        print(f"转换失败: {str(e)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="将webp格式图片转换为jpg或png格式")
    parser.add_argument("input_file", help="输入的webp文件")
    parser.add_argument("-f", "--format", choices=["jpg", "png"], default="jpg",
                        help="输出格式,默认为jpg")
    args = parser.parse_args()

    convert_webp_to_jpg_png(args.input_file, args.format)
