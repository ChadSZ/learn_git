#!/user/bin/env python
# _*_ coding:utf-8 _*_
    # Filename: gif2ascii.py
# Time: 2018-12-07 14:47:36
# Created by 2048K, kairan2048@163.com

import os, sys
import imageio
import argparse
from PIL import Image, ImageDraw, ImageFont

def gif2png(fileName, asciiChar, font, isgray, scale):
    ''' 将GIF拆分，并将每一帧处理成字符画
    fileName: GIF文件
    asciiChar: 灰度值对应的字符串
    font: ImageFont对象
    isgray: 是否生成黑白动图
    scale: 缩放比例
    '''
    im = Image.open(fileName)      # GIF文件打开为一个序列
    path = os.getcwd()
    # Cache文件用以保存拆分后的图片和生成的字符画
    if(not os.path.exists(path+"/Cache")):
        os.mkdir(path+"/Cache")
    os.chdir(path+"/Cache")
    # 清空Cache文件夹下的内容，防止多次运行时被之前的文件影响
    for f in os.listdir(path+"/Cache"):
        os.remove(f)
    # GIF打开后的序列通过tell返回每一帧的索引，超出索引范围后抛出异常
    try:
        while 1:
            current = im.tell()
            name = fileName.split('.')[0]+'-'+str(current)+'.png'
            im.save(name)   # 保存每一帧图片   
            # 将每一帧处理为字符画
            img2ascii(name, asciiChar, font, isgray, scale)
            im.seek(current+1)  # 继续处理下一帧
    except:
        os.chdir(path)


# 将不同的灰度值映射为ASCII字符
def get_char(asciiChar, r, g, b):
    # if alpha == 0:
    #     return ''
    length = len(asciiChar)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    return asciiChar[int(gray/(256/length))]


# 将图片处理成字符画
def img2ascii(img, asciiChar, font, isgray, scale):
    scale = scale
    im = Image.open(img).convert('RGB')  # 注意，此处需要先将图片转换为RGB模式
    # 设定处理后的字符画大小，需要为整型
    raw_width = int(im.width * scale)
    raw_height = int(im.height * scale)
    # 获取设定的字体的尺寸，ImageFont默认的尺寸大小为6x11，其他字体会有所不同
    # 此处使用的字体为truetype字体，大小为10px
    font_x, font_y = font.getsize(' ')
    # 确定单元的大小
    block_x = int(font_x * scale)
    block_y = int(font_y * scale)
    # 确定长宽各有几个单元
    w = int(raw_width/block_x)
    h = int(raw_height/block_y)
    # 将每个单元缩小为一个像素
    im = im.resize((w, h), Image.NEAREST)
    # txts和colors分别存储对应块的ASCII字符和RGB值
    txts = []
    colors = []
    for i in range(h):
        line = ''
        lineColor = []
        for j in range(w):
            pixel = im.getpixel((j, i))
            lineColor.append((pixel[0], pixel[1], pixel[2]))
            # if len(pixel) == 3:
            line += get_char(asciiChar, pixel[0], pixel[1], pixel[2])
            # if len(pixel) == 4:
            #     line += get_char(asciiChar, pixel[0], pixel[1], pixel[2], pixel[3])
        txts.append(line)
        colors.append(lineColor)
    # 创建新画布
    im_txt = Image.new("RGB", (raw_width, raw_height), (255, 255, 255))
    # 创建ImageDraw对象以写入ASCII
    draw_handle = ImageDraw.Draw(im_txt)
    for j in range(len(txts)):
        for i in range(len(txts[0])):
            if isgray:
                draw_handle.text((i*block_x, j*block_y), txts[j][i], (50, 50, 50))
            else:
                draw_handle.text((i*block_x, j*block_y), txts[j][i], colors[j][i])
    im_txt.save(img)

# 读取Cache文件夹下的文件，合成GIF动画
def png2gif(dir_name, duration):
    path = os.getcwd()
    os.chdir(dir_name)
    dirs = os.listdir()
    images = []
    num = 0
    for d in dirs:
        images.append(imageio.imread(d))
        num += 1
    os.chdir(path)
    imageio.mimsave(d.split('-')[0]+'-ascii.gif',images,duration = duration)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--file', dest='fileName', required=True,
        help="the name of GIF file to concert"
    )
    parser.add_argument(
        '--duration', dest='duration', required=False,
        help="duration of every frame"
    )
    parser.add_argument(
        '--fontsize', dest='fontSize', required=False,
        help="font size of character"
    )
    parser.add_argument(
        '--isgray', dest='isgray', required=False,
        help="the color of character. if TRUE, will be similar to orign image"
    )
    parser.add_argument(
        '--scale', dest='scale', required=False,
        help="zoom the image"
    )
    args = parser.parse_args()
    fileName = args.fileName
    duration = 0.2
    fontSize = 10
    isgray = False
    scale = 1.0
    if args.duration:
        duration = float(args.duration)
    if args.fontSize:
        fontSize = int(args.fontSize)
    if str(args.isgray).upper() == 'TRUE':
        isgray = True
    if args.scale:
        scale = float(args.scale)
    asciiChar = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
    font = ImageFont.truetype('hei.ttf', size=int(fontSize))
    gif2png(fileName, asciiChar, font, isgray, scale)
    png2gif('./Cache', duration)