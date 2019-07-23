from PIL import Image,ImageDraw
import os,imageio
CUR_PATH = r'imgs'
isgoingon = 1
def img_src(filename):
    gif_img = Image.open(filename)
    lx = gif_img.tell()
    gif_img.seek(lx)
    i=0

    try:
        while True:
            img_i = deal(gif_img)
            img_i.save("imgs/img"+str(i)+".png")
            gif_img.seek(gif_img.tell()+1)
            i += 1
    except EOFError:
        print("逐帧处理完成！")
        pass

def deal(girf_img):

    pix=[
         "Z", "O", "0", "Q", "L", "C", "J", "U", "Y", "X", "z", "c", "v", "u", "n", "x", "r", "j", "f",
         "t", "/", "\\","|","?"," - ","_"," + ","~"," < "," > ",
         ";",": ",", ","`","'","."," "]

    new_im = girf_img.convert("L")
    newL = Image.new("L",(new_im.width,new_im.height),255)
    draw = ImageDraw.Draw(newL)
    fillColor = "#ff0000"
    for x in range(0,new_im.width,4):
        for y in range(0, new_im.height, 4):
            xy_degree = new_im.getpixel((x,y))
            index = int(xy_degree/(256/len(pix)))
            draw.text((x,y),pix[index],fill=fillColor)
    return newL
def img_created():

    files = os.listdir("imgs")

    for i in range(len(files)):
        im = Image.open("imgs/img"+str(i)+".png")
        (x, y) = im.size  # read image size
        x_s = 800  # define standard width
        y_s = y * x_s / x  # calc height based on standard width
        out = im.resize((int(x_s), int(y_s)), Image.ANTIALIAS)  # resize image with high-quality
        out.save("imgs/img"+str(i)+".png")
    print(len(files))
    frames = []

    for i in range(len(files)):
        frames.append(imageio.imread("imgs/img"+str(i)+".png"))
    imageio.mimsave("final.gif",frames,'GIF',duration = 0.15)
    print("gif已生成")

def del_file(path):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        os.remove(c_path)
def show():
    os.startfile("final.gif")

def action(filename):
    path =os.getcwd()
    if not os.path.exists(path+"\imgs"):
        os.mkdir("imgs")
    if ifgoing() == 0:
        return
    del_file("imgs")
    if ifgoing() == 0:
        return
    img_src(filename)
    if ifgoing() == 0:
        return
    img_created()
    if ifgoing() == 0:
        return
    show()

def ifgoing():
    if isgoingon == 1:
        return 1
    else :
        return 0


