import tkinter
from tkinter import filedialog
from PIL import Image, ImageTk, ImageEnhance
from torchvision import transforms
import os
#保存图片
def save():
    global count
    count += 1
    global save_image
    save_image.save(os.path.join(saveroute, 'test' + str(count) + '.jpg'))
#选择图片
def select():
    selected = tkinter.filedialog.askopenfilename(title='请选择图片')
    load = Image.open(selected)
    load = transforms.Resize((150,200))(load)
    global original
    original = load
    render = ImageTk.PhotoImage(load)
    img  = tkinter.Label(root,image=render)
    img.image = render
    img.place(x=100,y=150)
#在根窗口root中显示图片
def resultshow():
    global render,img2
    img2.destroy()
    img2  = tkinter.Label(root,image=render)
    img2.image = render
    img2.place(x=500,y=150)
#调节亮度
def bright():
    enh_bri = ImageEnhance.Brightness(original)
    brightness = float(input("请输入亮度（1为原亮度）:"))
    image_brightened = enh_bri.enhance(brightness)
   
    global save_image
    save_image = image_brightened
    global render
    render = ImageTk.PhotoImage(image_brightened)
    resultshow()
    
#调节对比度
def contrast():
    enh_con = ImageEnhance.Contrast(original)
    contrast = float(input("请输入对比度（1为原对比度）:"))
    image_contrasted = enh_con.enhance(contrast)
    image_contrasted.show()
    global save_image
    save_image = image_contrasted
    global render
    render = ImageTk.PhotoImage(image_contrasted)
    resultshow()
#旋转
def rotation():
    # 输入旋转角度
    angle = int(input("请输入旋转角度:"))
    modi_img = original.rotate(angle)
    modi_img.show()
    global save_image
    save_image = modi_img
    global render
    render = ImageTk.PhotoImage(modi_img)
    resultshow()
#裁剪
def cut():
    print('图片的大小:', original.size)
    print("选取裁剪的四个方位点")
    picture_size = list(original.size)
    # 报错函数
    def error_report():
        print(
            "Sorry, the parameters must meet the following conditions:"
            "Value_3 must be GREATER than value_1.Value_4 must be GREATER than value_2."
            "Besides,tile CAN NOT extend outside image.Please enter an appropriate value again.")

    # 执行函数
    def execution_fun(val):
        values.append(val)

    order = 1
    values = []
    while order <= 4:
        value = int(float(input("Please enter the positive integer value_{order}:")))
        if (order % 2) != 0:
            parameter = 0
        else:
            parameter = 1
        if order <= 2:
            if 0 <= value < picture_size[parameter]:
                execution_fun(value)
                order += 1
            else:
                error_report()
        else:
            if 0 < value <= picture_size[parameter] and value > values[parameter]:
                execution_fun(value)
                order += 1
            else:
                error_report()

    values = tuple(values)
    print(values)
    # 剪裁
    img_crop = original.crop(values)
    img_crop.show()
    global save_image
    save_image = img_crop
    global render
    render = ImageTk.PhotoImage(img_crop)
    resultshow()
#尺寸
def size():
    heigh=int(input("变换后的高为(像素):"))
    wide=int(input("变换后的宽为(像素):"))
    im = original
    new_im = im.resize((wide, heigh))
    new_im.show()
    global save_image
    save_image = new_im
    global render
    render = ImageTk.PhotoImage(new_im)
    resultshow()

original = Image.new('RGB', (500, 500))
final = Image.new('RGB', (500, 500))
count = 0
saveroute = 'D:\\'

#创建一个图形化界面窗口
root = tkinter.Tk()
root.title("图像处理")         #设置界面标题
root.geometry("800x600")       #设置界面大小：800*600
img2 = tkinter.Label(root)
#说明标签
expl = tkinter.Label(root,text="请选择图片,处理后点击保存,图片将保存在D:\\testx.jpg\n" ).pack()
#保存图片按钮
savebutton = tkinter.Button(root,text="保存图片", command = save)
savebutton.place(x=380,y=60)
#选择图片按钮
selectbutton = tkinter.Button(root, text ="选择图片", command = select)
selectbutton.place(x=380,y=100)
#亮度按钮
brightnessbutton = tkinter.Button(root,text="亮度", command = bright)
brightnessbutton.place(x=380,y=140)
#对比度按钮
contrastbutton = tkinter.Button(root,text="对比度",command= contrast)
contrastbutton.place(x=380,y=180)
#旋转按钮
rotationbutton = tkinter.Button(root,text="旋转",command= rotation)
rotationbutton.place(x=380,y=220)
#裁剪按钮
cutbutton = tkinter.Button(root,text="裁剪",command = cut )
cutbutton.place(x=380,y=260)
#放大缩小按钮
sizebutton = tkinter.Button(root,text="尺寸",command = size )
sizebutton.place(x=380,y=300)
#显示原图像和修改后的图像的标签
orig = tkinter.Label(root,text='原图像(150x200)')
orig.place(x=190,y=100)
result = tkinter.Label(root,text='处理结果')
result.place(x=570,y=100)
root.mainloop()
