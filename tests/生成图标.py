#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PIL import Image

image_size = [512, 256, 144, 140, 128, 120, 108, 100, 88, 72, 48, 32, 28]


def create_icon():
    for size in image_size:
        pri_image = Image.open("window_icon.png")
        pri_image.resize((size, size), Image.ANTIALIAS).save("icom_%d.ico" % (size))


if __name__ == "__main__":
    create_icon()
